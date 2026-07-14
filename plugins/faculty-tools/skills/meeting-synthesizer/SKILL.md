---
name: meeting-synthesizer
description: "Synthesize university meetings, committee notes, department discussions, and teaching-team records into confirmed decisions, action items, risks, open questions, and optional follow-up messages. Trigger for minutes or decision logs; preserve uncertainty and do not invent consensus, owners, or dates."
---

# Meeting Synthesizer

## Outcome

Convert messy meeting notes into decisions, action items, risks, and a useful
follow-up record.

## Inputs And Defaults

Inspect all supplied notes, transcript segments, agenda items, and prior action
logs. Infer a concise internal record unless the user requests formal minutes or
an email. Ask one focused question only when audience or confidentiality changes
what can safely be included; otherwise label ambiguous status, owners, and dates
as `Needs confirmation`.

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

Omit the follow-up message unless requested. Preserve the organization's minute
template when one is supplied.

## Completion Check

- Decisions are separated from proposals, discussion, and inference.
- Every action has an owner, due date, and dependency, or an explicit missing
  value rather than an invented one.
- Sensitive detail is limited to what the audience needs.

## Boundaries

Do not invent consensus, owners, dates, or approvals. If notes are ambiguous,
label the item as "needs confirmation."
