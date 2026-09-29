# Day-3 OWASP Top 10, Broken Web Application & Metasploitable  - Bug Bounty Free Course [ Hindi ] — English Translation

*Translated from: `079 - Day-3 OWASP Top 10, Broken Web Application & Metasploitable  - Bug Bounty Free Course [ Hindi ].hi-orig.srt`*
*Style: faithful edited translation; repeated live-chat checks, promotions, and caption stutters are condensed.*

---

Day 3 establishes the legal practice environment needed before live bug-bounty work. The instructor introduces the OWASP Top 10 as a map of common web-application risk categories and demonstrates obtaining deliberately vulnerable virtual machines.

## Using the OWASP Top 10

The Top 10 is an awareness document, not a step-by-step scanner checklist. The lesson names categories such as broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, authentication failures, integrity failures, logging/monitoring failures, and SSRF. Each category must be studied through its cause, observable behavior, impact, remediation, and hands-on lab—not by memorizing payloads.

Students are assigned to review the official OWASP material and practise every concept in a legal environment. The instructor stresses that failing to build fundamentals leads to poor reports and unsafe testing.

## Deliberately vulnerable machines

Two resources are introduced: the OWASP Broken Web Applications project and Metasploitable. These are intentionally insecure images for an isolated lab. Download from a trustworthy project/archive source, extract the appliance, and import/open it in VMware or VirtualBox rather than treating it as a normal production OS.

Network configuration is critical. Use host-only or an isolated NAT lab so the attacker VM can reach the target but untrusted services are not exposed to the household, campus, workplace, or public network. Avoid bridged mode for vulnerable machines. Identify the target's private IP from its console or DHCP leases, verify connectivity from Kali, and browse to the hosted training applications.

## Safe workflow

1. Keep vulnerable VMs isolated and take a clean snapshot.
2. Start Kali and one target VM on the same controlled virtual network.
3. Discover the target and enumerate only that lab address.
4. Choose one OWASP category and reproduce it in the relevant training app.
5. Record request, response, impact, and remediation.
6. Revert the snapshot when an exercise damages state.

A VPN/certificate issue mentioned during the live session is treated as a connection/configuration problem, not a reason to weaken certificate validation globally. The long-term plan is to progress from labs to reconnaissance and only then to live assets explicitly listed in a program's scope.

<!-- DONE-079 -->
