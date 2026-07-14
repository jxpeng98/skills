---
name: pr-description
description: "Draft reviewer-ready pull request or merge request descriptions, release-note summaries, and review instructions from actual diffs, commits, linked issues, and validation evidence. Trigger for PR/MR write-ups; do not invent tests, impact, screenshots, or issue links."
---

# PR Description

## Outcome

Write a reviewer-ready pull request description grounded in the actual changes.

## Workflow

1. Read repository PR guidance, then inspect the intended base/head diff, changed
   files, commit history, linked issue text, and fresh validation output when
   available. State the compared range if it is ambiguous.
2. Separate confirmed behavior from inference. Do not invent test results, issue
   numbers, screenshots, migration impact, or user impact.
3. Organize around reviewer needs: why the change exists, what behavior changed,
   how it was verified, where risk remains, and what deserves close review.
4. Include only checklist items that fit the repository. Leave an item unchecked
   unless evidence shows it is complete.
5. Keep the result paste-ready. Omit empty sections instead of filling them with
   generic text.

## Template

```markdown
## Summary

- <change>

## Motivation

<why this change exists>

## Changes

<major changes by module or behavior>

## Testing

- Ran: <commands or "Not run">
- Recommended: <reviewer checks>

## Review Focus

- <specific area>

## Risk & Rollback

<risk and mitigation>

## Checklist

- [ ] Code follows project conventions
- [ ] Tests have been added or updated
- [ ] Documentation has been updated if needed
- [ ] No sensitive data is included
- [ ] Backward compatibility has been considered
```

## Completion Check

- Every material claim is supported by the diff, issue, or validation output.
- The testing section distinguishes commands actually run from recommended
  follow-up checks.
- Review focus, risk, and rollback guidance are specific to this change.
