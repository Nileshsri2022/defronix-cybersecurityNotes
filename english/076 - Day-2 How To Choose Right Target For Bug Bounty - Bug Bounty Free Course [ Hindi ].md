# Day-2 How To Choose Right Target For Bug Bounty - Bug Bounty Free Course [ Hindi ] — English Translation

*Translated from: `076 - Day-2 How To Choose Right Target For Bug Bounty - Bug Bounty Free Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation; repeated live-chat, promotional passages, and rolling-caption duplication are consolidated.*

---

Day 2 explains that target selection is itself a skill. Beginners often choose the most famous program, repeat obvious checks already performed by thousands of researchers, receive duplicates or `Not Applicable` decisions, and become discouraged. Duplicates are normal, but thoughtful selection reduces avoidable competition.

The instructor compares two hypothetical programs. One has about five thousand active researchers, narrow scope, and slow triage. Another has fewer researchers, broader scope, and faster responses. The second initially appears better, but skill fit can reverse the decision: if the first program's technology and allowed vulnerability classes match what you understand deeply, it may offer better opportunities for you.

Important factors include scope size and clarity; web/API/mobile asset variety; wildcard domains and exclusions; program age; number of researchers; recent asset additions; triage and response history; reward ranges; eligible severities; account availability; product complexity; policy restrictions; and your own skills. The highest advertised bounty is not automatically the best first target.

Using a platform program page, the class examines **Scope and rewards**. Scope is the exact set of assets that may be tested, often with asset-specific eligibility. A company name is not scope. Third-party services, related brands, acquired domains, IP addresses, and production data remain excluded unless listed. A wildcard can include many subdomains but may still have written exceptions.

Read the complete policy: out-of-scope bugs, known issues, prohibited automation, rate limits, denial-of-service rules, social engineering restrictions, disclosure policy, and report requirements. If ownership is ambiguous, ask the program instead of assuming.

A practical method is to shortlist several programs and score each for authorization clarity, skill fit, accessible functionality, scope depth, competition, response quality, and realistic rewards. Spend a fixed trial period understanding one product instead of firing the same scanner at every domain. Read disclosed reports to learn the product's historical weaknesses without merely reproducing old findings.

The instructor's final advice is to choose a target where you can create accounts safely, understand workflows, investigate permitted features deeply, and produce a reproducible report. Motivation improves when your plan matches your present skills.

## Technical clarification and retained takeaway

Recheck scope before every test and before submission. Keep a scope inventory with source URL and date. Distinguish asset eligibility from bounty eligibility: some assets may accept reports but pay no reward. Track what you tested, assumptions, and results to avoid repeating shallow checks. Depth on one authorized product usually outperforms indiscriminate breadth.

<!-- DONE-076 -->
