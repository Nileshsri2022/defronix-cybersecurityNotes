# English Translation — 038 — Day 2: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/038 - Day-2 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation; auto-generated Hindi ASR with heavy garbling restored where the intent is clear, flagged **[?]** where not. Music tags and repetitive tics compressed.

---

## Opening

*[music]* …So hello guys, I'm here — tell me: is my voice coming through fine for everyone or not? Because these days a lot of people have had trouble with my voice in the mornings *[referencing Day 1's mic issues; garbled]* — will it be understandable? Come on — confirmation — security *[?].* OK, let's move ahead.

## Data types — why they exist

Today we're starting — what is it — is it a **string**, is it our **number**, what is it — **date/time** — meaning, *what kind of thing is it*?

Here's what happens: whenever we're having data **input** — from any user, or by an automatic system — the data to be stored goes column-wise, and there's this rule: in *this* column you can only put a number; in *that* column you can only put such-and-such; in this column you can put only this many digits' worth of stuff. OK?

So those kinds of rules exist. **Mostly there are three types in our SQL:** a **string** type, a **number** type, and **date & time**. OK. There's also **binary** — for storing files and such — but we won't go that deep right now; we'll cover the rest later.

And note: your **system/version can shift these by platform** — this is the *one thing that differs platform-wise*; otherwise in SQL nothing else really changes *[? — he says: this is the one thing that differs; the rest is common]*. But many things are common across platforms, and we'll do those in here.

### The string family

Look — whichever data type it is: it will store data — and **how much** will it store? Everything has its **limit**. So: there's our **CHAR**. When we declare a CHAR we have to give its **size**: what should its size be — how much will you store — so that memory allocation stays right. You must have seen this: people with very long names — when they go to show up in the latest [app] lists *[?]* — their names come out shortened: after some number of characters, their name gets **cut**. OK? It stays like that if [the size]. Now — how much can it store… a character takes at minimum one or two bytes *[ASR garbles this into "2000 bits 2018" — the intended point: ~1–2 bytes per character; not much up-down]*. I'm telling you an average, OK.

Then there's another: **NCHAR** — used to take **Unicode** and such — it takes **national characters**. You know — Unicode is a bit different: beyond what's on the keyboard there are many more characters, and those come under Unicode — it stores them.

Then comes this **VARCHAR2** — it stores strings. So in this regard, these are used differently from each other — and they have their own **special features** too, OK. What does what — you'll start seeing it and tell me; if possible I'll hand this over in text form… Tell me: does this show up everywhere *[?]*? OK — "we'll move with you."

So right now we'll mostly use **VARCHAR2**. And it's not limited to just these — there's **VARCHAR** too inside it. Those exist as well, but these are the **main** ones — the ones used most often everywhere.

**Rudra's question:** "Brother, you should explain better — which part should be explained more deeply here?" Rudra — don't load onto this so much right now: what it is, how it works — when we actually take these things **practical**, this will get clearer. But if you're asking me to explain more deeply — fine, I'll explain.

A **data type** is nothing exotic — it's called the **type of the data**. Whenever we make tables in SQL — Rudra, I think you weren't there in the first lecture; I'd explained the table format — inside every column we fill in one data item, and while filling we must **define** it: what will this data's type be? Will this be a number, will it be a date, or time, or a file — what will it be? That's our data type. What comes inside it — so that later, when we want to **filter** everything out, things stay *easy*. That's why telling the **data type is compulsory** — but telling its **size is not compulsory**: they have **default sizes** which they take by themselves.

### The number family

So nothing much — we just assign a data type to any data. "What is it?" — look: the data I gave **[draws]** — two things: number… and a type with the point — after the **point** — what thing is that — how many values can you place after the point?

So: **NUMBER**. Suppose I wrote here inside this number an example *[music]* — it looks like this — the **P** *[precision]*. Now suppose I've put a comma and ahead of it — let me explain with a doubt-clearing example — what will it mean? **NUMBER(5,2)**: total digits should be five, **out of which two** will be after the point. It comes like that.

