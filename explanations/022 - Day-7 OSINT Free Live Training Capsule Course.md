# Explanation — OSINT Day 7: Twitter Technical Method — 9 Search "Tricks"

**Lecture:** 022 — Day 7, OSINT Free Live Training Capsule Course
**Translation:** [`english/022 - Day-7 OSINT Free Live Training Capsule Course.md`](../english/022%20-%20Day-7%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 6 (non-technical Twitter recon on Paytm) · **Continues:** more tricks next class

---

## Part 1 — Where this fits

Day 6 produced the raw material by hand: handles (@Paytm, @PaytmCare, @PaytmMoney, @PaytmBank, @PaytmBusiness), people (founder Vijay Shekhar Sharma, Paytm Money CEO Varun Sridhar, CPO/CFO), interests, locations. Day 7 turns that into **precise queries** using Twitter's advanced search operators — the "technical method". Key premise repeated: *technical without non-technical is useless* — every operator below needs a seed (name, surname, hashtag, date, place) that only manual recon provides.

Teaching format: **tricks only, not full recon** — a complete pass over a company's Twitter would take *"one–two months."*

---

## Part 2 — The nine tricks

### 1. `*` wildcard — enumerate people around a name
- `Vijay Shekhar *` → every handle beginning with the name.
- `* Sharma` → everyone with the surname at the end.
- **The insight:** the executive is security-aware; his **family members are not**. Relatives almost always keep the family surname in their profiles — so surname-wildcarding is a family-member enumeration technique. Expect noise (Anushka/Kapil/Rohit Sharma…) — every suspect profile must be opened and checked manually.

### 2. Date-scoped search (month/year)
Scope a keyword/handle to a **specific month or year** you suspect activity in (from prior intel/news). Gives *"accurate results instead of random results."* Corresponds to Twitter's date-restricted search (see trick 9 for exact dates).

### 3. `#hashtag` — confirm interests
A single football tweet might be noise; **regular** engagement on `#football` confirms a genuine interest. Interests = future phishing/social-engineering hooks. Hashtags combine with the date scope (tricks 2+3) — the revision example: a target who used to post stadium selfies with `#cricket` + location, then stopped after security training; old date-scoped hashtag searches still recover the exposure.

### 4. `from:` / `to:` — relationship verification
| Query | Returns |
|---|---|
| `from:A to:B` | A's tweets addressed to B |
| `from:B to:A` | the reverse direction |
| `from:* to:A` | everyone tweeting at A |
| `from:A` | all of A's tweets |
| `from:A keyword` | A's tweets containing the keyword |

Purpose: **confirm** a suspected friend/partner/high-profile-employee link by finding actual tweet communication — and read *what topic* they discussed (projects, policies = "hot issues" for later scenarios).

### 5. `filter:` — media narrowing
`filter:images`, `filter:videos`, `filter:periscope` (live) — combined with any handle/keyword/hashtag. Rationale: most substantive posts carry media; filtering kills the noise and narrows output. Framed as a differentiator: *"these tricks only hackers have — a normal user has no use for narrowing down."*

### 6. Logic: `AND` / `OR`
- `@A AND @B` → posts mentioning **both** ⇒ proof of some relationship (an information leak that helps you link people).
- `@A OR @B` → three result classes (both / only A / only B).
- Works with keywords too; combine like Linux pipelines — more combination, better output. Demo surfaced a customer rant comparing Paytm to WeChat, addressed to both accounts.

### 7. `near:"place" within:Xkm` — geographic recon
- Seed: any exposed location (profile says "India" — too big; a reply mentioning **Gurgaon** — usable).
- `near:Gurgaon within:5km` + handle/hashtag draws a **perimeter circle** and returns tweets from inside it.
- Who's in the circle? **Customers** (they also confirm the location) and **friends/partners/relatives/neighbours**.
- The social insight: family back in the hometown brags to a favourite neighbour; the neighbour then comments on everything to get noticed ("I'm from your village!") — **neighbours and proud relatives become an attacker's entry steps.**

### 8. `-` exclusion
- `@handle -keyword` → drop posts containing the **word** (e.g. `-Paytm`).
- `@handle -@Paytm` → drop posts mentioning the **account** — the @ changes what gets excluded (word vs username).
- Syntax rule for all operators: **no space** after the operator/hyphen.

### 9. `since:` / `until:` — exact date ranges
- `since:2018-01-20 until:2019-01-01` → only that window's posts.
- More precise than trick 2; used when intel points at a launch/announcement window where partners, colleagues and customers were talking.
- Live find: an old reply asking *"do you have a connection with Vijay Shekhar?"* → evidence of a **former friendship**. The instructor's follow-on lesson: an **ex-friend/ex-partner is a prime secondary target** — they hold insider knowledge and may be more willing to talk (social engineering / manipulation techniques).

---

## Part 3 — Doctrine woven through the demos

1. **Seeds before operators.** Every trick consumed something from Day 6's manual recon (surname, hashtag, suspected friend, Gurgaon mention, 2018 hunch). Operators amplify intel; they don't create it.
2. **Confirm, don't assume.** Hashtag regularity confirms interests; `from:/to:` confirms relationships; `near:` confirms locations. Each operator is framed as a *verification* instrument.
3. **The weak ring around the target.** Family (unaware, surname-keeping), neighbours (attention-seeking), ex-friends (knowledgeable, disgruntled) — the technical tricks systematically map the human perimeter rather than the hardened centre.
4. **Combine operators** (hashtag + date, username + filter + exclusion, near + within + hashtag) — like chaining commands in Linux.
5. **Time honesty:** real target work = 10–15 days minimum, months for big targets — the tricks exist precisely to make that time productive and the results accurate.
6. **Ethics:** same standing disclaimer — educational purposes only; the demo deliberately avoids revealing private individuals.

---

## Part 4 — Admin & next

- More tricks remain — **continued next class** (announcement in the group about whether the session runs tomorrow).
- Students are expected to redo the queries themselves: *"information gathering is YOUR work; my work today is only to tell you the tricks."*

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | 🔄 Twitter: non-technical ✅ (Day 6), technical tricks 1–9 ✅ (Day 7), more pending |
| 4 | Emails, phone numbers, personal info | |
| 5 | Website intelligence | |
| 6 | Steganography | |
