---
name: app-store-release
description: Prepare, audit, build, upload, distribute through TestFlight, submit, or release Apple-platform apps through App Store Connect. Use for App Store 上架, release configuration, store information and review issues. For explicit API automation, prefer app-store-connect-api when available.
---

# App Store Release

Move an app from its evidenced current state to the user's requested App Store
or TestFlight stage. Apply the same workflow to iOS/iPadOS, macOS, tvOS, visionOS,
and watchOS, adapting to the actual targets and Connect records. Preserve the
project's framework, build system, locales, distribution choices, and tooling.
For a headless release job or direct API calls, use `app-store-connect-api`
when available. Otherwise use the project's authenticated tooling.

## Establish the task

Infer these from the request, project instructions, existing release records, and
available artifacts; ask only for facts that materially block the next step:

- **Target:** developer team, app record/bundle IDs, platform and embedded targets,
  version/build, and intended distribution channel or tester group.
- **Outcome:** advice, audit, local preparation, saving Connect changes, build,
  upload, beta distribution, review submission, release, or status/rejection work.
  Combine only the stages needed for the requested outcome; uploading does not
  imply inviting testers or submitting to App Review.
- **Evidence and access:** source/configuration, candidate artifacts, metadata,
  existing checks, available tools/account roles, and applicable test constraints.
  For advice or an offline audit, use supplied evidence and label remote state
  unverified; do not require account access or create files just to answer.

Reuse existing app records, builds, drafts, and unchanged confirmed decisions.
Before Connect changes or a live status check, inspect the relevant current state.
Distinguish app-wide fields from platform/version/build-specific fields before
changing them. Never copy ownership, privacy, pricing, access, regions, or legal
attestations from an unrelated app. Unknown is different from not applicable.

Preserve authorization already given for this target and outcome. An audit alone
authorizes no changes; local preparation alone authorizes no Connect writes. An
authorized submission does not need another confirmation just because it reaches
the final action. Complete independent work while a material fact is unresolved.

## Choose the affected work

| Task or change | Work and reference to load |
| --- | --- |
| App record, store text/media, declarations, pricing or availability | Use `references/store-information.md`. Change only the relevant fields. Metadata alone needs no new binary, though its publication may depend on version state or review. |
| Release configuration, code or packaged resources | Use `references/build-and-upload.md`. Make the needed change in the project's source of truth, then build and inspect the candidate; refresh evidence affected by the change. |
| Existing artifact, upload, replacement build or TestFlight | Use `references/build-and-upload.md`. Inspect/reuse the candidate first; perform only the requested upload, association or beta distribution. |
| Review draft, submission, rejection, release or live status | Use `references/review-and-release.md`. Resume at the observed state and stop at the requested outcome. |
| Shipped dependency notices, source delivery or replacement obligations | Use `references/open-source-distribution.md` only for applicable components and obligations. Simple attribution does not require a relinking workflow. |

Load only references needed by the task. For an end-to-end release, cover the
applicable build, store, and review work; for a narrow task, do not turn unrelated
release checks into prerequisites. For general repository/plugin release gates,
prefer `release-readiness` when available, otherwise follow the repository checks.
Handle general feature development and other distribution channels with their
own project workflows rather than applying Connect submission steps.

## Execute and verify

Use existing project scripts/CI and available supported tools or APIs; use browser
controls when needed. Do not require a particular connector, new release framework,
or local Xcode when an existing remote build or supplied artifact covers the task.
Let the user complete authentication when necessary; never recover credentials
from browser storage or put them in source, commands, or public logs.

Verify changing Apple requirements against current official documentation and the
actual platform/form: SDKs, media sizes, declarations, eligibility, and review
rules are not fixed constants. If unavailable, identify the unverified requirement
and continue work that does not depend on it.

After a write, re-fetch the record or re-open the form and verify values, media,
identifiers, and state. A disabled Save button or successful upload alone is
insufficient. Before retrying an uncertain upload, submission, or release, inspect
the remote result; do not duplicate or cancel work to clear uncertainty. Stop
dependent mutations when the result cannot be established. If the host blocks an
action, report its reason and resume after it is resolved; do not bypass the block.

## Report the reached outcome

Give the target and reached stage, relevant artifact/record link, checks actually
performed, and concrete blockers or next action. Distinguish uploaded, processing,
beta availability, selected build, saved draft, submitted, approved, and available
in the intended storefronts. Do not promise review approval or timing.

For work that changes release artifacts or remote state, update the existing
release record with relevant revision/dirty inputs, version/build, artifact hashes,
decisions and sources, checks, and observed Connect state with time/URL. Use a
concise handoff if no record exists; do not impose a new documentation structure.
Keep private reviewer details and credentials out of public materials. Separate
package inspection, runtime checks (including who performed them), and unresolved
terms assessments; none proves the others.
