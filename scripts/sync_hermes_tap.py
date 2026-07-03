#!/usr/bin/env python3
"""Sync the top-level skills/ directory used by Hermes taps."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


EXCLUDE_DIRS = {"__pycache__"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plugins-root", default="plugins")
    parser.add_argument("--skills-root", default="skills")
    parser.add_argument(
        "--check",
        action="store_true",
        help="check that skills/ matches plugin skills without writing files",
    )
    args = parser.parse_args()

    plugins_root = Path(args.plugins_root)
    skills_root = Path(args.skills_root)
    plugin_skills = collect_plugin_skills(plugins_root)

    if args.check:
        errors = check_mirror(plugin_skills, skills_root)
        if errors:
            print("Hermes tap sync check failed:")
            for error in errors:
                print(f"- {error}")
            raise SystemExit(1)
        print("Hermes tap sync check passed")
        return

    rebuild_mirror(plugin_skills, skills_root)
    print(f"Synced {len(plugin_skills)} skills into {skills_root}")


def collect_plugin_skills(plugins_root: Path) -> dict[str, Path]:
    if not plugins_root.is_dir():
        raise SystemExit(f"missing plugins root: {plugins_root}")

    skills: dict[str, Path] = {}
    duplicates: list[str] = []
    for skill_dir in sorted(plugins_root.glob("*/skills/*")):
        if not skill_dir.is_dir():
            continue
        if skill_dir.name in skills:
            duplicates.append(skill_dir.name)
            continue
        skills[skill_dir.name] = skill_dir

    if duplicates:
        names = ", ".join(sorted(set(duplicates)))
        raise SystemExit(f"duplicate skill names cannot be mirrored for Hermes: {names}")
    return skills


def check_mirror(plugin_skills: dict[str, Path], skills_root: Path) -> list[str]:
    errors: list[str] = []
    if not skills_root.is_dir():
        errors.append("missing skills/ directory")
        return errors

    for name, source_dir in sorted(plugin_skills.items()):
        mirror_dir = skills_root / name
        if not mirror_dir.is_dir():
            errors.append(f"missing skills/{name}")
        elif not directories_match(source_dir, mirror_dir):
            errors.append(f"skills/{name} does not match {source_dir}")

    for mirror_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        if mirror_dir.name not in plugin_skills:
            errors.append(f"skills/{mirror_dir.name} has no matching plugin skill")

    return errors


def rebuild_mirror(plugin_skills: dict[str, Path], skills_root: Path) -> None:
    tmp_root = skills_root.with_name(f".{skills_root.name}.tmp")
    if tmp_root.exists():
        shutil.rmtree(tmp_root)
    tmp_root.mkdir(parents=True)

    for name, source_dir in sorted(plugin_skills.items()):
        shutil.copytree(
            source_dir,
            tmp_root / name,
            ignore=shutil.ignore_patterns(*EXCLUDE_DIRS),
        )

    if skills_root.exists():
        shutil.rmtree(skills_root)
    tmp_root.replace(skills_root)


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


if __name__ == "__main__":
    main()
