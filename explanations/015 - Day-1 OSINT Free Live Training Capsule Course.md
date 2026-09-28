# Explanation — OSINT Day 1: Introduction & Why It Matters

**Lecture:** 015 — Day 1, OSINT Free Live Training Capsule Course
**Translation:** [`english/015 - Day-1 OSINT Free Live Training Capsule Course.md`](../english/015%20-%20Day-1%20OSINT%20Free%20Live%20Training%20Capsule%20Course.md)
**Note:** This begins a **new 10-day course**, separate from the Kali Linux series. It interleaves with the remaining Kali sessions in the transcript numbering.

---

## ⚠ Part 0 — The disclaimer (read first)

The session opens with a formal warning, repeated three times across the hour:

> **This course is for EDUCATIONAL PURPOSES ONLY.**

| If you… | Consequence stated |
|---|---|
| Use this knowledge **illegally** | You come under **cyber law** |
| Perform **malicious activity** | Possible **large financial penalty** |
| Try to **cause harm** to anyone | Possible **imprisonment** |

> **"From Defronix Cyber Security, we will NOT provide any kind of support"** to anyone who deliberately causes harm — *"rather, we will provide whatever help is required [to the authorities]."*

### The legal line, stated precisely

This is the clearest formulation in the lecture and worth memorising:

> **OSINT is LEGAL as long as you are looking at, reading, or collecting publicly available information.**
>
> **It becomes ILLEGAL the moment there is wrong intention behind it.** Acting on that information without permission makes it **a crime.**

The distinction is **intent and authorisation**, not technique.

---

## Part 1 — What OSINT is

### The formal definition

> **Open Source Intelligence is a multi-step methodology for collecting, analysing and making decisions about data accessible in publicly available sources.**
>
> The term **"open"** refers to **publicly available** sources.

### The three verbs

| Stage | What you do |
|---|---|
| **Collect** | Gather publicly available information about a target |
| **Analyse** | Process and correlate it |
| **Decide** | Determine whether the information is **accurate or not** |

> Note that OSINT is **not just searching** — the analysis and validation stages are what make it intelligence rather than data collection.

---

## Part 2 — Who it's for

The list given deliberately spans the whole spectrum:

- Ethical hacker · black hat · forensic expert
- Threat hunter · incident responder · bug bounty hunter
- **A normal person** · technical or non-technical
- **"Even our PARENTS"**

> **"In OSINT there is no single role of a data analyst or anybody. EVERY SINGLE INDIVIDUAL has a role."**

**The only prerequisite stated:** *"In this, all you need is COMMON SENSE."*

---

## Part 3 — ⭐ The core argument

The lecture is built around one question:

> **How does a hacker hack your system?**

### The chain

```
You cannot attack what you do not know
            ↓
So the FIRST step of any attack is INFORMATION GATHERING
            ↓
And information gathering is possible BECAUSE OF OSINT
            ↓
Therefore OSINT is the first step of every attack
```

### What an attacker needs before they can act

| Category | Examples |
|---|---|
| Identity | name, username, email address |
| Location | where they live, where they go |
| Activity | what they do, what they like |
| Contact | mobile number |
| Presence | social media accounts |
| Assets | which car they own |

> **"Until an attacker knows all this information, they cannot attack."**

### The ocean metaphor

> **OSINT is an OCEAN** — *"such an ocean where information lies"* in abundance.

But having an ocean doesn't mean you can drink from it:

- Extracting information requires **different steps and methodologies**
- **There is no guarantee** the information you need is there
- Some information is **public**, some has been **hidden** or is **private**

**The methodology is what the rest of the course teaches.**

---

## Part 4 — OSINT is defensive too

> **OSINT was originally created for defensive use** — by cyber security engineers, to secure organizations.
>
> **But attackers have started using it wrongly**, to harm people.

### Why everyone should learn it

> **"You should know HOW an attacker extracts that information from you. Only if you know will you be able to PROTECT yourself."**

The common objection the trainer anticipates:

> *"What information of mine is public? Why would anyone hack me? I don't have any information at all."*

The rest of the lecture exists to demolish that assumption.

---

## Part 5 — What information gets gathered

### 5.1 About a person — the profile

