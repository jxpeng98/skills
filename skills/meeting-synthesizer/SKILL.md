---
name: meeting-synthesizer
description: Use when summarizing university meetings, committee notes, department discussions, teaching-team meetings, action items, decisions, and follow-up emails.
---

# Meeting Synthesizer

## Purpose

Convert messy meeting notes into decisions, action items, risks, and a useful
follow-up record.

## Before Drafting

Use `grill-me` when the goal, desired result, audience, confidentiality level, or
decision status is unclear. Ask whether the output is private notes, minutes, a
follow-up email, or a decision log.

## Workflow

1. Identify meeting type, participants or roles, date, and intended audience.
2. Separate confirmed decisions from discussion points, proposals, and open
   questions.
3. Extract action items with owner, due date, dependency, and next checkpoint.
4. Preserve uncertainty: mark unresolved items instead of smoothing them into
   decisions.
5. Remove irrelevant chatter while keeping rationale that explains why a
   decision was made.
6. Avoid sensitive personal details unless they are necessary and already in the
   provided notes.
7. For follow-up emails, keep the message short and focused on decisions and
   next actions.

## Output

Use this structure:

```markdown
## Meeting Goal

<goal and desired result>

## Decisions

- <decision> - rationale: <why>

## Action Items

| Owner | Task | Due | Dependency |
| --- | --- | --- | --- |
| <owner> | <task> | <date> | <dependency> |

## Open Questions

- <question>

## Follow-Up Message

<email-ready summary if requested>
```

## Boundaries

Do not invent consensus, owners, dates, or approvals. If notes are ambiguous,
label the item as "needs confirmation."
