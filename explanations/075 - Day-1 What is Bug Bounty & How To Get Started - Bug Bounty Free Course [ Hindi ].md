# Bug bounty fundamentals and a beginner roadmap — Explained

## Lesson map

The course opens by defining bug bounty from both sides. An organization publishes rules and invites independent security researchers to test specified assets. Researchers responsibly report valid security weaknesses; depending on the program, accepted findings may earn money, points, recognition, or a place in a hall of fame. This is authorized testing under a policy—not permission to attack anything associated with the company.

## Programs and platforms

A bug-bounty platform connects organizations and researchers, hosts program briefs, receives reports, supports triage, and may coordinate rewards. The instructor tours well-known public platforms such as HackerOne, Bugcrowd, and Open Bug Bounty while noting that many other platforms and independently hosted programs exist. Programs can be public or private and paid or recognition-only. A vulnerability disclosure program may provide a reporting channel without promising a bounty.

Before touching a target, read the brief completely: in-scope assets, out-of-scope assets, accepted vulnerability classes, prohibited testing, rate limits, safe-harbor terms, disclosure rules, and reward table. Platform membership never overrides the individual program's policy.

## The beginner workflow

1. Build web, networking, Linux, and HTTP fundamentals.
2. Learn vulnerability concepts rather than collecting payloads.
3. Practise in legal labs such as TryHackMe and deliberately vulnerable applications.
4. Choose a clearly authorized program and read its scope.
5. Perform reconnaissance to understand the exposed attack surface.
6. Test carefully, minimize impact, preserve evidence, and stop after demonstrating risk.
7. Submit a reproducible report and communicate professionally with triage.

Reconnaissance is described as the opening stage: collect public information, enumerate authorized assets, understand technologies and features, and form hypotheses. It is not a license to scan unrelated infrastructure.

## Course plan and expectations

The instructor plans to combine concepts, labs, OWASP-style vulnerability classes, reconnaissance, platform navigation, and eventually testing of explicitly permitted live targets. Students are asked to maintain notes and a vulnerability checklist, choose a target based on what they are currently learning, and accept that duplicates and rejected reports are part of developing judgment.

The closing principle is legality and patience: use only labs or assets for which permission is explicit, do not chase income before learning the fundamentals, and focus on writing reports that help an organization reproduce and fix a real security issue.

## Review checklist

- Work only on assets explicitly included in an authorized lab or program scope.
- Explain the purpose and risk of each step rather than copying commands blindly.
- Test success, failure, and invalid-input paths.
- Record observations and preserve enough evidence for reproducible notes.

<!-- DONE-075 -->
