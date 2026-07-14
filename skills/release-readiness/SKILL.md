---
name: release-readiness
description: "Assess a skill, plugin, repository change, or marketplace update for release, publication, installation testing, or reviewer handoff using fresh validation evidence. Trigger for readiness checks and release gates; report blockers without publishing, tagging, or pushing unless explicitly asked."
---

# Release Readiness

## Outcome

Verify that a skill or plugin is ready to publish or hand off without relying on assumptions.

## Workflow

1. Read repository release guidance and identify the exact artifact, intended
   release surface, changed files, and applicable version.
2. Inspect before mutating. Run the cheapest targeted checks first; run
   independent checks in parallel when safe, then run broader packaging or
   installation checks only when they add confidence.
3. Classify findings as blockers, warnings, or residual risks. A missing check is
   not a pass.
4. Re-read the final diff and status so generated files, mirrors, version bumps,
   or unrelated changes are not missed.

## Checks

Run or request evidence for:

- Clean intended file layout under `plugins/<plugin-name>/skills/<skill-name>/`
- Synced Hermes tap mirror under repository-level `skills/<skill-name>/`
- Valid `.codex-plugin/plugin.json` for installable plugins
- `SKILL.md` frontmatter with `name` and a concise, trigger-front-loaded
  `description`
- `SKILL.md` with an explicit outcome and completion check
- `agents/openai.yaml` with current display metadata and a default prompt that
  explicitly invokes the skill
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

## Completion Check

- Every applicable release gate has fresh evidence or is explicitly marked not
  run with a reason.
- Versions, manifests, mirrors, packaged contents, and documented install paths
  agree.
- `Ready` is used only when no blocker remains. Do not publish, tag, push, or
  create a release unless the user explicitly requests that action.
