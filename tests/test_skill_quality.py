from __future__ import annotations

import unittest
from pathlib import Path

from scripts.validate_plugins import parse_frontmatter, validate_skill


ROOT = Path(__file__).resolve().parents[1]


class SkillQualityTests(unittest.TestCase):
    def canonical_skills(self) -> list[Path]:
        return sorted(ROOT.glob("plugins/*/skills/*"))

    def test_all_canonical_skills_pass_quality_contract(self) -> None:
        for skill_dir in self.canonical_skills():
            with self.subTest(skill=skill_dir.name):
                errors: list[str] = []
                validate_skill(skill_dir, errors)
                self.assertEqual(errors, [])

    def test_skill_discovery_metadata_fits_codex_budget(self) -> None:
        descriptors: list[str] = []
        for skill_dir in self.canonical_skills():
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            frontmatter = parse_frontmatter(text)
            self.assertIsNotNone(frontmatter)
            assert frontmatter is not None
            name = frontmatter["name"]
            description = frontmatter["description"]
            self.assertFalse(description.startswith("Use when"))
            descriptors.append(f"{name}: {description}")

        self.assertLess(sum(map(len, descriptors)), 8_000)

    def test_every_skill_has_explicit_outcome_and_stop_bar(self) -> None:
        for skill_dir in self.canonical_skills():
            with self.subTest(skill=skill_dir.name):
                text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("## Outcome", text)
                self.assertIn("## Completion Check", text)


if __name__ == "__main__":
    unittest.main()