| Category | What it reveals |
|---|---|
| **Likes / dislikes** | preferences, interests |
| **Education** | how far, and **from where** |
| **Activity patterns** | **when you are active, when you are not** |
| **Places** | where you like to go |
| **Weaknesses** | what you are vulnerable to |
| **Emotions** | mood, state of mind |

**How emotions leak:** happy posts when things go well, different stories when there's a problem. Likes, comments and stories build a behavioural profile over time.

### ⚠ The uncomfortable point

> **"Where is all this information coming from? From the PROFILE. You are telling everything yourself."**
>
> **"The hacker is not forcing it from you — but you are giving that information":** when you cry, when you laugh, where you like to go, what you do, your name.

**And your friends make it worse.** Their comments reveal *"what is this person's character, what are they afraid of"* — corroborating detail you didn't post yourself.

### 5.2 About an organization — the platform

| Target | Information sought |
|---|---|
| **Domain** | domain name, hostname, **subdomains** |
| **Hidden content** | hidden files on the server |
| **Network** | internal IP, external IP, **full IP range** |
| **Software** | OS type, **OS version**, technologies in use |
| **Services** | which services they run (often found via **news**) |
| **Defences** | **which firewall** — vendor, and whether legacy or **next-generation** |

> **"We gather all this information, and there we even find out the VULNERABILITIES."**

---

## Part 6 — Why it's non-negotiable for security work

> **"If you don't know OSINT and you are a cyber security engineer, then LEAVE that field."**

The reasoning:

1. **Information gathering is the first step** of every pen test.
2. Information gathering **runs on OSINT methodology**.
3. **If you can't do step one, steps two and three are impossible** — you have no information to work with.

---

## Part 7 — ⚠ The case study: when OSINT costs a life

A real 2020 case is walked through in detail. It is included specifically for people who believe *"nobody can do anything to me without my permission."*

> **"Those who feel like this — either their eyes are closed, or they don't know how things happen."**

### The timeline of disclosure

| Post | What was leaked |
|---|---|
| **18 Feb, ~11:00** — lands in California, posts story | **Location on**, background shows the venue |
| Next — haircut at barber shop | **Location on** |
| Next — pool photos | **Location on** |
| Next — bathing, hotel room, front/back views, outside the hotel | Building and surroundings |
| **The mistake** — photos in a car holding **cash** | **Home address visible in the left corner**; wealth displayed |
| Next — driving | Movement pattern |
| **~11 PM** — video of shopping bags | **Shipping tag on the bag revealed the FULL address** |

### How the pieces combined

```
Wealth displayed        →  worth targeting
Location tagged         →  which city, which venue
Partial address (3 of
4 digits visible)       →  only 1 digit left to guess (1-9)
Vehicle visible         →  identification and confirmation
Shopping bag tag        →  FULL address revealed
Continuous posting      →  real-time movement tracking
```

> They were being **followed continuously** through the posts. *"Actually they were thieves; they were following him."*

**Outcome:** last post at **4:30 a.m.** Four people entered the home that night while he slept, took cash and phone, and killed him.

### The lesson

> **"Those who did this were NOT cyber security engineers, they were NOT hackers. They used OSINT — and they killed someone."**

**The daily habits that created the exposure:**

- Posting **with location enabled**
- Posting **in real time** rather than after leaving
- Displaying **wealth and valuables**
- Not checking **backgrounds and corners** of photos
- Not checking **labels, tags and documents** visible in frame
- **Continuous** posting establishing a predictable pattern

**Defensive takeaways:**

| Habit | Fix |
|---|---|
| Location tags | **Turn off**; post after you leave |
| Real-time posting | **Delay** posts |
| Backgrounds | **Check every corner** before posting |
| Documents/tags in frame | **Crop or blur** |
| Displaying valuables | **Don't** |

---

## Part 8 — The syllabus (10 days)

| # | Topic | What it covers |
|---|---|---|
| **1** | **Advanced search engines / Google Dorking** | Extracting what the first page *doesn't* show you. Google, Yahoo, DuckDuckGo, Bing. Also called "Google hacking." |
| **2** | **Image analysis & geolocation** | Who took the image, **when**, **where** — down to exact coordinates |
| **3** | **Emails, phone numbers, personal info** | Tools for finding contact details and interests |
| **4** | **Social media OSINT** | Facebook, Instagram — *"where we can extract the most information"* |
| **5** | **Website intelligence** | Domain, infrastructure and technology profiling |
| **6** | **Steganography** | Information **hidden behind** image, video or audio files |

