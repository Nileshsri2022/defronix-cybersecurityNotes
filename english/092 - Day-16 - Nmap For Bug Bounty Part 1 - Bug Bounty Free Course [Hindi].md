# Day-16 — Nmap for Bug Bounty, Part 1 — English Translation

*Translated from: `092 - Day-16 - Nmap For Bug Bounty Part 1 - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

Nmap is a network mapper used for host discovery, port scanning, and service identification. The class begins with authorization and target selection: scan only assets explicitly covered by the policy, and do not convert an in-scope domain into an indiscriminate scan of shared/CDN infrastructure.

The default scan checks a common TCP-port set. `-p` selects ports, `-p-` selects all TCP ports, `--top-ports N` selects the most common N, and `-sV` performs service/version detection. `-Pn` skips discovery and treats the host as online; it is useful when discovery probes are blocked but can waste traffic across large lists. `-n` skips reverse DNS.

TCP connect scanning (`-sT`) completes connections; SYN scanning (`-sS`) uses raw packets and normally requires privilege. Open, closed, and filtered describe observed network behavior, not exploitability. Use conservative timing/rate settings and save output with `-oA` for reproducibility.

Examples for an authorized lab:

```bash
nmap -sT --top-ports 100 target
nmap -sV -p 22,80,443 target
nmap -p- --max-rate 100 -oA full-tcp target
```

Read results carefully. Service names are guesses based on ports/probes; version banners can be altered or proxied. Confirm interesting findings using a protocol-appropriate non-destructive request. Nmap's purpose in recon is to create an exposure inventory that guides careful manual investigation.

<!-- DONE-092 -->
