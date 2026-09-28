# 017 — Day 2 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/017 - Day-2 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** How search engines work · Crawling, indexing, ranking · `robots.txt` · Sitemaps · Google Dorking
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`गूगल डोर`/`गूगल वर्किंग`/`गूगल डी वर्किंग`/`गूगल टॉकिंग`/`गूगल डॉग्स` = "Google Dorking"/"Google Dorks", `क्राउलर`/`कॉलर`/`करोल`/`क्रॉस`/`प्रॉब्लम` = "crawler"/"crawl", `करोल करना` = "to crawl", `रोबोट डॉट टक्स`/`रोबोट 2` = `robots.txt`, `साइट मैप`/`सेट मैप`/`ठीक मैप` = "sitemap", `एसएमएल`/`एक्सटर्नल` = "XML", `इन यूआरएल` = `inurl`, `इन टाइटल`/`इंटेक्स` = `intitle`/`intext`, `परिसर` = "complex", `बल्लमपति`/`वल्लबिलटी` = "vulnerability", `एफटीपी`/`एफबी`/`अप` = "FTP", `बौंती`/`भगवती` = "bounty", `स्क्रिप्ट कीड़ी`/`स्किप किडनी` = "script kiddie", `डॉग्स`/`वर्स्ट टॉप 10` = "OWASP Top 10"). The intended technical term has been restored where unambiguous.

---

[Music] [Applause] [Music] Hello everyone, good evening friends.

Tell me once — is my voice reaching everyone clearly? Tell me once in the chat. Okay, thank you.

So welcome, all of you, to the YouTube channel. **Let's continue from where we left off last time.**

So [we'll cover] what [Google Dorking] is, and some **real-world examples**. Some people will join in between, so let's start our topic.

---

## Part 1 — Why we start with the basics

Look — [Google Dorking] is used by a normal person to find out text, video, news [and so on]. **But from an information security perspective, Google Dorking is VERY VERY USEFUL.**

### The central question

> **Can one person, using Google, hack any website — or extract sensitive information about any website?**

**If I have to give you the answer to this question, then before that I have to answer some other questions.** After that you will get the answer to this question automatically:

1. **First of all, we need to understand HOW SEARCH ENGINES WORK.**
2. Second — [how websites get indexed].
3. **We also need to understand what `robots.txt` is, along with what a SITEMAP is.**

> **After understanding all these topics, automatically you will understand what I am trying to [convey].** On this basis, Google Dorking will be understood by you quite well.

### The trainer's approach

> Look, **my method is a bit different. I go from absolutely ZERO and leave you at an intermediate [level].**
>
> Basically — **delivering Google Dorking would hardly take 15 to 20 minutes.** I could deliver Google Dorking [in that time]. **But I don't want the concept of Google Dorking to be delivered within only 15 to 20 minutes**, because **a very basic concept is attached to it.**
>
> **If you don't know that basic concept, then in doing Google Dorking — or if tomorrow you have to build YOUR OWN Google Dorks — you will not be able to build them.**

**So these are three or four questions:**

> Your **search engine** — because on what do you do a Google search? **On a search engine.** So **if you don't even know how a search engine works**, or what a search engine is, or **how WEB CRAWLERS work**, **how your website gets INDEXED**, what the importance of a `robots.txt` file is — because you are a hacker, an ethical hacker, so you find this out — or how you get to see the `sitemap.xml` file...
>
> **If you don't know about these things, then you will have some problem in understanding Google Dorking** — because **Google Dorking cannot be taught to you just by firing four commands.** Because behind the scenes, how Google is used, how that [search] is performed — **if you don't know its basic concepts, then it's difficult.**

**Because my way of explaining is this, so I will explain it like this.** I think if some people are not interested in understanding the basics — [saying] *"Sir, we came to study Google Dorking, but you people are going to teach what a search engine does, what a crawler is"* — **then I am sorry for that. But my way is this**, because I am completely in the habit of explaining from the basics so that everyone understands.

---

## Part 2 — What is a search engine?

Look, you would have seen on screen that this type of Google search engine appears to you, and here there is a **search bar**; **whenever you put any keyword into it, then within a few MILLISECONDS you get its answer.**

> **So HOW do you get that answer?**

To find that out, **first you have to know: what is this search engine, and how does this search engine work?**

### Definition

> **A search engine is a [complex] program designed to search for information on the World Wide Web (WWW).**

**It's a complex program** — because a search engine has **billions of websites**; [it's] complex software.

