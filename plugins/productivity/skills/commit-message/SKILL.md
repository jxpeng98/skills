---
name: commit-message
description: "Generate evidence-grounded Conventional Commit messages from staged or unstaged Git diffs, including type, optional scope, breaking-change footers, and split-commit advice. Trigger for commit-message drafting or commit type/scope selection; do not create the commit unless explicitly asked."
---

# Commit Message

## Outcome

Produce a paste-ready Conventional Commit message whose claims are supported by
the actual repository changes.

## Workflow

1. Read repository guidance that defines commit conventions, then inspect the
   relevant diff. Prefer the staged diff when staged changes exist or the user
   says the commit is ready; otherwise inspect the unstaged diff and state the
   scope used.
2. Identify the primary intent, not merely the largest changed file. If the diff
   mixes independent intents, recommend the smallest sensible commit split.
3. Choose the most specific type: `feat`, `fix`, `docs`, `style`, `refactor`,
   `perf`, `test`, `build`, `ci`, `chore`, or `revert`.
4. Add a scope only when one stable module, package, or domain clearly owns the
   change.
5. Write an imperative subject with no trailing period and keep it under 72
   characters when practical. Follow repository language conventions; default
   to English only when no convention or user preference is available.
6. Add a body only when the reason, behavior change, migration note, or split
   rationale would help a future reader.
7. Add `BREAKING CHANGE:` and issue footers only when the diff or supplied
   context supports them.

## Output

When the user asks only for the commit message, output only the final commit message.

When the user asks for help choosing, include:

- Selected type and scope
- Split-commit concerns
- Final commit message

## Completion Check

- Every subject/body claim is traceable to the inspected diff or supplied issue.
- The type describes intent, the scope is not guessed, and no issue ID or
  breaking change is invented.
- Do not stage, commit, amend, or push unless the user explicitly requests it.
