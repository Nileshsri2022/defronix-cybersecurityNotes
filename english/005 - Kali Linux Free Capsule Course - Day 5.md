# 005 — Kali Linux Free Capsule Course — Day 5

**Source transcript:** `transcripts/005 - Kali Linux Free Capsule Course - Day 5 [ Hindi ].hi-orig.srt`
**Topics:** `sed` delete & insert operations · `grep` in depth · `egrep` / `fgrep` · Doubt session
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`सेट`/`सीडी`/`एलसीडी` = `sed`, `ग्राफ`/`गैप`/`ग्रेप्स`/`ग्रह` = `grep`, `डीएस` = `dns`, `करनाल` = "kernel", `लाइनेक्स`/`लिरिक्स` = "Linux", `सीटीसी`/`ईटीसी` = `/etc`, `पास डी` = `passwd`, `रॉटविलर`/`रोटी` = "root", `शब्द` = "word"). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone. Let's wait a minute for the rest of the people to come; after that we'll start. [Music]

Very good — you used it; the output you provided, the command that I needed, you gave the correct command that was my expectation. It was homework. Very good.

We had left off — there, at the end, when we had the find-and-replace topic, there we had left our `sed` command [incomplete]. So let's continue with the `sed` command that is remaining. After that, the next command will be the **`grep`** command. And if we have time, we are going to learn about the **`cut`** command — in valid detail, as we have always done; we'll do that this time too.

---

## `sed` — Delete operation

So let's start: in the `sed` (stream editor) command, how do we perform any **delete operation**? How will we perform a delete operation? Let me tell you.

Simply, what do you have to do — let me look once at where my file is, where I had my [samples]. Okay.

If I do `cat sample.txt` — now what do I want to do, I want to **delete** lines. So how will I do it? For that the command is: simply `cat`... `sed`... after that what do I have to do — [lines] 12 to 15; from 12 up to where do I have to do it, up to 15 I have to do it. So we will do it like this, and simply hit enter.

Otherwise, the other syntax of this — we can use that too: we will use the `sed` command, and after that, instead of giving `cat -n`, we can give the file's name with this itself. In two ways — you know how you can do it.

Let's perform a bit. Now look, from 12 to 15, our line numbers — it **deleted** them.

```bash
sed '12,15d' sample.txt
```

### Delete everything EXCEPT a line

Now if I show you a file — first let me do this, let me save it. If I do `ls` — `sample.txt`. Okay.

Okay, `sed`, after that what I am going to do — single quotes; after that we are going to use line number `12`, and after that we will use this **exclamation mark `!`**.

What does this mean — **NOT**. That line 12, the line which is number 12 — **leaving that aside, delete all the lines.** Simply we will use the `d` option with it, and hit enter.

```bash
sed '12!d' sample.txt
```

Now look, in this what did it do — it deleted [everything else].

### On-screen vs in-file

But the thing is, you know that here it performs **two types of operation**: one is on screen, and one in the main file. But up to now you have been performing the operation [on screen] — how will our command work, with which we want to perform the operation? So we have done it and seen it.

If I have to do all these things inside the **main file**, have to perform the delete operation [permanently], then simply I can use **`-i`** with it.

```bash
sed -i '12,15d' sample.txt
```

---

## `sed` — Insert operation

Now, like — what do I have to do — that was how we can perform a delete operation with the stream editor command.

Now next, inside this, I am going to tell you **how you can insert your text before any line number.**

For that, simply — like, I do `cat sample.txt`. Now what do I want: above line number 57 — what do I want to do — before this I want to **insert a line**. Which one do I want to [insert]?

So how will I do it? Simply `sed`, after that `-` — sorry — [`57i`] "Hello, I am [a] practitioner". Simply the file's name, `sample`; after that what to do — simply [enter].

```bash
sed '57i Hello World' sample.txt
```

Now see — here it is, 57 — because it is working **on screen**. So look, here "Hello World" got added, and above it was line number 57. In the last [class] we had shown you inserting; so you had seen that.

So what is happening — it's happening **on screen**. If I had to insert **inside the main file**, then how would I do it? Let me show you with [`-i`].

Now at [line] 58 "Hello World" will get added — **permanently** changed inside the main file.

```bash
sed -i '57i Hello World' sample.txt
```

So this was about our `sed` command, about the stream editor command — explained in very [good] detail. Whatever is inside it — okay.

---

