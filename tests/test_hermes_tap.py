from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_plugins import validate_hermes_tap


class HermesTapValidationTests(unittest.TestCase):
    def test_accepts_matching_top_level_skill_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plugins" / "productivity" / "skills" / "commit-message"
            mirror = root / "skills" / "commit-message"
            source.mkdir(parents=True)
            mirror.mkdir(parents=True)
            skill_md = "---\nname: commit-message\ndescription: Use when writing commits.\n---\n"
            (source / "SKILL.md").write_text(skill_md, encoding="utf-8")
            (mirror / "SKILL.md").write_text(skill_md, encoding="utf-8")

            errors: list[str] = []
            validate_hermes_tap(root, root / "plugins", errors)

            self.assertEqual(errors, [])

    def test_rejects_missing_top_level_skill_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plugins" / "productivity" / "skills" / "commit-message"
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text(
                "---\nname: commit-message\ndescription: Use when writing commits.\n---\n",
                encoding="utf-8",
            )

            errors: list[str] = []
            validate_hermes_tap(root, root / "plugins", errors)

            self.assertIn("skills/commit-message is missing for Hermes tap", errors)

    def test_rejects_mismatched_top_level_skill_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "plugins" / "productivity" / "skills" / "commit-message"
            mirror = root / "skills" / "commit-message"
            source.mkdir(parents=True)
            mirror.mkdir(parents=True)
            (source / "SKILL.md").write_text(
                "---\nname: commit-message\ndescription: Use when writing commits.\n---\n",
                encoding="utf-8",
            )
            (mirror / "SKILL.md").write_text(
                "---\nname: commit-message\ndescription: Use when editing commits.\n---\n",
                encoding="utf-8",
            )

            errors: list[str] = []
            validate_hermes_tap(root, root / "plugins", errors)

            self.assertIn(
                "skills/commit-message does not match plugins/productivity/skills/commit-message",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
