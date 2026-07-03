---
name: repo-boundary-review
description: Use when changes touch a skills repository, plugin layout, marketplace integration, repository boundaries, installable skill packaging, or files that may belong in a separate marketplace catalog.
---

# Repo Boundary Review

## Purpose

Check whether repository changes belong in the skills repository, a plugin directory, a draft area, or a separate marketplace catalog.

## Review Checklist

Inspect the changed files and flag:

- Marketplace catalog files copied into this repository
- Skill source copied into a marketplace repository
- Plugin manifests outside plugin directories
- Draft skills that should be promoted before publishing
- Local absolute paths or machine-specific configuration
- Secrets, tokens, cookies, certificates, or private data
- Bundled third-party content that is not clearly required
- Shared references duplicated across multiple skills
- Repository-level `skills/` files that do not match the corresponding
  `plugins/<plugin>/skills/<skill>/` source

## Output

Lead with findings by severity. For each finding include:

- File path
- Problem
- Why it violates the repository boundary
- Concrete fix

If no boundary issues are found, say so and list any remaining publishing checks.
