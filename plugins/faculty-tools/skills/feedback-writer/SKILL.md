---
name: feedback-writer
description: "Write evidence-based, constructive feedback on student essays, reports, assignments, drafts, presentations, reflections, and project work, tied to the prompt or rubric when available. Trigger for formative or summative feedback; do not invent grades, evidence, or student characteristics."
---

# Feedback Writer

## Outcome

Write feedback that helps students understand what worked, what to improve, and
what concrete next step to take.

## Inputs And Defaults

Inspect the student's work, task prompt, rubric, and instructor notes before
making evaluative claims. If the work itself is missing, request it rather than
fabricating evidence. Infer a supportive, direct tone and prioritize the few
changes with the highest learning value. Ask only when grade status or feedback
purpose would materially change the output.

## Workflow

1. Inspect the student's work, prompt, rubric, and any instructor notes before
   writing feedback.
2. Separate task performance from the student's identity or intent.
3. Lead with the highest-value strengths and the 1-3 most important improvements.
4. Tie comments to evidence in the work: argument, structure, source use,
   method, analysis, clarity, or presentation.
5. Give actionable revision advice: what to change, where to change it, and why.
6. Match stakes: concise for routine feedback, more detailed for major drafts or
   struggling students.
7. Preserve institutional and instructor voice. Do not add grades, penalties, or
   accommodations unless supplied.

## Output

Use this structure:

```markdown
## Overall Feedback

<balanced summary tied to the assignment goal and desired result>

## What Is Working

- <specific evidence>

## Priority Improvements

- <issue>: <why it matters> -> <next action>

## Revision Plan

1. <first concrete step>
2. <second concrete step>

## Optional Margin Comments

- <location>: <comment>
```

Use the instructor's required format when one exists. For short work, return a
compact paragraph plus priority actions instead of forcing every section.

## Completion Check

- Each praise or criticism points to observable evidence in the submitted work.
- Priority improvements explain what to change, where, and why.
- Tone addresses the work rather than diagnosing the student, and no grade or
  policy consequence is added without authority.

## Boundaries

Do not diagnose ability, motivation, language background, disability, or personal
circumstances. Do not fabricate rubric alignment, grades, or evidence not shown
in the student's work.
