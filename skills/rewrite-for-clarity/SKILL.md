---
name: rewrite-for-clarity
description: "Rewrite, edit, tighten, or adapt supplied text for clarity, directness, professionalism, tone, channel, or audience while preserving meaning, facts, commitments, and level of force. Trigger for a cleaner version of existing prose; do not add unsupported claims or silently change intent."
---

# Rewrite For Clarity

## Outcome

Improve text while preserving the user's intended meaning, audience, and level of force.

## Inputs And Defaults

Infer audience, medium, tone, and length from context. Ask one focused question
only when an ambiguity would materially change meaning or stakes; otherwise use
a direct, professional tone and preserve the source structure when it is useful.

## Workflow

1. Identify the requested outcome and protect facts, commitments, caveats,
   quotations, citations, technical meaning, and degree of certainty.
2. Fix the information order before polishing sentences: put the point, request,
   decision, or conclusion where the reader needs it.
3. Remove filler, vague phrasing, repeated ideas, unnecessary hedging, and
   process language that does not belong in the artifact.
4. Adapt vocabulary, sentence length, and formality to the audience without
   making the text more promotional, warmer, firmer, or more certain than asked.
5. Do not add claims, numbers, names, promises, examples, or policy details that
   are absent from the source.

## Output

For short text, provide only the rewrite unless the user asks for explanation.

For important or sensitive text, include:

- Rewrite
- What changed
- Any meaning that may need user confirmation

## Completion Check

- Source and revision make the same factual claims and commitments.
- The main point is easier to find, references are unambiguous, and unnecessary
  words are removed.
- Material ambiguity is surfaced rather than resolved by invention.
