# 019 — Day 4 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/019 - Day-4 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Image OSINT labs · Geolocation from a caption report · Photo verification · Identifying people in a photo · Signature analysis
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the auto-captions are heavily garbled in places (`ओसियन` = OSINT, `सोफिया संतोष`/`सो टायर सेंटॉस` = **Sofia Santos**, the author of the published OSINT exercise set used for these labs, `एसियाड क्लासीफाइड डॉक्यूमेंट` = "a CIA classified document", `असकानिया`/`अस्कानिया` = **Askania** (the Berlin factory), `तेल इसको`/`टेलिस्कोप` = "telescope", `बोन`/`बोर्ड` = **Bonn**, `माउंट पार्लर`/`अमाउंट पलस` = **Mount Palomar**, `कोऑर्डिनेट्स` = "coordinates", `जिओ लॉकेट` = "geolocate", `जेंटलमैन`/`डेंटल मां` = "gentleman", `लिबींस`/`लेवल पॉलीटिकल` = "Libyan Political (Agreement)", `मुस्तफा आबू शाखा` = a Libyan signatory's name as read from translated Wikipedia). The intended technical term has been restored where unambiguous. Passages where the captions collapse entirely are summarised in [square brackets].

---

[Applause] [Music] Hello everyone, good evening friends. Tell me once whether my voice is reaching all of you or not… Thank you, Tom [a viewer]. We won't wait too long — we will continue our topic — but let's see how many people come, how many people join, after about 5 minutes. At least yesterday's strength is needed, because yesterday you people promised when 27 of you were live…

So welcome, all of you, to the YouTube channel. My request to all of you: **please don't leave in the middle** — quite an interesting topic is running, and all the classes in the coming time are going to be very interesting; you're going to get to learn a lot.

## Course admin

So if you like these sessions, if you feel that [this training on] **publicly available information** is going to help you a lot, then make an ID [on LinkedIn], go there, go to our page, and what you have to do — **comment**. From that we get to know about your presence, how actively you are engaging with our present class.

In these classes **we are going to do maximum practice through labs**, so you will get to learn a lot, so that you become comfortable with how any information gathering is done. After that we'll move on to further topics.

## Recap of the previous class

I have already told you the first points we are learning:

- **How to do image reverse search** — you all know this now.
- Some important things — **EXIF / metadata of an image** — I have also told you about that.
- Some important points related to **OSINT** I have already told you.

Whoever doesn't know this — anyone who has joined the class for the first day today — **please go and definitely watch the last class**; our classes are running on that base. [It covered] how you can **geolocate any image**, and there was an example [of that] which we have already done by looking at that image. Mostly I think people will have done it; those who haven't — do it quickly.

And I don't know, brother, why people ask in the group — *"Bhaiya…"* — when I have already told you on the channel: go to a website, it is **Sofia Santos's**, and from there you can get the information; go there and look at **task number 7** or whichever it is. Then why do you need it specially provided? After going there you have to do one good Google search. **If you cannot search for a website that is live, on which your task is, then how will you say "I will extract information about images"?** That I don't understand.

---

## Today's plan

Today there are **two examples** that we are going to do, going to learn, in today's class. If we need to give any additional information about any tool, I will provide it during the class itself. **There will be no slides and no special lecture for this, because we are going to do totally practicals** — quite interesting practicals.

### Disclaimer

One thing here — you can call it a disclaimer: **all the practice being done here is for educational purposes**, and all the information we are using in our exercises here has been taken from a website by **Sofia Santos**, who has provided very good exercises for OSINT practice — so very thankful to you. **But all of this is for educational purposes; it is not for exploiting or misusing anything in any wrong way.**

---

## Example 1 — The telescope in the classified caption report

So the task we are going to look at — what is today's task?

> *"The image below is a screenshot taken from a CIA classified document. It depicts a caption report of an undisclosed photo. The text mentions a telescope being assembled at a factory. Your task is to find a photo that matches the description on the caption report, and the exact location of where the telescope was placed once completed."*

So your first task is: **find the photo that fully, exactly matches this description.** And [second]: **find the exact location** — where this thing is at present, after the work that was going on was completed — **and you also have to provide the coordinates.** There is not much information in it for us to work with.

I have brought that photo in front of you — this is the [screenshot] on whose basis we will do our analysis. Let's start the practical quickly, we won't waste time. Let me take a sip of my tea… okay, let's go to Sofia [Santos's site]. Okay — we download it and will do the full analysis on its basis.

