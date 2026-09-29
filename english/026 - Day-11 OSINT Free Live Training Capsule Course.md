# 026 — Day 11 — OSINT Free Live Training Capsule Course

**Source transcript:** `transcripts/026 - Day-11 OSINT Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Topics:** Hands-on lab session (TryHackMe-style "Sakura" OSINT room) · Image forensics → metadata username leak · Username pivot across Google/Twitter/Instagram/GitHub · OpSec failures analysis · GPG key import → email recovery · GitHub audit-history hunting (edited/deleted info) · Bitcoin wallet / mining-pool tracing on a block explorer · Geolocation homework · Course-admin: participation, next classes
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** this lab session is demo-heavy and the auto-captions badly garble the on-screen artifacts — usernames, the email, the crypto addresses appear only as phonetic mush (`प्रून मिशन`, `रोड पीएनजी`, `टीजीपी`/`बीजेपी` = **GPG** spoken aloud, `मटर डेटा` = "metadata", `हिफिन हिफिन` = `--` flags, `ईथर camp` = an **Ethereum** explorer, `क्रिप्टो ई` = "crypto"). Where the exact string is unrecoverable I describe the artifact as seen; I do NOT invent the lab's answers. `[square brackets]` = summary narration.

---

[Music] Hello everyone, good evening friends. Tell me once — can everyone hear my voice or not? Confirm in the chat. Okay, thank you. Welcome, all of you, to the YouTube channel.

So till now, in the fast classes, the little things we studied — now let's do this: look at the **practical** — through some **labs**. You all were saying repeatedly: *"we want more practical practice; we're not getting anything — give us tasks; we're just following videos and making notes — we get to see nothing about what to do and how to perform."* Alright then — today we **live-solve**. The difficulty level in this [room] is easy-ish and it's quite interesting — **maximum of your techniques will get used**. And whatever of the pattern is left — which we'll discuss: **Instagram** and the rest, plus a little bit more remaining — that too we'll [cover]. But now, to show you a demo of "how does the thing work in practice" — through a lab.

So this lab: it will include some graded text to help guide you in the right direction, plus one or more questions that need to be answered in order to continue the investigation. Basically: before answering each question there's a **challenge**, and to complete it you get just a small **hint**, through which you can complete the task. For a **beginner**, many things at the start are challenging — that's why a few things are described to you as hints. If you're ready — "let's go", write it… okay, "let's go" is coming [in chat] — tell me quickly in chat. Okay — let's start.

## Task 1 — the image left behind

> *"There is no major damage and there does not appear to be any other significant indicator of compromise on any of our systems. **However, during forensic analysis our admins found an image left behind by the cybercriminals**…"*

Basically: a cyber-attack happened in which no major damage occurred, but there were some indications — the admins, during the forensic analysis, found some presence of an attacker — and there an **image** was found, left behind by mistake or on purpose by the cybercriminal. To reach the attacker you get small clues.

So I copied/opened that left-behind image, and read the instructions: it says the image can hold information **beneath the surface** — open it and build with it — within the file itself humans find information… when the photo… you will need to [use] the image found by open-source intelligence… in order to obtain basic information [from it]. 

Now we have an image. What can we do with the image? Let me open it side by side… [zooms] Ctrl-plus-plus… whatever image you see in front of you — if you look at it carefully, zooming… although we had named it **`.png`** at the end — here you see a **PATH** — it shows an export path: where it was exported from, which system it was sent to. So possibly the attacker **forgot to clear the metadata** — or deliberately left a trace for us, to prove himself.

First — **exiftool** on it: [terminal] Downloads… permissions don't matter to us… look: image with image-height — nothing great — but SEE what information we're getting here: an exported **path** — under the **home directory** — like when you're directly inside the Desktop, `/home/…/Desktop` — see what you're looking at: **this could be a USERNAME — any username.**

Let me copy it, and **Google** it — open — paste — and — see: when I searched — what do you get here — a **Twitter page** comes; I open it; there's an article-writer reference; an **Instagram page** too — this whole set of information is now with us. I open this one — the data page — look: **whatever you've learned so far — you can apply ALL of it here.** I'm just solving the lab for you; but *you* don't have to just watch the lab being solved — you go and apply what you learned on Facebook, Twitter — you have your target — practice easily — this isn't illegal — go and gather information just like this — good information will be visible; you'll get the idea of how information [comes] about a target.

Look — here you found the **file-path** — you found the CPU-minus-[flags]… So — **first question:** the lab asks: **"What username does the attacker go by?"** — for us, which username was it? This one — this `…Angel` string could be the username for us — copy — paste — **submit** — ✔.

## Task 2 — OpSec failures: username reuse

Second question — what does it want to know? It wants to know [about] the **fatal mistake in their operational security**: *"they seem to have reused their username across other social media platforms."* He was an expert at something, used his expertise, but didn't know how to save himself. What mistakes did he make?

1. He ran a cyber-attack — and left his **username** — exposed through the **metadata of the image**.
2. Second mistake: **he used the same username on every social-media platform.**

If he'd used a unique name — if we only found the username inside the metadata and nowhere else — we couldn't do much, because with just a username **alone**, "without [more] we can't find anything." But since the whole of social media [holds] the username, our work became even easier.

The instruction says: most digital platforms make it easy to find other accounts owned by the same person when the username is **unique** — this can be especially helpful on platforms such as job/hunting sites where a user is more likely to provide **real information about themselves** — full name, location… so that you can transfer and expand the OSINT investigation onto other platforms, in order to gather additional identifying information on the attacker.

Now we have to find: **"What is the full email address used by the attacker?"** — that's one question; and **"What is the attacker's full real name?"**

What do we have? This data — one Twitter [account] — go to Twitter, try searching.

Now — we don't know if the photo is **original or duplicate** — for us it's original **until proven otherwise** — because if it's a cyber guy, **definitely** this could be a **false/fake profile** too. Second: he used a name for this [Twitter] account — but look: the **username** you see for the account — **`@puro…low`** — this is his username — you can see it. Now: the target is with you. You've got quite a lot of information: one, the [display] name; the username on Twitter — this one we got from Twitter.

There's information: **21 [followers]**; **1 following** — you can open and see — you know well how to [analyse] — one following: **Microsoft — "mission to empower every person and every organization on the planet to achieve more"** — support… not much information in the following. Back to the profile. Username found. Now his **tweets** — read:

- *"No more forgetting meet-ups… [X.1]… I get new phones…"* — okay.
- Something shared — *"regular Wi-Fi and passwords…"* — okay.
- *"About someone else finding themselves on the dark web… anyone who wants them will have to do a real deep search to find where I posted them…"* — okay.
- *"Looks like my last page got removed when the website changed domains — adding a new one to remember…"* — this is what he said, this post — January 24 [one post]; in **October 20[20]** this was posted.
- *"Silly me — I forget to introduce myself… there I am **@<a different username>**"* — look: here you see **another username** — a different profile — fresh — beginner's "Chinese blossom season"…
- *"close to home — can't wait to finally be back"*…
- *"taking out some last-minute cherry blossom before heading home"* — okay.

So some information… but so far nothing related to the questions — **no email address anywhere** — these three posts, 29 followers, 46 [following]… for that you'd have to log in — and **Instagram OSINT I haven't taught you yet — I will, in a few days.** Nothing here… 

Now what do we have? This — it's his **GitHub** — open in new tab: there's a **DTA/DTH** [repo], there's **PGP** — you know what PGP is? — **GPG** is used whenever you [encrypt] an email's description, or communicate between software — we call it **GNU Privacy Guard** — we use it. Then a **Bitcoin** [repo] — open it… "hello world public" — a small program, **import Java** — nothing much. Then this — a **"minus-script"**-type thing — I click — what does it show: *"Paytm worker ID password @ meaningful port…"* — something something… let's leave it — but about the **email**, we got something on this — open it: in the **PGP** repo you'll see what a **public key** looks like — a public key for something — inside it you may find **hidden information*** — or a key for some access — **any public key** may be sitting there. Since this is a GPG [key], it could relate to email encryption — anything. So: click **Raw**, copy it, save it into a file — `public.key` — saved. Then the command — the command is **gpg** — and **`--import`** — I imported the public key — and HERE, look, in the imported key's details you **see the email ID** — which is what we wanted for the question — **select** it.

Question: **"What is the full email address?"** — the email address he used — **submit** ✔.

Next: **"What is the attacker's full real name?"** — the real name — you know — we already got it — submit ✔ — the full real name — paste it. THAT many questions are solved for us.

## Task 3 — the GitHub audit trail (info that was edited/removed)

Next we push on:

> *"The cyber-criminal is aware that we are onto them — investigating their GitHub account…"*

While investigating the GitHub account we saw certain indicators — we observed some things related to the account owner — where I showed you information related to **editing and deleting**. So as it's written here — read it gently, take your time:

> *"On some platforms, [revision/audit history is] available; this audit history allows investigators to locate information that was once included — possibly by mistake or oversight — and then removed by the user [before] investigation… In order to transfer [further] you will need to perform a deeper dive into the hacker's GitHub account for any additional information that may have been altered or removed. You can utilise this information to address some of the attacker's [cryptocurrency]."*

The questions:

- **"What is the attacker's [crypto]wallet address?"**
- **"What mining pool did the attacker receive payment from, on January 23rd [20]21?"**

Look — you must have got a hint here — the name **Bitcoin**… if I search it — "price today…" — that kind of related information. The PGP work is done; this tab is open; this tab is open… and **Bitcoin** — I told you to open it — let's open the Bitcoin one in a new page — we opened the Bitcoin one: here also — is there any such information visible? [Music] Look, you have to see… let me — some information — Ctrl… let me show you what information can appear here: the **address** — "what mining pool"…

Now — many times websites [help you]: if you have some ID — any **transaction ID** — you can view the transaction. Why would we skip trying? Let's open the website — which website do we open? [opens an **Ethereum/blockchain explorer**] — *"No user was found with this email"* — okay — email and password… hmm — even so this isn't working… alright, open [this other one] — okay — look: **this one worked now** — and its **date** — you'll see here — open — transfer — look — **"from this ID it went out — this much value — and what token"** — and then — the translation… What was our question? [checks] — okay, the spelling is wrong [in my answer]… this can't be… okay yes yes yes — information with using [it]…

**Whatever I have had you do so far** — nothing is "outside the village" 🙂 — everything: just find it out. What I'm doing is the same thing — no unavailable [tool] used — only that information gathering — on this basis I'm trying to answer these questions — nothing different.

# Homework + course admin

Got bored? Tell me — got bored? Why, Prince — tell me… *"gathering information about them after their…"* — look — what happened: the cyber-criminal realised we're onto him — that we gather information about him — and **after the attack, he used a different username** — he switched his Twitter account to a different name! Obviously — the Twitter account they used after the attack is a different scenario, right? — "I don't see what you are doing back home" [bio quip] — he did that after attacking… and a message… okay okay — the target's [new] Twitter account — where is it — here it is — **THIS is that [new] Twitter account** — and in it, quite a lot of information will be visible to you.

Now what will we do: the way I made you do information gathering on Twitter over **three days** within [that much] time — **now it's time for YOU** — it's your time now. You have to **read ALL these posts, these tweets, understand these tweets** — what is he saying in this tweet — and gather each [fact] — your job is to gather the information I need, **which will give you answers to the coming questions**:

- the **Twitter account** (complete OSINT on it — every post, every picture you find — use **image reverse**, use **Twitter's advanced techniques** — the ones I taught);
- **geo-locate** him — from the information you keep digging — geo-locate him!

This is your task. And prepare a **good report before the next class** — and you should have the **answers to those questions** (wallet address; the mining pool on the given date). I don't know how [you'll get them] — I WILL show how those answers come, in the comment section, next [class].

Look — in front of you, EVERYTHING about the target is lying around — and what a **demo target** it is — packed with information. In a real-life scenario, if you target someone like this, you'll **never** see this much information. Everyone — whoever is watching the recording, even a year later: **this is a permanent thing** — its pattern won't change; maybe Twitter will update, **but these techniques will remain roughly the same.** So tell me — everyone can do it, right? Of those watching the recording later — I can expect it too: even if they watch it a year later, they'll come to our page and tell us by liking and commenting. Tell me — total eleven people here — how many will take the Twitter account [task]? …You can't comment there? Tell me… Okay — **two people said** — Prince and one more — "we will do it" — other than these two…? **Only three peoples are volunteering** to give answers, complete the task. Apart from these three, is nobody interested that "I will do this task"?… not doing it… 

In the **next class** I will teach — our series is going to run quite long — and don't worry: I don't actually think you'll have doubts, because I've told everyone in quite detail — and whatever type [of thing], it's **my guarantee** — this OSINT, the complete course, free, which people charge quite big amounts for — I'm making it **freely available for everyone**, distributing it, and distributing it in quite detail. More topics are coming in the future which will also be freely available.

Before that it was important to show you **how the thing comes into use** — how you'd do OSINT on any target — on any such "live" target. You saw: here I was guided step by step — but this is what YOU had to do, information gathering. Because I have the idea — I've been teaching you for quite a while — so I know which hint is where, which information is right, which could be wrong — that's why I could do it fast — but it's YOUR job: how far you can involve yourselves, how much you can participate. This [room] is **free**, no paid lab — even create an account on TryHackMe, join this [room], and simply start performing its tasks — you'll have fun AND you'll get to use whatever you've learned.

Till now you were saying: *"sir, you people have stopped us… on Paytm or Facebook — companies you show us live — you stopped us from [practising] those; you can [only] do educational…"* — so **Task no. 5 & 6** — I'll do in the next class! Besides that, we go towards **one more excellent, beautiful, slightly-hard OSINT lab** — quite interesting, quite fun — after that some interesting topics — and then we think about winding the course down — thinking of ending the session that's long now. **Don't worry** — a lot of you have the request coming — you'll get everything — whatever comes, it will come in such a way that you never have to pay money for it.

I believe none of you has any doubt — so I'll [end the session here]…