## Why `grep` matters: the log file scenario

We have a **log file** with us. Meaning, what is it — there is a log file, a log file.

Now what is a log file — you all must know. On Linux, or [if] you are a cyber security engineer, you [work in a] SOC channel [SOC centre], or you are doing continuous log monitoring duty.

Now what happens is that when you were doing log monitoring, some attacker tried to hit your machine. Even if his username came, or his IP address came on your screen — now what did you do, you recognized him; he came into your notice: "yes, something has happened, something is **anomalous**" — that something happened different from normal, other than what happens on a daily basis; that is what we call it. You identified it.

When he was hitting, what did you do — you noted down his IP address, or you noted his name, added the name; and on that, whatever you did — after that what did you do, you collected information about him and tried to tell that user.

Now the user is saying "I didn't do it" — he is **denying** it. But [you] know that in the log file you will find his entry.

For example, if you do searching inside it [manually], it's a very difficult task. If you sit and search manually like that, it will take you hours, and even then you will not be able to search for that thing — because every time, what is a log file? It keeps getting **updated**, every second, every [milli]second.

Now, to do this thing — instead of doing it manually, to make that work easier — we use [`grep`]. In it, what do we do: we give a **pattern**. We know that when he hit, a pattern would have come — where all, in which lines, you get to see it. So that your work becomes very easy and you will be able to identify it.

Look, this is a log file. When you tried to attack with the server, the server has logged it, and you were denying it. Now look at this — in how many places, in this line, on this line number — your log has come to us; the entry has been made. Now he cannot lie.

So to do all these things... because most of the work is Linux — because totally, whether you do ethical hacking, do cyber security, do anything, or become a Linux admin, or work in any company — the most used are Linux; the main servers are of Linux only. And for performing attacking too it is used, and for [other] tasks too — for everything there is Linux.

To make our work easier, we use different-different commands. All the work — printing work — it does so easily.

Here, if you used the `cat` command, after that you searched in it; used the `less` command, then searched in it; used the `more` command; the `head` command said [search] only from the top — top-to-bottom it searched; [`tail`] searches from the bottom; now [`sed`] searches according to line number.

Like this, every single command has been built according to its own [purpose]; according to the requirement, different commands are used. But all the commands we discussed [in the] last day — I had mentioned a series which we are going to start, which we are going to discuss on — they have their own roles in their own fields. Okay? Because that option is used in its right place.

Because a command's importance extends only up to a certain point; after that what happens is that its **limitations** come. To fulfil those limitations, another command has come. So as we discuss all these things, we will come to know which command we should prefer how much, and how much we should not.

And the 10 to 15 commands I am telling you about now are **the most important commands** — because if you have done these, after that, wherever you work, whatever you do, on top of this your work will become very easy, because your work in real [life] will become very easy.

---

## `grep` — searching patterns

Come on, let's talk about how we can use this `grep` command, how we can search patterns. I will tell you about it quite deeply; next, all of its flags, I will try to tell you about them.

Come on, let's talk about the `grep` command. Its straightforward use: **`grep` is used to search a pattern in any file and any command.**

**Syntax** — if I show you on screen, its syntax is:

```
grep [options] pattern filename
```

After `grep` you have to provide the **options** — whatever option you want to give, if [you want] options with grep; after that you give the **pattern** which you want to search; after that you give the **file name**.

Or: `... | grep [options] pattern`

After that, wherever the pattern matched, it printed that line in front of your screen.

Now see — this file was something like 2017 lines; out of that, how easy it became to grab a particular pattern.

### `-n` — show line numbers

Now we want — whichever pattern we search, [shown] on screen — I want to see its **line number** too. It's not that I can't even tell in which line number this pattern that I grepped was grabbed. If I want to know this too, then simply for this I will use a flag:

```bash
grep -n root demo.txt
```

Pattern name `root`, after that the file name `demo.txt` — in which you got the `root` pattern; [for example] at line number 390.

### `-c` — count matching lines

Now I want to **count** this pattern. On screen, what do I want to do — I want to count the **total number of lines** and write [it]: how many total lines there are inside which this pattern has been grabbed, or this pattern has been detected, inside this particular log file.

So how can I do that? For that there is an option:

```bash
grep -c root demo.txt
```

And now I will use `root`, and then `demo.txt`. So there are 12 lines.

### `-i` — ignore case

