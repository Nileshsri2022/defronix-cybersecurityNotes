# 018 — Day 3 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/018 - Day-3 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Image OSINT · Reverse image search · EXIF/metadata · Geolocation methodology · Mapping platforms · Browser plugins
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`एग्जिट डाटा`/`एक्जीबिट डाटा`/`एक्सिम डाटा` = "EXIF data", `मटर डाटा`/`मेटल डाटा`/`मतदा` = "metadata", `जिओ लॉकेट` = "geolocate", `कोऑर्डिनेटर`/`कोऑर्डिनेट्स` = "coordinates", `इंडेक्स` (as a search engine) = **Yandex**, `स्टेट व्यू`/`स्टूडियो` = "Street View", `डबल मैप`/`मैप्पी` = **Mapillary**, `प्रोग्राम`/`फोर ग्राउंड` = "foreground", `त्रिकोण`/`टिनआई` = TinEye, `एक न्यूज़`/`फेक न्यूज़ डिबंकर` = "Fake News Debunker", `माइथॉलजी`/`मेट्रोलॉजी`/`पैथोलॉजी` = "methodology", `हनी पहचाने` = "cause harm", `ओसियन` = OSINT, `शैडो` = "shadow", `सोफिया संतोष` = the exercise site author). The intended technical term has been restored where unambiguous.

---

[Music] [Applause] Hello everyone, good evening friends. Confirm once whether my voice is audible to everyone. Please tell me quickly in the chat. Okay, thank you.

So welcome, all of you, to the **Defronix Academy** YouTube channel.

**[Today: Image] Open Source Intelligence** — how we do OSINT on the basis of an image. Meaning: **we get an image, or there is some text in an image, or the image is not clear — on that basis how will we do ANALYSIS?**

How will we do Open Source Intelligence:
- **Who** would have taken this image?
- **Can it be geolocated?**
- **When** would it have been taken?
- **Where** was it from?

So let's move ahead. **We have two days of OSINT on images**, in which we will do some **labs**, and **from today you will get some TASKS.**

---

## Course admin

What you have to do — you have already been told: **whatever you learn in class, what you learned in today's class, what our topic was, what it was related to** — all those things you have to [write up].

**Go to our LinkedIn page** — the link is in the description of our YouTube channel. **That is our Defronix official page**; every day's class on any topic gets updated there. **Go there and comment.**

> **Through that we will come to know how many people are active**, how many people are doing [the work].

### The tasks

**Today you will get two tasks.** What you basically have to do:

1. **Do a full ANALYSIS**
2. **Don't do anything miscellaneous with it** — *"first of all there is nothing to misuse in it, they are labs anyway; but still you must keep in mind: do not try anything illegal with it"*
3. **Make a REPORT:** *"which steps you performed, what tool you used, what you analysed, what you looked at, and how you found it out"*
4. Make it in **OneNote** or anything you like, **put it on a Google Drive link**, and **share the Drive link on our LinkedIn page**

> After the 10 days are complete, we will analyse [everyone] in two or three days, **and the lucky [winner] among you will get a message** and will be announced — **the lucky winner of the T-shirt.**

---

## Part 1 — What you'll learn in image OSINT

| # | Skill |
|---|---|
| 1 | **How to do image reverse search** |
| 2 | **How to find the EXIF data and metadata** of any image |
| 3 | **How to geolocate an image** |
| 4 | **How to geolocate a video** |
| 5 | **How to pull TEXT out of an image** |
| 6 | **How to calculate TIME from a SHADOW** |

**On #5:** *"Many times there are images which contain text — if it's in simple language it's easy, but many times there is text you don't understand. For that there are tools; some search engines extract it automatically."*

**On #6 — the most interesting:**

> *"The most important, and quite an interesting fact, and quite time-consuming — and quite challenging for me too: **HOW TO CALCULATE TIME FROM A SHADOW.** You have an image in which there is a shadow. On the basis of the shadow, how can you find out at what TIME this image would have been taken?"*

---

## Part 2 — The four intelligence questions

> **No matter who you are or where you are in the world, if you have internet and your daily-use device** — laptops, desktops, mobile — **you can extract information sitting at home**, using publicly available information.

**In any intelligence work there are some important questions** — whether it's police intelligence, an intelligence agency, or any intelligence at all:

| Question | What you're establishing |
|---|---|
| **WHAT** | What may be happening in this photo? |
| **WHERE** | Where is it? |
| **WHEN** | When was it taken? |
| **WHO** | Who took it / who is responsible? |

