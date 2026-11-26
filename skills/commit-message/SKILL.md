---
name: commit-message
description: "Draft a Conventional Commit message from a Git diff, either on its own or as part of an authorized commit task."
---

# Commit Message

Use the language required by repository guidance. Name the behavior or artifact
that changed so the subject makes sense in Git history on its own.

1. Read repository commit guidance and inspect the diff. Prefer staged changes;
   otherwise state which diff you used.
2. Identify the primary intent. Recommend a split when changes have independent
   purposes.
3. Choose the narrowest valid type: `feat`, `fix`, `docs`, `style`, `refactor`,
   `perf`, `test`, `build`, `ci`, `chore`, or `revert`.
4. Add a scope only when one stable module owns the change.
5. Write an imperative subject with no trailing period, under 72 characters when
   practical. When the reason or compatibility impact is important, explain it
   in the body using the supplied evidence. Add footers only when supported.

Check the final message against the actual diff and repository format.

For a message-only request, return the message without changing Git state; include
rationale or split advice only when requested. Within an authorized commit task,
use the message and continue that task. Message generation does not grant new
permission to stage, commit, or push. Never invent issue IDs or breaking changes.
