from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FacultyToolsTests(unittest.TestCase):
    def test_faculty_tools_plugin_has_codex_ready_daily_skill_set(self) -> None:
        plugin = ROOT / "plugins" / "faculty-tools"
        expected_skills = {
            "course-planner",
            "assignment-brief",
            "feedback-writer",
            "faculty-email",
            "meeting-synthesizer",
            "statement-drafter",
        }

        self.assertTrue((plugin / ".codex-plugin" / "plugin.json").is_file())
        self.assertTrue((plugin / ".claude-plugin" / "plugin.json").is_file())
        self.assertTrue((plugin / "plugin.json").is_file())
        self.assertTrue((plugin / "skillsplace.json").is_file())

        skill_names = {
            path.name
            for path in (plugin / "skills").iterdir()
            if path.is_dir()
        }
        self.assertEqual(skill_names, expected_skills)

        for skill_name in sorted(expected_skills):
            skill_md = plugin / "skills" / skill_name / "SKILL.md"
            text = skill_md.read_text(encoding="utf-8")
            self.assertRegex(text, rf"^---\nname: {re.escape(skill_name)}\n")
            self.assertIn('description: "', text)
            self.assertNotIn("description: Use when", text)
            self.assertIn("## Outcome", text)
            self.assertIn("## Inputs And Defaults", text)
            self.assertIn("## Workflow", text)
            self.assertIn("## Output", text)
            self.assertIn("## Completion Check", text)
            self.assertTrue((skill_md.parent / "agents" / "openai.yaml").is_file())

    def test_humanizer_supports_coach_and_polisher_modes_for_university_writing(self) -> None:
        text = (
            ROOT
            / "plugins"
            / "writing-tools"
            / "skills"
            / "humanizer"
            / "SKILL.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "Coach Mode",
            "Polisher Mode",
            "essay",
            "report",
            "assessed academic work",
            "detector evasion",
            "protected-content ledger",
            "desired result",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_humanizer_uses_progressive_disclosure(self) -> None:
        skill = (
            ROOT / "plugins" / "writing-tools" / "skills" / "humanizer"
        )
        text = (
            skill / "SKILL.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "## Inputs And Defaults",
            "## Completion Check",
            "light",
            "standard",
            "deep",
            "references/academic-editing.md",
            "references/style-diagnostics.md",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        self.assertLess(len(text.splitlines()), 140)
        self.assertTrue((skill / "references" / "academic-editing.md").is_file())
        self.assertTrue((skill / "references" / "style-diagnostics.md").is_file())

    def test_humanizer_academic_reference_has_section_aware_checks(self) -> None:
        text = (
            ROOT
            / "plugins"
            / "writing-tools"
            / "skills"
            / "humanizer"
            / "references"
            / "academic-editing.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "## Section Checks",
            "Introduction",
            "Body paragraph",
            "Methods",
            "Results or findings",
            "Conclusion",
            "claim-evidence fit",
            "author decisions",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_writing_tools_version_bumped_for_codex_optimization(self) -> None:
        paths = [
            ROOT / "plugins" / "writing-tools" / ".codex-plugin" / "plugin.json",
            ROOT / "plugins" / "writing-tools" / ".claude-plugin" / "plugin.json",
            ROOT / "plugins" / "writing-tools" / "skillsplace.json",
        ]

        for path in paths:
            with self.subTest(path=path.as_posix()):
                self.assertIn('"version": "0.2.0"', path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