**And basically this complex software** — the one used by normal users on the internet — **is Google; the Google search engine is used**, [and] the other search engines that are left, like **Yahoo**, **Bing**, or others — those are used by around 20–30% of people.

> So basically I can say: **a search engine is a mechanism for finding information for us**, in which we put in a **query** and it provides us with information related to it.

---

## Part 3 — How a search engine works

To understand this you have to understand the **working** of a search engine.

> **"To show information, search engines do a lot of BACKGROUND WORK, so that when you click on the search button you are presented with a set of high-quality results that answer your questions."**

**What this means:** whenever you search any keyword in your search bar, **to provide you the answer to that keyword, the search engine has ALREADY done a lot of background work.**

### The three stages

> That background work has been divided into **three stages:**

| Stage | What happens |
|---|---|
| **1. Crawling** | Programs scan the web and collect data |
| **2. Indexing** | The collected data is organised and stored |
| **3. Ranking** | Results are ordered by relevance |

---

### 3.1 Crawling

> **Crawlers are programs responsible for finding information that is publicly available on the internet.**
>
> **These programs SCAN the web and create a list of websites; they scan the whole HTML code and then try to UNDERSTAND it.**

**What does the crawler scan?** It scans **every single page** of the website; **it scans the entire HTML code**, and from there **it tries to understand:**

- What the **structure** of the web page is
- What **type of content** is inside it
- What the **meaning** of the content is
- **When** it was created
- **When** it was updated

> Whenever we create any website, or do any updates in it, **or even post a blog — Google's CRAWLER, which we also call a SPIDER, CRAWLS that site's data.**

**What did it do then — it gave [the data] to the search engine.** After crawling, it gave it to the search engine, **and the search engine STORED it in its LOCAL SERVER.**

---

### 3.2 Indexing

**When the Google search engine has this much information** — it has so much information, of **billions of websites** — **if it has to give its best result, then what will it have to do? It will have to do INDEXING.**

> **What does indexing mean — like it happens in a LIBRARY.**

### Why indexing matters

> **If any website has to come into Google's search index, then what will it have to do? It will HAVE to be crawled.** Otherwise it **will not be VISIBLE** in Google's search engine.
>
> **If it is not crawled, that website will not be indexed. If that website is not indexed, then it will NEVER appear in your search results.**

### What actually gets stored

**Generally search engines do NOT store all the information**; they store **some ELEMENTS** of every website:

- The **title**
- The **description** of the website
- The **type of content** of the page
- Some **associated keywords**
- The **number of incoming and outgoing links**

---

### 3.3 The library analogy

Let me take an example. **There is a LIBRARY, and inside it there are three employees**, and you are the in-charge, the supervisor.

| Employee | Task | Equivalent to |
|---|---|---|
| **Employee 1** | *"Go and take out all the books and bring them to the central table"* | **WEB CRAWLER** |
| **Employee 2** | *"Partitions/indexes are already made — put Hindi literature in the Hindi section, English in English, History in History, Science in Science, Maths in Maths, novels in novels"* | **INDEXING** |
| **Employee 3** | *"Sit at the reception. Whenever anyone requests a book, go and bring it to them quickly"* | **RANKING** |

> **How can [Employee 3] bring it quickly? Only when the indexing and ranking have been done well.** [He] knows which [books] are requested most, **so those will be at the top** and he will pick them up quickly. **If there is some book that is rarely requested, then it will take him time.**

**In the same way, your web page works like this too.** So this was a small library example, through which you would have understood **how web crawling, indexing and ranking work.**

---

### 3.4 A worked crawling example

Let me show you one more. **There is a website, `mywebsite.com`.** I hosted `mywebsite.com`.

**When I hosted my website:**

