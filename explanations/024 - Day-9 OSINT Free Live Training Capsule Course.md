# Explanation — OSINT Day 9: Facebook OSINT (Meta & Zuckerberg walkthrough + tool suite)

**Lecture:** 024 — Day 9, OSINT Free Live Training Capsule Course
**Translation:** [`english/024 - Day-9 OSINT Free Live Training Capsule Course.md`](../english/024%20-%20Day-9%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Days 6–8 (Twitter + LinkedIn) · **Continues to:** next session (rest of Facebook / Instagram expected)

---

## Part 1 — Why Facebook is special for OSINT

The instructor's thesis: Facebook is where people *live* socially — likes, comments, tags, friendships, feelings — accumulated over **years**. Nobody remembers their own old footprint, yet it stays searchable. Hence: *"forgotten activities… for hackers that information is very, very important,"* and the platform often yields **surprisingly accurate** information not found elsewhere (Twitter is limited; Facebook is a whole social life).

Same two-method frame as Twitter: **traditional** (manual, target-aware clicking) first, then **technical** (tricks + tools). Practical setup rules given before any demo:

- **Log in** — logged-out view is limited and can't reach maximum information.
- **Desktop version on Linux** — flexible, fast, and safer than mobile, where an accidental double-tap can drop a stray *like* on a paranoid target and burn the recon.
- **Notes in Google Docs** — pasted URLs auto-linkify, making a cross-platform intel file navigable.

---

## Part 2 — Traditional method

### Company page (target: Meta)
| Surface | Intel harvested |
|---|---|
| Browser "About Meta" search | Founders list; founded **Feb 2004, Cambridge**; website; links to FB/Twitter pages |
| FB search "Meta" → Pages | Ecosystem of pages: Business, Engineering, Meta for Media, Social Impact, For Developers, Education |
| Main page (4.2M followers) | Tagline, meta.com; Intro; photos (emoji-wise like reactor lists — thumbs-up vs heart counts — commenters) |
| **About → Page Transparency** | **Page ID**, creation date (Apr 1, 2020), **admin countries: India (15), Germany (1)…** |

The admin-country list is the quiet gem: it reveals **where the page's operators sit** — a staffing/geography lead no search trick would fabricate.

### Individual profile (Mark Zuckerberg)
Full About scrape: roles (founder), the non-profit run with his wife, CS/tech study, **lives-in / from**, **married to**, high school, places lived, contact & basic info (**DOB May 14, 1984**), **languages (English, Mandarin Chinese)**, family & relationships, "details about", favourites, **life events (first update years)**. Then:

- **Profile/cover photos clickable?** Opening them exposes the reaction lists (2.8M), comments, and **exact posting dates** (Oct 18, 2022; cover June 28, 2018 celebrating "2 billion people").
- **Friends + followers** tabs, photos/videos/reels — *check everything, leave no tab*.
- **In-profile search bar** — scopes keyword search to *that profile only* (demo: "meta" inside Zuckerberg's profile).
- **Watch videos where the target speaks** — spontaneous speech leaks information scripted posts never would.

The realism disclaimer repeats: one lecture can only teach *approach*; a real profile takes **15+ days** of gathering.

### Account-age estimation (no exact tool exists)
1. About → **life events** — the earliest update year brackets the creation year (1998-ish ⇒ created ~1997/98).
2. **Marketplace** — any listing the user created shows "Joined Facebook in …".

---

## Part 3 — Facebook search tricks (which Twitter tricks survive)

| Trick | Works on Facebook? | Notes |
|---|---|---|
| `*` wildcard (`Mark *`, `* Zuckerberg`) | ✅ | Same use: enumerate same-name people; **surname-wildcard → family members** |
| Related-search suggestions | ✅ (emphasised) | The platform's own related queries often surface what your query shape missed — *search them all* |
| Media keywords (`pictures`, `photos`, `videos`) | ✅ | Different keywords → genuinely different result sets |
| `AND` / `OR` logic | ✅ | **Run AND both ways** (spelled out and short-form) — the two variants return different results; OR = either-or |
| Location keyword combos | ✅ | e.g. name + Palo Alto |
| Tag/comment/like logic | doctrine | People tag friends & family only; comments = acquaintances or interest; likes = views — read them with a "hacker mind" |

Two standing orders: **grab the ENTIRE friends list** (select-all, copy) — never skip it; and **collect every possible keyword** during recon and try them all, because *"even a small bit of information can help compromise big systems."*

---

## Part 4 — Technical method: username vs user ID

The two artifacts tools demand:

1. **Username** — from the profile URL (`facebook.com/<username>`).
2. **User ID (UID)** — Facebook's numeric identifier, needed by most third-party tools for accurate, person-specific results.

Three ID situations/techniques:

- URL of the form `profile.php?id=<number>` → the number **is** the UID; it also means **no username was ever set**.
- **View Page Source → Ctrl+F "userVanity"** → the identifiers (username/UID, e.g. `893399…`) are embedded in the markup — the manual method when tools fail.
- **lookup-id.com** → paste a profile URL, get the UID (demo was flaky — "tools fail; do it manually").

---

## Part 5 — The tool suite (login-aware)

Meta-point the instructor drills repeatedly: **these tools don't crawl anything themselves — they build advanced Facebook-search URLs and redirect you into Facebook with the query assembled.** Therefore most of them **require you to be logged in** (a fake/research account is implied) — "you're not doing anything separately; they work WITH your search engine."

| # | Tool | What it does |
|---|---|---|
| 1 | **lookup-id.com** | Profile URL → numeric user ID |
| 2 | **OSINTCombine.com → Facebook tools** | Multi-tool kit: Get ID; **search by specific day / month / interval** (the `since:`/`until:` idea as a GUI — demo: all posts of a chosen date; Feb '23 search surfaced birthday/family posts); **location-ID search** (location's own page-source ID → "posts from Palo Alto, California"); **posts from UID X about keyword** (demo: UID **4** = Zuckerberg + "meta"); Instagram post-by-date |
| 3 | **intelx.io** | Similar advanced post search (keyword, month, interval from–to, from-someone-about-something), with its own grouped results interface; must be logged into FB to view |
| 4 | **Graph-scanner-style builder** (same suite) | Stacked clauses: add keywords + author UID + tagged location + date filter → "open in new window" |
| 5 | **Tabbed filter tool** | Posts / People / Photos / Pages / Places / Videos / Events with keyword + ID + location + year-month assembly |
| 6 | **Three-option tool** | (a) **mutual-friends comparer** (target UID + suspect UID → both friend lists — **currently broken after FB's update**); (b) **multi-keyword** search scoped to profile/page/group; (c) **find photos by multiple keywords** — all login-gated |

Workflow add-ons: always also chase the **related searches** after tool redirects; and learn to pull other ID types (**location ID, group ID, event ID**) from page source — the remainder was deferred to the next session when his system hung mid-demo.

---

## Part 6 — Ethics & closing doctrine

- **Black-hat mindset, ethical-hacker execution:** recon is performed *thinking* like an attacker (that's what makes gathering effective), but everything beyond public-OSINT stays legal and permission-based.
- Keyword diligence: note every candidate keyword during recon and search every one — "small bits compromise big systems."
- Courses admin: doubts window; **next session tomorrow** (the deferred "other IDs how-to" was promised then); the by-now ritual like/subscribe nag.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | 🔄 Twitter ✅ · LinkedIn ✅ · **Facebook ~mostly done (Day 9)** · Instagram pending |
| 4 | Emails, phone numbers, personal info | ⏭ announced |
| 5 | Website intelligence | |
| 6 | Steganography | |
