# Bug Bounty Day 6 — Shodan and public exposure research — Explained

## Lesson reconstruction

Day 6 uses Shodan as a search engine for internet-exposed services. Shodan indexes service banners and metadata observed on public IP addresses. Researchers can search by organization, hostname/domain, network, port, product, country, TLS certificate details, and other fields to discover exposure associated with an authorized program.

The first task is attribution. An IP mentioning a company name may belong to a CDN, cloud provider, contractor, or unrelated tenant. Verify through program scope, DNS history, certificates, WHOIS/RDAP, autonomous-system context, and current resolution. Never treat a Shodan result as authorization by itself.

Useful findings can include forgotten administrative panels, unusual ports, old product versions, database banners, development hosts, certificate names, screenshots, and cloud endpoints. Historical Shodan data can explain past exposure but may no longer be reachable.

The lesson discusses “secrets” carefully: banners, screenshots, HTML, or indexed files may accidentally expose API keys, tokens, credentials, internal names, or configuration. Do not use a discovered credential to access additional systems unless the program explicitly authorizes that validation. Preserve minimal evidence, redact the value, and report through the approved channel. Avoid downloading datasets or viewing user records.

Combine Shodan with DNS and certificate results. Search both exact hostnames and verified organization networks, then add confirmed in-scope services to the inventory with observation date, port, protocol, banner, and confidence. Validate gently with a single appropriate connection rather than launching broad exploitation.

Defensively, organizations should minimize public services, remove verbose banners, rotate exposed secrets, monitor attack-surface search engines, restrict management interfaces, patch supported software, and maintain ownership inventories.

## Engineering and safety notes

Shodan data can be stale and banners can be deceptive. A version string is not proof of vulnerability because vendors backport patches. Search API usage must respect account limits and program rate rules. Evidence should establish exposure and impact without publishing a reusable secret. If a key appears to belong to a third party, stop and coordinate through the program.

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

<!-- DONE-082 -->
