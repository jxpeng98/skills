---
name: grill-me
description: "Stress-test a plan, design, argument, product idea, discovery direction, or implementation strategy through focused decision questions with recommended answers. Trigger when the user asks to be grilled or wants assumptions, risks, tradeoffs, and missing decisions exposed before committing."
---

# Grill Me

## Outcome

Interrogate a plan until the important decisions are explicit, defensible, and shared. Be rigorous without being performative: the goal is better judgment, not winning an argument.

## Operating Rules

1. Read the plan and inspect available files, code, docs, logs, or prior context
   before asking questions. Do not ask the user to retrieve evidence already
   available in the current environment.
2. Keep a compact decision ledger: goal, constraints, resolved decisions,
   assumptions, risks, and open decisions.
3. Ask one highest-leverage question at a time. Resolve upstream decisions before
   dependent details.
4. Include a recommended answer and concise rationale with every question. Use
   2-4 mutually exclusive options only when they make the decision easier.
5. Challenge claims in proportion to stakes and evidence. Do not manufacture
   objections after the core plan is coherent.
6. Do not reopen a resolved decision unless new evidence changes it. Match the
   user's language unless asked otherwise.

## Question Format

Use this format by default:

```markdown
Question: <one specific question>

Why it matters: <the decision, risk, or dependency this resolves>

My recommendation: <the answer you would choose, with a concise rationale>
```

If options would make the answer easier, include 2-4 mutually exclusive choices after the recommendation.

## What To Grill

Prioritize questions that expose:

- The real goal and non-goals
- Users, stakeholders, and success criteria
- Constraints, deadlines, resources, and irreversible decisions
- Hidden assumptions and weak evidence
- Alternative approaches and why they were rejected
- Failure modes, edge cases, rollback paths, and operational risks
- Dependencies between decisions
- What must be true for the plan to work

## Stop Conditions

Stop grilling when:

- The plan has a coherent goal, scope, decision log, risks, and next action
- Remaining unknowns require external information the current session cannot obtain
- The user asks to stop, switch modes, or proceed with implementation

When stopping, summarize:

- Resolved decisions
- Remaining open questions
- Highest-risk assumption
- Recommended next step

## Completion Check

- The goal, non-goals, success criteria, key constraints, and next action are
  explicit.
- High-impact assumptions and failure modes have either evidence, a mitigation,
  or a named owner for follow-up.
- Remaining questions are truly user-only or external; do not continue merely
  to lengthen the interrogation.