Write it in small letters, write it in big letters — big-in-small, small-in-big — **makes no difference**; however you write it, it only takes that much *[case-insensitivity]*. We're using the number — the ones with the **point** — fruits *[? — "FLOAT"]*: it means the first-point one; both catch *that* job — for those who do the new *[?]* — note this: it does the same work — the point's work — gives the point's value — and its **range is so much bigger**, because it's working only for the point-cases. So the thing is: the values of P differ across them — it's a small **game of memory**; it runs by memory. Together with that you'd have to fully understand memory — that can't happen here; *[that's too]* technical.

### Date

So this gets placed like so: suppose you've first written the **month**, then you have to write the date — properly installed *[?]* — meaning the way I've put the new one in the recording. OK.

## Q&A: what about SQLMap?

"Brother, what about **SQLMap**?" — SQLMap is a **different thing** altogether. OK? That you'll be able to understand — but: when you put in parameters, it keeps **striking injections** as per those parameters on its own. Now — what it's *trying*, what's the **logic behind it**, what all shows up for you in the middle — you'll see it using **UNION**-based stuff, you'll see it using **bitwise** *[? ASR: "bitwise"]* — that much shows in front of you. But what those things *actually are* — that we'll look at: the different ways it can do it — "but how do I make **custom queries** of my own, so the database gets exploited *by me*?" — that whole layer is what we're building toward.

## Password / connection check

I told you the password yesterday *[he set "electronic"; the default admin user is **system**]*. Now please tell me — what's its username? Meaning — if you people have also put in some username and password, write it in chat — nobody's going to open your PC and peek here! *[joking]* Open up Oracle — let's see what details we've stored in it.

So write your username and password here in chat. I also need to figure out here how many of you actually connected — because **nobody sent the task on Telegram** — nobody tagged me. I checked too — I didn't see it anywhere. Tell me how to put it in… anyone… OK, whatever.

The one you should take a screenshot with is the **system** password — the one I told yesterday. OK — so I also feel you were paying attention in yesterday's lecture: *[checks chat]* yes, putting it in — OK.

## Live demo: the notepad "hack" and CREATE TABLE

So for this, what we'll do: suppose while typing something in here, an error shows up. Then we don't want to rewrite the whole thing in one go — in one click we should be able to have it all written again. So for that, what do we do? A small **hack** — this will be your life-hack: **I'll write the command in a notepad first**. After writing it there, I'll **paste** the command here — so that if I get any error here, I'll directly fix it in my notepad and paste it again *[ASR: "gift it to someone" — garble]* — so I don't have to go through the trouble of writing it back here or doing anything — I won't have trouble.

So first — how do we grow this thing — its control — OK — then these brackets get placed. If you're making a student's database, what all details can you keep of the student? Me — class number, roll number… If inside a table you keep the roll number's data — hey, I told you about text before — so what do you think — meaning that one is — if you apply even plain **common sense** here: what could a roll number's data type be?

*[chat answer]* "Number" — very good, **nice**.

If I want a new column of ours — the details' setting — Abhishek brother *[? garbled]*, no idea how much interior *[garble]* — I haven't done that either, I think, inside this. OK.

So for me to add the **next column**, look — I put the **comma**. If I forget the comma — then — I put the name here — what can the **name** be — what can we store there? There you can put a **limit** *[size]* — some more could run too — those who know, know — OK? But for now I'm thinking let's go up to about [twenty–thirty] *[? — he picks a size]* — OK — this was my friend… *[column]* **ADMISSION_DATE** — look — one thing you keep in mind: the **pattern** — inside the screen — spaces — **you can't use** them here. Time it stays — I feel like — OK.

