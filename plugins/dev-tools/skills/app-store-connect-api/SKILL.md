---
name: app-store-connect-api
description: Automate Apple app releases through the App Store Connect API. Use for JWT-authenticated requests, headless release jobs, TestFlight, App Review submission and storefront rollout. For general App Store preparation, use app-store-release when available.
---

# App Store Connect API

Identify the app, platform and version or build. If the user asks for its status,
read the record and report what Apple shows. If they ask for a release, resume
at that state and continue to the stage they requested. API writes change the
production account, so match the build, audience and release policy to the request.

## Connect to the app

Use the project's authenticated API client or CI credentials. For direct HTTP
requests, the bundled Node.js 18+ client signs each request with a short-lived
JWT. Set `ASC_KEY_ID` and `ASC_PRIVATE_KEY_PATH` through the environment. Set
`ASC_ISSUER_ID` for a team key and leave it unset for an individual key. Keep
the private key in the team's secret store or protected key file. [Apple’s JWT guide](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests)

From this skill's directory, look up the app by its bundle ID. Replace
`com.example.app` in this example.

```sh
node scripts/request.mjs GET '/v1/apps?filter[bundleId]=com.example.app&fields[apps]=name,bundleId'
```

Match the returned bundle ID and use its `data[].id` for subsequent calls.
Follow `links.next` on list responses before concluding a record is missing.
If the app is absent, check the team and the key's access. A first release needs
an app record created on the Connect website. Resume with its ID. [Apple’s app records](https://developer.apple.com/documentation/appstoreconnectapi/apps)

Pass the client an HTTP method and an API path or full Connect API URL. For a
POST or PATCH, pass the JSON body file as the third argument. A write may return
an empty body, so read the resource back to confirm the change. If a response
contains signed upload URLs or private review details, pipe it directly to the
next tool or save it in a protected temporary file.

## Run the requested stage

| When the job needs… | What to do |
| --- | --- |
| A new build, a binary upload or TestFlight distribution | Follow `references/builds-and-testflight.md` to start an existing CI workflow or deliver a signed artifact, then identify the processed build and its audience. |
| Store text, screenshots, version settings or build selection | Use `references/store-version.md` to find the record that owns the field and verify each change on the intended version and locale. |
| App Review, rejection recovery or public release | Use `references/review-and-rollout.md` to assemble and check the draft, submit it, and follow the chosen release policy. |

Check the method, required fields and writable relationships in Apple's current
specification. Some steps, such as accepting a new agreement, take place on the
website. Tell the user which form needs attention and resume once the account
shows the change. For compilation and signing, follow the project's build
workflow or use `app-store-release` when available. [Apple’s OpenAPI specification](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip)

## Resume after an interruption

Keep the resource IDs returned by each write. After a timeout, conflict or
interrupted run, read the resource and its parent relationship before deciding
whether another write is needed. If Apple might still be processing the first
request, poll with backoff. When the outcome remains ambiguous, pause that write
and report the last observed state.

Use Apple's error code, detail and field pointer to find the cause. A 401 calls
for checking the token, clock and key. For a 403, check the role and app access.
On a 429, respect any retry delay and space out reads. For a monitoring request,
continue until the requested state, an actionable failure or the agreed deadline.
Report the app, platform, version/build, resource ID, last observed state and
time. If the job is pending, say which resource to read next.
