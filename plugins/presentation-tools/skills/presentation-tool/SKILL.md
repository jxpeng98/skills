---
name: presentation-tool
description: "Route, create, edit, review, convert, or export presentations across Slidev, PowerPoint/PPTX, LaTeX Beamer, Marp, Quarto, PDF, or multiple deliverables. Trigger when format is undecided, PPTX/Beamer/template fidelity matters, or deck QA is required; use slidev-slides directly only when Slidev is already fixed."
---

# Presentation Tool

## Outcome

Route presentation work to the format that best matches the deliverable, then apply format-specific build and QA discipline. Prefer editable source formats for collaboration, but honor native PowerPoint or Beamer/PDF requirements when those are the real deliverables.

Use `slidev-slides` for detailed Slidev implementation after routing when the deck is clearly Slidev-based.

## Inputs And Defaults

Inspect supplied notes, existing decks, templates, brand assets, project files,
and build tooling first. Infer ordinary narrative and design choices. Ask one
focused question only when audience, talk length, required artifact, editability,
or template fidelity would change the format choice; otherwise preserve the
existing toolchain and proceed.

## Workflow

1. Inspect existing materials before creating anything: `slides.md`, `.pptx`, `.tex`, `_quarto.yml`, `package.json`, assets, templates, fonts, and build scripts.
2. Identify audience, talk length, final deliverable, editability requirements, brand/template constraints, and whether speaker notes or handouts are needed.
3. Draft a format-neutral outline first: opening claim, sections, evidence or demo path, decision points, risks, and close.
4. Choose the format using the router below and preserve local project conventions for package manager, TeX engine, output paths, and asset organization.
5. Build the deck in the chosen source format.
6. Verify by rendering the actual target artifact, not just by reading source.

## Format Router

| Use this | When it fits | Avoid when |
| --- | --- | --- |
| Slidev | Source-controlled technical decks, live demos, code snippets, web delivery, fast Markdown iteration | The required deliverable is an editable corporate `.pptx` |
| Native PPTX | A `.pptx` template is supplied, PowerPoint editing is required, brand masters/layouts matter, or an existing deck must be restyled | The user mainly needs reproducible text source or precise math typesetting |
| LaTeX Beamer | PDF is the deliverable, math/citations/code are central, the audience expects academic or technical TeX output | The user needs editable PowerPoint objects |
| Marp | Plain Markdown slides with quick HTML/PDF/PPTX/image export are enough | Complex component logic or heavy custom interactivity is needed |
| Quarto | Technical publishing, executable notebooks, citations, cross-references, or multiple output formats are central | A lightweight one-off deck is all that is needed |

## Native PPTX

When a template or existing `.pptx` drives the task:

1. Inspect the deck before editing: slide size, masters, layouts, placeholder geometry, theme colors, fonts, logos, footers, and existing notes.
2. Build from the template's own masters/layouts instead of recreating brand elements manually.
3. Keep content in a structured outline or object model before writing slides; map each slide to an available layout.
4. For existing decks, copy the file first and make the smallest reliable edits. Preserve editable text, tables, charts, notes, and media when feasible.
5. Prefer `python-pptx` in Python workflows and PptxGenJS in JavaScript/TypeScript or browser workflows. Use PowerPoint, Keynote, or LibreOffice only for visual QA or conversion unless the user explicitly wants manual application automation.
6. Do not use image-based exports when the user expects editable PowerPoint text and objects.

Surface limitations clearly: SmartArt, animations, deeply custom chart styling, and slide-level decoration outside masters may need manual review.

## LaTeX Beamer

When Beamer is the right target:

1. Inspect the TeX project first: main `.tex`, theme `.sty`/`.cls`, bibliography files, images, `latexmkrc`, and existing build commands.
2. Keep structure semantic: `\section`, `\subsection`, and focused `frame` blocks. Use one primary idea per frame.
3. Use overlays sparingly and deliberately; avoid overlay-heavy source unless the reveal sequence is part of the talk.
4. Use `fragile` frames for code or verbatim content.
5. Choose the engine from the project if present. Otherwise use `pdflatex` for simple Latin text, and `xelatex` or `lualatex` when system fonts or Unicode text matter.
6. Compile with the existing command, `latexmk`, or `tectonic` when available. Fix missing assets, unresolved references, and visible overfull content before calling the deck ready.

Do not turn a presentation request into a literature review, citation search, thesis plan, or paper workflow unless the user explicitly asks for that work.

## Markdown Multi-Output

Use Marp or Quarto when the source should remain plain Markdown but the output may need HTML, PDF, PPTX, or images.

- Use Marp for lightweight Markdown decks and quick export.
- Use Quarto when executable code, citations, cross-references, notebooks, or shared project configuration matter.
- Use Pandoc directly only for simple conversion when the project already depends on it or the deck has minimal layout requirements.

## Completion Check

Before calling a presentation ready:

- Run the relevant build/export command when feasible: Slidev build/export, PPTX generation script, LibreOffice conversion, `latexmk`, `tectonic`, `marp`, `quarto render`, or Pandoc.
- Inspect rendered slides or exported images/PDF for overflow, cropped content, broken images, wrong aspect ratio, missing fonts, unreadable code, and lost speaker notes.
- For PPTX, open or render the actual `.pptx`; verify masters/layouts, logos, footers, notes, tables, charts, and editable text survived.
- For Beamer, inspect the compiled PDF and fix warnings that affect visible output.
- Report commands that could not be run and the remaining manual checks.
- Confirm the narrative fits the available talk time and each slide has one
  primary job.
- Do not call source-only review complete when the requested deliverable is a
  rendered PPTX, PDF, image set, or hosted deck.

## References

Read `references/github-patterns.md` when adapting the GitHub-derived PPTX, Beamer, Marp, or Quarto patterns, or when explaining why one format was selected over another.
