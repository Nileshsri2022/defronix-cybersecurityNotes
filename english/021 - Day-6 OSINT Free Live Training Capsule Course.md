# 021 — Day 6 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/021 - Day-6 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Social media OSINT · Twitter OSINT (non-technical/traditional method) · OPSEC for investigators · Note-making · Live demo on Paytm
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the captions are heavily garbled in places (`ओपन सोशल इंटेलिजेंस`/`ओपन 100 से इंटेलिजेंस` = "open-source intelligence", `ओसियन` = OSINT, `एग्रीकल्चर`/`आर्टिकल हैकर्स` = "ethical hackers", `त्रिकोण से मेथड` = "two kinds of methods", `फैंटास्टिक`/`फैन टेस्टिंग` = "pentesting", `विजिबल एनवायरनमेंट` = "virtual environment", `पीएम वेयर` = VMware, `बचपन बुक्स` = VirtualBox, `अनुमति`/`अनुमानाइज` = "anonymity/anonymised", `डाइजेस्ट कर सकता है` = "de-anonymise you", `काली निक` = Kali Linux, `वन नोट`/`दी ओ सी एस` = OneNote / Google Docs, `विजय शेखावत शर्मा` = **Vijay Shekhar Sharma** (Paytm founder), `सीटू`/`सीपीयू`/`सी पी ओ` = CTO/CFO/CPO (C-suite), `रेट वेट`/`रिट्स` = "retweet", `हनी पहुंचाना` = "cause harm", `डिप्रॉनिक्स` = Defronix). The intended technical term has been restored where unambiguous.

---

[Music] [Applause] Hello everyone, good evening friends. Everyone confirm once that you can hear me… So here we meet again — and I had expected more [people], because **today's topic is Social Media Open-Source Intelligence** — I'm about to start it, and as far as I know this is the most in-demand, everyone's favourite topic, in which we are going to study:

- **Twitter** OSINT
- **Facebook** OSINT
- **Instagram** OSINT
- **LinkedIn** OSINT
- and a bit extra on top

— quite well, in quite some detail. We'll keep it scenario-based, but everything we do will stay **within limits** [legal/ethical]. I thought since it's everyone's favourite topic, many people would come and attend.

## Why Twitter matters for OSINT

When the talk is of hacking — ethical hacking, or pentesting — the first thing that comes up is **open-source intelligence activities**. Every ethical hacker, when it comes to collecting information about any organisation, or gathering information about any target, about any famous person, does it **with the help of open-source intelligence**. Using **Twitter OSINT** he can gather a lot of information about his target.

Now, what do people do? People usually use Twitter to **share their thoughts, their interests, their emotions** — all of which helps a hacker. Just a minute, guys… okay, let's continue. So the target [audience] — I mean the hackers, the ethical hackers I was talking about — gather a lot of information with the help of Twitter, precisely because people use Twitter to share their views and their tastes.

So Twitter is a very good platform, especially for hackers — for **ethical** hackers — to perform all those activities: about any target company, any target, any individual — especially to **monitor their [public] activities**, and to [use] their outside information… to [eventually] exploit an organisation. If you have any target — the target could be a company, an organisation, or some very popular person — **if they have a Twitter account and are using it actively, and have been using it for a long time, then definitely you can find a significant amount of information about them there.**

Now you'll have one question in your mind: *"What about LinkedIn?"* Look — **LinkedIn is mostly used by professional people**, and people [there] interact through comments, likes and posts — understood? Let me say it in English/Hindi: it is used by professional people; people don't have each other's contacts, but they contact each other, chat, talk through it, or through comments — they share information with each other. [We will cover it separately.]

---

## The two methods of Twitter OSINT

What I'm going to teach you today — basically inside Twitter OSINT — some **advanced tricks** and some tactics that are used by ethical hackers to reveal information about your target.

Using Twitter you can do OSINT with **two kinds of methods**:

1. **Non-technical method** — we can also call it the **traditional method**.
2. **Technical method** — generally used by ethical hackers / hackers [tooling, covered next class].

### The traditional / non-technical method

What is the non-technical method? Any person who has been using Twitter for a long time, who has experience running Twitter, can do a **general information gathering**. Because actually, apart from an ethical hacker/pentester, nobody knows what [OSINT] is — [ordinary users] use Twitter just for their likes, comments, posts; they don't know how to perform the real things, no matter how much experience they have. Still, sometimes, using experience, they crack a little bit of information.

