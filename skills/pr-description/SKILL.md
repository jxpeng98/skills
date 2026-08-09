---
name: pr-description
description: "Draft reviewer-ready pull request or merge request descriptions from diffs, commits, linked issues, and actual validation evidence. Use for description text only; do not create or publish the PR."
---

# PR Description

1. Read repository PR guidance and inspect the intended base/head diff, commits,
   linked issue, and validation output. State the range if ambiguous.
2. Explain why the change exists, what changed, how it was verified, remaining
   risk, and what deserves close review.
3. Separate facts from inference. Never invent tests, issue IDs, screenshots,
   migration impact, or user impact.
4. Omit empty or generic sections. Leave checklist items unchecked unless
   evidence proves them complete.

Return a paste-ready description with only useful sections from: Summary,
Motivation, Changes, Testing, Review Focus, Risk & Rollback, and Checklist.