### Reading the caption report

Now here is that image. Look at the image — what do you feel when you look at it? First of all, the report written in it is **entirely in English**. So there are some things you will understand just by reading:

- At the top you read **"caption report"** — so you learn this is a report made about some photo.
- **Where was the report made?** Germany — specifically **Berlin**. So the report is from Berlin, in Germany. That's one thing we learned.
- Second, you also get **coordinates** — 52…/53… [partially readable] — you can see them with the help of this image.
- **Continent** information is also visible.

Then there is the **description**. Reading the description, what do we understand from it?

> *"…Askania factory … for the University of Bonn … the size … 20 times bigger than the Mount Palomar telescope camera … 20 feet … weight … January 18, 1953."*

So some description is mentioned in it. Now look — right now **our biggest challenge is that we do not have the photo.** The biggest challenge is that we don't have the photo. First we have to analyse what information we can put into our notes on the basis of this:

1. The report was filled in **Germany**; there is some **coordinate** information.
2. What do we have here? A **telescope** — so we have telescope information.
3. Where was it made? It was made at a **factory** [the Askania factory].
4. For whom? **The University of Bonn** — for Bonn's university.
5. One more piece of information you will see: *"being assembled at the factory"* — meaning **it was assembled in the factory**.
6. Its size: *"20 times bigger than the Mount Palomar telescope [camera]"* — so we are automatically talking about some **large telescope**, not a small one.
7. Also, [with it] a large size of stars can be seen.
8. And **when is this report from? January 18, 1953.**

### The four questions again

For any report, for any image, we have those four-five questions: **WHO, WHAT, WHEN, WHERE.** Now, we have the answers to some of the questions here:

| Question | Do we have it? |
|---|---|
| **WHAT** | ✅ a telescope |
| **WHERE** (of the report) | ✅ Berlin, Germany |
| **WHEN** | ✅ January 1953 |
| **WHO** | ❌ to find |

So we have the answers to three questions — **what, where, when** — and our analysis, and our Google searching, will start on the basis of exactly these three, because now we have to try to find out the [remaining] information.

So let's go to Google. And if in between I pause for a second or two — I am taking my tea, so if you are also working along, you can also take it. 😄

### Googling the description

Let's Google. What do we have? A **telescope** — I have already worked on this earlier — so we simply enter it into Google [something like *Askania telescope University of Bonn 1953*]. What do we get from here? We get several results; let's first go to the first report, on **[an image archive site]**. Look, what is written here… okay, we have found some information which we now try to analyse.

One minute — what I do is open our image [the screenshot] in a new browser window alongside, so I can compare. [Reading the found article:]

> *"…telescope has been built in the Berlin factory of Askania … for the first time since the war … January 1953 … for the University of Bonn … to study and take pictures of stars … with this telescope stars of the 23rd [magnitude] can be seen … the size of the camera … 20 feet … weight …"*

So: it was made in the **Askania factory** — that **matches**. *"For the University of Bonn"* — that matches too. *"To study and take pictures of stars… with this telescope stars of the 23rd [magnitude] can be seen"* — okay, so a second description point **matches** with ours. Then *"size of the camera 20 feet… weight…"* — meaning the type of description we see in this report matches this article.

And with this article we get a **picture** — this is the picture we can see on our screen. This *could be* the picture we are talking about: look, the size is quite big, and on top there is some camera-type thing mounted. But **we are still not SURE** whether this really is the picture. See — we had a report, and on the basis of the report the sense we were building, the things we could verify from the document's description — this [picture] is in front of us, and its description is exactly the same. **But we are not ready to accept it yet** — we are not sure. So to verify this information, what do we do? **A little more research** — whether this picture is exact or not.

### Reasoning about where the telescope went

