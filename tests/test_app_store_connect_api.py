"""Exercise the shipped client with an ephemeral key and an offline Apple response."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


CLIENT = (Path(__file__).resolve().parents[1] / "plugins/dev-tools/skills"
          / "app-store-connect-api/scripts/request.mjs")

# Runs before the actual CLI, so even a failed assertion stays offline.
MOCK = """
const assert = require('node:assert/strict');
const {generateKeyPairSync, verify} = require('node:crypto');
const {writeFileSync} = require('node:fs');
const {privateKey, publicKey} = generateKeyPairSync('ec', {namedCurve: 'P-256'});
writeFileSync(process.env.ASC_PRIVATE_KEY_PATH, privateKey.export({type: 'pkcs8', format: 'pem'}));
global.fetch = async (url, options) => {
  assert.equal(url.origin, 'https://api.appstoreconnect.apple.com');
  assert.equal(options.redirect, 'error');
  const [header, payload, sig] = options.headers.Authorization.slice(7).split('.');
  const decode = part => JSON.parse(Buffer.from(part, 'base64url'));
  assert.deepEqual(decode(header), {alg: 'ES256', kid: 'test-key', typ: 'JWT'});
  assert.ok(verify('sha256', Buffer.from(header + '.' + payload),
    {key: publicKey, dsaEncoding: 'ieee-p1363'}, Buffer.from(sig, 'base64url')));
  const claims = decode(payload);
  assert.equal(claims.aud, 'appstoreconnect-v1');
  assert.ok(claims.iat <= Date.now() / 1000 && claims.exp > Date.now() / 1000);
  assert.ok(claims.exp - claims.iat <= 1200);
  assert.equal(claims.iss, process.env.ASC_ISSUER_ID);
  assert.equal(claims.sub, process.env.ASC_ISSUER_ID ? undefined : 'user');
  if (options.method === 'PATCH') {
    assert.equal(options.headers['Content-Type'], 'application/json');
    assert.deepEqual(JSON.parse(options.body), {data: {type: 'builds', id: 'B37'}});
    return new Response(null, {status: 204});
  }
  if (url.pathname === '/v1/builds') {
    return new Response('rate limited', {status: 429, headers: {'Retry-After': '30'}});
  }
  assert.equal(url.searchParams.get('filter[bundleId]'), 'com.example.app');
  return Response.json({data: [{id: 'A1'}]});
};
"""


@unittest.skipUnless(shutil.which("node"), "Node.js is required to exercise the API client")
class AppStoreConnectRequestTests(unittest.TestCase):
    def test_cli_with_offline_transport(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            mock = folder / "apple.cjs"
            mock.write_text(MOCK)
            body = folder / "body.json"
            body.write_text('{"data":{"type":"builds","id":"B37"}}')
            env = {"PATH": os.environ["PATH"], "ASC_KEY_ID": "test-key",
                   "ASC_PRIVATE_KEY_PATH": str(folder / "test.p8")}

            def run(*args):
                return subprocess.run(["node", "--require", mock, CLIENT, *args],
                                      env=env, text=True, capture_output=True, timeout=10)

            result = run("GET", "/v1/apps?filter[bundleId]=com.example.app")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["data"][0]["id"], "A1")

            env["ASC_ISSUER_ID"] = "team"
            result = run("PATCH", "/v1/appStoreVersions/V2/relationships/build", body)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")

            result = run("GET", "/v1/builds")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("HTTP 429 (Retry-After: 30)", result.stderr)
            result = run("GET", "https://uploads.example/v1/file")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("App Store Connect API resource URL", result.stderr)
            body.write_text("private reviewer detail")
            result = run("PATCH", "/v1/appStoreReviewDetails/R1", body)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stderr.strip(), "The request body must be valid JSON.")