Now let's talk — now what am I doing: now searching a second pattern. Now what am I doing — right now, think: this `dns` that is there, is it in small [case]? If any of these `dns` words were in **capital**, then it will not grep it — because you all already know that **Linux is a case-sensitive operating system.**

Whatever you write in front of it, whether inside single quotes or inside double quotes, it will print it out on your screen.

So what do I have to do inside it — for that I will have to use the option:

```bash
grep -i dns demo.txt
```

Now, like, here the `dns` that was in capital too — it showed that too in the output on your screen. Because **it is not necessary that the pattern we are trying to grep is in small [case]**; it is possible it is in capital, the one we are trying to find. So what did we do — the case sensitivity, we **ignored** it.

### `-o` — print only the matched pattern

Now, what is [next] — we want that wherever it is available... now what did we do — we had taken the example that now we want that wherever `root` is available, now I don't want that [whole] line; I only have to **print this word**, only this word, this pattern — I have to print this.

How can I do that? For that I use `-o`:

```bash
grep -o root demo.txt
```

My pattern is `root`, after that — it did not print the whole line, but whichever line had `root`, it printed **only that pattern**, only this one.

Now what is the benefit of this — that if we want to [extract] only this pattern from somewhere, we can do it; if [we] want to do something, then in that way.

### `-v` — invert match

Now let's talk about how we can do an **invert match** — meaning, the pattern that I am trying to match, **leaving that pattern aside**, print all the rest on your screen. How can we do that?

```bash
grep -v root demo.txt
```

What I did — I did `grep -v`; what am I doing — `root`; leaving `root` aside, [print] everything inside `demo.txt` on my screen.

**Multiple options can be used together.**

Here I have explained to you people so far: what `-i` [does] — how you can make case-sensitive into case-insensitive; how you can print with line number; if you only want to count; if you only had to print that pattern on your screen; or otherwise if you want an inverted match, in the sense that you want to see everything except a particular keyword on the screen — you can do that too.

In which cases can you use it? It may be that you have a small file and you have to [exclude some entries]. For example, we can take: a school attendance register, or [a list of who] was present — okay, one by one, what will I do, I will highlight this one; apart from that, leaving that aside, I am printing all the rest. Like that — we can take such an example here.

### `-w` — exact word match

Let me show you one more useful case of it, how we can use it.

Now, for example, what am I doing: I added a user, `manish` — M-A-N-I-S-H, `manish`. [In] `/etc/passwd`, I only want to see this `manish`; I have no concern with [other partial matches]. What do I have to do — I have to **exactly match**.

If [I want] an absolutely exact match pattern, and this is the pattern — if you want to exactly match, for that too a flag is used: `-w`.

```bash
grep -w manish /etc/passwd
```

After that what I did — `manish`; it printed `manish`, after that `/etc/passwd`. I hit enter. Now you see that this will show your pattern in the output **only with an exact match**.

### `-B`, `-A`, `-C` — context lines

Now let's talk more. Look, now what do I have to do — up to now what I did was that the pattern I grepped, it showed it in the output on the screen.

Now it may be that I want to see — in my log file, I want to see that the pattern I grepped, I want to see four or five lines **above** it, and I also want to see four or five lines **below** it. So how can I see that? For that too there are some options.

For example, what am I doing — `dns`; after that, which line number is it — line number 1557. I want to see four or five more lines above 1557; I want to see what type it is, what logs have been made, whether I can find something more related to this.

So how will I do it? Simply I will say `grep`, and `-n`; after that what I did — `-A`... what does `A` mean? **After**. Okay, sorry, I want to see **before** first; after that, how many lines do I want to see — I want to see four lines, `dns`:

```bash
grep -n -B 4 dns demo.txt     # 4 lines BEFORE
```

After that, along with it, the four more lines that were there — it printed them with the output.

Now what do I want — no, at 1557, the line where you see `dns`, I want to see four more lines **below** this. I won't [see] before, I want to see **after** — what is in the after. So I can see that too. Simply, here what will I do — I will use **capital `A`**:

```bash
grep -n -A 4 dns demo.txt     # 4 lines AFTER
```

So this will be shown to you. Enter. Now see, after 1557 too there are four lines; it showed: "yes, after this is this in the log, after this is this, after this is this." With this, I will become more clear about whether I am actually finding out what I really want.

What do I have to do — the pattern I am grepping, I want to see four lines above and four lines below **at once**. For that too there is a flag. Simply what will you do — you will simply use **capital `C`**, and after that four lines above, four lines [below]:

