# Advanced Nmap — Explained

## NSE safety

Before execution:

```bash
nmap --script-help http-title
```

Read arguments, network behavior, and category. Pin the exact scripts rather than using broad `vuln` or `*` patterns against production.

## UDP

```bash
sudo nmap -sU -p 53,123,161 --version-light target
```

No response is ambiguous. ICMP unreachable can establish closed; protocol response can establish open. Rate limiting makes repeated aggressive probes less reliable.

## Accuracy controls

- scan hostname context when virtual hosting matters;
- preserve DNS resolution and timestamps;
- avoid `-A` until each component is justified;
- use selected ports/scripts;
- manually validate banners and findings;
- distinguish tool inference from confirmed fact.

## Evasion ethics

Techniques intended to bypass controls can violate program rules and monitoring expectations. They also make attribution/evidence worse. Do not use decoys because they generate traffic that appears to originate from uninvolved hosts.

## Review questions

1. What does `-A` enable?
2. Why is an NSE category not a safety guarantee?
3. Why does UDP yield `open|filtered`?
4. Why can OS detection be wrong?
5. Why are decoys unsuitable for normal bounty testing?

<!-- DONE-093 -->