Note one thing here: it says it was **assembled** at the factory **for the University of Bonn**. That means it was made for some research purpose. So it's possible that, since it was made for the University of Bonn, **it was also placed somewhere for that purpose**. And if it was placed somewhere — such a popular, famous thing — **someone or the other must have taken a photo of it.** Let's try to find out.

So now we come to full screen and Google a bit more. I have already done this: [searching] *telescope … university … 1953*. Hit enter — now what information do I get? A variety [of results]; the top article — I could open any number of them — let's try to open the very first article.

In this article, what is there? Some categories… some old [photos]… look, **some locations are mentioned**… okay. This could be the building. So we try to match that description with it. [Instructor compares the found photos against the saved image.] This one is not it — the size is quite small, the description says "possibly not"… go down, go down, go down… okay, this is also not there… this is also not it… and this — okay, **this could be it**, but the chances… we try to match it with the exact image.

### Finding the exact location — the observatory towers

Our second question was to find the **exact location** — where this telescope [ended up]. In this article some information is visible: *"…**34/50-centimetre telescope**…"* — so we have the telescope's name/type; then *"**Askania, Berlin, 1954**"* — so it took about a year more; and then *"…**list tower … 1953/54**…"* [the **Hoher List Observatory** towers of the University of Bonn] — and photos.

So we have the telescope's designation. Let's Google it. Copy… and we will try to use a small [advanced] operator: we put it inside **double quotes** and use advanced Google search, [restricting the years] 1953… 1954… hit enter. Some information comes… the university… and if we go to **Images**, we see all those things — this photo we already have, and — for example, let me open this one — this information I have… and **this one — look — we have a CLEAR image.** If I zoom it and show you: **the same description matches.** This is the full image — workers must have been working on it, [assembling] it.

And one more thing — look here, if I zoom… let's open it in a new page… we have some more information — a presentation-type / graph-type diagram of it too. Okay — this is also a very good find. So we got this information; Google image search — done.

Then we go to the website [of the observatory] to find **exactly where** this is. For that, a location is mentioned — **Tower [1] … 1953/54** — and if you noticed, when we were scrolling that website up and down, we saw that its **latitude and longitude were mentioned somewhere** on it. When we looked right at the front — here it is — it shows: okay, it's publicly [listed] — **here are the latitude and longitude.** So we have them.

So let's open them in **Google Maps** — paste… enter… [the map takes a while] — no no no, the internet is fine, but it is taking so much time… Is anything available on the map at this latitude/longitude location? Okay… let's test… okay — **it found something.** If there are photos, we'll get them… and look — **all the photos of this very location are available here.** Absolutely, absolutely — what is this? **Tower 4… and this is Tower 1.**

Look at the image of **Tower 1** once. What does it have? If you analyse it: right at its side there's a building, there's a **tree**, a small **pathway** is made… So which of these could our Tower [from the 1950s photos] be? Looking at the type — **it should be this one** — because look: three matching things — a small [pathway], and the same kind of [dome] work is visible there.

But we are still not sure which tower it is. So we try more: okay, here we have a [user-contributed photo] — click — what can we see from here? Look… if we zoom this… yes, it appears like this… let me open this in a new tab too… here it is… and now if we zoom this: do you see some **markings** here? On this side… and here as well, at night, we can see the same… okay — so we can see these things on the tower.

Look — okay, these are the buildings… the same **small tree** is also visible on this side, right in front… it isn't appearing here because the photo was taken from a single angle — it depends from which angle the photo was taken — so we have to guess a little. Okay: **this is that building; this is that big tree** — if we look, this tree looks quite [prominent]; and look here — this would be that tree's shadow, you can see it. One minute… yes — in front of this tree there is — okay — a **strip going across — meaning a path is made**; then you'll see **one, two [benches?]** — right next to this building — one, two, visible… meaning: yes, one and two are visible.

So basically, what could we establish?

1. **This is Tower 1** — of that we became sure from here;
2. we could see **the big tree, the path** that we saw [in the old photo];
3. since the [old] image was taken from quite far, the building [from which it was taken] wouldn't itself appear in it — it could be one of these — this one, or this one.