But when it comes to a hacker — an ethical hacker — **he uses the traditional method WITH A HACKING MINDSET.** When the traditional method is used with a hacking mindset, he uses some skills: **manipulation techniques, tricks, and the prior knowledge of his field**, and tries to collect information **that a normal person cannot collect**.

### Order matters

One very important thing: **without the traditional/non-technical method, you *can* use the technical method — but there will be no benefit** for any target or organisation. So I will start you first with [non-technical] information gathering; we'll finish it, and after that learn quite a few advanced techniques.

---

## Disclaimer / warning

Again, a disclaimer for you: whatever we use here — via technical method or non-technical method — the organisation I take as an example is **for educational purposes only**. Even if I am "targeting" an organisation here, it is only for educational purposes. **You will not use it [wrongly]** — do whatever [practice] you like, but **do not follow my target**. If you tried to do anything [illegal] — **we are not responsible; the Defronix company will not be responsible for you; you yourself will be responsible.** Everything we learn today is fully for educational purposes; nobody should try to misuse it, nobody should use it with any wrong activity in mind. This is a **throat-clearing warning** in advance — don't later say "sir, but you said so". You will be responsible for serious trouble.

(And by the way — the target I'm going to use today, **I have not performed anything on it beforehand**; I have not come to today's class with a pre-worked target.)

---

## Safety steps (OPSEC) before doing OSINT

Whenever you try to perform open-source intelligence — social media, image reverse search, anything — basically, as far as possible:

1. **Do not use a mobile phone or mobile applications.** Keep mobiles away, especially when you're planning this type of work — even more so if hacking-type activities are on your mind — because it can **de-anonymise/expose you**; it can reveal where you are sitting while doing these things. (By mistake you tap some application, and from there your anonymity is straight-away unprotected — you get exposed.)
2. **Use a VIRTUAL ENVIRONMENT** on your machine — inside your laptop/desktop PC. To create a virtual environment, if you don't already know, you can use **VMware or VirtualBox**, and in it use a **Linux operating system** — if you use **Kali Linux, it is even better**, because Kali is a very good OS [for this]. In Linux, when you use Firefox or Google Chrome, also use the **private tab** — that gives you anonymity to quite an extent (not fully!), but it's better than engaging directly.
3. **If you want to become the best OSINT investigator** and want to keep yourself somewhat hidden, my suggestion: **use a VPN** along with it. It will take a little more time to collect any information, but with a VPN you become anonymised — it will take anyone time to trace you.
4. **NOTE-MAKING — for every single thing.** Whether you use **OneNote**, **Google Docs**, or by hand — whatever pattern you have — you must make notes of every piece of information you get about your target. *Whatever you notice — note it.* You have many hacking scenarios, many attack techniques; you will use the information you wrote down when attacking your target — to exploit the **target's** device, system, or network.

### Why: information = attack surface

When you do information gathering: **the more information you have about a particular target, the more [options] you get** — whether it's security-awareness related [phishing angles] or a vulnerability on some target device — your chances of finding [a way in] increase, *if* you perform information gathering well. That's why it is very important to note things down.

And if you ever feel *"this isn't important, we can skip this information"* — **DON'T SKIP IT. Believe me: all information, every bit of it, is important.** Even if it doesn't look important today, after some time it will — because the more information you have, the bigger the hacking scenario you can create, and using that information you can perform exploitation properly on any target/organisation.

---

## Setup for today

Look, I am myself going to use a **virtual [machine]** for this work. And [again] — if you use Kali Linux, it's very much better. We are going to perform the **traditional / non-technical method** on Twitter OSINT — because as ethical hackers **we cannot risk missing any step** in the matter of information gathering. We are going to perform it absolutely live, on our target. Only after that will we go technical — because the more information you can collect in the non-technical phase, the easier the technical phase's deep recon of information becomes.

**First step:** your Twitter [account] — it's good if it's not a fake account 🙂 — **log in / sign in**. Why? Look: **without signing in you *can* do information gathering, but there are restrictions** — you won't be able to gather as much information as you can after signing in. Because after signing in you are inside that database — you can [query] that data; without signing in you can get some results on top of the database, but you can't perform fully. When it comes to performing fully, you have to go inside that system.

---

## Live demo — target: Paytm (educational purposes only)

So today's target — basically, **this is for education purposes only** — the company we are going to target is **Paytm**. I'm going to do it totally in front of you.

