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

    if codex is not None:
        validate_common_manifest(codex, name, plugin_dir / ".codex-plugin" / "plugin.json", errors)
        if codex.get("skills") != "./skills/":
            errors.append(f"{plugin_dir}/.codex-plugin/plugin.json must set skills to ./skills/")

    if claude is not None:
        validate_common_manifest(claude, name, plugin_dir / ".claude-plugin" / "plugin.json", errors)

    if antigravity is not None and antigravity.get("name") != name:
        errors.append(f"{plugin_dir}/plugin.json name must match directory name")

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

    name = frontmatter.get("name")
    if name != skill_dir.name:
        errors.append(f"{skill_md} frontmatter name must match directory name")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.startswith("Use when"):
        errors.append(f"{skill_md} description must start with 'Use when'")


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
