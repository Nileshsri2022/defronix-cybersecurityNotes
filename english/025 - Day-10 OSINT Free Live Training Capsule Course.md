# 025 — Day 10 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/025 - Day-10 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Finding group/page/event IDs · Manual URL manipulation of Facebook search (categories, `?q=`, base64 JSON filters) · Combining filters (JSON merge rules) · Private accounts → friend-pivot social engineering · Multi-account detection via Messenger · Tool barrage: Profil3r (GitHub CLI), reverse-image sites, whatsmyname.app, namecheckup.com, FBI (Facebook Information) CLI · Laptop-buying Q&A
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** heavy garbling around the tooling — `यूपीएससी`/`व्यू पे सॉल्व` = "view page source", `जशन फॉर्मेट`/`जेसन` = **JSON format**, `बेस 64` = **base64**, `करी`/`कितेंद्र` = "query", `मिस्टर नोज…प्रोफाइल`/`प्रोफाइल वाइफ` = the GitHub CLI profiler (consistent with **Profil3r** — a name-based social/email enumeration tool), `व्हाट मैं नेम्स डॉट अप` = **whatsmyname.app**, `नाम checkup.com` = **namecheckup.com**, `एफबीआई` = the **FBI (Facebook Information)** Python tool, `डिस्कवर/डिस्काउंट/डिस्कार्ड` = Messenger's **Discover** section, `मेनू प्लेलिस्ट` = "URL manipulation". Best-effort restorations; [brackets] mark summaries.

---

[Music] Hello everyone, good evening friends. Once again tell me — can you hear my voice or not? Give the voice [confirm] — then we start from where we left the topic in the last class. Okay, thank you — [welcome] to the academy's YouTube channel. Tell me once — what did we do in the last class? Where did we hold the last class? Anyone remember? …[answers] Really? …Yes, really — **Facebook OSINT got completed**… 

I had said it, Kumar Ojha-ji: we will solve labs — quite medium-level ones — in which everything gets used: image-reverse, Google Dorking — everything will be involved in it. Don't worry about it — it's in my plan already. But right now your decision [poll] will come in the group — it will decide the future of this OSINT course for you. Actually, if it were up to me, I wouldn't want to finish OSINT so quickly — because a lot remains for you in OSINT, and quite interesting things remain that you should know. So it depends on you all — in what way you want it, in what way you want information, what kind of course you want. Because even if you go somewhere else to do such a course, this much detail you won't get… You could say thank you to me — I saved your ₹1000 [and more] 🙂 — if you did only OSINT [as a course] on some platform…

So — last topic, remember where I told you? I remember: **today's class is FULL of tools** — packed with tools. And whichever tools are shown in this class — a text file of them will be made and shared in your Telegram group, soon after the class ends. Let's start.

You know what Facebook OSINT is, and both technical/non-technical were running; we've entered the technical part. So sir-sir — we'll do practical. My last target was **Mark Zuckerberg** — because for gathering information about the Meta company, the technical method helps you quite a lot.

---

## Part 1 — Leftover: event ID · page ID · group ID

The challenge coming repeatedly before you: for any target, if you need the **event ID**, the **page ID**, or the **group ID** — how will you find them? Location ID I told you — you must have understood — I showed it at the end of the last class. (The tool we used wasn't working in the last class — no issue, we don't depend on tools.)

How to find them — **one single technique**:

- **Page ID:** go to any **page** → **right-click → View Page Source** → **Ctrl+F** → search **"page_id"** — it will show.
- **Event ID:** go to the **event** (e.g. from the profile's About → life events, click whatever event they attended/created) → view page source → search the event ID.
- **Group ID:** if your target is **added in any group** — or from your investigation you feel "they could be part of this group" — go to that **group's page** → right-click → view page source → search **"group_id"** — you'll find the group ID there.
- **Alternative:** copy ALL the code (Ctrl+A, Ctrl+C), save it into any **text file**, then use the **`grep` command** — you can find it out very easily — but for that you'll have to use the command line.

This is how you find out every ID — because look: for the categories — example: for pages, go to the page and find the page ID; for events — the ones they've shared — event ID; here ID… group ID likewise. Earlier I spent quite a lot of time tackling this — in the last class I showed it… whatever your target's ID — username ID — on that basis I told you. We will NOT waste time on this; we're going directly… Mark — this much you must have understood.

---

## Part 2 — Manual URL manipulation (when every tool fails)

Now think of one thing: suppose you used all the tools so far — and the tools didn't do their job, or the tools aren't in working condition — **but we are ethical hackers**; we don't remain dependent on any one tool. What's our solution then? **The manual method** — and in the manual method I'll teach you: **how to manufacture [queries] with the URL — how to manipulate the URL.**

Look: Photos, Videos, Marketplace, Pages, Places, Groups, Events — you can see all these things. All the tools we've used so far give you search results on the basis of these very things, inside Facebook's page itself — they just use Facebook technically: you put keywords and extra details — some ID — location ID, target ID, post ID — and they give you information, each with their own output style and capability on separate pages.

Whatever you see here — this is called **categories** — these are all **categories**. And every category has **sub-categories**: I do Posts [category] — inside it you see sub-categories; I do **People** — that's a main category, and inside it the sub-categories — **Friends, City, Education**. Sub-categories then have **filters**.

### Anatomy of the Facebook search URL

Let me copy this into the notebook. Look — the first thing you see: this [the `https://`] is the **protocol**. In the next part, what you see (`www.facebook.com`) — we call it the **domain** — or **subdomain**. Then its **path** — then the next thing you see — this we call the **category** — the very categories I was talking about. Then down: you see **`?q=`** — the question-mark — meaning: "I'm querying" — on the basis of keywords you get information — `q=` then = **Mark** — our keyword we mention here.

Many times you'll ALSO see one more thing: **`&filter=`** (F-I-L-T-E-R) — and then some **random value**. This is the **filter** — the filter on the basis of which we [narrow]. Whatever value shows in front of `filter=` — it is given to you **base64-encoded, in JSON [form]**. And when you **decode** this value, ALL the [filter definitions] will be there.

So you understood this… what is JSON — tell me first… *"It's JavaScript Object [Notation]… in encoded form"* — Facebook processes on this basis. If you directly [paste raw JSON] inside the URL's query, you'll see an **error** — it won't show you any result — just a random error. But if you take whatever you're trying to find — the JSON — **convert it once into base64** and then filter with it — then it will show output **your way**.

### The pipeline: JSON → compact → base64 → URL

I have a document for you — you must have got it [shared link] — everything is mentioned in it about how you'll work with your Facebook queries. You'll have to read it yourself. Look: what did we see here? `search/top` — Top is **one category**. If I do Posts — this becomes Posts; if I do People — it becomes People — the category changes. Inside it, the sub-categories: **"Sort by — Most recent," "Posts from — posts from you, posts from your friends, posts from your groups and pages, posts from public, posts from pages," "Post type — seen posts," "Posts in group," "posted in group — location…"** These you have to see.

And whenever you have any **JSON format** — keep one thing in mind: **there must be NO space anywhere between [the JSON]** — no space, none at all.

Now watch the machine. [Copies the filter JSON into the formatter website] — paste… we put it… "compact" — meaning **no space** — **Process** — it shows **Valid** — **Copy to clipboard**. Now we have to convert into base64 — for that one more website — Ctrl+C… paste — encode — look: your **encoded value** is visible — **Copy to clipboard**.

Now: with Mark, which was our category? **Top** — and inside it we picked [a sub-category], and whichever filters we want to apply — go to the URL: first change [the category part] to `top`; then `?q=`… then `&`… then **filter** (F-I-L-T-E-R) — then the equal sign — Ctrl+V — paste. Now watch: **on this basis it shows you the answer** — see — this is the same [result] that was selected there as "Most recent" earlier — on this very basis it shows.

If you want to see [other filters]: "posts from you… posts from your groups and pages" — on that basis… If you want "posts from page" — **careful** — for that you'll need the **page's ID** — the page ID mentioned there — and you know how to find the page ID / event ID / group ID — I told you. Simply: before taking it [to base64], in the formatter itself you can **change this value** — put the [page ID/location ID] in. For location too, you'll have to [swap]: paste the location… you have to go to Mark's profile — we need his **location ID** first — for the location ID we [open the place]… next… click… "Things to do" — copy — base64 — next — the match was: **tagged location**. Then back — paste — Enter. **You can do information gathering by manipulating the URL.** I've shown you two ways. I've told you — you have to try each one yourself: if you want to become better in OSINT, to pull maximum information — I'm very happy for you — but you're limited without practice. Your job is to practice; the document's with you — read and experiment.

## Part 3 — Combining filters: the JSON merge rules

Now: till now we manipulated ONE filter. What if you want to use a **combination of more than one filter**?

**The rules — keep them in mind always:**

1. Main category → sub-categories → and inside each sub-category, its **filter options** (e.g. "Posts from: you / your friends / your groups and pages / public / pages" — that's five options in ONE sub-category).
2. **Within ONE sub-category you cannot combine two options** — you can use only ONE of the five at a time.
3. **You CAN combine one option from sub-category A with one option from sub-category B** — e.g. "Most recent" (Sort-by) + "Posts from pages" (Posts-from) + one from Post-type. Building a 3–4 filter combination is fine **as long as each clause comes from a different sub-category of the SAME main category.**
4. **You canNOT combine across main categories** — `search/top` filters can never be merged with `search/posts` filters. If you're making 3–4 combinations, they must be **within one main category**, using [different] sub-categories of it.

**How to merge two filter JSONs — the mechanics:**

JSON always **starts with `{` and ends with `}`**; the filters live inside as key–value information. To combine:

1. Take the first filter's JSON — **delete its closing `}`**.
2. Take the second filter's JSON — **delete its opening `{`**.
3. Put a **comma** between the two halves (any spaces you leave are no issue — we'll remove them).

Now it's one `{ … , … }` — a combination of two filters — both taken from different sub-categories. Copy it → into the formatter → it **auto-compacts** → Process → shows **Valid** → Copy to clipboard → to the **base64 encoder** — clear the box — paste — **Encode** — see: it added both — this is its base64 value — **Copy to clipboard** → back to the URL — remove the old filter value — paste — Enter.

Now — **it will show output on the basis of exactly these two filters** — "Most recent" + "from this ID". And you'll notice one more thing: on the left, the UI **highlights** the very facets your query used — if I change the category in front of you, you'll see the other category… the highlights tell you which sub-categories are active. Keep one thing in mind: once you've used the URL-manipulation technique, if you then use Facebook's **own search bar** again [in that flow], the manipulation **stops working** — it will then work by Facebook's own rules.

---

## Part 4 — Q&A: private accounts? → the friend pivot

**Anything… social engineering is the LAST option.** You'll have to use social engineering — and here's why, in the case of private accounts: if your target made his account private — but **his friends, his close friends, his relatives, his family members — will they ALL have private accounts?** Someone or the other — some group member, some family member, some close friend — will be found who has **not** made his account private.

Even if he made his own account private — look: you [the attacker] are connected with the second person, the friend — so **make THAT friend your target**. When you make him your target, you don't need the main target's information [directly]: you start information gathering with the second man. On his basis — his keyboard/timeline — somewhere or the other you'll find information which, though the target kept it private, is **public through the friend** — because **you cannot guarantee your friends' [privacy]**.

Try this technique yourselves to see: make your own account private — hide everything — but from your account you commented somewhere, or with some friend you exposed a location — you made YOUR account private, but **through the friend you directly exposed yourself**: the account may be "black-private", but you exposed yourself there, with the friend.

So in that case you'll target the main target **through the friend's account** — because that friend will get **manipulated easily**: you'll talk as if you're his friend — if you're not getting information from him, you have to **create a movie-type scene** 🙂 — you'll have to go through the friend, through the family member, to gather information. And there too you'll get quite a lot; after that you can use him easily.

("I hope I answered your question, Manmohan" — about how to use multiple [filters] in combination — the URL-manipulation technique — "did everyone understand, yes or no?" — and the recap of the rules: only **inside** one main category, using one filter each from its different sub-categories — never crossing main categories.)

---

## Part 5 — Does the target have other accounts? Messenger trick + tool barrage

If you want to know whether your target has **multiple accounts** — any **Instagram** account:

**Trick one — Messenger:** you have the first name, last name — simply search it in **Messenger** — a **list** comes; and this information is often also visible: **whether they have an Instagram account** — it shows in [Messenger's] **Discover** — you can confirm from there too: a list comes, and in Discover the Instagram [linking] is visible.

Now the tools — use them yourselves:

### 1) Profil3r — name-based enumeration (GitHub CLI)

This one [points to the screen]: on **GitHub** — a **Profil3r** ["profile"] tool. If you don't know how to install: clone it — `git clone` — open your **terminal**; you can keep it inside a "Facebook OSINT tools" folder — `ls`… Enter — "already exists" because I downloaded it earlier — you'll download it the same way. Then: `cd` into it, install the setup/requirements, and use it like: `python3 … -h` → the **help file** shows (if you don't know Linux, please go to our [Linux] series — helps a lot!) — then **`-p`** for the profile: I searched **Mark Zuckerberg** and hit Enter. It asks: **which separator — dot, dash, or underscore?** (I keep dot — use space to select; I selected the first.) Then it says: what-all to extract with this name — domain names? **email**? internet-forum postings? [number/breach] programs? searches on **Facebook, Instagram, LinkedIn, MySpace, Twitter**? Select them all — then hit Enter, brother — it **starts gathering**: emails, multiple accounts linked to this name… "type: no result"… here — 97 [findings] — quite a lot of information shows — then it's up to you how to use it. And look — so many IDs found on Facebook related to it; then it'll find **images** [attached to the emails]; for every email it finds it'll keep digging… Meanwhile, more tools.

### 2) Reverse-image tools (two web apps)

You have the target's profile picture: on this basis you can **analyse where-where this profile [picture] has been shared**. For that there are some tools — you got the list — both of these: open them, **upload any picture**, and it gives you results related to it. (In the demo one was down/not responding — "your job: you'll show ME which finds what kind of result" — because until you use a tool yourself, you can't know how it's used.) **Pro tip for small targets:** if your target is a small one — a 2–5 person practice target — do **reverse image search on EVERY photo** with these tools: you'll find where that photo was used — maybe the target didn't use it, but someone used his photo somewhere — you'll get to those places too, click through to whichever social media or site it shows.

### 3) whatsmyname.app — exact-username sweep

If you have the **exact username** of any target — not the general name — there is **whatsmyname.app**: simply put the username (I put just **"mark"**) — Search — it starts — shows where-where an account exists with this name — it's checking its **581[-site] database** — look: dev.to, hyperlink, games, debates… it found an account in each — click any and you'll see (some may not run [dead links]) — but here, with the name "mark", something-or-other is found — it will try to find it everywhere.

### 4) namecheckup.com — color-coded availability

Second: **namecheckup.com** — type the keyword — I typed "mark" — if you have the exact username, simply… look: the **RED** ones here = no account there / not available; the **yellow/light-pink** ones = account not found [uncertain]; the **GREEN** = at these very places accounts EXIST with this name. E.g. I open the Facebook [chip] — look: the "mark" Facebook account — the very one I was talking about. And there can be **false positives/negatives** here — the Telegram one came yellow — so try and see what-all you find. Two websites told; that's third and fourth.

### 5) FBI — "Facebook Information" (token-driven CLI)

Next, one which helps quite a lot in information gathering — **especially finding your FRIENDS LIST, finding your friends**: this one — when you open it — you have to **gift-clone** it [git clone], download — same process — simply: `apt update` and upgrade your machine first, then `pip install -r` [requirements]… its output: information in **JSON format and HTML** both. Look how many email addresses are visible… — "mark@gmail.com"-type results… it shows quite a lot in between… the Activator… if I zoom in and show you — this was your [output] — shown zoomed. 

Back: `cd`, `ls`… `python3 …` — the remote: open, help, about, exit. **To use it you first must add a TOKEN**: to add the token — [log in with] your Facebook account email-ID/password → **"Generate access token"** — once the token is generated, simply: **`get_data`** — "fetching friends' data" — whichever ID's [token] you're using, **all ITS friends' data** will be visible — since we logged in, all MY friends' data will come. Otherwise YOU can mention the ID here — **dump ID** — and this is how you use this tool — it's written [in the README] — and look what it does basically: **get_info → information about your friends**; **dump → phone numbers too** (if publicly available), **emails too** (if public, not private); **"dump ID from your friends"** — mention the ID between [the flags]; **remove**… The **bot** option: whatever ID you generated the token with — in that ID — you can even **delete that ID's friends' posts**… but this part **needs updates** right now — I worked on it; if anyone knows **Python scripting**, they can operate [fix] it — otherwise the rest [works] — everything's clearly explained in it — type **help** — here too you have to log in every once [token basis]… These were the tools whose little names are written here — I told you two [classes'?] tools… and these — the list I provided — quite good tools.

---

## Part 6 — Facebook OSINT: FINISHED

So today we **finish Facebook OSINT right here.** I hope — tell me once — yes or no — did you understand? Which tools did I show you: the ones where you upload a **photo** and get information; where with any **username** (or, without a name, first/last + keyword) you find where-where accounts exist under it; then **Profil3r**; then the **base64 encoder/decoder** and the **JSON formatter** — the file on whose basis you'll do ALL your URL manipulations — and IntelX [from before], the screenshots in your group — take screenshots if you haven't got them. If those tools don't work — **this WILL work, 100%**. Please just tell me — understood or not?

## Part 7 — Q&A: what laptop for hacking?

- **RAM:** minimum **16 GB** (if you want to do good hacking practicals, and programming alongside).
- **Graphics card:** min **4 GB**, better **6 GB** — if you want to run multiple machines in VirtualBox, you need the minimum [specs].
- **Processor:** minimum **i5**; if **i7** — very good.
- **Company doesn't matter:** in hacking/programming, the final work is **processing** — for processing you need RAM and a good processor.
- We recently posted a **blog/video** — go to YouTube, take the guide on which laptop to purchase.
- **Don't fall for pen-drive "hacking kits":** people install tools in a pen drive and say "we made our own OS" — a pen drive is SO slow — and it's just a money-making gimmick. [Don't buy into it.]

Okay — a lot remains [in the course]; it will be decided sitting together — you'll find out in the group today itself: **if decided, your first session will be on Sunday** — otherwise I can't say anything. Check Flipkart if you want [for laptops], bro — it'll be right, good for you. And if there's any [other doubt] — ask [your friends]… Alright — [session ends].