Now inside admission date — I've already told you about **date** separately. The **last call** I'll use, the work ends *[? — closing bracket]*. One thing to remember: **no query runs halfway/inner-ly *[?]* — the whole thing at once**. I've written it here in separate lines — its meaning is **absolutely not** that you must write it in separate lines. If you keep it in a single line, the query will still run. Not necessary that it stays separated — but for good looks I've split it — because looking good should matter *[readability]*.

Then here will come our— column's name, detail, type — its **size** — not that the size happens *[?]* — because inside it — OK — now we'll copy this and paste it.

## Reading errors — the classic beginner mistakes

Remember this, man — this thing — even my classmates and all my people used to stay stuck with this: "brother — the table, did it get made or not — I mean — I put the credit/created it *[?]*, but why didn't it get made, man?" — **they didn't look at the output**! "The table got made." Apart from that, if anything at all comes up — I mean — somewhere, *somewhere* an er— an error happened. They're not that hard to understand.

If I try making this table a second time — then it'll show me here the error: "table is pe—" — this: **after STUDENT**, look — it put a **STAR**. Wherever your error will be, **before it, it puts this star** *[the `*` marker under the offending line]*. OK? It can be a little up-down sometimes, but it'll be *near* it — the thing will be around that history *[? — the starred neighborhood]*. So this star: understand that around here — somewhere a mistake was made by me — or here — or here there's a mistake because of my previous line.

But look below — how clearly it's written: **"name is already used by an existing object."** Everything here is an **object**: a table is an object; with the CREATE command you can make tables, you can make **views**, you can make **indexes**, you can make **procedures**. And wait — let me look at every message here — there's no need at all to do this right now — all that will be taught; don't take tension for it. Right now inside this table there's no primary key or anything — see, it's happening object-wise *[i.e., the name collision is at object level]*.

So it's written there — what — using common sense you can understand: I've already used it somewhere — made it before. So **change the name and make the table**.

OK — now I'm making the table with a changed name — **but here I forget the comma**. Then it will keep saying — look: **before ADMISSION_DATE, a star came up here**. So like I told you: when the star comes for you, look before and after it — whether something of yours got skipped in the writing-and-forgetting shuffle — an error's coming — it's understanding it like this: that *ahead of this*, this line is making it happen more *[?]* — because I told you: if you want to tell it that you want to put in one more column — if you want to add a new column — **you must put the comma** for that. If you don't put the comma, it'll give that vibe: maybe these were all the columns — so it said exactly that: "I'm seeing a **missing parenthesis**" — meaning to it, we should have put the parenthesis and the semicolon — it's feeling like "this was supposed to come, and you've missed putting it." **But that's not the scene** — we have more columns left; *we* have to put the comma here.

This thing will become understandable to you along with practice — what it is. But the joined text *[the statement]* will remain just the same. OK. So our table got made.

And there are some such errors which you'll **commonly** get to see at starting time — which I've just cleared for you: what's what — meaning, what thing is how — how a table gets made inside this.

## DESCRIBE — checking the schema

Now suppose a table's been made. After it's made, I want to check: "OK — for my knowledge — what columns does the table have, what all is there, what's this table's **schema**?" — so to see the schema there's a command. You put the **semicolon** *[terminating]* — then from here it told us — OK — line got done — so I copy it further inside this, paste here, and press Enter here — so look — I'd made the student's table — look—

—Now look: inside NAME, however much I'd given it — what's it called — how much **size** I'd given it — that much shows up here *[the size column in DESCRIBE output]*. OK? OK. So brother — don't think that in this name-thing there's this much here *[ASR garbling the exact numbers]* — it comes per the highest *[? the display width is the max]*. That works too. Don't use your brain up to here at all — I've just told you casually *[i.e., don't overanalyze the DESCRIBE display]*.

Did anyone actually tell me or not — I checked the description — meaning — like me, people didn't get the spelling "description" *[light self-joke]*. So look — here it's written **NULL** with the **question mark** [*Null? column*] — the constraints and all — the rules that exist — this table — right now these rules… we'll put them after finding them. Entering *[data]* — what data should be entered. Ahead, we'll apply **rules** on the table too: these-these rules will exist. OK? While entering data — so that the entry of data stays **sanitized** — its **integrity** stays maintained — those are **constraints**. Come on — OK — good thing.

