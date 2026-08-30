---
name: change-review
description: "Review a branch, pull request, commit range, or working-tree diff for request fidelity and behavior, regression, compatibility, and maintainability risks. Return findings only; use repo-boundary-review for file ownership and placement."
---

# Change Review

Review only. Do not edit files, commit, push, or approve a release unless the
user separately asks for that action.

1. Fix the comparison point before reviewing: the requested base, merge base,
   parent commit, staged diff, or current working tree. State it when ambiguous.
2. Read repository guidance and the actual request, issue, or acceptance criteria.
   Mark unavailable requirements as unknown rather than inventing intent.
3. Inspect the complete diff and the affected callers, tests, schemas, public
   interfaces, and platform boundaries.
4. Review on two separate axes:
   - request fidelity: missing behavior, wrong scope, unintended scope, or a
     result that does not meet the stated acceptance criteria;
   - implementation risk: correctness, regression, compatibility, security at
     trust boundaries, error handling, and meaningful test coverage.
5. Report only actionable findings introduced or exposed by the change. Skip
   style preferences and issues an enforced formatter or linter already settles.

Order findings by severity. For each one, give a tight file and line location,
the evidence, likely impact, and smallest credible correction. If there are no
findings, say so and name any material checks or environments not covered.
