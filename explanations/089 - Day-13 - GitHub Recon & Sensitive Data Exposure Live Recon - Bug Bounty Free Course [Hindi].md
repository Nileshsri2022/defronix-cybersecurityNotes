# GitHub Recon — Explained

## Search model

```text
verified organization/repository
→ code and commit search
→ candidate classification
→ minimal authorized validation
→ private report and rotation
```

Useful qualifiers can be combined:

```text
org:example "example.com"
org:example filename:.env
repo:example/app path:config password
org:example "BEGIN PRIVATE KEY"
```

Search syntax evolves; use current GitHub documentation. API automation must paginate, handle rate limits, and store no unnecessary source.

## History

Inspect commits that introduced and removed a value. A secret can remain valid after deletion. Forks and clones mean history rewriting is incomplete containment.

## False positives

- documentation examples;
- test fixtures;
- public/publishable API keys;
- random hashes;
- encrypted values;
- revoked credentials;
- another organization with a similar name.

## Safe handling

Never paste a live secret into search engines, public issues, chat, terminal screenshots, or command lines that enter history. Use redaction and restrictive evidence storage. Revoke first when you control the environment.

## Remediation order

1. Revoke/rotate.
2. Review provider/audit logs.
3. Reduce permissions and lifetime.
4. Replace code with secret-manager references.
5. Clean history if useful.
6. Add scanning and push protection.

## Review questions

1. Why is deleting the current file insufficient?
2. What proves repository ownership?
3. Why is entropy only a triage signal?
4. Why rotate before rewriting history?
5. What evidence is enough without using privileged access?

<!-- DONE-089 -->
