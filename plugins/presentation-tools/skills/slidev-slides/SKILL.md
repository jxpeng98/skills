---
name: slidev-slides
description: "Create, edit, review, or export Slidev decks and accompanying handouts. Use presentation-tool for format selection or native editable PPTX and Beamer."
---

# Slidev Slides

Inspect the relevant `slides.md`, frontmatter, layouts, components, assets, and
package scripts. Reuse the project's package manager, Node version, theme,
fonts, and commands; a local edit needs only its affected dependencies.

For native editable PPTX or Beamer, use `presentation-tool` when available.
Otherwise preserve the requested output with compatible tooling and report
missing capabilities. An image-based export does not satisfy native editability.

Choose the requested operation:

- **Create or redesign:** identify audience, purpose, talk length, and export;
  account for prior knowledge and plan the explanation and layouts before authoring.
- **Edit:** change the affected slides while preserving unrelated content and
  design. Do not draft a new outline for a local wording or data change.
- **Review:** report slide-specific issues and corrections without editing.
- **Export:** use the existing source and scripts, preserving its design and
  content. Do not treat an export request as permission to rewrite the deck.

For new decks or requested content/design improvements:

1. Give each substantive slide a clear point or question supported by a concrete
   example, mechanism, comparison, data, or decision tradeoff. Explain what the
   evidence means; "improve efficiency" or "key benefits" alone is not content.
   Put essential evidence and reasoning on the slide, with extended explanation
   in notes. Covers and dividers can stay brief. Do not impose a bullet quota.
2. Use supported finding titles for results and specific topic titles for setup
   or explanation. Use natural clause order, clear actions, and precise modifiers
   in the audience's language; don't replace reasoning with ornate noun stacks.
   Introduce unfamiliar terms before using them, connect steps across slides,
   and explain how a worked example supports the point instead of only showing
   its answer. Compact labels need not be full sentences.
   Preserve terminology, units, time windows, denominators, source references,
   and uncertainty. Label proposals and illustrations; never invent results or
   citations to make the deck seem detailed. Surface consequential evidence gaps.
3. Define stable title, content, and source positions in the existing theme or
   layouts. Choose a readable type hierarchy, common margins, and clear contrast;
   keep color roles consistent. Use a comparison layout for comparable evidence,
   a diagram for a mechanism, or annotated code for behavior. Do not force every
   slide into the same card grid or title-plus-three-bullets pattern.
   Put deck-wide CSS in `style.css`, `styles/index.css`, or shared layouts,
   with selectors under `.slidev-layout`; a Markdown `<style>` block affects
   only its own slide. A single-file deck must carry needed styles on each slide.
4. Test representative, content-filled slides, including a dense comparison or
   the longest code/text case, before extending a new design. Preserve supplied
   template constraints; split or restructure overload before shrinking text.
   Do not move all explanation into notes or delete important caveats to fit.
5. Use valid Markdown separators and frontmatter. Keep informative images
   accessible, and provide static explanations for click sequences, live demos,
   or interactive components whose meaning would otherwise be lost in export.

Only create accompanying notes or handouts when requested. Speaker notes can hold
delivery cues and extended explanation. A reading handout needs connected prose,
definitions, worked steps or examples, and limits that make sense without the
speaker; copying bullets or exporting slide images does not meet that request.
Preserve a requested slide printout as such. Keep shared facts, terms, and examples
consistent across outputs; label teaching illustrations and invent no results.
Check the handout independently for readable structure and complete explanations.

Build or export with the project's existing commands. Common direct commands:

```bash
slidev slides.md
slidev build
slidev export
slidev export --format pptx
```

The CLI package is `@slidev/cli`; do not assume `npx slidev` resolves it. PDF,
PPTX, and PNG export may require `playwright-chromium`; PPTX slides are image-based,
and static exports can lose interactivity.

Inspect all slides for a new deck, redesign, or export-wide change; for a local
edit, inspect affected slides and their continuity. Check evidence and explanation,
labels, source/caveat visibility, overflow, assets, fonts, code, notes, links,
contrast, and static meaning. Repair issues caused by the work and rerun affected
checks. If tools are unavailable, provide the usable source and exact remaining
build/render step, clearly distinguishing it from a finished, inspected export.