1. **The web crawler came.** It **crawled** my website.
2. Crawling it, it **read all the web contents**, and from there it read: its **title**, its **description**, **what type of content** it is, the **structure**, what **meaningful content** the page has.
3. Because this is the first time, it took that information.
4. It made a **keyword list** — for example: *apple, banana, [pear]* — it found those keywords out of the website.
5. **It took that data and gave it to the SEARCH ENGINE.**
6. **The search engine stored it in its LOCAL SERVER.**

**Next, when a user submits a query** — for example the keyword `s[trawberry]` — you gave it to your search engine.

**What happened:** the website's keywords were stored on the local server, **indexing was done there**, and an **organiser** was placed there too.

**So the search engine went to the local server, found out: "okay, whose keyword is this?"** — and found out it belongs to `mywebsite.com`. So it went to `mywebsite.com`, fetched your web page and **showed it on your screen.**

### Crawling continues

**Now, again — what do crawlers keep doing? They keep crawling.**

So: your `mywebsite.com` — you **added a link to another website** in it.

The crawler comes back to check whether anything was updated:

1. Goes to `mywebsite.com` again → sees the web content → *"okay, keywords apple, banana, [pear], nothing changed"*
2. **Next, it found a URL — `anotherwebsite.com`**
3. **It goes to that URL** and crawls its web contents too — finding out which contents and which other pages it has
4. There it found three keywords: **tomato, strawberry, pineapple**
5. **It combined both sets of data** and **gave it back to the search engine**, which stored it on the local server

> **So in this manner the process keeps going** — however many links you put inside a website, it makes a keyword list, collects the data and gives it to the server.

### Crawlers multiply

**Now you will say: does only one crawler work? No, it's not like that.**

> **One crawler can MULTIPLY itself.** What it does: it was crawling one website, `mywebsite.com`; then **from there it generated a second one** for `anotherwebsite.com`, and left that crawler there.
>
> **So in this manner crawling works.**

**Next time the search engine now has knowledge of TWO domains:**

| Domain | Keywords |
|---|---|
| `mywebsite.com` | apple, banana, [pear] |
| `anotherwebsite.com` | tomato, strawberry, pineapple |

> **So in this manner it does its work; indexing of websites keeps happening.**
>
> **So all the billions and trillions of websites that are stored — they worked in exactly this manner from the start**, through web [crawlers].

---

## Part 4 — `robots.txt`

Let me tell you — **you would have heard this many times.**

> **Whenever [a hacker sits down to test] any website, the first thing you try is `robots.txt`** — **every hacker [looks for it]; it's the first information.**
>
> **What is the purpose of this file, and why is it so important?**

### What it is

I have told you: **if any website has to appear in a search engine's result, it has to go through a process**, and every search engine has some programs which we call **crawlers.**

> **These crawlers work on a principle: whenever they crawl any website, the FIRST thing they check is whether there is a file in the ROOT DIRECTORY of that domain or server. That file's name is `robots.txt`.**
>
> **The major job of this file is [to specify] which content on a server or web application SHOULD be crawled and which should NOT.**

### The format

**This file has its own format.** As you see here:

```
User-agent: *
Disallow: /admin/
Allow: /public/
Crawl-delay: 10
```

| Directive | Meaning |
|---|---|
| **`User-agent`** | **The crawler's NAME.** In many places you'll see **`*`** — meaning **all crawlers** can crawl. If a particular name is given (e.g. `Amazonbot`, `Bingbot`), **only that one** may crawl |
| **`Disallow`** | *"Even if you crawl my website, the content mentioned here — you must NOT crawl it"* |
| **`Allow`** | *"Only crawl this."* Otherwise, if you don't specify Allow, **everything except the Disallowed items gets crawled** |
| **`Crawl-delay`** | *"When you crawl, DELAY a bit"* — put a few seconds between one crawl and the next. Perhaps there's a problem, or your website/server is running slow |

> **And this `robots.txt` file is found inside your ROOT DIRECTORY.**

### ⚠ The mistake developers make

> **This does not mean you should use `robots.txt` to HIDE any private information.** *"Okay, let me put the private [stuff] in it"* — **it's not like that.** It is only for **telling** [crawlers what to do].
>
> **But this is the very mistake developers make: BY MISTAKE they mention some PRIVATE information in `Disallow`** — because of which **any hacker, any ethical hacker** [can find it].

