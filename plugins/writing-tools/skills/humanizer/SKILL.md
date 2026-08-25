---
name: humanizer
description: "Polish user-authored writing when natural voice, specificity, or robotic phrasing is the problem. Preserve facts and authorship; use rewrite-for-clarity for direct clarity or tone edits, never for detector evasion."
---

# Humanizer

Preserve facts, claims, intent, genre, audience, citations, quotations,
terminology, commitments, caveats, and conclusions. Never fabricate experience,
credentials, relationships, numbers, sources, or detail. Do not help evade AI,
plagiarism, authorship, or moderation checks. For assessed work, coach or lightly
polish the user's reasoning; do not supply missing intellectual work.

Defaults:

- `Polisher Mode` for an existing draft; `Coach Mode` when the user asks to learn
  or the work is assessed.
- A humanizing request authorizes sentence and within-paragraph reconstruction,
  not just synonym swaps. Use `light` editing for assessed work; reserve `deep`
  editing for reordering ideas or paragraphs.

Choose the voice anchor in this order: a supplied sample or stated preference,
the writer's natural phrasing elsewhere in the draft, the relationship and
genre, then plain contemporary language. Match the source language, regional
variety, and punctuation conventions unless translation is requested. Do not
preserve robotic patterns merely because they appear in the source, and do not
invent quirks to simulate a person.

1. Identify audience, genre, desired result, mode, intensity, and fixed length or
   structure.
2. Protect names, numbers, dates, citations, claims, methods, findings, caveats,
   commitments, and domain terms. Flag suspected errors as `Needs verification`.
3. Read `references/academic-editing.md` for academic or coursework editing.
   Read `references/style-diagnostics.md` only for deep or robotic/generic style
   problems.
4. Identify each paragraph's job and essential content. Rewrite from that meaning
   rather than editing the original sentence frame word by word. Restore protected
   facts and necessary terminology after the sentence sounds natural.
5. Cut generic setup, repeated conclusions, decorative transitions, and sentences
   that add no fact, implication, feeling, or action. Let sentence and paragraph
   length follow the thought instead of forcing polished symmetry.
6. Read the revision as continuous prose. Compare it with the source for meaning,
   evidence, certainty, voice, genre, length, and structure; rewrite any passage
   that still sounds reusable in an unrelated document.

For quick polish, return only the revision. In `Polisher Mode`, add notes only
for material changes or uncertainties. In `Coach Mode`, give 1-3 priorities,
targeted revisions, reasons, and author decisions. Avoid forced slang,
fragments, vulnerability, ornate synonyms, deliberate mistakes, or unsupported
confidence.