```bash
grep -n -C 4 dns demo.txt     # 4 lines BEFORE and AFTER
```

Now see, in this, the pattern that matched — from that pattern it showed the four lines above and showed the four lines below, in the output on your screen.

### Space-separated patterns

Now let me show you a thing: if there is any **space-separated pattern** in your machine, in your log file, which you have to grep — then how will you do it? You cannot do a space-separated one like [this].

What I did — I did `grep`; now I put... let me add one more example first inside it; whether it will be in this or not — let me first add it inside this. I did [it], I added this too.

Now what do I do — I want to grep this very thing. How will I do it? You will simply do... and what I did — `dns`, and after that what did I do — the name; after that what am I doing — `dns name`; and after that simply the file [name].

Right now, with the latest version, `grep` has also been updated, so now this works. But the thing is, [if] only the space-separated line and directory — it didn't get it; simply what it is doing is that it is case-insensitive, whatever it is; it took `dns` [and] more parameters, space-separated — it showed all of them here in front of your screen.

But the thing is, **if you gave it space-separated, then it understood that this is one file and this is a second file.** But if you have to do this type of searching, then how will you do it? Like, what do I have to do — after that I take quotes; after that what do I want to do, `dns name`; after that, if I search, [it's] clear.

```bash
grep "dns name" demo.txt
```

So in this manner, if you want to [search] any pattern with a space, then you can do it in this manner.

### `^` — lines starting with a pattern

Now let's talk; let's move ahead in this.

Now what do I want to do — the first pattern I had, the `root` one, I had tried to search in the log file. Now what I want is that **I want to print only those lines which have that particular pattern at the beginning.**

For example, I had taken `root`; the lines which have `root` at the beginning — only [those] lines is what I want to print; I don't want the rest. So how will I do it?

For that the command is `grep`, after that single quote or double quote — you can give anything; after that you [use] the **`^`** symbol, this one which is above [the 6 key]; after that what do you have to do — `root`, the pattern's name; simply after that what to do — write the file's name:

```bash
grep '^root' demo.txt
```

It printed [those lines] in front of you — whereas last time when I printed `root` at the start, the pattern, it printed 12 to 13 lines; but now it did not, because now I have specially told it that "the lines which have this pattern **at the beginning** — print only those lines."

### `$` — lines ending with a pattern

Now what I want: **if this pattern is at the ending of a line, I only want to search that.** Simply, what will I do — **`$`**.

```bash
grep 'root$' demo.txt
```

So, the line at whose **end** this pattern is — it will do that. But it showed nothing, because this pattern is not at the end of any line.

If I search some other pattern — for example, what do I do — [`bash$`], hit enter — this is also not a pattern. So I [know] — `nologin` will definitely be found:

```bash
grep 'nologin$' demo.txt
```

`nologin`, enter. Now in this file, whichever lines have [it] at the last — it showed them in the output on your screen.

Now next — so I have told you: if the pattern is from the beginning of a line, how to print that; and how to print from the ending — you would have come to know.

---

## Practice question

Now let's talk — here I give you people one more practice question. If you people, like — yesterday too one or two students did it; the rest of you also, if you wish, can do it. If you people feel that it's a waste of your time, that you don't have time, then don't [do it]; I will not post [about] it, I won't say anything to you. For that, if you want, you can do it.

Let me give you people the practice question. What is it — you have to find out a particular pattern. [Music]

> **Choose some pattern of your own between line number 25 and line number 35.** What do you have to do — you have to get that pattern shown in the output on your screen, with the help of the `grep` command.
>
> **The condition here is: you must not grep the entire file.** You have to grep only [lines] 25 to 35, and inside that itself you have to search that pattern.

How will you do it, how will you not — this you know. So its output, the command that you use — after the video is complete, after the class is complete, you can send it in the comments section, like the one who had sent it in the last class. For that — he did it; otherwise nobody knows, nobody did it.

---

## `grep` on command output

So that means — now let's continue. For example, `lscpu`, which shows your architecture — what do I want to do: this pattern, I want to grep this pattern. How will I do it?

Look, how will I do it: I used the `lscpu` command, pipe symbol, after that `grep`, after that this `-i`; I wrote on my screen this pattern which I want to search; simply, I hit enter:

```bash
lscpu | grep -i <pattern>
```

Now see — out of such a big [output], it showed exactly this in the output on your screen. **How helpful it is**; how easy it made your work — the output you want to see on your screen.

If you want to make a report for someone, want to mention [it] in some report — that only... but now in that report you don't want to mention all the matter — then in this manner you can grep and [take] that parameter on the screen, save it inside a file, and give the report to anyone.

Now [suppose] I want — here it is, `CPU op-mode`, a `Model name`. If I have to [grep] this "Model name" — since there is a **space** in "Model name", I have already told you how we will do it. `lscpu | grep -i` — I shouldn't use [it plainly].

Now what do I want to do — "Model name"; if I write it directly like that, then you will not get the output you want. Simply what I do — I add it inside **double quotes**:

```bash
lscpu | grep -i "model name"
```

Now see, in this it did it — "Model", "BIOS Model name", or whatever it is — it printed the two out on your screen.

So this was how you can use `grep` even better. All these things you get to see in live.

---

## `egrep` — multiple patterns

Now what I want — I want to **search multiple patterns**. How will I search multiple patterns? Because not every time — I'd do one pattern, then fire the command, then I'll use a second pattern, then fire the command. **No, I don't want it.**

Suppose I have to search multiple patterns; how will I do it for that?

Look, if [I did] what I did — now what will you do — you did: in `demo.txt` I want to search `root` too, and I want to search `ftp` too, and I want to search `dns` too. Simply, `demo` [file].

Now this actually did not work, because we have already seen this: in it, only `root`, only one pattern — keeping this in mind, what did it understand? It understood [the rest as] file names. Now there is no file by [that] name; [there] is a file inside which you got to see the pattern in these lines.

So, brother, now how will we do it? I have to search multiple patterns, so how will I do it?

To do this work we use the **`egrep`** command. I showed you — we use it for searching this pattern, multiple patterns.

**In the command there is only one difference:** `grep` can search a **single pattern**, whereas this command can search **multiple patterns** inside a file. Apart from this there is no difference at all — all the flags are used [the same], the output comes [the same]; absolutely no difference. Only one difference: single pattern and multiple pattern.

Now, for example, what do I have to do — if I wanted to search these three patterns inside this file, how? After that what will I do — single quote, after that like `root`, and **pipe symbol**, after that `ftp`, pipe symbol, and `dns`, and after that what to do, the file's name `demo.txt`:

```bash
egrep 'root|ftp|dns' demo.txt
```

And let me use it — it showed the `dns` pattern on the screen too, and the `root` one too. And although perhaps `ftp` is not in this, so that is why the `ftp` pattern didn't appear, nothing showed on your screen.

In this manner we can search multiple patterns too. But [the output] will be absolutely the same.

If [you ask] what this means — for that we have to use a special, an advanced option. But if you feel that [you want] to do multiple options — so how can you do it with the [`grep`] command? We will do it with [`-E`].

Now what I did — inside it I gave `root`, and after that what am I doing... [so we] searched multiple patterns inside any file.

### `fgrep` and multiple files

Now what I want to do — searching one pattern. If I want, I can use it with `grep`, but let me show you once by using it.

Look, what I did — I did `fgrep`; I go `root`, `root` — inside this, one is the `passwd` file; I want to search inside this. Inside `/etc` there is a file of mine, **`group`** — G-R-O-U-P; I will tell you about it in very [good] detail; there is a file named `group` — I want to search inside this. And one more inside `/etc` — I want to search [in that].

[Music] So I can do that too. How will I do it — `-f`... **capital `-F`**; after that what will I do, after that `/etc/group`, and simply enter:

```bash
fgrep root /etc/passwd /etc/group /etc/shadow
```

Then too it will work the same, as we did with the last command.

Let me tell you one more thing: but the `grep` that is the latest, the one that works right now on this machine — right now what is it, **by default it has been merged** with it; there is no need to give [the separate command]. So simply, even if I use it **without the `-F` option**, it will show you on your screen. So simply, it's fine — because it has been **integrated** into the `grep` command, that flag; now you don't need to mention it separately.

But if it is that you have to [use] the flag, then you will have to use it — if you want to search **multiple patterns** in a single file.

Now what am I doing — if what I did was... let me do one more thing and show you in front of you. What I did — I did a `grep`, after that hyphen; I did [`-E`], after that `-F` and [combined], and everyone knows what this means.

And I am saying, after this `root`, inside `root` what am I doing — `ftp`; after that what am I doing — that **multiple patterns, multiple files** — [plain `grep`] does not work on a single file [for multiple patterns]. To use `grep` for multiple patterns, for that you will have to give the [`-E`] option. Then you will get the output nicely, the one you wanted.

So this was the thing about the `grep` command — the information about how you can use it.

### `-r` — recursive search

Now let me tell some things: a problem comes in front of you, like — **we forgot the file's path.** The file I wanted to search in, I forgot its path.

Now I only remember this much: "yes, inside [somewhere] there is a folder named `default`; inside it there are a lot of files, and among them, in some one file, that pattern [exists]" — or that particular file is the one, that pattern is in some one [of them]. But up to this point he is guaranteeing it; but after that he doesn't know where it is.

If I want to find that out, then how will I do it? For that there is an option. If you do `grep` — I have an example of it; right now it isn't coming to mind. So do `grep`, you will use **hyphen capital `R`**, the pattern, and whatever path you know, so `/etc` for example:

```bash
grep -R pattern /etc
```

What will this do — first it will search inside `/etc` itself, inside the defaults; after that, [for] all of these — **recursive** means simply that it will go on searching this pattern inside every single one; after that it will show your output on the screen.

So — about the `grep` command and about the `sed` (stream editor) command, [that was the] information. So I hope everyone would have understood up to here. Tell me once in the chat — if someone feels that they did not understand these things, tell me once in the chat. [Music]

---

## Why only two topics today

Okay, so let's keep this much for today. What we will do — today we will teach only two things; we won't do too many things now, because there is no benefit. However much [we] teach, [only] that much will come — because I know that there is no value [in overloading].

We know — understand it like this: it's not that; we have made your content so powerful that we have not done time-pass. So no problem, because what we started — I deliver it to you wherever, whatever; there you provide attendance too. There, what happens is that... [Music]

You will see the recording. I say that really it's not necessary — what we do is provide you live [teaching]; we provide that thing.

One thing we have to do: **we are teaching in a pattern**, so that you people, in your field, gradually — when you join with us through this channel, when you complete all the things, then one day you will realize what you learned with us. Because we know in which manner you have to go forward, in which manner you people have to study, in this manner you should do it, from whom you have to learn.

**We are the experts** — some of us have five years', some have 7 years' experience. We are absolutely not [the kind] that "yaar, class today and today we told you [something]".

---

## Doubt session

Okay, so let's do one thing: let's keep a **10-minute doubt session** — whatever you have to ask up to now related to this. Right now it's an open session for the next 10 minutes; so you people can ask in the live chat, I will answer you.

Hello — you people can ask anything, wherever you have a doubt up to now: Day 1, Day 2, [Day 3] — whatever doubt, "I didn't understand, I want to ask something" — you can ask. The doubt session is open for you right now and for the next 7–8 minutes, 5 minutes, 10 minutes; you can say anything. So you can ask questions in the chat.

### Q: Public and Private place (recap)

"In the fourth class I was absent" — [Music] tell me; tell me once.

We tried to make you understand with an example: when you use this, how will you use it — in private and public place. We explained it in this manner.

What did I say public/private place means? That in Linux, **two types of users** work:
- One is the **admin**, which we call the **root user**.
- One is the **normal user**, who has no privileges — meaning they have nothing; just normal, they will work only where the work has been given to them; apart from that they cannot do anything at all with the machine.

Now what happens is that — the File System Hierarchy we told about, or when I took that Day 1 class, I had told that in Linux there are around 17 directories in the machine.

Now, in Linux, what is it — **on every directory some permission or another is defined.** On the `bin` directory some permissions are defined, and [on] the home directory — on that, all three permissions are defined: you can **read** inside it, you can **write** too, and you can **execute** too; all three permissions are there inside that directory.

In the same way, on every directory some permission or another is defined.

Now, the home account which is your own, the home directory — that has been called the **private place**. And after that, whether you are a normal user or you are root — after that the whole [rest] has been called the **public place**.

**In your house you can do anything**: you can create any file, delete any file — you have full rights; inside it you can do anything, inside your home account. That is your house; you'll go by [your own rules].

Now let's talk about the **public place**. In a public place you have **no right** to do all these things. You simply have to behave like [you would in] a public place: whatever permissions you have there, you will work only according to those. Apart from that you cannot work according to your own wish, inside any directory.

If on some directory it has been said that you have **read-only** permission — what does read-only mean? That you can view its contents, can read them, but you can neither do any modification inside it, nor change anything inside it.

If these permissions are on some directory — it is a public place — then who can change it? Its **admin** can change it; apart from him nobody can change it, [that] which is defined.

**Generally speaking:** in your house you can do whatever you like; but when you come outside your house, then you have to live according to the **society's rules**. After that you come onto the road, then you have to follow **road traffic rules**. After that, [if] you have to talk to some person, whatever problem there is — after that, you have to follow a lot of people['s rules].

