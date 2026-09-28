# 023 — Day 8 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/023 - Day-8 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Twitter tricks #10 (language-filter) & #11 (geocode:) · Combining operators · One Million Tweet Map · Reverse-image-search extension · Recon doctrine (focus, notes, linking) · LinkedIn OSINT (company page → employees → individual profiles) · Contact-out style plugins · Usernames from URLs
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are garbled in places (`ट्रिक नंबर नाइंटील` = "trick number nine", `प्लास्टिक बनाना` = nonsense garble for a recap phrase, `लेंथ`/`zn4` = **`lang:`** operator garbled, `मोमेंटम रेडियस` = "mention radius", `₹35`/35 — where the instructor audibly says `()` — is the captions mishearing his input while typing **parentheses** to combine queries, `1 मिलियन ट्विटर`/`वन मिलियन विथ डॉट मैप` = **One Million Tweet Map**, `आर डबल आई डबल एक्शन`/`ए 143 14 एक्सटेंशन` = a **reverse-image-search browser extension** (demoed but laggy), `कांटेक्ट आउट करके प्लगइन` = a **ContactOut-type email-revealer plugin**, `दी आई एफ आर ओ एफ`/`डिप्रैस` = the instructor's own company page **Defronix (cyber security)**, `काली होगा` in the sign-off = "will be tomorrow" (कल). Restored where unambiguous; [square brackets] mark summaries where captions collapse.

---

[Music] [Applause] Hello everyone, good evening friends. Confirm once — can everyone hear me? Okay, thank you. Welcome, all of you, once again to the YouTube channel.

So today we continue from where we left off — the tricks that remained — and after that we'll move to the next topic. Twitter, on the basis of its tricks, is quite long in itself. And now I understand your situation — continuously watching without doing practicals is a problem for you all… and you aren't doing [the practice either]. **If you want to target something, you can pick targets from Bugcrowd or HackerOne** — programs run there, so you can do all of this there: you can perform all the information gathering. I understand what you'll say — don't worry: once we finish our social-media topic — as soon as we finish Facebook, Insta — right after that we will **solve some labs** — quite interesting, **medium-level labs** (not easy ones). That will give you a slightly more realistic feel — "okay, THIS is how things happen" — because on those you don't do OSINT in this much detail, but you get an **idea**, a direction, of how to proceed and how to understand things.

Let's start. Someone who was present in the last session — tell me, what was the last trick we learned? Give the trick number or whatever it was, if anyone remembers. [Someone answers: trick number nine — the since/until date-range.] Right — trick 9 was about the **specific** [date-range]. So we continue from there.

---

## Trick #10 — `lang:` — language-specific search

Trick number ten: the **language** trick. We use it as the `lang:` operator, and along with it we mention the **language** — for example for English, or for Chinese — here we mention **in which language**.

First, the example: why would you use it? For example, most targets are found successful speaking **English** — it's the common language; it's not that easy to do information gathering in [every] language. But if you have an idea **which language your target can speak** — how do you get that idea? By **reading their posts, their tweets**. It can be that your target knows **multiple languages** — Hindi, Urdu, French, Chinese, whatever — Japanese — any language. There are chances, because any operating company doesn't exist in only ONE place; it works in **multiple countries**. It straightforwardly follows: they have **clients and employees from multiple countries**. If it's a big multi-corporate company with foreign clients, then for talking to those foreign clients — fine, English is common — but it may be that your target knows multiple languages; to tweet or talk with foreign clients they'll prefer that language. Maybe they're not a master of that language, but they have some idea of it.

So — through their tweets you can figure out that besides English your target, for example, knows **Chinese** too. Then you can use the **language-specific** trick to check: has any tweet happened **in that language**? You can jump to that particular tweet. With this you **confirm** that your target — or the target company — **has foreign clients too**. Second, if your target is conversing in another language, it simply means **their friends are foreigners too** — right, they have foreigner friends — and on that basis you do information gathering: maybe there are certain tweets between them because they're good friends — and then: maybe your target can't be compromised, **but the foreigner friend might be** — so you try to compromise *them* with social engineering, try a bit more information gathering, and it may be that they provide you with much more information about your target.

**How to use it:** Look — this is my [Twitter]; now I want to find out… in the search bar I put the target's name — you all know my target's name — the example I took [the Paytm handle] — Ctrl+V — and how do I know the language codes? [On a reference site] — those are the **ISO codes**, mentioned language-wise — e.g. **EN** for English, this one for Chinese — and for example let's use **Bengali — `bn`**, the Bengali one. [Types] …so if your target can speak Chinese because they replied in Chinese or there are posts in the Chinese language — okay, "can they speak it or not — but look, the Chinese [partner] has received replies" — meaning [their posts] were used — here's the reply… So they found out: the Chinese partner has also tweeted at them — that's why this mention is showing to you. But [we can't say] "they speak it" — still, **on this basis we can filter out**.

