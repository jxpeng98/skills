# Deliver a build

Look for the candidate first. On `GET /v1/builds`, filter by `app`,
`preReleaseVersion.platform`, `preReleaseVersion.version` (marketing version)
and `version` (build number). If the matching build is valid, use its ID. For a
new candidate, match the artifact's bundle ID, platform, version, build number
and signing team to the requested release.

## Start from CI or a signed artifact

- **Xcode Cloud.** Read `GET /v1/apps/{id}/ciProduct`, then use the product ID
  in `GET /v1/ciProducts/{id}/workflows` to find the distribution workflow.
  Check the source branch/tag and the workflow's distribution actions.
  To start an authorized run, send `POST /v1/ciBuildRuns` with the `workflow`
  and `sourceBranchOrTag` relationships. Poll `GET /v1/ciBuildRuns/{id}`, verify
  the source commit and result, then read `GET /v1/ciBuildRuns/{id}/builds`.
  If the run delivered the build, continue with that build ID.
- **Other CI or local builds.** Use the project's signing and archive commands
  when a build is needed. If the user supplied a signed IPA or Mac App Store
  package, use that artifact directly after checking its identity. An existing
  Transporter pipeline with API-key authentication can also deliver it. For a
  direct REST upload, follow the file reservation steps below. [Apple’s build uploads](https://developer.apple.com/documentation/appstoreconnectapi/build-uploads)

## Upload a binary over REST

1. List `GET /v1/apps/{id}/buildUploads` for the platform, marketing version
   and build number. Inspect any matching upload and its files before starting
   another. To start a new upload, send the artifact's version numbers, platform
   and app ID to `POST /v1/buildUploads`. This example reserves iOS build 37.

   ```json
   {
     "data": {
       "type": "buildUploads",
       "attributes": {
         "platform": "IOS",
         "cfBundleShortVersionString": "2.4",
         "cfBundleVersion": "37"
       },
       "relationships": {
         "app": {"data": {"type": "apps", "id": "APP_ID"}}
       }
     }
   }
   ```

2. Reserve each file with `POST /v1/buildUploadFiles`. Link `buildUpload` to
   the upload ID. For the binary, send `assetType: ASSET`, its actual `fileName`
   and byte `fileSize`, and the matching `uti` (`com.apple.ipa` or
   `com.apple.pkg`). Keep the file ID.
3. For each `uploadOperations` entry, read the file at the given offset for
   the specified length. Send those bytes to the signed URL using the entry's
   HTTP method and headers. A plain HTTPS client can do this part. Keep the
   Connect bearer token on the API origin. If a signed URL expires, read the
   file reservation again before resuming.
4. Once every part succeeds, send `PATCH /v1/buildUploadFiles/{id}` with its
   type, ID, `uploaded: true` and the original file's checksum in
   `attributes.sourceFileChecksums.file` (`algorithm` and `hash`). Poll
   `GET /v1/buildUploads/{id}?include=build`. Read `attributes.state.state`
   and any processing errors. On completion, follow the build relationship and
   check `attributes.processingState` on the build itself. Use its build ID for
   TestFlight or App Store version selection.

## Distribute to TestFlight

1. Read `GET /v1/apps/{id}/betaGroups` and match the requested group ID and
   `isInternalGroup`. Check the build's audience, expiry, processing and export
   compliance, as well as existing group membership and automatic distribution.
   Use the app owner's confirmed export classification if Apple asks for one.
2. For a requested group assignment, send `POST /v1/betaGroups/{id}/relationships/builds`
   with `{"data":[{"type":"builds","id":"BUILD_ID"}]}` if the build is absent.
   Consider who will be notified before assigning a build to an automatic group.
3. For external testing, check test information, review access and the build's
   beta review state. If Beta App Review is required and in scope, use
   `POST /v1/betaAppReviewSubmissions` with the `build` relationship. Inspect
   `GET /v1/builds/{id}/betaAppReviewSubmission` before retrying.
4. Verify the build in `GET /v1/betaGroups/{id}/builds` and the relevant
   internal or external state in `GET /v1/builds/{id}/buildBetaDetail`.
   Tell the user whether the group can install this build or is waiting for
   review. Invite new testers or enable a public link only if the user asked to
   reach that audience. [TestFlight overview](https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview)
