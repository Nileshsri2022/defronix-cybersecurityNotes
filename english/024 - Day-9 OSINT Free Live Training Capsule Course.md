# 024 — Day 9 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/024 - Day-9 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Facebook OSINT intro · Traditional method on Meta (company) and Mark Zuckerberg (individual) · Profile/page extraction checklist · FB search tricks (`*`, related searches, AND/OR, media keywords) · Friends-list grabbing · Account-age estimation · Technical method: username vs user ID (`profile.php?id=`), page-source ID hunting, lookup tools · OSINT tool suite (lookup-id, intelx.io, OSINT Combine graph searcher, multi-keyword tools)
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** garbled-caption restorations — `मेटा`/`मैदा`/`मटर`/`माता`/`मिडा` = **Meta**, `मार्क्स अगरबत`/`मार्क्स अग्रवाल`/`मार्क जुकरबर्ग/जकरबर्ग/जगह` = **Mark Zuckerberg**, `ऑस्टेंट combined.com` = **OSINTCombine.com** (the graph-search tool), `इंटेल एक्स`/`इंटेक्स` = **IntelX (intelx.io)**, `आईडी लुक`/`lookup.com id.com` = **lookup-id.com** (FB numeric-ID finder), `यूजर वैनिटी` = the **"userVanity"** string searched inside page source, `यूपीएससी` = "view page source", `गूगल डॉग्स` = **Google Docs**, `परिंदेंस` = parentheses, `व्हाट्सएप परफॉर्म` fragments = misheard speech. Restorations applied where unambiguous; [square brackets] mark summaries.

---

[Music] Hello everyone, good evening friends. Tell me once — can you hear my voice or not? Confirm in the chat — yes or no. Thank you.

Welcome, all of you, once again to the YouTube channel. Today's topic is **Facebook OSINT** — our new topic. Let's continue; we'll wait for nobody — the ones who are on time, join now — because the one who is on time does every job on time; the one who is late is late in his life as well 🙂. Let's start.

We're going to study Facebook OSINT, because we have little time. Look:

> "Facebook OSINT — also the most popular social-media service, and it could help in gathering a decent amount of information about a target."

Everyone knows Facebook is a very popular social-media service — a platform, you could say — and it can help you quite a lot with information you can't find from other platforms. When you use Facebook for open-source intelligence, many times you find such information that you yourself get surprised — is this information real or right? You definitely get quite **accurate** information.

### Forgotten activities are gold

> "…forgotten and 'gotten' activities — like: posts that it liked, posts that it commented on, pictures it shared, likes, tags, places shared…"

What happens: when you target someone who has had a Facebook account for a long time — created years ago — one thing works in our favour. On Twitter we only tweet limited things; but Facebook is a complete social [network] where you **like, comment, try to connect with other human beings, talk to them about feelings, make friendships** — you do ALL of it through Facebook. So one thing is guaranteed: you yourself will have **forgotten** — after using a Facebook account for so many years — **which post you made when, which post you liked, which post you commented on, which picture you tagged whom in, which place** — you won't even remember the information you left lying on Facebook, because for years you've been using it. Nobody remembers their old Facebook [footprint].

> "Of course — there are a number of activities that they've completely forgotten about; for hackers, that information is very, very important."

Yes — many such activities exist that you've completely forgotten; for hackers, all that information is important.

Like the other platforms, here too there are **two methods** of OSINT: one **non-technical** — called the traditional method — and one **technical** — called the hackers' method. Twitter I made you analyse for three days; what could have been delivered in two classes, we delivered Twitter in three classes. Facebook we won't stretch — I've given Twitter that much time, so giving the same for Facebook is no use, because you'll get bored.

### Setup rules

First of all: whatever your Facebook account is — **you have to log in**. Why log in? If you are limited [logged out], that means you won't be able to get the maximum information.

