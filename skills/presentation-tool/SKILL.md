---
name: presentation-tool
description: "Choose or work across Slidev, PowerPoint/PPTX, Beamer, Marp, Quarto, or PDF presentation workflows. Use when the format is undecided or not fixed to Slidev; use slidev-slides when Slidev is already chosen."
---

# Presentation Tool

Use `slidev-slides` directly when Slidev is already fixed. Otherwise inspect the
existing deck, template, assets, project files, and build tooling before choosing
a format.

| Format | Choose it when |
| --- | --- |
| Slidev | Source control, code, demos, or web delivery matter |
| PPTX | PowerPoint editing, supplied templates, masters, or brand layouts matter |
| Beamer | Reproducible PDF, math, citations, or TeX source matter |
| Marp | Plain Markdown and simple export are enough |
| Quarto | Executable code, notebooks, citations, or multi-output publishing matter |

1. Identify audience, talk length, final artifact, editability, template/brand
   constraints, and notes or handout needs.
2. Draft a short format-neutral outline, then keep the existing project toolchain
   unless it cannot produce the required artifact.
3. Build one primary idea per slide and preserve local paths, engines, themes,
   fonts, and package manager.
4. Render the actual target artifact and inspect it before finishing.

Format rules:

- PPTX: use supplied masters/layouts; preserve editable text, tables, charts,
  notes, and media. Use the project's existing PPTX library.
- Beamer: preserve the TeX project and engine; use semantic frames, sparse
  overlays, and `fragile` for verbatim content; compile the PDF.
- Marp/Quarto: choose Marp for simple decks and Quarto only when its executable or
  publishing features are needed.

Check overflow, cropping, broken assets, aspect ratio, fonts, code readability,
notes, links, talk time, and format-specific editability. Report checks not run.
Do not substitute image-only PPTX slides when editable objects are required.
