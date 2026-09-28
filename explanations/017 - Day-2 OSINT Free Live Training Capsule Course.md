# Explanation — OSINT Day 2: Search Engines & Google Dorking

**Lecture:** 017 — Day 2, OSINT Free Live Training Capsule Course
**Translation:** [`english/017 - Day-2 OSINT Free Live Training Capsule Course.md`](../english/017%20-%20Day-2%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Builds on:** OSINT Day 1 (what OSINT is, the legal boundary)

---

## Part 0 — Why half this lecture is "basics"

The trainer spends the first half on search engine mechanics before touching a single dork. His justification is worth keeping:

> **"Delivering Google Dorking would hardly take 15 to 20 minutes. But I don't want the concept delivered in only 15 minutes, because a very basic concept is attached to it."**
>
> **"If you don't know that basic concept, then if tomorrow you have to build YOUR OWN Google Dorks, you will not be able to build them."**

### The failure mode this prevents

> You blindly search for a website with dorks. Nothing comes back. You conclude *"Google Dorking doesn't work."*
>
> **The real reason: that website was never INDEXED.** Google has no information about it at all. No dork can retrieve what was never crawled.

**Diagnostic rule:** if a plain search returns nothing for a target, **a dork will not help either.** Check indexing first.

---

## Part 1 — What a search engine is

> **A complex program designed to search for information on the World Wide Web.**

| Engine | Approximate share of use |
|---|---|
| **Google** | the large majority |
| Yahoo, Bing, others | ~20–30% combined |

The key insight: when you get results in milliseconds, **the work was already done long before you typed anything.**

---

## Part 2 — ⭐ The three stages

> **"To show information, search engines do a lot of BACKGROUND WORK."**

| Stage | What happens |
|---|---|
| **1. Crawling** | Programs scan the web and collect data |
| **2. Indexing** | That data is organised and stored |
| **3. Ranking** | Results are ordered by relevance |

### 2.1 Crawling

> **Crawlers (also called SPIDERS) are programs responsible for finding information publicly available on the internet.** They **scan the whole HTML code** and try to **understand** it.

What a crawler extracts from each page:

- **Structure** of the page
- **Type of content**
- **Meaning** of the content
- **When created**
- **When updated**

The crawler then hands this to the search engine, which **stores it on its local server.**

### 2.2 Indexing

With **billions of websites**, raw storage is useless — it must be organised. *"Like it happens in a LIBRARY."*

**What actually gets stored** (not the whole page):

- Title
- Description
- Type of content
- Associated keywords
- Number of **incoming and outgoing links**

### 2.3 ⚠ The visibility chain

> **Not crawled → not indexed → NEVER appears in search results.**

This single chain explains why some targets are invisible to any amount of dorking.

---

## Part 3 — The library analogy

| Employee | Task | Search engine equivalent |
|---|---|---|
| **1** | Fetch all the books to a central table | **CRAWLER** |
| **2** | Sort them into sections — Hindi, English, History, Science, Maths, novels | **INDEXING** |
| **3** | Sit at reception; fetch requested books quickly | **RANKING** |

> Employee 3 can only be fast **if indexing and ranking were done well.** Frequently requested books sit at the top and are retrieved instantly; rarely requested ones take time.

---

## Part 4 — A worked crawl

```
1. mywebsite.com is hosted
2. Crawler arrives → reads title, description, content type, structure
3. Builds a keyword list:  apple, banana, pear
4. Hands data to the search engine
5. Search engine stores it on its local server
6. User searches "strawberry" → engine consults the index → returns the page
```

**Crawling never stops.** On the next visit the crawler finds a **link to `anotherwebsite.com`**, follows it, crawls that site too (`tomato, strawberry, pineapple`), and adds it to the index.

### Crawlers multiply

> **"One crawler can MULTIPLY itself."** It was crawling `mywebsite.com`; it **generated a second crawler** for `anotherwebsite.com` and left it there.

This is how **billions of sites** get indexed from a handful of starting points.

---

## Part 5 — `robots.txt`

> **"Every hacker's favourite file."** The first thing checked on any target.

### What it is

> When a crawler arrives, **the FIRST thing it checks is whether `robots.txt` exists in the ROOT DIRECTORY.**
>
> Its job: **specify which content should be crawled and which should not.**

### The format

```
User-agent: *
Disallow: /admin/
Allow: /public/
Crawl-delay: 10
```

| Directive | Meaning |
|---|---|
| **`User-agent`** | Which crawler this applies to. **`*`** = all. A name (`Bingbot`, `Amazonbot`) = only that one |
| **`Disallow`** | Do **not** crawl this path |
| **`Allow`** | Crawl **only** this. Without it, everything not disallowed is crawled |
| **`Crawl-delay`** | Wait N seconds between requests — useful if the server is slow |

### ⚠ The mistake that makes it valuable to attackers

> **`robots.txt` is NOT a place to hide private information.** It only *tells* crawlers what to skip.
>
> **But developers make exactly this mistake** — they list **private paths** under `Disallow`: an admin page, a hidden directory, a backup location.

**The result:** a publicly readable file that **advertises exactly which paths the owner considers sensitive.**

**Two properties make it trivial to find:**

1. Always at a **fixed location** — `/robots.txt`
2. **Anyone can read it**, not just crawlers

> Paths found here can then be probed, brute-forced or enumerated.

---

## Part 6 — Sitemaps

### The problem

A crawler navigating a tangled site wanders in circles, **takes a long time, and may SKIP pages entirely.**

### The solution

An explicit map of the structure:

```
example.com
├── About
├── Contacts
└── Category
    └── Subcategory
        ├── Product 1
        └── Product 2
```

> *"Its work is easier and our work is easier too."*

### Two types

| Type | Audience | Purpose |
|---|---|---|
| **HTML sitemap** | **Users** | Smooth navigation — find contact, login, home |
| **XML sitemap** | **Crawlers** | Gives the crawler the **exact structure** |

**For OSINT:** `sitemap.xml` is a **map of the entire site handed to you**, including pages not linked from anywhere obvious.

---

## Part 7 — Google Dorking

### The name

**Google** + **Dork** — where a *dork* is a **query** or **query operator**.

### Where it sits

| | **Black box** | **White box** |
|---|---|---|
| You know | **Nothing** — a URL or IP only | The **source code** and internal detail |
| Location | External | Usually inside the company |
| Task | Gather info → find vulnerabilities → **report** | Test the code → find bugs → report |

> **Google Dorking is BLACK BOX testing.**

### The core idea

> **"After TUNING UP our search query, we will find some more information [hidden] as well."**
>
> If you tune the query well, **sensitive information the developer never imagined would be reachable becomes reachable.**

---

## Part 8 — The operators

| Operator | Restricts to | Example |
|---|---|---|
| **`site:`** | a domain or TLD | `site:*.edu` |
| **`inurl:`** | text in the **URL** | `inurl:admin` |
| **`intitle:`** | text in the **page title** | `intitle:"index of"` |
| **`intext:`** | text in the **page body** | `intext:password` |
| **`filetype:`** | a **file extension** | `filetype:pdf` |
| **`" "`** | **exact string** match | `"index of"` |
| **`after:`** | results **after a date** | `after:2020` |

**On `intext:`** — *"however many web pages there are inside the website, wherever it sees that TEXT, it will search for it."*

### Understanding the URL parameter

```
google.com/search?q=best+laptop
```

> **`q=` is the query parameter; `+` is an encoded SPACE.** Recognising that search itself is just a parameterised request is the mental shift that makes dorking make sense.

---

## Part 9 — Worked dorks

### Domain and URL filtering

```
site:*.com inurl:india          # .com sites with "india" in the URL
site:*.com inurl:hack
site:*.edu inurl:india          # educational domains only
```

### Finding documents

```
site:*.com filetype:pdf hacking for dummies
site:*.com "networking" filetype:ppt
```

> Legitimate everyday use: *"if I quickly had to make a PPT, I can go from here."*

### Finding open FTP servers

```
intitle:"index of" inurl:ftp
intitle:"index of" inurl:ftp after:2020     # filter out stale results
```

### Finding exposed log files

```
inurl:username filetype:log
```

**Why logs matter** — this maps to **OWASP Top 10: Security Logging and Monitoring Failures.**

> Logs record every login, logout and action on a server. They are **regularly monitored** and backed up. **If log files are openly readable on the internet, that is reportable.**

### Finding exposed email lists

```
filetype:xls [company keyword]
```

> A company saved emails in an **Excel file**, shared it, and **it is still on the internet** — a full employee email list is a **sensitive information leak.**

### Finding default server pages

```
intitle:"Ubuntu" "index page"
```

> Indicates a web server deployed **without OS hardening** — the default page was never removed.

### Finding exposed admin panels

```
intitle:"index of" inurl:phpmyadmin
```

In the live demo this surfaced a site with `token.php`, `translator.php` and **readable PHP source** in an open directory.

> **"The BEST thing for you will be to REPORT it."**

---

## Part 10 — ⚠ The ethical boundary, restated

> **"INFORMATION COLLECTION IS NOT THE OFFENCE."** The offence is what you do next.

### The trainer's repeated instruction

| Situation | Correct action |
|---|---|
| You find an open FTP server | **Find their email and REPORT it** |
| You find exposed logs | **Report it** |
| You find an open admin panel | **Report it** |
| You find leaked emails | **Try to report it** |

> **"Do not misuse it. If you misuse it, you can land in serious problems."**

### Realistic expectations

Three honest caveats given during the live demo:

1. **Most results are stale.** *"The information you find is lying there from long before; it won't even be active now."* One result dated from **2005**.
2. **Most results are noise.** *"Out of 100, 80 or 90 websites you find will be FAKE."*
3. **It is slow work.** *"You have to work quite hard, do a lot of research, and continuously investigate whether it is right or wrong."*

### Search all the pages

> **Don't stop at page one.** The thing you're looking for may be **poorly ranked and far behind.**
>
> *"It's possible that what you are trying to find is among your 200 results — maybe the LAST two — and all the rest are fake."*

---

## Part 11 — Tools mentioned

### Google's date filter

**Tools → Any time →** Past hour / Past week / Past month / Past year / **Custom range**

> Described as *"also an ADVANCED FEATURE"* — essential for separating live findings from decade-old noise.

### The Google Hacking Database (GHDB)

A public, community-submitted collection of dorks — **7,600+ entries**.

> *"You can use them one by one according to your requirement."* Also searchable as **"Google Dorks cheat sheet."**
>
> **"And if you want, you can BUILD YOUR OWN."** — which is the entire point of teaching the mechanics first.

---

## Part 12 — ⚠ On script kiddies

Triggered by a learner asking how to find someone's phone number. The answer is the most direct passage in the course.

### The claim

> **"In India, professional ethical hackers are 30%; the other 70% are UNGUIDED"** — no knowledge, *"whatever they got, they picked it up and copy-pasted it."*

### Script kiddie vs professional

| | **Script kiddie** | **Professional ethical hacker** |
|---|---|---|
| Knowledge | Copy-pastes without understanding | Collects info, then **develops skills for their domain** |
| Judgement | **Doesn't know right from wrong** | Knows **which information is how sensitive**, who should have it, and the **consequences of misuse** |
| Measure of success | *"I hacked a Facebook/Instagram account"* | Structured testing and reporting |
| Outcome | *"They end up in jail, not knowing anything"* | A career |

### The blunt version

> **"If someone feels 'I am an ethical hacker, but I couldn't hack Facebook, so I am not a hacker' — then YOU CAN LEAVE THIS CLASS."**
>
> **"This channel is NOT for those who have come only to become script kiddies."**

### The path instead

> After the basics, **specialise**: networking, network security, cloud security, or bug bounty. **Upgrade yourself accordingly.**
>
> **"If you just remain a script kiddie, then YOU ARE A VERY DANGEROUS PERSON TO ANYONE"** — *"because you are not a professional and you don't know what is right and wrong."*

---

## Part 13 — Complete cheat sheet

```
# ---- how it works ----
Crawling  →  Indexing  →  Ranking
Not crawled → not indexed → never in results

# ---- reconnaissance files ----
target.com/robots.txt      # what the owner tells crawlers to SKIP
target.com/sitemap.xml     # the full site structure

# ---- operators ----
site:example.com           # restrict to a domain
site:*.edu                 # restrict to a TLD
inurl:admin                # text in the URL
intitle:"index of"         # text in the page title
intext:password            # text in the page body
filetype:pdf               # by file extension
"exact phrase"             # exact string
after:2020                 # date filter

# ---- common dorks ----
site:*.com filetype:pdf "book title"
site:*.com "networking" filetype:ppt
intitle:"index of" inurl:ftp
intitle:"index of" inurl:ftp after:2020
inurl:username filetype:log
filetype:xls [company]
intitle:"Ubuntu" "index page"
intitle:"index of" inurl:phpmyadmin

# ---- resources ----
Google Hacking Database (GHDB) — 7,600+ dorks
"Google Dorks cheat sheet"
Google Tools → Any time → Custom range
```

---

## Part 14 — Self-check questions

1. Why does the trainer refuse to teach dorking in 15 minutes?
2. What is the diagnostic failure a beginner hits when dorking an unindexed site?
3. Define a search engine. Roughly what share of use is Google's?
4. Name the three background stages and what each does.
5. What does a crawler extract from a page? What is a crawler also called?
6. What does a search engine actually store — the whole page, or what?
7. State the visibility chain in three steps.
8. Map each library employee to a search-engine stage.
9. Trace a full crawl of a new site, from hosting to a user's search result.
10. What does it mean that crawlers "multiply"?
11. Where is `robots.txt` always found? Who can read it?
12. Explain `User-agent`, `Disallow`, `Allow` and `Crawl-delay`.
13. What mistake do developers make with `robots.txt`, and why is it so useful to an attacker?
14. What problem does a sitemap solve? Difference between HTML and XML sitemaps?
15. Break down the term "Google Dorking." What is a dork?
16. Distinguish black box from white box testing. Which does dorking belong to?
17. Give the purpose of `site:`, `inurl:`, `intitle:`, `intext:`, `filetype:`, `" "` and `after:`.
18. Write dorks for: PDFs on a topic; open FTP servers since 2020; exposed log files; leaked spreadsheets; open phpMyAdmin.
19. Which OWASP Top 10 category do exposed logs relate to?
20. State the ethical rule in one sentence. What is the correct action on finding an exposure?
21. Give three realistic limitations of dorking observed during the live demo.
22. Why must you search beyond page one?
23. What is the GHDB and how many entries does it hold?
24. Contrast a script kiddie with a professional on knowledge, judgement and outcome.

---

## Part 15 — Where this fits

**Syllabus item 1 of 6 is now complete.**

| # | Topic | Status |
|---|---|---|
| **1** | **Advanced search engines / Google Dorking** | ✅ **Done** |
| 2 | Image analysis & geolocation | next |
| 3 | Emails, phone numbers, personal info | |
| 4 | Social media OSINT | |
| 5 | Website intelligence | |
| 6 | Steganography | |

A **username enumeration** module was also referenced as coming later — the answer to *"how do I check what's exposed about me?"*
