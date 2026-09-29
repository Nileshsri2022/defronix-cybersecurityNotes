# Open-Port and Service Scanning — Explained

## Safe progression

```text
policy → scope hostnames → DNS/ownership → common TCP ports
→ service detection → targeted validation → evidence
```

Example, only within authorization:

```bash
nmap -sT --top-ports 100 --max-rate 50 -oA scans/common target
nmap -sV -p 22,80,443 -oA scans/services target
```

`-sT` uses completed TCP connections and works without raw-packet privileges. SYN scanning, OS detection, NSE scripts, and full-port scans add traffic/complexity and require explicit judgment.

## Interpretation

- **open:** application accepted/responded;
- **closed:** host reachable but no listener;
- **filtered:** filtering prevents a definite result;
- **open|filtered:** common ambiguous UDP result.

Scan through both hostname and address context. TLS SNI/HTTP Host routing can make direct-IP behavior unrelated to the in-scope virtual host.

## Evidence and ethics

Save `.nmap`, XML, and grepable/JSON-compatible output as appropriate. Sanitize it before sharing. Do not equate `ssh open` or `mysql open` with vulnerability; demonstrate missing access control or risky configuration safely.

## Review questions

1. Why does hostname scope not automatically authorize every resolved IP?
2. Why are UDP results ambiguous?
3. Why is banner version insufficient CVE proof?
4. When should an all-port scan be avoided?
5. What makes an exposed service reportable?

<!-- DONE-091 -->