In this manner — Linux, why — if you compare it with the outer world, then basically your home in Linux... the home would be treated like a **private place**; and just as you step out of your house, in the same way in Linux when you step out of your house, that is your **public place**. There, what is it — there are completely different rules, and you will have to follow them, because they have been **forced upon you**; you cannot [change] them. If [you] tamper with them — obviously, you know that if outside there is civil [order], after that you compare — then the **government** [decides]; in the same way, who is the government? **Root** — the one who is its admin.

So I hope you would have understood well what public and private place is. Because as long as this is clear in your mind — where I can work and where I cannot — then whenever you work with any file at all, you are not going to have a problem in future, ever, because a **mindset** will become clear to you: in which directory I can work and what I cannot. And whenever you work, you will find it quite interesting too. That's it.

I hope — Prince, tell me in the comment that it would have become clear to you. Any other question from anyone's side? Still not understood, understood? Okay, thank you Prince.

### The key learning advice

So now, that thing — if you **compare things with the things around you**, the surroundings where you live, the home, however it is — then whether it is cyber security, it's like that.

**Once you learn to compare those things with the outside world**, then the computer world — leaving aside the word "cyber security" — if you understand your whole PC world, whatever work you do inside that PC, whether it's the operating system, programming, or anything at all, as you work — then if inside that, if someone is teaching you properly, someone is telling you, giving you **conceptual knowledge**, and if you try to **correlate** that concept with the normal work you do, then, by God, truly you are going to enjoy it a lot. **Only then does interest get built**; otherwise you will get bored and keep [it aside], keep [it aside].

