from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FacultyToolsTests(unittest.TestCase):
    def test_faculty_tools_plugin_has_concrete_daily_skill_set(self) -> None:
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
            self.assertIn("description: Use when", text)
            self.assertIn("## Workflow", text)
            self.assertIn("## Output", text)
            self.assertIn("grill-me", text)
            self.assertIn("goal", text.lower())
            self.assertIn("desired result", text.lower())

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
            "academic integrity",
            "not to make the text sound like a native speaker",
            "grill-me",
            "desired result",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_humanizer_has_general_and_academic_directions(self) -> None:
        text = (
            ROOT
            / "plugins"
            / "writing-tools"
            / "skills"
            / "humanizer"
            / "SKILL.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "General Writing Direction",
            "Academic Writing Direction",
            "Direction Selection",
            "General + Coach",
            "General + Polisher",
            "Academic + Coach",
            "Academic + Polisher",
            "audience and channel",
            "argument, evidence, structure, and academic register",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_humanizer_has_preflight_diagnosis_and_audit_contract(self) -> None:
        text = (
            ROOT
            / "plugins"
            / "writing-tools"
            / "skills"
            / "humanizer"
            / "SKILL.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "## Preflight Diagnosis",
            "## AI-Feel Diagnosis",
            "## Protected Facts",
            "## Edit Intensity",
            "## Post-Edit Audit",
            "light",
            "standard",
            "deep",
            "process bleed",
            "clean but empty",
            "No detector-evasion objective",
            "What was preserved",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_humanizer_has_section_aware_academic_checks(self) -> None:
        text = (
            ROOT
            / "plugins"
            / "writing-tools"
            / "skills"
            / "humanizer"
            / "SKILL.md"
        ).read_text(encoding="utf-8")

        required_phrases = [
            "## Section-Aware Academic Checks",
            "Introduction",
            "Body Paragraph",
            "Report Methods",
            "Results or Findings",
            "Conclusion",
            "claim-evidence fit",
            "author decision needed",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_writing_tools_version_bumped_for_humanizer_contract(self) -> None:
        paths = [
            ROOT / "plugins" / "writing-tools" / ".codex-plugin" / "plugin.json",
            ROOT / "plugins" / "writing-tools" / ".claude-plugin" / "plugin.json",
            ROOT / "plugins" / "writing-tools" / "skillsplace.json",
        ]

        for path in paths:
            with self.subTest(path=path.as_posix()):
                self.assertIn('"version": "0.1.4"', path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
