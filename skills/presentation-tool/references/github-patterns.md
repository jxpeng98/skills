# GitHub Presentation Patterns

Use this reference when a presentation task needs format-specific judgment beyond the core workflow in `SKILL.md`.

## PPTX Template-First Pattern

Source reviewed: `ghanemja/stencil`, especially `pptx-template-styler`.

Reusable pattern:

- Treat a user-supplied `.pptx` as a structural template, not just a color sample.
- Inspect masters, layouts, placeholders, theme colors, fonts, logos, and footers before generating slides.
- Build a structured content model first, then map slides to template layouts.
- For restyling, explain that results can be lossy when source content depends on one-off slide decorations rather than master/layout definitions.
- Always do visual QA because text overflow and placeholder mismatch are common PPTX failures.

## PPTX Library Pattern

Sources reviewed: `scanny/python-pptx` and `gitbrent/PptxGenJS`.

Reusable pattern:

- Use `python-pptx` when the project is Python-based or when the task is reading, creating, or updating `.pptx` files without requiring PowerPoint to be installed.
- Use PptxGenJS when the project is JavaScript/TypeScript-based, browser-facing, or already produces slides from web/app data.
- Prefer native OOXML output when editable PowerPoint objects matter.
- Keep charts, tables, text, and images as editable slide objects whenever possible.

## Animation And Math Media

Source reviewed: `ghanemja/stencil` companion Manim skills.

Reusable pattern:

- Represent repeatable math/data animations with structured specs before rendering media.
- Embed rendered GIFs or images into PPTX only when the final deck needs media playback rather than editable formulas.
- Warn that animated GIFs usually play in slideshow mode, while edit mode may show only the first frame.
- Do not run arbitrary animation code from untrusted input.

## LaTeX Beamer Pattern

Source reviewed: `josephwright/beamer`.

Reusable pattern:

- Use Beamer when semantic TeX source, reproducible PDF output, math, citations, and technical structure matter more than PowerPoint editability.
- Keep appearance in themes/templates and content in frames/sections.
- Use Beamer overlays only when the reveal behavior serves the talk.
- Compile and inspect the PDF; source correctness is not enough.

## Markdown Multi-Output Pattern

Sources reviewed: `marp-team/marp` and `quarto-dev/quarto-cli`.

Reusable pattern:

- Use Marp for plain Markdown decks with straightforward HTML/PDF/PPTX/image export.
- Use Quarto for technical publishing workflows that combine Markdown with code, citations, cross-references, notebooks, or project-level rendering.
- Prefer existing project configuration over introducing a new presentation toolchain.

## Source Links

- https://github.com/ghanemja/stencil
- https://github.com/scanny/python-pptx
- https://github.com/gitbrent/PptxGenJS
- https://github.com/josephwright/beamer
- https://github.com/marp-team/marp
- https://github.com/quarto-dev/quarto-cli