In the world, I never [give] return to anything — sir, practical work happens, and apart from this no work happens. You will be able to [do it in] practice when you connect it with the things around you — like private/public place, we simply connected it with our home and the outside place; so then always what is it — it will stay in your mind: "okay, work like this", because just as you can behave in the house, in Linux too you can [behave] like that. Simple.

### Q: stdin and stdout (recap)

The next question was — simply, simply, simply. Okay: **stdin and stdout.**

Look, if you have studied my file descriptor topic: what is a file descriptor? That there is a **table**, to **track open files**, by the **kernel**. And that same table — what is it — it also helps other programs, or helps the process, so that it will come to know: the file I am trying to access, the file I am trying to open — all these things it comes to know.

But this table that is there — in this, [regarding] the process, any modification, any updating, if anyone has to do anything at all — and its **first three entries**, you will find them in all [processes].

Because think of one thing: you are firing any command on your screen — with what are you firing it? The standard is that if you do anything with that program — by default, in the command, like I'm taking the example — **your keyboard is the default**, because whenever you type inside that keyboard it appears on your screen.

After that, what do you do — as you hit enter, meaning that is a process: whatever command you fired, whatever input you gave from the keyboard, after it is processed — now what do you do, you **wait**. Because you wait that "I should get something or the other, only then will I know whether what I did happened or not."

