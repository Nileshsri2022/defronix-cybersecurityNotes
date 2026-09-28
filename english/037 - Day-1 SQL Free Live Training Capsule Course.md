# English Translation — 037 — Day 1: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/037 - Day-1 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation. The transcript is auto-generated Hindi with heavy ASR garbling; restorations are marked **[?]** where uncertain, and filler/ASR noise ([संगीत] music tags, "अपन/अपुन" tics) is rendered as natural conversational English.

---

## Opening — mic trouble and a false start

*[music]* …OK, let's wait a little more. First of all, about SQL — we'll look at what SQL actually is. So first let's understand where SQL is even used — basically, we'll build everything from the ground up. So first, let's understand: what is **data**?

Data is nothing but the **raw form of information**. Meaning — data is how information exists before it's processed. You have information sitting around; whatever you actually need out of that raw form, you separate out, so that it becomes **useful information** for you…

Hello— *testing* — was my mic bad earlier? Tell me, how's my voice now? The mic — please, how does it sound? Earlier it wasn't this good maybe. I'll restart the whole thing from the top if needed — please tell me how the voice is. Last time there was some issue with the earphones, so I've changed some things now… Is it OK now?

…Give me two minutes, let me load a few things from the office side and check. Just wait two minutes. *[music]*

OK OK — if it's fine now, let's start the session once more, from the top. If you're all hearing "no problem," then fine, let's go. **Sorry for the interruption, everyone — I'm starting over.**

So — I'm **Hardik**; welcome back to another session of Defronix's capsule *[lit. "ice-cream" — ASR garble for "capsule"]*. Just like you (hopefully) liked the Python capsule, I've started another session — this one on SQL. And for this one too, I'll definitely need your reviews.

Let's begin.

## What is data?

First of all: **what is data?**

Data is the **raw form** of your information. Meaning — anything you have lying around, out of which you extract whatever informative thing you need so it can become useful — that's data. Anything that *matters* is data. Say, in your house there are lots of things lying around — but the things that are actually *useful to you*, those are what you'd call your "data." OK? So: information's raw form — that's the thing. OK.

## What is a Database Management System?

Now let's understand: what is a **Database Management System**?

Look — any **database**… imagine you've made a whole **bookshelf**, and on that shelf you've kept many books. That right there is your database. OK? But you can't just leave the books lying any old way on that shelf, can you? You have to **manage** it properly: OK, don't keep these books like this — keep them upright, or vertical, or horizontal — however. How should they be arranged? Suppose you want to arrange them **by author**; or arrange them in a **sequence** you've decided; or arrange everything **alphabetically**. You can do any of that. That's management — a management layer. Now if you build a **system** for this, it becomes a complete management system.

Like my book example: if you want to see a good books-management system somewhere — take a **library**. Inside a library, all the books are managed properly. Exactly like that, a **DBMS** exists: you've built a whole database, and on top of that data you build a system to manage it all — "this is how we'll manage all our data."

What was there before? In the old days there was no structured data — data was **stored inside files**. Then, whenever you wanted to access some data, what did you have to do? You had to go look through files, open files, then dig the needed information out of them and show it. And with lots of files there'd be lots of trouble: where do we keep the files, how do we keep them, in what arrangement — so many issues. OK.

## So what is SQL?

**SQL** — when you want to *mine* and *manage* that data, a **language** was created for it: "OK — the data is here; how do we work with the data?"

Now — the database management I just described: earlier it was done in files; that system was dropped, and things were redesigned in **tabular form**: inside a **table** there will be **columns**, and under the columns, **rows**. OK? Every column holds one kind of data; with every row, data can be **aggregated**: OK — this is one person; this is his roll number; this is his name; this is the phone number; he studies in this class. So you build a whole table-format structure — so that whenever you want to access anything… Look: when your college result comes out, it comes as a whole **table** — "where's my name? what's my name? find it" — and then you trace the whole line across. It even happened in *3 Idiots* — they start reading from the bottom. OK.

So you put your data in tabular form, and through that you can see things much better: the names are all written here, the roll numbers are all written here; it's arranged this way — arranged roll-number-wise, arranged name-wise — all of it.

