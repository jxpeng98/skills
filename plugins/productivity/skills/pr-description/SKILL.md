---
name: pr-description
description: "Draft reviewer-ready pull request or merge request descriptions from diffs, commits, linked issues, and actual validation evidence. Use for description text only; do not create or publish the PR."
---

# PR Description

Use the requested language and write for a reviewer seeing the change for the
first time. Use the repository's terminology and name the affected behavior.

1. Read repository PR guidance and inspect the intended base/head diff, commits,
   linked issue, and validation output. State the range if ambiguous.
2. Explain the reason for the change, affected behavior, and reviewer decisions.
   Include material compatibility, migration, or rollback details when supported.
3. Give checks run and observed results. Label proposed checks and unresolved
   impact so a reviewer can act on them. Leave checklist items unchecked unless
   supported by evidence. Never invent tests, issue IDs, or screenshots.

Return a paste-ready description in the required template. Where no template
applies, choose useful sections from Summary, Motivation, Changes, Testing,
Review Focus, Risk & Rollback, and Checklist.
