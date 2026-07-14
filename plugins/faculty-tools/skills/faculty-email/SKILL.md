---
name: faculty-email
description: "Draft university faculty emails to students, colleagues, administrators, committees, supervisors, external partners, and teaching teams, with tone and action matched to the relationship and stakes. Trigger for email drafting or revision; do not invent policy exceptions, authority, or confidential facts."
---

# Faculty Email

## Outcome

Draft university email that is clear, bounded, professional, and appropriate to
the relationship and stakes.

## Inputs And Defaults

Use the supplied thread, policy text, names, dates, and relationship context.
Infer ordinary tone and formatting choices. Ask one focused question only when
recipient authority, confidentiality, or the requested commitment materially
changes the message; otherwise use a neutral placeholder or flag the uncertainty.

## Workflow

1. Identify recipient, relationship, urgency, confidentiality, and desired
   action.
2. Choose tone: warm student support, concise administrative update, collegial
   request, firm boundary, or formal escalation.
3. State the point early. Use one email for one primary ask when possible.
4. Include necessary context without overexplaining.
5. Make next steps explicit: deadline, owner, link, meeting time, or decision
   needed.
6. For sensitive student matters, keep details minimal and avoid unnecessary
   personal or health information.
7. Check that the email does not promise policy exceptions, grades, references,
   funding, or approvals not provided by the user.

## Output

Return only the send-ready draft by default:

```markdown
Subject: <specific subject>

Dear <recipient>,

<opening context>

<main request, decision, or update>

<next step and deadline>

Best,
<sender>
```

Add a short `Notes to sender` section only when wording depends on an unresolved
policy, promise, recipient detail, or attachment.

## Completion Check

- The purpose and requested action are clear in the opening and closing.
- Names, dates, links, commitments, confidentiality, and authority match the
  supplied context.
- The draft is ready to review but is not sent or posted by the skill.

## Boundaries

Do not invent institutional policy, legal advice, grades, accommodations, or
confidential facts. For high-stakes conflict, recommend the user confirm wording
with the appropriate university office.
