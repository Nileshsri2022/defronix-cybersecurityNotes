# Bug Bounty Day 8 — content discovery and visual triage — Explained

## Lesson reconstruction

Day 8 continues recon after identifying live web hosts. The instructor adds directory/content discovery, screenshots, and additional subdomain sources.

Directory brute forcing sends candidate paths from a wordlist to a web server and compares responses. Use tools such as Gobuster, ffuf, or Feroxbuster only on in-scope hosts and at an allowed rate. Begin with a small relevant list and known extensions rather than maximum concurrency. Establish a baseline random path so custom 404 pages, redirects, and wildcard responses do not create thousands of false positives.

Record status code, size, words/lines, redirect location, and content type. Interesting responses include 200, authentication-related 401, authorization-related 403, redirects, and distinctive error behavior. A 403 path is not proof of sensitive content and should not trigger bypass attempts unless allowed. Avoid recursive discovery until the initial results are understood.

Screenshots provide fast visual triage across many hosts. A screenshot tool can reveal login pages, default installations, dashboards, parked domains, error pages, and duplicated applications. It does not replace HTTP metadata or manual verification. Store screenshots securely because pages may contain tokens or personal data, and exclude unrelated third-party redirects.

Additional passive subdomain collection is merged into the existing pipeline: normalize, deduplicate, detect wildcards, resolve, verify ownership/scope, then probe. Do not maintain separate unreviewed lists that later leak out-of-scope hosts into tools.

Prioritize combinations: an unusual subdomain plus a distinctive login page plus exposed paths is more informative than any item alone. The session's goal is organized attack-surface enrichment, not claiming every hidden path as a vulnerability.

## Engineering and safety notes

Use response filtering carefully: identical size alone can collide, so compare status, hash, words, and title. Respect `Retry-After`, rate-limit responses, and program concurrency rules. Keep tool user-agent/contact details where appropriate. Never download backups, repositories, or sensitive files beyond the minimum proof authorized by policy.

## Verification checklist

- Reproduce the workflow only in an isolated lab or explicitly authorized scope.
- Validate inputs, quote paths and variables, and test failure behavior.
- Preserve source, date, command, and minimal evidence for every observation.
- Distinguish a lead from a verified finding; do not overstate impact.
- Remove secrets and personal data from notes before sharing.

## Review questions

1. What prerequisite or authorization boundary controls this workflow?
2. Which output justifies the next action, and which output is only a lead?
3. How can false positives or stale data appear?
4. What is the safest failure/cleanup behavior?
5. How would a defender prevent or detect the weakness discussed?

<!-- DONE-084 -->
