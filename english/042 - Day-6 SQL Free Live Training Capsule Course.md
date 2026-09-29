# English Translation — 042 — Day 6: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/042 - Day-6 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation; moderate ASR garble restored where intent is clear, flagged **[?]** otherwise. ("आइसक्रीम जंक्शन" = *injection*; "परसों वन/टू" = the demo tables *person1/person2*; "फर्स्ट लेवल" ≈ *first table*.)

---

## Opening — short but important

*[music]* So hello guys — I'm back again with a question — our SQL one — it may be a little small, meaning — if I tell it, you shouldn't forget the concept — that's why it's small — but it's important for us to understand it, because it can come useful for you in very many places — because it's found inside *injection* — it keeps coming, if you look. So for this, today's class could be small — but it's an important class — not necessary it's a 1-hour one.

And also — yesterday I forgot to tell some commands of ours. *[music]* So today we'll finish those commands. OK.

## SET operators — what and why (with the injection hook)

So — what do **SET operators** do? What they do: two or more — can be from different tables — they **combine** them and bring a **single result**. Basically — the queries of two different tables — it brings them into a single result. OK?

What's it called for us — suppose — in our websites and such: on **one command** you're able to inject — meaning, at one single place you're able to inject — but at the injection you have to see commands such that **along with your table, you can affect the rest of the tables too** — so that everyone's data-entry keeps happening for you *[i.e., data from other tables pours out]*. OK? So that thing becomes necessary for us to do. In this affair we'll see SET [operators] a bit more nicely.

We have **four** types of operators. So among the four, first comes our **UNION operator**. What the UNION operator does: suppose we have two tables — **leaving aside the duplicate records of the two tables, all the remaining records** — it'll show both tables' records — but **duplicate records it'll show only once** — it won't repeat them. UNION ALL — the operator — what it does: for now we'll tell with 2 tables — you can apply more-than-two too. If you people try [with more than two] and get stuck — tell me — I'll definitely do its solution inside our Telegram channel — and you can join the technical channels too from the description.