But still — we're not going to do this work in February at all *[? — garbled aside; likely: not rushing]* — calmly, every single part, we'll go at our own pace, totally relaxed.

## Constraints (integrity rules)

OK — seeing the table, making the table — now we'll look at: **what all rules can exist on tables** — when entering data. OK? So for that — whenever we do any **data entry**, checking its **validation** is called **integrity**: checking that the validation — is it valid or not — or not… so it stays in integrity. For now — we'll do the most… **it plays a very important role** — this — the **primary key** that we put in it.

Now look — we people were given such a number back then — man, a **roll number**, in school time; a phone number too — a phone comes by it — compulsory *[?]* — so what happens by that: in our **data finding** — inside rows — it stays very easy: OK — that that part of the data is **not empty** — we can fill the data — so — it stays in our own hands that we fill the data — someone might leave it empty — so in this chicken *[?? — his own verbal tic]* — the **primary key** has a voice *[?]* — this — mostly **we ourselves generate it** and give it to the other side — like every user has an **ID** — every student likewise.

What does a primary key do? It's **never empty** — meaning it's not like someone didn't get an ID, or someone has their own same-work *[?]* — not right now — the one that is — like the name: everyone has their own name. Everyone's putting a name — like "what's your name?" — OK — it's not like some news has no name *[there's no such thing as a nameless person]*. So inside the name [column] — everyone's names *can* repeat — but it can't be that someone simply has **no name**. In that case we put it in the normal category *[?]*: "you — do one thing — keep it not-empty."

That must be **unique**: the best example — look at the phone-number option: it stays **optional** — fine — but when you *do* enter a phone number, that phone number **must not match anyone else's** — it must be unique. In that case we can use the **UNIQUE** constraint.

Now after that comes **DEFAULT**: suppose for some data you didn't put any data — then whatever was set "by [default]" stays set — it comes there. If there's a "jyada" *[? — nothing]* there — we entered nothing — then it'll stay entered in the default — it comes there.

And the **primary key**: that's a **mixture of both of these** — **NOT NULL and UNIQUE**. OK.

