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

1. Clarify the direction and mode. If the task direction is underspecified, use
   `grill-me` before rewriting: ask for goal, audience, desired result,
   constraints, whether this is General Writing Direction or Academic Writing
   Direction, and whether the user wants coaching notes or a polished version.
2. Identify the writing context: essay, report, email, statement, post,
   application text, feedback, or personal note.
3. Preserve claims, facts, commitments, caveats, citations, and technical
   meaning.
4. Improve the path of thought: paragraph order, sentence logic, transitions,
   emphasis, and reader expectations.
5. Replace generic or awkward phrasing with plain, specific language from the
   user's own context.
6. For university writing, keep an appropriate academic register: precise,
   direct, and evidence-aware, not grand or artificially native-sounding.
7. If authenticity depends on details the user has not provided, ask for those
   details or leave a clear placeholder.

## Output

For quick polishing, output only the revised text if the user asks for that.

For Coach Mode, include:

- Revised text or targeted excerpts
- What changed
- Why it improves clarity or argument flow
- Remaining issues the writer should decide
- Academic integrity notes when the text is assessed work

For Polisher Mode, include:

- Revised text
- Key edits made
- Meaning or evidence that needs user confirmation

Use these combinations:

- General + Coach: diagnose audience and channel fit, tone, emphasis, and
  clarity; explain the most useful revision moves.
- General + Polisher: return a cleaner version with smoother flow and plain,
  natural wording.
- Academic + Coach: diagnose argument, evidence, structure, and academic
  register; teach the writer what to revise and why.
- Academic + Polisher: improve sentence flow, paragraph logic, transitions, and
  academic tone without inventing claims, evidence, citations, or conclusions.

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

## University Writing Checks

For essay and report work, check:

- Does each paragraph have a clear job?
- Does the evidence support the claim being made?
- Are transitions showing logic, not just adding signposts?
- Is the tone appropriately academic without being inflated?
- Are citations, data, and examples preserved exactly as supplied?
- Does the revised version still sound like the user's own thinking?
