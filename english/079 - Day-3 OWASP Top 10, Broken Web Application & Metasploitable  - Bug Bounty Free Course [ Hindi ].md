# Day-3 OWASP Top 10, Broken Web Application & Metasploitable  - Bug Bounty Free Course [ Hindi ] — English Translation

*Translated from: `079 - Day-3 OWASP Top 10, Broken Web Application & Metasploitable  - Bug Bounty Free Course [ Hindi ].hi-orig.srt`*
*Style: detailed edited translation; repeated live-chat, promotional passages, and rolling-caption duplication are consolidated.*

---

Day 3 establishes a legal web-security practice environment before live bug-bounty testing. The OWASP Top 10 is introduced as an awareness map of major web-application risk categories, not as a scanner checklist. The class names broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable/outdated components, identification and authentication failures, software/data integrity failures, logging/monitoring failures, and SSRF.

Each category must be learned through cause, behavior, impact, evidence, and remediation. Memorizing payloads without understanding application logic produces weak testing and weak reports.

The instructor introduces two deliberately vulnerable resources: **OWASP Broken Web Applications** and **Metasploitable**. Download the appliance from a trustworthy project/archive source, extract it, and import/open it in VMware or VirtualBox. These images contain intentional vulnerabilities and must never be exposed as normal production hosts.

Network design is critical. Put Kali and the target on the same isolated host-only or controlled NAT lab network. Avoid bridged mode, which can expose vulnerable services to the household, school, office, or public network. Take a clean snapshot. Find the target's private address from its console/DHCP information, verify connectivity from Kali, and open the hosted training applications in a browser.

The practice workflow is: choose one OWASP category; select a matching vulnerable application; capture a baseline request; reproduce the weakness; preserve minimal evidence; explain impact; identify the missing control; and reset state from a snapshot if necessary.

A live VPN certificate-verification problem is mentioned. Certificate errors should be diagnosed—clock, profile, chain, expiry, and configuration—not “fixed” by globally disabling verification.

The assignment is to complete setup and begin structured OWASP practice. The course will later add intelligent information gathering and permitted live programs, but labs come first so mistakes do not harm real users.

## Technical clarification and retained takeaway

Treat vulnerable VM downloads as untrusted. Verify hashes when available, disable shared folders/clipboard unless needed, isolate the network, and power targets off after practice. Keep a lab inventory with image version and snapshot. OWASP rankings change over time; use the official current document and supporting cheat sheets rather than relying solely on a lecture's year-specific list.

<!-- DONE-079 -->