Now we come to — let's meet with an example — our IDDBS *[ASR]* — into RDBMS — inside its category — the **FOREIGN KEY** — this AI-command *[?]* — inside meeting/linking the data. Like: suppose you have a student's… a paper *[?]* — OK — now suppose we've put one more thing in the screen: say we put **B.Com** here; and I also kept its ID — kept as `b.com`. OK. And now here I put **BCA**, and here its ID too I made the same way. So — see what's in this case: and suppose here I kept it on the student's table — look — you're understanding absolutely nothing *[he's mid-drawing]* — see — if you try to understand the table later, take a screenshot of it — how — my setting's making sense to me — but yes — that person still passed me *[? — classroom-aside garble; skip]* — because maybe he'd have shown it sitting with the chemist *[pure ASR noise — dropped]*. OK — in front — just for showing — this is written. OK.

So suppose: you've made a **student table**. In it you've put the name, put its ID, then for him you put the **course** here. What had you done? Inside this "Bharat" *[ASR for "course" table? — ?]* — you'd given the option of **ID**: "enter the course ID here." Now what's happened: **inside the other/old table**, this ID thing — this ID column — you'd given it the **primary key**. Now the primary key — what will happen inside this ID: **no repetition**, and **no staying empty**.

In this regard, only the primary key gets made *[chosen as the link target]*. This student table will remain **linked** to some other thing — it stays linked with the library *[ASR: "library" — likely "like-a" garble]* — one key, brother — to check it — it uses it or not — so such a thing exists too. So brother — one table can be **linked with different tables**. For linking it, the **foreign key** command came along: we put in the **other table's name**, and the name of **which column we're linking it through** — that column's name.

Mostly — if you're linking through some column — in that case you should link it **only through a primary-key column**. OK? Because — so that our — the repetition — and that it not stay empty — for that, the one you link from must be a primary key. OK.

Inside the student [table], we put the question here *[?]* — the foreign key which is linking — from our "spirit" *[ASR — parent?]* table — how the linking happens — **we'll see that going ahead** — but right now we're studying about the foreign key, so I'm explaining it to you. Don't use much brain in this yet — when you see it practically, going ahead later, you'll understand this thing more. OK? As much as you're understanding right now — good thing if you're understanding; if you're not understanding — no reason to take tension: when we do this **practically** ahead, the thing will come into your understanding even better — it'll get clear in your head.

It's entered — it's linked with this table's primary-key column. **In the first step it'll go and check**: "brother, is that data **available here or not** — in that column?" — **only then** will it place the entry; otherwise it won't place the entry. Explained with an example. OK?

## Close-out and homework

Understood? It's making sense? Please tell me in chat how many people understood — so it feels a little good. Please tell me once whether it's making sense to you people… No problem — we'll see.

So for today, that's it. OK? A little— for today this much is to be known: you have to understand these things, and its **implementation will happen tomorrow itself** — but you have to come after **revising this**, so that in tomorrow's implementation you don't face trouble. If you're understanding — you need the answer *[?]* — and if you've tried it yourself too — then those of you who were already so prepared will have understood what I'm about to do. But still — I'm telling you again — if you have to go in Hindi *[?]* — in today-tomorrow it'll come — about that: **write in the comments** that you have read this — this has reached you. OK?

So please tell me in chat, brother — it'll start making sense again *[?]*. Tomorrow also you'll get its overview — don't take trouble for it. This last slide — I'll put it first in tomorrow's PPT itself. OK?

So thank you guys — if you have any complaint, or — how did the session feel — if you want to give any feedback — **I am open for feedback**. Meaning — **notes**, brother — **notes won't be given until you people tag me and tell me**. But I can't see it in the [LinkedIn] post — your task — or you'll just drop it summarized inside Telegram — "did this task, did that task" — **tag me** — until then I won't grasp that you're serious and that notes should be given to you. Because everything is running live — it's recorded — you can make your own notes too if you want. But if your hard work is visible — giving notes will also feel good — that's all there is to it. Meaning — until the post comes on LinkedIn, tag me on Telegram and drop your screenshots here — we're standing here *[?]*.

So that's all for today, guys. Thank you — bye-bye — good night — *shabba khair* — Jai Hind — Vande Mataram — Jai ho. *[music]*

---

### Translator's notes (significant garble / reconstructions)

- **DAY-2 content anchors:** data types (CHAR / NCHAR / VARCHAR2 / NUMBER(p,s) / FLOAT / DATE), live `CREATE TABLE` demo on a `student` table, error-reading (`*` marker; "name is already used by an existing object"; missing-comma → phantom "missing parenthesis"), `DESCRIBE`, and constraints (PRIMARY KEY / NOT NULL / UNIQUE / DEFAULT / FOREIGN KEY).
- **"आम सेंस"** = "common sense." **"डेट की अलग बात"** — he *did* cover DATE in this lecture before the demo (the line "I've told you about date separately" refers back to it).
- **"इस कैसे में… चिकन"** — recurring nonsense tics in the ASR (e.g. "chicken") were treated as verbal filler and dropped.
- **Foreign-key example** is heavily garbled at the drawing-board moment; reconstructed faithfully to the standard interpretation he confirms verbally: a courses table with IDs (`b.com`, `bca`) holds the primary keys; the student table's course column is the foreign key; entry is accepted only if the value already exists on the parent side.
- **"फरवरी"** ("February") line and the "chemist/library/spirit" bits are ASR noise; where unrecoverable they are marked or omitted; all *instructive* content is preserved.