> **Every hacker's favourite file is `robots.txt`** — because **by mistake, developers leave behind some information there which is HIDDEN**, which can then be **brute-forced** or accessed using other techniques, enumeration, scanning.
>
> Or **any sensitive information may be written there** — maybe they've hidden an **admin page**, or hidden anything — **those things should actually not be there.**
>
> **So people take advantage of exactly this thing with `robots.txt`.**

**Two reasons it's easy to find:**

1. **It is in the root directory** (always at `/robots.txt`)
2. **It's not that only [crawlers] can access it — ANYONE can access it**, as you can see on screen

---

## Part 5 — Sitemaps

**Now let's talk about what a SITEMAP is.**

> It's possible that **your website is quite tangled**, and your website is **not coming into the index** and not appearing on Google's search engine. **So for that, a sitemap is made.**

### The problem it solves

For example, my website `example.com` has: an **About** page, **Contacts**, **Category**, **Product 1** (part of a subcategory) and **Product 2** (also under subcategory).

**Looking at it, it seems to you that every one is a separate page — but they are parts of the subcategory.**

**Now, the crawler came:** went to Contacts → then went into Category 1 → then to Product 1 → **then from Product 1 it went back to Category 1** → and so on.

> **This is a small example with 5 pages. If it's a very big website — [the crawler] got confused, right? It's taking a lot of time to crawl, and it's possible it SKIPS some [pages].**
>
> **For this very reason we use a SITEMAP.**

### With a sitemap

**The structure is given explicitly:**

```
example.com
├── About
├── Contacts
└── Category
    └── Subcategory
        ├── Product 1
        └── Product 2
```

**So the crawler comes: `example.com` → About → Contacts → Category → Subcategory → Product.** **So easily — its work is easier and our work is easier too.**

### Two types of sitemap

| Type | Used by | Purpose |
|---|---|---|
| **HTML sitemap** | **Your USERS** | So users can **navigate the website smoothly** — find the contact page, the login, the home page |
| **XML sitemap** | **CRAWLERS** | So the crawler gets the **exact structure** |

---

## Part 6 — What is Google Dorking?

**Now let's talk about our [topic]: what is Google Dorking?**

> Look — all these things I told you about crawlers, web crawlers, sitemaps, `robots.txt` — **all this information is a big part [of it].**

### Why the basics mattered

> **Now tell me one thing: if you don't know about crawlers, [don't know] how a website gets indexed** — and you are trying to search about a website, **blindly searching Google about a website which IS NOT EVEN INDEXED**, because Google doesn't have its information at all —
>
> **and you are blindly at it, saying "Google is bad, where is Google Dorking?"** — **no.** Because you don't know.
>
> **If you search normally for that website first and it's still not coming — then you will not find it with a Google Dork either, because that website is NOT INDEXED.**
>
> **If you don't know this logic behind the scenes, then how [would you know]? Not possible.**

> **My motto is this: before understanding any concept, explain its BASIC concept** — then, even when you work on anything, **you will enjoy it a bit more.**

### The definition

**`Google Dorking` is made of two words: Google + Dork.**

- **Google** — you know what it is; I have already told you what a search engine is and how a search engine works
- **Dork** — **basically it is a QUERY that you search**, or **a QUERY OPERATOR**

### Where it fits: Black box vs White box

> **Google Dorking comes under BLACK BOX penetration testing.**

| | **Black box** | **White box** |
|---|---|---|
| What you know | **Nothing** — just a URL or an IP address | You are given the **source code** and lots of information |
| Where | External | Usually **inside the company** |
| Task | **Gather as much information as possible**, then find vulnerabilities and **report** them | Pen-test the code, find bugs, test and report |

> **Google Dorking is used for BLACK BOX testing.**

### The core idea

> **"After TUNING UP our search [query], we will find some more information [hidden] as well."**
>
> **If you can TUNE your search query well and understand it, then it's possible that some SENSITIVE INFORMATION which the developer never even imagined will reach you** — you can search for it. **This is the whole concept of Google Dorking.**

---

## Part 7 — The search operators

