# Skills Repository Development Guide

This repository, `jxpeng98/skills`, is the source repository for reusable agent
skills and installable skill plugins.

It is intentionally separate from `jxpeng98/skillsplace`, which is the marketplace
catalog repository.

## Repository Relationship

Use this split:

- `jxpeng98/skills`: owns the real skill and plugin content.
- `jxpeng98/skillsplace`: owns marketplace metadata that points to installable
  plugin paths in this repository.

The normal publishing flow is:

1. Develop or update skills in `jxpeng98/skills`.
2. Package related skills under a plugin directory in `jxpeng98/skills`.
3. Test the skill or plugin from its source path.
4. Update `jxpeng98/skillsplace` so the marketplace points to the plugin path.
5. Run `npm run validate` in `jxpeng98/skillsplace`.

`skillsplace` should not copy skill source code. It should only reference this
repository through Git URLs, GitHub URLs, or `git-subdir` paths.

`skills` should not become a marketplace catalog. It can contain plugin manifests,
skill files, references, scripts, and assets, but it should not maintain the
aggregate marketplace files that belong to `skillsplace`.

## Boundary Of This Repository

This repository may contain:

- Skill directories with `SKILL.md`.
- Plugin directories that package related skills.
- Platform plugin manifests inside plugin directories.
- A top-level `skills/` Hermes tap mirror generated from plugin skill
  directories.
- Skill-specific `references/`, `scripts/`, and `assets/`.
- Shared references or helper scripts when they are directly used by skills.
- Repository-level development documentation.
- Repository-local maintenance skills under `.agents/skills/` when they should
  not ship in a public plugin.

This repository should not contain:

- Marketplace catalog files such as `marketplace.json`,
  `.agents/plugins/marketplace.json`, or `.claude-plugin/marketplace.json`.
- Copied marketplace metadata from `skillsplace`.
- Unrelated application source trees.
- Bundled third-party package contents unless they are reviewed and required.
- Secrets, API keys, tokens, private certificates, cookies, or credentials.
- Local absolute paths or user-specific machine configuration.
- Private customer data or internal documents that should not be distributed.
- Academic research workflows, literature review systems, citation workflows, or
  thesis/paper planning skills. Teaching, student support, faculty service, and
  university-writing coaching are allowed when they preserve academic integrity
  and do not replace the user's own research or assessed work.

Plugin manifests are allowed here when they are part of an installable plugin
directory. Marketplace catalog files are not.

## Recommended Layout

Use `plugins/` for anything intended to be installable from `skillsplace`:

```text
.
├── DEVELOPMENT.md
├── README.md
├── skills/
│   ├── grill-me/
│   │   └── SKILL.md
│   └── pr-description/
│       └── SKILL.md
├── drafts/
│   └── experimental-skill/
│       └── SKILL.md
└── plugins/
    ├── productivity/
    │   ├── plugin.json
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── .claude-plugin/
    │   │   └── plugin.json
    │   └── skills/
    │       ├── grill-me/
    │       │   └── SKILL.md
    │       └── pr-description/
    │           └── SKILL.md
    └── presentation-tools/
        ├── plugin.json
        ├── .codex-plugin/
        │   └── plugin.json
        ├── .claude-plugin/
        │   └── plugin.json
        └── skills/
            └── slidev-slides/
                └── SKILL.md
```

The top-level `skills/` tree is generated for Hermes taps. Do not edit it
directly. Edit `plugins/<plugin-name>/skills/<skill-name>/`, then run:

```bash
python scripts/sync_hermes_tap.py
```

Keep repository-only maintenance workflows in `.agents/skills/`. Do not package
or mirror them unless they are deliberately redesigned as general public skills.

Use `drafts/` or a temporary top-level category folder only for early local
experiments. Before publishing through `skillsplace`, move the skill into:

```text
plugins/<plugin-name>/skills/<skill-name>/SKILL.md
```

A top-level draft layout such as `productivity/grill-me/SKILL.md` is acceptable
only for early local experiments. For marketplace distribution, promote it to:

```text
plugins/productivity/skills/grill-me/SKILL.md
```

## Plugin Boundaries

A skill is the behavior unit. A plugin is the installable unit.

Group skills into the same plugin when users would naturally install them
together:

- `productivity`: planning, critique, decision review, commit, PR, and release
  helpers.
