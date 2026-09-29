# Nmap Part 1 — Explained

## Scan design

Decide before running:

- authorized hostname/IP range;
- TCP ports and discovery method;
- rate/concurrency allowed;
- required evidence/output;
- stop conditions.

Useful output:

```bash
nmap -sT -sV --top-ports 100 -oA scans/target target
```

`-oA` writes normal, XML, and grepable formats. XML is useful for parsing; retain the human-readable command and timestamp too.

## State model

Nmap infers state from responses or silence. Firewalls, packet loss, NAT, load balancers, and rate limits affect conclusions. Repeat only enough to resolve uncertainty; do not raise speed until a target responds.

## Common mistakes

- using `-Pn` against huge unverified ranges;
- running `-p- -A` as a first action;
- treating service labels as confirmed products;
- scanning shared IP neighbors;
- reporting an open port without a security impact;
- failing to save exact commands/output.

## Review questions

1. What changes when `-Pn` is used?
2. How do `-sT` and `-sS` differ?
3. Why save XML and normal output?
4. Why is `-p-` not always appropriate?
5. What does “filtered” actually establish?

<!-- DONE-092 -->