So we got a good idea — **this can be your Tower 1.** But are we yet SURE that [the telescope] is in this very tower? For that we need a little more clarity — **is it really placed in Tower 1?** Who can give us that clarity? **YouTube can.** So for clarity we go to YouTube and search… what was it… **observatory** — **Hoher List Observatory** — see, in analysis it's always like this, it takes time — we type the name… B-A/T-O-R… something will be found… and we can [scan the videos] — we have some… at 16–17 [minutes?] — look, an image — **this image — one more image — of that same place.** And one gets a little confused whether it is mounted inside this very Tower 1 — but finding that inside these videos **will take time**.

**So this work is yours** 🙂: from YouTube (or something else) you have to **confirm** that this is Tower 1 and that the thing we are looking for is inside this very one. Okay? You will do this. We have everything… okay, one more thing… done.

So — **we finished one task.** Let's quickly close all these things. In this way we completed one more OSINT [exercise] very successfully.

---

## Task 2 (homework) — Verify the Pakistan "suicide attack" photo

Now, next, there is a **Task 2** for you which you have to do and bring. What is it?

> *"On January 19, 2023, a journalist with almost 140K followers on Twitter shared a photo of smoke and fire, claiming it depicted a suicide attack in a city of Pakistan that killed 3 Pakistani police officers. The photo is not of the event described by the journalist. Verify the statement above."*

What the statement is telling you: on 19 January 2023 a post went out from a Twitter [account] — a photo was posted — and **on that basis you have to analyse: is this right or wrong?** You have to analyse this. The photo — you will find it easily; I will tell you where it is, which [exercise] number it is. So that is your work.

---

## Example 3 — Who are the four gentlemen?

