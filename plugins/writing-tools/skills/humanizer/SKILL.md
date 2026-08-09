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
- `standard` editing for ordinary prose, `light` for assessed work, and `deep`
  only when restructuring is authorized.

1. Identify audience, genre, desired result, mode, intensity, and fixed length or
   structure.
2. Protect names, numbers, dates, citations, claims, methods, findings, caveats,
   commitments, and domain terms. Flag suspected errors as `Needs verification`.
3. Read `references/academic-editing.md` for academic or coursework editing.
   Read `references/style-diagnostics.md` only for deep or robotic/generic style
   problems.
4. Fix the smallest set of problems in logic, emphasis, paragraph purpose,
   rhythm, register, repetition, or vague wording.
5. Compare the revision with the source for meaning, evidence, certainty, voice,
   genre, length, and structure.

For quick polish, return only the revision. In `Polisher Mode`, add notes only
for material changes or uncertainties. In `Coach Mode`, give 1-3 priorities,
targeted revisions, reasons, and author decisions. Avoid forced slang,
vulnerability, ornate synonyms, or unsupported confidence.