Now that work happened — meaning, whose wait are you doing? If you ever go [into] — whenever you look, when you learn programming, then see: **by default, in any operating system, the standard input is the keyboard.** By default, [for] any program, your PC's screen or your laptop's screen is your default — "you did some work; now how will I know it got done?" We will call that **output**. So **standard out** by default — these are: one, your keyboard, and one, your screen.

**stderr** — which we call **standard error**. Now, brother, you did some work and some error came in it; now that error came, so that too has to be detected, that too has to be known. If an error came and you did not show it in the output, then too there is a problem, because you are not even coming to know; if you are waiting "yes, it will happen, it will happen" and are sitting for hours...

So now we have to see the error somewhere too — that is why for that too, brother, the standard that has been maintained, of standard error, that too is **your screen**, or the **terminal**.

**In [which] cases do you [redirect] in cyber security, anywhere?** What do you do — instead of these three things being according to [the default], give the input of some **file**; it will read from that and give you output. Then, if you want, whatever that output is — make it the input of something else; make **stdout** the input of something. Sorry: standard output — make it something's input. And the output coming from the input, if you want that "no, I don't [want to] see it on the screen" — then save it inside some file.

So **totally**, what are you doing — however many commands you are firing on the screen, all of them...

Now look, what I have done: I have written a command here. If I think — right now, here it is: here, what is this? **stdout** is coming on the screen; this is fine. The command's options are there; according to the command, logic has been applied inside it about what I have to do.

