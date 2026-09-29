# OSINT Day 3 — Image Intelligence aur Geolocation (Hinglish Explanation)

**Source transcript:** `transcripts/018 - Day-3 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** OSINT Day 2 — search engines, Google Dorking aur translation
**Note:** Ye explanation Hindi original transcript ko context ke saath samajh kar likhi gayi hai; ye literal translation nahi hai. Image analysis/reverse-search examples published lab material ke context mein hain. Kisi private person ki photo/location trace karne ki koshish bina consent/authorization nahi karni chahiye.

---

## 1. Day 3 ka focus

Aaj OSINT ko images ke saath apply kiya jata hai. Trainer six image-intelligence skills ka roadmap batate hain:

1. Reverse image search
2. EXIF/metadata analysis
3. Image geolocation
4. Video geolocation — next session
5. Image se text extraction
6. Shadow se time calculation — next session

Image OSINT mein goal sirf “photo kahan ki hai” nahi. Four intelligence questions repeatedly use hote hain:

```text
WHAT?  WHERE?  WHEN?  WHO?
```

---

## 2. Four intelligence questions

| Question | Image analysis mein meaning |
|---|---|
| WHAT | Scene/object/event kya hai? |
| WHERE | Photo kahan li gayi? |
| WHEN | Kab li gayi? Date/time clues kya hain? |
| WHO | Kaun person/organization/event se related hai? |

Real life mein geolocation hours, days ya weeks le sakti hai. Lab image mein answer available hone ki wajah se quick lag sakta hai; methodology ko real-world certainty samajhna galat hai.

> Image OSINT ka strongest answer single clue se nahi, multiple independent clues ke convergence se banta hai.

---

## 3. EXIF aur metadata

Image file ke saath metadata attached ho sakta hai:

- camera/mobile model
- image dimensions/resolution
- creation/modification timestamps
- software used
- GPS coordinates, agar location enabled thi
- kabhi upload path/username jaisi accidental information

Apni authorized test image par metadata inspect karne ke liye:

```bash
exiftool image.jpg
```

GUI mein file properties ya EXIF viewer bhi use ho sakta hai.

### 3.1 Metadata reliable truth nahi

Metadata deliberately edit/fake ki ja sakti hai. Attacker/target date ko believable way se shift kar sakta hai, ya GPS ko old location set kar sakta hai. Agar aap sirf metadata par report base karoge to wrong conclusion aa sakta hai.

Rules:

1. Har metadata fact ka source/time note karo.
2. Multiple independent clues se cross-check karo.
3. Image content, reverse search, maps, news aur surrounding context compare karo.
4. Contradiction ko hide mat karo; report mein uncertainty likho.

### 3.2 Social-media metadata stripping

Facebook, Instagram, WhatsApp, Twitter jaise platforms uploaded images ko resize/re-encode karke metadata strip kar sakte hain. Isliye:

- original camera file aur downloaded social copy alag ho sakti hain,
- social copy mein GPS na milne ka matlab original mein GPS nahi tha, ye conclude nahi kar sakte,
- direct/original file aur website-hosted file mein metadata survive ho sakta hai.

Apni photo par test karo: original metadata compare karo, social platform se downloaded copy ka metadata compare karo.

---

## 4. Geolocation methodology

Trainer structured approach batate hain:

### Step 1 — Context

Reverse image search aur metadata se general information collect karo. Jo bhi fact milta hai note karo:

- source URL
- date/time
- image version
- exact claim
- uncertainty

### Step 2 — Foreground

Photo ke front area mein dekho:

- road/sidewalk
- lane markings
- traffic signs
- flags
- language/text
- vehicles/plates
- animals/clothing
- public transport

### Step 3 — Background

Background often strongest location clue de sakta hai:

- architecture
- building shape
- mountains/hills
- rivers/lakes/sea
- parks/vegetation
- tower/bridge/monument
- skyline
- weather/terrain

### Step 4 — Map marking

Exact answer assume mat karo. Candidate region map par mark karo:

- hill/river relation
- building orientation
- road pattern
- distance between landmarks
- likely camera direction

### Step 5 — Trial, error aur verification

Search queries, reverse engines, translations, maps aur archives iterate karo. Candidate milne par independent confirmation required hai.

> “Trial and error” random guessing nahi; hypothesis bana kar observable clues se test karna hai.

---

## 5. Worked exercise: Somalia–Turkey handshake photo

Transcript mein April 2017 ke Somalia president ke Turkey visit ki handshake photograph ka exact location identify karne ka exercise hai.

### 5.1 Starting facts

- Time: April 2017
- Person: Somalia ke president
- Country: Turkey
- Event: first international visit
- Meeting: Turkey ke president ke saath

### 5.2 Tool se pehle visual analysis

Photo ko pehle carefully observe karo:

- Do leaders handshake kar rahe hain.
- Photographer unke saamne press position mein hai.
- Background mein large door/building.
- Flags arranged hain.
- Logo/star jaise visual clues.
- Formal/high-security setup; normal public place jaisa nahi.

Ye clues bina tool ke `WHAT/WHERE/WHEN/WHO` hypotheses create karte hain.

### 5.3 Reverse image search

Authorized lab image ko download/upload karke Google Images/Lens se search kiya ja sakta hai. Same event ki copies aur articles mil sakte hain.

Search results Turkish language mein zyada useful ho sakte hain. Day 2 ka translation workflow apply karo:

- Turkish result page open
- Browser translate
- Names/date/location terms note
- Original source preserve

### 5.4 Multiple angles collect karo

Ek photo se answer assume mat karo. Same event ki other photographs find karke compare karo:

- three large pillars
- building entrance geometry
- gardens/paths
- wider architecture
- event date `26 April 2017`
- “Presidential Palace” type location wording

### 5.5 Google Maps/Earth confirmation

Candidate place ko Google Maps par search karo. Ground photograph aur satellite/3D view mein distinctive features match karo:

- three pillars
- gardens
- entrance alignment
- surrounding building shape

Google Earth desktop historical imagery se different years compare kar sakte ho, lekin imagery availability location par depend karti hai.

Conclusion ko report mein evidence ke saath likho:

```text
Candidate: Presidential Palace, Ankara, Turkey
Evidence: event/date + translated reports + three pillars/gardens + map match
Limitation: Street View/360 coverage unavailable
```

No Street View bhi useful negative result hai: ek verification path available nahi tha, isliye alternative sources use karne pade.

---

## 6. Mapping platforms

Ek hi mapping service par depend mat karo:

| Platform | Useful capability |
|---|---|
| Google Maps/Earth | Maps, satellite, 3D, historical imagery in Earth |
| Apple Maps | Kuch locations par 3D/clarity |
| Mapillary | Crowdsourced street-level images; contributor/time metadata |
| Yandex Maps | Kuch regions mein useful coverage |
| OpenStreetMap | Community-mapped roads/places |
| Region-specific services | Local coverage, access/availability vary |

Mapillary crowd-uploaded images ke source/time information se context mil sakta hai, lekin user-generated data ko independently verify karo.

---

## 7. Reverse image search engines

### 7.1 Google Images/Lens

General-purpose reverse search, text/object/visual similarity ke liye useful.

### 7.2 Yandex Images

Trainer Yandex ko places/scenes/faces/text ke liye strong alternative batate hain. Capabilities:

- landmark/scene similarity
- image crop search
- object detection
- text extraction/translation hints
- flags/language clues

Result ko proof nahi, lead samjho.

### 7.3 Bing Images

Third opinion ke roop mein use kar sakte ho. Different index/algorithm se different results mil sakte hain.

### 7.4 TinEye

Image ke other appearances/earlier occurrences identify karne ke liye useful. Exact match coverage search engine index par depend karti hai.

### 7.5 Crop-based search

Full photo noisy ho to relevant region crop karo:

- sign
- building
- flag
- face only with ethical/authorized purpose
- logo/object

Har crop ka result context ke saath compare karo; face search ko doxxing/stalking ke liye use mat karo.

---

## 8. Browser plugins/tools

Trainer tools mention karte hain:

| Tool | Use |
|---|---|
| Google Translate | Foreign result pages translate |
| Fake News Debunker/InVID-WeVerify | Multiple reverse searches, magnifier/forensic helpers |
| EXIF Viewer Pro | Browser page image ka EXIF inspect |

Fake News Debunker type tools download-upload cycle reduce kar sakte hain aur reverse engines combine kar sakte hain. Tool output ko verify karna phir bhi necessary hai.

Social media images se metadata absent milna normal ho sakta hai; original-file assumption mat banao.

---

## 9. Dorking + translation combo

Day 2 ke dorking aur Day 3 ke image workflow ko combine karo:

```text
1. Target region/country identify
2. Local language identify
3. Search terms translate
4. Dork operators apply
5. Date filter apply
6. Results translate back
7. Sources cross-check
```

Example safe/public lab query:

```text
site:youtube.com "local-language event term"
```

Google UI mein date filter use karo:

```text
Tools -> Any time -> Custom range
```

English-only search se non-English web ka large part miss ho sakta hai. Local-language result often:

- original news source,
- official statement,
- local event name,
- exact place spelling,
- regional archive
provide kar sakta hai.

Translation errors bhi possible hain, isliye original-language text preserve karo.

---

## 10. Day 3 practical/report workflow

Image OSINT report template:

1. **Question:** photo kahan/kab/kis event ki hai?
2. **Input:** original URL/file hash/available metadata.
3. **Visual observations:** foreground/background/context.
4. **Searches:** engines, query language, operators.
5. **Candidate:** first hypothesis.
6. **Verification:** maps, second source, archive, date.
7. **Negative results:** Street View unavailable, metadata absent, etc.
8. **Confidence:** high/medium/low with reasons.
9. **Ethics:** lab/public-source scope, no intrusive action.

Trainer course task ko report form mein submit karne aur published answer directly copy na karne ko kehte hain. Methodology answer se more important hai.

---

## 11. Common mistakes aur safety points

1. Single EXIF field ko final truth maan lena.
2. Metadata faked/old ho sakta hai, ye ignore karna.
3. Social-media re-encoding ko original metadata samajhna.
4. Foreground/background systematically inspect na karna.
5. First reverse-search result ko verify kiye bina accept karna.
6. Non-English sources ko ignore karna.
7. Map match mein one feature dekhkar overconfidence.
8. No Street View ko investigation failure samajhna; alternative maps/archives try karo.
9. Face/image search ko unauthorized person tracking ke liye use karna.
10. Public image ko private-person address/location reveal ke liye exploit karna.
11. Source URL, date aur screenshot/evidence note na karna.
12. Tool result ko conclusion aur hypothesis ko fact samajhna.
13. Published exercise ka answer copy karke methodology skip karna.

---

## 12. Self-check questions

1. Image OSINT ke six skills kaunse hain?
2. `WHAT/WHERE/WHEN/WHO` questions ko photo analysis mein apply karo.
3. EXIF se kaunsi information mil sakti hai?
4. Metadata fake hone par investigation kaise mislead ho sakti hai?
5. Social platforms metadata kyu strip kar sakte hain?
6. Five-step geolocation methodology likho.
7. Foreground aur background clues ke examples do.
8. Reverse search ke baad independent verification kyu zaruri hai?
9. Somalia–Turkey exercise mein three pillars ka role kya tha?
10. Google Earth historical imagery kis situation mein useful hai?
11. Mapillary ka data Google Street View se kaise different hai?
12. Yandex/Bing/TinEye ko Google ke saath kyu try karna chahiye?
13. Dorking + translation workflow ke seven steps likho.
14. Aap image-OSINT report mein negative result kyu document karoge?
15. Lab/public image research aur private-person tracking ke beech ethical boundary kya hai?

---

## 13. Final takeaway

- Image OSINT structured observation se start hota hai, reverse-search button se nahi.
- Metadata useful clue hai, guaranteed truth nahi.
- Context, foreground, background, maps aur multiple sources combine karo.
- Local language search reach ko dramatically improve kar sakta hai.
- Google, Yandex, Bing, TinEye aur mapping platforms complementary results de sakte hain.
- Every candidate location ko independent visual/map evidence se verify karo.
- Report mein source, method, limitation aur confidence document karo.
- Next session video geolocation aur shadow-based time calculation continue karega.
