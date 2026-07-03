---
name: slidev-slides
description: Use when the user wants to create, edit, review, present, build, or export slides with Slidev; asks for a Markdown-based deck; or needs engineering, product, architecture, demo, project-review, or technical-talk slides.
---

# Slidev Slides

## Purpose

Create practical Slidev decks for engineering and project communication. Favor clear narrative, inspectable Markdown, and exportable artifacts over decorative slide volume.

## Workflow

1. Inspect the repository for existing Slidev files before creating new structure: `slides.md`, `package.json`, `components/`, `layouts/`, `public/`, theme config, and scripts.
2. Identify audience, outcome, delivery length, and target format. If one missing detail blocks the deck structure, ask one focused question.
3. Draft a slide outline first: opening claim, context, core sections, decision or demo path, risks, and close.
4. Write slides in Markdown with stable `---` slide separators and frontmatter when needed.
5. For engineering decks, prefer architecture diagrams, workflows, code snippets, decision tables, tradeoffs, screenshots, and demo checkpoints.
6. Keep each slide scannable: one primary idea, short bullets, readable code, and no dense paragraphs.
7. Preserve local project conventions for package manager, scripts, theme, fonts, and asset paths.

## Commands

Slidev requires Node.js 20.12.0 or newer.

Prefer existing `package.json` scripts. Common Slidev commands are:

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

## Verification

Before calling a deck ready:

- Run the relevant command when feasible: dev server, `slidev build`, or `slidev export`.
- Inspect rendered slides or exported artifacts for overflow, cropped content, unreadable code, broken images, missing fonts, and incorrect aspect ratio.
- Check that speaker notes, links, diagrams, and code highlighting behave as intended.
- Report any command that could not be run and what still needs manual review.

## Scope

This repository is for daily development and engineering project workflows. Do not turn this into an academic lecture, citation, or paper-planning workflow unless the user explicitly asks for that outside this repository's normal scope.