### Why search engines need a whole module

> **"The first page always shows you that thing which a company WANTS to show you."**
>
> A hacker gets **none** of the information they need from page one. Advanced operators are how you reach the rest.

---

## Part 9 — Course logistics

| Item | Detail |
|---|---|
| **Duration** | **10 days**, running **every other day** |
| **Why the gap** | So you can **revise, make notes and write your own report** |
| **Prerequisites** | **None.** No Linux, no security background, *"come from absolutely zero"* |
| **Practicals** | *"The course is full of practicals"* — performed **in a lab**, never against real targets |

### Three things tracked, and the prize

1. **Attendance** from Day 1 to the end
2. **Comments** on the LinkedIn page — notes written up **like a report**
3. **An assignment** during the course, submitted as **report writing**

One student is selected on this basis and contacted **via LinkedIn**.

### On LinkedIn

> **Not just for the course.** *"If you have to get a job anywhere, your LinkedIn account is looked at."* Add every course and certification you complete.

---

## Part 10 — Q&A highlights

**Prior knowledge needed?** None at all.

**Will we learn to hide our own information?** **Yes** — and the recommended exercise is to **run OSINT on yourself** to see how much of you is publicly exposed.

**Can we practise on real people?** **No.**

> *"We cannot take out anyone's social media account online; nobody can do that with anyone, ever. Wherever you do training, you have to practise in the LAB."*

**What about someone with no social media presence at all?**

> *"What did I tell you — the information is PUBLICLY AVAILABLE. That is what I said."* OSINT works on what has been exposed; it is not magic.

### OSINT's role in threat intelligence

A substantial answer worth extracting:

```
Risk Management
      └── Threat Intelligence  (a part of risk management)
                └── OSINT      (the engine underneath)
```

**During incident response**, an attacker leaves fragments — an **IP**, a **name**, a **URL**. You then use OSINT to ask:

- Is there information about this **on social media**?
- Has this **IP been used in an attack before**?
- What else is known about this URL/indicator?

**Frameworks mentioned:** **MITRE** and similar — *"they do the work of Open Source Intelligence for you"*, publishing indicators of compromise and APT group activity.

**For genuinely novel attacks** — malware not yet in any SIEM or IDS signature — **OSINT is the only analysis route available.**

> **"The stronger your OSINT is, the stronger the analysis you will be able to do."**

---

## Part 11 — Self-check questions

1. State the disclaimer. At exactly what point does OSINT cross from legal to illegal?
2. Give the formal definition of OSINT. What does "open" refer to?
3. Name the three stages of the OSINT methodology. Why isn't it just "searching"?
4. Reconstruct the four-step chain from "you cannot attack what you don't know" to OSINT.
5. List six pieces of information an attacker needs before they can act.
6. Explain the ocean metaphor. Why doesn't a vast amount of information guarantee you can use it?
7. What was OSINT originally created for, and how did that change?
8. Why should a non-technical person learn OSINT?
9. List six categories of personal information exposed through a social media profile.
10. How do a person's *friends* increase their exposure?
11. List six categories of organizational information gathered during OSINT.
12. Why is OSINT described as non-negotiable for a security engineer?
13. In the case study, list every distinct piece of information leaked, in order.
14. How did three visible address digits become a full address?
15. Name five daily posting habits that created the exposure, and the fix for each.
16. What is the significance of the perpetrators not being hackers?
17. Name the six syllabus topics.
18. Why does the first page of Google results rarely help an attacker?
19. Define steganography.
20. Draw the relationship between risk management, threat intelligence and OSINT.
21. Why is OSINT the only option when analysing a genuinely novel attack?

---

## Part 12 — Where this sits in the roadmap

> **"Your PEN TESTING JOURNEY is starting. We have already had you do Linux; from Linux we have started your pen testing journey. This is also the SECOND PART of the roadmap."**

| Stage | Course |
|---|---|
| **1** | Kali Linux fundamentals (Days 1–15) |
| **2** | **OSINT / information gathering** ← you are here |
| **3** | Penetration testing (future) |

The Kali course is **not a prerequisite** for OSINT, but is recommended alongside it.
