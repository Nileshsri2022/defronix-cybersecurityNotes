# Day-12 — Sensitive Data from JavaScript Files, Live Recon — English Translation

*Translated from: `088 - Day-12 - Sensitive Data From Java Script Files, Live Recon - Bug Bounty Free Course [Hindi].hi-orig.srt`*
*Style: detailed edited translation with repeated stream dialogue consolidated.*

---

Today's reconnaissance topic is client-side JavaScript. A web application sends JavaScript bundles to every browser, so they can reveal routes, API hosts, parameter names, feature flags, source-map references, third-party integrations, and accidentally embedded secrets.

Begin only with authorized web hosts. Browse normally through Burp or collect script URLs from HTML `script src` elements, HTTP history, archive sources, and tools such as Katana. Resolve relative URLs against the page and deduplicate them. Do not assume a script discovered historically is still in scope.

Download files at a controlled rate and preserve the source URL, timestamp, status, and hash. Beautify minified code for reading, but retain the original evidence. Search for high-signal terms such as `api`, `token`, `secret`, `Authorization`, `Bearer`, `client_id`, `graphql`, `admin`, `debug`, `staging`, `s3`, and full URLs. Automated tools such as LinkFinder or SecretFinder can extract candidates, but their regex matches are not proof.

JavaScript commonly reveals API endpoints and hidden application features. Feed discovered hosts back through scope validation before probing them. A route absent from the visible UI is not automatically vulnerable; test its server-side authentication and authorization only where permitted.

Distinguish public configuration from a genuine secret. Analytics IDs, public Firebase configuration, OAuth client IDs, map API keys, and publishable payment keys may be intended for browsers. Risk depends on restrictions and privileges. A private cloud key, reusable bearer token, database credential, signing secret, or unrestricted privileged API key is different.

Validate with minimum impact. Prefer provider metadata or a harmless identity/quota call approved by policy. Never use a key to read user data, modify resources, send messages, or pivot into another system merely to prove severity. Redact values in notes and reports; show only a short prefix/suffix.

Search for source maps such as `app.js.map`. They can reconstruct original modules, comments, paths, and source names. Download them only from in-scope hosts and treat resulting source as sensitive. Historical bundles may contain revoked credentials but still reveal architecture.

The workflow is:

```text
collect authorized pages
→ extract JS URLs
→ normalize/deduplicate
→ download slowly
→ beautify and inspect
→ extract endpoints/secret candidates
→ validate scope and privilege safely
→ report with redaction
```

Remediation is to remove secrets from client bundles and repository history, rotate exposed credentials, restrict keys by origin/IP/API and least privilege, keep privileged operations server-side, disable unnecessary production source maps, and add secret scanning to development and build pipelines.

<!-- DONE-088 -->
