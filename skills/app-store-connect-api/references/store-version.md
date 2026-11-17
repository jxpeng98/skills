# Prepare the store version

Read `GET /v1/apps/{id}/appStoreVersions` with the platform and version string.
If the requested version is missing and creation is in scope, send
`POST /v1/appStoreVersions` with `attributes.platform`, `attributes.versionString`
and the `app` relationship. Keep its ID and check `appVersionState` before edits.

| Content | Where it lives |
| --- | --- |
| Name, subtitle and privacy policy URL | Find the editable app-info record in `GET /v1/apps/{id}/appInfos`, then the locale in `GET /v1/appInfos/{id}/appInfoLocalizations`. |
| Description, keywords, support URL and what's new | Use `GET /v1/appStoreVersions/{id}/appStoreVersionLocalizations`. Match the locale before changing it. |
| Age rating | Read `GET /v1/appInfos/{id}/ageRatingDeclaration`, then use `PATCH /v1/ageRatingDeclarations/{id}` with the declaration ID and confirmed answers. |
| Privacy disclosures | An authorized team member publishes the answers in **App Privacy** on the website. Saving the policy URL and publishing the disclosures are separate steps. [Apple’s privacy workflow](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy) |
| Export compliance | Use the build's verified classification. If it needs an existing approved declaration, find it in `GET /v1/apps/{id}/appEncryptionDeclarations` and link it with `PATCH /v1/builds/{id}/relationships/appEncryptionDeclaration`. |
| Review access | Read `GET /v1/appStoreVersions/{id}/appStoreReviewDetail`. Create or update the version's `appStoreReviewDetails` record with the supplied contact, notes and demo access. Keep private values in protected inputs and out of release summaries. |
| Price and territories | Inspect `GET /v1/apps/{id}/appPriceSchedule` and `GET /v1/apps/{id}/appAvailabilityV2`. Before changing a schedule or territory selection, check its effective dates and preserve existing choices outside the request. Use the current schema for `POST /v1/appPriceSchedules` or `POST /v2/appAvailabilities`. |

For an existing locale, PATCH the localization record with the fields that
changed. To add a locale, POST to the collection and link the new record to its parent.
For example, the following body updates only the release notes with
`PATCH /v1/appStoreVersionLocalizations/{id}`. Substitute the locale record's
ID and the approved text, then read that record back.

```json
{
  "data": {
    "type": "appStoreVersionLocalizations",
    "id": "LOCALE_ID",
    "attributes": {"whatsNew": "Adds offline search."}
  }
}
```

Save the approved body in `notes.json` and use the same localization ID in
both requests. On readback, check the locale and the release notes.

```sh
node scripts/request.mjs PATCH "/v1/appStoreVersionLocalizations/$LOCALE_ID" notes.json
node scripts/request.mjs GET "/v1/appStoreVersionLocalizations/$LOCALE_ID"
```

## Screenshots and previews

Find the locale's `appScreenshotSets` or `appPreviewSets` relationship. Match
the display type before reserving each asset. For a screenshot, use
`POST /v1/appScreenshots` with the `appScreenshotSet` relationship, file name
and size. Send the returned byte ranges to their signed URLs using the supplied
headers only. Commit with `PATCH /v1/appScreenshots/{id}`, setting `uploaded`
and `sourceFileChecksum` from the original file as Apple specifies. For a
preview, use the corresponding preview set, resource and media attributes.
Verify the processed asset's `assetDeliveryState` and its position in the set.
Preserve existing media when adding a locale or recovering a partial upload.
[Apple’s asset upload guide](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect)

## Select the build

Read `GET /v1/appStoreVersions/{id}/build` and compare its ID with the requested
processed build. To select it, send `PATCH /v1/appStoreVersions/{id}/relationships/build`
with the body below and read the build association again. Here the path ID
identifies the store version, and the body ID identifies the build.

```json
{"data":{"type":"builds","id":"BUILD_ID"}}
```

Once the version draft is saved, report its version, build number and affected
locales. If the user also wants it ready for review, continue to the review draft.