Now there are some operators. **The list of search operators** that you get to see:

| Operator | Purpose |
|---|---|
| **`site:`** | restrict to a domain |
| **`inurl:`** | keyword must appear **in the URL** |
| **`intitle:`** | keyword must appear **in the page title** |
| **`intext:`** | keyword must appear **in the page text** |
| **`filetype:`** | restrict to a **file type** |
| **`" "`** | **exact string** match |

> Because these are **search operators** — since **indexing is done in this very manner**, so that it can show results on your screen very easily and in a very good way.

---

## Part 8 — Practical demonstrations

Come on then, let's do it practically.

### 8.1 Understanding the URL query parameter

On `google.com` I searched `best laptops`. **It instantly showed your result on your screen.**

**Now pay attention to one thing.** Look at the **URL**:

```
google.com/search?q=best+laptop&...
```

> **Here a PARAMETER is formed — a parameter of the search query.** `q=best` — `+` means a **SPACE**, because this has been **URL-encoded** — `q=best+laptop`.
>
> **So inside the query itself, your parameter is being formed** — the parameter of what you searched.

*(He deletes the trailing parameters to show the core query still works.)*

> **So this is a NORMAL search, from a normal person's, a normal user's perspective.**

---

### 8.2 `site:` and `inurl:`

**Now let's talk about how we use Google Dorks.**

For example, I want to search for a website:

```
site:*.com inurl:india
```

- **`site:`** is an operator — *"list all those websites which end in `.com`"*
- **`inurl:india`** means **`india` must appear in the URL**

**And I search it.** So all these sites are listed whose URL has `india` — `weindia.com`, `unsc-india.com`, `blue.amazon.com/india`, `services.india.gov.in`, `footballmatch.com/india`, `india.star.bg`...

**Another example:**

```
site:*.com inurl:hack
```

**Now all those sites will appear whose URL contains `hack`.** For example, if I open a website — **in its URL too you get to see `hack`.**

**Restricting to educational domains:**

```
site:*.edu inurl:india
```

> *"All the sites whose [TLD] is `.edu` — it will show all those sites on your screen, but with `india` in the URL."*

---

### 8.3 `filetype:` — finding documents

**Now, for example, I want to download a BOOK:**

```
site:*.com filetype:pdf hacking for dummies
```

**Meaning:** *"List out all those websites, `.com` — you can give a particular website's name too if you know it — after that the filetype is PDF, and the book's name should be `hacking for dummies` inside the PDF."*

**Look, this whole 'Hacking for Dummies' book — the ones that are PAID on Amazon — you got it here.**

**Another: finding a presentation quickly:**

```
site:*.com "networking" filetype:ppt
```

> **What does the DOUBLE QUOTE mean — you are searching that STRING [exactly]**; inside the query you are giving a particular keyword, [and] that keyword must be [present].

*"For example, if I quickly had to make a PPT, then I can go from here too"* — cyber security, [and] you'll get a PPT to download.

---

### 8.4 Finding open FTP servers

**Now, if you have to find out about an FTP server** — it's possible some organization is using an FTP server and **left it open on the internet**; they **forgot to secure it**, or left it open, **a serious [mis]configuration**.

**To find out how many are lying open on the internet:**

```
intitle:"index of" inurl:ftp
```

- **`intitle:`** — *"in the TITLE there should be `index of`"*
- **`inurl:ftp`**

### ⚠ The ethical boundary

> **KEEP ONE THING IN MIND: INFORMATION COLLECTION IS NOT THE OFFENCE.** The offence is [what you do next].
>
> **The problem here is that a lot of people will be new**, so as soon as they get information, **they'll start MISUSING it.**
>
> Actually, **the information you will find now is information that has been lying there from long before**, which won't even be active now.
>
> **If by chance you feel that there is a site with a security misconfiguration** — it has left FTP servers open and it is something serious — **then REPORT it.** Find out their email and report it to them. **Do not misuse it.**
>
> **If you misuse it, you can land in serious problems.**

**Looking at the results:** *"index of ... `mailbs.org`"* — he opens one to confirm, finds a directory listing, checks whether it's a real website, notes the data is from **2005** — *"quite an old database, so a lot of people would have seen it already."*