- `writing-tools`: editing, translation, tone, and summarization helpers.
- `dev-tools`: debugging, repository maintenance, and release automation helpers.
- `faculty-tools`: university teaching, assignment design, student feedback,
  faculty communication, meetings, and light academic-service writing helpers.
- `presentation-tools`: format routing, Slidev decks, editable PPTX decks,
  LaTeX Beamer slides, engineering presentations, technical talks, project
  reviews, and architecture walkthroughs.

Create separate plugins when:

- The skills target different audiences.
- They require different permissions or trust levels.
- Users should be able to install one group without the others.
- They have different release cadences.

Keep plugin names in kebab-case and keep published names stable.

## Skill Directory Standard

Each skill should live in its own directory:

```text
skills/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

Only `SKILL.md` is required by the cross-platform skill format. This repository
also requires `agents/openai.yaml` for Codex UI metadata. Add references,
scripts, and assets only when the skill needs them.

`SKILL.md` must start with YAML frontmatter:

```markdown
---
name: skill-name
description: Create or review <artifact> from <evidence> for <specific requests>; use <adjacent-skill> instead for <boundary>.
---
```

Rules:

- Use lowercase kebab-case for skill names.
- Keep skill names short and stable.
- Front-load the action, artifact, and trigger terms in `description`; do not
  spend the first words on generic phrases such as `Use when`.
- Name the nearest non-trigger or sibling skill when users could reasonably
  confuse them.
- Keep descriptions and `SKILL.md` as short as the workflow allows.
- Move long examples, policies, API notes, and domain references into
  `references/`.
- Add scripts only when deterministic behavior or repeated execution justifies
  them.
- Add assets only when the skill needs templates or reusable files.
- Add `agents/openai.yaml` with `display_name`, a 25-64 character
  `short_description`, and a one-sentence `default_prompt` that explicitly
  mentions `$skill-name`.

## Minimal Skill Profile

Keep model choice and general agent behavior outside individual skills. Before
adding instructions or resources, stop at the first option that works:

1. Do not create a skill for a one-off prompt or existing `AGENTS.md` rule.
2. Reuse an existing skill, resource, standard library, or native tool.
3. Prefer a few instructions over a script; add a script only for repeated,
   deterministic work.
4. Keep only domain knowledge, routing, safety boundaries, output contracts, and
   validation that change behavior. Delete generic agent advice and repetition.
5. Use directly linked references only when conditional detail would otherwise
   burden every invocation.
6. Validate the actual deliverable. Add one small runnable check for non-trivial
   scripts; do not test Markdown phrasing.

## Precision Contract

Include only the clauses that prevent wrong behavior:

- **Trigger:** define the direct request and the nearest adjacent non-trigger.
- **Evidence:** name authoritative inputs and mark missing evidence as unknown.
- **Route:** add branches only when different inputs require different methods.
- **Output:** state the exact deliverable and useful default shape.
- **Stop:** state verification and external-write boundaries.

Record one direct prompt, one paraphrase, and one adjacent negative prompt for
every distributable skill in `evals/skill-routing.json`. Use them for forward
behavior checks; do not turn them into keyword tests for generated prose. Simple
skills can express the contract in a short sequence; complex or fragile workflows
may use explicit sections and deterministic scripts.

For overlapping or environment-dependent workflows, add a behavioral scenario
with `available_skills`, a self-contained `prompt`, `expected_skill`, and observable
`checks`. Include raw source material in the prompt. Give forward evaluators only
the available skills and prompt, withholding the expected route and checks; record
actual outcomes separately from structural validation. A sibling skill may be
absent in an independent plugin or Hermes installation, so provide a usable
fallback instead of treating a routing hint as an installed dependency.

## Supporting Resources

Use `references/` for detailed material the agent should load only when relevant:

```text
references/
├── api.md
├── examples.md
└── style-guide.md
```

Use `scripts/` for reliable executable helpers:

```text
scripts/
└── validate_output.py
```

Use `assets/` for templates and reusable output files:

```text
assets/
└── report-template.docx
```

Do not duplicate the same large reference across multiple skills. Put shared
material at the plugin level when practical and point individual skills to it.

## Marketplace Integration

When a plugin is ready, register it from `skillsplace` using a `git-subdir`
source that points into this repository.

Example Codex marketplace entry in `skillsplace/.agents/plugins/marketplace.json`:

```json
{
  "name": "productivity",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/jxpeng98/skills.git",
    "path": "./plugins/productivity",
    "ref": "main"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Example Claude Code marketplace entry in `skillsplace/.claude-plugin/marketplace.json`:

```json
{
  "name": "productivity",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/jxpeng98/skills.git",
    "path": "plugins/productivity",
    "ref": "main"
  },
  "description": "Productivity skills for planning, critique, review, and release work."
}
```

After changing marketplace metadata, validate from the `skillsplace` repository:

```bash
npm run validate
```

## Versioning Policy

This repository uses synchronized releases. For a repository tag `vX.Y.Z`, every
plugin must use `X.Y.Z` in its Codex manifest, Claude manifest, and
`skillsplace.json`, including plugins whose behavior did not change in that
release. `python scripts/validate_plugins.py` rejects cross-plugin version drift.

## Platform Compatibility

Each publishable plugin should include these platform markers:

- `.codex-plugin/plugin.json` for Codex.
- `.claude-plugin/plugin.json` for Claude Code.
- Root `plugin.json` for Antigravity.

Keep shared skills at the plugin root under `skills/<skill-name>/SKILL.md`.
Do not move `skills/` inside a platform-specific manifest directory.

For Hermes, keep the repository-level `skills/<skill-name>/SKILL.md` mirror in
sync. Hermes taps default to the repository `skills/` path, so users can install
with:

```bash
hermes skills tap add jxpeng98/skills
hermes skills install jxpeng98/skills/<skill-name>
```

Check the mirror without changing files:

```bash
python scripts/sync_hermes_tap.py --check
```

Validate the repo-local plugin layout before publishing:

```bash
python scripts/validate_plugins.py
```

Build release archives locally when needed:

```bash
python scripts/package_plugins.py --output dist
```

The GitHub Actions release workflow packages each plugin as `.zip` and
`.tar.gz`, creates `all-plugins.zip`, and publishes those files as release
assets when a `v*` tag is pushed.

## Public And Private Use

This repository does not have to be public. It only needs to be accessible to the
users or tools installing from it.

Use a public repository when:

- The skills are intended for broad distribution.
- `skillsplace` is public and should offer installable entries to everyone.
- Users should not need extra Git authentication.

Use a private repository when:

- Skills include personal, team, or internal workflows.
- Skills mention private systems, policies, or operating procedures.
- Installation is limited to users with repository access.

If a public marketplace points to a private skills repository, users without
access may see the catalog entry but will not be able to install it.

## Development Workflow

1. Decide whether the skill is a draft or part of a publishable plugin.
2. Create or choose the plugin directory.
3. Add the skill under `plugins/<plugin-name>/skills/<skill-name>/`.
4. Write the `SKILL.md` frontmatter and minimal workflow.
5. Add `references/`, `scripts/`, or `assets/` only if needed.
6. Review for trigger accuracy, unnecessary context, and safety issues.
7. Test with realistic prompts.
8. Update plugin manifests if packaging details changed.
9. Run `python scripts/sync_hermes_tap.py` to refresh the Hermes mirror.
10. Update `skillsplace` only after the plugin path is stable.

## Review Checklist

Before publishing a new or changed skill:

- [ ] The skill name is kebab-case and stable.
- [ ] The `description` clearly states when to use the skill.
- [ ] `SKILL.md` is concise and avoids unnecessary background.
- [ ] Long supporting material is under `references/`.
- [ ] Executable helpers are under `scripts/` and reviewed.
- [ ] Reusable templates or files are under `assets/`.
- [ ] No secrets, local paths, or private data are present.
- [ ] The plugin boundary is coherent.
- [ ] The Hermes `skills/` mirror matches plugin skill sources.
- [ ] Marketplace entries point to plugin directories, not draft folders.
- [ ] The skill has been tested with realistic prompts.

## Release Checklist

Before registering or updating a plugin in `skillsplace`:

1. Confirm the plugin path is stable.
2. Confirm all included skills are ready for the target audience.
3. Confirm platform plugin manifests are present when needed.
4. Confirm repository visibility matches the intended audience.
5. Confirm every plugin manifest version matches the repository release tag.
6. Tag or pin a release if consumers need reproducible installs.
7. Run `python scripts/sync_hermes_tap.py --check`.
8. Update `skillsplace` marketplace metadata.
9. Run `npm run validate` in `skillsplace`.
10. Install from the marketplace in a clean environment and test the skill trigger.
