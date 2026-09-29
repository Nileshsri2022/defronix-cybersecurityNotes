# Day-15 — Scanning Targets for Open Ports and Services — English Translation

*Translated from: `091 - Day-15 - Scanning Targets For Open Ports & Services Live Recon - Bug Bounty Free Course [Hindi].hi-orig.srt`*

---

Port scanning asks which TCP/UDP services an authorized target exposes. Begin with the program policy: many web bounties exclude infrastructure scanning, cloud/CDN addresses, denial-of-service behavior, or high-rate automation. Resolve only reviewed in-scope hostnames and verify IP ownership; shared hosting means an IP can serve unrelated tenants.

A port is a transport endpoint, not a vulnerability. Scanning identifies states such as open, closed, or filtered. Service detection then estimates protocol and version. Banners can be hidden, proxied, or misleading, and vendors backport patches, so a version string is not proof of a CVE.

Start with a narrow, low-rate TCP scan of common ports and save machine-readable output. Expand to all TCP ports only when authorized and necessary. UDP requires separate probes and is slower/less conclusive because silence can mean open, filtered, or dropped traffic. Avoid aggressive scripts until basic service identity and scope are clear.

Prioritize unexpected administration, database, remote-access, storage, debug, and development services. Validate with protocol-appropriate, non-destructive handshakes. Do not brute-force credentials or execute exploits merely because a service is open.

Record hostname, resolved address, time, tool/version, command, port, transport, state, service evidence, TLS name, and ownership confidence. Report exposed services only when a concrete weakness or prohibited exposure is demonstrated.

Defenders should minimize listening services, bind management interfaces privately, firewall by source, patch supported software, require strong authentication, segment systems, and continuously compare external exposure with inventory.

<!-- DONE-091 -->
