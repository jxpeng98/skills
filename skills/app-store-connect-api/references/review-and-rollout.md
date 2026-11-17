# Submit the version and follow its release

## Assemble the review draft

1. Verify the version, selected build, metadata, required declarations and
   review access. Read its `releaseType` before sending it to Apple. With
   `AFTER_APPROVAL` or `SCHEDULED`, submission can lead to public release
   without another request. Resolve any conflict with the user's release plan.
2. Read `GET /v1/reviewSubmissions` filtered by app and platform. Inspect
   `GET /v1/reviewSubmissions/{id}/items` for each relevant draft. Reuse one
   whose items match the request. If a new draft is needed, send
   `POST /v1/reviewSubmissions` with `attributes.platform` and the `app`
   relationship. Keep its submission ID.
3. Add the version once with `POST /v1/reviewSubmissionItems`. Substitute the
   two IDs in the body below. Read the items again and check every item that
   would be sent. If the draft contains other work outside the release scope,
   leave it intact and resolve which submission to use.

   ```json
   {
     "data": {
       "type": "reviewSubmissionItems",
       "relationships": {
         "reviewSubmission": {"data": {"type": "reviewSubmissions", "id": "SUBMISSION_ID"}},
         "appStoreVersion": {"data": {"type": "appStoreVersions", "id": "VERSION_ID"}}
       }
     }
   }
   ```

4. A draft request ends here. To send the authorized submission to Apple, issue
   `PATCH /v1/reviewSubmissions/{id}` with the following body. Read the same
   submission back. Report `WAITING_FOR_REVIEW` or `IN_REVIEW` when observed.

   ```json
   {
     "data": {
       "type": "reviewSubmissions",
       "id": "SUBMISSION_ID",
       "attributes": {"submitted": true}
     }
   }
   ```

If the request times out, read the submission and its items. A state of
`WAITING_FOR_REVIEW` or `IN_REVIEW` means Apple already has the submission.

For `UNRESOLVED_ISSUES`, check the affected item's state and Apple's message.
Metadata and review-access fixes can often use the same binary. Once the issue
is fixed, mark the item resolved with `PATCH /v1/reviewSubmissionItems/{id}`
and `attributes.resolved` set to true. Check the items again and resubmit when
authorized. Withdraw an item or send a reply only if the user requested that
action. [Apple’s submission workflow](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app/)

## Release and verify availability

Set a requested release policy on the editable version with
`PATCH /v1/appStoreVersions/{id}`. Use `MANUAL`, `AFTER_APPROVAL` or
`SCHEDULED` for `releaseType`. Include the agreed `earliestReleaseDate` with an
explicit timezone for a scheduled release. Read the policy back before submission.

- **Manual.** When `appVersionState` is `PENDING_DEVELOPER_RELEASE` and release
  is authorized, send `POST /v1/appStoreVersionReleaseRequests` with an
  `appStoreVersion` relationship to this version. Read the version again.
- **Automatic or scheduled.** Follow the version state after approval. The
  scheduled time is the earliest Apple may release it.
- **Phased updates.** For an eligible update with phased release requested,
  read `GET /v1/appStoreVersions/{id}/appStoreVersionPhasedRelease`. Create a
  missing configuration with `POST /v1/appStoreVersionPhasedReleases` linked
  to the version. Use `PATCH /v1/appStoreVersionPhasedReleases/{id}` to pause,
  resume or complete it when requested. Check its state and day number. Phasing
  controls automatic updates. Customers can download the update manually from
  day one. [Apple’s phased release guide](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases)

For an availability request, check the version's `appVersionState` and the
requested territories via `GET /v2/appAvailabilities/{id}/territoryAvailabilities`
using the *availability* ID. Verify the version on the intended storefront when
possible. A territory can be enabled while the new version is still propagating.
Give the time and storefront of the observation and identify any pending rollout.
