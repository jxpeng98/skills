# Review, release, and recovery

Use the current [submission flow](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app/)
and [review guidelines](https://developer.apple.com/app-store/review/guidelines/)
for the actual platform and submission type. For an audit, report the relevant
gaps without executing these actions. For a status request, inspect the record
and report its state without starting a new release checklist.

## Prepare and submit

1. Open the intended platform/version and verify the exact processed build and
   export-compliance state. Check applicable metadata/media, review access,
   contact details, privacy publication, age rating, content rights, pricing,
   territories, and release mode. Resolve actual account restrictions. Include
   purchases, subscriptions, or other review items only when the app uses them
   and their current requirements are satisfied.
2. Save and verify changed fields and build association. Use **Add for Review**
   (or its supported API equivalent) only when preparing a review draft is in
   scope. Inspect all items in the resulting draft. This prepares a submission;
   it does not send it to Apple.
3. Before **Submit for Review**, match the draft to the intended platform,
   version/build and existing authorization. Inspect any new required attestation
   or agreement under the host's approval rules. If a fact or approval is missing,
   present the completed draft and the exact outstanding question.
4. Submit when authorized, then verify the resulting submission record and status.
   Record its ID/URL, version/build, and time. Report **Waiting for Review** or
   **In Review** only when that state is observed. An enabled control or successful
   request alone does not establish the resulting state.

## Rejection and replacement

Read Apple's actual message, affected item, and current submission state. Separate
metadata/review-access fixes from binary defects; a rejection does not always
require a new build. Correct the cited issue and refresh only affected evidence.
Draft replies from verified facts; send a reply only when authorized.

If replacement is needed, follow [build-and-upload.md](build-and-upload.md) and inspect whether the
current state permits changing the association. Cancelling an active review,
withdrawing items, or expiring a beta is a separate consequential action; do it
only when within the requested recovery scope. Preserve unaffected draft items
and stop if the intended replacement cannot be identified reliably.

## Approval and availability

Follow the confirmed [version release option](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option):
manual release requires its authorized action; automatic or scheduled release
requires observing the resulting availability. Check any chosen phased rollout
against its current eligibility and status. Do not change release mode, regions,
or other platforms merely to make one version appear complete.

Approval is not proof of availability in every intended storefront. Inspect
Connect and the relevant product-page/availability result and report any pending
propagation or restrictions. If an upload, submission, or release remains pending,
report that state and a concrete next check. Schedule monitoring only when asked
and supported; a one-time status request does not authorize an ongoing monitor.
