# Skills

This repository contains reusable agent skills for daily development,
engineering projects, writing, productivity, and technical presentations.

It is the source repository for installable skill plugins. Marketplace catalog
metadata belongs in `jxpeng98/skillsplace`, not in this repository.

This repository may include teaching, faculty-service, student-support, and
university-writing helpers. It intentionally does not include academic research
workflows, literature reviews, citation workflows, thesis planning, or
paper-planning skills.

## Repository Layout

```text
.
├── DEVELOPMENT.md
├── skills/                    # Hermes tap mirror, generated from plugins/*/skills
└── plugins/
    ├── dev-tools/
    ├── faculty-tools/
    ├── presentation-tools/
    ├── productivity/
    └── writing-tools/
```

Each plugin is an installable unit. Each skill is a behavior unit under:

```text
plugins/<plugin-name>/skills/<skill-name>/SKILL.md
```

The top-level `skills/` directory is a Hermes tap compatibility mirror generated
from those plugin skill directories. Edit the canonical skill under `plugins/`,
then run:

```bash
python scripts/sync_hermes_tap.py
```

Each plugin includes platform markers for the current target platforms:

```text
plugins/<plugin-name>/
├── .codex-plugin/plugin.json      # Codex plugin manifest
├── .claude-plugin/plugin.json     # Claude Code plugin manifest
├── plugin.json                    # Antigravity plugin marker
└── skills/
```

See [DEVELOPMENT.md](DEVELOPMENT.md) for repository boundaries, plugin layout,
and marketplace publishing guidance.

## Plugins

### `productivity`

Productivity skills for planning, critique, decisions, commits, and PR work.

| Skill | Use When |
| --- | --- |
| `grill-me` | Stress-test a plan, design, argument, product idea, discovery direction, or implementation strategy. |
| `decide-between-options` | Compare approaches, tools, architectures, vendors, workflows, or plans and choose one. |
| `commit-message` | Turn staged or unstaged changes into a Conventional Commit message. |
| `pr-description` | Write a reviewer-ready pull request or merge request description from actual changes. |

### `dev-tools`

Developer skills for repository hygiene, plugin boundaries, and release
readiness.

| Skill | Use When |
| --- | --- |
| `repo-boundary-review` | Check whether changed files belong in this skills repo, a plugin, a draft area, or a marketplace catalog. |
| `release-readiness` | Verify a skill, plugin, repository change, or marketplace update before publication or handoff. |

### `faculty-tools`

Daily university faculty skills for teaching, feedback, student communication,
meetings, and light academic-service writing.

| Skill | Use When |
| --- | --- |
| `course-planner` | Plan courses, weekly classes, seminars, tutorials, reading sessions, or classroom activities. |
| `assignment-brief` | Create assignment prompts, essay or report briefs, submission requirements, and rubrics. |
| `feedback-writer` | Write constructive feedback on student essays, reports, assignments, drafts, presentations, or projects. |
| `faculty-email` | Draft emails to students, colleagues, administrators, committees, or teaching teams. |
| `meeting-synthesizer` | Summarize university meetings, committee notes, department discussions, and action items. |
| `statement-drafter` | Draft or improve teaching statements, service statements, grant-support text, award nominations, bios, or review narratives. |

### `writing-tools`

Writing skills for clarity, tone, humanization, summarization, and reusable text
transformation.

| Skill | Use When |
| --- | --- |
| `humanizer` | Coach or polish general writing and academic writing, including essay/report improvement with academic integrity boundaries. |
| `rewrite-for-clarity` | Rewrite, edit, tighten, or adapt text while preserving meaning. |
| `summarize-material` | Summarize notes, articles, transcripts, documents, meetings, or long context into useful decisions and actions. |

### `presentation-tools`

Presentation skills for Slidev-based engineering and project slides.

| Skill | Use When |
| --- | --- |
| `slidev-slides` | Create, edit, review, present, build, or export Markdown-based Slidev decks. |

## Development

Sync the Hermes tap mirror after changing plugin skills:

```bash
python scripts/sync_hermes_tap.py
```

Check that the mirror is current:

```bash
python scripts/sync_hermes_tap.py --check
```

Validate plugin manifests and skill frontmatter after changes:

```bash
python scripts/validate_plugins.py
```

Check Markdown and whitespace before committing:

```bash
git diff --check
```

Build local release archives:

```bash
python scripts/package_plugins.py --output dist
```

## Installation And Releases

Marketplace metadata should live in `jxpeng98/skillsplace` and point to plugin
subdirectories in this repository with `git-subdir` sources, for example:

```text
plugins/productivity
plugins/dev-tools
plugins/faculty-tools
plugins/writing-tools
plugins/presentation-tools
```

GitHub release packages are built by `.github/workflows/release.yml` on tags
matching `v*` or by manual `workflow_dispatch`. The workflow validates all
plugins, creates per-plugin `.zip` and `.tar.gz` archives, creates
`all-plugins.zip`, and uploads `checksums.txt`.

Platform support:

- Codex: reads `.codex-plugin/plugin.json` and `skills/`.
- Claude Code: reads `.claude-plugin/plugin.json` and root-level `skills/`.
- Antigravity: reads root `plugin.json` and root-level `skills/`.
- Hermes: installs from the repository-level `skills/` tap mirror.

Claude Code can test a local plugin directory or zip archive with
`claude --plugin-dir`. Antigravity can install a local plugin directory with
`agy plugin install /path/to/plugin`.

Hermes can add this repository as a custom skill tap:

```bash
hermes skills tap add jxpeng98/skills
hermes skills search commit
hermes skills install jxpeng98/skills/commit-message
```

## Credits And References

These skills are local adaptations, not vendored copies. Reference sources are
credited here so future changes can preserve intent and update behavior when the
upstream guidance changes.

| Area | Reference |
| --- | --- |
| Skill structure and `SKILL.md` conventions | [Open Agent Skills specification](https://openagentskills.dev/docs/specification) and this repository's [DEVELOPMENT.md](DEVELOPMENT.md). |
| Codex plugin packaging | [OpenAI Academy: Plugins and skills](https://openai.com/academy/codex-plugins-and-skills/) and the local Codex plugin manifest conventions used by this repository. |
| Claude Code plugin packaging | [Claude Code plugin docs](https://code.claude.com/docs/en/plugins) and [plugin reference](https://code.claude.com/docs/en/plugins-reference). |
| Antigravity plugin packaging | [Google Antigravity plugins documentation](https://antigravity.google/docs/plugins) and [CLI plugins documentation](https://antigravity.google/docs/cli-plugins). |
| Hermes skill tap packaging | [Hermes Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills) and [Hermes Skills System](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md). |
| `grill-me` | Inspired by Matt Pocock's [`grill-me` skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md). |
| `commit-message` | Based on [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). |
| `pr-description` | Informed by GitHub Docs on [helping others review your changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes). |
| `slidev-slides` | Based on official Slidev documentation: [Getting Started](https://sli.dev/guide/), [CLI](https://sli.dev/builtin/cli), and [Exporting](https://sli.dev/guide/exporting). |
| `faculty-tools`, `decide-between-options`, `repo-boundary-review`, `release-readiness`, `humanizer`, `rewrite-for-clarity`, `summarize-material` | Original local workflow skills derived from day-to-day teaching, engineering, repository maintenance, and communication practice. |
