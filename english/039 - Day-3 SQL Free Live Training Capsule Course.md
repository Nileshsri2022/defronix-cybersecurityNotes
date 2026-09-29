# English Translation — 039 — Day 3: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/039 - Day-3 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer:** Hardik (Defronix Academy) — live session
**Style note:** verbatim-style translation of a heavily garbled auto-Hindi transcript; reconstructions marked **[?]**. Music tags and filler tics compressed; all instructional content preserved.

---

## Opening — continuity note

*[music]* …So — the **previous lectures** are also very important for understanding the data side. If you're someone who's just joined the lectures now, go watch them once. But either way, a bit of the practical part keeps getting revised along the way — its recap keeps happening anyway. OK? This time maybe we won't look at revision separately, because it'll keep happening a little by itself. So — basically — last time we learned to **build** [tables]; today we'll learn to **drop** the table. OK?

*[music]* Go below *[in the apps list]* — then here's our **Run SQL Command Line**. The password will be asked — OK —

## Warm-up question

Quickly tell me: **if I've made a table, how can I see its structure?** I told you in the last lecture. So please — I need to see a table's structure — quick, tell me how I can see the structure of a table…

*[while waiting]* …until then, so we can move a little further ahead, let me open a notepad. You can install [Oracle] anytime — I told you on the first day how. It'll stay exactly like that.

*[chat answers: DESCRIBE / DESC]*

## Dropping the table — and "object … is not a table"

OK — so the table that I made — this table — I'll drop it now: `DROP TABLE student;` —

Ah — look — it goes into the command above it: **"object STUDENT [is] not a table"** *[Oracle: ORA-… object does not exist / renamed]*. Right — because we'd changed this table's name back then. OK?

Now — there's a command with which we can wipe the **data inside** the table. And note — the thing written here *[on screen — the DESCRIBE listing]* — **don't take this as data** — this is **not our data** — this is our table's **structure** — the columns' names. Data is different — the names and such that get entered. OK. Data, data — same point — and that too we'll see going ahead.

## Constraints — one quick recital

So look — what's inside the primary key… I mean once — OK — so *[reciting with the class]*: the primary rule — at data-entry time — we impose these rules on data — all these rules — these "check-type" *[?]* rules we can impose. So first: it should be **unique**; in the middle there will be a relationship *[?]*; this is our status — life's status — married, not-married, single, committed *[joke]*— this very **foreign key** defines it; they should be different. Its example was told — the one with the phone number — can be an example. Good. In NOT NULL: your address can be there. Good example. Then this one also works: if you put something into the data — if you did some input — then that input stays; **if you people didn't input data, then in its place—** the **default**. And CHECK's funda — honestly, even *I* don't understand it fully myself *[laughs]* — but no problem — we'll study it. Like history — as we read on: "brother, will this ever be of use ahead?" — but people say you have to do it anyway; likewise these are some things we just have to do. OK.

So — these were our constraints — repeated once more. But when we see its **practical implementation**, we'll know a little more deeply what things inside it are.

## Building the fresh table (emp)

So first we'll make a table — once more — *"kebal"*? *[? — "...one I told only yesterday"]* — OK: table — table — *very nice* — tell me now — **primary key** — OK.

Our next — now here we take the **name** — its size — I won't leave it empty *[NOT NULL intended]*. OK — name done. **Contact number** we'll give. And to figure out — who is from where — here I'll also put a **state** option — inside this [column], `VARCHAR2`. OK.

Now suppose someone doesn't enter their state — meaning he just puts his city — then what I'll do in my **default**… All these strings we'll create as strings. Put it in quotes here — look — this thing — see — this is how it's taken today *[ASR: " आईटी इस ही लिया जाता है" — i.e. the syntax with DEFAULT 'Rajasthan']*. So suppose: inside STATE, at data-input time, if I entered "RS" small *(i.e. typed something myself)* — then the **default case won't fire** — whatever you entered goes in — inside that case it goes. OK? That makes no difference — no difference from it — but the string-thing will remain just as it is. OK.

That department — good — maybe *[music]* — press Enter here — then I'll have to change here — so in exchange I'll do it like this here *[adjusting]*.

## INSERT (DML begins)