> **"These are small questions whose answers are very DIFFICULT"** — because finding them out on the basis of one image or one video is **"a very tricky task; it is not easy."**

### ⚠ Realistic time expectations

> *"It's not that I will sit in a one-hour class and get it done. These are LABS, [so] it will be found here. **But in real life it can take you two days, three days, one week, 10 days** to extract such information, because you will have to search the whole internet to find the answers to these four questions."*

---

## Part 3 — EXIF and metadata

> **"Looking at the EXIF and metadata of an image can [reveal] HIDDEN INFORMATION that may be left behind by someone"** — which may answer one of your four questions.

### What you might find

- The **mobile/camera** information — **which camera took it**
- **Pixels** / resolution
- Sometimes a **directory path** where the image was uploaded — **which can expose a username**

---

## Part 4 — ⚠ Critical cautions for all OSINT

> **"Make a BRIEF NOTE of each and everything when doing any type of Open Source Intelligence — especially when viewing metadata and EXIF data. It CAN BE EDITED, or has been taken in the past, to [alter] different properties, and may even be [used] to MISLEAD your investigation, which leads you to a wrong location or name, etc. So keep this in mind and make sure you are always [cross-checking] information."**

Let me explain this simply.

### 4.1 Always take notes

> **Whenever you do any type of intelligence, you must ALWAYS keep NOTES.** Whatever information you get, you will have to write it in those notes, **because you will not remember which page gave you which information.**
>
> **So make a brief note of everything**, [recording] which source that information came from.

### 4.2 ⚠ Metadata can be deliberately faked

> **Metadata can be CHANGED.**
>
> It's possible that the person you are investigating **is themselves in intelligence**, is some cyber expert, or is simply smart — *"because foolish people don't do such work; it's the smart one through whom you do intelligence."*
>
> **So it's possible they put in information to MISLEAD you, to lead your investigation [astray]** — information which is not the present one but from the past.

**Why a crude fake wouldn't work:**

> *"If they changed the whole information, you would understand — 'yes, this person has changed the metadata; this doesn't even match my investigation.'"*

**The subtle version is the dangerous one:**

> *"What they will do: you are investigating, you are on a good track, and you get the metadata — but that metadata is **4 years old** and leads you to a 4-year-old [trail]."*

### 4.3 The rule: never trust a single source

> **Never depend on any SINGLE SOURCE. You have to collect information from MULTIPLE SOURCES.** Keep notes of every one, and **at least CROSS-CHECK it.**
>
> **If you cross-check, then it will never happen that every platform gives different data** — you will collect the same data. **If somewhere it differs** [then you investigate].

### The failure this prevents

> You are carrying **4-year-old information** from metadata; on its basis **coordinates were exposed** and a **name was exposed**. You research on that, [thinking] *"I got everything"*, and **you submit the report** —
>
> **and it turns out that was a very old location**, and you never [checked] in your report that **other coordinates were found somewhere, other locations, other [leads]** in the investigation. **So you have to keep all these things in mind.**

### 4.4 ⚠ Social media strips metadata

> **Nowadays, whenever any image is uploaded to WhatsApp or social media, by default all the websites DELETE its metadata.**
>
> Check: your own mobile's image — right click → Properties — **you will find it full [of data].** **But as soon as it goes to social media** — Facebook, Twitter, Instagram, WhatsApp — **its metadata basically changes**, because many websites **CLEAN it**, for **DATA PROTECTION** reasons.
>
> **So there are very few chances that you will get [metadata].**
>
> **But it's possible some website is not doing this**, or someone **by mistake shared the direct [original] somewhere** and you get that [file].

---

## Part 5 — ⭐ The geolocation methodology

> **How to identify location from a photo or video — which we call GEOLOCATION.**

*"There is a common methodology, which I too learned from someone. These may be the methods; there may be more steps than these — you can add [your own]."*

### The five steps

#### Step 1 — CONTEXT

> **"It is very important to look at the CONTEXT of a photo or video"** — for example by doing **image reverse search** and by **looking at the metadata**, trying to find possible information about the image or video.

> **Whatever general information you get** from reverse search or EXIF data — **search it as much as possible, and make NOTES of that information.**

#### Step 2 — FOREGROUND

> **"What you can see in the FRONT of the photo."** Look at what is in the foreground:
>
> - Is there a **street** visible? A **lane**? A **road**?
> - Is there a **marking/stripe** on the road?
> - Is there a **dog** nearby?
> - Is there a **symbol**, a **traffic sign**, a **flag**, or anything at all?
>
> **Note it down; highlight the foreground.**

