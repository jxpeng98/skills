---
name: systematic-debugging
description: "Diagnose bugs, failing tests, build failures, unexpected behavior, or performance regressions with reproducible evidence and a root-cause fix. Use for diagnosis or repair; use change-review for review-only requests."
---

# Systematic Debugging

Respect the requested scope: diagnose only unless the user also asks for a fix.

1. Read project instructions and inspect the failing path, recent changes, and
   callers of any shared code involved.
2. Define the smallest observable failure. Record the command or input,
   environment, expected result, and actual result. If it cannot be reproduced,
   state what evidence is missing instead of guessing.
3. Shorten the feedback loop and remove irrelevant variables. Preserve the
   original failure as the final check.
4. Rank one to three falsifiable hypotheses. Test one variable at a time and
   discard hypotheses that the evidence contradicts.
5. Trace data and control flow to the earliest wrong value or assumption. Treat
   downstream errors, retries, and crashes as symptoms until shown otherwise.
6. If a fix is authorized, change the shared root cause once. Avoid broad
   refactors, speculative hardening, or unrelated cleanup.
7. Re-run the minimal reproduction, the relevant existing checks, and one small
   regression check. Remove temporary instrumentation.

Return the root cause, decisive evidence, change made if any, checks run, and
remaining risk. Do not call an unrun check passed or hide a failure behind a
workaround.
