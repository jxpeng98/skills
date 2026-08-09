---
name: slidev-slides
description: "Create, edit, review, build, present, or export Markdown-based Slidev decks. Use only when Slidev is the chosen format; use presentation-tool for format selection or native PPTX and Beamer workflows."
---

# Slidev Slides

Inspect `slides.md`, `package.json`, components, layouts, assets, theme, and
scripts. Reuse the project's package manager, Node version, commands, fonts, and
paths.

1. Identify audience, desired outcome, talk length, and target export.
2. Outline the opening claim, core sections, demo or decision path, risks, and
   close.
3. Write stable Markdown slide separators and frontmatter. Keep one idea per
   slide, short bullets, and readable code.
4. Prefer diagrams, workflows, code, decisions, screenshots, and demo checkpoints
   that carry information; skip decorative slide volume.
5. Build or export with existing scripts.

Common direct commands:

```bash
slidev slides.md
slidev build
slidev export
slidev export --format pptx
```

The CLI package is `@slidev/cli`; do not assume `npx slidev` resolves it. PDF,
PPTX, and PNG export may require `playwright-chromium`; PPTX text is image-based,
and static exports can lose interactivity.

Inspect the rendered result for overflow, cropping, assets, fonts, aspect ratio,
code, notes, links, and lost interactive meaning. Report checks not run.
