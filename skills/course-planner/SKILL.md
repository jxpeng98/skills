---
name: course-planner
description: "Plan university courses, weekly classes, seminars, tutorials, reading sessions, classroom activities, learning outcomes, and teaching schedules. Trigger for course or session design; preserve supplied syllabus constraints and flag unknown institutional requirements rather than guessing."
---

# Course Planner

## Outcome

Turn a course or class idea into a teachable plan with clear learning goals,
student preparation, in-class work, and follow-up.

## Inputs And Defaults

Inspect any syllabus, timetable, reading list, assessment map, and prior session
plan first. Infer low-risk teaching choices and proceed. Ask one focused question
only when a missing item such as level, duration, modality, or assessed outcome
would materially change the plan; otherwise state the assumption. Use
one-question-at-a-time decision review only when the user explicitly asks for it.

## Workflow

1. Identify the teaching context: course, week, level, class size, modality,
   time available, and required readings or materials.
2. Convert the topic into 2-4 measurable learning outcomes.
3. Split the session into preparation, opening, core activity, discussion or
   practice, synthesis, and after-class work.
4. Make activities concrete: prompt, grouping, time box, materials, and what the
   instructor checks while students work.
5. Include accessibility and workload checks: reading load, assumed knowledge,
   participation alternatives, and time required outside class.
6. If the user provides an existing syllabus, preserve its terminology,
   assessment structure, and institutional constraints.

## Output

Use this structure:

```markdown
## Teaching Goal

<goal and desired result>

## Learning Outcomes

- <students can do X>

## Session Plan

| Time | Activity | Instructor Role | Student Work |
| --- | --- | --- | --- |
| <minutes> | <activity> | <action> | <action> |

## Materials

- <reading, slide, handout, dataset, prompt>

## Follow-Up

- <homework, reflection, next-session bridge>

## Risks To Check

- <workload, prior knowledge, accessibility, timing>
```

For a single class, keep the output at session level. For a full course, add a
week-by-week map and assessment alignment only when useful.

## Completion Check

- Outcomes are observable and each activity contributes to at least one outcome.
- The timing fits the available session, including transitions and synthesis.
- Preparation, materials, workload, accessibility alternatives, and follow-up
  are explicit enough to teach from.

## Boundaries

Do not invent institutional policies, grading rules, learning disability
accommodations, or accreditation requirements. Ask for them or mark them as
needing confirmation.