So what does SQL do? SQL is a **language created to manage all these things**: OK — the data you want to pull out — how do you pull it? SQL's full form: **Structured Query Language**. It's a query language — meaning it *helps in a language* you run — the commands you learn and run, we call them **queries**. You run a query; then your data comes out of the table. OK?

## RDBMS — relational databases

This mostly happens inside **RDBMS**. What's RDBMS? **Relational Database Management System.**

Now — you built one table. Then a second table can exist too. When you **associate** one table with another — you've created a **relationship** between the two. Take two people: get them related — they become friends; now there's a relation between them. Sometimes it breaks too — that's another matter — but a relation it is. So relations exist everywhere — believe it or not, there *is* a relation.

Example: there's one table where you've listed all the **courses**. Now in your other table — say a students table — when someone enters a **course**, at insert-time the table will **check**: "this course being entered — is it in that old table we talked about, the one holding all the courses?" If it's in there, *then* it lets the data into itself. See — a relation got built between the two tables: OK — "this course thing will go into this table **only if** it exists in the old table first." That's what relations are.

So — this was about SQL, about data, about DBMS, about RDBMS. That's how data management is done today, or how it *should* be done — what's trending nowadays. RDBMS is the current thing; before it came plain DBMS; before that, the file-management system — and going back, except older systems again. All that's been set aside; RDBMS is what's trending today.

Within this, **we're not going too deep** — into **normalization** and such — First Normal Form, Second Normal Form… OK? We won't go that deep for now, because that would get too heavy for us. Right now we'll stay at this level: how things work, what's what, how it should be, what happens. OK.

## Instructor check-in

So first — everyone, tell me: whatever I've explained so far — is all of it making sense or not? Any trouble? Any mic trouble? Voice trouble? Am I talking too fast — what's going on? Tell me.

…"Understood, perfect" — OK.

Now tell me: those of you from CBSE — I was in CBSE myself — how many of you have studied this before? Who all have read about SQL before, played with data before? Speak up — so I get on record what you already know: "OK — these people know this much about SQL, this much about data" — so I know what level to teach at, or not.

…"Basics should come — start everything from zero. Though a little is known. Want to know how much the audience knows about this. No idea of SQL. A little bit —"

OK — "a little bit." We won't go "a *lot* further" for now… Actually — yes we will: **we'll take this till college level** in a very good way — don't you worry about that at all. In fact — do one thing: write down your college syllabus and send it over; I'll look at what's in it and what isn't. That's an option too. We'll see everything on Telegram — what all needs to be done.

## Installation (Windows)

OK — now we move to the next step: **installation**.

Look — those of you on Telegram: I sent a link to download. Did you download it or not? Write quickly in chat — have you downloaded it or not?

We'll learn on this. And look — SQL runs everywhere; small things differ up-or-down — every platform does its own improvisations. But we're starting from the **basics**, and *that* stays the same everywhere. Like in **Oracle** you'll find small differences — data types are a little different there; Oracle also has a nice **PL/SQL** feature in it. Meanwhile **MySQL** has the normal data types and so on… and *[ASR: "and Apple is used everywhere nowadays"]* — that bit's garbled; the point is MySQL is everywhere these days. *[?]* Anyway — Oracle's also good to learn for us. But the **queries** you run — those same queries run everywhere; no issue there. OK?

"The link didn't arrive" — I'll do one thing: drop the link in chat too. As for Telegram — I've been saying from the start: join our Telegram, join it — but you people don't join. All the links come only on Telegram. The Telegram link is in this video's **description** too — you'll find it there. So you can go to Telegram and download it. Apart from that, let me try dropping the link in chat right now if it's available.

…OK — I've dropped the link in chat just now. *[music]* But for now we can do this on only one platform — the one I think it should be on. OK, kids *[tone: affectionate]*.

So from there — tell me quickly how many downloaded it, then I'll tell you the next steps — what to do, what not to do.

Look — I'll show you the install. Many people were asking, "brother, find out about Oracle." So here's what we do — this will do for us right now: **Oracle Database 10g** *[ASR renders as "Oracle 10g"]* — that's the one to download. We double-click it here… *[music]*

