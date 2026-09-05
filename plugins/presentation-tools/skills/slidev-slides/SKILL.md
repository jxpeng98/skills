---
name: slidev-slides
description: "Create, edit, review, build, present, or export Markdown-based Slidev decks. Use only when Slidev is the chosen format; use presentation-tool for format selection or native PPTX and Beamer workflows."
---

# Slidev Slides

Use the language and regional variety required by the audience. Write slide text
as people normally speak: common words, natural phrases, and only the technical
terms the subject needs. Avoid report prose, consultant headings, and showy wording.

Inspect `slides.md`, `package.json`, components, layouts, assets, theme, and
scripts. Reuse the project's package manager, Node version, commands, fonts, and
paths.

If the requested deliverable changes to native editable PPTX or Beamer, use
`presentation-tool` when available. If unavailable, preserve the required format
with compatible tooling and report missing capabilities; an image-based Slidev
export does not satisfy native editability.

1. Identify audience, desired outcome, talk length, and target export.
2. Outline the opening claim, core sections, demo or decision path, risks, and
   close.
3. Write stable Markdown slide separators and frontmatter. Keep one idea per
   slide, short bullets, and readable code.
4. Prefer diagrams, workflows, code, decisions, screenshots, and demo checkpoints
   that carry information; skip decorative slide volume.
5. Give informative images meaningful alt text, preserve a logical reading
   order, use legible type and contrast, and provide a static fallback for every
   live demo or interaction.
6. Build or export with existing scripts.

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
code, speaker notes, links, talk time, reading order, contrast, and lost
interactive meaning. Report checks not run.
