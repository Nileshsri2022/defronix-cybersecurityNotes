# English Translation — 043 — Day 7: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/043 - Day-7 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation; live-demo ASR garble (student/course names, salary–fee numbers) restored where intent is clear, flagged **[?]** otherwise. Numeric demo values are approximate (the transcript wobbles on exact figures).

---

## Opening — the heavy one

*[music]* Hello — brother — language — so today's session could be a big one, meaning — even when *I* had studied this topic — that whole TV-topic *[?]* — it's a kind of "conjuring" topic *[feels spooky/confusing at first]*. That's why I'd released yesterday's class quickly: "man — today's topic is the next one" — if I'd made yesterday grand with it, then today's too would've gone up-down — because both topics are similar-ish — but still, some things are different-different. OK.

So let's start: our *desh* — meaning — **JOIN** — it joins two tables by their — any **logical relationship** it's called — likewise we can come with two tables. So about that thing we'll know today, in a good way — what it is — what you people [get]. So first of all — OK — this one's a little important. OK — so "my sorry" we'll learn *[? — garbled phrase; likely "maafi/self-deprecating joke"]*.

## Setup — the course table (with fictional fees)

So — `CREATE TABLE course` we make. Won't write a big-big name — *nyu*? — I'll put this into my tables. OK — this message I'm telling you: **these fees are not real** — I'm just telling here — nothing else. Here I'll write **SQL**. OK — and here if it gets too big *[music]*. OK — the student's *[music]*.

OK — so the table's made now — 6th January — and one more — Vishal — pranam to them *[greeting latecomers — music]*. "Employee it is?" — no — right now it's **student**. OK.

You'd applied the equals-to operator and such. OK? When joining **two columns — two tables** — whatever the column's field-build is — everything should be the *same* *[datatypes]*. So look — I'll do a stunt with these two tables. First look: inside this — our **course_id** that was — was an integer — here it's course_id which we've taken in our end. So — if its rate is same — so with these I can see whatever — "oh ho — good thing — if I like money — I like money very much" *[his businessman persona continues — music]*.

## Equijoin (WHERE-style inner join)

So here I'll write the name — course_id — student table — meaning what's the scene? OK? So look: `SELECT * FROM student` — and `course` I put here — so what's the meaning of this — "select — show everything of ours — from within student-of-course — **where from the student table our course_id — its course_id — should match with the course's course_id**."

So look — what-all is here: the *games* one's *tan* was *[?]* — OK — this one too — it took out its course too and showed alongside: **networking** — this one's again our three — here 500 — so here 20 came — here Mohammad Kaif brother's **Python** — then 3000 — then the 30's **25000** — in place of it too it got written — so it repeats there for you. OK?

But — it's become like this — but you can notice one thing inside it: **the 106 one of ours — Ayush-hai's *[a student]* — had put *edit* there — meaning — no course by that number exists here at all** *[his course_id = 40, no such course]*. So in this affair, the output isn't shown either — because when there's no code that's right — this condition of ours — this condition will [fail]. Let me take out my pen: this is our **student table** — whose code-*sadi* is written here — that should match — there the output should show. OK? Its course here — per its matching here — this table's output is getting shown. OK?

Yes — "it won't lift the message" — you're saying right. So this became our **equation** *[equijoin]*. OK.

## LEFT OUTER JOIN

The right one — what it'll do: it'll show the whole of the **right side's** table — and the left-common thing it'll show — that's ours — everything of the right will show — and from the left only-common — in both tables the output *[hold on — sequence]*. OK — so let's do it. OK. Come on — before [that], in the old video I show you a simple thing, man: what had you written ahead — this "course" is written — so — student — **however many times we keep adding conditions** — because look — we can apply our AND / OR conditions too — because we're using the **WHERE** operator — with where we can put anything — the condition stays like — as rubber-conditions ran *[?]*. So look — **every time we have to write `student.course_id = course.course_id` like this**. OK? If I want — man — however — to keep the table's name small — then for that what will I do — in front of the table's name I'll give a step-*ais* name **[alias]**. Meaning — student's — we'll tell like this: course → `c`. OK — her work's going *[?]*.

Now — in place of star — fan-copy-paste I do — so here what can I write — I want from **s**: `s.` — I want **name** here — **id** I want — commerce — `c.` — `c.name` I want — and `c.` — it's right — but [otherwise] one'd have to write "student" — so to save from that thing I've done this here. "It's looking good — straight — meaning it was showing twice — putting SELECT star — if I want" — no problem there.

