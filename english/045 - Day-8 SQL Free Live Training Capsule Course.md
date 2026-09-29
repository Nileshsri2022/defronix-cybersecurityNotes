# English Translation — 045 — Day 8: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/045 - Day-8 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation; live-demo ASR garble (salary figures 95000/98000/94000/90000/85000/80000/60000, course ids 50, names) restored where intent is clear, flagged **[?]** otherwise. Demo numbers wobble in the ASR and are approximate.

---

## Opening — keep full concentration today

*[music — "khuda" fragment — music]*

So hello guys — I've come back again with our [session] — our **SQL** one. So look — today's topic is a bit **important** and will also feel a bit **hard** to you. So in today's session you have to keep your **concentration fully built** — right on this side *[on screen]*. OK. Instead of trying to struggle through things yourselves, today you should just **watch this session** — because it'll also feel a bit interesting — if a question didn't come into your minds like "**how does this thing work** — that thing — meaning — how do we do this, how do we do that" — then if it *did* come, today you'll get the **solutions** too. OK.

So let's go — today's topic — I'll review it later — first let's talk about the **problems you people faced**. OK?

## The first problem — the name with the max salary (enter the subquery)

"One *[? — 'maximum']* salary — I can extract it — how? With SELECT — **but if I write the name too along here, it won't work**. OK? So still — its name — how do we **bring the name** here? That's our *[? — 'general']* one — so that **term** is called our — what is it? — a **subquery** *[the ASR dropped the word; the day's whole topic]*. So — on the **base of the result** we write the **upper query** — and after **WHERE** it works on the base of that *[inner result]*. OK? It's written **inside the clause**. OK?

So our question was: "yaar — **of the maximum-salary person I want the name** — the details" — so: **salary equals-to SELECT MAX(salary) FROM** — everything — that **employees** table with salary — when this one's result comes, then here the salary — you can do that, you people.

Now — "if we want the **detail of the max one** *[ASR: 'क्लास परिसर वाले का' — 'of the class-campus one' — garbled]*, then what'll we do?" — "we had nothing here of that sort by which we could extract it" — so for this we'll do this: **we'll write one query — OK? — and inside it there'll be one more query** — so the one that **returns the value here** — I'll try to explain slowly-slowly. OK? So please — this is how it is — so it was showing us the output of **95000** — it happens — how to say — whenever some *[reason?]* happens, then it'll get written here — I wrote 94 *[94000?]* here — "what's written will come here" — "what thing is this — which one — you said the name — this wasn't — these days — some things you'll surely understand — it'll go over the top *[? — 'it'll click from the top down']*".

## The classic — the SECOND-highest salary

"I want the **name of the person with the second-highest salary** — of those whose salary is **less than 95000** — salary less than 98000 *[ASR wobble]* — among them what's the **maximum** — show here." But yaar — **how would we even know 95000?** Because when we made the table — we don't put the values — we just make the table — putting values in we do in programming — programming or whatever development we do — inside that we input the values. OK? So you put 19 *[?]* — meaning — if you made it for some company and that company's owner *[sets]* ₹1 lakh — out of all — the **maximum-finding query** — what'll it do — it'll extract **95000** for me — and then **after that this big query** will extract **9000** *[90000]* for us. After showing this — `SELECT *` *[the full-row version]* — we can execute it like this and see — that's why I keep asking again and again — we'll go a bit **deep** today. OK? Very good. So — let's move ahead.

## Interlude — Paras-bhai's LEFT OUTER revision

