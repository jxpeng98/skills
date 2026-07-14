---
name: decide-between-options
description: "Compare competing approaches, tools, architectures, designs, vendors, workflows, or plans and recommend one using explicit criteria, evidence, tradeoffs, assumptions, and reversal conditions. Trigger when the user needs a decision rather than a neutral list of options."
---

# Decide Between Options

## Outcome

Turn competing options into a concrete recommendation that the user can accept, reject, or revise.

## Workflow

1. State the decision, viable options, hard constraints, time horizon, and costly
   or irreversible consequences.
2. Inspect available files, prior context, and current authoritative sources when
   the decision depends on them. Ask only for a missing fact that would
   materially change the recommendation; otherwise state a reasonable
   assumption and proceed.
3. Select 3-6 decision criteria that distinguish the options. Weight them only
   when weighting changes the result.
4. Compare options against the same criteria. Separate observed evidence from
   inference and unknowns.
5. Recommend one option, name its main cost, and state the evidence or condition
   that would reverse the choice.

## Output

Lead with the recommendation. Use this structure when it improves scanability:

```markdown
Recommendation: <option>

Why: <concise rationale>

Tradeoffs:
- <option>: <strengths, weaknesses, risks>

Assumptions:
- <assumption>

What would change my mind:
- <condition or evidence>
```

For a simple decision, omit empty sections and answer in a compact paragraph.

## Completion Check

- The recommendation follows from the stated criteria rather than preference or
  option order.
- Material uncertainty, switching costs, and downside risk are visible.
- The user can tell both what to choose now and what new evidence would change
  the decision.
