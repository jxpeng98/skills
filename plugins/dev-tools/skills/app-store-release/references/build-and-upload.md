# Build, upload, and associate the candidate

## Before archiving

- Read the project build instructions and existing scripts/CI. Identify the scheme,
  workspace/project, Release configuration, version, build number, and signing
  method. Use the project's source of truth for generated Xcode files.
- Confirm main-app and extension bundle IDs, team, App Groups and other shared
  capabilities, provisioning profiles, and entitlements agree. A bundle rename
  can affect extensions and shared-container access; a display-name change alone
  does not require renaming the project or bundle identifier.
- Check installed Xcode/SDK versions against Apple's current
  [upload requirements](https://developer.apple.com/news/upcoming-requirements/).
  The SDK used to build and the minimum supported runtime OS are different values.
  Do not raise the deployment target merely to satisfy an SDK requirement.
- Before the build, record the revision, dirty source/configuration inputs,
  dependency versions, and hashes of relevant generated resources. Include newly
  bundled notices, privacy files, icons, and support/relinking URLs. A later source
  edit cannot be covered by an earlier successful archive.
- Use an unused, valid build number for a new upload and keep embedded targets
  consistent under the project's versioning rules. Check existing Connect builds
  before retrying an upload whose outcome is uncertain.

## Archive and inspect

Reuse the project command when available. For a manual Xcode workflow, select the
intended scheme and device archive destination, choose **Product > Archive**,
then select that exact archive in Organizer. Validate and use **Distribute App >
App Store Connect** with the current Xcode options. An existing CI, Transporter,
or supported command-line route can serve the same task; do not introduce a new
upload framework just for this release. See [Apple's upload guide](https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds).

Inspect the resulting `.xcarchive` and exported `.ipa`, not only build settings:

- Confirm app/extension identifiers, version/build numbers, architectures,
  deployment target, signing identity, provisioning and effective entitlements.
  Check embedded frameworks and extensions are present and correctly signed.
- Verify the actual packaged privacy manifests, permission strings, app icons,
  localizations, licenses, notices, and other release-critical resources. Check
  framework dependencies or symbols when excluding optional licensed components.
- Preserve the archive, export options without secrets, upload/validation logs,
  applicable dSYMs, and artifact checksums in the existing release location.
  Keep private source, object files, profiles, and credentials out of public
  packages unless a specific non-secret distribution artifact is intended.
- Resolve validation failures. Record meaningful warnings and their effect; do
  not rewrite unrelated dependencies merely to remove every historical warning.

Run the project's required static checks and compilation. Respect instructions
that reserve simulator/device tests for the user. Report runtime checks as
user-reported when that is their source; compilation does not prove recording,
imports, exports, sharing, permissions, accessibility, or visual correctness.
Changed behavior needs appropriately refreshed validation evidence.

## Encryption/export compliance

Inventory the actual app and SDK cryptography: system-provided encryption,
embedded implementations, protocols, and purposes. A hash function, MP3 encoding,
and encryption are different operations; do not infer export classification from
an algorithm name alone. Check Apple's current
[export-compliance workflow](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance)
and documentation requirements for the app's distribution.

Set `ITSAppUsesNonExemptEncryption` and any approval code only when supported by
that classification. Do not default the key to false to suppress a questionnaire.
Complete required documentation/approval when applicable and verify the processed
build no longer has an unresolved compliance condition. Keep technical findings
separate from owner attestations or a legal conclusion that remains unresolved.

## Upload, processing, and build replacement

1. Upload the inspected candidate through the authorized route. Keep authentication
   in the host's supported credential handling, never in source files, shell
   history, public logs, or reviewer notes.
2. Observe processing until the result is known, or report processing as pending.
   Upload success does not establish processing success, TestFlight availability,
   or App Review submission. Inspect failures before producing another build.
3. Open the intended App Store version and inspect its Build section. Verify the
   exact version/build and processing/compliance state before selecting it. A
   TestFlight build is not automatically the version's selected build.
4. If an authorized replacement requires removing the old association, verify the
   current control's scope. Apple's [choose-a-build guide](https://developer.apple.com/help/app-store-connect/manage-builds/choose-a-build-to-submit)
   distinguishes removing a build from a version from removing it from the
   account. Do not confuse this with expiring testing, deleting an app, or
   cancelling an active review. Follow actual tool approval constraints.
5. Save, re-open, and verify the new association. Resume the submission workflow
   only to the user's requested stage; selecting a build does not submit it.
