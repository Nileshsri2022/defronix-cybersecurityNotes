# Day-5 Live Recon For Gathering All Information  - Bug Bounty Free Course [ Hindi ] — English Translation

*Translated from: `081 - Day-5 Live Recon For Gathering All Information  - Bug Bounty Free Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation; repeated live-chat, promotional passages, and rolling-caption duplication are consolidated.*

---

Day 5 begins a structured reconnaissance workflow for an explicitly authorized bug-bounty target. Reconnaissance means building an accurate attack-surface inventory before testing vulnerabilities. The instructor distinguishes passive collection—using public sources without directly probing the target—from active enumeration that sends requests to in-scope systems.

Start by reading and saving the program policy. Record root domains, wildcard assets, exclusions, rate limits, prohibited automation, and third-party boundaries. Create a target workspace with separate raw, normalized, resolved, live, and notes files so every result has provenance.

Collect organization and domain context from search engines, certificate transparency logs, DNS records, public code and documentation, archive sources, and the program's own asset list. Search for subdomains and historical URLs, but treat every discovered name as a candidate until scope and ownership are verified.

Normalize and deduplicate results. Resolve DNS to distinguish live records from stale names. Record A/AAAA/CNAME/MX/NS/TXT data. CNAME chains can reveal cloud/SaaS dependencies; they do not automatically authorize testing the provider. Probe permitted web hosts gently to collect status code, title, redirect, technology hints, and final URL.

The class emphasizes note-taking: tool, date, command, source, output, and interpretation. Recon is iterative. A login page may reveal API hosts; JavaScript may reference paths; documentation may expose a staging hostname. Feed new candidates back through scope validation and normalization.

Do not confuse volume with quality. Thousands of unsorted subdomains are less useful than a smaller verified inventory tagged by function and ownership. Avoid high request rates and never scan unrelated IP ranges merely because an in-scope name points to shared hosting.

The output of recon is an attack-surface map and prioritized hypotheses, not an immediate vulnerability claim.

## Technical clarification and retained takeaway

A reproducible pipeline stores raw source output before transformation, uses lowercase/canonical hostnames, strips wildcard noise, resolves with multiple trusted resolvers when necessary, and timestamps observations. Detect wildcard DNS to avoid false positives. Separate `in-scope`, `needs confirmation`, and `out-of-scope` inventories; tools should consume only the first.

<!-- DONE-081 -->