"You're right, brother Mohammad Kaif *[a student]*" — or maybe change the description a bit — yes, look, it's come up here. So I **Next** it — you always have to **Accept** the terms; if you don't, nothing works — could anything? OK. So I'll go **next, next**; here it'll ask me for a **password** — everyone: whatever password you put in, **remember it**, because changing it later is a big pain — seriously. So be careful with the password. I'm putting in "electronic" this time *[trainer's actual pick]* — you'll remember yours, right? Write it down — that's enough. The link's also in the chat — download from there. Nothing else to it: next-next, fill the password, next-next, done.

*[music]*

"On Android?" — no brother, not on Android. On Android — we'll learn within the system; we're not doing the phone thing *[i.e., the Oracle install is for desktop]*. For Android too we'll look into it, but this install is — full Windows. OK? And Oracle 10g — you can also search it for Mac or whatever — if you find it, fine; I have no idea about it — I have Windows, so no idea about other OSes. Use the link I've provided as far as possible.

OK — now look: everything's done. Now if we check where Oracle 10g got downloaded/installed… did I put it in the channel's description or not…

## Connecting — Oracle SQL command line

So here you click the **Start** button — and in the apps you'll see the **Oracle SQL command line** — click that. After clicking, something like this will open in front of you *[console window]*. *[joking]* This isn't a stick, guys *[the console looks plain]* — it can't do anything for you. OK — then you put in your password; I'll also tell you what the ID — the username — is, and how exactly we connect.

"Will the system get slow?" — the system doesn't slow down in general… well actually — look, **at install time** many things run in the background: the SQL instance has to craft your **server** in the background of your PC. In the course of that it builds databases and things. So yes — you might feel it a bit slow **during the install**; but after the install, there won't be anything heavy. OK? And SQL has its own separate **port** anyway. So that's how we connect.

Now — how tables are made and all — we'll definitely see all that in the coming time. For today it's the installation — and this is how the install happens. Once installed, here's **your task for today**: do this installation on this window — the one I just did — you don't have to show your ID and password, that's fine — just show me that "Connected" — that you got connected. OK? That'll be your task for today. I'll tell you where to post it in a bit. Any trouble — Telegram is always open; **tag me** there and I'll definitely solve your problem.

OK. Let's move ahead.

## SQL's subdivisions — what can we do with data?

So the installation part is done. Now we'll look at: **what are SQL's subdivisions** — meaning: what all can we *do* with data? How can we meddle with it? They've divided it up here for us.

I've already shown you here: this one is the main one, this one is important, this one is the "M" one… apart from that, the five-sixth ones are the extras — how do I put it — they're *extended* into these. All those come *inside* these. So don't worry, guys — whatever exists, this is it. There are more, but they're extensions of these. This is the main set.

It looks something like this: **what can we do with data — how can data be changed** — and we'll look at it ahead in depth: *[reading the chart]* DDL… DML… DCL… TCL — Transaction Control Language. *[music]*

## Why a security student studies SQL

SQL is a **language** on whose basis we manage things. There's no direct meeting between **DBMS** and **SQL** — the two are quite different — interlinked, yes, but not the same cloth at all. SQL is a language we run so we can get our **desired output** out. This whole thing *[the system]* is what we call the DBMS.

Where is any of this needed? In any website, any online thing — because, look, you know it: today everything is **data**; no data, no nothing. You could become a database **administrator**: if anything happens with the data — anything goes up or down — *you* are the responsible one: how stuff goes into the data, what gets done, what doesn't.

And in **cyber security** this emerges like so: what happens is — you're running a website. Now when you **log in** on that website, there's some database standing behind it. OK — look, let me draw this… *[draws a login form]* there it is. Let me pass this in. OK — it's passing. The **username and password** — a **query** runs, which goes and checks: "is this data in there or not?" and gives the output. If it's there — admin — we logged in.

**If we meddle inside that query** — meddle with what's asked — OK? That's possible too. Or suppose we tweak something in our SQL such that **straight away, right here, we become** — what's it called — the **admin login**. That's also a thing that can happen.