#### Step 3 — BACKGROUND

> **"It is the easiest give-away; MOST of the geolocation [comes from here]."**
>
> Analyse the background: **how big the buildings are**, is there a **mountain**, a **park**, a **lake**, an **animal** behind, or **any locations that can expose it.**

#### Step 4 — MAP MARKING

> **Mapping is not easy, but you can form an idea.**
>
> *"Is there a hill in the background? Okay, you saw hills. Is a river coming? Okay, a river"* — on that basis you can judge whether the river is big or small, **or anything that comes in useful for map marking.**

#### Step 5 — TRIAL AND ERROR

> **"Fifth and foremost."**
>
> **Whatever information, whether you're in the security field or forensic field or anywhere — you always have to TRY.** Trial and error: **you will get errors, so keep trying until you get the full information correctly.**
>
> **"Because somewhere or other you WILL get that information; somewhere or other it will have been publicly exposed. It simply cannot be that it was never exposed anywhere."**

### Why a methodology matters

> **"When you don't have a methodology and you don't have an APPROACH, then you will do these things BLINDLY and your time will be WASTED."**

---

## Part 6 — ⭐ Worked exercise: geolocating a photograph

### The source of the exercises

> These exercises come from a website — **"Sofia [Santos]"** — *"they have made quite good Open Source Intelligence practice exercises and are doing very good work. Very thank you from the side of Defronix Academy"*, because through these **we can give practice on OSINT exercises** — *"otherwise, if we just use anything [live], someone could create a problem in an illegal way."*

> The exercise page has **18 tasks** in total and **keeps getting updated.** *"You can go there and practise."*

### ⚠ Ethics statement

> **"Let me first say that this is JUST FOR EDUCATIONAL PURPOSES ONLY, not to cause harm to anybody.** We have taken it from where it was [published] and used it as a practice exercise. **We have no wrong intention in investigating this."**

### The task

> **"In April 2017, [the President of Somalia made his first international visit to Turkey]. Find out the NAME OF THE LOCATION."**

### The information you start with

| Given | Value |
|---|---|
| **Date** | April 2017 |
| **Person** | Mohamed Abdullahi [Farmaajo] |
| **Designation** | **President of Somalia** |
| **Event** | First international visit |
| **Country visited** | **Turkey** |
| **Source** | A news agency published the photo |
| **Met with** | The President of Turkey |

> *"So see how much information you have: a date, a city — it was visited, in Turkey — after that, who visited: the President of Somalia, whose name is this — after that, with whom did he visit: with the President of Turkey."*

### Step 1 — Analyse the photo itself

*"Now we don't know which one is the President of Turkey and which is the President of Somalia. We just have a photo. Now on this basis we will do a full analysis, and we will try to reach the EXACT COORDINATES of where they are standing."*

**Observations from the image:**

| Observation | Inference |
|---|---|
| A **flag** is visible | Belongs to some country |
| **Two people shaking hands**, looking at the camera | **The photographer is directly in front of them** |
| **A large DOOR** behind them | Entrance to a significant building |
| **A large BUILDING** | *"Some special building — it wouldn't be a normal building, wouldn't be a hotel"* |
| Both are **presidents** | *"Definitely this place will be quite confidential and will be under HIGH SECURITY"* |
| Extremely **clean and tidy**, flags of both countries arranged | *"It is not a public place — if it were public, they would be found walking around"* |
| A **logo** and a **star** visible | Identifying marks |

### Step 2 — Reverse image search

**Download the image**, then go to **Google Images → the camera icon → upload.**

> *"Now it is giving you some related information — same flag, same building, same people."*

He opens several results in new tabs, discarding irrelevant ones, and finds the same image on **Twitter** and on foreign-language news sites.

### Step 3 — ⭐ Use translation

> **The most important topic here.**
>
> *"This is not in our English language, so what will you have to do — TRANSLATE."*

**Install the Google Translate Chrome extension:**

> Search **"Google Chrome Translate"** → **Add to Chrome.** *"So that it becomes easy for you."*

> **"Many times a situation will come where the result you need will NOT be in [English]. For that we will use Google Translate."**

Right-click → **Translate this page** → English. *"Now you understand what's in it — it's a news [item]: 'Watch photo: President [X] met with President [Y]'."*

### Step 4 — Gather more angles

