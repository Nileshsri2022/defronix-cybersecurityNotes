# Explanation — OSINT Day 3: Image Intelligence & Geolocation

**Lecture:** 018 — Day 3, OSINT Free Live Training Capsule Course
**Translation:** [`english/018 - Day-3 OSINT Free Live Training Capsule Course.md`](../english/018%20-%20Day-3%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 2 (Google Dorking) — which gets combined with translation here

---

## Part 1 — What image OSINT covers

Two days are allocated to images. The six skills:

| # | Skill | Covered today |
|---|---|---|
| 1 | Reverse image search | ✅ |
| 2 | EXIF data and metadata | ✅ |
| 3 | Geolocating an **image** | ✅ |
| 4 | Geolocating a **video** | next session |
| 5 | Extracting **text** from an image | ✅ (via Yandex) |
| 6 | **Calculating time from a SHADOW** | next session |

> Skill 6 is flagged as *"the most important, quite an interesting fact, quite time-consuming, and quite challenging for me too."*

---

## Part 2 — The four intelligence questions

Every intelligence discipline — police, agency, corporate — reduces to four questions:

| Question | Establishing |
|---|---|
| **WHAT** | What is happening in this photo? |
| **WHERE** | Where was it taken? |
| **WHEN** | When was it taken? |
| **WHO** | Who took it / who is responsible? |

### ⚠ Realistic expectations

> *"These are LABS, so it will be found here. **But in real life it can take two days, three days, one week, 10 days**, because you will have to search the whole internet."*

This is worth internalising before starting: **geolocation is slow, iterative work**, not a single clever query.

---

## Part 3 — EXIF and metadata

### What you might find

- Which **camera or mobile** took it
- **Pixel** dimensions / resolution
- Sometimes an **upload directory path** — which can **expose a username**
- **GPS coordinates**, if location was enabled

### 3.1 ⚠ Metadata can be deliberately faked

The most important caution in the session:

> Your target **may be smarter than you assume** — *"it's possible the person you are investigating is themselves in intelligence, or a cyber expert, or simply smart."*

**Why crude fakes fail but subtle ones work:**

| Tampering | Result |
|---|---|
| **Change everything** | *"You would understand — this doesn't even match my investigation"* |
| **Shift the date back 4 years** | **You follow it.** It looks plausible and leads you to a dead trail |

### The failure scenario spelled out

```
Metadata gives you coordinates + a name
        ↓
You research it, find corroboration
        ↓
You submit the report
        ↓
It was a location from FOUR YEARS AGO
        ↓
And you never noted the OTHER coordinates and leads
   found elsewhere in the investigation
```

### 3.2 The two rules

> **1. Take notes on everything.** *"You will not remember which page gave you which information."* Record **which source** each fact came from.
>
> **2. Never depend on a SINGLE SOURCE.** Collect from **multiple sources** and **cross-check.**

> *"If you cross-check, it will never happen that every platform gives different data — you will collect the same data."* Divergence is itself a signal.

### 3.3 ⚠ Social media strips metadata

> **Facebook, Twitter, Instagram, WhatsApp all DELETE metadata by default** — for **data protection** reasons.

**Test it yourself:** right-click a photo from your own phone → Properties → *"you will find it full of data."* Upload it, download it back → the metadata is gone.

**Where you still get lucky:**

- A website that **doesn't** strip it
- Someone **shared the original file directly** rather than through a platform

---

## Part 4 — ⭐ The geolocation methodology

> **"When you don't have a methodology and don't have an APPROACH, you will do these things BLINDLY and your time will be WASTED."**

### The five steps

| Step | Name | What you do |
|---|---|---|
| **1** | **CONTEXT** | Reverse image search + metadata. Gather any general information and **note it** |
| **2** | **FOREGROUND** | What is in front: street, lane, road markings, signs, traffic symbols, flags, animals |
| **3** | **BACKGROUND** | **"The easiest give-away — MOST of the geolocation comes from here."** Building sizes, mountains, parks, lakes, distinctive features |
| **4** | **MAP MARKING** | Not exact, but form an idea: hills present? A river? How big? Narrow the candidate region |
| **5** | **TRIAL AND ERROR** | **"Fifth and foremost."** Keep trying until the information is confirmed |

### The optimistic premise behind step 5

> **"Somewhere or other you WILL get that information; somewhere or other it will have been publicly exposed. It simply cannot be that it was never exposed anywhere."**

---

## Part 5 — ⭐ The worked exercise

A complete geolocation, start to finish. **Worth studying as a template.**

### The brief

> *In April 2017 the President of Somalia made his first international visit to Turkey.* **Find the exact location of the handshake photograph.**

### Starting information

| Given | Value |
|---|---|
| Date | April 2017 |
| Person | President of Somalia |
| Country | Turkey |
| Event | First international visit |
| Met with | President of Turkey |

### Step 1 — Read the photograph itself

| Observation | Inference |
|---|---|
| Two men shaking hands, facing camera | **Photographer is directly in front** — a press position |
| Large **door** behind | Entrance to a significant building |
| Large **building** | *"Some special building — not a normal building, not a hotel"* |
| Both are **heads of state** | *"Quite confidential, under HIGH SECURITY"* |
| Extremely clean; **both flags arranged** | *"Not a public place — if it were public they'd be walking around"* |
| A **logo** and a **star** | Identifying marks |

> This stage requires no tools at all — **just structured looking.**

### Step 2 — Reverse image search

Download → **Google Images → camera icon → upload.** Returns the same flag, building and people across several sites.

### Step 3 — ⭐ Translate

The useful results are in **Turkish**, not English.

> **"Many times the result you need will NOT be in English."**

**Install the Google Translate Chrome extension.** Right-click → Translate this page.

### Step 4 — Collect more angles

Each new photo of the same event adds detail:

| New detail | Value |
|---|---|
| **Three large PILLARS** | Strong architectural identifier |
| Wider view | *"Really quite a big building"* |
| Clearer angle | Additional objects in the scene |
| **Date: 26 April 2017** | Precise |
| **Name: "Presidential Palace"** | ⭐ The breakthrough |

> **The principle: one photo rarely solves it; the SET of photos does.**

### Step 5 — Confirm on Google Maps

Search the place name. *"Is the location the same or not? It's confirmed."*

### Step 6 — Google Earth historical imagery

> **Download the DESKTOP version.**

Use **Historical Imagery** to step back through 2023 → 2022 → 2021, hunting for a clearer angle matching the photograph.

> *"Look — the part sticking out. So it could be from slightly outside this building."*

### The answer

| Item | Result |
|---|---|
| **Place** | Presidential Palace |
| **City** | **Ankara, Turkey** |
| **Coordinates** | Confirmed via the **three pillars** and **gardens** visible in both the photo and the satellite view |

> The confirmation is the key move: **matching a distinctive feature (three pillars) between the ground photo and the overhead view.**

### Negative result recorded

No Street View exists at the location — *"no 360 camera is anywhere around it that would expose it."*

> **Recording what ISN'T available is part of the methodology** — it tells you which avenues are closed.

---

## Part 6 — Mapping platforms

Never rely on one map.

| Platform | Strength |
|---|---|
| **Google Maps / Earth** | Default. Earth desktop has **historical imagery** |
| **Apple Maps** | *"Quite good in 3D; sometimes MORE clarity than Google"* — needs Apple devices |
| **Mapillary** | **Facebook-owned**, crowdsourced. *"Street Views not available on Google Maps"* |
| **Yandex Maps** | *"Quite good data sometimes"* |
| **OpenStreetMap** | Community-mapped |
| Chinese services | High quality for China; access restricted |

### Mapillary's distinctive feature

Because it is **crowdsourced from uploaded photos**, you can see **who took which photo and when** — useful both for coverage where Google hasn't driven, and as a data source in itself.

---

## Part 7 — Reverse image search engines

### ⭐ Yandex Images often beats Google

> **"Yandex Images provides quite good results — BETTER results."**

Observed capabilities:

| Capability | Detail |
|---|---|
| **More clarity** | *"We didn't have this much information; that image wasn't of this much clarity"* |
| **Auto-detects language** and translates | |
| **Object identification** | Identifies foreground/background objects and returns matches |
| **Text extraction** | *"Detects text in the image, tries to guess it, and shows it on the right side"* — solves skill #5 |
| **Flag identification** | *"On the basis of the flag alone you can find out"* |
| **Crop tool** | Narrow to one region and search again |

> **Why it matters:** Yandex is consistently stronger at **landmark and scene matching**, particularly outside the English-speaking web.

### The engines to try

| Engine | Use |
|---|---|
| **Google Images / Lens** | General, strong on products and text |
| **Yandex** | **Strongest on places, faces, scenes** |
| **Bing** | Third opinion |
| **TinEye** | Finds **where else** an image appears, and oldest occurrence |

---

## Part 8 — Browser plugins

| Plugin | Purpose |
|---|---|
| **Google Translate** | Translate foreign-language result pages |
| **Fake News Debunker** (InVID-WeVerify) | **One right-click → reverse search across Google, Google Lens, Yandex, Bing, Reddit, or all**; plus Image Magnifier and Image Forensic |
| **EXIF Viewer Pro** | Right-click → **Show EXIF** on any image on a page |

> **Why Fake News Debunker matters:** *"You will not need to DOWNLOAD the image."* Removes the download-and-upload cycle entirely.

**Observed limitation:** *"From Instagram you will get NOTHING"* — confirming the metadata-stripping point.

---

## Part 9 — ⭐ Dorking + Translation

The strongest practical idea in the session, combining Day 2 with Day 3.

```
site:youtube.com [keyword in the LOCAL language]
+ Tools → Any time → Custom range
```

### Why this multiplies your reach

> **"Many times you will find results that are few in English — but the result related to that LANGUAGE will be rich."**
>
> **"Many times the LOCAL LANGUAGE gives you more and more EXACT things than English."**

### The workflow

```
1. Identify the local language of the target region
2. Translate your search terms into it
3. Apply Google Dork operators
4. Apply date filters (Tools → Custom range)
5. Translate the results back
```

> **"If you learned the COMBO of Google Dorking plus Google Translator — I'm telling you, you will really enjoy it. You can make any searching [strategy]."**

**The underlying insight:** the English-language web is a *fraction* of the indexed web. Searching only in English discards most of what exists about a non-English-speaking target.

---

## Part 10 — Complete cheat sheet

```
# ---- the four questions ----
WHAT is happening?  WHERE?  WHEN?  WHO?

# ---- geolocation methodology ----
1. CONTEXT      reverse search + metadata, take notes
2. FOREGROUND   streets, signs, markings, flags, objects
3. BACKGROUND   buildings, mountains, parks, lakes  <- biggest give-away
4. MAP MARKING  narrow the candidate region
5. TRIAL & ERROR  iterate until confirmed

# ---- reverse image search ----
Google Images  -> camera icon -> upload
Yandex Images  -> often BETTER for places/scenes/text
Bing Images
TinEye         -> where else it appears, oldest occurrence

# ---- metadata ----
Right click -> Properties
EXIF Viewer Pro plugin -> right click -> Show EXIF
# WARNING: social media STRIPS metadata
# WARNING: metadata CAN BE FAKED — cross-check everything

# ---- maps ----
Google Maps / Google Earth (desktop -> HISTORICAL IMAGERY)
Apple Maps      3D clarity
Mapillary       Facebook, crowdsourced street view
Yandex Maps
OpenStreetMap

# ---- plugins ----
Google Translate
Fake News Debunker   right click -> reverse search all engines
EXIF Viewer Pro      right click -> Show EXIF

# ---- dorking + translation combo ----
site:youtube.com [term in LOCAL language]
Tools -> Any time -> Custom range
```

---

## Part 11 — Self-check questions

1. Name the six image-OSINT skills. Which two are deferred?
2. State the four intelligence questions.
3. How long can a real geolocation take, versus a lab exercise?
4. What can EXIF data reveal? Name four items.
5. Why is a *subtle* metadata fake more dangerous than a wholesale one?
6. State the two rules for handling metadata.
7. Which platforms strip metadata, and why? How can you test this yourself?
8. List the five geolocation steps in order. Which yields the most?
9. What premise justifies "trial and error" as a formal step?
10. In the worked exercise, what could be inferred *before* using any tool?
11. What was the breakthrough that produced the place name?
12. How were the coordinates finally confirmed?
13. Why is recording "no Street View here" part of the method?
14. Name five mapping platforms and one strength of each.
15. What makes Mapillary's data different in kind from Google's?
16. Give four capabilities where Yandex Images outperforms Google.
17. Which Yandex feature solves the "extract text from an image" problem?
18. Name the three plugins and what each does. What does Fake News Debunker save you?
19. Why does combining dorking with translation multiply your results?
20. Write the five-step dork-plus-translate workflow.

---

## Part 12 — Course logistics

### Today's task

**Exercise 7** from the practice site. Produce a **report**: steps performed, tools used, what you analysed, how you found it.

> ⚠ **"PLEASE DON'T USE THE ANSWER"** — the site publishes write-ups; *"if you want to practise, don't go through the write-up."*

**Submission:** OneNote or similar → **Google Drive link** → posted on the **LinkedIn page**.

### What's being tracked

1. **Attendance** across all 10 days
2. **Comments** on the LinkedIn page
3. **Task reports** submitted

One student is selected and contacted via LinkedIn — **the T-shirt winner.**

### The attendance conditions

> *"I need a minimum of **30 students** live. Today there are 27. **If even one is less tomorrow**, then [daily sessions won't continue]."*
>
> *"And I need **30 LIKES before the session starts.**"*

### Ethics reminder

> **"This is JUST FOR EDUCATIONAL PURPOSES ONLY, not to cause harm to anybody."** The exercises are deliberately drawn from a **published practice set** rather than live targets — *"otherwise, if we just use anything live, someone could create a problem in an illegal way."*

---

## Part 13 — Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| **2** | **Image analysis & geolocation** | 🔄 **Day 3 — continues next session** |
| 3 | Emails, phone numbers, personal info | |
| 4 | Social media OSINT | |
| 5 | Website intelligence | |
| 6 | Steganography | |

**Next session:** video geolocation and **calculating time from shadows.**
