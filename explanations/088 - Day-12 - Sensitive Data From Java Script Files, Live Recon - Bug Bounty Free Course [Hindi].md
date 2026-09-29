# JavaScript Recon and Sensitive-Data Exposure — Explained

## Collection

Use browser/Burp history first because it reflects real application behavior. Additional authorized discovery:

```bash
katana -u https://app.example -jc -o urls.txt
grep -Ei '\.m?js([?#].*)?$' urls.txt | sort -u > js.txt
```

Review tool flags and rate limits. Keep third-party scripts separate; their presence does not put vendor domains in scope.

## Analysis layers

1. **URLs/routes:** REST paths, GraphQL endpoints, WebSocket URLs, upload paths.
2. **Architecture:** service names, environments, versions, feature modules.
3. **Parameters:** IDs, role names, debug flags, object fields.
4. **Credentials:** tokens, passwords, private keys, webhook secrets.
5. **Source maps:** original filenames/source content.

Beautifiers improve readability but can alter formatting. Hash and preserve originals.

Useful searches:

```bash
rg -ni 'authorization|bearer|api[_-]?key|secret|token|password' js/
rg -no 'https?://[^"'"' ]+' js/
```

Regex output is triage. Random strings, examples, test fixtures, and public identifiers generate false positives.

## Secret classification

Ask:

- Is it intended to be public?
- Is it active?
- What service accepts it?
- What exact permissions/restrictions apply?
- Does safe validation remain inside scope?
- Has it already been rotated?

Do not submit “API key exposed” without establishing why that key grants unauthorized capability. Conversely, never over-validate a clearly privileged credential.

## Source maps

A bundle comment may contain:

```text
//# sourceMappingURL=app.js.map
```

Maps can embed `sourcesContent`. They may reveal source but are not automatically a vulnerability. Severity depends on exposed sensitive information or how the disclosure enables a concrete attack.

## Reporting

Include script URL, hash/version, line/snippet with redaction, credential type, safe validation result, demonstrated permissions, and rotation recommendation. Do not paste the complete secret into a broadly visible report field.

## Defensive controls

Build-time environment variables can still be bundled if referenced by client code. Prefix conventions such as `PUBLIC_` should be reviewed. Use server-side secret stores, short-lived tokens, least privilege, provider restrictions, pre-commit/CI secret scanning, and post-incident history cleanup plus rotation.

## Review questions

1. Why is a hidden endpoint not automatically vulnerable?
2. Why can an OAuth client ID be public while a client secret cannot?
3. What makes source-map exposure impactful?
4. Why preserve original minified files?
5. What is the least-invasive way to validate a candidate credential?

<!-- DONE-088 -->
