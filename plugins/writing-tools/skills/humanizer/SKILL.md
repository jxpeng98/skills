---
name: humanizer
description: Use when the user wants text to sound more natural, human, conversational, warm, direct, less robotic, less generic, less stitched together, or closer to a specific authentic voice while preserving meaning and truthfulness.
---

# Humanizer

## Purpose

Make writing feel like it came from a thoughtful person in a specific situation. Preserve the user's meaning, facts, and intent while improving rhythm, coherence, specificity, and voice.

Core principle: human writing has a through-line. Do not just swap words, add warmth, or sprinkle details. Make each sentence lead naturally to the next.

## Boundaries

Do not help with:

- Evading AI detectors, plagiarism checks, academic integrity systems, or platform moderation
- Faking lived experience, credentials, identity, relationships, or first-hand knowledge
- Adding fabricated anecdotes, numbers, quotes, citations, sensory details, or personal memories
- Making deceptive, manipulative, or impersonated writing sound more believable

If the user asks for detector evasion, reframe the task as legitimate voice editing.

## Workflow

1. Identify audience, channel, stakes, and desired voice from context.
2. Find the through-line: what the writer is trying to say, why it matters, and what the reader should understand or do next.
3. Build a detail bank from only the user's material: names, constraints, examples, dates, tradeoffs, feelings, decisions, and concrete nouns. If key details are missing, ask for them or leave a clear placeholder.
4. Rewrite around the through-line. Use cause, contrast, time, or priority to connect ideas instead of stacking unrelated sentences.
5. Replace abstract claims with earned details from the detail bank. One grounded detail is usually better than three vague embellishments.
6. Vary sentence length and paragraph shape. Let important points breathe; keep routine connective tissue short.
7. Remove assistant tells: empty transitions, generic praise, exaggerated balance, inflated certainty, filler summaries, and over-neat paragraph symmetry.
8. Read the draft for continuity: each paragraph should answer "why this next?" and each detail should support a real claim.

## Coherence Checks

Before returning the rewrite, check:

- The first sentence gives the reader a clear reason to keep reading.
- Details are attached to claims, not dropped in as decoration.
- Transitions show the relationship between ideas: because, but, after, so, for example, in practice.
- The tone matches the channel: concise for work messages, warmer for personal notes, sharper for persuasive writing.
- Nothing new is asserted unless it is present in the user's context or marked for confirmation.

## Output

For simple rewrites, output only the revised text.

When the source is thin or high-stakes, include:

- Revised text
- Meaning-preservation notes
- Details that need user confirmation

If the user asks for "more human" but gives almost no context, ask for 2-4 concrete details: audience, relationship, desired tone, and one real example or constraint.

## Style Moves

Prefer:

- Specific nouns and verbs
- Natural contractions when appropriate
- Small concrete details that come from the user's context
- Plain transitions that explain how ideas connect
- A clear point of view without overexplaining it
- Slightly uneven paragraph lengths when that matches natural emphasis

Avoid:

- "In today's fast-paced world"
- "It's important to note"
- "Delve", "leverage", "utilize", and similar default assistant diction
- Random flourishes that make the text feel patched together
- Orphaned details that do not change the reader's understanding
- Fake vulnerability, forced casualness, or invented intimacy
- Over-symmetrical paragraphs and list-like prose when the user asked for a human voice