So: **UNION [ALL]** — it'll print **all records** — whether duplicate or not — it doesn't care. So it'll show records from both tables. Not that — first table's records it'll show — and alongside — if inside the first table some second table — removing those — only first — only the records of the first table — only belonging to the first — only those it'll show *[that's MINUS — previewed]*. OK? And the **INTERSECT** operator — it'll show us **only the common records**. Right now we'll also do practical representation in front of you.

## Demo setup — two tables, engineered overlap

From the tables we'll make these *[person1, person2]* — now we'll set data — one set — so don't take much tension for it. Using the UNION operator — before that let's set a separate table — so we can create the situation — like inside the situation we can show our thing in peace. So to create that situation, first of all — let me connect. *[music]*

OK — this table — *cricketer*? *[ASR — typing the CREATE]* — I have to pat the values here — so please — those who haven't seen the last sessions — go watch the sessions — then these people will understand things, all. OK — so the insert got done — and nothing more. Here — if you press **Control-C**, this will shut off — don't forget — it'll be visible. OK?

Here I put *person-two* — one-two-three-four-five — five data — I'll put in that too — so I can give you proper emotion *[intuition]* about what happens — the chart I told you — what-all they're doing — three of it — let me take from here. *[music]*

"Bada maan jayegi" — "we should learn the video in Hindi — have to watch the video inside Facebook — write the command for me and give" *[chat requests]* — "from the **person1 table** I want all-all data — what data is there — so please write me the command so I can write here" — "the command — the table from — SD? — tell" — I gave this in the *vikas*? *[ASR]* — tell, man — **`SELECT * FROM`** — here the table — first table — "what's happening to me today, I don't know" — *person-one*, *person-two*. OK?

## UNION — all records, duplicates once

So first — this — look — inside this it gave a **lottery** *[? — sorted output]* — meaning — like we'd used the ORDER BY command — inside this **by itself it gave us ordering**. OK? So don't think that "how is this output coming — it must be up-down." So look — they were here. OK. So in this affair — the repeated one — it showed **once** only.

So after UNION our next comes our **UNION ALL** — and it'll show **all records** — like the name, like the work. So now if I write UNION ALL here — then — it was showing repeat data. OK?

## Company parable — why these exist

This works **mainly on common columns**, man — look: suppose a company's **employee table** is distributed — OK — and a company's **manager table** is distributed. Now if you look — a manager *is* an employee — so he'll come inside the employee table too — and that manager will come in his table too — so **in both tables the records stay**. But we have to see records like — "which people haven't signed in *[? — which people exist anywhere, deduplicated]*" — so in that case we can use **UNION**. Or — from both tables — want to see everything — then we can use **UNION ALL**.

"I should check chat" — brother, I see the whole chat — the thing that reaches you from here — that just gets delayed a bit. So don't think that much — for me it's visible — it's not like — I've delivered here and you see it after seconds — so OK. To see everything — and repeat — look — nothing — however it stays — it'll show it only single-time. OK — this record — these both tables — this table-one, this table-two. These repeated records won't be shown to us — the repeat-data it'll show once only — and our 2 data was repeating — 2 from the first table and 2 from the second — this was ours for checking — it just showed it once.

About UNION: **UNION ALL shows everything; UNION only doesn't show repeated data — shows it once only.** Should be understandable — on my saying — let me open both tables again: `SELECT * FROM person1 …`

## MINUS — only what the first table owns

MINUS — OK — the second table's [rows] were repeating — so the **MINUS operator** — what it's doing: the first table — it shows fully — **but from the first table it shows only that data which is *latest-only* inside the first table** — inside the second table, the data that's repeated from the first table — that data it's **not** showing here. Let me repeat once more: what MINUS is doing — it shows us records from the first table — **but the second table's records which are also repeating inside the first table — removing those it shows** — meaning **only that unique-unique it'll show in front of us**. I have to recommend *[?]* — understood or not — first semester?

## INTERSECT — only the commons

Now we have one more kid: **INTERSECT** — our operator — that shows us — from both tables — only what's **common** — only that. I'll show you only-common-records_once *[?]*. The rest — from both tables — records show *[elsewhere]*. OK — the data that's repeating — it'll show it only once.

**Recap** — the UNION ALL operator shows everything — repeating, not repeating — it absolutely doesn't care. OK. [MINUS]: shows records from the first table — but the records of ours that are inside the second table too — it removes those records — only that record it'll dedicate which **belongs to our first table**. The INTERSECT operator — what it'll do — did it make sense — OK — any question on these four operators — come on — nobody?

## IS NULL — finding the unfilled cells

So — look now — here — one data — in null — if I want something like: "the one inside which the **phone number is empty** — bring me their rate *[records]*." If we see a real-life example: when we request someone — "what — you haven't kept this data — playing — your **KYC** isn't complete" — or if you — your letter-pad-based — to someone — "your this isn't done — that isn't done — put your address — put this — put payment details" — so in its nishaan *[tracks]* we — from our tables — check: "the guy — what hasn't he fooled *[filled]* — has he left something **null**?" So — that — to see that — what do we do — we have to put one small command here: what column I have to see — so look — here **phone was null** — I want that data — so look — this "P" data of ours came. OK? Where hasn't our data been filled — this small table — when there are **big-big tables, there this can come in handy**. It just checks: where is the value null — [in] the column's data.

## clear screen

And look — if — suppose — you people have to **clean** all this that's written — like the thing needed for cleaning — inside this too there is — like yes — look — writing **clear screen** — all-all simple-*saral* cleaned. Look — if I dirty it a bit like this — have to clean it — the whole screen will get clear — meaning shut off. I had time left — so I thought — let me just do it — so in this river *[?]* I've done it or not — look.

## Why the class stayed small

I kept it small because — man — because the concept **after** this is a slightly **heavy concept**. OK? It's not that we did nothing — we don't just have to finish the days — like "finish fast for me" — nothing like that at all. We'll take things calmly — because we have to understand things all the way inside — everything deep — I can finish it while doing-doing-doing — but I'm not wanting to finish it that way — meaning — **understanding matters**. Look — making sense matters — anybody can complete a course for you — look inside college itself: our — live behind — standing in front there, the course has to be dumped *[finished]* — so he dumps it and moves ahead. But here — even the sim *[?]* — absolutely not — here **you should understand** — and you — how it's walking, how the thing works — that thing making sense to you — **all your doubts should get solved — there we focus more**. OK?

## Task + tomorrow's warning

So what's your task for today? Did you understand these set operators — how they work — tell me — you can pin it *[?]*. So like — this one — didn't understand — what it is — so I'll guide you there — you'll get the solution — "if you type me *[tag]*, you'll get it fast." How you'll do the solution — you have to show me in front here — with the screenshot — go in your Chrome — whatever browser — see — whose account hasn't waited *[? — who hasn't posted]* — because recently I haven't done much-jyada for this — go in the **comments** — and after going in comments — what we'll say in the task — like — "you know — doctor and such — **try with more than 2 tables**" — so you try and send me there. In the **discussion** you can put it — man — look, I've seen — on our Telegram channel it is there — but that discussion — those people can't join — you people stay with the **community** — they'll stay for helping — so you can take help there too. So all the links — you'll get all links in this video's — any video's — **description** — however many there are. So go there and join.

Thank you — ta-ta — bye-bye — see you — good night — shabba khair — and — Defronix keeps winning *[?]* — now we meet tomorrow — **tomorrow's season can be a bit heavy** — so please do come tomorrow for sure, man — coming after reversing *[revising]* the behind stuff — **but tomorrow we're going to do JOINS**. OK? — if possible read a bit about joints too and come — what happens — where it happens. OK?

---

### Translator's notes (garble / reconstructions of consequence)

- **Core content fully intact:** the four set operators and their exact duplicate semantics — **UNION** = both tables merged, duplicates **once** (and he notices the output arrived **self-sorted**, ORDER-BY-like, and warns not to misread that); **UNION ALL** = everything, duplicates included; **MINUS** = first-table-only rows (everything in table 1 not also present in table 2); **INTERSECT** = only rows common to both (once).
- **Motivation is explicitly offensive:** set operators are what lets a single injection point drag **other tables'** data out through one command — the UNION-based-injection teaser; full mechanics later.
- Demo scaffolding: two 5-row tables (person1/person2) with **2 deliberate common rows** ("this was ours for checking"); Ctrl+C warning for the SQL command window.
- **IS NULL** (`WHERE phone IS NULL`) taught via KYC/pending-details realism; **clear screen** shown as housekeeping.
- Task: try the operators **with more than 2 tables**, post in the LinkedIn post comments/discussion; Telegram + community links in the description.
- **Tomorrow announced: JOINS — heavy; revise + pre-read.**
- The employee/manager parable is the canonical "records living in both tables" picture; ASR wobble around "signed in" marked **[?]**.