Now we move to our third [item] — one more example (I wrote "Example 2" [on the slide], it should be Example 3 — it's okay).

The biggest challenge we have here: **we have just a simple photo**, and we have to find out **who the four gentlemen are** — 1, 2, 3, 4, whom you can see. **A very typical task — it is not easy.** There are four gentlemen; we have a photo, and the photo has been shot focused only on them; and on that basis we have to work — **you have to find out the names of all four.**

Let me tell you where this task is. We go to Sofia [Santos's site] — I have already opened it — this was our [previous] task… and the one you have to do — you have to go to this one: **gralhix[.]com's list of exercises** — okay. [Exercise no. 6.]

### First: analyse the photo itself

Now let's start the analysis: what can you see from this photo? *This is exactly the specialty of image analysis — look at every single thing carefully.* It won't even zoom [much]. So:

- First of all, in this photo you can see **four gentlemen** — 1, 2, 3, 4.
- Look carefully at everything: **tiles** are installed [on the wall] — blue-coloured with a dotted-line pattern.
- There is **one more gentleman behind them**, [partially] visible, who is wearing **spectacles**.
- Then, one gentleman has a **pen in his hand**. From the pen one more piece of information gets confirmed — he is **right-handed**.
- You can see a **long table**, and on the table you can see **HEADPHONES**. Now generally, where do you get to see headphones at a venue? We see headphones especially where **translation work** happens — nobody gives headphones for music. So this is a place where — the four gentlemen you see sitting — it may be a **meeting of countries, a conference of countries**, because translators are used — meaning **not one language is in use; multiple languages are in use**. And where are multiple countries usually involved? Okay — this is confirmed/clear [as a hypothesis].
- Then look at the **bottles** — not simple water bottles; they look expensive, stylish. So definitely [a high-level event].
- In the **background** there is a **banner** — so some **deal is happening or some event is happening** here. This is the way it is where events happen or deals/signings happen.
- We can't read [the banner] — it is completely blurred; if you zoom an edited/blurred thing it will only get worse. We are not reading a single word from it. [But] an event is happening or a deal is being signed; **on top of that — the headphones, the table, the banner — definitely there would be MEDIA COVERAGE here.**

> And [a tip]: don't just try to [find someone else's write-up] and quickly grab the information. **If you do the analysis yourself, it will be better for you** — otherwise you'll have a big problem later; you won't be able to do it.

### Reverse search

So this much information we could extract from here. Now we do a **Google reverse [image] search**. Right-click — we have the extension — reverse search the image… quickly, image, come on… okay, let's download it and search with the file. Okay — what do we get to see… no article comes… okay, okay — we can see some **sources**… and I am seeing something interesting here: **"UN Security Council … 17 December 2015"** — we have some information!

So what do we have now? A **political agreement**… where… and one more interesting thing — let's open it — look, this is **their website** [UNSMIL]. On top of that, from this we learn **when this photo was taken and by whom**. So the chances are this photo will be found inside this [site].

*"Wow, you work so fast, so fast!"* [reading chat] — but did you do the analysis yourself? On the basis of the article, how much analysis could you have done **if that article had not been found**?

So on the basis of this information we search inside it: we have **"security"… and "December 17"**… okay, search… we get some related information: 18 December… 17 December… an agreement happened… **"Libyan parties signed the Libyan Political Agreement"** — okay, we open it — *"…political dialogue … have turned the page … in the history…"* — okay.

### Matching faces

Now we will try to match a bit. Some information is visible here. First: do you feel you can identify any of these three [people in the article photos]? Does any one seem to match a gentleman? **No** — look, this one has [glasses] but not like his; this one has hair on his head… Next image — to verify whether these three are the same people… next — can you see anyone matching in these three images? **No.** Next, next — nothing special… okay, next — okay, we found an image; let's open it in a new tab. Does anything match for you? Look at him, and look at him — a little bit… it's a bit dark [blurry]… okay.

So now we are at [gentleman] **number 4** — we're trying to identify him. He is wearing **glasses** — exactly that style — and **look at the hairstyle: exactly the same** — and the height… If we guess a little — look, if we zoom — look at the cut/parting, if we try to identify the body [build] — and likewise above his glasses — you'll see a slight [distinctive mark] if you can zoom — **absolutely, it is him.** And then, look here a little carefully — his **beard**… So we became fairly sure: **this fourth one — it is him**, the one in the image we have — comparing this photo with the one we have… okay — **we found the image match.**

Next, look here — absolutely… *"arre, where are you going?"* [to the browser] … okay. And more information: the picture you can see — the one we just opened — **exactly the same style of [suit] he is wearing, with that lining, that colour** — if you try to identify — like that, white [shirt]… and if we look here — from the same event we have a **clear photo** of this person.

So basically we could [confirm] **two people's [faces]** — but names still have to be identified, and we [only] have images. Is there any more information in this?… No… Meaning now we need [something else]. Is this the **first time** such a meeting happened? It wouldn't be the first time — big deals don't happen in one day — so there must have been [meetings] before this too. Let's try more; let's try to find more images… next, next, next… okay okay okay… we [see] a name — **political dialogue** — could be… related to this… next, something else… *"honoured by … Libyan Political …"* okay… anything else, getting some information… **"Libyan Political Agreement …"** [searching inside] the secret… let's try.

Look — if I show you an interesting piece of information — look here… one minute, go back… and — look at this — if I zoom and show you: **what do you see?** They match, don't they… the same people we [saw]… look here… okay — **the file is the same.**

And let's try one more gentleman: if [we compare] the coat — look at this image, and this image, and this image — the shape matches a bit, doesn't it… a little… absolutely — the same style, blue [suit], slightly white [shirt]… beyond this we don't have a clearer image, but on this basis, here — hmm, it doesn't quite match that way… okay… let's see… So this is what we can use to figure out whether it's him or not — meaning we have a rough idea.

### The Wikipedia + translation trick

Okay — look, this information — because this image of ours had become clear here — inside this image… let's use **Google Lens** a bit… okay, using Google [Lens] image magnifier… no, no, no… [trying repeatedly] …

If we can even get an idea — [someone is] signing a document at the table… so hard… okay — so let's see, let's try a bit more… the file… because look, this is right at the end, the file [signing] is about to finish… if we guess… Let's do one thing first: we have this [photo] from here — let's do a **Google reverse image search** on it… my Google image search works in its own weird way, I don't know… let me just download it… *"come on, brother"*… okay, let's talk about translating: okay — no, is anything visible to you here? no…

Then if we test here: look — [an Arabic-language page] — okay. **If we translate it — we can translate it** — because it is **the same image, the exact same image** — you'll read about him **in Wikipedia**; we can translate the whole page. How? Simple — we have the translator: **right-click → Translate this page.** Next… okay — **"Mustafa Abu Shagur"** [Mustafa A.G. Abushagur / "Mustafa Abu Shakha" as rendered] — **we got a name!** We have one name — Mustafa. Look, after that: *"…who is the most…"* — you can go read about him — a [former] Libyan [Deputy] Prime Minister — and you can see more about him, see him in meetings, and more. Meaning: **we have one name — one name has come to us.** Okay — so we could confirm one person; we got his name.

At the start I had said — one minute — there was a good image here… this one's work is done, let me remove it… I've downloaded it… look — **this is what Google can find out about an image.** It will translate if it can, otherwise it won't…

### The signatures trick

If we look next: *"…Mohammed…"* — let me highlight all of it — is more information coming? and this information… okay, fine — let's work with what we have. We have the image, right? So — okay — let's **zoom this information**: now, **where are they signing?** Look at where the signatures are: if you look carefully — first, second, **third** — [our man] signs at **number three**, because we have the picture of the signatures [page]! Great — for us there could be nothing better than this.

We go back to our picture — **the third signature** — here it is — so we **copy** it and try to find out which person it is. We go to Google, next, find their names… we have this… so it's the same person… here — *"translate it, translate it"* — his image… now to identify this name properly, we translate it — to English. Okay, we translated it into English, and the name we see — if we also search it in English… [Music] *"this is the limit — copy it, yaar, copy-shopy"*… let's do something… okay, come on, come on… *"arre, it's showing something — Google has also gone mad"*… **information, related images — quite a lot of information about him has come out.**

**So two names have come before us.** To confirm, you'd Google a little more — you'll get time.

---

## Wrap-up, homework and admin

Now look, one thing — it's 7:30 — tell me, is everyone enjoying it? See, **in this way anyone's information can be extracted — they are even inside their signatures; we have to identify them, analyse on that basis, and we can extract their names, their information.**

So in this way **we have found out the names of two gentlemen, and two are left**. Those two — you people will do them. *"Is it getting a bit boring? Wake up a bit!"* 🙂 — for some of the exercises I come slightly prepared in advance, because otherwise, if I sat here [doing everything live], how much time would it take?

So do one thing: this image's exercise number on Sofia's [site] — **I found the names of these [two], and you have to find the names of the two that are left, and tell them by commenting** — everyone — what the names of these two people are. **It is exercise number six.** If we go back — this exercise of yours — if you go, you will see it. **Just don't look at the SOLUTION.** [And earlier] I had told you [exercise] number 11 — finding [the location] — that one too. Our session has already become quite long… finding the name is your job — it will get done.

[Answering a chat question:] *"If someone clicked [a photo] at their house and sent us a screenshot of it, can we get their location?"* — Look, what happens is — you can TRY. Suppose you take a photo inside a room and it's saved in your mobile — for that, the type [of analysis] is different. **Everything is possible if it is publicly available.** [Metadata, etc., otherwise not.]

So — you are getting the present status. Comment there too, on the **LinkedIn page** — for your presence — and the task of the previous class, and today's task, and along with it a third task got included: **two names I found; two names you have to find and tell in the comments on the LinkedIn page.**

And note one thing: even if someone couldn't come to the live class, **anyone can answer by commenting on the LinkedIn page — even someone watching this video one year later, two years later.** They can send the information there. Definitely we will [acknowledge] — don't worry about that.

**Tomorrow there will be no session** — because I also need time [to prepare] — [next time] you'll enjoy it a lot. I've told you a lot already: we will do **a lab on that SUN/shadow [calculation]** — a very interesting lab — I'll tell you where I took it from, and it will be there for you to perform too; you'll really enjoy it.

Next class I will bring you some exercises; we'll do them — we'll try to do two exercises if possible. **After that we will start Twitter- and Instagram-related [OSINT]** — we'll start that in the coming sessions. So there will be one or two more classes on images, and after that, what we are going to deliver next — we'll continue after one more class, then Instagram, and so on.

[Session ends.]
