from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_plugins import (
    validate_hermes_tap,
    validate_skill_routing_cases,
    validate_synchronized_plugin_versions,
)


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
    def test_behavior_cases_require_available_routes_and_observable_checks(self) -> None:
        skills = {"summarize-material": Path("unused")}
        case = {
            "available_skills": ["summarize-material"],
            "expected_skill": "summarize-material",
            "prompt": "Summarize these notes.",
            "checks": ["Preserve uncertain decisions as uncertain."],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "skill-routing.json"
            for changes, expected_error in (
                ({}, None),
                ({"expected_skill": "meeting-synthesizer"}, "expected_skill"),
                ({"available_skills": ["missing-skill"]}, "available_skills"),
                ({"available_skills": [{}]}, "available_skills"),
                ({"prompt": " "}, "prompt"),
                ({"checks": [""]}, "checks"),
            ):
                with self.subTest(changes=changes):
                    path.write_text(json.dumps({
                        "skills": {"summarize-material": {
                            "direct": "Summarize these notes.",
                            "paraphrase": "Condense the record.",
                            "adjacent_negative": "Rewrite this email.",
                        }},
                        "scenarios": {"isolated-install": {**case, **changes}},
                    }), encoding="utf-8")
                    errors: list[str] = []
                    validate_skill_routing_cases(path, skills, errors)
                    if expected_error is None:
                        self.assertEqual(errors, [])
                    else:
                        self.assertEqual(len(errors), 1)
                        self.assertIn(expected_error, errors[0])

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


class PluginVersionValidationTests(unittest.TestCase):
    def test_rejects_cross_plugin_version_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, version in (("dev-tools", "0.6.1"), ("writing-tools", "0.5.0")):
                path = root / name / ".codex-plugin" / "plugin.json"
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps({"version": version}), encoding="utf-8")

            errors: list[str] = []
            validate_synchronized_plugin_versions(root, errors)

            self.assertEqual(
                errors,
                [
                    "plugin versions must be synchronized: "
                    "dev-tools=0.6.1, writing-tools=0.5.0"
                ],
            )


if __name__ == "__main__":
    unittest.main()
