# Explanation — OSINT Day 11: Live Lab Solve (the "Sakura"-style OSINT room)

**Lecture:** 026 — Day 11, OSINT Free Live Training Capsule Course
**Translation:** [`english/026 - Day-11 OSINT Free Live Training Capsule Course.md`](../english/026%20-%20Day-11%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** everything so far (image forensics, username pivots, Twitter tradecraft) · **Continues to:** Day 12 — lab tasks 5 & 6 + a harder OSINT room

---

## Part 1 — Why a lab session

Students had been asking for hands-on tasks instead of passive video-following. The instructor obliges with a beginner/medium **TryHackMe-style OSINT investigation room** walked through live. Two stated purposes: (1) prove that the techniques from Days 2–10 chain together end-to-end; (2) give everyone a legal, info-rich, permanent practice target (labs stay up even if platforms update — "the techniques remain roughly the same").

Format: staged investigation text + hints + questions that must be answered to progress.

---

## Part 2 — Task chain as solved live

### Stage A — image forensics → the username
- Scenario text: no major breach damage, but forensics found **an image left behind by the criminals**. Hint language: information lives "beneath the surface" of files.
- Technique: open the image + **`exiftool`**; the file's **export path** (`/home/<username>/Desktop/…`) survived in the metadata — the attacker forgot to scrub it (or left it as a boast). The path's home-directory component = **a username** (the transcript only preserves that it ended in "…Angel").
- **Pivot #1:** Google the username → **Twitter account**, an article byline, and an **Instagram page**. Q1 (*what username does the attacker go by?*) solved.

### Stage B — OpSec autopsy (the two fatal mistakes)
The lab itself narrates them; the instructor unpacks the doctrine:
1. **Catalogue hygiene** — metadata left in an uploaded/"trophy" artifact.
2. **Username reuse across platforms** — one unique handle makes cross-platform correlation trivial ("most digital platforms make it easy to find other accounts owned by the same person when the username is unique"); job/community sites then leak **real-world identity** (full name, location).
- Twitter sweep (Days 6–8 tradecraft): 21 followers / 1 following (Microsoft), tweets disclosing habits (meet-up reminders, phone upgrades, "regular Wi-Fi and passwords"), dark-web boasting ("anyone who wants them will have to do a real deep search"), a vanished paste page ("last page got removed when the website changed domains"), a **self-introduction tweet containing a second, different @handle**, and **travel/season clues** — "cherry blossom season," "close to home, can't wait to finally be back," "taking out some last-minute cherry blossom" — i.e. seeds for the later **geolocation** answer.
- Identity questions solved here: full email (next stage) and **full real name** (recovered from the pivot set).

### Stage C — GitHub → GPG → email
- The username pivot also exposes a **GitHub account**: a hello-world Java repo, a suspicious "worker ID/password" file, a **PGP repo**, and a **Bitcoin repo**.
- Technique taught: **PGP/GPG public keys embed identity metadata.** Copy the repo's public key (`Raw` → save as `public.key`) → **`gpg --import public.key`** → the import output **displays the email address** bound to the key. Q (*full email address used by the attacker*) solved.

### Stage D — audit history & crypto
- New scenario turn: *the criminal knows he's being hunted and has scrubbed things.* Teaching point: **platforms retain revision/audit history** — information included by mistake and later deleted remains recoverable via a "deeper dive" into the GitHub account (edited/removed commits/files).
- Remaining live questions: **the wallet address** and **which mining pool paid him on 23 January 2021** — answered by tracing the Bitcoin/Ethereum artifact through a **block explorer** (transaction IDs → values, tokens, counterparties). The instructor demos the explorer hopping (one explorer rejects the identifier, another resolves it) and the from/to value columns, then **stops deliberately**.

---

## Part 3 — Homework (the real point of the session)

Before answers to the crypto/geolocation questions are revealed next class, students must produce:

1. **Full Twitter OSINT** on the attacker's (newly-renamed, post-attack) account — every tweet read and interpreted; **reverse-image search** every image; **Twitter advanced-search operators** (Days 6–7) where useful.
2. **Geolocate the attacker** from the assembled clues (the cherry-blossom photos etc.).
3. A **written report** + the outstanding answers (wallet address; mining pool of 23 Jan 2021).

Participation reality-check: out of 11 live attendees only 3 volunteer — prompting the recurring pep talk: this complete course is free, labs are free, and real targets never expose this much.

---

## Part 4 — Techniques-to-syllabus mapping

| Lab step | Technique | Where taught |
|---|---|---|
| Image → export path | metadata / exiftool | Days 3–5 (image analysis) |
| Google the username from metadata | username pivot | Day 8 (URL/username lesson), Day 10 (name sweeps) |
| Twitter account analysis | traditional + advanced operators | Days 6–8 |
| Cross-platform identity stitching | social-media OSINT | Days 6–10 |
| GPG key → email extraction | `gpg --import` key metadata | **new today** |
| GitHub edited/deleted content | revision/audit-history diving | **new today** |
| Wallet + mining-pool trace | blockchain explorers | **new today** |
| Cherry-blossom photos → location | image geolocation | Days 3–5 |

## Part 5 — Admin

- **Next class:** lab tasks **5 & 6** solved with answers in comments; then **one more, harder OSINT room**; then remaining Instagram/OSINT odds and ends; then wind-down decisions.
- Repeats the guarantee: future topics stay free and equally detailed.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | ✅ core complete (Twitter, LinkedIn, Facebook) · Instagram still pending |
| 4 | Emails, phone numbers, personal info | ⏭ announced |
| 5 | Website intelligence | |
| 6 | Steganography | |
| — | **Applied labs** | 🔄 Day 11 (Sakura-style room, tasks 1–4 done live; 5–6 next class) |