"Nice — nice" — restaurant? *[garble]* — our **left-side table** — it's showing **all records of that table** — but **from the right table it shows only those records which are matching with the left-side table**. This I'd told you about **LEFT OUTER JOIN** — inside the side — the same thing is happening here: the left table — all are shown here. OK — but the right — this table — **only that many records** shown — as many records as are matching with this. If I — look here — inside this — there's a "15EM" one of ours — the "54-saadi" one was *[? — demo values]* — it didn't show here — because this is LEFT OUTER JOIN we're using inside. So inside left-outer — ours this stays: **show all of its records, and from the bright *[right]* table show ONLY matching records** — just this is its work. OK?

## RIGHT OUTER JOIN

Now we go to the right side — in place of "on one" **[ON?]** — OK — writing ON like this it stays. OK — so keep watching those things too from your side — what's running, what's happening. Here — the left table should show? — if — by the right table's account — by the red table's sequence's account — the left table's output is coming — that too you people will understand a bit fear-fully *[?]*. The left one — our right one's — it shows its **full-full data** here. OK? Showing all records — the ones not-matching from right — from left not-matching — I've made a bit too many boxes here *[drawing]* — the records inside the right table that aren't matching from the left — this **50-record isn't matching from our left** — **still it's been shown here**. And the right one inside which was 106 — that brother's — on which 40 was written as course-id — **that wasn't in our course table at all** — so that record doesn't start here — because it wasn't in matching with this. OK? "Not matching — makes no difference" — meaning — per this table's work's account — about showing the table's records — did everyone understand or not — tell me — then I move ahead.

## CROSS JOIN — the accidental explosion

Ahead ours — **CROSS JOIN** also exists; "idhar join" **[INNER]** also exists; **SELF JOIN** also exists. Right now the first simple-liquid join I told you — till now we've balanced *[covered]* — did it make sense or not — in two-three ways it should make sense — very necessary. Come on — fine, no problem — moving on.

Check this — or some such *conditioner* goes *[?]* — in that case our **CROSS JOIN** happens. OK? How does it look — like: `SELECT * FROM student, course` — if here — *kar-dan*? — and in the second one how many records were there — *kar* records — **this many records it showed us** — you can see: how a program's mistake looks. And one more way here too I can write. So this — this — *tabiyat* — our husband will be *[?]* — this problem will be — "from the table, some conditions are to be met inside our own table and shown in front" — meaning — from one column into the second column, meeting a condition and showing — for that case also we have **SELF JOIN**.

## SELF JOIN — who is whose manager

What happens: if some company has some employee — meaning like — if you're a manager in some company — then if you look — you're also that company's **employee** — so meaning you'll come inside the employee table too — inside that table this stays written too: **who is your manager**. OK? So what'll happen inside this case: inside **one same table** the manager's listing stays — and inside one same table — in front of our employee's success *[? — name]* — the **manager's ID** also stays written. OK — so who is whose manager — that's written for us inside one same table — but we want it **with their names**: "man — this is his matter — who is whose manager" — how'll that be — that — we do with **SELF JOIN** — because inside our same table there are such records which we have to get checked with each other — like getting the **manager checked from the employees** — because the manager too is ours — employer-table.

About **crossing**, brother *[clarifying CROSS]* — nothing — they happen by a **mistake**, or in the affair of giving bad conditions — you gave a condition that's **always true** — meaning here we gave some condition — a *zero* condition *[?]* — that's always true — **or you forgot to give the condition** — in that case your CROSS JOIN happens. OK? Inside CROSS JOIN, **everything gets shown meeting each other**: this equal-to this; this equal-to that; his record; her record; from that this record; this record. So in the affair of showing everything meeting each other — ours becomes **M × N**. M is one table of ours; N is the second table. OK? So meaning — inside one table there are 6 records of ours; inside the second if we have — *kar* records — then 6 × 4 — **24** — records will get shown to us. OK?

So when we make our **employee table** — I'll band this *[?]* — and with them we do one more work — and one more — "no, man — our Vishal brother is — sex-brother — whose manager he is not — emp_id = 2" *[demo row names]* — different-different table — the table's manager — let me write it properly. OK — so this — the reverse-pan was coming to read *[ASR noise]*. Then next — our **Rohit brother's manager is our Vishal**; **Ayush's — our maj-re — Rohit** *[demo hierarchy]*. Vishal — we can take out — earlier likewise — meaning — inside left's earlier — the manager — did you understand in the last lecture or not — tell me, man — did it make sense, or not — come right now. OK.

## INNER JOIN recap + the relationship question

"Student — course_id" written — OK — inside this what to say — all records shown here for us — OK — because look — what's an outline — inside the left-outer-ring what happens: left's all records shown — from right, not-matching ones shown *[?]* — inside red — right's side-records shown — left's matching ones shown — matching happening — still shown; not happening — still shown — but what it's doing: **it shows only those records which match — the records not matching — those records it doesn't show**.

OK — so what did this one do — the records that were matching — only those records it showed — this work happens of ours — it'll show **both tables** — the records matching — beyond that — did everyone understand or not — tell me, man — did it make sense or did it make sense. OK?

