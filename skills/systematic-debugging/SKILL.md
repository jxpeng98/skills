---
name: systematic-debugging
description: "Diagnose or fix bugs, failing tests, builds, and performance regressions. Use change-review for reviewing otherwise working changes."
---

# Systematic Debugging

For an explanation or diagnosis-only request, report the cause without editing.
For a repair request, including getting a failing build or workflow running,
complete the relevant fix and verification within existing authorization.

1. Read project instructions and inspect the failing path, recent changes, and
   callers of any shared code involved.
2. Define the smallest observable failure. Record the command or input,
   environment, expected result, and actual result. If it cannot be reproduced,
   state what evidence is missing instead of guessing.
3. Shorten the feedback loop and remove irrelevant variables. Preserve the
   original failure as the final check.
4. Test the most plausible falsifiable hypothesis, changing one variable at a time;
   discard hypotheses that the evidence contradicts.
5. Trace data and control flow to the earliest wrong value or assumption. Treat
   downstream errors, retries, and crashes as symptoms until shown otherwise.
6. If a fix is authorized, change the shared root cause once. Avoid broad
   refactors, speculative hardening, or unrelated cleanup.
7. Re-run the reproduction and affected checks; add a regression check only when
   existing coverage does not catch the failure. Fix failures caused by the change,
   then stop when the requested behavior works or a concrete blocker remains.
   Remove temporary instrumentation.

Return the root cause, decisive evidence, change made if any, checks run, and
remaining risk. Do not call an unrun check passed or hide a failure behind a
workaround.
