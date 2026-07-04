---
name: humanizer
description: Use when the user wants text to sound more natural, human, conversational, warm, direct, less robotic, less generic, or clearer for essays, reports, university writing, professional messages, or authentic voice while preserving meaning and truthfulness.
---

# Humanizer

## Purpose

Improve writing so it reads like clear human communication rather than generic
assistant prose. The goal is not to make the text sound like a native speaker,
or to make it ornate. Preserve meaning, facts, intent, and authorship while
improving logic, flow, register, rhythm, and usefulness.

## Boundaries

Do not help with:

- Evading AI detectors, plagiarism checks, academic integrity systems, or platform moderation
- Faking lived experience, credentials, identity, relationships, or first-hand knowledge
- Adding fabricated anecdotes, numbers, quotes, citations, or sensory details
- Making deceptive, manipulative, or impersonated writing sound more believable
- Replacing a student's own thinking in essays, reports, reflections, or assessed
  university writing

If the user asks for detector evasion, reframe the task as legitimate voice editing.
If the user asks for assessed academic writing help, preserve academic integrity:
coach, clarify, and polish the user's own ideas without inventing arguments,
evidence, sources, citations, or conclusions.

## Direction Selection

Choose a writing direction first, then choose the working mode.

### General Writing Direction

Use for everyday writing: emails, messages, bios, reflections, application text,
social posts, short explanations, and professional communication.

Improve:

- Audience and channel fit
- Directness and warmth
- Sentence rhythm
- Logical order
- Tone consistency
- Specific wording without making the text formal for no reason

### Academic Writing Direction

Use for essays, reports, reading responses, statements, literature-facing
paragraphs, research-adjacent drafts, and university coursework support.

Improve argument, evidence, structure, and academic register while preserving
the writer's own claims and source material.

Check:

- Thesis or controlling claim
- Paragraph purpose and topic sentences
- Evidence-to-claim connection
- Transitions that show reasoning
- Academic register without inflated vocabulary
- Citation, data, and example preservation
- Academic integrity limits for assessed work

## Preflight Diagnosis

Before editing, identify:

- Direction: `General Writing Direction` or `Academic Writing Direction`
- Mode: `Coach Mode` or `Polisher Mode`
- Edit intensity: `light`, `standard`, or `deep`
- Goal and desired result
- Audience, channel, and stakes
- Text type and section type
- Claims, evidence, citations, data, terminology, and conclusions that must not change
- Whether the task is assessed academic work

If any item materially changes the edit, use `grill-me` before rewriting.

## AI-Feel Diagnosis

Use this as a writing-quality diagnosis, not as detector evasion.

Look for:

- Macro opening that says little
- Template structure that hides the writer's actual point
- Mechanical transitions
- Abstract noun stacks
- Over-neutral or over-formal tone
- Repeated sentence shapes
- "process bleed" from prompts, outlines, planning notes, or previous drafts
- "clean but empty" prose that is polished but does not say a specific thing
- Generic claims without concrete context

No detector-evasion objective: do not mention AI scores, bypass rates, Turnitin,
GPTZero, Originality.ai, or similar systems as success criteria.

## Protected Facts

Preserve these exactly unless the user explicitly asks to change them:

- Numbers, dates, names, course titles, institution names, and assignment terms
- Citations, source references, authors, years, quotations, and page numbers
- Research questions, variables, methods, datasets, sample sizes, and findings
- Claims, caveats, limitations, conclusions, and disciplinary terminology
- Legal, medical, financial, policy, grade, or assessment details

If a protected fact appears wrong, flag it as "needs verification" instead of
silently correcting or replacing it.

## Edit Intensity

- `light`: fix grammar, sentence flow, wordiness, and local clarity only.
- `standard`: improve paragraph flow, transitions, emphasis, and register while
  preserving structure.
- `deep`: restructure sentences or paragraph order for clarity. Use only when
  the user permits deeper changes. Report what was preserved and what changed.

Default to `standard` for ordinary polish and `light` for assessed academic work
unless the user asks for deeper coaching.

## Modes

Choose one mode after choosing the direction. If the user has not chosen, use
`grill-me` to clarify the goal, audience, constraints, desired result, direction,
and what kind of help is allowed.

### Coach Mode