Yes — Paras-bhai — every session of mine — "please will you explain to me once — what our **LEFT OUTER** is" — meaning — sort of for **revision** — I have to repeat yesterday's — the answer to my question is coming — "do you know LEFT OUTER — what it does — waiting-for-reply chat *[?]*" — **it'll show ALL the records of the LEFT table — plus the matching records** — "yaar — really — love you — I love you — feels good when you do *[ask]*" — OK — Mohammad Paras-bhai has left — meaning — look yaar — who all are there — there are these people who talk **so much** in the group — but in real life do nothing. *[teacher's teasing]*

## One output vs many outputs — ANY and ALL

A **function** of ours gives you **one output** *[ASR: 'login']* — OK — so suppose we have **multiple outputs** — in that case — if we have to *[ASR: 'सफेद रंग'/'white colour' — garbled; 'compare']* — then we call it the **multiple-rows case**. OK?

So — first of all let me — sorry — sorry — from this — if any result comes inside it — **ANY** — what'll it do — our 19/95/90 *[the demo values again]* — what it'll do — look — these are our values — **multiple values** — "do-kar one — carry-on-karke" *[? — 'we could've pulled it with a straight query']* — but that gets done instantly — I've shown it to you like this. OK. So this took a **list** — inside it lie multiple values — **if salary's value is greater than ANY ONE of these values** — then its — 95000 is written somewhere in it — it'll give me here — look — **all these values are bigger than 85000** — and if I write **95000** here — OK? — then it **won't give** anything — because it's not bigger than it — *[no row's salary exceeds the max itself]*.

But now understand the **concept** — how **ANY** works: any — meaning — **if our value — the salary's — is bigger than ANY ONE value from these — it brings the output**. That's ANY's work — it works like this. OK. So look — however many values we have — from those values it'll check with **any one value** — "salary" *[?]* — greater, smaller — or whatever we give here — it'll check it. It's going a little hard, or whatever — tell me if you understood or not — otherwise I'll try to explain it finer — maybe I'm not explaining well — or you're not getting it — tell me in this thing.

"With any **one** of them — if we give a *[Jay Samand? — garbled name]* condition — give a **logical condition** — accordingly — from with any-one value it checks that logical condition — and accordingly whatever output comes — brings it for us here." I can tell you just this much: what ANY does — there are values — **from any one of those values it'll try the logical operation**. *[music]*

OK — look — alright — listening? — ANY's work: **from the list of values — from every/any value** — if an output comes — it brings the output for us. This here is simple — the simplest example I can explain: however many values ANY has — from any one of them — if our logical operation's output comes — it brings your output. Logical operations — I've told you — these ones are the logical operations *(>, <, = …)*. OK.

But — like we did `salary EQUALS-TO` — earlier with equals we only got the chance to write **one value** — 95, 2018, ₹1 lakh *[wobble]* — whereas here it should bring [it against] any value — so if 10000's output isn't there — doesn't matter — it just won't give us output — that's it. **ANY — after it, whatever values there are — it goes and checks with EACH value and gives the output** — and we can put **multiple** in it — we can also understand it this way. OK.

**ALL:** now look — I did in salary — greater — it brings the whole *[list]* — checks among all those values — **if some salary is bigger than ALL the values — then output** — otherwise it won't bring it at all. If I do it — it'll bring the value here — here brother — values smaller than both 98[000] and 95000 — which are they — **80000, 80000 and 60000** — these are our values — so "smaller than both?" — here it'll check: brother — **from either one of the two if our value is bigger** — wait no *[self-correction]* — **it must be bigger than BOTH** — brother — the values we've given here — out of ALL those values — if some value is bigger — we've given the sign *[>]* — so if any value is bigger **than them all** — then bring it. OK — now it must be fully clear to you.

## EXISTS — courses with (and without) students

Our — the *address-wala* one's result it'll bring *[? — transition garble]* — we'll understand this with the **example** — you'll understand better. So first — SELECT. OK.

So our question is like this: yaar — **in WHICH courses are students enrolled** — to see that — every child's *[record]* — OK? BUT — some courses are also such — meaning — some are also such **inside which no child is enrolled at all** — so how do we bring that result? For that — for that the **EXISTS**-wala one will work. Let me explain.

In our course table there's **course_id**, right. Now — when I run this command simply just-like-this — what'll happen — tell fast — which join's *ghamand* is this *[ASR: 'कौन से जॉइन की घमंड है' — likely 'command hai' garbled]* — come on — nobody's came — *[...]* — I only — but it's somewhere — our 50 didn't come — the **output of this command will be this**. OK. Meaning — I — a bit below — the record's output — look here — **the record inside it didn't come** — for us — what's happening in the game of **EXISTS**: from the command you put here — from this command — **whichever course's record shows to us** — that's what shows. OK? So here — if no output comes — nothing comes — **but if a record shows here — then the output comes — from the [outer] table**. But think about it once — maybe right now you won't understand it. OK.

**NOT EXISTS**: we'll write NOT EXISTS — brother — **the records whose output is NOT showing — bring those records here**. So — those not showing — bring the output of those records here. So in this — it worked — brother — in this one it wasn't — now in this one **50** is there — other than 50 the rest are there — so I brought them here. OK — this is our EXISTS — a bit — understanding-wise — maybe it got hard — **for me too — and for you people together** *[laughs]* — watch it **three times** if you — if you'll run the commands yourselves — I'd maybe told earlier in personal-message too — **if you try doing the thing yourself — build the logic yourselves — maybe you'll understand the things much better**. So this EXISTS is — meaning — it stays hard — if you watch you'll maybe understand well — it's not nothing— OK — write it down for now — so we can solve that thing.

## Close — task + tomorrow

Had understood *[?]* — what it does — you people have to run and see them. OK. Have to go on the company's page — have to go inside the **company post** *[LinkedIn task — the academy page post]*. OK. Likewise the **date** will also come here *[?]*. OK. So — the date coming — after that — yours — inside it — if you — if the date doesn't come here — till then you can also tell in **Telegram** — and if you have any trouble — ask. OK. So for today — just this much — and everything else you'll get in the **description**. So thank-you — so please — tomorrow everyone for giving *[?]* — so come on — ta-ta bye-bye — good night to all. *[end]*

---

### Translator's notes (garble / reconstructions of consequence)

- **The day's topic is the subquery family**: the word itself got eaten by the ASR ("उसे टर्म को मां बोलते हैं अपना क्या होता है" — "that term is called our — what is it"), but the entire session demonstrably teaches: ① single-value subquery in WHERE (`salary = (SELECT MAX(salary) …)`), ② **nested** subquery for the **second-highest salary** classic (`salary < (SELECT MAX…)` → `MAX` of those), ③ **`ANY`** (true if the comparison holds for **at least one** value of the subquery's list), ④ **`ALL`** (must hold against **every** value), ⑤ **`EXISTS` / `NOT EXISTS`** (outer row passes iff the inner query returns ≥1 / 0 rows) applied to **courses with no enrolled students**.
- Demo-value set (ASR-wobbly): salaries ~95000/94000/90000/85000/80000/80000/60000, ₹1-lakh company-owner hypothetical, course_id **50** as the "now it has students" pivot.
- The **Paras-bhai interlude** restates LEFT OUTER JOIN on demand: all left-table rows + the matching right-side ones.
- The "function gives one output… multiple outputs" bridge motivates why `= (subquery)` breaks with multiple rows and ANY/ALL exist.
- Close norms: run the commands yourself (builds logic), tasks via the academy's LinkedIn company post (date appears there), doubts → Telegram; everything else in the video description.