That is the **language-specific trick**. Today we'll move a bit fast because a lot is left. With English, Chinese — whatever language — you can check things. And if they're Indian, we can use **Hindi** too — for Hindi we [set `lang:hi`] — let's use it once: "talk is happening in Hindi too" — look here — something visible here — someone referred to them or complained [in Hindi] — something or the other will show up for you here.

---

## Trick #11 — `geocode:` — latitude, longitude, radius

Trick number 11 — what do you do?

1. Write **`geocode:`** here.
2. Then write the **latitude** — L-A-T-I-T-U-D-E.
3. Next to it write the **longitude** — L-O-N-G-I-T-U-D-E.
4. Then mention the **radius** — 5 kilometre, 10 kilometre, whatever — I wrote **5km**, like that.

What is latitude? North–south — geographical coordinates: your latitude is called the **north–south** coordinate; longitude [the other axis]. If you got an **address** during information gathering, from the address you can find out the **coordinates** — where your target could be, in that area. You go to **Google Maps**, copy the latitude-longitude from there — Delhi, Delhi… I'm getting an area-specific [match]; I'm getting an idea like "your target could be around here" — somewhere… You have to scroll… whatever you see — I **right-click** here and take its longitude [and latitude pop up].

Now what do I want? I want to see **all the tweets from this area**. So here I make a sort of **circle** — *take music, enjoy* 🙂 — this lady… within the **5-kilometre area** of this, whichever tweets happened, on their basis I take… I want to find out ALL of them. First I have [the area] by name — area-wise I'm making a **perimeter**… perimeter — quite an interesting thing it is.

How can I do it? For example, if I have no target-info at all, we can take an address… And let me also tell you one more thing: if you have a **PIN code** — on the basis of the PIN code, if you want to find out longitude-latitude, how do you do that? There's a website — which one? **geocode.xyz** — G-E-O-C-O-D-E dot X-Y-Z. Okay — that one. We can take any PIN code here… By the way, look whose coordinates it is showing — one minute — any PIN code — can someone tell me one in the chat, so I can show you in front of you how it works? Anyone — one PIN code? [Music]

Alright, let's do one thing — without [waiting]: we do `geocode:` — first latitude, longitude — **Ctrl+V** — I wrote latitude and longitude here; on that basis, then **comma**, and I want only **30 kilometre** — I did 30… "let's do one thing — what's our best option — Google…" — here we have no prior intel because I don't have that much time to search things out separately — so here: **keyword → then geocode → then latitude and longitude → then you mention the radius**. Combined with the keyword, what can it do? If you have a slight **idea about your target's location**, now on the basis of tweets you can **narrow down** — you can make a circle: "in THIS area your target could be; from this very area your tweets came out" — that's how you can do it.

Let me — one minute — that website of ours… `Paytm geocode:` then next, Ctrl+V… In this way you can narrow down your output even further. Okay — so this was **trick number 11**.

Trick 12 — let's go… [checks notes] — no no, that trick isn't ours — okay, no more tricks — done, done, done — **that's all; Twitter's trick list is complete** 🙂.

### Recap of 10 & 11

