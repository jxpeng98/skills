---
name: commit-message
description: Use when the user asks for a Git commit message, wants staged or unstaged changes summarized into a Conventional Commit, or needs commit scope and type chosen from a diff.
---

# Commit Message

## Purpose

Produce a precise Conventional Commit message from the actual repository changes.

## Workflow

1. Inspect the relevant diff before writing the message. Prefer staged changes when the user says the commit is ready.
2. Identify the primary intent. If the diff contains unrelated changes, call that out and recommend splitting commits.
3. Choose the most specific Conventional Commit type: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, or `revert`.
4. Add a scope only when the changed module is clear.
5. Write the subject in English, imperative mood, lowercase first word, no trailing period, and under 72 characters when practical.
6. Include a body only when it adds useful why/what context.
7. Include `BREAKING CHANGE:` or issue footers only when supported by evidence.

## Output

When the user asks only for the commit message, output only the final commit message.

When the user asks for help choosing, include:

- Selected type and scope
- Split-commit concerns
- Final commit message