### Step 1 — The search bar

For example, you can see I am signed in. You see this **search bar**. Suppose we have just one keyword — we have no information — we have one word: **"Paytm"**. I search it… typing P-A-Y-T-M… and as we slow-scroll down, we get information: **Paytm… Paytm Care… Paytm [Money]…** Let me view [the main one].

Whenever you [find] a page — before anything — **confirm once that this is really Paytm's page**, its profile page. I'm not confirmed yet — but we can check, because the Paytm logo is on it and quite a lot matches…

### Step 2 — Google "About" first

One more thing, let me tell you: **if you are going to target any organisation/company, first Google it.** Go to Google once and search **"about Paytm"**. You will see — look at the social media [links] — because any website has an **About** [page/panel] with a lot of information; if it's a popular company they will have put its **contact number, its email, its social media handles/pages** there. **This is exactly the information we need at the start** — because to take any step forward we need a basic username, some anchor on whose basis we can move forward.

Now, look here — [on the About/knowledge panel] you'll see a **Twitter handle** — let me open it in a new tab (there's also Instagram and Facebook, but I'm talking about Twitter). Okay — now from this I will also get confirmation whether the thing we were trying to confirm is right or wrong. It's opening… **this is exactly it — Paytm, @Paytm — we found Paytm's official [Twitter] page.**

And if you look at the information here: *"Paytm — an Indian multinational financial technology [company] … Vijay Shekhar Sharma … founded [2010] … One97 Communications"* — okay, now we have **the founder's information: Vijay Shekhar Sharma** (the CEO is also him). Revenue — we don't care. Its areas: **India, Japan**… okay.

### Step 3 — Note down every handle

We have this information; profiles are visible here. So we do **note-making**: first, we have Paytm's handle — **@Paytm** — copy… (one minute, sorry for the disturbance)… we copy it — no, no, don't click! — and **note it down**. Any other information inside the profile? No — this much is visible from here for now. Fine — that's enough; let's start the analysis.

We have more to look at: **@PaytmCare** — there's quite a lot — **Paytm Money**… let's note them all down; there could be others. Next is **Paytm Money**, then **Paytm Payments Bank** (@PaytmBank), and there's a business one too — B-U-S-I-N-E-S-S — **Paytm Business**. So this much information I have already extracted about it; on this very basis we are going to proceed further.

> Everything I've gathered so far is important — none of it is useless.

### Step 4 — Walk every tab: People, Latest, Photos

Now look — we have these **People** [results], because a lot of information is visible: see what's coming out related to Paytm — and if you scroll down, you'll see a lot related to Paytm. [This is live] information gathering performed in front of you.

I looked at **Latest** — in Latest there's some information; searching in it will take a bit of time… Then in **People** we already found things. Now let me look at **Photos** — photos are visible — and you have to slow-scroll and *look*.

**Why is it necessary to go into every tab?** Whether you're finding out about an individual target or targeting a company, or even just carrying a keyword — keep this in mind: the chances here are that you'll see **employees' information**, or the company's **customers** — customer-related information gets revealed here — or **managers'** information may be leaking. All of that can be found here. Just now inside People we saw the handles — the official Paytm ones. That's why I say there are many chances of finding some **interesting information about your target company** here.

Now think once: if you successfully find information about an **employee or customer** of your target company — that's very important information for you. Because later, when you perform your exploitation steps, you need many **hacking scenarios**, many attacking scenarios; and when you use those scenarios during exploitation, you need a LOT of information there. It may be that with the information currently available you cannot exploit — then, to exploit further, you'll have to take whatever individual information you found — a customer's, an employee's, a manager's, the CEO's, the CTO's — and **target that individual separately**, keep performing on them. Every piece of information you gather in OSINT is important — that's exactly why I keep saying **note everything down**, so that in future, whenever you need to perform a hacking step, that information can be used.

### Step 5 — Inside @Paytm: posts, replies, retweets, likes

Now I have the official page handle. I put the **@** in front — because until now all the information coming was just "Paytm" [keyword results], not the account. Everyone knows what a **username** is — a unique name for every profile, every account. Now every piece of information you see here — in the posts, wherever you look — all of it belongs only to this **@Paytm**.

Let's find something interesting… inside Posts, inside Latest… okay, you can see [a campaign] — cricket [promotions] — after that, if you see any photo on the side, first go into **Photos** and check whether any information is being revealed. Like here: *"Paytm business settlement amount…"*

