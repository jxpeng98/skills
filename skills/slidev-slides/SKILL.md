---
name: slidev-slides
description: "Create, edit, review, present, build, or export Markdown-based Slidev decks for engineering, product, architecture, demos, project reviews, and technical talks. Trigger when Slidev is the chosen format; use presentation-tool first when PPTX, Beamer, Marp, Quarto, or the target format is still undecided."
---

# Slidev Slides

## Outcome

Create practical Slidev decks for engineering and project communication. Favor clear narrative, inspectable Markdown, and exportable artifacts over decorative slide volume.

## Inputs And Defaults

Inspect the existing deck, theme, components, assets, scripts, and package-manager
files first. Infer ordinary visual and narrative choices from the project. Ask
one focused question only when audience, talk length, target export, or required
branding would materially change the deck.

## Workflow

1. Inspect the repository for existing Slidev files before creating new structure: `slides.md`, `package.json`, `components/`, `layouts/`, `public/`, theme config, and scripts.
2. Identify audience, outcome, delivery length, and target format.
3. Draft a slide outline first: opening claim, context, core sections, decision or demo path, risks, and close.
4. Write slides in Markdown with stable `---` slide separators and frontmatter when needed.
5. For engineering decks, prefer architecture diagrams, workflows, code snippets, decision tables, tradeoffs, screenshots, and demo checkpoints.
6. Keep each slide scannable: one primary idea, short bullets, readable code, and no dense paragraphs.
7. Preserve local project conventions for package manager, scripts, theme, fonts, and asset paths.

## Commands

Prefer the project's declared Node.js/package-manager versions and existing
`package.json` scripts. For a new project, verify current Slidev prerequisites
instead of pinning a remembered runtime version. Common Slidev commands are:

```bash
pnpm create slidev
npm init slidev@latest
slidev
slidev slides.md
slidev build
slidev export
slidev export --format pptx
slidev export --format png
slidev export --format md
```

If using npm scripts and passing Slidev options, include the extra separator:

```bash
npm run slidev -- --port 3030 --open
```

Do not assume `npx slidev` works. The CLI package is `@slidev/cli`; use the project-local CLI or package scripts when available.

## Export Notes

- PDF, PPTX, and PNG export rely on Playwright rendering and may require `playwright-chromium`.
- PPTX exports slides as images, so text may not remain selectable.
- Interactive features can be lost in static exports; use `slidev build` when the interactive web deck is the deliverable.
- For missing content, unfinished animations, or timeout issues, try export options such as `--wait`, `--timeout`, or the browser export UI.

## Completion Check

Before calling a deck ready:

- Run the relevant command when feasible: dev server, `slidev build`, or `slidev export`.
- Inspect rendered slides or exported artifacts for overflow, cropped content, unreadable code, broken images, missing fonts, and incorrect aspect ratio.
- Check that speaker notes, links, diagrams, and code highlighting behave as intended.
- Report any command that could not be run and what still needs manual review.
- Confirm the deck fits the planned talk time, each slide has one primary idea,
  and static exports do not silently lose required interactive meaning.

## Scope

This repository is for daily development and engineering project workflows. Do not turn this into an academic lecture, citation, or paper-planning workflow unless the user explicitly asks for that outside this repository's normal scope.
