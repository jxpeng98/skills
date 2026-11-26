---
name: presentation-tool
description: "Create, edit, review, or export presentations and accompanying handouts, including native editable PPTX and Beamer. Use slidev-slides when Slidev is the chosen output."
---

# Presentation Tool

Choose by the requested artifact, not the source extension. Use `slidev-slides`
for a Slidev workflow when available; otherwise complete it with compatible
project tooling. Preserve supplied templates, fonts, engines, paths, and the
package manager unless a requested change requires otherwise.

Match the operation:

- **Create or redesign:** establish audience, purpose, talk length, required
  artifact/editability, prior knowledge, and template constraints. Infer what is
  clear. Plan the argument and visual hierarchy, then build and verify the deck.
- **Edit:** inspect the affected slides and their layout dependencies. Make the
  requested change without re-outlining or redesigning unrelated slides.
- **Review:** inspect the source and available render; return findings with slide
  locations, evidence, and fixes. Do not modify the deck unless asked.
- **Export:** reuse the existing source and build route. Verify the requested
  output without rewriting the content or replacing the design.

When the output format is undecided, use this choice:

| Format | Choose it when |
| --- | --- |
| Slidev | Source control, code, demos, or web delivery matter |
| PPTX | PowerPoint editing, supplied masters, or brand layouts matter |
| Beamer | Reproducible PDF, math, citations, or TeX source matter |
| Marp | Plain Markdown and simple export are enough |
| Quarto | Executable code, notebooks, or multi-output publishing matter |

For new PPTX/Beamer projects, missing tools, or rendering limitations, read
`references/format-workflows.md`. For new decks or changes to content depth,
templates, visual hierarchy, or accompanying handouts, read
`references/content-and-layout.md`.
A typo fix or routine export does not need a fresh content/design planning pass.

Content and layout requirements:

- Give each substantive slide a clear point or question and enough concrete
  support to understand it: a finding, mechanism, worked example, comparison,
  or decision with its tradeoff. Keep essential explanation on the slide; notes
  can extend it. Fit the content to the time and audience by removing repetition
  and choosing the strongest support. Restructure a crowded slide before
  cutting the evidence or qualification the audience needs. Keep covers and
  section dividers simple.
- Use a supported takeaway title for a finding; use a specific topic title for
  a process, definition, or setup. Avoid unsupported insight or generic labels.
  Use natural English or Chinese clause order, with clear actors, actions, and
  conditions. Keep technical distinctions; do not compress reasoning into noun
  stacks or choose ornate terms at the cost of fluency. A compact title or label
  is fine when its relationship to the explanation is clear.
- Sequence ideas so the audience has the definitions and context needed for each
  next step. Explain how an example or result supports the point; transitions
  must express the actual relationship, not disguise a jump in reasoning.
- Create only requested materials. Slides need visible support for their point;
  speaker notes can add delivery cues and detail. A reading handout must explain
  the topic without the speaker, using relevant definitions, worked reasoning,
  examples, and limits. Keep shared facts and terms consistent across outputs.
- Keep evidence, interpretation, and proposed action distinct. Preserve units,
  time periods, denominators, comparison bases, caveats, and source anchors.
  If evidence is thin, identify the specific gap or use a clearly labelled
  illustration; do not fabricate numbers, explanations, or citations for depth.
- Make the template concrete: consistent title, evidence/body, and source areas;
  a readable type hierarchy, alignment, spacing, and color roles; a small set of
  layouts selected for the content. Use imagery that explains the subject or
  serves the supplied design. Test layouts with real, dense material before
  extending them.
- Preserve required native editable text, tables, charts, diagrams, and notes.
  Image-only Slidev export cannot satisfy native editable PPTX. Give demos and
  interactions a static fallback, and preserve accessible reading order,
  contrast, and meaningful alt text or adjacent explanations.

For creation or a deck-wide redesign, render and inspect every slide. For local
edits, inspect affected slides and adjacent continuity; expand checks for global
font, theme, master, or export changes. Check both argument coverage and visual
legibility: unsupported claims, generic filler, missing explanation, overflow,
cropping, assets, labels, fonts, editability, and static-export meaning.
Check requested handouts separately for complete explanations and, for formatted
documents, rendered legibility and page breaks.
Repair failures caused by the work and rerun affected checks until the requested
artifact is usable or a concrete blocker remains. Distinguish source creation,
successful export, and inspected layout; report only checks actually performed.
