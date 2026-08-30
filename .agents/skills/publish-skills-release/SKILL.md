---
name: publish-skills-release
description: "Publish a version of this skills repository after the user explicitly asks to release it. Validate, package, commit, tag, push, wait for GitHub Actions, and verify release assets without rewriting history."
---

# Publish Skills Release

This is a repository-local maintenance skill. Do not copy it into a public
plugin or the generated `skills/` mirror.

1. Read `DEVELOPMENT.md`, `.github/workflows/release.yml`, current manifests,
   Git status and diff, the latest tag, and the remote before changing release
   state.
2. Confirm the intended files and semantic version. If the requested release
   level is genuinely ambiguous, ask before changing every plugin version or tag.
3. Update only the manifests that belong to the released plugin versions. Sync
   the Hermes mirror with `python scripts/sync_hermes_tap.py`.
4. Run `python scripts/validate_plugins.py`, the repository tests,
   `git diff --check`, and `python scripts/package_plugins.py --output dist`.
   Inspect the archives, expected asset list, and `checksums.txt`; smoke-test an
   extracted archive rather than only the source tree.
5. Re-read status and diff. Commit with a Conventional Commit message, create
   the requested `v*` tag, and push the branch and tag only after every release
   gate passes and the user has authorized publishing.
6. Wait for `.github/workflows/release.yml`. Verify the GitHub release exists and
   contains every per-plugin archive, `all-plugins.zip`, and `checksums.txt`.

Return the version, commit, tag, workflow result, release URL, assets, checks,
and any residual risk. Never force-push, rewrite history, delete or replace a
remote tag, publish unintended dirty files, or call a queued workflow successful.