Now suppose — I see it — OK. Our next — about the command — I told you yesterday that I'm telling you about DDL — doesn't come on Instagram *[? garble]* — this comes in **DML** — but right now we're only understanding about constraints and such — and we *want* to do the practical, man: "brother — you told all this — these are talks in the air — how is its implementation actually happening in the backend — I mean — the constraint doesn't even *show* on the front — we make it — fine — *[applause]* — we're patting it — is it really *deleting* or not *[i.e., is the rule really enforced]* — did I tell it right or not?" — that thing wanders a lot. So now here — for **INSERT** I'll have to write — straight: `INSERT INTO <table>`. **There are two ways.** The first way I'll tell going ahead — here the values get filled. OK — I'll give 1001 — and first, give a name — to this one — inside this — contact number — sorry — inside state — here: default is Rajasthan… so whose state is yours — I'm meaning — not asking your address — so I'd have to think for it — keep it within Gujarat itself — feels good by itself. OK — if you press in yours *[?]* — so that thing is there.

Here — what is it — primary — just revised it — **not-null** it should be — and **unique** it should be. OK? So look: the 1001 I'd put — I'd *already* done it from here — in this whole affair I'm writing 102 — and here — the row got made — very good — very *[nice]*.

## Why the command line, not a GUI?

"Brother — SQL query's interface — why not use *that* one?" — We're not using that — first, it doesn't look good to me. OK? Look — we'll work in the C drive *[CLI]* — more fun — because you won't *get* to work on a GUI everywhere — because this thing — we're going to work **on servers**. OK? There — no GUI thing will come along to *help* you. Like — if you had to open with — in phpMyAdmin you could put SQL share *[? — i.e., a GUI panel could fire your queries]* — you won't get that GUI-based work everywhere. Suppose you're working on any server — what will you do there? You'd have to **install** there — solve *[set up]* inside the server — then inside it you'd connect with SQL — then afterwards — if there's any reason here, working through a GUI makes no sense. Everything stays the same — below the command comes — you highlight the commands and click them there — it runs there. OK — it isn't compulsory to find that everywhere. OK.

"Paras Singh" — Bharat Singh had told — that from the start I'll tell you — you have quite some trouble *[? — a chat exchange about following along]*. But this thing was fine up to some limit — my location, tell me — had to be used *[? — garbled chat back-and-forth]*.

## INSERT method 2 — named columns

So here — this is number — in place of the contact number we'd put UNIQUE here — that's why that happened. While entering values — here — the **sequence** stays this-way — I'll tell you: "just tune with" *[?]* — yes — meaning — inside that too there are tables, but you can't use the data *[?]*. What's in this case: it's that same table — stays made of yours. Your data's there — inside the server — comes with "IT is" *[?]*. How the work happens in the server — that thing he's watching even on his own *[?]*. OK — now if I change Paras-brother's number right now — then after that — look — here our rock got dated *[? — a row updated/duplicated]* — if I write "tax" here *[?]* — then I copied it here — from here too — so *as-it-is* — inside the server — you'd never get it back for retrieval. OK? What you'd said — where the primary key was put — all that was put — you don't get to know that. OK — fine — you have to push it further here — we'll find out more *[music]*.

So — this stays like **simple English** — stays on simple English only: "read, make" — table's name — by this MP's name *[? — he means the phrasing]* — it's simple-ish — like its English — if you do it twice — meaning it'll come in one-two tries — literally if you do it once or twice.

Now tell me in chat: **who all is practising** — man — what I'd told — the picture's *[?]* — until I move ahead — I'll put "umpire" *[? — a name]* here — I'll put 10 here — meaning I put 105 — so look — what's there in this case: **if you're not doing columns [named], then you have to walk [the full sequence]** — then whatever the columns are — you have to go **by the sequence of the table's columns** — not necessary inside that *[?]* — so here this I've written ahead — this MP *[row]* I can slip into the middle — no trouble in that — but you have to understand the **concept**. The concept is exactly this: here — however I may write it — **but** since I've **specified columns** here, now I must put the **values by those columns only**. When I wasn't doing Congress *[? — "columns"!]* above, I had to put **every** column — and this message by *its* sequence — but here I've dealt with only three columns — so I'll tell **only three columns'** worth here. OK?

## SELECT — today, only a taste

