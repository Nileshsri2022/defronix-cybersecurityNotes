# Explanation — OSINT Day 10: Facebook Finale — URL Manipulation & the Tool Barrage

**Lecture:** 025 — Day 10, OSINT Free Live Training Capsule Course
**Translation:** [`english/025 - Day-10 OSINT Free Live Training Capsule Course.md`](../english/025%20-%20Day-10%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 9 (Facebook OSINT, search tricks, tool suite) · **Closes:** TVe Facebook block (Instagram next if the course continues)

---

## Part 1 — Housekeeping & the leftover ID problem

- Recap: Facebook OSINT was essentially done; students' outstanding challenge was finding **event / page / group IDs**. Answer: one technique for all — open the object → **View Page Source → Ctrl+F** for `page_id` / `event_id` / `group_id`; or dump the source to a text file and **`grep`** it. Same family of method as location ID and user ID from Day 9.
- A **text file listing all tools** from this class was promised to the Telegram group; the course's continuation (and the promised medium-level labs mixing image-reverse + dorking) goes to a **group poll**.
- Framing: a standalone OSINT course elsewhere would cost money and still be shallower than this detail.

---

## Part 2 — The centerpiece: manual Facebook URL manipulation

The doctrine: **never be tool-dependent.** Every tool from Day 9 merely assembles Facebook-search URLs — so if the tools die, manufacture the URLs by hand.

### URL anatomy (as dissected live)

```
https:// www.facebook.com /search/top ?q=mark &filter=<base64(JSON)>
└protocol┘ └──domain────┘ └──path/category──┘ └query keyword┘ └─filtered view─┘
```

- **Main categories** = the `search/<category>` segment: `top`, `posts`, `people`, …
- Every category has **sub-categories** (People → Friends, City, Education; Top → Sort-by, Posts-from, Post-type, Posted-in-group…), and each sub-category offers **filter options** in the left-hand UI.
- Applied filters are serialized into the URL as **`filter=` + base64-encoded JSON**. Pasting raw JSON into the URL errors out — Facebook only accepts the encoded form. Paste a well-formed compact JSON → encode → it works ("it will show output your way").

### The pipeline (single filter)
1. Set UI filters as desired → read the produced `filter=` value from the URL.
2. **Decode** base64 → JSON to understand the schema (keys per sub-category).
3. Edit JSON values by hand (drop in a **page ID** or **location ID** found via page-source, e.g. Zuckerberg's Palo Alto "tagged location").
4. **Remove all spaces** (a JSON formatter's *Compact/Process* — also validates the JSON).
5. **Base64-encode** → paste after `&filter=` → Enter. The results honour the filter; the left UI even highlights the active facets.

### Combining filters — the merge rules (heavily tested in Q&A)

| Rule | Content |
|---|---|
| R1 | A sub-category's multiple options are **mutually exclusive** — you can't take "posts from you" **and** "posts from friends" (same sub-category) |
| R2 | You **can** combine **one option per sub-category across sub-categories of the same main category** — e.g. `Most recent` + `Posts from pages` + a Post-type (3–4 clauses fine) |
| R3 | You **can never** merge filters from two **different main categories** (`search/top` × `search/posts` = invalid) |

**Merge mechanics:** JSON = `{ … }`. To fuse two filter objects: **delete first's closing `}` + second's opening `{`, join with a comma** → compact → encode → paste. Warning: after driving results via the URL, **don't re-use Facebook's own search bar** in that flow — it resets the query to Facebook's rules.

Deliverable: a **shared document** with the category/filter JSON schemas — students must experiment (the instructor's recurring line: "your job is to practice").

---

## Part 3 — Private accounts → the friend pivot (social engineering as last resort)

If the target locks down their account:

1. **"Will all their friends be private too?"** — enumerate friends, close friends, relatives, group members; find one public profile.
2. **Target the friend.** Their timeline/comments/tags inevitably leak the private target — *you can't guarantee your friends' privacy*: a comment left, a location shared with friends, a tag — all public on the friend's side. (Self-test: privatise your own account and see what your friends still expose about you.)
3. Friends are **softer targets** — easier to befriend and manipulate ("create a movie-type scene"; classic pretexting) — then harvest the target through them.

This is the deliberate ethical boundary: flagged as **the last option**, consistent with the black-hat-mindset/ethical-execution rule from Day 9.

---

## Part 4 — Multi-account detection & the tool barrage

**Messenger trick:** search first+last name in **Messenger** → result list frequently reveals a linked **Instagram** account (Discover section) — quick multi-account confirmation.

| # | Tool | Type | What it does |
|---|---|---|---|
| 1 | **Profil3r** (GitHub CLI) | name/username enumeration | `git clone` → `python3 … -h` / `-p <name>` → pick separator (`.` `-` `_`) → selects: emails, domains, forum posts, **Facebook/Instagram/LinkedIn/MySpace/Twitter** presence → cascades into emails → images → multiple linked accounts |
| 2–3 | Two **reverse-image web apps** | photo pivot | Upload the target's profile picture → find every site/social account reusing it. Pro tip: for small 2–5-person practice targets, run **every photo** through both |
| 4 | **whatsmyname.app** | exact-username sweep | Checks the username against a **581-site** database; lists hits (dev.to, forums, gaming sites…) — demoed with `mark` |
| 5 | **namecheckup.com** | username availability map | Color-coded: **green = exists**, red = none/free, yellow = uncertain — *has false positives/negatives* (Telegram demo came yellow); click-through to verify (Facebook "mark" resolved correctly) |
| 6 | **FBI – Facebook Information** (`git clone`, `pip install -r requirements`) | token-driven friend-graph dump | Log in with FB email/password → **generate access token** → `get_data` caches the friends' data; `get_info` per friend; **dump phone numbers & emails** where public; dump IDs; outputs **JSON + HTML**; a bot module (even mass-actions on the token account's friends' posts) is **stale/needs updates** — "if you know Python scripting, you can operate [repair] it" |

Instructor's guarantee: if the flashy tools fail, **the manual URL technique "works 100%"** — which is why it was taught before the tools.

---

## Part 5 — Outro Q&A (laptop advice) & admin

- **Specs for hacking practice:** 16 GB RAM minimum, 4–6 GB graphics, **i5 minimum** (i7 better) — because the real bottleneck is **processing** (VMs in VirtualBox + programming alongside); brand irrelevant. A buying-guide video is on the channel; avoid "pen-drive hacking OS" gimmicks (too slow, money-trap).
- **Facebook OSINT: officially finished.** All tool lists/screenshots promised to the group; continuation (Instagram etc.) subject to the **group poll**; if approved, **first session Sunday**.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | 🔄 Twitter ✅ · LinkedIn ✅ · **Facebook ✅ complete (Days 9–10)** · Instagram pending (continuation vote) |
| 4 | Emails, phone numbers, personal info | ⏭ announced |
| 5 | Website intelligence | |
| 6 | Steganography | |
