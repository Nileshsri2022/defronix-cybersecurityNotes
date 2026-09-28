# 020 — Day 5 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/020 - Day-5 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Image OSINT CTF lab (IMINT/GEOINT room) · Reverse image search in practice · Video geolocation · Report writing
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the captions are extremely fragmentary — this class is a fast, silent-typing screen-share of a CTF lab, so long stretches of the audio are just half-sentences spoken while clicking. Garbled terms restored where unambiguous: `इमेज ओपन सोशल इंटेलिजेंस` = "image open-source intelligence", `जिओ इंटेलिजेंस` = GEOINT, `मेट्रोलॉजी` = "methodology", `जिओ लॉकेट` = "geolocate", `ईटीएफ` = **CTF**, `बीकानेरी सर्कस`/`सर्कस स्टेशन` = **Piccadilly Circus (tube station)**, `वेंकूवर इंटरनेशनल एयरपोर्ट` = Vancouver International Airport, `एडिनबर्ग वूलन मिल` = Edinburgh Woollen Mill, `अल्बर्ट बयान` = **Albert V. Bryan** (U.S. Courthouse), `लेडी जस्टिस` = Lady Justice, `नव होटल`/`मेरी नव होटल` = **Novotel**, `डिप्लोनिक्स` = Defronix. The lab being solved is an **IMINT/GEOINT CTF room** (a "Searchlight IMINT"-style room on a CTF learning platform). Passages where captions collapse are summarised in [square brackets].

---

[Music] [Applause] Hello everyone, good evening friends. Tell me once whether everyone can hear my voice — quickly in the chat, yes or no… Hello, thank you.

First of all, welcome all of you to our **Defronix Academy** YouTube channel.

## Today: the last image-OSINT class — full lab, solved live

So what is today's topic? Again — where we left off in the last class — **Image Open-Source Intelligence** was running; this is its **last class** (the third class on it), because now it is a **totally practical class**. There is a lab — a full, complete lab — that **we will solve LIVE in front of you.** So watch how it gets solved, and if possible, you can also do it along — there's nothing [stopping you] if you have a laptop.

And if in between I take a small break while talking — please sorry for that, **I am taking my tea. Evening tea, that's it.** 🙂

### The platform

So this is the kind of platform where you can learn all the [security topics] — whatever there is, all the pentesting and everything — you can **practise** here, you can **play CTFs** here, on the basis of which you'll get good practice, and from here you'll get the real-life fun of how [challenges] are found and solved. **This will help you use your own methodology and see whether you can find things out yourself.**

Let me quickly **join the room**, and after that we will solve this lab completely. Okay:

> *"Welcome to the [Searchlight IMINT] room. In this room you will be exploring the disciplines of image open-source intelligence and geospatial intelligence — which is the short form: imagery intelligence (IMINT) and geospatial intelligence (GEOINT). This room is suited for those of you who are just beginning your open-source intelligence journey and those brand new to the field of IMINT/GEOINT."*

Okay, some things are written in it — all sorts of things — we won't pay attention to [all of] that; if you want, you people should pay attention to everything, but I don't need to read it like that; we're going to work directly.