One thing to always remember: on your **Linux machine**, always use the **desktop version** of Facebook — it's quite **flexible, fast, and less risky** than mobile. Because look — if your target is **too paranoid**, and by chance on mobile you tapped twice on something — two likes happen — and if the paranoid target [notices] you're stuck in such situations. Something wrong could happen.

Let's go to our machine. I'm logged in — don't try anything on this login; it's my own 🙂. Now — today's target: my method will be the **traditional method** first, then we'll go to the hackers' method. In the traditional method, the target I'm taking is a **second target — the Meta company**.

---

## Part 1 — Traditional method: Meta (company page)

So to target the Meta company — first step, as always: open the browser and search **"about"** for the company. "About Meta — a new company…" Something is visible here. In About you can see the Facebook page of the company, the company's website, the Twitter page as well. But let me do one thing — from this very page, what information do we get? Here I get the **founders** — who are the founders? I copy them [into the notes].

**A piece of advice:** whenever you make notes, the best is to use **Google Docs (D-O-C-S)** — whatever links you paste (Ctrl+V) **automatically become clickable links**; click on it and it goes straight to that Facebook page or Instagram page — from the link you pasted.

What do we have now? The founders — Mark Zuckerberg and others — we got the founders list from About. What else: **founded in February 2004, in Cambridge** — this information is given [copy it]. Okay — and [his] basic info — "Information about Andrew…" [a co-founder reference appears] — copy what shows.