Now — running that query isn't in the user's hands — it's the **backend query** — but it too can be **breached** — and that very thing is our **SQL injection**: inside SQL we've dropped our *own* thing; we've **injected** something because of which the database does something abnormal — behaves abnormally. And that becomes a huge **plus point** for us: if we want to get into something — to help ourselves in — using SQL injection we can slip inside. You put in something like a **condition that is always true** — true means it logs us straight in. Something like **1 = 1** *[OR 1=1]*. If you read injection in depth, you'll see.

And for this very reason it's **necessary to know SQL first**: how a database is made, how it works, how data is made, how data goes in, how we pull data out; how one data item joins to make a second one; how things associate with each other. Knowing this is very necessary when you go to inject. That's why we're understanding this deeply here today.

And as for **developers** — they need to store data, show data — so they obviously must study SQL too: they're building a website, building an app, building anything — needed, that's it.

## A recap, in plainer words

So that's the thing — **why we're studying SQL today**. Did everyone understand *why* we're studying SQL today? …Let's change the pen color so it shows tomorrow *[a side remark about the drawing tool]*… Please tell me — oh, about Krishna's question: changing the pen color — no need to summarize that. Did everyone get it? First tell me — did everyone understand why we're studying SQL today? OK, OK.

"Highlighting too much will make everything highlighted, brother" — true; as it is, everything's fine.

"Repeat — Gaurav brother, repeat once more." OK — look: why are we studying SQL today? Because — in development it gets used anyway… the tables and such, you're going to understand how things work, what they do. And in **this class's last class** we'll definitely try to do a **SQL injection example** — we'll definitely try; if I manage to set the lab up, I'll definitely try it.

So — it's like this: tables exist ready-made. In them, say, this part's our **username**, and here's our **password**. Then all these **columns** exist — under them the **rows** exist. This is called a **column**; this is our **row**. OK?

The **query** that runs against the database — against the table we've built holding our data — tables exist inside databases. And it can be one table or many; a database can be one or many. Data's here, tables everywhere… SQL runs its **query** on it. Don't overthink this right now — I'm telling you again: going ahead you'll automatically understand what I meant just now. But since you people asked for a repeat, I'm repeating. OK?

So — if the password's wrong, nothing's available. If it's right — available. Wrong means it brings nothing; if something matches, it brings it back to us.

## Injection, cracking, and why we learn defense too

In cyber security, what do we do? There's this thing called **SQL injection** — what's it called — the injection thing — in which: if we succeed in putting something **malicious** into an SQL command, because of which our database **behaves abnormally** and fetches us output — and that output can be *anything* — even user credentials. Like when we can *see* the users' credentials, we then get the database to **dump** itself.

People who do **cracking** will probably understand this — if you've studied cracking deeply — where did that data of ours come from? Where did the username-password data come from? It's exactly this: they'd go on small-ish websites — knowing them beforehand — using **dorks**; reach some small website via the dork; use an SQL query — SQL injection — on that website; get the database to **dump**. They'd get the dumps; then they'd **try that same username-password everywhere** to see — where's it still valid? In cracking, basically this same logic gets used — SQL injection gets used. Those who've studied it deeply know; if not — no problem; those watching this video later will probably understand too.

One warning: **cracking is completely illegal — don't even try it.** OK?

So that's why we're studying this inside cyber security: what a database is, what tables are, what's inside them, what SQL queries are — so that when we do injection, we can do it **properly**. How does the database work? Look — doing a thing isn't what's important; **how the thing works** — that's what we should know. Otherwise a person doesn't even know how the thing works — they just run a tool, run one-two commands — that person we call a **script kiddie**: the ones who don't know all this — what it *is* — who don't know what's happening in the backend, what changes are being made to the data. They're just running the work: "yeah, we're proper hackers — ran a second command, some script ran, someone else's." They have — pardon the emphasis — **zero** clue how the script works, what happens inside it. That's a script kiddie: they don't work on the concept; they just think "we know how to run it." Fine — but when the thing breaks, then how will you fix it? They won't know. But you're learning this **in depth** — so if something breaks, you can go and **fix** it too.

In cyber security we don't just learn to **break** things — we also learn to **fix** things: if an attack happens on some website, and somewhere we have to go protect them — "an injection has happened" — how will you sanitize it? Against injection and such? That too we must know. And we'll all know it when we can understand *how to break it*.

