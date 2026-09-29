# Day-17 — Advanced Nmap for Bug Bounty, Part 2 — English Translation

*Translated from: `093 - Day-17 - Nmap Advanced For Bug Bounty Part 2 - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

Part 2 covers deeper Nmap features after basic port discovery. OS detection (`-O`) infers a fingerprint and is uncertain through firewalls, virtualization, and proxies. `-A` combines OS detection, version detection, default scripts, and traceroute; because it is noisy and broad, it should not be a default bug-bounty command.

NSE scripts automate protocol checks. Categories include `default`, `safe`, `discovery`, `auth`, `vuln`, `intrusive`, `brute`, and others. Category names are not permission: inspect a script's documentation/source before running it. Avoid brute-force, denial-of-service, exploit, and intrusive scripts unless explicitly authorized.

Examples in a controlled lab:

```bash
nmap -sV --script safe -p 80,443 target
nmap --script http-title,http-headers -p 80,443 target
nmap --script-help SCRIPT_NAME
```

UDP scanning (`-sU`) is slower and often returns `open|filtered`; target selected ports and use protocol-aware probes. Timing templates and `--min-rate`/`--max-rate` influence load and reliability. Faster is not automatically better.

Firewall-evasion flags, fragmentation, decoys, spoofing, and source-port tricks are explained as network concepts but are inappropriate for most bounty programs and can affect third parties. The practical objective remains accurate inventory, minimal traffic, and manual verification of meaningful exposure.

<!-- DONE-093 -->
