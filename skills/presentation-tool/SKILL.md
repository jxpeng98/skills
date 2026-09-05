---
name: presentation-tool
description: "Create, edit, review, or route PowerPoint/PPTX, Beamer, Marp, Quarto, PDF, or undecided presentation work. Prefer slidev-slides when Slidev remains the chosen output; use this for native editable PPTX even from Slidev sources."
---

# Presentation Tool

Use the language and regional variety required by the audience. Write slide text
as people normally speak: common words, natural phrases, and only the technical
terms the subject needs. Avoid report prose, consultant headings, and showy wording.

Choose by the required output, not just the source extension. Use `slidev-slides`
when Slidev remains the chosen workflow and that skill is available; otherwise
use existing project scripts and the checks below. Inspect the deck, template,
assets, and tooling before choosing a format.

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
   For new PPTX or Beamer projects, missing tooling, or rendering limitations,
   read `references/format-workflows.md`.
3. Build one primary idea per slide and preserve local paths, engines, themes,
   fonts, and package manager.
4. Keep important claims traceable to supplied sources. Give every live demo or
   interactive step a static fallback that still communicates the result.
5. Render the actual target artifact and inspect it before finishing.

Format rules:

- PPTX: use supplied masters/layouts and tooling that preserves the required
  editable text, tables, charts, notes, and media. Do not flatten Slidev output
  into images when native editable objects are required.
- Beamer: preserve the TeX project and engine; use semantic frames, sparse
  overlays, and `fragile` for verbatim content; compile the PDF.
- Marp/Quarto: choose Marp for simple decks and Quarto only when its executable or
  publishing features are needed.

Check overflow, cropping, broken assets, aspect ratio, fonts, code readability,
speaker notes, links, talk time, reading order, contrast, meaningful alt text or
nearby explanations, static-export meaning, and format-specific editability.
Report checks not run. Do not substitute image-only PPTX slides when editable
objects are required. Distinguish artifact creation from successful rendering;
an unrendered deliverable still has unverified layout.
