---
name: pr-description
description: Use when the user asks for a pull request description, merge request description, release note draft, reviewer instructions, or a structured summary of code changes for review.
---

# PR Description

## Purpose

Write a reviewer-ready pull request description grounded in the actual changes.

## Workflow

1. Inspect the diff, changed files, linked issue text, and test output when available.
2. Separate confirmed facts from assumptions. Do not invent test results, issue numbers, screenshots, or user impact.
3. Summarize by reviewer concern: what changed, why it changed, how it was verified, and where risk remains.
4. Keep the description concise enough to paste into GitHub or GitLab.

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