From the translated news pages and Twitter he collects **more photographs of the same event from different angles**, each revealing more:

| New detail found | Value |
|---|---|
| **Three large PILLARS** | Strong architectural identifier |
| A much **wider view of the building** | *"Really quite a big building"* |
| **Another angle, much clearer** | Something placed in the scene becomes visible |
| **Date confirmed** | 26 April 2017 |
| **Place name found** | **"Presidential Palace"** |

> *"Because the angle changed, we have more photos from different angles with more clarity — we got something more."*

### Step 5 — Confirm on Google Maps

Copy the place name → **open Google Maps** → search.

> *"Is the location the same or not? Look — it's confirmed. We have the location."*

### Step 6 — Google Earth for historical imagery

> **"Download the DESKTOP VERSION"** into your machine.

Paste the location and search. Then use the **HISTORICAL IMAGERY** option:

> *"The latest one shows up to [20]23. Can we go BACK? Is there a clearer angle?"*

He steps back through **2022, 2021**, looking for a clearer view:

> *"Look, here something is visible — that image would be this; the part sticking out. So it could be from slightly outside this building."*

He checks whether a **camera / Street View** is available nearby, highlights the spot, and zooms in:

> *"We got the EXACT location. **Which coordinates?** We can say the coordinates are here — because through this we confirmed that the location will be here, and **those three pillars are visible here**, between them [the handshake happened] — because the **gardens** are also visible."*

### The answer

| Item | Answer |
|---|---|
| **Place name** | **Presidential Palace** |
| **Location** | **Ankara** [Turkey] |
| **Exact coordinates** | Identified on the map |

> *"So those are the coordinates where the two were shaking hands, according to this image."*

### A note on Street View

He checks whether Street View exists at the spot:

> *"There is no Street View here; nothing is visible. I clicked here — there is nothing at all nearby. **No 360 camera is anywhere around it** that would expose it."*

---

## Part 7 — Mapping platforms

*"Since Street View came up, let me tell you about [alternatives]. There are some maps — listen carefully."*

| # | Platform | Notes |
|---|---|---|
| **1** | **Google Maps / Google Earth** | The default. Google Earth desktop has **historical imagery** |
| **2** | **Apple Maps** | *"Quite good in 3D terms; sometimes gives MORE clarity than Google"* — but needs Apple devices |
| **3** | **Mapillary** | **Owned by Facebook.** *"It has quite a lot of data too. Sometimes there will be Street Views not available on Google Maps"* — crowdsourced |
| **4** | **Yandex Maps** | *"Quite good data sometimes"* |
| **5** | **OpenStreetMap** | *"There are a lot of things in it too"* |
| **6** | [Chinese mapping service] | *"Quite good quality for China; buildings are all visible"* — but access is restricted |

### Mapillary demonstrated

> *"The green part is related to Street View."*

Searching Delhi, India: *"Look, quite a lot of data — Delhi is all GREEN."* Clicking a panorama:

> *"You get it in quite good detail. If I play it, it runs according to how the person took the photos, continuously."*
>
> *"You can even check **who took which photo and when**. It has collected data based on whatever photos you upload."*

---

## Part 8 — Reverse image search options

### 8.1 Yandex Images — often the best

> **"Yandex Images provides quite good results — BETTER results"** [than Google for this task].

He uploads the same image to Yandex:

> *"Look, in this it has **MORE CLARITY**, more results."*
>
> *"It figured out which language it would be in and translated it accordingly."*
>
> *"Look how smoothly it works — I clicked on this, and look, **quite a good [view] of the place, and more images came.** Actually we didn't have this much information; that image wasn't of this much clarity."*

**Yandex additional capabilities observed:**

- **Identifies objects** in the foreground/background and shows results accordingly
- **Detects text in the image** and *"tries to guess it and shows it on the right side of your screen"*
- **Can identify a flag** — *"Look, on the basis of the flag alone you can find out"*
- **Crop tool** — *"You can crop and extract even more information"*

**Combining with translation:** copy the foreign text → **open with Google Translate** → *"It will translate and give it to you in English. **How helpful is this for you?**"*

### 8.2 The Fake News Debunker plugin

> Install the plugin named **"Fake News Debunker"** [by InVID-WeVerify].

> **"After that you will not need to DOWNLOAD the image."**

**How to use it:** go to the website with the image → **right click** → the plugin's options appear:

