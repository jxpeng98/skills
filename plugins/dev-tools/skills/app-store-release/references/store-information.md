# Store information and declarations

Use the project's existing facts and the current Connect form. A filled field is
not evidence that its answer is correct. Record confirmed decisions once and
reuse them while their scope and facts remain unchanged.

## App record and product page

- Confirm the developer team, supported platforms, registered bundle ID, app name,
  primary language, SKU, and intended user access before creating a missing app.
  Team-wide Full Access is an access decision, not a required default.
- Map prepared text to name, subtitle, promotional text, description, keywords,
  category, copyright, support URL, and applicable marketing URL. Verify current
  limits and required localizations. Keep Chinese and English claims consistent
  when both are supported; do not invent features or support promises.
- Review contact details go to Apple. Public support details and privacy URLs
  serve customers. Do not copy private reviewer details into public metadata.
  Supply a usable review account only if login is required, plus concise steps
  for non-obvious features, permissions, hardware, purchases, or sample content.
  Do not invent credentials or claim an unreachable backend works.

## Screenshots and previews

1. Find the existing capture/export workflow and current candidate UI. Respect
   project rules reserving simulator or device interaction for the user; explicit
   screenshot capture authorization applies only to the requested work.
2. Use Apple's current [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)
   and the actual media manager to identify required device sizes and locales.
   Check dimensions, orientation, readability, order, and rights to shown content.
   Use real app views; never fabricate UI or include personal data.
3. Prepare replacements before removing old images. For an authorized replacement,
   update the intended slots and verify processing, saved counts, order, and any
   inherited device/localization sets. Do not assume a thumbnail means every
   required screenshot set is complete.

## Content rights and age rating

Ask the owner to resolve unsupported ownership or licensing facts for bundled
media, screenshots, icons, and store copy. Distinguish a third-party content
catalog, user-imported files, public user-generated content, and software-library
licensing. Local import alone establishes none of their rights declarations.

Answer the current [age-rating questionnaire](https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating)
from actual features and content: communication, web access, content controls,
health topics, violence, sexual content, gambling, and other prompts as applicable.
Let Apple calculate the rating; justify any override or regional requirement.
Being a utility does not establish a particular rating or all-negative answers.

## Privacy: three separate checks

| Layer | Evidence and action |
| --- | --- |
| Public policy and Connect privacy declaration | Review actual app and third-party SDK data flows, collection, linking, tracking, and purposes against Apple's definitions. Verify the public policy is reachable and accurate. Save questionnaire changes and separately verify publication. |
| Packaged privacy manifest | Inspect applicable `PrivacyInfo.xcprivacy` files, required-reason APIs and their approved reasons, and SDK manifest/signature requirements in the actual archive. |
| Runtime permission prompts | Verify purpose strings, localization, and requesting behavior for the protected resources actually used. |

These checks cannot substitute for one another. A local-first design does not
alone prove Data Not Collected: inspect analytics, crashes, accounts, cloud sync,
network services, and dependencies. Unknown practices must remain unresolved.
For an existing live app, align publication timing with Apple's guidance for the
currently available version and app-wide platform coverage.
See [manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy),
[privacy definitions](https://developer.apple.com/app-store/app-privacy-details/),
and [privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

## Accessibility labels

Check the current [Accessibility Nutrition Label requirements](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels)
and feature-specific evaluation criteria. Labels describe demonstrated support on
each platform, including completing common app tasks with the feature enabled.
Native controls, source annotations, compilation, and a contrast check alone do
not establish full VoiceOver or other accessibility support.

Record the evaluated flows, device/platform, feature, and who tested them. Follow
project constraints on runtime testing. Unverified support is not equivalent to
unsupported; do not manufacture affirmative or negative labels. Check whether
unprovided labels currently block submission instead of hard-coding optionality.
Updating the label alone does not add accessibility behavior to the binary.

## Commercial and regional settings

Verify price and effective date separately from availability. Free pricing does
not select sales territories. Apply the user's confirmed regions, inspect
account-eligible availability, and preserve intended Mac/visionOS distribution.
Do not silently broaden platforms, access, or sales regions.

Resolve applicable trader status, regional registrations, tax category,
agreements, banking, and purchase/subscription requirements from actual account
prompts and owner-supplied facts. Do not assume all are required for every free
app or choose a legal classification merely to clear a form. Preserve the chosen
manual, automatic, or scheduled release behavior and verify it before submission.