> **"But in this manner you can get details of any FTP service."**
>
> **"We will not go further than this."**

### Filtering by date

**"This is quite old data coming; I want to FILTER it":**

```
intitle:"index of" inurl:ftp after:2020
```

> **`after:`** — *"I want data after 2020."*

**Examining a government/educational site** he finds an FTP timeline, observation set, target science instrument data:

> *"So you can see whether it is genuinely report-worthy or not. It's a real website, an education website. So if you want, you can do HUNTING on it — if you get a bug bounty, you can try."*
>
> *"But there's no guarantee whether this data is confidential or not; all these things matter. You will have to research this thing."*

---

### 8.5 Finding exposed log files

**You know about the OWASP Top 10, in which there is "Security Logging and Monitoring Failures."**

> **Logs are a very, very important thing for any company, any organization**, and they are **regularly monitored**. Whatever work happens on any server — who logs in, who logs out, any work done on it — **it is logged**, and a file, a directory, a whole **backup server** is maintained for it.
>
> **If you find a URL whose log files are OPEN** — if you get to see log files on the internet — **then you can REPORT it.**

```
inurl:username filetype:log
```

**Result:** 42 results.

*He finds system logs from 2017 on a `security.net` site* — *"some system logs you'll get to see."*

> *"People keep working and find a bug, then report it, and they get a good bounty. But you have to work quite hard, do a lot of research, and continuously investigate whether it is right or wrong."*

---

### 8.6 Google's date-filter tool

**One more thing about Google:**