You all understood: tricks 1…2…3…4…5…7…8 up to nine I had told you already. In 10 I've told you: with the **language-specific** filter you can find out particular posts. And 11 you can use quite well: if you know the **exact keyword** — you know from information-gathering that "this keyword was used" — because either some event was running or some hot issue — and you have an idea of the location, that "your target lives around this location and tweets happened from this location" — then with a **perimeter** you can take latitude-longitude from **Google Maps**, zoom, take out the coordinates, define your radius — and yes, that website was there which brings [coordinates] out nicely too. Then you define the parameter. Start the range with **100km**, keep a lot, then **50**, then do **30** — you'll see: if nothing is coming in 30 but it's coming in 50, it means "in the 50-kilometre area it is" — every time you're reaching **closer to the target**. And then you can define target-spacing: "yes — THIS is the area; from inside this very area the activity happened — like your target does it — or it's his customers, employees, partners" — because somewhere or the other they ARE mobile 🙂 — so in a way you can do **tracking-type** work from here. That was your 11th trick you should know for Twitter.

---

## Combining tricks — parentheses for compound queries

Now let me tell you one thing: you can **combine** these tricks with each other. How? The simple way: you've done a decent amount of information gathering; now you're **verifying your results**, or trying to find **accurate results** — in that, you want to use multiple tricks together. How? Put the tricks **inside parentheses** — define each trick inside a bracket-group and they combine. 

[Demo] I put the target's name — look, this name — I copied it… first I use it single, and yes, the single one works. With `()` — many times it happens that you're trying to find things about your target and the information gathering just doesn't happen; some information doesn't come in front of you. But now, with the brackets, you use [the compound query] and maybe you see **more results**. Then you keep combining more tricks with it: space, then [the next group] — I gave the keyword **Paytm** — only "Paytm" — then to find posts: **`since:`** — from when? — **`until:`** — which end date? — for example **July 12, 2019** — "accurate result: wherever Paytm was used on July 12, 2019, all those posts will come before you." Look here — *"this is my Paytm June-month statement; check the ₹164 charged to me"* — see, he'd Paytm'd it… All such things you get to see. **In this way you can use multiple tricks together.**

Let me write it in the notes so it gets clearer — one minute… Like this: if you want to use multiple [operators] together at once, you use them like this — the example shows 1, 2, 3 [grouped clauses] — we can even add **geocode** inside it if we want — how? [groups] — on that basis you find out your result. What did I ask it to do? "Whatever I told you to do — make a **combined result** of all of it and show it on my screen, on my output, or print it for me." So it first searches each [clause], and the combined result gets shown to you — **that's why you see more accurate [output]**.

**That was Twitter** — Twitter OSINT. So tell me once: did everyone understand or not? Whatever Twitter OSINT I've made you do till now — does anyone have any doubt, or feel like something went over their head, or they didn't understand? Please tell me.

---

## Tool: One Million Tweet Map

Two-three more tools now — you'll have to **practice** these. The first: **One Million Tweet Map**. It's an application where whatever tweets were made in the **last 24 hours** from whichever locations — it **represents them to you on a map, with counting, with the exact location** ("which lane, where"). 

**Conditions:** 
1. It is **time-specific** — last 24 hours' [tweets]. 
2. You'll get **only those** whose **location access was given to Twitter** — those who have location access enabled along with their tweets. Basically: users by mistake, or earlier, gave Twitter permission — "you may access my tweets" / "my Twitter application may access location" — because your Twitter is connected with maps, with Google Maps, so it can access location.

If your target has **not** given such permission… if he hasn't posted with location — then on the basis of posts you can do **accurate analysis** only for the ones that do. Here you can give a **keyword**, a **hashtag**, and a **username** too. For example I do `@Paytm` — whichever tweets happened, it shows them… look: here's **Ludhiana**, it shows… — but it was **updating in real time**; and it shows [even those] — not only last-24-hours posts — it shows **any** post whenever it captured it with location. **Now, there is no guarantee** that [the target] is available here or not — because your target may not have given it access. If the last-24-hours and the location [permission]… it will show **any random tweet** sitting there that was tweeted with location access.

