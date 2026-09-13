# Shipped open-source components

Use this branch for dependencies that the app actually distributes. First inspect
the pinned source, licenses and notices, wrapper packages, build configuration,
and packaged binary. A dependency name or a commercial-use FAQ is not a complete
license inventory. Do not send the app through a copyleft checklist when all
shipped dependencies only require simpler notices.

## Establish the applicable obligations

Record component/version, origin and checksum, exact license text and any
“or later” option, local modifications, linkage, shipped features, and delivery
method. Read source-file headers as well as top-level license files. Distinguish
the library from wrappers and optional codecs or decoders.

For LAME, the [official commercial-use guidance](https://lame.sourceforge.io/license.txt)
is an entry point; inspect the selected source release to establish the license
version. Treat historical mpglib/GPL warnings as a reason to investigate the
actual decoder sources and build output, not proof that every LAME binary includes
that decoder. If claiming encoder-only distribution, retain configuration,
linked-object/dependency, and relevant symbol evidence. An unused API can still
be packaged.

LGPL can permit a proprietary application under its conditions; neither a
commercial-use statement nor a separately named framework proves those conditions
are met. Consult the applicable text, such as
[LGPL v2](https://www.gnu.org/licenses/old-licenses/lgpl-2.0.html),
[LGPL v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html), or
[LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html). Identify the relevant source
delivery and combined-work clauses rather than silently upgrading the license.
The selected route may require corresponding library source, modifications,
notices, and materials allowing recipients to modify the library and relink the
application. Dynamic linking on a signed mobile platform does not by itself
demonstrate usable replacement. Evaluate the actual route and license version.

## Prepare and verify the developer's delivery

When the chosen route requires replacement/relinking support, use the project's
existing packaging workflow. Prepare the exact library source and modifications,
license and attribution files, relevant object files/resources, and complete
build/relink instructions for the distributed app version. Explain prerequisites
and limitations, including the recipient's own signing identity, bundle IDs,
App Groups, and provisioning where applicable. Never distribute signing keys,
credentials, or private review contacts.

Validate the delivered artifacts, not just a developer checkout:

1. Download/extract the candidate package into a fresh directory and verify its
   checksum and completeness. Run the documented procedure using those inputs.
2. Rebuild with the original library, then with a compatible, intentionally modified
   library. Show that the latter binary actually uses the replacement through
   appropriate dependency, symbol, or behavior evidence; copying a file is not
   enough. Record the commands, toolchain, outputs, and limitations.
3. Track relinking, recipient-controlled signing, installation, and functional
   device validation as separate results. A local relink check does not establish
   an independent recipient's successful installation. Respect project testing
   restrictions and say which checks remain unperformed.
4. Match the package to the final submitted build. If applicable inputs change,
   regenerate the affected materials and repeat the relevant validation.

The developer supplies this route; ordinary customers need not modify the
library to use the app. Describe it as an available right and procedure, not a
required setup step in the normal product flow.

## Notices, hosting, and distribution terms

Add accurate attribution, license text/access, source and replacement-package
links, and clear instructions to the app's About/help area and release documents
as required by the chosen license route. Keep supported UI languages consistent.
If bundled resources change, include them in a new app build.

Publish intended non-secret materials through the existing authorized website or
release channel. Use versioned URLs/checksums, retain materials needed by earlier
recipients, and verify real downloads and embedded links. Updating a shared
support site must preserve unrelated products and pages. A plan to publish, or
an upstream homepage alone, is not evidence of delivering the required materials.

Compare the selected license route with the actual app EULA, Apple's current
[Standard EULA](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/),
[Developer Program agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/),
and relevant distribution restrictions. Where the applicable LGPL clauses require
it, preserve permission for personal modification and reverse engineering to debug
those modifications; assess any installation-information requirements as well.
Identify which terms apply, their date,
the required recipient rights, and any remaining incompatibility or uncertainty.
Read open-source exceptions in context; a supplemental notice is not proof that
every platform restriction is resolved.

Report technical validation and the terms assessment separately. Do not certify
legal compatibility from a successful build, an Apple upload, or App Review
acceptance. If a material issue cannot be resolved from the applicable sources,
state the specific question for qualified legal review before distribution; do
not impose a generic legal-approval gate on unrelated apps.
