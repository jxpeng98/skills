from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_plugins import validate_hermes_tap, validate_skill_routing_cases


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


class SkillRoutingValidationTests(unittest.TestCase):
    def test_rejects_a_skill_without_all_routing_cases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skill-routing.json"
            path.write_text(
                json.dumps(
                    {
                        "skills": {
                            "commit-message": {
                                "direct": "Write a commit message.",
                                "paraphrase": "Name this change.",
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )

            errors: list[str] = []
            validate_skill_routing_cases(
                path,
                {"commit-message": Path("plugins/productivity/skills/commit-message")},
                errors,
            )

            self.assertIn(
                f"{path} routing cases for commit-message are missing: adjacent_negative",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
