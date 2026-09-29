# Explanation — 049 — Day 5: Network Security (Free Capsule Course)

**Source:** `transcripts/049 - Day-5 Network Security Free Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/049 - Day-5 Network Security Free Capsule Course.md`
**Level:** Beginner security, Day 5 (trainer **Ayush Pathak**) — the **reconnaissance** lecture: the ethical-hacking chain, active vs passive recon, then hands-on with **whois, dig/nslookup, dnsdumpster, Shodan, VirusTotal, and the Wayback Machine**.

---

## 1. Framing — where attacks start

After four theory lectures (fundamentals module), the series enters the security module's first room. Two orienting pictures are drawn before any tool:

- **The 5-step ethical-hacking chain:** **recon → scanning/enumeration → gaining access (win an initial foothold) → maintaining access (persistence) → clearing tracks** — presented as a general, *iterative/cyclic* process, not a strict once-through pipeline.
- **The 3-band kill-chain diagram:** *getting in* (recon → resource development → **delivery** → **exploitation** past their protection) → *hacking through* (**persistence** → **command & control** of the target → **discovery** → privilege escalation → **lateral movement** inside the network → **collection/exfiltration**) → *taking it out* (**impact / objectives**). His promise: the track is a skeleton; he'll bolt on extras throughout.

Environment norm: the room runs against TryHackMe's **AttackBox** (a browser VM wired into their network; free tier ≈ 1–2 hrs/day, premium more) or your own Kali over the VPN — and the first three rooms of the module are free.

## 2. ACTIVE vs PASSIVE reconnaissance — the lecture's core

**The one-line test he drills:** *did you directly interact with the target or not?*

- **PASSIVE** — *binoculars from afar, never stepping onto the territory:* only **publicly-available** information; the target sees nothing.
  - **Public DNS/whois records** (already-covered rooms)
  - **Job-ad OSINT (the gem of the session):** read the company's **naukri.com postings** — "cyber-security analyst must know X language / Y framework" leaks **their internal tech stack** and hiring profile without asking anyone
  - **Company news/updates** and, in the quiz, the **Facebook page → employee names** (answer: PASSIVE)
- **ACTIVE** — *checking the locks on the doors and windows:* any direct engagement; the target can see you (packets, logs).
  - **Port scans** (requests hit the target), **ping/ICMP** ("it knows my packets are coming — logs get made")
  - **Banner grabbing:** connect to FTP/HTTP/SMTP servers and read what the service announces
  - **Social engineering** — even non-technical: the quiz's *meet the IT admin and sweet-talk network details* is ACTIVE (direct interaction of any kind counts)
- Demo that lands the point: on the Metasploitable-2 VM (**192.168.47.138**), a bare `telnet`/`ftp` connect returns the **service banner — including version — with zero login**. That's exactly where nmap's version detection reads from; it only fails when admins bother to hide/fix the banner.
- Legal-adjacent aside worth keeping: **companies do hire people to social-engineer their own staff** (posed as a new joiner) to expose human weak links — "humans are bundles of mistakes," and employees are where entry points live.

## 3. Toolset #1 — WHOIS

A **request/response protocol (RFC 3912)** — whois servers listen on **port 43**; registrars (GoDaddy, **Namecheap**) maintain the per-domain record. Fields to read: **registrar** (through whom bought), **registrant contact info** (usually **REDACTED — privacy services hide owner details**; his "unless privacy" caveat), **creation / updated / expiry dates**, **name servers**. Live: `whois tryhackme.com` on Kali.

## 4. Toolset #2 — DNS pulling (dig / nslookup)

- Baseline queries show the domain's IPs etc., answered **via the configured gateway resolver**.
- **Record-specific queries** — ask for **A** or **TXT** alone ("important intel hides in TXT records").
- **Custom resolvers:** point the query at a chosen server — Google **8.8.8.8**, Cloudflare **1.1.1.1** (the demo flips the resolver and re-runs) — prelude to why controlled resolvers matter later.
- Online equivalents give the same answers in a browser; the room's final **flag** is read off a record and submitted.

## 5. Toolset #3 — dnsdumpster.com

Free domain-intel web app: same concept, nicer presentation — a **zoomable host map** of the domain plus **PNG/XLS report exports**. Its subdomain-harvesting powers the room quiz: besides `www`/`blog`, which "interesting subdomain" exists for the target — options admin/testing/remote → **answer: `remote`** (admin fails when tried).

## 6. Toolset #4 — Shodan.io

The search engine for **internet-connected devices** (IoT cameras, exposed services): it shows **banners**, IPs, hosting providers, geolocation, ports—and crucially, **things you'd never get by directly touching the target** (a purely passive bonus). Room stats questions: second-top country by publicly-accessible devices (answer garbled in ASR); **third most-common port → 8080** (after 80 was rejected). Paid Shodan unlocks more — "barely matters at this stage."

## 7. Toolset #5+ — the overflow kit he name-drops

- **VirusTotal** → search a domain → **Relations** tab: **subdomains** (found *more* than dnsdumpster here) + **passive-DNS ↔ IP** mappings — directly ammunition for scope-testing in web hacking.
- CLI enumerators mentioned for later: **amass**, **subfinder**.
- Doctrine: **manual is best** — tools differ, the *concept* is one; google-dorking and friends sit in the same family.

## 8. Toolset #6 — the Wayback Machine (archive.org)

The internet's time machine: pick a date, see the site's **past state** (Facebook of 2018-02-18 vs today — dramatically different UI). Recon value: **information/technologies that were on the site earlier and later removed** — "brother, you *used* to use this stack…" is a clue about what they still run.

## 9. Assignment & channel norms

Finish the recon rooms yourself, **share the completed room**, and — his recurring plea, now with the **3K-subscriber celebration** on top — leave feedback on Telegram/comments: *views are coming but responses aren't; typed reactions decide which series continues.*

## 10. Study pointers

1. Sort these into passive/active without notes: reading whois · pinging the target · digesting naukri.com ads · telnet-to-FTP banner · browsing archived pages · chatting up the IT admin. (Answers: P, A, P, A, P, A.)
2. Hands-on: `whois <a real domain>` and find **all four**: registrar, dates, name servers, and the hidden-registrant privacy mask.
3. Practice the DNS trio: default query, **TXT-record-only** query, and the same query forced through **1.1.1.1**.
4. Same domain → run dnsdumpster + VirusTotal relations; diff the subdomain lists (his point: tools complement — manual/archival checks (Wayback) fill the gaps).
5. Explain in one breath *why a banner grab is classified as active recon but reading Shodan's cached banner of the same host is passive.*