| Option | Purpose |
|---|---|
| **Image Magnifier** | Zoom into detail |
| **Image Forensic** | Forensic analysis |
| **Image Reverse Search** | Search across engines |
| Individual engines | **Google**, **Google Lens**, **Yandex**, **Bing**, **Reddit**, **all of them** |

> *"You don't need to drag and drop. The same information showed on your screen. So it's quite good; you can use it."*

### 8.3 Other tools mentioned

**TinEye** — also usable for reverse image search.

---

## Part 9 — Extracting EXIF data

### Method 1 — Right click → Properties

> *"One way: right click on it and go to its Properties."*

In his demo the downloaded file showed little: *"16 July — meaning it's today's, because we [downloaded] it; this is its size."*

> **But normally:** *"Whenever there's a photo and you right click, **you get to see quite a lot of information** — which camera the photo was taken from, and **the geo-coordinates if the location was shared.**"*

### Method 2 — The EXIF Viewer Pro plugin

> **The plugin's name is "EXIF Viewer Pro."**

**How to use:** right click → **Show EXIF**

> *"Look — we got this information from EXIF."*
>
> **On Instagram images:** *"From Instagram you will get NOTHING."*
>
> On another: *"You get the EXIF information — **which location it came from**, the website's name, the image's size. That's all, because it doesn't actually have EXIF data."*

> *"If any image has data, then this can help you quite a lot; it will show you. So it is also a good plugin."*

### Plugin summary

| Plugin | Purpose |
|---|---|
| **Google Translate** | Translate foreign-language pages |
| **Fake News Debunker** | One-click reverse search across many engines |
| **EXIF Viewer Pro** | Read EXIF/metadata from any image on a page |

---

## Part 10 — ⭐ Combining Google Dorking with translation

> **"An important piece of information."**

Building on Day 2's Google Dorking:

```
site:youtube.com [keyword in local language]
```

He demonstrates with a famous valley name, then narrows using **Tools → Any time → Custom range** (from Day 2) to filter to a specific date range.

### Why translation multiplies dorking

> **"If you learned to use the COMBO of Google Dorking PLUS Google Translator, then I'm telling you — you will really enjoy it.**
>
> **You can make any searching [strategy]**, because you can go as far back as you want.
>
> For example, **if you have to search in another language, your work becomes very easy.**
>
> **Many times you will find results that are few in English — but the result related to that LANGUAGE [will be rich].** Because when you investigate, you will get an idea: *'yes, this place has this language.'*
>
> **Many times the LOCAL LANGUAGE gives you more and more EXACT things** than English. So what will you do — [if] it's German, French or anything — **you use Google Translate** and try to find out that information."**

**The workflow:**

```
1. Identify the local language of your target region
2. Translate your search terms into that language
3. Use them with Google Dork operators
4. Apply date filters
5. Translate the results back
```

> *"So you can change [your approach]. **If you learned the combo of Google Dorking plus translator, you will really enjoy it a lot.**"*

---

## Part 11 — Today's task

> **"Task for you people."** The image is on screen; **the screenshot will be sent in your group.**

**Exercise number 7** from the practice site.

> **"PLEASE DON'T USE THE ANSWER."** *"If you want, you can cheat there, no problem — but they have also given the answer and a write-up. Please, if you want to practise, DON'T go through the write-up."*

**To get the group link:** go to the Defronix Academy YouTube channel → **Playlists** → the **announcement video** (2–2½ minutes) posted before the course started → **the Telegram group link is there.**

> **"Keep the report of these answers ready."**

---

## Closing

*"So today's session — let's end it here; it got quite long. Already 7:15."*

### The poll for an extra session

> *"If you people are enjoying it — I'll run a POLL in the group. **If enough people participate, I can hold a session for you TOMORROW** on OSINT image analysis, because it's a long topic, an interesting topic, and I had some more labs to solve for you."*
>
> **The conditions stated:** *"I need a minimum of **30 students** live. Today there are 27; I need 30. **If even one is less tomorrow**, then [it won't continue daily]."*
>
> *"And one more condition: as soon as the session is scheduled, **I need LIKES before it starts** — as many as are coming. Here there were 23–27 people, so **I need 30 likes** before starting."*

**Go to the Telegram group, find the poll, and select whether you want tomorrow's session.**

Okay — so let's end today's session. **Bye bye, good day, and thank you for supporting.**

**So quickly like, subscribe, and don't forget to comment** if you people liked it. **And go to LinkedIn, to our page**, and there too don't forget to like and [comment].

Okay — see you the day after tomorrow.
