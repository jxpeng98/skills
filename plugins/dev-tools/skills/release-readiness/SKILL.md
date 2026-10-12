---
name: release-readiness
description: "Check skill, plugin, or repository release readiness from validation and packaging evidence, on its own or as a gate within an authorized release."
---

# Release Readiness

Report in plain language appropriate to the user and repository.

1. Read release guidance and identify the artifact, release surface, changed
   files, and version.
2. Run the cheapest relevant checks first; run broader package or install checks
   only when they add confidence.
3. Build the release artifact, then run clean-install or smoke checks from an
   extracted archive or package in a temporary location, not only from the source
   tree. Verify the expected asset list and checksums when they exist.
4. Classify results as blockers, warnings, or residual risks. A missing check is
   not a pass.
5. Re-read the final diff and status.

Check what applies:

- canonical plugin layout and synced `skills/` mirror;
- matching manifest versions and valid skill/agent metadata;
- no placeholders, secrets, local paths, or unused resources;
- fresh tests, validation, packaging, and installation evidence;
- marketplace changes live only in the marketplace repository;
- Git status contains only intended changes.

Report `Ready` or `Not ready` with blockers, checks run, and material remaining risks.
An assessment alone does not authorize publishing. When this is a gate within an
already authorized release, continue that workflow after the checks pass; do not
treat the readiness report as its completion or request the same approval again.
