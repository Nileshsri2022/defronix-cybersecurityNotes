# Bug Bounty Day 1 — fundamentals and roadmap — Explained

## Lesson reconstruction

The course opens by defining a bug-bounty program from both sides. An organization publishes a policy and invites independent security researchers to test specified assets. A researcher who finds a genuine security weakness submits it privately with evidence and reproduction steps. Depending on the program, an accepted report may receive money, points, recognition, or only coordinated remediation.

A program is not permission to attack an entire company. Authorization comes from the individual brief: exact in-scope assets, accepted vulnerability categories, prohibited techniques, rate limits, data-handling rules, disclosure terms, and safe-harbor language. Anything not clearly included must be treated as out of scope.

Platforms such as HackerOne, Bugcrowd, and Open Bug Bounty connect researchers with organizations, list programs, receive reports, and support triage. Other public, private, crowdsourced, and independently hosted programs also exist. A vulnerability disclosure program may provide a reporting channel without promising payment. The instructor tours program listings to show where researchers read policies and submit reports.

Reconnaissance is introduced as the first technical phase: collect authorized public information, enumerate permitted assets, understand technologies and features, and create an attack-surface map. Recon is not uncontrolled scanning. Scope must constrain every tool and request.

The beginner roadmap is: learn networking, Linux, HTTP and web fundamentals; study vulnerability causes and impact; practise in TryHackMe and deliberately vulnerable applications; choose a program whose policy is clear; recon carefully; test one hypothesis at a time; minimize impact; save evidence; and submit a professional report. OWASP concepts and legal labs will appear throughout the course, followed later by testing explicitly permitted live targets.

A strong report contains a clear title, affected asset, prerequisites, numbered reproduction steps, request/response evidence, demonstrated impact, and remediation guidance. Stop after proving the issue; do not access unrelated user data or create unnecessary damage.

The instructor warns against treating bug bounty as guaranteed quick income. Duplicates, informative findings, and rejected reports are part of learning. Build judgment and communication rather than collecting payloads. Use only your own labs or targets for which the owner has granted explicit permission.

## Engineering and safety notes

Before testing, save the policy date and verify scope again because programs change. Separate discovery notes from sensitive evidence, redact tokens and personal data, and follow the platform's communication channel. Never use denial of service, social engineering, credential attacks, or automated volume unless the program explicitly allows them. Responsible research is defined as much by restraint and reporting quality as by technical skill.

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

<!-- DONE-075 -->