What does it say? It says that if you have to **submit a flag** — whenever you solve any answer to my questions — you have to write it in **this pattern** [the room's flag format], and after that submit your answer; [where] "no answer required", okay. So you have to keep your answers ready. Once — *"yes, I am ready"* — and after that let me tell them… let's go.

---

## Announcement — your task: the DETAILED REPORT

One more announcement for you people. What am I doing? This lab of mine — **I will try to solve it fully, completely** — if I leave something, it will be for you people to solve; otherwise I'll try to solve the whole thing, however much time it takes.

But you people have one job here: after we solve this lab, **on every single image you have to perform an analysis** — what you saw in it, what information you could collect up to what level — and for every task, for the answers to its questions, **you have to prepare a DETAILED REPORT.**

That detailed report — you have to make a **Google Drive link** of it and **submit it in the comment section on our LinkedIn page.** Whoever writes the **best report** — we will also announce that this person did the best analysis. Let's see who has learned how much.

So please, a request: if someone is interested… and if someone isn't — *"sir, we just come to attend live and watch"* — it makes no difference to me 🙂. But note: **whether someone is watching this as a recording or watching it live today — anyone, at any time, can go to our channel/page and submit their Drive link in the comment section on the LinkedIn page.**

---

## Task 1 — "Welcome to Kanab" (the state)

Let's download [the image] for the first challenge — all the techniques I have taught you are going to be applied here. Downloaded — let's open it. Now an image is in front of you — let me zoom.

You all know: whenever an image comes to you, to analyse it you have the **five techniques** I told you — **context, background, foreground,** [crossroads/signage, map verification] — those things. So let's analyse.

What do we see? Zooming: **"WELCOME TO KANAB"** — "welcome to Kanab" [town sign] — and here you see **"22 stalls…"** / some lettering like *F-O-R / N-O-R-N-O* [partially readable]. But this will be a very simple challenge.

First we look at **what he wants to ask**: the question says — *"What is the name of the STATE where this image [was taken]?"* You have to tell the name of that place — the place where the photo was taken.

We have quite a small photo, but "WELCOME TO KANAB" is written on it. So just looking at it, I think that itself should lead to the answer; otherwise, if that's not the answer, we'll also check it once with **image reverse search** — then you'll know. So let me do that — we perform a reverse image search — here it is — upload… and you can see the [matching] images came, it's on YouTube too, in many places. He only asked the name [of the state] — so that is our answer [**Kanab → Utah**].

We'll try to solve everything, totally — but **we won't spend that much time on every single image**, because look: in the last two classes what did I do? I taught you the techniques — how to [analyse] an image, how to geolocate — I've told you all of it. **You have to apply all those techniques here.**

---

## Task 2 — The London tube station

Next: the questions first. It asks: *"Which city is this tube station located in?"* and *"Which two [attractions/stores] are there…"* — a **tube station** — "tube" [can mean] an underground passage made to go somewhere, under the road, or there may be an underground **metro** under it — anything could be underground.

Now, what was written on top? Let's zoom: it says **"…CIRCUS … STATION"** — yes, a "…circus station" is visible here; the rest is hidden. And if we look to the side: a **GAP store** is visible, and above it a **HYUNDAI logo**, and a bit above that a **COCA-COLA logo** on the building nearby. Next, if we zoom — yes, a [curved corner building] built together…

So this is our analysis. First perform [the search]: what does the place name suggest — **Piccadilly Circus**, okay… I mean [Music] it is that, but it could be… you'll see many images… no, this is not it… no… station… okay, okay… Wikipedia… lots of photos… is it that one… hmm, something's missing… okay okay — these pictures we have — this kind of street — meaning it's near it. So what do we check around? If you look at the [street] camera footage — the **GAP store is somewhere on this side** — you'll be seeing it — now look at that photo: there was the Hyundai [sign], this is the GAP store — basically it would be right here; there's a road, it's somewhere nearby, because it's not exactly adjacent — it would have been taken at this angle. **London** — okay, it says it's in **London**, and the right station… *"arre yaar, bhaiya, what are you saying"* [reading chat] — you can find that out anyway, because we have the information; from here Google search will do the work for us. Done — [answers submitted].

---

## Task — The airport building

Task 4 has come. Now this picture: *"Which country is this building located in?"* and *"Which city is this building located in?"* — where was this photo of the building taken from, which building; which country is this building in and which city?

Very good — general analysis: what's visible? This is mounted here — [a "YVR" sign / airport signage] — [reverse search] → **"Vancouver International Airport"** [appears in results; also a similar Bengaluru airport stock image]. Meaning **this is a picture of an airport** — like airport stock footage — look, about this we get the general information — here it is, everyone must be seeing it — like that, look, on top of it… a building **inside the airport** — right? Yes — correct.

*"Which country is this building located in?"* — which country? Now we have the airport, so we look at where — Wikipedia — city — [Vancouver, **Canada**] — and the airport location. **I don't know any of this in advance — I am doing it right in front of you.** Done.

---

## Task — The coffee shop (email, owner, phone)

Next — let me download this and close that. Now we have an image — meaning it's some **coffee shop** — yes, we can guess it's a coffee shop… [zooming] **"Edinburgh Woollen Mill"** / **EWM** — that's what I can see in it.

So let's do one thing — first, about this, we do **image reverse search**. That's what we always do first — reverse search; we'll give the answers to the questions later. Upload… our first job is: **what does Google know about this image?**

From a **Facebook page** we have this… there's an **Instagram page** too — we don't need that yet — and what [do the questions ask]: first, the **email address**; *"What is the surname of the owner?"* — interesting! — I think it should be this… **got the mobile number**… and here we got the **email ID**.

If you have doubt about anything — suspicion — **you MUST verify.** To verify, we go to **Google Maps** [find the café's listing] — the mobile number… *"in which [city] is this coffee [shop] located"* — the name — I think it was right here… where did the Facebook page go… no, no — I think it's this one… it's a coffee shop… the website — you can read it… let's open [their pages]… okay — done. **So we solved this lab [task] too.**

---

## Task — The restaurant

*"Quite something — reverse your thinking!"* Let's see what's in this one: [people] sitting, and quite a lot of lighting… open it… [reverse search]… let's see what he wants to ask — okay: *"Which restaurant…?"* — we see some **nickname**… what did we search? [the deli] — location — and this is what keeps coming out. If I confirm — it **is a 24-hour restaurant**… something about it in Wikipedia… [Music] …what is this — *"[the outlet's] deputy editor Andrew … recently at the legendary 129-year-old…"* [article confirming the restaurant] — downloaded, done.

---

## Task — The statue (Lady Justice)

First: *"What is the name of the statue?"* Close, close, close these… the last [tab]… yes, there are many — 99… let's see… opening… and there's one more… next, next… information… no… *"not just the answer — justify [it]"*… [Music] *"arre yaar, you tell me, yaar"* [struggling]… this one didn't work out — it works and it doesn't… **similar images**… not done… we're trying to find out — so what should we do? There's nothing here, nothing here — so we always have to go [to the next tool].

Let's also try searching [in another reverse-search engine]: there is *something* — the statue's name — but it's not coming here. Let's take an idea: S-T-A-T… the spelling of "statue"… [Music] *"it's some… liberty or justice…"*.

Now, this task — these are not photos of its inside; it's in front — meaning we can infer: the photo you see, where this statue is installed — **it's installed somewhere OUTSIDE a building**, and in front of it there's some building — quite a big building — because from the side where it's mounted, look: **1, 2, 3** — we can see one, two, three buildings. Okay.

So let's reverse-search this one too. Now look — something shows up: *"What is the name of the character that the statue depicts?"* — okay, "name of the character". Let's open an article about it — some information — meaning **it's some COURT-type place** — a place where there's a court — **and it's exactly the same image.** The image's name… [various results]… let me translate — same location… *"what about it… no, no… BLIND JUSTICE"* — it looks exactly of this type… okay, friend — about it: **"Justice holds the scales of justice and stands above the front entrance of the Albert V. Bryan [United States Courthouse]"** — okay! We got a piece of information: **it is in Alexandria, Virginia.** Okay okay.

*"What was the…?"* — what was our question — here it is — *"statue located…"* — same location… and what about this photo… but — **there should be a NAME** [of the character]. So let's do one thing: we go to the location on **Google Maps** — Google Maps — what do we get, any information visible — here — what is written on it — so it's **opposite** [the courthouse] — we saw, right — the **district court**… reviews… related, some more information — the district court — let's locate exactly — I think **this is exactly that building** — exact — and back — **yes! We got the building's name.**

Let's check what more information there might be: [Music] — *"the statue … **LADY JUSTICE** … is the model…"* — J-U-S-T-I-C-E — **Lady Justice** — the district court. *"But what's the name?… sir…"* — yes, we have to make certain of the statue's name — so do it: what hint do we have? You would have to read the whole Wikipedia [article] about it, because — it's possible — **the blindfold is tied** [blindfolded Justice] and — absolutely — we'd definitely have to make sure what it really is. But whenever you search **"Lady Justice"** — what should I search within Lady Justice — there it is, in front of you. **Got it.** Next.

---

## Task — Geolocating a VIDEO (the Singapore hotel)

Next number — let's see what it is. It's a **video**. Now keep one thing in mind — a small method lesson:

> **Whenever you try to geolocate through any video:** first **watch the FULL video**, and then [note that] the video will always be turning either **left-to-right or right-to-left**. Once you've watched it fully, you'll know how it's taking the angle — left-to-right while recording, or right-to-left. After deciding that, **take screenshots of the places you think [are useful]**, then put all the screenshots one next to another / one over the other and try to match them. This way you will have many images, because of which — whatever you do — it will give you the idea of what I actually want to do.

So now what are we doing — look, I'm watching the video again: whoever is shooting this video is at quite a **height** — and — one minute, wait — yes, here it is — there's a **balcony**; and this — a **riverside point** — it's written on it… next you see an interesting place — you have this — a [river]side point [Music] — visible — **"CENTRAL"** — meaning basically its name is **Central** [The Central mall, Clarke Quay] — after that you can see **three big buildings**…

Okay, last start — analysis: where is "Central"? — **Central, Singapore** — meaning it could be **in Singapore**. Let's directly open it inside Google Maps. It should have images — okay — inside-out — I don't care about the inside — okay, **I got the 360° view** — 360° view — the **river** is there too. If [I check] this video — [the name] is written on one of these buildings — and it's also exactly **opposite** it — look, **the video is being shot from right in front of it.**

One minute — before zooming — here — the video is being shot like this — one minute, one minute — from directly opposite. So — look — because if you look at the angle — let me go back a bit — you'll see — 1 minute, 1 minute, 1 minute — **here it is.** After zooming, if you look — it's exactly in front of me, and at an angle, and I'm at a new angle — so we can [start] confirming: it could be one of these buildings — either this one… then we look — is anything else visible — I can't see it — meaning I've got this much idea: **Central**… and this one — look — that same one…

If you can't see it, let's go back… okay, we found it — where did it go — *"arre, go back"* — and then — come on — **the building I'm talking about — it could be this building** — and if I turn it more, make an angle — if I look from an angle — here it is — **this hotel** — and I'm in 3D a bit — and if I look at it: **here they are — the three buildings that were visible right in front — in front of the hotel — the ones that have the park on top** [the towers with the sky-garden] — that was visible too. **So I became CONFIRMED: the video would definitely have been taken from THIS building.**

If I do one more thing — there's a 360° here — let me look — one minute — we turn — now this building — for me to remove doubt — what is this — **it is the NOVOTEL hotel.** We can check — let's look at it — the photos are the same — the inside photos — submit — **Novotel** — yes, this is the name. *"What is the name of the hotel?"* — my friends — let me write its name. And if I [check] the angles — yes, right — because all the angles being formed are from this side — **and this is that hotel.** If you want, see for yourselves — here they are. (Here there are only so many photos, taken long ago… and anyway there's no outside view anywhere inside it.)

---

## Last task — the motorcycle photo / the Twitter handle

Let's open the [room] again — last, number seven — here it is. Let's search once more with this — we must have missed something in the hurry. Last number 7 — open — next, next — let's work — **Facebook**… chrome **master cylinder** [motorcycle part]… *"could it be this one?"* — now we've found something — a **motorcycle**… **2012, December**… problem… **up in D.C.** — so the location — let's dig behind it some more — we'll find something or other… [Music] …this isn't it… and **what is his name — okay — his TWITTER HANDLE** — we got the answer to our question.

---

## Wrap-up

Tell me once — did everyone enjoy it or not? **You have to write the report** — let's see who can write how detailed a report about their searching. Tell me, tell me!

[Session ends.]
