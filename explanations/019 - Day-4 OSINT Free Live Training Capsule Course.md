# Explanation — OSINT Day 4: Image Geolocation & People-Identification Labs

**Lecture:** 019 — Day 4, OSINT Free Live Training Capsule Course
**Translation:** [`english/019 - Day-4 OSINT Free Live Training Capsule Course.md`](../english/019%20-%20Day-4%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 3 (reverse image search, EXIF/metadata, geolocation methodology)

---

## Part 1 — Session structure

This is a **100% hands-on lab session** — no slides, no theory. Two labs are worked live and one is assigned as homework, all drawn (with credit) from **Sofia Santos's published OSINT exercise set** (gralhix.com):

| # | Lab | Done in class? |
|---|---|---|
| 1 | Telescope in a CIA caption report → find the photo + exact placement location + coordinates | ✅ live |
| 2 | Verify a journalist's "suicide attack in Pakistan" photo (19 Jan 2023) | 📝 homework |
| 3 | Identify four gentlemen in a single event photo (exercise #6) | ✅ live (2 of 4 names; other 2 are homework) |

**Ethics disclaimer repeated:** everything is for educational purposes only; the exercises are deliberately from a published practice set, not live targets.

---

## Part 2 — Lab 1: working *without* the photo

### The twist

The evidence is a **declassified CIA "caption report"** *describing* an undisclosed photo. The photo itself is missing — the core skill practised is **turning a text description into search leads**.

### Step 1 — Extract every fact from the document

| Fact | Value |
|---|---|
| Report origin | Berlin, **Germany** (+ partial coordinates printed on the form) |
| Object | A large **telescope** |
| Built at | A **factory** (Askania, Berlin) — "being assembled at the factory" |
| Built for | **University of Bonn** |
| Scale | "20× bigger than the Mount Palomar telescope camera", ~20 ft, heavy |
| Date | **January 18, 1953** |

### Step 2 — Map facts onto the intelligence questions

WHAT (telescope) ✅ · WHERE (Berlin/Germany) ✅ · WHEN (Jan 1953) ✅ · WHO ❌ → the missing pieces drive the search.

> **Method lesson:** every Google query in the lab is constructed from the WHAT/WHERE/WHEN triple, not guessed.

### Step 3 — Search → candidate article → *verify, don't accept*

A search like `Askania telescope University of Bonn 1953` surfaces a press-archive article whose text matches the caption point-for-point (Askania's Berlin factory, first since the war, Uni Bonn, photographing stars to the 23rd magnitude, ~20 ft camera). It even includes a candidate photo.

**Key discipline taught:** even with a perfect textual match, *"we are not ready to accept it — we are not sure"* → keep corroborating.

### Step 4 — Reason forward to the final location

Logical chain: built **for** Uni Bonn → must have been **installed** somewhere for research → famous object ⇒ someone photographed it. Follow-up searches (using **double quotes** and year restriction — Day-2 dorking applied) lead to the **University of Bonn observatory** (Hoher List) with:

- a **clear archive photo** matching the caption (workers assembling it),
- a **tower** ("Tower 1", 1953/54) where the telescope was mounted,
- **latitude/longitude published on the observatory's own website** → answers the "provide coordinates" requirement.

### Step 5 — Confirm the tower with Google Maps user photos

Paste the coordinates into Google Maps → browse **user-contributed photos** → match environmental details between the archive photo and today:

- the **big tree** (and its shadow),
- the **path/strip** in front,
- the **benches** next to the building,
- **markings on the tower** visible in day and night photos.

Conclusion: *Tower 1* — probable but **not yet certain** → final confirmation delegated to students via **YouTube footage** of the observatory interior.

> **Takeaway:** geolocation verification = stacking small environmental matches (tree, path, bench, marking), never a single "aha".

---

## Part 3 — Lab 3: identifying four unknown men (exercise #6)

### Step 1 — Squeeze the photo before searching

Before any reverse search, the instructor inventories visual clues:

| Clue | Inference |
|---|---|
| **Headphones** on the table | Translation equipment → **multilingual, multi-country meeting** |
| Long table, banner backdrop | Formal event — a **signing / deal** |
| Fancy water bottles | High-level, expensive venue |
| Pen in hand | The man is **right-handed**; a signing is in progress |
| Banner too blurred | Explicitly **not** over-interpreted — "don't zoom blurred text, you'll invent words" |
| Media-style framing | The event certainly had **press coverage** → photos exist online |

### Step 2 — Reverse search → event identified

Reverse image search leads to **UN Security Council / UNSMIL material, 17 December 2015** → the **Libyan Political Agreement signing (Skhirat)**. Now the problem changes from "who are these men?" to "who attended this documented event?" — a much easier problem.

### Step 3 — Face matching, honestly

The instructor models careful matching: glasses style, hairstyle, hair parting, a mark above the glasses, beard, suit colour/lining — and openly rejects non-matches ("No — he has glasses but not like his"). Two of the four are visually pinned to clear event photos.

### Step 4 — Two clever pivots for the *names*

1. **Cross-language Wikipedia + auto-translate:** the same photo appears on an **Arabic Wikipedia page**; *right-click → Translate this page* yields the name **Mustafa Abushagur** (former Libyan deputy PM). Lesson: **don't search only in English** — the richest sources on a person are often in their own language.
2. **The signature-order trick:** an event photo shows the **signature page**; the target signs **third**. Match the third signature block, translate the Arabic name to English, search it → second name confirmed.

> **Takeaway:** identity OSINT chains *event → attendee lists/coverage → language pivot → document artefacts (signatures)*. Names two found live; the remaining two are homework (answer via LinkedIn page comments; **don't peek at the published solution**).

---

## Part 4 — Homework task: photo verification (exercise on the Pakistan claim)

> A journalist (~140K Twitter followers) posted a smoke/fire photo on **19 Jan 2023** claiming a suicide attack in a Pakistani city killed 3 police officers. **The photo is not of that event.** Students must *prove* the mismatch.

This is a classic **misinformation-debunking** drill: reverse-search the image, find its true origin/date, compare with the claim. (Ties directly to Day 3's "Fake News Debunker" plugin discussion.)

---

## Part 5 — Recurring teaching themes

1. **Do the analysis yourself first.** Twice the instructor scolds shortcuts: students asking for links they can Google, and students praising the speed of finding the article — *"how much analysis could you have done if that article had not been found?"*
2. **Verification over discovery.** Every find (article photo, tower, faces) is treated as a hypothesis until at least one independent source corroborates it.
3. **Real OSINT is slow.** YouTube-footage confirmation is skipped in class *because* it takes time — and that's normal.
4. **Public availability is the boundary.** Q&A answer: a random photo from someone's house is only traceable if data about it is public (e.g. metadata) — "everything is possible **if it is publicly available**."

---

## Part 6 — Admin & what's next

- **Attendance leverage continues:** LinkedIn page comments = proof of presence; tasks answered there (open even to late viewers of the recording).
- **No session tomorrow** — preparation day.
- **Coming up:** the promised **shadow/sun-position lab** (time-from-shadow calculation), 1–2 more image exercises, then **Twitter & Instagram OSINT**.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | 🔄 Day 3–4 — labs; shadow lab pending |
| 3 | Emails, phone numbers, personal info | |
| 4 | Social media OSINT (Twitter/Instagram) | ⏭ announced next |
| 5 | Website intelligence | |
| 6 | Steganography | |
