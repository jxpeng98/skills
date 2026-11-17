import { sign } from 'node:crypto';
import { readFileSync } from 'node:fs';

const api = 'https://api.appstoreconnect.apple.com';

function jwt() {
  const { ASC_KEY_ID: kid, ASC_PRIVATE_KEY_PATH: path, ASC_ISSUER_ID: issuer } = process.env;
  if (!kid || !path) throw new Error('Set ASC_KEY_ID and ASC_PRIVATE_KEY_PATH for the intended key.');

  const iat = Math.floor(Date.now() / 1000);
  const subject = issuer ? { iss: issuer } : { sub: 'user' };
  const encode = value => Buffer.from(JSON.stringify(value)).toString('base64url');
  const header = encode({ alg: 'ES256', kid, typ: 'JWT' });
  const claims = encode({ ...subject, iat, exp: iat + 300, aud: 'appstoreconnect-v1' });
  const payload = `${header}.${claims}`;
  const signature = sign('sha256', Buffer.from(payload), {
    key: readFileSync(path),
    dsaEncoding: 'ieee-p1363',
  });
  return `${payload}.${signature.toString('base64url')}`;
}

async function main() {
  const [method, path, file, ...extra] = process.argv.slice(2);
  if (!['GET', 'POST', 'PATCH', 'DELETE'].includes(method) || !path || extra.length ||
      (method === 'GET' && file) || (['POST', 'PATCH'].includes(method) && !file)) {
    throw new Error('Usage: node request.mjs GET|POST|PATCH|DELETE /v1/resource [request.json]');
  }
  const url = new URL(path, api);
  if (url.origin !== api || url.username || url.password || !/^\/v\d+\//.test(url.pathname)) {
    throw new Error('Use an App Store Connect API resource URL.');
  }
  const body = file ? readFileSync(file, 'utf8') : undefined;
  if (file) {
    try {
      JSON.parse(body);
    } catch {
      throw new Error('The request body must be valid JSON.');
    }
  }
  const headers = { Authorization: `Bearer ${jwt()}` };
  if (file) headers['Content-Type'] = 'application/json';
  const response = await fetch(url, {
    method, headers, body, redirect: 'error', signal: AbortSignal.timeout(30000),
  });
  const data = await response.text();
  if (!response.ok) {
    const retry = response.headers.get('retry-after');
    throw new Error(`HTTP ${response.status}${retry ? ` (Retry-After: ${retry})` : ''}\n${data}`);
  }
  if (data) process.stdout.write(data + '\n');
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
