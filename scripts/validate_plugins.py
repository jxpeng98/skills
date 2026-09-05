#!/usr/bin/env python3
"""Validate this repository's plugin layout without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
NAME_RE = re.compile(r"^[a-z0-9-]+$")
DISALLOWED_PLUGIN_NAMES = {"research-tools"}
EXCLUDE_DIRS = {"__pycache__"}
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}
ROUTING_CASE_FIELDS = {"direct", "paraphrase", "adjacent_negative"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plugins-root", default="plugins")
    args = parser.parse_args()

    root = Path(args.plugins_root)
    errors: list[str] = []

    if not root.is_dir():
        errors.append("missing plugins/ directory")
    else:
        for plugin_dir in sorted(path for path in root.iterdir() if path.is_dir()):
            validate_plugin(plugin_dir, errors)
        validate_synchronized_plugin_versions(root, errors)
        skills = collect_plugin_skills(Path("."), root, errors)
        validate_hermes_tap(Path("."), root, errors, skills)
        validate_skill_routing_cases(Path("evals/skill-routing.json"), skills, errors)

    validate_repository_boundaries(Path("."), errors)

    if errors:
        print("Plugin validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Plugin validation passed")


def validate_plugin(plugin_dir: Path, errors: list[str]) -> None:
    name = plugin_dir.name
    if name in DISALLOWED_PLUGIN_NAMES:
        errors.append(f"disallowed plugin remains: {name}")
    if NAME_RE.fullmatch(name) is None:
        errors.append(f"plugin name must be kebab-case: {name}")

    codex = load_json(plugin_dir / ".codex-plugin" / "plugin.json", errors)
    claude = load_json(plugin_dir / ".claude-plugin" / "plugin.json", errors)
    antigravity = load_json(plugin_dir / "plugin.json", errors)
    skillsplace = load_json(plugin_dir / "skillsplace.json", errors)

    if codex is not None:
        validate_common_manifest(codex, name, plugin_dir / ".codex-plugin" / "plugin.json", errors)
        if codex.get("skills") != "./skills/":
            errors.append(f"{plugin_dir}/.codex-plugin/plugin.json must set skills to ./skills/")

    if claude is not None:
        validate_common_manifest(claude, name, plugin_dir / ".claude-plugin" / "plugin.json", errors)

    if antigravity is not None and antigravity.get("name") != name:
        errors.append(f"{plugin_dir}/plugin.json name must match directory name")

    versions = {
        payload.get("version")
        for payload in (codex, claude, skillsplace)
        if payload is not None and isinstance(payload.get("version"), str)
    }
    if len(versions) > 1:
        errors.append(
            f"{plugin_dir} versions must match across Codex, Claude, and skillsplace manifests"
        )

    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        errors.append(f"{plugin_dir} is missing skills/")
        return

    skill_dirs = [path for path in sorted(skills_dir.iterdir()) if path.is_dir()]
    if not skill_dirs:
        errors.append(f"{plugin_dir}/skills has no skills")
    for skill_dir in skill_dirs:
        validate_skill(skill_dir, errors)


def validate_common_manifest(
    payload: dict[str, object],
    expected_name: str,
    path: Path,
    errors: list[str],
) -> None:
    if payload.get("name") != expected_name:
        errors.append(f"{path} name must match plugin directory")
    description = payload.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path} must include a non-empty description")
    version = payload.get("version")
    if not isinstance(version, str) or SEMVER_RE.fullmatch(version) is None:
        errors.append(f"{path} must include strict semver version")


def validate_synchronized_plugin_versions(
    plugins_root: Path,
    errors: list[str],
) -> None:
    """Require one version across all bundled plugins."""

    versions: dict[str, str] = {}
    for plugin_dir in sorted(path for path in plugins_root.iterdir() if path.is_dir()):
        path = plugin_dir / ".codex-plugin" / "plugin.json"
        if not path.is_file():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        version = payload.get("version") if isinstance(payload, dict) else None
        if isinstance(version, str) and SEMVER_RE.fullmatch(version):
            versions[plugin_dir.name] = version

    if len(set(versions.values())) > 1:
        summary = ", ".join(f"{name}={version}" for name, version in versions.items())
        errors.append(f"plugin versions must be synchronized: {summary}")


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{skill_dir} is missing SKILL.md")
        return

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        errors.append(f"{skill_md} must start with YAML frontmatter")
        return

    unexpected_keys = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    missing_keys = ALLOWED_FRONTMATTER_KEYS - set(frontmatter)
    if unexpected_keys:
        keys = ", ".join(sorted(unexpected_keys))
        errors.append(f"{skill_md} has unsupported frontmatter keys: {keys}")
    if missing_keys:
        keys = ", ".join(sorted(missing_keys))
        errors.append(f"{skill_md} is missing frontmatter keys: {keys}")

    name = frontmatter.get("name")
    if name != skill_dir.name:
        errors.append(f"{skill_md} frontmatter name must match directory name")
    if not isinstance(name, str) or NAME_RE.fullmatch(name) is None:
        errors.append(f"{skill_md} name must be lowercase kebab-case")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_md} must include a non-empty description")

    validate_openai_yaml(skill_dir, name if isinstance(name, str) else skill_dir.name, errors)
    validate_references(skill_dir, text, errors)


def validate_openai_yaml(
    skill_dir: Path,
    skill_name: str,
    errors: list[str],
) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        errors.append(f"{skill_dir} is missing agents/openai.yaml")
        return

    text = path.read_text(encoding="utf-8")
    if not text.startswith("interface:\n"):
        errors.append(f"{path} must start with an interface mapping")

    values: dict[str, str] = {}
    for key in ("display_name", "short_description", "default_prompt"):
        pattern = re.compile(
            rf'^  {re.escape(key)}:\s*("(?:[^"\\]|\\.)*")\s*$',
            re.MULTILINE,
        )
        match = pattern.search(text)
        if match is None:
            errors.append(f"{path} must include a quoted interface.{key}")
            continue
        try:
            value = json.loads(match.group(1))
        except json.JSONDecodeError:
            errors.append(f"{path} interface.{key} must be a valid quoted string")
            continue
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path} interface.{key} must be non-empty")
            continue
        values[key] = value

    short_description = values.get("short_description")
    if short_description is not None and not 25 <= len(short_description) <= 64:
        errors.append(
            f"{path} interface.short_description must be 25-64 characters "
            f"(got {len(short_description)})"
        )

    default_prompt = values.get("default_prompt")
    if default_prompt is not None and f"${skill_name}" not in default_prompt:
        errors.append(
            f"{path} interface.default_prompt must explicitly mention ${skill_name}"
        )


def validate_references(skill_dir: Path, skill_text: str, errors: list[str]) -> None:
    referenced = set(
        re.findall(r"`(references/[A-Za-z0-9._/-]+\.md)`", skill_text)
    )
    for relative in sorted(referenced):
        path = skill_dir / relative
        if not path.is_file():
            errors.append(f"{skill_dir}/SKILL.md references missing {relative}")

    references_dir = skill_dir / "references"
    if references_dir.is_dir():
        for path in sorted(references_dir.rglob("*.md")):
            relative = path.relative_to(skill_dir).as_posix()
            if relative not in referenced:
                errors.append(f"{path} is not routed from SKILL.md")


def validate_hermes_tap(
    root: Path,
    plugins_root: Path,
    errors: list[str],
    skills: dict[str, Path] | None = None,
) -> None:
    """Validate the top-level skills/ mirror consumed by Hermes taps."""

    if skills is None:
        skills = collect_plugin_skills(root, plugins_root, errors)
    hermes_root = root / "skills"

    if not hermes_root.is_dir():
        errors.append("missing skills/ directory for Hermes tap")

    for name, source_dir in sorted(skills.items()):
        mirror_dir = hermes_root / name
        if not mirror_dir.is_dir():
            errors.append(f"skills/{name} is missing for Hermes tap")
            continue
        if not directories_match(source_dir, mirror_dir):
            errors.append(
                f"skills/{name} does not match {relative_path(source_dir, root)}"
            )

    if hermes_root.is_dir():
        for mirror_dir in sorted(path for path in hermes_root.iterdir() if path.is_dir()):
            if mirror_dir.name not in skills:
                errors.append(f"skills/{mirror_dir.name} has no matching plugin skill")


def validate_skill_routing_cases(
    path: Path,
    skills: dict[str, Path],
    errors: list[str],
) -> None:
    """Ensure every distributable skill has a small routing prompt set."""

    payload = load_json(path, errors)
    if payload is None:
        return
    cases = payload.get("skills")
    if not isinstance(cases, dict):
        errors.append(f"{path} must contain a skills object")
        return

    expected = set(skills)
    actual = set(cases)
    for name in sorted(expected - actual):
        errors.append(f"{path} is missing routing cases for {name}")
    for name in sorted(actual - expected):
        errors.append(f"{path} has routing cases for unknown skill {name}")

    for name, prompts in sorted(cases.items()):
        if not isinstance(prompts, dict):
            errors.append(f"{path} routing cases for {name} must be an object")
            continue
        missing = ROUTING_CASE_FIELDS - set(prompts)
        extra = set(prompts) - ROUTING_CASE_FIELDS
        if missing:
            errors.append(
                f"{path} routing cases for {name} are missing: "
                + ", ".join(sorted(missing))
            )
        if extra:
            errors.append(
                f"{path} routing cases for {name} have unknown fields: "
                + ", ".join(sorted(extra))
            )
        for field in sorted(ROUTING_CASE_FIELDS & set(prompts)):
            prompt = prompts[field]
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append(f"{path} {name}.{field} must be a non-empty string")

    # These checks validate fixtures, not a model's routing or generated prose.
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, dict) or not scenarios:
        errors.append(f"{path} must contain non-empty behavioral scenarios")
        return
    for name, case in sorted(scenarios.items()):
        label = f"{path} scenario {name}"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue
        available = case.get("available_skills")
        if (
            not isinstance(available, list)
            or not available
            or any(not isinstance(skill, str) or skill not in skills for skill in available)
        ):
            errors.append(f"{label} available_skills must list known skills")
        elif case.get("expected_skill") not in available:
            errors.append(f"{label} expected_skill must be available in this scenario")
        prompt = case.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{label} prompt must be a non-empty string")
        checks = case.get("checks")
        if (
            not isinstance(checks, list)
            or not checks
            or any(not isinstance(check, str) or not check.strip() for check in checks)
        ):
            errors.append(f"{label} checks must list observable behavior")


def collect_plugin_skills(
    root: Path,
    plugins_root: Path,
    errors: list[str],
) -> dict[str, Path]:
    skills: dict[str, Path] = {}
    for skill_dir in sorted(plugins_root.glob("*/skills/*")):
        if not skill_dir.is_dir():
            continue
        existing = skills.get(skill_dir.name)
        if existing is not None:
            errors.append(
                "duplicate skill name for Hermes tap: "
                f"{skill_dir.name} in {relative_path(existing, root)} and "
                f"{relative_path(skill_dir, root)}"
            )
            continue
        skills[skill_dir.name] = skill_dir
    return skills


def directories_match(left: Path, right: Path) -> bool:
    left_files = set(iter_relative_files(left))
    right_files = set(iter_relative_files(right))
    if left_files != right_files:
        return False
    return all(
        (left / path).read_bytes() == (right / path).read_bytes()
        for path in left_files
    )


def iter_relative_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path.relative_to(root))
    return sorted(files)


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def load_json(path: Path, errors: list[str]) -> dict[str, object] | None:
    if not path.is_file():
        errors.append(f"missing {path}")
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{path} is invalid JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"{path} must contain a JSON object")
        return None
    return payload


def validate_repository_boundaries(root: Path, errors: list[str]) -> None:
    forbidden = {
        ".agents/plugins/marketplace.json",
        ".claude-plugin/marketplace.json",
        "marketplace.json",
    }
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        normalized = path.as_posix().lstrip("./")
        if normalized in forbidden or normalized.endswith("/marketplace.json"):
            errors.append(f"marketplace catalog file belongs in skillsplace: {normalized}")


if __name__ == "__main__":
    main()
