---
name: assignment-brief
description: "Create or improve university assignment prompts, essay and report briefs, submission requirements, grading criteria, rubrics, and student-facing task descriptions. Trigger for assessment design or brief revision; preserve supplied course policy and mark missing policy decisions instead of inventing them."
---

# Assignment Brief

## Outcome

Create student-facing assignment instructions that make the task, standards,
scope, and deliverables concrete.

## Inputs And Defaults

Inspect the syllabus, learning outcomes, existing brief, rubric, and policy text
when available. Infer low-risk presentation choices and proceed. Ask one focused
question only when a missing decision would materially change the assessment;
otherwise mark it `[Instructor to confirm]`. If the user wants an interactive
design review, resolve one highest-impact decision at a time and recommend a
default with each question.

## Workflow

1. Identify the assignment type: essay, report, presentation, reflection,
   project, lab, portfolio, or exam alternative.
2. State the learning purpose in plain language before listing requirements.
3. Define deliverables: format, length, sources or materials, file type,
   deadline, collaboration rules, and submission location.
4. Write task steps students can follow without hidden assumptions.
5. Build a rubric with observable criteria, not vague traits. Include weighting
   if provided.
6. Add academic integrity guidance: allowed help, citation expectations,
   collaboration boundaries, and what must be the student's own work.
7. Include a short checklist students can use before submission.

## Output

Use this structure:

```markdown
## Assignment Goal

<goal and desired result>

## Task

<student-facing prompt>

## Deliverables

- <format, length, due date, submission method>

## Requirements

- <source, method, evidence, citation, collaboration rule>

## Rubric

| Criterion | Excellent | Satisfactory | Needs Work |
| --- | --- | --- | --- |
| <criterion> | <observable evidence> | <observable evidence> | <observable evidence> |

## Submission Checklist

- [ ] <student check>
```

Adapt the structure to the institution's existing template. Omit sections that
do not apply; do not fill unknown policy fields with plausible defaults.

## Completion Check

- A student can identify the task, required evidence, deliverables, constraints,
  submission route, and basis of evaluation without hidden assumptions.
- Rubric criteria are observable and align with the stated learning outcomes.
- All dates, weights, penalties, and AI/collaboration rules are supplied or
  clearly marked for instructor confirmation.

## Boundaries

Do not invent course policies, late penalties, AI-use rules, or grading weights.
If they are not provided, mark them as instructor decisions.