And if, without location access or in the last 24 hours, your target tweeted nothing — or if your target is **security-aware**, he knows "I must not provide location access to Twitter" — then you cannot identify him through this app. Now two tweets are visible — [someone] got banned by Paytm, so it's showing the tweet… This is one quite–till-now [handy] app. **But:** like many apps I've read about, some don't work at all. If you adopt the **manual** method you get time but you do **good analysis**; if you chase speed you may also get **false positives** — some apps simply don't work.

## Tool: reverse-image-search extension

Then — a slight timing difference — but here's an **extension** you can use. Which one? One minute… what you have to do is — search here — this one — it appears with an "R-I"-type [name] — a reverse [image search] extension; turn it **on**, and **allow "Run in private windows"** — you have to allow running in private windows. Alright — this is doing its work. Now let's go to our tweets — whichever tweets there are; my target is what we targeted… you'll use the extension; whenever you **click on any post**, automatically an **icon** is visible to you — of **"reverse"** — you click there — one minute — it's working, it's working — as you click on reverse, it creates and shows you a sort of **image** [search result page]… it's hanging a lot, loading — try using it yourselves; if it doesn't run, tell me. Now Twitter is also working slow for me.

So that was — two things for Twitter: one app, one extension — I told you. Now let's go back to our screen… You'll manage these two, right? Try these two yourselves once; all of you tell me in the group — "working / not working".

---

## Methodology talk: focus, notes, linking — don't get disappointed

Now — whatever we've learned so far in Twitter, let me remind you of it in summary.

> *"We have learnt good tricks in order to reveal and gather information about our target on Twitter."*

These tricks will help you quite a lot in information gathering. **When it comes to hacking, we need to FOCUS** — when you perform ethical-hacking activities, your whole work becomes "boxing in": you must **focus on one particular thing**. First make your focus strong; on that basis you can analyse more things, read about more things, gather more information. And **don't get disappointed** — if something isn't turning up, if you can't link things — don't get disappointed: **just try, and keep doing it**. Maybe that thing won't make sense in one day — you're a beginner — maybe in **10 days** it will **automatically** click. You'll keep thinking about it, and when you're not even trying to imagine it, after 10–15 days, while you keep focusing on the same thing, *automatically* "this could be it, that could be it" — an **image starts forming**, the **links form on their own**.

Everyone knows: **the first stage of any hacking is information gathering** — that's why it's given the most time. If you don't give time here, the next stages get quite frustrated — because the more information gathering you have about your target — his friends, any account, whatever — the more, in quantity, the better you can focus and work.

**"Don't believe anything"** — you must not directly believe any single thing, any fact — no blind faith. **"You have to note whatever you find, and try to link [them] together, and every day just read [the notes]"** — read quickly **before you start** the next steps. By doing this you can easily guess what your next steps will be.

Meaning: today you did 2 hours of information gathering on someone — note down **every single thing, relevant or irrelevant**, write it. Then [after] you spent [time] on the internet — understand the things: how was this collected, and try to link them. Suppose in 2 hours you pulled just **1–2%** of the information. The next time you sit down to gather, before the steps: **first go through all those notes once** — the relevant and the irrelevant information — see what you currently have; **then** take the next step. Because when the things you noted go through your head once, it stays in your mind: *"I already know this."* Then whenever you take the next step — dig into detail, or start again from somewhere — you already have some information, so you **try to link everything**. To link, you must have information — otherwise you can't link. And you'll have it only if you go through it once.

And even when your information-gathering stage is complete — you gathered for a **month** on some target company, and you have maybe **10–15 pages** of information — out of those pages, maybe **2–3 pages** of it is information you can link with each other. Even then — suppose you move to the next stages: scanning, enumeration, vulnerability analysis — **before going anywhere, every single time, go through ALL the previous steps once** — half an hour, 15 minutes. When that information is with you, remembered, then in the next stage you'll **build attacks easily** — you'll think of more things. Sitting to try something, you'll say: *"yaar, there was one thing I couldn't link — can I use that information here?"* — and maybe that unlinked information **just works** here — the linked information to explore that thing, and the **unlinked information to exploit it**. 