It's like this: if you put too much salt in the food *[Maggi noodles]*, the Maggi's ruined — yes — **but** those who are cooks will put in turmeric or something, whatever — *reduce* that excess salt's concentration somehow — add another masala and make it tasty again. So that exists too. Look — I don't know how to cook and still I gave the example; if the example sounded off — you can't just throw in anything quickly — sorry, guys, I seriously don't know how to cook. I only know Maggi — no, I don't even know Maggi's concept. If anyone meets me, "I will make juice for them" — coffee — that much I can do; shakes and such — whoever meets me, I'll definitely treat them.

OK — moving on — we went quite far off-track. Let's move the topic forward a little.

## DDL — Data Definition Language

So: what is **DDL — Data Definition Language**? Moving ahead. *[music]*

Definition language — meaning: how is the data's **creation** happening? **From creation, to changes within the data, to dropping the data — dropping it all the way to the ground — everything comes inside DDL.** It has a few main commands: **CREATE, ALTER, DROP**.

The CREATE command makes the data — well, basically data isn't "made" — what we make is the table's **structure**. It's for making a change in the data's **schema**. Sorry — I said "data"; I mean the data's schema — like, we've made this table. Now in this table — how many columns will there be? What will go inside each column? All of that — the DDL uncle decides *[personification: DDL as the strict elder]*.

DDL uncle says more: "kid — here you should put a number; here put a string; here put a date; here it'll go on like such-and-such." So this DDL uncle tells us how the data should be *[structured]*.

Now look — you're human; even we make mistakes. And for fixing mistakes, *they've given us a command too*: the **ALTER** command exists for us. We'll use the ALTER command so that whatever slip-ups we made while building the data's schema, we can go fix them later. You'll understand at the right time *[when we demo it]*: "oh, at that time I made this smaller; let's make it bigger now" — that's when it comes into use.

And suppose — your mood is like: "ugh, today we quit." You've had it, sitting in status-update meetings all day *[? garbled]* — that day you'll blow the whole data away with the **DROP** command and walk off *[joking]*. *[laughs]* "Keep them sitting there; make them work; I'm out" — for that sort of case too they've given the DROP command.

Sorry, guys — **don't actually use it like that**: dropping all the data when you leave someplace — please don't do that, please. A real use for DROP comes when company work genuinely requires a table to be dropped: when we're restructuring things inside a company — "we don't need these things; this data is just lying around" — *that's* when the job of dropping gets done. OK? Seriously though — don't do the exit-and-drop thing. Don't have some admin *[?]* say "Hardik sir taught exactly this wisdom before I dropped the DB — so before you quit, drop the data." No — sorry. OK?

## DCL — Data Control Language

What's **DCL**? Brother — look: now the table exists, and you've become — D-B-what? — the **administrator**. You're the king of this whole world: every bit of data in the table is yours. Great.

Now inside this there will also be **pawns** — pawns as in chess; I've never played chess *[laughs]* — Wait, it comes free with it *[?]* — I know what it is, but if you don't: a pawn is the small-fry piece; the little folks who exist — like in the movies too: everyone in the world besides the hero gets killed — all those are pawns; the hero's our king.

So these pawns — in our case the small-time developers or whatever junior folks there are *[joking: "we won't call them dwarfs"]* — for them, there exist commands for **giving them rights**: "you can INSERT data into mine; you cannot DELETE it."

Look — it might not even be a human: it can be a thing on a website too. Think: on a website we're always inserting data or pulling it out — we don't get the right to **delete** data. So in that case we've already given the website its **permissions**: "you can only insert data." Like whenever we go create anything *[accounts etc.]*, it should be [configured] such that data can be entered — meaning nobody should *modify* it in weird ways: nobody should be able to pull data out, delete it, do everything. That scene shouldn't happen.

It's not that DCL is only used when giving *people* rights — it's not like that. This one has two keywords: **GRANT** and *[ASR: "TRUTH"]* — **REVOKE** *[?]*. Grant — everyone will understand: when we **grant** them rights: "you can do this; you can insert; you can view things; you can update; you can delete."

