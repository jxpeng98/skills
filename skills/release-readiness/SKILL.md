---
name: release-readiness
description: Use when preparing a skill, plugin, repository change, or marketplace update for release, publication, installation testing, or handoff to reviewers.
---

# Release Readiness

## Purpose

Verify that a skill or plugin is ready to publish or hand off without relying on assumptions.

## Checks

Run or request evidence for:

- Clean intended file layout under `plugins/<plugin-name>/skills/<skill-name>/`
- Synced Hermes tap mirror under repository-level `skills/<skill-name>/`
- Valid `.codex-plugin/plugin.json` for installable plugins
- `SKILL.md` frontmatter with `name` and trigger-focused `description`
- No leftover placeholders, TODO markers, secrets, or local paths
- References, scripts, and assets included only when directly used
- Relevant validation commands and their fresh output
- `python scripts/sync_hermes_tap.py --check` when plugin skills changed
- Marketplace metadata updated only in the marketplace repository
- Git status showing only intended changes

## Output

Use this structure:

```markdown
Status: Ready | Not ready

Blocking issues:
- <issue or "None">

Validation run:
- <command>: <result>

Remaining risks:
- <risk>

Recommended next step:
- <action>
```