That was the information-gathering stage — through Twitter, this was my little [gift] for you about Twitter… It'll take 15 minutes — let's do it — actually let's not finish Twitter today, because it's been **three days**; you all got bored too 🙂.

---

## LinkedIn OSINT — start

So next up: open-source intelligence through **LinkedIn**. Everyone knows who uses LinkedIn — and we ourselves make you use LinkedIn too 🙂. So today, for LinkedIn, we'll **change our target** a bit.

You all know: **LinkedIn is also the most popular platform for [business] intelligence** — because **business professionals** use it. On Twitter some things you just can't collect; you can't build the links — and Twitter alone isn't the one on whose basis you can analyse and verify ALL the information. To verify information, the **whole of social media** comes into play — you can't verify everything on the basis of Twitter alone — so through LinkedIn [too] you have information, and here you can **link** those things as well.

### The company page

Whenever you do LinkedIn intelligence — its posts, where on the [page] — because on LinkedIn's [company] page you find **quite detailed information** about the target. Example — live: this is my LinkedIn… now I open [the company page] — here you can post posts, and here you can search. For example I'm typing **Defronix** [the instructor's own company] — subscribe — here you can see: **245 followers** — **View Page** — meaning I want to open Defronix's web page on LinkedIn. I opened the LinkedIn web page of Defronix Cyber Security.

Now here — quite a lot of information — read it: **"India's leading cyber-security technology training certification"** — okay. It has 245 followers. Just watch how much information shows up here — till now, even for the Paytm company (if I take that example), we didn't have this kind of information. I open more — in **More** I can [see details] — you can send requests/messages — then **Home** — look, what's written on the home page — Mumbai — look at the details: okay — this is their **website** — let's open the website… **industry: education** — normally it shouldn't be [exposed], but it's given here. Then **Posts** — from posts you'll get ideas of what's going on: here they're running a **training**; after "first"… and look at the **likes and comments** — you'll get ideas from here: *who* likes? Right now, the training's **students** will be there — and it's quite definite: among the students, someone from the company — a support-team member, some team, some **trainer** — will be **replying** there. Why will he reply? Because to build interaction — he's liking too — so from there you have [intel]: *"this could be an employee of theirs, or a receptionist, or anyone."* Now read all the posts: "nice — this could be another course they delivered"; there's SO much information here.

Now the **Jobs** tab — when does a company offer a job? Right now they're not offering any job. After that, go to **People** — here you can see the **employees' details** — **22 employees** here — who-who are the employees? Look how nicely it's given: 23 [in] **India** — Maharashtra, Haryana, Greater Delhi Area — this is quite good information — "where do they live" — okay, India — Maharashtra — Haryana — Greater Delhi area. [This may be] information given by them; and totally correct information at that. Look — this one — [each profile] — you can go view every page: which employee, what location they've given.

### Individual profiles — what to extract

Let's take one example — I look at **Ritesh Singh**: here you can see — **"Defronix Cyber Security — founder; co-founder, Matrix Solution; [content] creator — Technical… [YouTube]"** — okay. So what did we do? We opened the **company's profile**; now here we can open the **individual's profile** too — because on LinkedIn that's exactly how information is found. He gave about himself: founder — "founder, Defronix Cyber Security; co-founder, Matrix Solutions; creator, Technical… [a YouTube name]" — these are his qualifications.

Look — about the company we got the **About** info; we got their **website** — on the website too we can see what info there is. And he is the founder — meaning **CEO** — we have that information. He has mentioned his **location** here: **"I belong to Patna, Bihar"** — alright — he even **exposed his location**. Then **Contact Info** — look what he has given in contact info: LinkedIn profile given, **website, blog website** — okay — **YouTube** and others; then **address: Patna** given — and he has even given his **email address** here — and he's given his **birthday** here too.

### The URL lesson: display name vs username

Now one thing — on LinkedIn, look what's coming here: his name shows as, e.g., *"Nitesh Singh (Technical …)"* — what do you think: **is this the username of this profile?** Yes or no? Tell me — could it be the username? [No.] What happens: some users give a different name here while the profile runs under this name — always pay attention HERE — look at **`linkedin.com/in/…`** — whatever you see after this — that is the **username** — actually, **THIS is this profile's username**. For anyone — Facebook, Twitter, Instagram — **everyone's username you get right here, in the URL** — whichever actual username is being used for this ID.

So on LinkedIn, what-all information can you see? If it's a company's [page] — you can see **its employees' details**, **what projects are running**, **what type** of company it is (from projects — because the company will be sharing something or other), its **contact information**. Once you have the company's data — after you get employees' details from the company page — what do you do further? Since you're not getting [more] info about the company itself, you go to **People** — among the people, the employees — you get **maximum employees, present employees, and past employees** too. Then you check each employee — except the big/tough ones: if someone looks **tough** — **don't touch it** — maybe he's a **threat hunter** or very much a cyber-security professional — if it seems so from his profile — **skip him for some time**, but **keep him in the target list**. Besides that: the **normal IDs — HR department, [other] departments** — those employees you'll find are **easy targets** for you — they can give you more information, because they don't have as much security knowledge as the technical guy. Then you'll check those employees' profiles **one by one** — 22 employees — you can check all 22.

On any single profile, what-all can you check?

- **Username** — is this actually the real username? It could be real or fake for this profile.
- **Cross-platform pivot:** by **Googling the username** you can find out whether other social-media platforms/handles exist for this name. Example: I opened it, copied it, pasted it [into search] — I see a **website**, I see **YouTube**, I see **Instagram on the same**, LinkedIn itself, **Facebook also on this**, and — look — even **Telegram by this same name**. If I don't find "Nitesh…" then maybe I use [the other form] — less info comes with it, but you searched with the technical username because it's popular — the IDs are built on this very basis.
- **Contact tab:** their **own website**, **address, email**, **birthday** — birthday helps quite a lot too.
- **Posts:** they'll have posted **some** posts that can be of use to you.
- **Emails:** besides the business email, normal email — here he put his own email; after that the business email can be found, **mobile number** too — someday [it may show].

And further down on the individual profile: **posts and comments**, **experience** — "solution[s]… content creator, Technical…, YouTube channel" — his experience; then **education** — studied at **Rajasthan Technical University**, **BTech, Computer Science Engineering** — then **10+2 (Science, Maths)** — from where he did it, which [school] — when: 2011–2012 … in **2016** he did his graduation; then 10th standard — SO much information, given by himself. Then **licenses/certifications** — on these bases you can do [much]: email-OSINT [next], username-OSINT, possible [pivots]. **The biggest attack is this very one: social engineering** — you'll do social engineering on these bases. All the more: that information you didn't get on Twitter, the profile-links you couldn't build — here you GET the profile links — and he can be used on Twitter too. 

So do this: **first LinkedIn-OSINT, then Twitter-OSINT**; LinkedIn's information came out better — **compare** it with [Twitter's] information — then your information-gathering **skill gets stronger**, your links are better. In this way you can extract maximum information about any target — and that's how you link things.

