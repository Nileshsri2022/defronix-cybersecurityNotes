# Explanation — OSINT Day 5: Full IMINT/GEOINT CTF Room Solved Live

**Lecture:** 020 — Day 5, OSINT Free Live Training Capsule Course
**Translation:** [`english/020 - Day-5 OSINT Free Live Training Capsule Course.md`](../english/020%20-%20Day-5%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Days 3–4 (image analysis techniques, reverse search, geolocation)

---

## Part 1 — What this session is

The **final image-OSINT class**: no theory at all. The instructor joins an **IMINT/GEOINT CTF room** on a security-training platform (a "Searchlight IMINT"-style room: *"you will be exploring the disciplines of imagery intelligence and geospatial intelligence… suited for those just beginning"*) and solves it end-to-end on stream, task by task, applying the Day-3/Day-4 techniques.

**Why a CTF room?** It gives structured practice with checkable flags — *"this will help you use your own methodology and see whether you can find things out yourself."*

---

## Part 2 — The student deliverable: a detailed report

The real homework isn't the flags — it's **documentation**:

1. Re-do the lab and perform your own analysis **on every image**;
2. Write a **detailed report** per task: what you observed, what information you collected, how you reached the answer;
3. Upload it to **Google Drive** and post the link in the **LinkedIn page's comment section**;
4. The **best report** gets publicly recognised.

> This mirrors real OSINT work, where the *report* — evidence, method, justification — is the product, not the answer. Note the room itself nudges the same way: *"not just the answer — justify it."*

---

## Part 3 — Task-by-task methodology

### Task: "Welcome to Kanab" sign → the U.S. state
- Apply the standard checklist (context, background, foreground, signage).
- The sign literally names the town (**Kanab**) → one search gives the state (**Utah**).
- Even so, a reverse image search is run **to confirm** — cheap verification is never skipped.

### Task: the London tube station
Clue stacking from one small photo:
| Clue | Value |
|---|---|
| Partially hidden sign "…CIRCUS … STATION" | A "circus" station — Piccadilly/Oxford family |
| **GAP** store, **Hyundai** logo, **Coca-Cola** sign | Matches the famous Piccadilly Circus corner |
| Street-view comparison at an angle | Confirms **Piccadilly Circus, London** |

Lesson: the photo wasn't taken *at* the landmark — matching required inferring the **camera angle** relative to the stores.

### Task: the airport building → country/city
Reverse search identifies **Vancouver International Airport** (→ Canada / Richmond–Vancouver). Instructor stresses: *"I don't know any of this in advance — I am doing it right in front of you."*

### Task: the coffee shop → email, owner's surname, phone
- Storefront lettering ("Edinburgh Woollen Mill" visible nearby) + reverse search → the shop's **Facebook page**.
- Business social pages leak: **email address, owner's name, mobile number**.
- Cross-check on **Google Maps listing** — *"if you have doubt about anything, you MUST verify."*
- This is business-OSINT: social pages + map listings = a full contact dossier from one photo.

### Task: the restaurant
Reverse search + articles (a *"legendary 129-year-old"* 24-hour deli) → name and nickname confirmed via Wikipedia/news.

### Task: the statue → **Lady Justice**, Albert V. Bryan U.S. Courthouse
The hardest one — several dead ends shown honestly (Google Lens failing, similar-image searches misfiring). Breakthroughs:
1. Scene inference: statue is **outside**, facing **three buildings** → a civic complex;
2. A matching article: *"Justice holds the scales… above the front entrance of the Albert V. Bryan [Courthouse]"* → **Alexandria, Virginia**;
3. **Google Maps** used in reverse — going to the location to confirm the building and finish the identification (**Lady Justice**, blindfold detail checked).

> Lesson: when reverse search stalls, switch engines, then switch *modes* (text search, maps, articles).

### Task: geolocating a **video** → Novotel, Clarke Quay, Singapore
The explicit method taught:

1. **Watch the full video first.**
2. Determine the **pan direction** (left→right or right→left).
3. **Screenshot** each informative frame; lay screenshots side by side to reconstruct the panorama.
4. Extract anchors: high **balcony** vantage, a **riverside** promenade, the sign **"CENTRAL"**, **three towers with a park on top**.
5. "Central" + river → **Singapore** → Google Maps **360° views** → line up the camera angle → the only building opposite with that view = **the Novotel hotel**.

This is the video-geolocation workflow promised back on Day 3, executed for real.

### Final task: the motorcycle photo → a Twitter handle
Reverse search → Facebook post (chrome master cylinder, **December 2012, Washington D.C.**) → pivot from photo to **poster's Twitter handle**. Shows the *photo → person → social account* chain.

---

## Part 4 — Habits reinforced throughout

1. **Reverse search first, questions later** — establish what the internet already knows about the image before analysing pixel details.
2. **Verification is mandatory** — every answer is double-checked in a second source (Maps listing, Wikipedia, street view).
3. **Dead ends are normal** — the instructor deliberately leaves his failed attempts in ("it works and it doesn't") to show real methodology.
4. **Don't over-spend on easy tasks** — time is budgeted; techniques were taught in Days 3–4, this class is about tempo.
5. **Video = many images** — reduce a video to screenshots and treat it with the same image toolkit.

---

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 (labs complete) |
| 3 | Emails, phone numbers, personal info | |
| 4 | Social media OSINT (Twitter/Instagram) | ⏭ next |
| 5 | Website intelligence | |
| 6 | Steganography | |