Now when a custom-one falls *[?]* — about SELECT — this isn't *that* right-of-course — SELECT has **a lot** inside it — literally a lot — SELECT got studied-studied *[?]* — for maybe **two full days SELECT alone will run**. OK? Maybe from tomorrow our SELECT starts. But today, know one small thing about it: what SELECT does: the data you've put in — inside your — what's it called — inside the **table** — **showing** it — that work it does. OK? `SELECT * FROM` — "stylish" we can also say *[ASR: from the table's name]* — the meaning of **star** is **everything**. I want columns here — for now *star* can happen — although star — here his phone number also came — look — everyone's phone numbers will show differently *[?]*.

"Department…" — now suppose: inside this — this last one that was — Mohammad Kaif brother's — I hadn't put the state at all here. In that case what happened: it took **Rajasthan by default** here — **look. Why did it take it? Because inside STATE here, we'd already put this constraint — the default — day-before-yesterday *[?]* we'd put Rajasthan — if you don't do [enter] a space/state, it'll put Rajasthan.** So this was the thing inside it.

So about INSERT, you had to know these **two things**. OK?

## ALTER — modifying the schema

And our — to **modify** the table's **schema** — the work comes — "kami rehte hain, pata nahi kyun" *[? garbled — "hardly know why it dwindles… still it's fun"]* — but — are you all having fun or not — whoever all are here — it's fun, right? Good thing or not — come on — good thing — it gets fun if you keep doing the practical alongside; "like se aa gaye" *[chat: someone came from a like]* — good thing — keep pressing the one same place again and again *[like button joke]* — OK, no problem — let's move ahead.

Now look — what was happening with **D-E-S-C** — DESC *emp* — look at this — now — now you must have come to know the different-thing difference between the **schema** and the table's **data** — meaning — must have come to know.

If — suppose — we have a problem — so I'll write here — I'll put **salary** here — our salary goes in **numbers**. So here I'm putting a **10-digit** one — I hope you all also get a salary of *over* 10 digits *[laughs]*. See — look — now here salary's come — and a nice one — for salary — somewhere — didn't come? Look — this — the data — written like this it comes — this is a bit of a loner's trouble *[?]*: the table shows kind of *tall-ish* — it comes in this affair — because look — I've given — ten-ten digits — that's that thing of ours — how much we've put inside it. If I reduce these, maybe it'll show decently — we'll look at this too — maybe we won't be able to see tomorrow — they're about to fly *[joke]*. OK?

Now — suppose — I have to drop a **column** too — delete it — I know — the DEPARTMENT column — I don't like it — I have to delete it. So what will I do? `ALTER TABLE` this `emp` — then after that I'll write here — we want to **DROP** — what do we want — the column I want to drop — which column do I want to drop? **Any can be dropped** — no compulsion that — man — only the one added recently — the salary I added — only that can drop — or the last one — **don't go into that pattern** — you can drop **any** column. So in this affair I've done it here — like afterwards some modification happens.

**But one thing to remember:** use ALTER **mainly when you've just made the table and freshly change it** — because what happens: after inputting data, if you change the table, you may later have to make changes in the data too. For this very reason — it sometimes happens that the data doesn't *let* you alter the table — this case also happens. So that's why this stays: finally, make the table — and right after it — if you have to make some alteration in the table — *then* why not — **after inputting data — or after the last data input — don't do alteration.**

A column has to be **modified** — a constraint has to be applied. Its inside this is 15 hours' *[? — digits]* — so I'll write ALTER — only stick it — man, brother — how's this — meaning — into its — we'll put a number — then in front of you some different errors will be learned — so that we can't see those errors — for that I'm switching this one thing on for you again and again — happens, man — like this — meaning — you're new-new *[?]*. So — when you don't take interest — then it walks in my [*own]* calculations — walk — I'll use all work here — although this is very different. OK — look, it's lots of fun. So here I — my ₹20,000 I give here *[salary value for the demo row]* — here I'll add it again — I said — told — that yours became original *[? — row inserted]* — so right now I'll do **DSC** here. OK?

Now this was the straight columns' thing, man — look:

## ALTER … RENAME — table and column

Now suppose — I have to change the **table's name itself**. In that case what will I do? `ALTER TABLE` — to — employee *[RENAME emp TO employee]* — I wrote the table-code — simple English of ours — you'll understand a little — like I'd told you — my English is also bad — meaning still — a little coming-*use* has happened inside it *[?]*.

Now if I do here — it'll show **"table does not exist"** — why will it show — quickly tell me in chat — *Mewati*: "the table's name got changed." Here the system got big — yesterday we did the work *[? garbled]*. OK.