Now to Facebook's own page: I go to Facebook, click the **search bar** on top, and search **"Meta"**. Papa 🙂 — look at the facilities: so many **options/filters** are visible. On mobile you'd get these options too, but with a lot of trouble; here in the desktop version you find juicy information and can collect much of it easily — Posts, Date-posted, "Posts you've seen" toggles, "if you want to see according to date — from 2004 — you can see that too", then **People**, because you know how general filtration/search is done (you've used Facebook for years) — **Photos**, **Videos** (also with date-posted), **Live**, and **Marketplace**.

I search Meta again and go to **Pages**: "Business Meta…", "Engineering at Meta…", "Meta for Media…", **Meta… Social Impact**, "Meta for Developers", "Education…" — quite a lot is visible. I click the [main] one: **"Internet company — helping build a future where people have more ways to play and connect"** — okay — **meta.com** — **4.2 million followers**. I open it.

This is the Meta company; I have to do information gathering about it. Going to the **Intro section** — whatever information is visible: internet company, meta.com — open it in a new tab; and the **photos** — click any photo: look, its **likes/comments** will all be visible. And look at the desktop-version advantage: you merely **hover** and partial info shows; if there are more, you click and all the information appears — everyone who liked or commented — this is the **thumbs-up** list, this is the **heart** list — **according to each emoji you can calculate the breakdown**; and see the comments too. Slowly download [note down] all this information. I'm not doing it all here — you have to do this yourself.

Then **About**: internet company; we got the **website**; [contact and basic information]; **Page Transparency** — "to help you understand the purpose of this page" — this is its **page ID** — **April 1, 2020** [creation]; **Admin information** — "they have permission to post content, comments… this page is running"; look: **"People who manage this page — primary countries: include India (15), more information — Germany (1), people, countries"** visible. Next: **Mentions** — go see. You already knew [the flow]: whatever you can collect from the company's web page — collect it all.

---

## Part 1b — Traditional method: Mark Zuckerberg (individual profile)

After that, we target the **individual profile**. Look — here's **Mark Zuckerberg's** profile — go to his page: latest post made July 18. Open his profile in a new tab. About him: he is the **founder**; there's also a **non-profit organisation — "building a just and healthy future for everyone"** — actually, if you look, this is **his wife's company** — the one which is his wife's — and it is *his* company too. Copy ALL the information — Ctrl… — then copy and keep all of it.

**About → more:** work/studied **computer science and technology**; his **location** — "lives in…" — and **"from"** where — and **married to…**; then education. Look — all this: you can copy everything (Ctrl+C) and keep it with you. Remove junk as needed; Google Docs makes collecting quite comfortable with links.

More About sections: **high school**; **places lived** — here they are; **contact and basic information** — in it, look: **born [May] 14, 1984**; **English language, Mandarin Chinese**; then **family and relationships** — you have to see! — then **details about Mark** — information about himself; **favourites** — what things he likes; **life events** — **15/12/…, 2019, started a job** — okay — this is what came. I [copy] it… What do you think — can quite a lot of information be found here? Definitely.

### Profile picture / cover photo — always check if clickable

One more thing to keep in mind: whenever you try to target any personal profile, **once check whether their profile picture is clickable or not**. If clickable, click it: look — you get so much information here — **2.8 million followers** [reactions] — the whole list of who liked and commented — and **when** he put this picture on Facebook — **October 18, 2022** — they've kept it on their page… look here — "please give me [a] blue-[tick]; I don't have…" [comment spam] — okay — quite a lot of information is here. It's your job: information gathering. Then going back: the side [cover] picture — open it too: June 28, 2018 — this picture — "celebrating with 2 billion people — the world is a little brighter" — 50,1… [reactions]. On the basis of the pictures you're gathering quite a lot of information.

Then **Friends/Followers**: these are his **followers** — those who follow him (a lot of information again), and **Photos/Videos/Reels**. Everything — I've told you — you have to gather; check every single thing.

### The in-profile search bar

One thing to know: inside a Facebook profile there is ALSO a **search filter** — this individual page's own **search bar**. If you remember any keyword — got to know about some keyword during recon — or want to find some friend in their list, or whether some follower exists — you can search that **here** — **only*this profile*** is searched. Example: I type "Facebook" — actually "meta" — Enter — whatever I searched, results are only from **inside this profile**.

### Watch the videos where the target speaks

One more thing to always keep in mind: watch ALL the videos — and **especially the videos where the target himself is speaking**. Because it may be that while sharing something with you [viewers], some **information leaks** from him — which proves helpful in information gathering.

### Reality check

Remember: whatever anyone teaches — in any lecture of one–two hours' duration, you cannot extract a lot of information about any single profile; if you haven't worked on a particular [target] for a month or fifteen days beforehand, in a small one–two-hour lecture you can't do information gathering on any target. **But we can tell you tricks, give tips, tell you the approach** — the rest of the gathering you'll have to do yourself. If I start looking at every single post in front of you, linking every single thing, then just for Facebook alone you'd be watching 15+ days of my OSINT demonstrations. Now that … if we continue 2–3 hours every day into live classes, we can't gather [in one go], because it's very difficult to fit everything into a live class. That's why I'm [compressing] things — and I've given Twitter this much time, so stretching Facebook equally is pointless — you'll get bored. So here too you understood what to do.

---

## Part 2 — Facebook search tricks

Go to Home… The tricks you used in Twitter's search bar — **here ALL of them don't work, but SOME do**:

### The star (`*`)
Example: I typed **"Mark"** and then a **`*`** — you know what star does — "anything after Mark" — `Mark *`. And again: if you want **family details** — you all know Mark Zuckerberg's surname — to find out **family members / relatives**, you'd place the star and then [[the surname]] — anything ahead, but at the end it must be [Zuckerberg]. Quite a lot of groups, photos, information appears.

### Related searches — never skip them
Whenever you perform **any** search here, **related [searches]** come — they're **quite helpful**. Because with the latest searches, someone or the other has searched these keywords. **Whatever related terms you see after any search — search through all of them** too. Many times it happens: through your own query you're trying to study information, but the way YOU searched doesn't find it — yet through the related search shown there, you find the information. On that very basis you get the information — in the same way.

### Media keywords
Now — only… I want: after the name, only **pictures** — `… pictures` — you'll get posts related only to pictures. If besides pictures you want **photos** — `… photos` — slightly different results — see, different results! — or **videos** — `… videos` — video-basis: the first name, last name, and then I gave any keyword — look — ALL videos only, because the username "Mark Zuckerberg" shows right here. So: **whatever possible keywords you can think of — search them ALL**.

### AND / OR logic — run it both ways
And the **AND and OR operators** work here too. How? When you perform **AND logic**, you have to use it **in both ways** — one, the **AND** written out, and the other way [short-form] too — because in the two ways, many times you find **different** results. Example: "Meta" — then I did [the Zuckerberg term] — Enter — it will find out all those posts or things in which **both** will be — Meta [and Zuckerberg]. See — all of them [match]. Second: instead of AND you can write it this way too — search — here the results are slightly different — look. And in [this case] the fifth one is not working… And with **OR**: either both, or any one of them — that works too, like this. For example, [combine with] his location as well — "on the basis of this particular location, what info comes". Instead of or, I can [compare]… All of this you'll have to try: **photos… videos… FB founder and CEO** — anything like this — this is how you'll gather all the information.

Friends can be found here; **family members can be found; close friends**; you all know how **tags** work: nobody tags someone for no reason — **you tag who's a friend, a close friend, a family member** — that's WHY you tag. Or you comment on someone — you don't directly comment for no reason — either you know them or there's interest. Likes, comments — you represent your emotions or views there. Same things — that's what you're here looking at. Using your **common sense with a hacker mind** you have to gather information — these things will be visible to you.

### Friends list — grab it entirely
You'll find his friends here too… anything shows there… one minute, let me delete… nothing else is showing… **anyway: NEVER forget the friends list.** Go over each friend — onto every single friend profile — highlight, copy it. You can directly select them ALL (Ctrl+A) — then Ctrl+C. In this way, always **grab the entire friends list** — never leave it.

### Estimate the account-creation date
One more: if you want to know **when the target account was created** — this Mark one — there are two places:

1. There's no tool that pulls the **exact** date. But going to **About → life events**: whenever someone registers on Facebook and [keeps] updating, they do it along these lines — so we can guess: for instance the first profile update here is **1998**-ish — meaning we can take an idea that around **1997–98** he created/updated this profile.
2. Second — **Marketplace:** if they ever launched/created a product on Marketplace — e.g. if Mark Zuckerberg created one — there, one information would be shown: **"when he joined Facebook."** Here too you get the joining date — a rough idea of the account-creation date.

That was one way you can target an individual profile.

I told the traditional method fast because you already know — you've got the idea what to do — it's in your hands now how you'll do information gathering. Mine is only to tell you which things to check. But one thing: **don't leave any single tab** — go on every tab, check everything.

---

## Part 3 — Technical method: username & user ID

Now let's talk about the **technical method**. Look: whenever you have a target, the two most important things you try to find out are:

1. their **username**, and
2. their **user ID** — because at many places, when you use tools, you have to put the **user ID** into the tool; on that basis you pull quite **accurate** information from a particular profile.

Now — the name you see ("Mark Zuckerberg") is the full name. To see the **username**, go to the **URL**: in the URL, their username is what appears (`facebook.com/<username>`). That's "their name on Facebook."

But many times you'll see the URL like: `https://www.facebook.com/` … then — **`profile.php`** (P-R-O-F-I-L-E dot P-H-P) — then — slash — `?` — **`id=`** — and some **random value**, like 1-2-3-4 — any such value. **That value IS the user ID.**

So: from a **user ID**, how do you find the **username**? You can do that too. And if you have the username, you can find the user ID:

**Method A — tool: lookup-id.com.** There's a tool — [writes on screen] — **`lookup-id.com`** — take a screenshot: `https://lookup-id.com` — I'll put the name in the chat, and provide the list. Paste the profile **URL**, press **Lookup** — it returns the [numeric] user ID. (Today, look, the tool is being moody — "I don't know why it's not working" — no issue, when tools fail, do it manually.)

**Method B — view page source.** Open the profile → **right-click → View Page Source** — lots of code opens → **Ctrl+F** → search **"userVanity"** (U-S-E-R-V-A-N-I-T-Y) — and you'll see the [identifiers]: the **user ID** shows right there, e.g. a number like `893399…`. Copy-control it; the same ID.

**Reading the signs:** if someone's profile opens as `profile.php?id=<number>` and no vanity name shows — it means **they haven't set a username**.

Now you know how to find anyone's user ID, and the username from it. Always do this when tools need it; if one tool doesn't work, another will — maybe one tool fails, the next will surely work with you.

---

## Part 4 — The Facebook OSINT tool suite

Now some tools — I'm providing you the list; take screenshots, otherwise I'll try my best to provide it in the group. These tools are all — **one by one**:

### 1) The graph-search builder (OSINT Combine — "Facebook tools")

The first tool's URL — this one… and a second — at **IntelX: `https://intelx.io`**… and then there's this tool where multiple tools live: **OSINTCombine.com — Facebook tools**. I'll explain them one by one.

Inside it you have **multiple tools**: you can find out the **ID (UID)** here too. Take the URL — which one was it — Mark Zuckerberg's — Ctrl+C — "Get ID" — paste, find — it'll try to find out in front of you. That's the same way I told you to check.

Then the **third option — Search**: quite an **advanced search** — the searches you *cannot* run inside Facebook's own search engine, you can do through this tool:

- **Search specific day:** I wrote keyword "Mark Zuckerberg" and put any random **date** — it searches Facebook… [the page says unavailable at first — reload trick: open the same URL again] — Ctrl+C, Ctrl+V — and it'll [load] — date — 23 June, 28 April, January, whatever — and **search**. On "Date posted" basis you can search — and although you can't select a particular date [in FB's own UI], **look: all the posts of the 2nd of January [whatever date set] — it showed them ALL.** This way information gathering happens.
- **Search specific month:** "Zuckerberg" + **February [20]23** → search → whatever posts existed in February '23, they're in front of you — look — *"mom… happy birthday to my favourite person, and me"* — quite important — "15 years since Harvard…" — such information will be visible.
- **Interval (from–to):** keyword "Mark" — **from when until when** — remember the same thing? — the **until/since** one — here we do it through the tool — all this information is visible.
- **Location-basis:** I have location — typed "Mark" — now **put the location's UID here**. How do you know the location's ID? From his profile: click the location — "From… Lives in **Palo Alto, California**" — I clicked it; when you click it you don't [immediately] see… do **View Page Source**; the **ID** there is the location ID — copy it, paste here, search — and now **with THIS location ID it searches and shows all your posts** — look — "post from Palo Alto, California" — [the posts tagged there]. That's how you do it.
- **Posts from [someone] about [something]:** mention the **UID** — e.g. Zuckerberg's (his is **4**) — and I only want to search "Meta" about that — it will show the posts accordingly.
- And **"Instagram post on date"** — give the Instagram URL and date-basis. So you can learn to use a tool like this.

### 2) IntelX (intelx.io)

Next tool: **IntelX** — it works **similarly**: search posts [by keyword], do it date-wise, **posts in a particular month** (select the month), **posts in an interval — from–to**, **posts from someone posting about something** (mention ID + keyword → search). One problem: every tool works in its own way — how results will show. For example: this will redirect to Facebook — **"Page not found" until you log in.** So you'll have to **log in** inside Facebook — because when it shows the result, it [opens] the prepared FB query. I logged in here… see: **its interface, its way of showing output is its own** — this is how it shows posts [grouped], people, etc. — its own style. [He accidentally opens it into his own profile — laughs — "grab my profile?!" — logs out.] So this is how IntelX works.

### 3) The "Graph-scanner"-style advanced builder (within the same suite)

There's one more — advanced, like a **graph scanner** — **post search**: **"posts from public"**… you have to **add** keywords — I wrote "Meta" — and added it; then **posts from a specific [entity/ID]** — e.g. I did **4** — add it — author added; **tag location** — if you have any — I added location too; then **filter date** — as you [build] — **"Open your [query] in a new window"** — it shows you much more. This is how it works.

### 4) The multi-tool tabbed filter (posts/people/photos/pages/places/videos/events)

This: the Facebook [tools] one with **options: posts, people, photos, pages, places, videos, events**. On "posts": add URL/keyword — I searched "Meta"; add **ID**; add **location**; then as target: **year 2020, month February** — add — and **open**. For everything I'd have to **log in** — once you're logged in [it'll run]; you should try these yourself — if I keep logging in again and again, I'll have to log out again and again. In this way the **filter** works. And **events** likewise — it'll show you.

### 5) The three-option tool (mutual friends · multi-keyword profiles/pages/groups · multi-keyword photos)

This one's interesting too — provides quite a lot. Three options:

1. **"Muchus/Mutual friends"** — you provide your target's **user ID** and if you have any friend-variety — any mutual friend you suspect "could be his friend", provide *their* ID — it finds out and gives you a list of **both friend lists** as a product. **But:** the first option **doesn't work with Facebook's latest update** — so this one currently doesn't work.
2. **Multiple keywords search — in profile, page, or group:** for example I select "person" — target "B.I.R.T.H. [birth-related?]" — "search relationship… with this I want to search" — and I search — and look: it opens in multiple steps — **login required for everything** — if you log in, it works (you may have a fake ID — anything — **you don't have to log in with your [real] one**, then it'll show you output). Instead of "person" you can select **page**; instead of page, **group**; and you can search **multiple keywords** together.
3. **Find photos using multiple keywords:** write the list of keywords and find photos with multiple [keywords] — again, **login required** inside your Facebook account — then it'll work.

So tell me: the tools whose names I told you and showed you on screen — did everyone understand how they actually work? Because **they work hand-in-hand with your search engine [Facebook's own]: you're not doing anything separately — they work WITH it**. Whenever you use these tools — a filter-use tool — after using the tool it **redirects onto your Facebook profile, with this ID**, whichever ID you were searching with.

And keep one more thing in mind: whenever — go to the **related searches** — you absolutely must gather information on the basis of related [terms] too; the related [links] you MUST explore.

---

## Part 5 — Doctrine, ethics, wrap-up

Look — one thing to keep in mind: whenever we do social-media OSINT, **we do it with a black-hat mindset** — because until we do OSINT with a black-hat mind, we won't be able to do information gathering. **But we are ethical hackers** — so we know what's legal and what's illegal — all [further] steps are to be done legally — nothing is to be performed without permission. But since you have permission to do [recon], whatever OSINT steps you perform, you perform them with the **black-hat mindset** while being an **ethical hacker** — trying to find these things out.

One more thing: whatever searches you're doing — **whatever possible keywords you get during information gathering — note them down**; whichever you think might [yield] — search them ALL. Maybe somewhere or the other you'll find that one piece which proves quite useful — because **always keep this in mind: even a small bit of information can help quite a lot in compromising big systems.** Your job: find that small bit of information — with it you can easily compromise even the biggest of systems.

Now — we wrap the session — Facebook OSINT is more or less half… not much is left actually. I've told you about the tools. And one more thing: I told you which tools — these tools also need **location ID, group ID, event ID** — how are those pulled? Like I told you the user ID one; for **location ID**: you know — right-click → open in new tab → the location shows… if it doesn't, **view page source**, Ctrl+C, Ctrl+Z… then search — particularly this one you'll definitely see — I search "things to do in…" — [the system hangs — laughs — "what happened yaar — close, close, my hands can do nothing now 🙂"]. Alright — tomorrow I'll tell you the rest.

If there's any doubt, you may ask. And again: **if you liked the session, please don't forget to like, subscribe, comment** — although you don't do it anyways 🙂. Sometime in life when you yourselves do such work — and you don't get likes/comments — you'll find out too: if WE never like/comment for anyone, what can we expect from others? Okay — five minutes for your doubts — anyone, any doubt related to today's session — you may ask. Anyone? Otherwise we end the session. No? **Your session will happen tomorrow too.** [Music]