**Whenever you click on any image/tweet**, you'll see: **comments/replies**, **retweets**, and **likes**. You must open EACH of these and look: what's in the comments, what's in the retweets, what's in the likes. For example, I opened the retweets — look at the side, what's written — someone has replied something… there's a validity/promotion [query] — and look: **Paytm Care directly replied inside it.** So more information can be found here.

Keep one thing in mind — this type of information can show you: **employees' information** — employees of different departments who work inside the company. Maybe the technical department is sensible, is aware; but there are also **non-technical departments** — HR and such — whose information can be found here, of people working inside that company. And not only that: you can also see **what they are talking about** — if there's something going on that they're discussing, definitely someone from the company is talking — and from that too we can gather information — about employees, about everyone — **just by analysing**.

So I'll say one thing: **DON'T LEAVE ANYTHING ON THE TWITTER PAGE.** You must look at every like, every [reply] — and yes, you'll have to give it time, you'll have to analyse. Analysing everything, you have to gather the maximum information. If you rush, [you'll miss things]. It will take time — not hours; **it can take DAYS**. And when you give it that much time, you'll find some sensitive information that will be very helpful for you.

### Step 6 — Followers vs Following

Let's move on — let's go into People again: **Paytm Cyber Cell… Paytm Bank…** okay… one more — @Paytm… there could be [fake/related] accounts inside… *"namaste, namaste — for education purposes I use it — don't claim on me!"* 🙂 — and look what this says: *"Founder @Paytm … Mr … and CPO Paytm…"* — look at the information we're getting! If you read **every profile carefully**, you'll find something or other in each.

So that was: how much information you can gather just by visiting the company's official web page on Twitter. **In just a fraction of minutes — not even 1% of the information — when we could gather this much, think what a big scenario we can create on the basis of information gathering.**

One more thing: the **Following** [list] — look, following and followers information — **the FOLLOWING reveals a lot** for any company. Because if the company is following someone, it means that person may be quite **important** to the company — that's why it follows them. There you may find its friends, even its **partners** — that information too.

### Step 7 — Individual targets: the founder & the C-suite

So far we only visited the company's web page. Now let's target **individual persons**. First, note-making: we have — **Vijay Shekhar [Sharma]** — his handle… and look, inside [his profile] there's more: he has **mentioned his location** — India — and **when he joined: November 2008** — that information is also visible. Let me open [another] in a new tab: okay — **CEO of Paytm Money** — okay — **Mumbai, India** — he lives in Mumbai — **joined 2013**. We'll get a lot of information about him. And the **CPO's** information is also visible… okay, got that too. Next: "about Paytm system architecture…" [bio details].

We'll first target the popular person [the founder]. Look at his photos — lots of photos visible. You have to open each one and look. For example, I look at this photo — what is he doing here… he has posted some photo — there are six comments — one minute — the information… retweets… okay okay… *"I will not…"* — now some information is visible here — look — next: *"…your attention… where my money got strength and not a single [rupee]…"* — this seemed interesting to me — something could be here.

**Notice one thing about retweets and likes:** think — have you ever seen anyone like or retweet someone *without any reason*? Nobody likes/retweets without a reason. So whoever it is — **either a customer, or a partner, or a friend** — that's information. That's why I say: especially when you're doing OSINT via the non-technical method, all these things are very important — no doubt about it.

And for example — he himself is the CEO — look at his **Following**: he follows **856 people**. What type of information can be found here? You may find the **CTO of this company**, or the CTO/[executives] of other companies who are partners with them — you may find him following them, and their information too; or some normal employees, or customers — their information you'll see more in **Followers** (because *they* follow the company, since it's the company they use/work in). And there are also chances of **high-profile accounts** here — some CXO — and if [they interact often] it may be that they are **close friends** with each other.

Look here — visible on top — an "MD & CEO @…" — he follows her — **Radhika Gupta** [MD & CEO of an asset-management company] — so something is there; other CXOs' information is visible here too… *"loves running, cycling, swimming…"* [bio] — so it may be that they are close friends.

### The core capability: CORRELATION

