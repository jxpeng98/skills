#!/usr/bin/env python3
"""Build release archives for every plugin in plugins/."""

from __future__ import annotations

import argparse
import hashlib
import tarfile
import zipfile
from pathlib import Path


EXCLUDE_DIRS = {".git", "__pycache__"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plugins-root", default="plugins")
    parser.add_argument("--output", default="dist")
    args = parser.parse_args()

    plugins_root = Path(args.plugins_root)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    plugin_dirs = sorted(path for path in plugins_root.iterdir() if path.is_dir())
    checksums: list[tuple[str, str]] = []

    for plugin_dir in plugin_dirs:
        zip_path = output / f"{plugin_dir.name}.zip"
        tar_path = output / f"{plugin_dir.name}.tar.gz"
        write_zip(zip_path, [plugin_dir], plugins_root)
        write_tar(tar_path, [plugin_dir], plugins_root)
        checksums.append((sha256(zip_path), zip_path.name))
        checksums.append((sha256(tar_path), tar_path.name))

    all_zip = output / "all-plugins.zip"
    write_zip(all_zip, plugin_dirs, plugins_root)
    checksums.append((sha256(all_zip), all_zip.name))

    (output / "checksums.txt").write_text(
        "\n".join(f"{digest}  {name}" for digest, name in checksums) + "\n",
        encoding="utf-8",
    )
    print(f"Packaged {len(plugin_dirs)} plugins into {output}")


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def write_zip(path: Path, plugin_dirs: list[Path], archive_root: Path) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for plugin_dir in plugin_dirs:
            for file_path in iter_files(plugin_dir):
                archive.write(file_path, file_path.relative_to(archive_root).as_posix())


def write_tar(path: Path, plugin_dirs: list[Path], archive_root: Path) -> None:
    with tarfile.open(path, "w:gz") as archive:
        for plugin_dir in plugin_dirs:
            for file_path in iter_files(plugin_dir):
                archive.add(file_path, arcname=file_path.relative_to(archive_root).as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


if __name__ == "__main__":
    main()