Then — Revoke: inside that, we said: "no — this kid's no good; he's misusing his rights and his power" — so we'll **snatch his powers back**. Like his mother snatching them from him *[joking]*; then he won't be able to sit back saying "my mistake, my scene." That's the **REVOKE** command's work. And who runs these? The one who is Grant's master *[?]* — your head's head — or you yourself, if you're the head. That's nice too. OK.

## DML — Data Manipulation Language

Now **DML**. Look — the data schema I was making tables with — let me pick this pen back up — look, this is our data. I told you what a **schema** is: it says how many columns there should be and what should be stored inside them. So that's the *outside* business.

And this **DML uncle** now — he'll talk about the **inside**: "I'll put data in; I'll look at data; I'll update the data." Earlier we were changing the table's schema — DDL. Inside DML, what can you do? With the data that's *inside the table* — you can meddle with **that data**: displaying the data; **inserting** the data — putting data inside; **deleting** the data.

Deleting data — well, even we make mistakes… leave our mistakes for now: when we go onto some website, what happens in our **profile**? We get an option: "you can change your own name; change your email; change this; change that." What's happening in that case? An **update** has to happen: suppose the person changed their own name — now the person made his name whatever — we can do anything — had a sweet-talk spree *[? garbled]* — it's his choice, since it's his name. For the thing he's changing, we have to **update** the record.

All of this is what DML does. **Don't get confused between DDL and DML at all** — DDL is for the table and its schema; DML's for the data inside.

Going ahead — as I said — inside DML there's: *[music]* **SELECT, INSERT, UPDATE, DELETE** — these are its main keywords, with which we meddle inside the data.

Now you people will Google it and say — "brother, Hardik sir told it wrong — inside DML there's only INSERT, UPDATE, DELETE!" *[SELECT is often grouped separately.]* OK, guys — so they made a separate class for SELECT *[DQL]* — that also works. Punish me if you like; next lecture I'll come and say, "brother, it's my mistake; I was wrong." OK.

## TCL — Transaction Control Language

**TCL — Transaction Control Language.** Look — this isn't much of our concern yet. **It comes into use when we're totally advanced** — when you're playing with a production database. That's when it matters — it's very important in exactly that place, when you're working in production. Otherwise there's not much use of TCL.

Now suppose: we make some change to the database. After making the change, to apply it **globally**, completely — what's it called — we **commit** the data. Now, commit — this thing will be very familiar to developers; it's in Git/GitHub too — *commit*. OK? When the changes above happen — to execute them fully: "yes — commit this — I am now final: **apply those changes**." After committing, the thing can't be *[undone]*.

So in that case this works — **COMMIT**: after a commit, the final changes get executed there; after final changes, we cannot bring them back.

Now suppose you've made a **temporary** change. After making it, you think — "we did it wrong." Then you can do a **ROLLBACK**: "brother — go back to how it was before."

We can see this on the **bank server** too: suppose you pay someone right now — you're at a shop; at the shop you paid; after paying, there'll be "processing" — and you're staring at the shopkeeper's face and he's staring at yours — quite an embarrassing situation happening there. And the **Paytm box** is supposed to speak — but neither does the box say "₹10 received," nor does the phone — nothing. "OK — this failed." So what's happening in that case? You're *trying* to send the money but the thing fails — then your whole system does a **rollback**: "go back to the old state." That's what happens there.

And sometimes it happens like this: you're staring at the guy's face, he's staring at yours; on *your* side it already shows **payment successful** — but his Paytm box didn't speak; his PhonePe box didn't speak; he checked his phone — the money hasn't come. In that case your money's already *gone* from your account… but it never arrived there. So if something fails in between, then too they roll it back. And after that: **you get your money back within 30 days**. That whole scene is also a thing — TCL uncle says: "yes, if some genuine problem happens with the database's changes — roll back."

Why? Because you know how it is: once money gets cut, your heartbeat spikes: "my balance is showing low, but his payment didn't arrive!" — and more trouble piles on. In the midst of all that, rollback gets performed: "whatever the balance was before, whatever the state was — go back to the earlier one."

So these were its types.

## Close-out and homework

