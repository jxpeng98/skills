---
name: summarize-material
description: "Summarize notes, articles, transcripts, documents, meeting records, or long context into a concise brief, decision record, action list, or cross-source synthesis. Trigger when the user needs compression grounded only in supplied material; preserve uncertainty, contradictions, attribution, dates, and owners."
---

# Summarize Material

## Outcome

Compress source material into useful decisions, facts, and next actions without losing uncertainty.

## Inputs And Defaults

Read all in-scope material before synthesizing. Infer the most useful structure
from the user's intended use. Ask only when audience, scope, or required length
would materially change what must be retained; otherwise lead with the core
conclusion and actions.

## Workflow

1. Identify source boundaries, source types, and the decision or use the summary
   should support.
2. Extract concrete facts, dates, names, decisions, risks, action items, and
   unresolved questions before compressing prose.
3. Separate source statements, cross-source synthesis, and inference. Preserve
   conflicts instead of forcing consensus.
4. Keep attribution when it changes meaning or accountability. Treat missing
   evidence as unknown, not as proof that something did not happen.
5. Use short quotations only when exact wording matters; otherwise paraphrase.
6. Remove repetition and background that does not change the conclusion, action,
   risk, or interpretation.

## Output Options

Choose the most useful structure:

- Executive summary
- Decisions and rationale
- Action items with owners and dates
- Risks and open questions
- Theme synthesis across multiple sources

State when the source is incomplete or when conclusions are inferred.

## Completion Check

- Every included claim is traceable to the supplied material.
- Decisions, proposals, opinions, and inferences remain distinguishable.
- Owners, dates, quantities, caveats, contradictions, and open questions survive
  compression when material.
