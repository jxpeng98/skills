---
name: commit-message
description: "Draft Conventional Commit messages from staged or unstaged Git diffs, including split advice. Use for message generation only; do not stage, commit, or push."
---

# Commit Message

1. Read repository commit guidance and inspect the diff. Prefer staged changes;
   otherwise state which diff you used.
2. Identify the primary intent. Recommend a split when changes have independent
   purposes.
3. Choose the narrowest valid type: `feat`, `fix`, `docs`, `style`, `refactor`,
   `perf`, `test`, `build`, `ci`, `chore`, or `revert`.
4. Add a scope only when one stable module owns the change.
5. Write an imperative subject with no trailing period, under 72 characters when
   practical. Add a body or footer only when the diff supports it.

Output only the commit message unless the user asks for rationale or split advice.
Never invent issue IDs or breaking changes, and do not commit unless asked.
