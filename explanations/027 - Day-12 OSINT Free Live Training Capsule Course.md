# Explanation — OSINT Day 12: Lab Tasks 5 & 6 (Deep Paste, BSSID, Geolocation)

**Lecture:** 027 — Day 12, OSINT Free Live Training Capsule Course
**Translation:** [`english/027 - Day-12 OSINT Free Live Training Capsule Course.md`](../english/027%20-%20Day-12%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** Day 11 (lab stages A–D) · **Continues to:** Day 13 — Instagram OSINT

---

## Part 1 — Context

Day 12 continues the same realistic OSINT room. The attacker, now aware of the hunt, taunts on Twitter (*"you would not catch me — I am already heading back home"*) — which itself becomes the lab's pivot into **movement tracking**. Questions worked live: current Twitter handle → password-cache location → home BSSID → home city → layover airport → final airport.

---

## Part 2 — Where the passwords live: the DeepPaste lead

- Tweet analysis: *"not too concerned about someone finding them on the dark web — …do a real deep search to find where I posted them."* The phrase "deep" + dark web → a **dark-web paste site (DeepPaste, .onion)** whose entries are indexed by **md5 hashes**; searching the hash returns the paste contents.
- Live-site reality: the .onion search **was down** during class — the instructor demonstrates resilience: the paste's content ("Regular Wi-Fi and passwords: computer-lab SSID/password, school Wi-Fi, society password…") was recovered **via clear-web mirrors/search**, no magic tools. **Home Wi-Fi SSID + password captured** (`dk1f-g`).
- Method note: dead links are normal in OSINT — pivot to caches, mirrors, and secondary sources instead of abandoning the thread.

---

## Part 3 — BSSID hunting with Wigle (`wigle.net`)

Concepts taught:

- **BSSID = the access point's MAC address** — distinct from the human-readable SSID; needed for precise AP geolocation.
- **Wigle** is the global wardriving database: **register → log in → search by SSID or BSSID.**
- Demo on `dk1f-g`: several query variants (case-sensitivity, the site's "commercial page" gating, a flaky download button) before results landed: **latitude/longitude, channel 11, neighbouring SSIDs, and a street address (a "society")**.
- The address (Japanese, translated) → **Google Maps paste → satellite view** confirms the neighbourhood. The home-city question resolves to **Hiroshima, Japan** — submitted answer marked **correct**.

---

## Part 4 — Geolocating the airports (reverse image + map terrain matching)

### Layover airport
- Artifact: the route-home tweet's photo — a roadway, a house, a **tower**, and a **lake**.
- **Google Lens** visible matches → *"University Park Campus… construction"* style hits; translation → **Washington (D.C.)** hypothesis; map walk near the **university ↔ water body ↔ park** geometry matches the photo's composition; right across sits **Ronald Reagan Washington National Airport (DCA)** — submitted, **correct**.
- Transferable drill: Lens for candidate identification → satellite/Street-View terrain triangulation to *verify* (never submit on a Lens match alone — "confirm a little more").

### Final airport — the Sakura Lounge (left open)
- Second tweet image → reverse search → **"Entrance to the JAL Sakura / First Class lounge" (Japan Airlines)** — meaning the final leg was a JAL departure; identifying **which airport hosts that lounge view** was left as the single open item (the helper site was down), to be closed later.

---

## Part 5 — Patterns worth keeping

| Move | Why it matters |
|---|---|
| Read adversary tweets **forensically** | The taunt ("heading home") doubles as a directional lead |
| Dark-web paste ↔ md5 search | How leaked caches are indexed; also: **sites die — mirror-search** |
| SSID → BSSID → lat/long (Wigle) | Wireless APs are **physical-location oracles** leaking the home address |
| Lens → cross-check in Maps | Reverse-image hits are hypotheses; terrain matching verifies |
| Lounge/airline clues | Even a lounge-entrance photo narrows carrier + airport |

## Part 6 — Community & admin

- **Report competition:** detailed, screenshot-rich write-ups (this room, the earlier "Searchlight" image-OSINT room, all assigned tasks) via Google Drive; the best author gets a personal shout-out and **publication on the academy's page** (credits to Prince, Lalit/Lakshan et al. already submitting).
- Encouragement for recording-watchers to send reports too.
- **Instagram OSINT** flagged as next; closing pep talk: OSINT pays off in everyday searching even outside hacking.

## Syllabus progress

| # | Topic | Status |
|---|---|---|
| 1 | Advanced search engines / Google Dorking | ✅ Day 2 |
| 2 | Image analysis & geolocation | ✅ Days 3–5 |
| 3 | Social media OSINT | ✅ core complete · **Instagram next (Day 13)** |
| 4 | Emails, phone numbers, personal info | ⏭ announced |
| 5 | Website intelligence | |
| 6 | Steganography | |
| — | Applied labs | 🔄 Sakura-style room: tasks 1–6 nearly closed (1 answer pending) · more labs teased |
