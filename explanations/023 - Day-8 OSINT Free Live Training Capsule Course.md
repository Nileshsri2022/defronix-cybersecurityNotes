# Explanation — OSINT Day 8: Twitter Finale (lang/geocode, tools, doctrine) + LinkedIn OSINT

**Lecture:** 023 — Day 8, OSINT Free Live Training Capsule Course
**Translation:** [`english/023 - Day-8 OSINT Free Live Training Capsule Course.md`](../english/023%20-%20Day-8%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 7 (Twitter tricks 1–9) · **Continues to:** Facebook OSINT, then email/phone OSINT

---

## Part 1 — The last two Twitter tricks

### Trick #10 — `lang:` (language-specific search)

Twitter lets you filter tweets by language using ISO-639-style codes (`en`, `zh`, `bn`, `hi`, …), referenced from a public codes list. The instructor's use-cases:

1. **Detect multilingual targets.** Read the target's tweets first; if they reply in another language, scope queries to it. Companies operating in multiple countries have multi-language footprints — foreign clients, foreign employees.
2. **Pivot to softer foreign friends.** If the target chats in Chinese with a friend, the friend is likely foreign — and "your target may not be compromisable, but the foreigner friend might be." The friend becomes a social-engineering pivot who may "provide much more information about your target."
3. **Confirm foreign business.** Any verified other-language tweet chain confirms the company has foreign clients — more personas to target.

### Trick #11 — `geocode:lat,long,radius`

The most precise location operator: `geocode:<latitude>,<longitude>,<radius>` (e.g. `... ,5km` or `30km`).

- **Get coordinates**: right-click a spot in Google Maps; or resolve a known **PIN code** via `geocode.xyz` when you only have the postal code from recon.
- **Combine with a keyword/handle** so only relevant tweets inside the circle surface.
- **Radius sweeping as convergence**: start 100 km → 50 → 30. If results exist at 50 but not 30, the activity lives in the 30–50 km ring — each iteration "reaches closer to the target," giving a quasi-tracking capability over who (customers, employees, partners) tweets from the zone.

### Compound queries — parentheses

Multiple operators can be grouped in parentheses so the engine searches each clause and returns the **combined** result — e.g. keyword + `since:` + `until:` + filter + `geocode:`. Purpose: verification and accuracy after bulk recon. Example surfaced live: a customer's Paytm fee complaint from July 2019.

With tricks 1–11, the **Twitter block is complete**.

---

## Part 2 — Tools (both need hands-on practice)

### One Million Tweet Map

A web app plotting **geotagged tweets from roughly the last 24 hours** on a map, with counts and near-exact locations. Searchable by keyword, hashtag, or username (@Paytm demo → pins in Ludhiana etc.). Two hard conditions:

1. The tweet must be **recent** (the map re-geos continuously; it also reshows whatever it has captured with location).
2. The user must have granted Twitter **location access** when tweeting.

Consequences called out by the instructor: a **security-aware target who disables location access is invisible** to it; and no guarantee a person of interest appears at all. Broader warning: fast/automated apps can yield **false positives** or simply not work — **manual analysis is slower but more reliable**.

### Reverse-image-search browser extension

A browser extension ("R-I…" style) that adds a **reverse** icon on posts/images for one-click reverse image search. Setup notes: enable it and tick **"Run in private windows."** Demo was laggy — students told to try it and report working/not-working in the group.

---

## Part 3 — Recon doctrine (the motivational segment)

The instructor paused to harden working habits. Key teachings:

1. **Focus is the job.** "When it comes to hacking, we need to focus" — box yourself onto one particular thing; strong focus is what lets you analyse/read/collect more.
2. **Don't get disappointed.** Links that refuse to form today often click "automatically in 10–15 days" as an image forms in your head. Just try, and keep doing.
3. **Note everything — relevant *and* irrelevant.** After each session (e.g. 2 hours), write down every finding.
4. **Re-read notes every day before resuming.** Going through prior notes keeps facts loaded in memory, which is what allows linking; refreshed context also tells you the next step ("by doing this you can easily guess what your next steps will be").
5. **Expect low yields.** A month of work may produce 10–15 pages, of which only 2–3 pages link with each other. That's normal.
6. **Unlinked info is a future exploit key.** Keep reviewing notes even in later stages (scanning → enumeration → vulnerability analysis): a fact you couldn't link during recon may "just work" later — *"the linked information to explore the thing, and the unlinked information to exploit it."*
7. **Information gathering is stage one of hacking** — it receives the most time; skimping it makes every later stage frustrating.

---

## Part 4 — LinkedIn OSINT

### Why LinkedIn
Business professionals live here, so the data is **strong information** — richer and more structured than Twitter's. It also **verifies and links** facts found elsewhere: social-media OSINT is cross-platform by nature.

### Company-page checklist (demoed on the instructor's own *Defronix Cyber Security* page)
| Area | What you pull |
|---|---|
| About/Home | Tagline ("India's leading cyber-security technology training…"), website, industry, follower count (245) |
| Posts | Likes/comments → students, trainers, support team, maybe a receptionist — *possible employees*; active trainings/courses |
| Jobs | Whether the company is currently hiring (none at demo time) |
| People | Employee list (22) **with locations** — India, Maharashtra, Haryana, Greater Delhi Area |

### Individual-profile checklist (demoed on the founder)
Headline roles (founder / co-founder / content creator) → location (Patna, Bihar — self-exposed) → Contact Info (LinkedIn URL, website, blog, YouTube, **email address**, **birthday**, address) → posts/comments → experience → education (Rajasthan Technical University, B.Tech CSE, 2016; 10+2; 10th) → licenses/certifications → skills → connections.

### Two pivotal lessons
1. **Display name ≠ username.** The real username is in the URL — `linkedin.com/in/<username>` — for LinkedIn *and* for Facebook/Twitter/Instagram.
2. **Username pivot.** Google the username to find the same handle elsewhere — the demo instantly found matching IDs on a personal website, YouTube, Instagram, Facebook and Telegram. If the literal name fails, try the stylised/brand username, since IDs are usually built on the popular handle.

### Target triage (offensive tradecraft)
- Enumerate **all** employees (present *and* past) — 22 profiles checked one by one.
- **Skip the tough ones** — threat hunters / security professionals — but keep them in the target list for later.
- **Prefer HR, marketing and other non-technical staff** — "easy targets" with less security awareness and more leakage.
- **"People also viewed"** side panel = a follower/friend radar; if the primary target won't compromise, find the weak friend there and **hop target → target → company**.
- **Order of operations**: run LinkedIn first (richer data), then Twitter, and **compare** the two — the comparison strengthens your links ("your information-gathering skill gets stronger").

### Paytm sweep (live)
LinkedIn search alone yielded: Junior Manager (NOC team), Software Engineer at Paytm (Delhi / Chandigarh / Punjab), Senior QA Engineer, Junior Manager Marketing Design (team lead, graphic design) — with education and skills exposed — i.e. titles + locations handed over "openly," info that Twitter never gave.

### Plugins — the teaser
Two–three LinkedIn **plugins/extensions** (registration required; full list promised later, in the email-OSINT segment) reveal data the platform itself hides. Live demo with a **ContactOut-type** plugin on "Rahul's" profile: clicking *View email* exposed **two emails** — a `@paytm.com` work address and a personal Gmail — neither visible on the page (no phone number that time). Another plugin surfaced location + employer + "8 years experience."

### End-state of social-media OSINT
Likes/dislikes, feelings, favourites, mobile numbers, personal + business emails, appearance — enough to **prepare an attack surface** and choose attacks, chiefly **social engineering and phishing** (which needs the email).

---

## Part 5 — Admin notes

- Practice targets: **Bugcrowd / HackerOne** programs are legitimate ground for running this whole workflow.
- After social media (Facebook/Instagram) finishes → **medium-level labs** for realistic practice.
- **Next session (tomorrow):** Facebook OSINT demo, then email OSINT and phone OSINT steps; the plugin list will be handed out then.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | 🔄 Twitter ✅ complete (Days 6–8) · LinkedIn ✅ basics (Day 8) · Facebook next |
| 4 | Emails, phone numbers, personal info | ⏭ announced (plugins list pending) |
| 5 | Website intelligence | |
| 6 | Steganography | |