If you want to become the best OSINT performer, then along with the tools you MUST use **common sense**; you MUST do analysis; and on the basis of analysis, your biggest capability should be: **how well you can CORRELATE things with each other — how you link them, how you join them together.** Your job is exactly this: joining these things together. Because as you read the chats, the tweets, the likes, the comments, the photo retweets — read every single thing — look, this is a fairly big company, and doing detailed research on its information **will take time — not one hour; it can even take your full month**, because [there are so many] things. But if you have given it time, then definitely, after some time, you will analyse and **link** all its information — and then you'll have such a scenario, so much information collected, that your attacking scenario becomes so big that **you'll run short of attacks** — you'll keep thinking about what to perform on whom. That's how big an attack [surface] you can build **with the help of open-source intelligence alone**. Doing it is your job — I will guide you in everything.

So, in this manner: in Followers you can find this information; building the attack scenario, linking pieces of information with each other — that is what you have to do when you are *really* going to attack a target, really going to gather information about one target. In that case you will have to do all these things yourself — because right now I've just done the non-technical [walkthrough] for one-two [profiles] — we've maybe covered 4% — and an hour has already passed. And you must **write all of it down in your notebook**.

### A few more clicks

From here let me open a tweet-related [link] — if I open it inside YouTube… if I open it in a new tab — you'll definitely find some information about it. It's not something that happens in a minute or in one day — not possible. Look — the **CFO of Paytm… "inside…" co-Paytm** — okay. Now let's look at his Following — whom does he follow — and one minute — in his followed people, is **Vijay [Shekhar Sharma]** there? okay… it's a big list; maybe he follows him, maybe not, I don't know… no — okay — **he doesn't follow him** — but "CEO of Paytm"… okay — next, next. Then you'll find things in Photos… if I look at **Media**… then **Replies** — how many people he replied to… "building… 4 hours ago… 3 hours ago…" — in this way we have to keep digging, keep building.

So like this, you'll have to look at **multiple profiles and cross-check them against each other.** A lot of information can be found here.

### The human weakness

Notice one thing: whoever we are targeting here is at quite a popular position — a designation-holder. **There is one weakness inside everyone: security awareness.** Many times, unknowingly, such tweets get posted — or some information that should not have been [shared] — no matter how much [training] is done, somewhere or other security awareness falls short, and by mistake such a tweet goes out because of which [the company] may have to pay. That's why I tell you: **while checking a profile, don't leave anything.** Don't leave anything — you must check every single thing.

---

## Wrap-up and Q&A

So this was your **traditional method** — how to correlate things with the traditional method. **Technical [method] — tomorrow.** Tomorrow you'll also have a live class — same time, same duration — because tomorrow we are studying the technical [tools]. But let me see how many people can [apply] and correlate the information.

Again I say: **these things are just for educational purposes only** — our intent is not to cause any kind of harm to anyone — to any employee, or even the CEO; finding an employee's information and doing [something] on its basis… Everything will be found, but it is a **time-consuming process** — you will have to give time. When you come into the OSINT field, you have to give time. If you gave good time on your first steps, then your next hacking scenarios you'll implement very well, because you'll have good [ground]: whom to target, when, how, which information — and if you link it all together, you get very good information.

So please tell me — did you enjoy today's class? Next class will be even more fun — quite interesting… Meanwhile, tell others… Okay, **5 minutes of doubt session** — if you have any doubts you can ask, then we'll end the session.

**[Q — Ritesh Kumar: on public information and companies]** Look — keep one thing in mind: in today's time, for a company, **business is the most important thing — making money in business** — and if for that they have to compromise a little with security, they do it — they make compromises. And tell me one thing — on Twitter and such social media platforms, however aware you are, some things somewhere get tweeted by mistake. It's even possible the [executive] doesn't handle the account himself — some other handler runs it — and that handler has no security awareness. **However much security awareness you keep, mistakes never stop happening.** And any one mistake can expose anyone. And — as long as mistakes exist, the cyber-security field will exist. **If there are no mistakes, we [cyber-security people] don't exist. And mistakes are bound to happen, because we are human beings.** 🙂

**[Q: "Sir, we'll study the technical part tomorrow, right?"]** Yes, absolutely — tomorrow we study the technical [method], and tomorrow the class is at the same time — there will definitely be a class.

And at the end I just want to say: if you liked our session, don't forget to **like and subscribe**, and please go to the LinkedIn page and comment, and comment here too — other people also get to learn a lot. And if you feel it wasn't good — **dislike it, no problem**; if you felt something was not useful for you, you can comment it out — we have no problem; we will give our 100% on it and try to improve.

So let's end today's session — bye-bye!