So today's session ends right here: these chart types and such — mostly **theoretical** stuff happened today; practical was one-two percent — like a couple of spoonfuls of solution *[?]*. Look — no matter how far ahead you want to get in one day, that thing cannot happen. It cannot. So in the coming days — sorry — in the coming ones we'll go **deep**: execute each and every command, build each and every table — in a proper, fun way. We'll do that scene too. So get ready for it.

And look — I will **not forget this**: I've given you a task: **install and send a screenshot**. Where to send it, how to send it — that I'll tell you now. Go to Chrome; after going to **LinkedIn** — use Oracle's username "system" and your password *[? — walking through the demo]* — then Oracle's [icon] will come up. Once it comes, you have to do nothing: go into the comments — **this video's comments** — and the installation I told you to do: install it, then **drop your screenshot in the comments** — "yes brother, done."

And inside our Telegram too — if you had or are having any trouble — drop it in our Telegram and tell us: "this problem happened; this trouble is coming; how do we solve it?" We'll look at all those things.

*[music]*

So — sorry you had to study from me *[self-deprecating]*, and if — how was it? There was that small mic issue — sorry. Probably in a day or two the issue gets fixed; I'm looking for a new one. If you people have any suggestion about a phone or audio gear *[?]*, tell me — what should I use? **My budget is small — up to ₹5000.** Tell me if there's a good one; I'll definitely act on your suggestion. Tell me on Telegram: "Hardik brother, this one's good within ₹5000 — use this." So that the [audio] is a little better. And please do give me a **review** of the session — how you liked today's: *[music]* improvements for next time.

For a day or two, sorry, you'll have to adjust with the mic — I'll order one and it'll take time to arrive. Actually I had a dedicated mic brought too, but it seems you're not getting better sound even from the dedicated mic. Whatever — OK.

Thank you for this — always open to your suggestions, your reviews, your feedback. **"Hardik zindabad"** — no need to chant that at all — **"Defronix zindabad"** is what it is. OK? It'll stay like that. If anyone has anything more to say — sir's great — *[laughs]*

…so — I don't believe in that; after this, what do we do… OK — you people show a good response and I'll enjoy telling you more. In this regard I've made **no commitment** for this series: that I'll run it 7 days, 10 days, 20 days. We'll go to a good — great — level; you people keep showing support. Good support — and we'll go further ahead. If you're enjoying, we'll make it utterly brilliant. You people will **demand** topics: "brother, teach this topic; teach that one" — those things will be taught here too; if a topic is big enough that it deserves a separate, stand-alone video experience, it'll get made for that too.

So thank you, guys. That's it for today's session — today was a short session. From tomorrow — well, tomorrow's a bit short too, because these will stay short-ish; later, when we get *into* DML and such — **for SELECT alone we'll spend a whole one-two days** — we'll go properly deep into the Selects *[?]*. So don't worry about that.

Thank you, guys, for today. And as always: please tell me in Telegram how you liked the session; if you need any improvisation — we're all fully active there; tag any one admin and everyone will reply to you.

So thank you, thank you, guys. Good night — ta-ta, bye-bye, sweet dreams. *[music]*

---

### Translator's notes (significant garble / reconstructions)

- **"आइसक्रीम का सेशन" (ice-cream session)** — recurring ASR garble for **"capsule"** (the channel's consistent term, per the prior capsules: Kali / Python / Network Security).
- **"और है कल / और एप्पल"** = **Oracle**; **"और कल 10g"** = **Oracle Database 10g** (the tool installed in class).
- **"पल एसक्यूएल"** = **PL/SQL** (Oracle's procedural extension).
- **"ग्रैंड ट्रुथ" / "रीबॉक"** = **GRANT / REVOKE**.
- **"डीएल / डीएमएल"** expansions restated per standard usage; the transcript occasionally merges letters.
- **"backend query" / "बैक हैंड"** — his "back hand" = backend.
- The **Maggi/salt** parable is literal in the source (offense teaches defense; a cook fixes excess salt with more masala) — kept verbatim with his own disclaimer that he can't cook.
- Minor live-class noise (mic tests, repeated check-ins, music cues, "OK?" tic) compressed but all *content* preserved.
