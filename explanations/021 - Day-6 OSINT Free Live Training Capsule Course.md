# Explanation — OSINT Day 6: Social Media OSINT — Twitter (Non-Technical Method)

**Lecture:** 021 — Day 6, OSINT Free Live Training Capsule Course
**Translation:** [`english/021 - Day-6 OSINT Free Live Training Capsule Course.md`](../english/021%20-%20Day-6%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Days 2–5 (dorking, image OSINT) · **Sets up:** Day 7 (technical Twitter OSINT tools)

---

## Part 1 — Why social media, and why Twitter first

Social-media OSINT is introduced as "everyone's favourite topic", planned across **Twitter → Facebook → Instagram → LinkedIn**. Twitter goes first because:

- People voluntarily broadcast **thoughts, interests, emotions** — raw material for profiling;
- Companies run official, active, high-signal accounts (support handles, promos, replies);
- LinkedIn (contrast drawn in class) is a *professional* network where interaction happens via posts/comments — it gets its own treatment later.

**Framing:** OSINT here is explicitly the **first phase of an ethical-hacking engagement** — everything gathered feeds later exploitation scenarios.

---

## Part 2 — The two-method model

| | Non-technical / "traditional" | Technical |
|---|---|---|
| Who | Anyone experienced with the platform | Hackers / ethical hackers (tools) |
| What | Manual browsing, searching, reading, correlating | Specialised tooling & automation (next class) |
| Key ingredient | **A hacking mindset** — manipulation techniques + domain knowledge applied to ordinary browsing | Built on top of manual findings |

**Ordering rule stressed hard:** *technical without non-technical gives no benefit.* Manual recon produces the usernames, names, relationships and context that tools then go deep on.

---

## Part 3 — Investigator OPSEC (safety steps)

Before any OSINT session:

1. **No mobile phones/apps** — a stray tap de-anonymises you and reveals where you're working from.
2. **Virtual environment** — VMware/VirtualBox, ideally **Kali Linux**; browse in **private tabs** (partial anonymity, better than nothing).
3. **VPN** for real anonymity — slower, but you become hard to trace.
4. **Note-making is non-negotiable** — OneNote / Google Docs / paper. And the golden rule: **never skip "unimportant" information** — *"believe me, all of it is important; it may matter only later."* More information ⇒ more hacking scenarios ⇒ better exploitation options.

Also: **sign in to the platform** for recon — logged-out access is rate/feature-restricted; full search and browsing needs an account ("you have to be inside that system"). (Tension with anonymity is implicitly resolved by using a research account, not your personal one.)

---

## Part 4 — The live demo: Paytm (educational only)

A strong, repeated **legal disclaimer**: the target (Paytm) is for demonstration only; students must not replicate against it; Defronix takes no responsibility for misuse.

### The workflow demonstrated

1. **Google "about <company>" first** → the knowledge panel / About page yields official **social handles, emails, phone numbers** — the anchor identifiers for everything else.
2. **Confirm authenticity** of the Twitter page (logo, details, cross-link from the official site) before trusting it — never assume the first search result is the real account.
3. **Harvest the handle family:** @Paytm, @PaytmCare, Paytm Money, Paytm Payments Bank, Paytm Business — every sub-brand handle is noted.
4. **Extract corporate facts from the bio/knowledge panel:** founder/CEO **Vijay Shekhar Sharma**, parent **One97 Communications**, operating areas (India, Japan).
5. **Walk every search tab** — People / Latest / Photos — because each leaks a different population: **employees** (esp. non-technical departments), **customers** (complaints reveal usage details), **managers/executives**.
6. **Open every tweet's replies, retweets, likes.** Nobody likes/retweets without a reason — each engager is a *customer, partner, employee or friend*, i.e. a lead. Example seen live: @PaytmCare replying directly inside a thread.
7. **Following vs Followers asymmetry:**
   - A company's **Following** list is curated → reveals partners, VIPs, friendly executives.
   - **Followers** are mostly customers/employees → a population to mine for individual targets.
8. **Pivot to individuals:** the founder's profile leaks **location (India), join date (Nov 2008)**; other profiles identify the **CEO of Paytm Money (Mumbai, joined 2013)**, the **CPO**, the **CFO** — and cross-checks (does the CFO follow the founder?) map the internal relationship graph. A followed "MD & CEO" (Radhika Gupta) hints at close industry friendships.

### The skill being taught: **correlation**

> *"Your biggest capability should be how well you can correlate things — link them, join them together."*

Tools come second; the differentiator is reading tweets/likes/replies/bios and **connecting** them into a relationship map and attack scenarios. Done fully, the attack surface becomes so large *"you'll run short of attacks."*

### Realistic time expectations

The demo covered "not even 1%… maybe 4%" in an hour. Real corporate recon takes **days to a month**. Slow, exhaustive, documented — *"don't leave anything on the Twitter page."*

---

## Part 5 — The security lesson on the defence side

The closing Q&A doubles as awareness training:

- Companies **prioritise business over security** and consciously accept exposure.
- Executives' accounts are often run by **social-media handlers** with no security awareness.
- **Mistakes are inevitable** ("we are human beings") — one wrong tweet can expose a company.
- Meta-point: *"As long as mistakes exist, the cyber-security field exists."*

For defenders, everything demonstrated is a checklist of what an attacker will read: support-handle replies, employee chatter, executives' follow lists, old tweets.

---

## Part 6 — Admin & next

- **Tomorrow: technical Twitter OSINT** (tools/automation), same time.
- Like/subscribe + comment on the **LinkedIn page** for attendance.
- Feedback invited openly (even dislikes).

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | 🔄 Day 6 — Twitter (non-technical); technical next |
| 4 | Emails, phone numbers, personal info | |
| 5 | Website intelligence | |
| 6 | Steganography | |