And like I said: social-media OSINT can dig out **anything** — his likes, dislikes, feelings, what he likes, what he doesn't like, what's his favourite, what isn't favourite — his **mobile number**, his **emails**, his **Gmail, business email**, and **how he looks** — ALL that information you can extract with social-media OSINT. After that you have options: you have to **prepare the attack surface** — how many types of attack you can do; then you'll think of **social engineering** — you'll think of **phishing** somewhere — because for phishing you'll need the **email**. So all these things you can extract from LinkedIn in this much time. This was just me pulling one person's information as an example.

### "People also viewed" — the side panel is a friend radar

Let me go back… Alright, for your [understanding]: take this profile — this is a security [professional] — now about him, more — from **Contact Info** — the technical/technology officer — from here you take it. After you have his email — personal email — and mobile number, you proceed on that basis. You can check his **connections** — quite a lot of information you can see about him too. That is how information gathering is carried out.

One more thing I tell you: whenever you do this work — whenever you open any single profile, like I opened **Hardik** [Asliwal?]'s profile — sorry for that if I'm pronouncing it wrong — I opened his profile — **notice one thing:** in the side panel — this one — **"People also viewed"** — whatever it **suggests** to you there — it suggests those who'd be **his followers**, or **his friends**, or those who follow them — so from this too you get ideas: *"the ones appearing here are not [appearing] for no reason"* — they're not yours — the profile lying open in front of you — **their followers are here, their friend-circle people are visible here**. Look — all of these you'll find related to him — the ones in his contact list. Then further: if Hardik-ji is our [target] and he isn't getting compromised for any reason — don't worry — **a slightly weak one will be found in this list** — you see from here, match it and see: "okay — is he in his following list? Does he work for this company or not? Okay — meaning friend — could be a close friend — so he's not revealing information [about himself]" — you'll make **him** your target; from this target you'll **skip to a second target**, and then you reach the **company**. In this way the information-gathering steps get performed.

