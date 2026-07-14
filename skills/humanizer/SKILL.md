---
name: humanizer
description: "Humanize and polish user-authored essays, reports, university writing, professional messages, and general prose while preserving facts, meaning, and authentic voice. Trigger for robotic, generic, stiff, or AI-like wording; not for detector evasion, impersonation, or ghostwriting assessed work."
---

# Humanizer

## Outcome

Return writing that sounds like a clear, situated person rather than a generic
assistant, without changing the author's claims, evidence, identity, or level of
certainty.

## Non-Negotiables

- Preserve facts, intent, genre, audience, citations, quotations, terminology,
  commitments, caveats, and conclusions unless the user explicitly changes them.
- Never fabricate anecdotes, experience, credentials, relationships, numbers,
  quotes, sources, or sensory detail to make prose feel more human.
- Do not optimize for AI-detector scores or help evade plagiarism, academic
  integrity, moderation, or authorship checks.
- For assessed academic work, coach and lightly polish the user's own reasoning;
  do not supply missing arguments, evidence, analysis, or conclusions as if they
  were the student's work.

## Inputs And Defaults

Infer audience, channel, stakes, and tone from the text and surrounding context.
Ask one focused question only when the intended voice, permitted academic help,
or edit depth would materially change the result; otherwise proceed with these
defaults:

- Mode: `Polisher Mode` for an existing draft; `Coach Mode` when the user asks to
  learn, diagnose, or revise assessed work.
- Intensity: `standard` for ordinary prose, `light` for assessed academic work,
  and `deep` only when the user authorizes restructuring.
- Direction: general writing unless the text is an essay, report, coursework,
  academic section, or other evidence-led university writing.

## Workflow

1. Identify mode, intensity, audience, genre, desired result, and any explicit
   length or structure constraint.
2. Create a protected-content ledger for names, numbers, dates, citations,
   quotations, claims, methods, findings, caveats, commitments, and domain terms.
   Flag a suspected error as `Needs verification`; do not silently correct it.
3. Load only the relevant guidance:
   - Read `references/academic-editing.md` for academic, coursework, or
     section-specific editing.
   - Read `references/style-diagnostics.md` for deep edits or requests to sound
     less robotic, generic, formulaic, or AI-like.
4. Diagnose the smallest set of issues that blocks the desired voice: logic,
   emphasis, paragraph purpose, sentence rhythm, register, repetition, vague
   abstraction, or process language left in the draft.
5. Edit at the chosen intensity. Prefer specific nouns and verbs, plain
   transitions, varied but natural sentence shapes, and wording already supported
   by the user's context.
6. Audit the revision against the protected-content ledger and the requested
   genre, length, structure, and force.

## Output

- For a quick polish, return only the revised text when requested.
- For `Polisher Mode`, lead with the revision; add brief notes only for a material
  change or an item needing confirmation.
- For `Coach Mode`, provide the diagnosis, 1-3 revision priorities, targeted
  revisions or examples, why they help, and decisions the author must make.
- For a `deep` edit, summarize structural changes and what was preserved.

## Completion Check

- The revision retains the author's meaning, evidence, uncertainty, and voice.
- No claim is broader, more confident, more promotional, or more personal than
  the source supports.
- Filler and generic assistant phrasing are reduced without replacing them with
  forced slang, fake vulnerability, ornate synonyms, or unnecessary formality.
- Any unresolved factual, citation, authorship, or policy issue is visible.
