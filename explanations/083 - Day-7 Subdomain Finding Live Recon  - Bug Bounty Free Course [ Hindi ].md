# Bug Bounty Day 7 — subdomain discovery — Explained

## Lesson reconstruction

Day 7 focuses on subdomain discovery, one of the main ways to expand an authorized wildcard scope. Subdomains often represent products, APIs, regional deployments, development systems, support portals, and infrastructure. Discovery must be followed by validation; a name alone says little about ownership or liveness.

Passive sources include certificate transparency, search engines, DNS datasets, archives, public code, and tools such as Subfinder or Amass configured with legal data sources. Active DNS brute force can query candidate labels from a wordlist, but it creates direct traffic and must comply with scope and rate limits.

Merge source outputs, lowercase hostnames, remove trailing dots, keep only syntactically valid names under the approved suffix, and deduplicate. Detect wildcard DNS by resolving random labels; otherwise every guessed name may appear valid. Resolve candidates and preserve A, AAAA, and CNAME chains.

Next, probe authorized web services carefully using both HTTP and HTTPS. Record status, title, redirect target, server/technology hints, content length, and resolved address. A 404 or 403 host is still live; a redirect to a third party requires a new scope decision. Shared IP ownership does not authorize scanning neighboring virtual hosts.

Prioritize names suggesting admin, api, auth, dev, stage, test, upload, legacy, or regional functionality, but do not assume they are vulnerable. Compare applications, authentication boundaries, headers, and technologies. Historical names can reveal decommissioning mistakes or dangling DNS; takeover testing must follow the program's specific policy and should avoid claiming third-party resources unnecessarily.

The final deliverable is a verified, tagged subdomain inventory with source and confidence—not merely a large text file.

## Engineering and safety notes

Keep stages separate: `candidates.txt`, `resolved.json`, `web-live.json`, and `in-scope.txt`. Re-resolve over time because DNS changes. Use resolvers responsibly, cap concurrency, and preserve CNAME evidence. Never feed unresolved or unconfirmed candidates directly into aggressive scanners.

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

<!-- DONE-083 -->