Now suppose — I have to change the **column's** name only. In that case what will I do — I have to premium *[? — rename]* — what — **which** column — which one do I want to denim *[? — rename]* — contact number — I want to write here **phone number** — "contact number TO phone" — all that I have to add — so how will I add it — **through ALTER** — so this thing — **you people will tell me** — **this will be your TASK** — which I'll tell you again — so don't be like "thank you, sir" *[?]*.

## DROP vs TRUNCATE

So now — our next — with **DROP** — some table — the table goes away *[gone entirely]*. But I'd also told you something along with it: that if we want the values *inside* the table to go — in that case what do we do? Once — TRUNCATE — one drawback of TRUNCATE — let me tell you:

**If you've used TRUNCATE once, you can never ROLL BACK.** Rollback's meaning I told you in the first session — what it was. I'm behind you *[? — he means: recall it]*: suppose you make changes — with truncate — something or other — then you *cannot* go from your current state back to the previous statement — such that you get the data back again. **TRUNCATE empties the whole record. The table doesn't get dropped — the table's records — those it blows away.** OK?

So here — I'm serious: **use TRUNCATE only when you're on very, very good terms with your company** *[joke]*. OK, OK — I'll press — "no rows selected" it's showing — meaning — inside this there isn't even one row left.

So that was about TRUNCATE: it blows away the whole data — and it blew it inside just one command — and from this we can never retrieve it — you can't take it to the old state.

## Tasks and homework

So I'd told you people a task: you have to **add a primary key and show it** — you have to show that task of ours — about the concrete *[? — constraint]* — full — the table's inside data — while inputting data — data — in one big — with one command — all-all data will get blown — which can never rollback *[i.e., also demonstrate TRUNCATE's danger — ?]*. OK?

So look — like right now this is Day-2's — likewise Day-3's post will also come. In that post you have to write **your command** and put the **screenshot** — with your **DSC**. And inside the post's **comments** you have to drop: **how you added a primary key via the ALTER command** — that very little [thing] we'll always take — always — to improve yourself. And on YouTube — you have to **add some column and show** it **with your ALTER command**.

"This website makes..." *[chat question]* — right: if you're making a global [site] — global SQL — by itself — does a certificate stay? *[? garbled]* — otherwise — inside a server you'd have to install SQL's server — you'd have to screenshot — after installing — we — if you want, you can do any service — and tomorrow you can also install — after your storing — whatever — like I've just told you the styles here — you connect — then **through your website you have to send the commands**. OK? I'm telling you — this is how it happens — it'll be taught inside development. OK.

## Voice pacing (response to feedback)

"Need voice — meaning what voice — active? What — active voice — meaning should I speak in a totally fast way — or what voice?" — If you watch the active *[?]* first lecture — I'd spoken very fast in it. I'd spoken totally actively there. But the thing is — beginners and all didn't understand that thing — so I'm speaking a little slow — and a bit haltingly — those people understood this thing well — for that reason — tell me: should I profile it like this *[?]* — so that if you have any slip in hearing or any slip's happened in my speaking — it gets corrected? For that only — OK — good.

If you people liked it nicely and well — then thank you — ta-ta — bye-bye — good night — shabba khair — and Jai Hind — Vande Mataram — and… *[end]*

---

### Translator's notes (garble / reconstructions of consequence)

- The transcript is exceptionally mangled mid-session (chat cross-talk rendered as nonsense words: "Congress" = *columns*, "umpire"/"MP"/"tax" ≈ demo values, "denim/kebal" ≈ *rename/only*); all SQL-command content above is reconstructed from the surviving syntax spoken aloud (DROP TABLE, INSERT … VALUES two ways, SELECT * FROM, ALTER TABLE ADD/DROP/MODIFY/RENAME, TRUNCATE) plus Day-2 continuity.
- **Factual anchors that survive cleanly:** DESC vs data distinction; DEFAULT fires only when nothing entered; INSERT's two forms (full-sequence vs named-columns); starred error-reading carried from Day-2; "table does not exist" after RENAME; **TRUNCATE = irreversible, rows-only wipe**; homework (**add a PRIMARY KEY via ALTER**; ADD a column via ALTER; discover **RENAME COLUMN** yourself) posted as command+screenshot in the day's LinkedIn-post comments.
- Unrecoverable conversational scraps (locations, like-button banter, server/phpMyAdmin aside) are condensed or flagged; nothing instructional is omitted.
