---
name: release-readiness
description: "Verify release readiness for skill, plugin, repository, or marketplace changes using fresh validation and packaging evidence. Use for readiness gates; never tag, push, publish, or count unrun checks as passed."
---

# Release Readiness

Use the language required by the user, audience, or repository. Prefer common
words and familiar sentence patterns. Keep needed technical terms, but do not add
formal or corporate wording just to sound polished.

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

Return `Ready` or `Not ready`, blockers, checks run, remaining risks, and the next
step. Do not publish, tag, or push unless explicitly asked.