So for that what command do I write — quick, tell me — here I'd told you — the people who've been here from before — come on — nobody's telling — so I'll write here myself: you — table — I'll make on table — so in that case — **between these two I'll have to make a relationship** — which is our **RDBMS** — it used to work *[that's the R in RDBMS]*.

## FOREIGN KEY — wiring the relationship live

So first of all there was the **course table**. Now look — I'll make an entry — the network one — our part — inside this — this course should be — this gets **connected** with our course table's **course_id** — so that **whenever anybody enters data inside this** — and enters the course_id — **it goes straight into the course table and checks**: "what, re — does this course_id **already exist** or not?" If it doesn't exist-adjust — then **it won't let the course's entry happen**. OK? So let's do it and see once.

Course setting — put here. OK? Now look — for this, what's the most important thing: **both should have the same data type**. So the course_id that's inside our student — its rate and size is default — and the one that's in our course — so inside that — come on — after that we do. So I — the Bharat-idea thing *[?]* — I want to meet the **course-id thing of the ports **[course]** table with the force-id** *[foreign key]* — so here I'll write — the **reference table** — the one from which I want meeting — so I want the meeting **with that table's course_id**. Look — **not necessary that here the column's name be the same** — with our second table's column's name — not necessary at all — **both's data types should be same**. OK? Of this thing keep a bit of proper care. "Tell the spelling — where's the mistake" — so we can solve from there. OK?

So right now I've **met this table with this**. Now the data that was of this — of the name — let me try: the **20 one — this too had gone away** — and our `SELECT * FROM course` — inside this table the course is totally *badiya* — after that too — it'd been done. So you — meaning along with going — this too see: **that table is connect to which — that column inside — with whom it's connected** — then open that table and see — that table I opened and saw — "man — this is trying to put — the sala here *[laughs]*" — so in this case **this 40-data it will simply not put**. OK?

## Task + help channels

So — **this is your task for today**: after doing the task you have to go on Chrome — go inside the post — like here Day-2's is put — Day-3's is too — likewise here Day-7's will also come. So inside it you have to **do and show** — take the screenshot and send it — "what — meaning — you've done fancy integrity nicely" — and alongside I've also done that — what's the name — **with more-than-two tables also I've used the JOIN** — so you do these two things and take the scanner-stranger *[screenshot]* and send it. OK? If you get an error — we're definitely sitting here — whatever the links are — you'll get all of them — the YouTube video running right now — live — inside this live video too — here too our Instagram *[etc.]*.

OK — today you'll have to do the first *[?]* — please — meaning those who haven't seen the first session — that — meaning — join first — so you get the thing. So you'll stay under this life? *[?]* — there coming — whatever queries are there right now, you can see them. OK — do join this channel — and after joining, join its discussion too — somewhere it shows — so in the **discussion** you can put your troubles — I'll "decide" those *[address them]* — otherwise in the next day's lecture we'll definitely try finishing it. OK — it's going to get a bit more heavy — meaning — fairly more heavy things we'll band ahead — totally doing — that very thing. So — just for today — *[end]*

---

### Translator's notes (garble / reconstructions of consequence)

- **Join coverage in this class (all live on `student` ↔ `course`, joined on `course_id`):** ① **equijoin/INNER** in both spellings — the old `WHERE s.course_id = c.course_id` form and the `INNER JOIN … ON` form (matches only); ② **LEFT OUTER JOIN** (all left rows; right only matches — non-matches show empty); ③ **RIGHT OUTER JOIN** (mirror — the studentless "50" course still appears; the student's bogus **40** course_id row vanishes); ④ **CROSS JOIN** = the mistake-join — missing/always-true condition ⇒ **M × N** rows (6 × 4 = 24) — "this is what a program's mistake looks like"; ⑤ **SELF JOIN** = table joined to itself — the canonical **employee-with-manager_id** hierarchy (who is whose manager, with names, via two aliases).
- **Table aliases** (`student s`, `course c`) taught as the typist's relief from `student.course_id = course.course_id`.
- **The relationship is then made real:** a **FOREIGN KEY** on `student.course_id` → `REFERENCES course(course_id)`; the two linked columns need **matching data types, not matching names**; after wiring, the bogus **40** entry is *refused* at insert-time (the 20-row had already gone) — Day 2's "insert-time check" finally executed.
- Tasks: do the joins + the FK wiring; screenshots into the **Day-7 LinkedIn post**; stretch goal: **JOIN more than two tables**; errors → discussion channel/Telegram (links in every video description). Tomorrow: heavier still.
- Demo-value wobble (fees 500/1500/3000/25000, ids 106/40/50/20, names Ayush/Vishal/Rohit) is inherent to the ASR and flagged, not authoritative.
