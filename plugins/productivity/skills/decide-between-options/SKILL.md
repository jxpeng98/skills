---
name: decide-between-options
description: Use when the user has multiple approaches, tools, architectures, designs, vendors, workflows, or plans and needs a recommendation with explicit tradeoffs, assumptions, and decision criteria.
---

# Decide Between Options

## Purpose

Turn competing options into a concrete recommendation that the user can accept, reject, or revise.

## Workflow

1. Identify the decision, options, constraints, and irreversible consequences.
2. If the options or constraints are discoverable from files or prior context, inspect that evidence before asking.
3. Choose 3-6 decision criteria that actually matter for this case.
4. Compare each option against those criteria.
5. Recommend one option, explain why, and state what would change the recommendation.

## Output

Use this structure:

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

If a missing fact would materially change the answer, ask one targeted question before making the recommendation.
