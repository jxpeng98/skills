---
name: repo-boundary-review
description: "Review changed files for correct placement across a skills repository, plugin directories, draft areas, generated mirrors, and a separate marketplace catalog. Trigger for repository-boundary, packaging, or marketplace-layout questions; report findings without moving files unless asked."
---

# Repo Boundary Review

## Outcome

Check whether repository changes belong in the skills repository, a plugin directory, a draft area, or a separate marketplace catalog.

## Workflow

1. Read repository boundary guidance and inspect the actual changed and untracked
   files before judging placement.
2. Identify the source of truth, generated mirrors, installable plugin roots,
   draft locations, and external marketplace repository.
3. Compare each questionable file with those ownership rules. Distinguish a
   boundary violation from an ordinary packaging or sync failure.
4. Lead with actionable findings. Do not move, delete, publish, or rewrite files
   during a review-only request.

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

## Completion Check

- Every finding names a real file and a documented ownership rule.
- Generated and canonical copies are not mistaken for two independent sources.
- Secrets or private data are called out without reproducing their contents.
