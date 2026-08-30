---
name: presentation-tool
description: "Create, edit, review, or route Slidev, PowerPoint/PPTX, Beamer, Marp, Quarto, or PDF presentation work. Use when the format is undecided or not fixed to Slidev; use slidev-slides when Slidev is already chosen."
---

# Presentation Tool

Use the language and regional variety required by the audience. Write slide text
as people normally speak: common words, natural phrases, and only the technical
terms the subject needs. Avoid report prose, consultant headings, and showy wording.

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
   constraints, and notes or handout needs. Infer what is clear; if one missing
   detail changes the format, ask one short, direct question.
2. Draft a short format-neutral outline, then keep the existing project toolchain
   unless it cannot produce the required artifact.
3. Build one primary idea per slide and preserve local paths, engines, themes,
   fonts, and package manager.
4. Keep important claims traceable to supplied sources. Give every live demo or
   interactive step a static fallback that still communicates the result.
5. Render the actual target artifact and inspect it before finishing.

Format rules:

- PPTX: use supplied masters/layouts; preserve editable text, tables, charts,
  notes, and media. Use the project's existing PPTX library.
- Beamer: preserve the TeX project and engine; use semantic frames, sparse
  overlays, and `fragile` for verbatim content; compile the PDF.
- Marp/Quarto: choose Marp for simple decks and Quarto only when its executable or
  publishing features are needed.

Check overflow, cropping, broken assets, aspect ratio, fonts, code readability,
speaker notes, links, talk time, reading order, contrast, meaningful alt text or
nearby explanations, static-export meaning, and format-specific editability.
Report checks not run. Do not substitute image-only PPTX slides when editable
objects are required.
