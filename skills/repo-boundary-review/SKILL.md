---
name: repo-boundary-review
description: "Review changed files for ownership and placement across canonical skill sources, plugin roots, generated mirrors, drafts, and marketplace catalogs. Use for findings, not file moves or release approval."
---

# Repo Boundary Review

Read repository ownership guidance and inspect changed and untracked files.
Identify the canonical source, generated mirrors, installable plugin roots,
drafts, and external marketplace repository.

Flag:

- marketplace catalogs or skill sources in the wrong repository;
- plugin manifests outside plugin directories;
- unpublished drafts mixed into release content;
- local paths, machine configuration, secrets, or private data;
- unnecessary third-party bundles or duplicated references;
- generated `skills/` content that differs from its plugin source.

Lead with findings by severity. For each, give the path, violated ownership rule,
and smallest fix. Do not mutate files during a review-only request, and never
reproduce secret values.
