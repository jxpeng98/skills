---
name: course-planner
description: Use when planning university courses, weekly classes, seminars, tutorials, reading sessions, classroom activities, learning outcomes, or teaching schedules.
---

# Course Planner

## Purpose

Turn a course or class idea into a teachable plan with clear learning goals,
student preparation, in-class work, and follow-up.

## Before Drafting

Use `grill-me` when the goal, audience, constraints, or desired result is
unclear. Ask for the course level, session length, student background,
assessment link, and what students should be able to do afterward.

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

## Boundaries

Do not invent institutional policies, grading rules, learning disability
accommodations, or accreditation requirements. Ask for them or mark them as
needing confirmation.