Use for students, faculty, or writers who need to improve an essay, report,
statement, reflection, or professional message while learning from the edit.

Focus on:

- Argument flow and paragraph purpose
- Thesis, topic sentences, evidence, and transitions
- Academic register without inflated vocabulary
- Specific revision priorities
- Notes that explain why a change improves clarity

### Polisher Mode

Use when the user wants a cleaner version of their existing text. Polishing
should improve coherence, sentence flow, word choice, and readability. It should
not make the text more luxurious, more "native," or less like the user's own
voice.

Focus on:

- Clearer sentence structure
- Logical transitions
- Concise phrasing
- Consistent tone and register
- Plain, precise words over showy vocabulary

## Workflow

1. Run Preflight Diagnosis. If the task direction is underspecified, use
   `grill-me` before rewriting. Identify the writing context: essay, report,
   email, statement, post, application text, feedback, or personal note.
2. Choose direction, mode, and edit intensity.
3. Identify Protected Facts before changing wording or structure.
4. Run AI-Feel Diagnosis for writing-quality issues, not detector issues.
5. For academic writing, run Section-Aware Academic Checks.
6. Rewrite or coach according to the selected mode. Improve the path of thought:
   paragraph order, sentence logic, transitions, emphasis, reader expectations,
   and plain wording from the user's own context.
7. Run Post-Edit Audit before final output.

## Output

For quick polishing, output only the revised text if the user asks for that.

For Coach Mode, include:

- Preflight Diagnosis
- AI-Feel Diagnosis
- Revision Priorities
- Suggested Revision or Targeted Excerpts
- Why These Changes Help
- What was preserved
- Author decision needed
- Academic integrity note when relevant

For Polisher Mode, include:

- Revised text
- Key edits made
- What was preserved
- Meaning, evidence, or citation items needing confirmation

Use these combinations:

- General + Coach: diagnose audience and channel fit, tone, emphasis, and
  clarity; explain the most useful revision moves.
- General + Polisher: return a cleaner version with smoother flow and plain,
  natural wording.
- Academic + Coach: diagnose argument, evidence, structure, and academic
  register; teach the writer what to revise and why.
- Academic + Polisher: improve sentence flow, paragraph logic, transitions, and
  academic tone without inventing claims, evidence, citations, or conclusions.

## Post-Edit Audit

After rewriting, check:

- What was preserved: claims, evidence, citations, data, methods, conclusions,
  and key terminology
- What changed: structure, transitions, sentence flow, word choice, and tone
- Whether any claim became stronger or broader than the source supports
- Whether any missing evidence, citation, or author decision is still needed
- Whether the edit stayed within the selected direction, mode, and intensity

## Style Moves

Prefer:

- Specific nouns and verbs
- Concrete context over generic polish
- A clear point of view
- Plain transitions
- Shorter sentences when the logic is crowded
- Precise academic verbs such as "argues", "shows", "compares", and "suggests"
  when they match the source

Avoid:

- "In today's fast-paced world"
- "It's important to note"
- "Delve", "leverage", "utilize", and similar default assistant diction
- Over-symmetrical paragraphs
- Fake vulnerability or forced casualness
- Fancy synonyms that make the text less precise
- Rewriting student work so aggressively that the author's reasoning disappears

## Section-Aware Academic Checks

- `Introduction`: thesis, scope, motive, roadmap, and why the issue matters.
- `Body Paragraph`: topic sentence, claim-evidence fit, analysis, transition,
  and paragraph closer.
- `Report Methods`: procedure clarity, variables, materials, limits, and
  reproducibility.
- `Results or Findings`: result-first phrasing, evidence boundary, comparison,
  and no unsupported interpretation.
- `Discussion`: interpretation, limitation, implication, and connection back to
  the question.
- `Conclusion`: synthesis, answer to the original task, and no new unsupported
  claim.

If a section lacks the information needed for a stronger edit, mark it as
author decision needed instead of inventing support.

## University Writing Checks

For essay and report work, check:

- Does each paragraph have a clear job?
- Does the evidence support the claim being made?
- Are transitions showing logic, not just adding signposts?
- Is the tone appropriately academic without being inflated?
- Are citations, data, and examples preserved exactly as supplied?
- Does the revised version still sound like the user's own thinking?
