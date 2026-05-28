---
name: grill-me
description: Use when the user wants to stress-test a plan, design, argument, product idea, discovery direction, or implementation strategy; asks to be grilled; or needs assumptions, tradeoffs, risks, and missing decisions exposed before committing.
---

# Grill Me

## Purpose

Interrogate a plan until the important decisions are explicit, defensible, and shared. Be rigorous without being performative: the goal is better judgment, not winning an argument.

## Operating Rules

1. Ask one question at a time.
2. If the answer can be found by inspecting available files, code, docs, logs, or prior conversation context, inspect that evidence instead of asking the user.
3. For every question, include your recommended answer and the reason you recommend it.
4. Keep walking the decision tree until dependencies are resolved or the next unresolved decision is clearly blocked on information only the user can provide.
5. Track resolved decisions briefly so later questions do not reopen settled ground unless new information changes the conclusion.
6. Match the user's language unless they ask otherwise.

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
