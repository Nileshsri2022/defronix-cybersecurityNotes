# Day-13 — GitHub Recon and Sensitive Data Exposure — English Translation

*Translated from: `089 - Day-13 - GitHub Recon & Sensitive Data Exposure Live Recon - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

GitHub reconnaissance searches public code and history for assets associated with an authorized organization: domains, API endpoints, configuration, employee naming patterns, and accidentally committed secrets. Start from the program's organization/repositories and confirmed domain names. A matching company word does not prove repository ownership.

Use GitHub's web search qualifiers such as `org:`, `repo:`, `path:`, `filename:`, `extension:`, and quoted domains. Search configuration formats (`.env`, YAML, JSON), cloud identifiers, authorization headers, private-key markers, and internal hostnames. Review commits and diffs because deleting a secret from the latest file does not remove it from Git history, forks, caches, or clones.

Tools such as GitLeaks, TruffleHog, and Gitrob automate pattern and entropy checks on repositories you are permitted to analyze. Authenticate with a minimally privileged token, respect GitHub rate limits, and never publish the token. Automated findings are candidates: examples, placeholders, checksums, public client identifiers, and revoked keys create false positives.

Classify a finding by ownership, validity, service, permissions, environment, and scope. Validate minimally—prefer a harmless identity call or provider-supported metadata check. Do not use a credential to access private repositories, customer records, cloud resources, or unrelated systems. If clear impact already exists, stop.

A report should cite repository URL, commit hash, file path, line range, discovery time, credential type, redacted value, safe validation, and remediation. Contact the program privately; do not open a public issue containing the secret.

Remediation requires immediate revocation/rotation, log review, least privilege, repository-history cleanup where appropriate, and secret scanning in pre-commit and CI. History rewriting does not invalidate a credential; rotation does. Move secrets to a managed secret store and use short-lived workload identity where possible.

<!-- DONE-089 -->
