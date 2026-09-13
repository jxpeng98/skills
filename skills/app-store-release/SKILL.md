---
name: app-store-release
description: Prepare, audit, build, upload, or submit an iOS or iPadOS app through App Store Connect using project evidence and current Apple requirements. Use for App Store 上架, metadata, screenshots, privacy, age ratings, accessibility, export compliance, build replacement, and review submission; honor the requested stopping point. Use release-readiness for generic repository or plugin release gates.
---

# App Store Release

Move the existing app from its verified current state to the user's requested
release stage. This workflow primarily covers iOS and iPadOS; check the relevant
Apple documentation before extending it to other platforms.

## Establish scope and evidence

1. Read project instructions, build configuration, release records, store copy,
   screenshots, dependency locks, privacy files, and existing distribution scripts.
   Identify the actual workspace and preserve unrelated changes.
2. Inspect the current developer team, app record, platform, version, selected
   build, and submission state using available authorized tools. Reuse existing
   records. An uploaded build or review draft is not a new app to create.
3. Match the requested stopping point: advice, audit, prepare/save, upload, or
   submit. Earlier authorization and verified business decisions remain valid
   unless the user changes them or the underlying facts change. An audit request
   alone does not authorize submission; an authorized submission need not be
   reconfirmed merely because the workflow reaches its final button.
4. Keep a compact release record in the project's existing documentation location:
   source revision and dirty inputs, app/version/build identifiers, artifacts and
   checksums, metadata decisions and sources, checks actually run, unresolved
   blockers, and the latest observed Connect state with time and URL.
5. Resolve unknown business facts with a focused question while completing
   independent preparation. Never infer ownership, pricing, sales territories,
   team-wide access, privacy practices, or legal attestations from another app.

Prefer project tooling and supported Apple tools/APIs; use browser controls when
needed and follow their current instructions. Re-read the visible form after a
navigation or save. Do not reuse stale controls or recover login credentials from
browser storage. Let the user complete authentication when required.

## Prepare only the affected layers

| Change | Work to perform |
| --- | --- |
| Store text, review contact, age answers, privacy declaration, accessibility label, price or territories | Update the relevant Connect section and verify its saved or published state; these edits alone do not require a new binary. |
| UI changes reflected in store screenshots | Build and capture the affected flows only when authorized; check the images against the candidate UI and replace the intended media slots. |
| Code, bundled notices, icons, permission text, entitlements, frameworks or other packaged resources | Produce and validate a new build; refresh associated evidence and affected store materials. |
| New build already uploaded or selected by the user | Inspect that build and association first; do not rebuild, upload again, or reset completed metadata without a reason. |

Read `references/store-information.md` when creating the app
record or preparing metadata, screenshots, questionnaires, and availability.
Read `references/build-and-upload.md` when changing identifiers,
archiving, uploading, or selecting a replacement build.
Read `references/open-source-distribution.md` when a
shipped dependency needs attribution, source delivery, or replacement/relinking
support. Do not impose the LGPL workflow on apps without such a dependency.

## Complete the submission

Check Apple's current [submission flow](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app/)
and [review guidelines](https://developer.apple.com/app-store/review/guidelines/)
alongside the actual form. Required fields, policies, and account-specific prompts
can change; an old checklist is not authoritative.

1. Re-open the version. Verify the exact processed build, export-compliance state,
   localized metadata and media, review access/instructions, contact information,
   privacy publication, age rating, content rights, pricing, territories, and
   chosen release mode. Resolve applicable agreements or account restrictions.
   Include purchases, subscriptions, or other review items only when the app uses
   them and their current submission requirements are satisfied.
2. Save and re-read changed fields. A disabled Save button alone does not prove a
   previous edit persisted. Verify the displayed values and media counts.
3. If submission is in scope, use **Add for Review** and inspect the resulting
   draft and all included items. This step prepares a submission; it does not send
   it to Apple. Resolve concrete validation errors using project evidence.
4. Before **Submit for Review**, match the draft to the intended version/build and
   existing authorization. Inspect any actual new attestation or agreement under
   the applicable tool/host approval rules. If a required fact or approval is
   missing, present the completed draft and the exact remaining question.
5. Submit when authorized, then verify the resulting submission record and status.
   Record its ID/URL, version, build, and time. Report **Waiting for Review** when
   observed; report **In Review** only when that state is actually shown.

If an automatic approval review blocks an action, do not switch tools or methods
to bypass it. Explain the blocked action and stated reason, complete unaffected
work, and request only the missing approval. If the user completes the step,
inspect the new state and resume; do not preserve an obsolete blocker.

## Resume and report accurately

Distinguish uploaded, processing, selectable, associated with a version, saved
review draft, submitted, approved, and available for download. Inspect the actual
record before retrying an uncertain upload or submission. Do not cancel an active
review or replace its build during a status check.

For a rejection, inspect Apple's actual message and fix the cited issue before
preparing a response or replacement. For approval, follow the selected release
mode: a manual release still needs the authorized release action; automatic or
scheduled release still needs an observed availability result. Reply to Apple,
release manually, or schedule monitoring only within the user's authorization.

Report the reached stage, exact version/build, relevant record or artifact link,
checks performed, and concrete remaining blockers. Separate compilation and
package inspection from user-reported device checks, independent runtime checks,
and unresolved legal conclusions. Do not promise approval or a review deadline.
Keep credentials and private reviewer details out of public release notes,
reusable skills, screenshots, and distribution archives.
