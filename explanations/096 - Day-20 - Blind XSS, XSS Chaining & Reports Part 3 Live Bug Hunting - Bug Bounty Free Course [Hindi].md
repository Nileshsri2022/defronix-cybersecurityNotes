# Blind XSS, Chaining, and Reporting — Explained

## Blind-XSS data flow

```text
researcher-controlled field
→ server stores value
→ internal/staff interface renders value
→ browser executes unsafe markup/script
→ minimal authorized callback
```

The callback proves execution but not automatically administrator privileges. Correlate a random identifier with the exact submitted field and timestamp.

## Safety requirements

- explicit program permission for out-of-band callbacks;
- domain/server controlled by researcher or approved platform;
- HTTPS and restricted logs;
- no cookie/DOM/keylogging collection;
- no persistent harmful actions;
- immediate cleanup and retention limit;
- coordination if staff interaction is required.

## Chaining discipline

A valid chain needs confirmed links. Example reasoning:

```text
stored execution in admin origin
+ admin can perform action X
+ server lacks re-auth/CSRF/authorization boundary
= demonstrated action X
```

Do not jump from “JavaScript executed” to “full account takeover” without proving each prerequisite safely.

## Report template

1. Summary and affected asset.
2. Input source and storage action.
3. Triggering interface/role.
4. Reproduction with harmless unique payload.
5. Callback timestamp and redacted request.
6. Demonstrated impact and prerequisites.
7. Cleanup status.
8. Root-cause remediation.

## Defense

Fix every sink, not only the submitted field. Existing stored values can execute after deployment, so locate and neutralize them. Use templating auto-escaping, safe DOM assignment, allowlist sanitization for rich text, CSP nonces/hashes, and separate high-privilege interfaces.

## Review questions

1. Why is blind XSS riskier to test?
2. What minimum callback data is sufficient?
3. Why does a callback not prove administrator compromise?
4. What makes an XSS chain credible?
5. Why must stored payloads be cleaned after the code fix?

<!-- DONE-096 -->