That was your **LinkedIn OSINT**. There's nothing much to LinkedIn — just this — but LinkedIn helps you **a lot** in information gathering, because whatever LinkedIn has — it's ALL **strong information**.

### Quick Paytm LinkedIn sweep

Honestly — all of it — strong information must be seen. If I show you on Chrome — in Chrome, LinkedIn — look here: **Junior Manager — NOC team; Software Engineer at Paytm** — it gives you SO much information: what was not even found over there [on Twitter] — "Software Engineer, Paytm — Delhi, India; Chandigarh, India; Punjab, India" — he opened up **everything** for you: "brother, I live here, I live here" — everything in front of you: **Senior Quality Assurance Engineer at Paytm; Junior Manager at Paytm — Uttar Pradesh, India**. I open this one — "you can… [limited] visibility" — okay — because I'm not a member [signed-in]. Then let's see the junior manager — **Junior Manager, Marketing Design, Paytm** — quite rich — Paytm experience: in [the world?] he's a **team lead**; there's **graphic design**; here's his **education**; where he studied from; and he's mentioned his **skills** here. You get information… He showed it all in front of you.

### Plugins: what the platform hides, extensions expose

But one thing — look — I have some **plugins** — some plugins — that I'll teach you to use: for LinkedIn there are **two-three plugins** which work quite well: there's some information which Rahul-ji here is **not showing** us — but some plugins **expose** that too. In the next topics — we'll do **email OSINT** — sorry — email open-source intelligence — and a bit more general OSINT — in that I'll tell you those plugins. If you want you can add the extensions [now]… actually leave it for now — **it's not the right time, because you'll have to register for every plugin**. Otherwise — you know what — I'll just give you the list… Alright — I'll make you [set up] all the plugins later, told together. There's the thing — **you have to register for all of the plugins** — three-five — they work specially with [proper] plugins; they give information. If I show you a demo of Rahul-ji — this is to expose him — this one — it's a **ContactOut**-type plugin. If you look: look — **no information is visible here** — watch — now I do **"View email"** — look — **two emails got exposed**: `rahul…saxena@paytm.com` and this one — `saxena.rahul3011@gmail…` — **both**. Mobile number — am I seeing? Okay — mobile number, no, we don't [have it] — but look — **two email addresses you got right here** — it showed you, while **here it was not visible to you at all**. Now further — on the basis of these too we can do information gathering, if possible. All these things you can find out like this.

And there's more here — like this one — this is also a plugin — some information is visible here — let's see — there's no info — **"Get post / Get prospect"** — junior manager [profile] — after this there's no info… then it gives info — maybe: **"Delhi, India — Junior [Manager], Paytm — 8 years experience"** — okay — it mentioned experience. And what else do we get to see — the profile… After the experience, you know…

### Wrap-up

For the next class: I'll try — first the **Facebook demo**, and after that we go a bit further in information gathering, try to perform more steps — **email OSINT** happened, then a bit of **phone OSINT** will happen — then we do — don't worry… When your [count] goes above ten — in 5 minutes you may ask me your doubts — anyone, any doubt you have, you may ask me. Any doubt — anyone? If not, please tell "no" — yes or no? Alright — no answers from anyone — let's end. Okay — bye-bye, take care. **One more thing: your next session will be tomorrow.**