But look at this — this is **stdin**; I took it from the keyboard, I took it only for the terminal; after that, look, I took it from this file — my input, stdin, I took from here; and here too I took stdin. After that, this is my **stdout**.

If there were any **error** in it, what would happen — right now by default, what is it, it appears on the screen. If it has to be [redirected], then simply what do you do — you use **`2>`** with the greater-than symbol, because [stderr] has [descriptor] 2. If you have to redirect it, for that you have to put a `2`.

But `0` and `1` — **stdin is 0 and stdout is 1** — those are by default with those symbols; you never need to put them.

That is why I had said that after studying my file descriptor concept, revise it once or twice; after that, the class that was on Day 3, the one that Nitesh sir did — okay, skip the first part; apart from that, what he had told, the commands he explained, that this is input or output redirection — if you correlate those once with this concept, then I can understand that **I have made the best concept**.

Now I have delivered it; ever — [whether] in scripting, or even in understanding any command — you are not going to have a problem, with **stdin, stdout and stderr**.

Let me tell you one thing: people do B.Tech. B.Tech people — when I was teaching a class, my first [batch's] class, then I asked them: "Yaar, are you working in B.Tech? You are in the last, final year, so you would have quite good knowledge of operating systems." They said, "We have no idea about it; we never studied where [it] comes."

So these are things which you don't find anywhere; but we **researched** it and discussed it in front of you. That is why — we compared it with [things]. **Knowledge about file descriptors you will get very little of, and whatever you get will be confusing** — [because] the deeper you go inside it, the deeper it is; because very deep knowledge of the operating system is needed, especially about [the architecture] and its organization, how it works. You will find many things — "yes, how a program is loaded, how it happens." But right now you don't need that much.

But whatever basic concept you knew, [you have to] correlate it — with any command, at the time of writing any scripting. So this is for you.

Next — okay, Prince, tell me. [Music]

Whatever you do — [if] you have to give some input, even if you install a package inside it — right now all these commands, you know them — then what is it, your work will become very easy in Linux. Because most of the work of ethical hacking, most of the work, or even inside [a SOC], anything at all — most of the work, what, happens on Linux.

So I will develop such a development [of] knowledge in you in this capsule course; after that I will tell you how you can use it. Because how to use it, I will keep telling you along the way.

Because look, I am telling you: what is going on right now — your concept is going on that, from the last class, [the] descriptor — after that, all the commands that are going to happen, **totally their whole game** is about how you have to grep whatever output there is. Basically you can go through a file of lakhs of lines; how you can see the output inside it.

Every command has its own limitations; every command has its own working [colour], you can use it. `grep`, `sed` — when you will be doing **scripting**, then they are very, very helpful.

Now look: any output — you will cut it so easily, so easily, big-big [ones] — because if someone gave you [a file] that in line 443 there is this, in 43 there is this, in this I only want — what do I want, this; inside this, this file name, okay; and inside this, what is it — I want this keyword, okay; apart from that then I want this last one...

If I have to cut all these things and give them, then how will I do it? You wouldn't have an idea, right? How will you do it — you will open it inside an editor, after that you will cut/copy/paste it, waste so much time. **Does anyone have that much time in life? No, they don't.** So for this there are all these commands — this work will happen for you in seconds.

So, like today, what I did — like this we will keep [holding these] in between; and you keep notes, keep noting down; we will clear it. After that, automatically, as the next concepts happen — when we do them along with these, it will become separate/clear to you: "yes, that day I needed that thing from there, and after that thing I am implementing it here." So that thing — we will connect such things like that. Don't worry, this knowledge of yours is not going to be [wasted]. It's my [promise].

Tell me. Okay, so then right now nobody has any doubt, so I can understand — all who are out there in the live, with them still... nothing is unclear? Everything is clear? So we'll get the session over.

So, bye bye, good night.