> **You get to see `Tools`.** If there are 42,000 results and you want to see them all, [it can't show everything]. **Simply go into Tools** — here the results [can be filtered by] **Any time**:

| Filter | Shows |
|---|---|
| Past hour | last 24 hours |
| Past week | |
| Past month | |
| Past year | |
| **Custom range** | **from which date to which date** |

> **This is also an ADVANCED FEATURE; you can use it.**

---

### 8.7 Finding exposed email lists

> **Using Google Dorks you can find out EMAILS too.**
>
> It's possible some company saved emails in an **Excel file** and shared it with someone, **and by mistake it is still lying on the internet.** That too can be a **sensitive information leak** — the full email list of its employees.

```
filetype:xls [keyword]
```

> *"You people can try this yourself. If you find something sensitive related to some website, then YOU CAN TRY TO REPORT [it]."*

### ⚠ Important search advice

> **You have to go to ALL the pages and search — not just the front page.** It's possible that the thing which is sensitive for you, or which you are trying to find out, **has poor indexing/ranking and is far behind.**
>
> **So you should scroll through all the pages, go to all the pages** and [check] all the websites. **It's possible that what you are trying to find is among your 200 [results] — maybe the LAST two results — and all the rest are fake.**

---

### 8.8 Finding default web server pages

Many times, when a company **hosts a web server** — for example **Apache** — the **default [page]** remains. It's possible they deployed the web server and, **because OS HARDENING was not done properly**, they **did not remove the default things.**

```
intitle:"Ubuntu" "index page"
```

*"If it shows an IP address then fine; otherwise we'll check another."*

---

### 8.9 Finding exposed admin/phpMyAdmin pages

```
intitle:"index of" inurl:phpmyadmin
```

**Result:** *"Look, you get such a page which is your default."*

He opens one: *"Look, they have left the whole website open."*

> ⚠ **"In this manner, out of 100, 80 or 90 websites you find will be FAKE."**

Going to page 6 of the results, he finds a live one with `token.php`, `translator.php`, `openlist.php` exposed, and PHP code visible in a directory:

> *"Look, PHP code you get to see. Meaning it's completely lying open. So if there is something — **the BEST thing for you will be to REPORT it.** Otherwise nothing else."*

---

## Part 9 — The Google Hacking Database (GHDB)

> There is also the **Google Hacking Database**. For example, look — *"just now I did online services"*... **this whole data, that page, continue, login portal** — someone has **submitted** this.
>
> **If you want to use these too, you can.** So here too there is a **Google Dorks CHEAT SHEET** — you can use them one by one **according to your requirement.** There are **[7,600+] entries** inside it; **this many Google Dorks are in front of you.**

> **So this was your Google Dorking. What more would you want?** You can search "**Google Dorks cheat sheet**" and you'll find more.
>
> **In this manner you can refer to these things and do your work. And if you want, you can BUILD YOUR OWN — you can learn that too.**

---

## Part 10 — Q&A

Comment and tell me whether everyone understood or not. **You have 5 minutes; if you have any doubt, you can ask.**

### Q: What does `intext:` do?

> **What `intext:` search basically means:** however many web pages there are inside your website — **inside those web pages, wherever it gets to see that TEXT, it will search for it.** There are web pages; **inside those, it will search and give it to you.**

### Q: Why use Google Dorking rather than normal search?

> **Google Dorking is an ADVANCED search [technique].** Basically, **when you do pen testing, or search about any target, you need MAXIMUM information about it.**
>
> There are some **databases** with Google — for example, ones which have **mobile numbers, email addresses** — the ones that are **publicly available**. **But you don't know about that thing**, that organization's [data] available to the public.
>
> **So what will you do — using Google Dorking you can try to find out that information. If you use a normal search engine, you will not get that level of information.**
>
> **Because your first motto is [gathering] INTELLIGENCE for any information security [work].** So when you do Open Source Intelligence, **you try to collect whatever information you can about any target, any person** — whether it comes from [one source] or from some tool.

---

## Part 11 — ⚠ On script kiddies

*A learner asks how to find someone's phone number.*

> **Look, one thing** — in India, take it anywhere — **professional ethical hackers [are] 30%; [the other] 70% are UNGUIDED**, who have no knowledge; **whatever they got, they picked it up and copy-pasted it.**
>
> **Those are SCRIPT KIDDIES — they are so dangerous.** They don't know what the thing actually is. **What they do: they get some information, pick it up and start MISUSING it** — and in this business **they end up in jail**, not knowing anything.

### What a professional does instead

> **A professional ethical hacker COLLECTS information** — everyone does that at the start. **After that, according to the requirement** — whether they need to learn the network part, learn coding — **they learn all those things according to their domain, and DEVELOP themselves; and after that they do testing.** That is a professional ethical hacker.
>
> **And they also know which information is how sensitive, who should have which information and who should not, which information they may use and which they may not — and what the circumstances of misusing some information could be. A professional ethical hacker knows all these things.**
>
> **But a script kiddie, at the start, considers himself [great]:** *"if I hacked Facebook or hacked Instagram, then I have done something huge, I am a hacker."*

> **Apart from this I will not call anyone an ethical hacker.** If someone feels *"I am an ethical hacker, but I couldn't hack Facebook/Instagram so I am not a hacker"* — **then YOU CAN LEAVE THIS CLASS; you don't need to come.**
>
> **I say it myself: this channel is NOT for those who have come only to become script kiddies.**

### The path forward

> **After the start, you have to go into whichever DOMAIN is yours** — whether your domain is **networking**, **network security**, **cloud security**, or **bug bounty** — **accordingly you will have to UPGRADE yourself**, will have to learn about it.
>
> **If you don't learn things accordingly and just remain a script kiddie, then YOU ARE A VERY DANGEROUS PERSON TO ANYONE.** Everyone will tell you this, **because you are not a professional and you don't know what is right and wrong.**
>
> **Your problem is exactly this: you don't know right from wrong. You are just blindly at it** — *"I have to do this, I have to do that"* — **but you don't actually know anything.**

---

## Closing

*A learner asks how to check [whether their own data is exposed]:*

> **We have some parts coming** — the **username enumeration** parts, and some others — **through those you can check. If your [data] is available, you will get that information.**

Okay, so let's end the session, and we'll meet in the next session. Thank you.

> **Once again a request: please don't forget to LIKE and SUBSCRIBE**, and **please share it with the maximum number of people** — so that **those who genuinely need it, who don't have money, who want free education and the best education**, who want to learn everything for free, **who have limited resources** — please share it with them. Add them yourself, subscribe, and tell them *"this thing has come at this time; at least you can watch it"* — so that those people get help and **they too can do something in their life.**

Okay — so let's end the session.
