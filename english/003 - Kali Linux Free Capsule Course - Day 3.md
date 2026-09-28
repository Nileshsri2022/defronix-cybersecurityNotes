# 003 — Kali Linux Free Capsule Course — Day 3

**Source transcript:** `transcripts/003 - Kali Linux Free Capsule Course - Day 3 [ Hindi ].hi-orig.srt`
**Trainer:** Nitesh Singh (Founder, Defronix)
**Topic:** Input/Output Redirection & File Descriptors
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the auto-captions are noisy in places (`लिरिक्स`/`नेक्स` = "Linux", `करनाल` = "kernel", `फाइल डिस्क्रिप्शन` = "file descriptor", `ल एस` = `ls`, `आईएसपी`/`नल` = `/dev/null`, `टी कमांड` = `tee` command, `ग्राफ`/`ग्रिप` = `grep`, `विम` = `vim`). The intended technical term has been restored where unambiguous.

---

[Music] Okay, so hello everyone, good evening. I think we are good — so you know. Come on, so okay, let's start; we will continue onwards from there.

And first of all, I would like to introduce myself. So I am **Nitesh Singh**, and I am the **founder of Defronix**, basically. And today — today we are going to study quite an interesting topic.

You people just tell me this: is my voice reaching you clearly? Please, please, just tell me this, whether my voice is clear to you people. Okay, alright, thanks. Okay great, absolutely clear.

**Redirection.** Okay — **Input/Output Redirection**. Okay. And it cannot be completed in one session, like... I'm normal [about that]. So in this session, as much as we can do — first of all, **we are going to understand** where this input/output redirection is basically going to come in useful, in what manner it is going to come in useful. We'll understand all those things.

---

## What is Input/Output Redirection?

Now look, what happens — right now, and here, here we talk about input/output redirection. Okay. Input/output redirection — **what is this input/output redirection?** Okay.

Now, in your system, you all must know that there is an **input device** and there is an **output device**. This is a very basic concept — a very basic concept, very basic — and you just have to understand it. Okay?

An input device is where we take input from; an output device is where we get output. Simple. [Music] ... A general input device, very basic, is our **keyboard** — absolutely right — and a basic output device is our **screen**. Simple: your screen, or your display. Okay?

We just have to **redirect** this input and this output. That's all input/output redirection is.

Now this redirection that happens — it happens in many, many ways. There are many kinds of concepts in it, many kinds of things, like different methods, the delimiter concept; after that, like — you can have the concept, there are others as well, like you can say... meaning, there are so many concepts in it, so many, that if we study it in full detail, then brother, it is not going to be completed in one session; it will take quite some time. Okay?

So I am taking you along from the absolutely basic level, taking you from the very start, and I will try to give you the maximum things in it. Okay? Then again, file descriptors and so on — many things.

Now here, let's first talk about: how does this input/output redirection happen, and why do we need it?

---

## First example: redirecting `date`

Now look, let me first show a small example of this, and then I will explain this thing to you properly. Okay?

For example, suppose I opened a terminal here. Let's suppose I opened this terminal here — I think it'll be visible; let me increase its font a bit more. Okay, what I did here was open a terminal.

Now, what I am going to do: here, let's suppose, I run a simple `date` [command]. A simple `date` command, we ran it. When we ran the `date` command — from where did we take the input? We took the input from our **keyboard**. Okay? To type the command. And where did we get the output? We got the output here, on the terminal — that is, on the **screen**. So our input device is the keyboard, output is our screen.

Now we have to redirect it. Redirection is very, very useful when you go a bit deeper — kind of, when you go into **error [capturing], error logging**, all these things: if you have to do system log, system error logging, or you have to do error logging of some program, capturing — in all these things it is used a lot, generally. Okay?

Generally we use it like: sending any output somewhere else, into some other file; taking input from somewhere like that — different kinds of things.

So suppose I have the `date` command, a very simple one; let me explain to you. Okay? Suppose this is my `date` command. Now what do I have to do — this `date` command's output here...

**What does "redirect" mean?** It means that the input you are taking — its output too you [can] direct; and an input, [you can] direct. If you want to redirect **input** — meaning, there is some other thing, some file, and you want to feed its input into something else — you can do that. And if you want to put some **output** somewhere else, into a file, you can do that. Simple.

The `date` command came. Now what do I have to do — let me do `ls` on the Desktop. On the Desktop there is no such file; let's do `ls -a` — so obviously there is no file here. It's a simple thing.

Now what do I have to do: this `date` command — I don't want to print it here on the terminal; I don't want to print it directly on the screen. Where do I want it? I want it inside a file, let's suppose.

So what will I do — I will use this **greater-than symbol**, and I will give the name of the file in which you want to print it. So I gave... let me give `date.txt`: `date.txt`. I took this file and hit enter. Simple.

Now if you look — if you do `ls`, you will get a file created: `date.txt`. That's it.

Now we'll view it: `cat date.txt`. This is a command for viewing a file. Right now a lot of Kali commands will be told to you from the absolute basics, okay, so don't take tension about "sir, what is this, what is the command."

Simple command: `ls` is used to view whatever directories and files are there at whichever location/directory you are in. Here we gave a greater-than symbol — this is a very useful symbol; I will talk about it in detail, what it is. Why? Because on giving this, its output will go into `date.txt`. And here we used the `cat` command, which basically shows the contents of the file on the screen in front of you.

So I did `cat date.txt`. Now look — you are seeing here, this date has been printed; it has been printed into the `date.txt` file. Look, let me open this file; let me open it graphically and show you.

Look at this, are you seeing this here? This file — look, let me make its font a bit bigger. Okay, here it got printed.

Now this `date` that I printed — this did **not** print on my screen. Look, when I simply entered this `date` command here, **this date did not print on screen**; where did it happen? It got printed into `date.txt`.

Now this concept is very simple, but very interesting. It looks very simple — "what, it just got printed over there."

### Overwrite (`>`) vs append (`>>`)

Now look at one thing; I will come into full detail. Now what do I do — let me run the calendar here. Okay, so it's not installed, so let me install it, no problem — the calendar, it comes from `cal`... from the repository. So from there we installed the `cal` command. Okay.

Now here, the `cal` command — enter `cal`; this is the calendar, you can see it. Okay? So I got the calendar for June 2023 here, whatever was the latest.

Now what do I do — let me try giving the `cal` command's output into this file, into `date`. And I hit enter. Now I did it — now this also went into it.

Now let's open this file graphically once and look. Look at this — I opened it graphically to show you: so, do you see anything here? Let me remove these numbers, the line numbers.

Now what you see: the `date` command has **disappeared**. The output that was of the `date` command — it has completely disappeared. And what came here instead? Here now — so the date, brother, disappeared.

What does this mean? That when we ran this command — simply, I think our terminal is open, is it open? Here it is — when we ran this command, what it did was put the `cal` command's output into `date.txt`, and what did it do to our earlier command's [output]? It **replaced** it; it threw it out and put this one's output in.

But if you want that "no, I don't want to throw that thing out, I now want to put the `date` command's output into this same one again, but the calendar output should also remain" — then for this we use **double greater-than (`>>`)**, and then what we do is put `date.txt` there, and hit enter.

Now when we did this double-greater-than, it means **append**, and this one [single `>`] means **replace the output**. Okay?

Right now I'll come to this; many things still to be told. If you open `date.txt`, then look — here, first the calendar's output that was already there, that is there; and after that your `date` output, that `date` output too has come here. Both outputs are basically visible to you here. That's it, got it?

This much you would have normally understood — normally you might have understood that yes, this thing is happening normally here. Come on, okay.

---

## The concept: redirection symbols and file descriptors

Now let's understand the concept, what these things are. That — I've told you the example. Okay? Now let's understand its concept a bit.

Look, in input/output redirection, when you are talking about Linux — here, this symbol, this greater-than symbol, its meaning is **overwrite**. To overwrite: your output — to give the output, and to overwrite; to take the output into some file, but from there, to overwrite and store it there. And this one's [`>>`] meaning is that in your **stdout**, it will basically get appended.

Now, this **stdin**, **stdout** — what are all these? You'll understand right away; I'll clear it up for you a bit, sir, it will become clear.

Now look at these things — these things you are seeing: this greater-than, then one more will come, your less-than; after that double greater-than, then double less-than. These things you are seeing, basically — guess — we call these **redirect symbols**, which work for **file descriptors**. These are the symbols for file descriptors; these are the redirect symbols for file descriptors.

Now a question came into someone's mind: "brother, what is a file descriptor? What is this? We were just studying input/output redirection." **What is a file descriptor?** Did this question come into anyone's mind? If someone can tell me in the chat, tell me — did it come into anyone's mind, what it is?

So let's understand a bit about file descriptors.

### What is a file descriptor?

Now look, about file descriptors too — as I already said, the topic is [big]; "file descriptor" is a thing in itself, there are many concepts, many things. We are going to understand it in a very simple way: brother, what is a file descriptor?

Come on — ah, you people have kept a notebook open? As I say, you people have kept a notebook open; somewhere you can write notes, type, please. Okay? So you people should write this thing down; it will be much better. File descriptor. Okay, there's a bit of a problem in writing, that's the thing — so ignore that a little, you people just understand the things.

**It is a number which basically identifies any open file** — it identifies an open file inside the OS. Identify. And an "open file" is in a process — whichever file is already being processed, whichever file is in use, is an open file. Simple. So our file descriptor identifies that.

Ah, tell me one thing — you people tell me one thing. In Linux, everything — if you don't know, you must be thinking there are directories, there are files, they are different things. Meaning, spin your head: every directory, that too is a file. Take it that way. Now why is it so — let me tell you. All are files, basically.

Now this **stdin** of yours, **stdout**, **stderr** — okay — these too are files. These are **special files**; these are special files.

For the file descriptor, what I told you, you can write it like this: it **describes** any data source. Okay? Any data source at all, it basically describes it, or you can say it **denotes** it. Okay?

At that time the **kernel** — the kernel, at that time it does these three things of yours. Okay:

1. Creates an **entry in the global file table**
2. Provides the **location of the entry**
3. And the third thing it does — it provides you the location [reference]

It does that whenever any operating system [operation happens]. If you don't know this, I would [not be able to] explain input/output redirection to you as a message, because you simply wouldn't know that thing — so understanding the concept is very, very important.

And as we had promised, that basically whatever your capsule course will be on this channel — whatever topic is there, **that will be [taught] in a detailed manner**. Even if it takes us a bit more time, that's fine, but we will deal with it in a detailed manner, explain it to you in detail, tell you and clear it for you. That's it. Take advantage of this thing.

And today I think there are very few present, so if someone is there, you can send the link in the group — at least, yaar, you are getting free learning, so at least join; see it, enjoy the live. Right now very interesting things are coming, see those too, what things are coming. Right?

So the kernel does these three things. Okay? So the file descriptor is identified. Okay?

Now let's understand this a bit too. Your — sorry — your file descriptor, the descriptor: [Music] I had told these three points; of the kernel, someone asked to state the 3 points — two and three. Okay: **creates an entry in the global file table**, and **provides the location of the entry**. The kernel does these three things. Okay?

You people do this — if you people cannot type it, then take a screenshot of it. Whenever something is written in front, take a screenshot of it; **that will do help in your notes.** Okay?

So these are file descriptors. Basically, how are they identified? Their identification — it will be... **unique, non-negative integers**; by these it is done. Okay?

For every open file — whatever open file there is — a file descriptor definitely has to be [created]; it definitely has to be. Okay? A file descriptor definitely has to be [created] for you. That's it.

Okay, so let me allow permission here once so that the link can be sent. And okay, we are sending, like, kind of — I think Sachin can send the link in the group; he is now admin, because I actually couldn't find Rishabh's group. So that — everyone knows; those who don't know, well, let them know once again, and they can join. Okay.

Come on, so — where is it — **unique non-negative integers**, by these they are denoted. A simple thing. Okay.

A file descriptor definitely exists for every open file. Just keep this much in mind — **you have to always keep [this] in mind**. Okay?

You can understand it like a cross-platform thing: this file descriptor of yours was first used in **UNIX**. Okay? Right now in Linux your use continues. Okay. And in **Microsoft Windows** they are called **file handles** — file handling, which you may know; basically they are called file handles. They are called file handles in Windows. We are talking about UNIX/Linux; "file handles" is what we call it in Windows. That's one thing.

---

## The three standard streams

Now let's come to the second thing, and understand this: that actually this input/output of yours — these special files, these file descriptors — let's understand their actual concept a bit. Okay?

Now look: whatever your **input** is, whatever your **output** is, whatever **error messages** there are that display on your terminal — okay — those are all **special files**, as I already told you. Okay? And they have a **location**, where they live. They have a location — brother, you also have a location, you also have a house. Okay? In this way, they too have a location where they live. It's a simple thing. Okay?

Now let's see, look — what, how, where do they live? Let me tell you. Okay?

Let me make a kind of table here; let me show it here. A table of special files — the table of special files will be here; here I'll make their corresponding file descriptor. Okay. Special files, location — let's give the location of special files. Okay.

So the first one is, brother, **stdin**. stdin — where is it recorded? **`/dev/stdin`**.

The second one that you have is **`/dev/stdout`**. Okay, brother.

And the third one, brother, that is yours — this became for output — **`/dev/stderr`**.

And this one — we will come to it also — this is a kind of **black hole** of yours; the way you know black holes, in the same way it is a black hole: whatever you send inside it will disappear. Okay? So this is **`/dev/null`**; we will come to it later.

First let's look at these three things. Come on:

| Special file | Location | File descriptor | Redirect symbol |
|---|---|---|---|
| **stdin** | `/dev/stdin` | **0** | `0<` |
| **stdout** | `/dev/stdout` | **1** | `1>` |
| **stderr** | `/dev/stderr` | **2** | `2>` |

Now, stdin, which is yours — `/dev/stdin` — its corresponding file descriptor is denoted by **0**. stdout is by **1**, stderr is by **2**. So its redirect symbol is `0<`; okay, after that this one is `1>`; this one is `2>`.

So, brother, we use the descriptor — meaning, if you have to give **input**, then you will use this symbol; for **output** you will use this symbol; and if you have to redirect **errors**, then you have to use this one. Okay?

And there are many more things which I'll tell you now, like `&>` — we will come to that too. But first understand this thing. Okay? Let me condense this here so that this circle goes away. Okay.

Now, this single one [`>`] — meaning, if you have already given an output into some file, if you use this for a second output, then it will remove, delete, the first output. Okay? And if you use **double greater-than**, then what will happen is that the earlier output will also remain, and the second one you put will go and get added to it, get **appended**. "Append" directly means to get added. That's its benefit.

That's it. The rest, our concept is this. Clear? Is this much clear to everyone? If anyone has any problem, let me know; please let me know — if anyone has any problem, then please you can tell in the chat.

Basically, Sachin sir's health was a bit unwell, so he can't take the live sessions, but for your doubts at least he is there. Okay? He can also take [them]. Your Ayush sir is also there. Okay.

---

## Practical: `ls` output into a file

Now look, what happens in this: if you have to send output into some file — output — then which one will you use? If you have to send output into some file, which will you use? Simple, use this one [`>`].

It's a confusing concept; some people will understand a bit late, but believe me — believe this one thing absolutely: if, let's suppose, in life you people don't understand something a bit — let's suppose — then **you can watch the recorded video**, which comes on YouTube already after the live ends. Watch it again, that thing, wherever you need to understand; it will become clear to you; it will become clearer first.

Right now, if I have to send output somewhere into a file, then you will use this `>`. For example, if I have to send the `date` command, then this is what I used. In place of this, in place of this, you can simply write `>` only after the `date` command and do it — both of these are the same. Okay? Very [straightforward]. So this is for whom? For your **stdout**.

### Seeing the special files in `/dev`

Now let me show you this location a bit, so that you get to visualize it — you should be visualizing it. So let's see the location. The location we just saw, we found out — its location is inside `/dev`. So you will find `/dev` inside the file system itself. If you go into the file system, there is a directory `/dev`; if you go into it, then here you can search — like kind of `std`. If you search `std`, then here you will find them; these three are showing you in one line: `stdin`, `stdout`, `stderr` — these three are your files. Okay?

In this same [place] our brother **`null`** will also be found; the `/dev/null` I was talking about, that too will be found right here.

These files are nothing, but they do a lot of work — they do a lot of work. There is nothing, nothing at all inside them, but the work is a very big work of theirs. Okay?

Come on, now we come to [`/dev/null`]. Now look — so this, your concept became clear; you would have understood this, it's a simple thing.

### Practical demonstration

Now let's come onto the screen. Let's come to this screen please. Those for whom it isn't clear — if let's suppose — then if you repeat it once, it will be 110% clear, because I am telling from the very basics, very simple. That is why I first told you the concept of a **file descriptor** too — what is a file descriptor.

Not "description" — it's "descriptor." Okay? It's file descriptor; we are not doing "description." This is the descriptor. If I ever say "descript", then ignore that; okay, it comes out of the mouth. **This is a descriptor.** And I increased it a bit, the display.

Now what do we do here — let's do `ls` on the Desktop, I think. So let me do one thing: let me go into the root directory, and I am going to the root location.

How do you know which directory this is? Then `pwd` — enter the command **present working directory**; from this you will come to know which directory of yours it is. So we are operating in `/root`, for the time being. Keep in mind, this symbol — this `/root` is showing you here. Okay?

And here if you go `cd /` — this will basically take you where? **Where it will take**: the file system. Because if you do `pwd` here, it will have gone inside `/`.

So come on, here for now this concept of yours will be clear already. So now let's come here; here we do `ls`. You are seeing all these directories here: Desktop, Documents, Downloads, Music, Pictures.

Let's use this same output that we got when we typed the `ls` command. Okay? Now, what we typed — `ls` — what output did you get? You got this output in front, on the screen.

Now I don't want this output here, brother. **I want this output to be inside of a file.** What will we do? What we did: we used **stdout**; put it into `out.txt`. Enter. It didn't come in front: **this output is being redirected now.**

Now do `ls`: `out.txt` — a file will have been created. To view it, use the `cat` command: `cat out.txt`, enter — and whatever you had sent into it, whatever you had redirected, that has been shown to you here.

Is this much clear? Is this much clear? Is this much clear, guys? Please, is yours clear, tell me quickly. This of yours got redirected.

### Doing it without the descriptor number

Now here, suppose — let's suppose — what do I have to do: like I used this command `1>`, I can also do it without this. For example, what do I do: I do `ls`; let me do `ls` here, and put it into `file.txt`; I hit enter. Still yours will happen — `file.txt` has been created. Open `file.txt` with the `cat` command: the entries that were there are in front of you.

Simple, meaning: use `1>` or simply use `>`. That's it, [greetings].

---

## Input redirection: `cat < file`

One more thing, one more thing let me tell you — an interesting thing. Now here you saw [`cat file.txt`]. Now what happened here? You see `cat file.txt`, so what does that mean? **What it means:** you are using **stdin** — because you are putting `file.txt` into `cat`'s input.

Is this concept understood? This concept is very interesting. If you think like this, then you will understand.

Look, basically what are we doing — we are not just running the `cat` command. This is a normal command that is told to all of us; **this is a very generic command** that is told to all of us. Simple — this is a very [common] command, right? We are doing something else here too; **we are doing something else too.**

What are we actually, originally running here? What we are originally running here is `cat 0< stdin`. Okay? We are giving the content as input.

You people, tell me one thing, everybody answer quickly in the chat — **I am currently reading the chat**, I am reading the chat right now, so tell me quickly, fast. Okay, alright.

This concept — generally, what happens is, you are **not told** this concept. Generally you are not told this concept. Okay? You are not told this concept; you are simply told the use of the `cat` command: `cat <space> file.txt`, and we can view that content.

But actually, what are we viewing? We are giving **stdin** to `cat`, and after that we are saying, "brother, show it" — because the `cat` command's job itself is that it will print and give whatever contents are inside your file. Okay?

So the file's input here — now hit enter, look, still you will see the file.

Now in place of this, **you can use this also**; you can use it **without the 0** also. Look, you got the same output. It was a simple concept; there wasn't much to it.

And its method — what could another standard command be, which actually we don't use at all? What should its actual command be? That: `cat < file`. Okay, we are giving input, brother.

So what did we do? Is the concept understood by you, in detail? Nobody told you that — and that too inside a free course; I guarantee this. But we promised, so we will fulfil it.

"Didn't understand the concept"? Arre yaar, it's so easy, you didn't understand? Let me tell you — I'll tell you simply, let me explain here.

You didn't get it? I'll explain. Look, look, look, brother — what had I told you here: **stdout**. Sorry, this stdout — brother, stdout — who is it for, what is it for? **Any kind of output we send here**; whatever output has come to you here, in this we basically redirect the output here. Just understand this much; this will make no difference.

So I am explaining that we are showing the output which we send to `/dev/stdout` — and enter; you are going to get the same output, a similar output. This much would be very easy; I think it would have become clear. This will give you the same output.

But one thing you will have to see here, one thing you will have to understand — what? That when you do `cat file.txt`, enter, in this manner, then you get the same output here — basically whatever contents there are inside `file.txt`, whatever the thing is, you are getting it here. And here, basically, with this too you are getting the same output.

But the one that is a **standard command** — that is this one. **This is the most standard command that we should use, but we don't use** — because... that is our motive: to clear the concept. The rest, the normal thing, anyone anywhere will tell you; you'll find it anywhere on the internet, available for free.

The standard command is used for viewing files or contents of files. That's it. Got it?

---

## Creating files in different ways

Now one thing — one more thing I would like to do in this, one more thing I would like to tell you.

Now, if I do this: `cat` — look, if you play with commands in Linux, you will enjoy it a lot; you will enjoy it a lot, it will feel interesting; you won't get bored at all.

Now look, I wrote `cat` here. Now this thing — I don't want to do this thing; doing it this way, it will become an entry thing, it will become your output thing. So you don't have to do this thing.

Now look, that would have been removed; do `ls` — I had done that. Now do `cat file.txt` here — there is no entry inside this either. Okay? We will come to that too; for now what are we doing — but like, what we are going to do...

What had we done? Its output, whatever output was coming — so we did `ls`, `ls`, and we put `ls` into `file.txt`, the way our `file.txt` was created, and all these entries of ours were in the file. Okay?

Now what do we do — we run the command `cat`, and here now, brother, we give the **less-than symbol**. Okay? And we redirect it to where? **`/dev/stdin`**. We did it into stdin.

Now, now if you hit enter — now if you read `cat file.txt`, then you won't get anything here; so here there is nothing. Yes, `0` is included. Understood here? Absolutely, it was very simple. Okay?

Just understand this much: that this greater-than — and one more thing to understand: the greater-than symbol, single, that is for [overwrite], and if we do double then this is ours for **appending**. Okay?

### Different ways to create a file

Now, when you create a file, what do you do? To create a file there are many different ways, right? Like:

- With the **`touch`** command a file is created. You gave `touch a` — a file got created; a file named `a` has been created.
- Then after that, to create a file, **`vim`** is used; the `vim` command is also used for file creation. I made a file named `b` with `vim`; this file is here. You will study [vim] in coming times. And here a file named `b` got created. Okay? In this way you create files.
- **If you want graphical**, then from the mouse pad I created a file named `c`, so this will open graphically, and here I typed "subscribe to Defronix Academy" and saved it and came out from here — so this file too got created.
- And you can create a file with the **`cat`** command as well. You do `cat`, okay — `cat`, and after that you have to create a file named `d`, so this greater-than — and greater-than, **what is it doing**? It will make a file named `d`, [if] the file exists [it overwrites]. Now when it creates it, it is asking, "brother, what do you want to redirect?" Meaning, do you want to put something in, or [do you want it] just like that — you redirected the `cat` command out into it. So if you have to type something, then "hello" — type anything, so type it; otherwise it's made. Using the redirect symbol you can do it. So how will it be made? [Music]

So this is your way of creating a file. Basically what are we doing — **we are giving output**. That's it, that's all.

---

## The `tee` command

Ah, now let's come here and understand the concept, which we have to understand — and this concept, we call it the **`tee` command**. Let's understand a bit, because we don't have much time, but still we will complete it. We'll wait a bit, take a little time; no problem.

We look at a command, `tee`. It is connected to this, so that's why I am telling you about it. Okay.

Now the `tee` command: suppose whatever output of yours is coming, and basically what do you do — kind of, you can understand that you have to give it to **stdout** as well. Okay? Both things have to be done, brother — meaning, the output, you want it on the **screen as well and in a file as well**. If you have to do this, then in these kinds of things your **`tee` command** comes in useful. All these you use — where do you use it?

### First, the pipe `|`

Now, when you use two commands — like, what does a **pipe** do? Like this is a pipe; to use this pipe... here — here, simply, what is this? This is a pipe. Okay? Let's suppose. Okay. And after the pipe you wrote a command named `grep`. Okay?

The first command — **the first command's output, it will make it the second command's input.** Got it? Whatever `ls`'s output is, that will become the input for `grep`, and it will do its work. Okay?

So `grep`'s job, basically, for now, if you understand it in absolutely simple language: `grep` is basically used to search any string, any regular [expression] — any kind of expression — we use it to search. If you have to search any string, any particular string, inside some file, inside anything, then you use `grep`.

Suppose I use the `ls` command here, hit enter — we get our output. Now what do I have to do: `ls`, after that I use a pipe, and I don't want all the output; I want — filter it out with `grep`, to search — and I only want that output which starts with [`D`], and I'll hit enter.

So the output you get here — look at this. This searches for a particular string and shows you the result against it. So I did `ls`; `ls`'s output — all of these come in the output — the pipe made it the input of `grep`, and `grep`'s job is to search string-wise: whatever particular string you are showing/giving there, it will search for it. So according to that string it searches and shows you whatever directories and files you have starting with `D`.

That's why I told you this pipe thing. Okay?

### Now `tee`

When you have to redirect into some file **and** print as well — both jobs — then we use the **`tee` command**. Like, if there is some output and you want it to be printed on the screen **and** also be redirected into some file, then we use `tee`. So for this type of redirection we use the `tee` command. That's it.

So here, brother, let's do `ls`. Okay, you know. Now what do we do — `ls`, and here we give — sorry, here we give `grep` — sorry, we don't use `grep`, we use `tee`. `tee` — after `ls` we give `tee` here.

Now we have to redirect, so now it has to be into some file; obviously, where will we redirect it? We can do it at any place — **whatever place we want**, whatever you have to do. So here I give the file `test.txt`; this is the file, and I hit enter.

So now what will happen? Guess. Look here: what it did — it redirected this output into `test.txt` as well, and also showed it on the screen here. That's it. Simple, this is the funda.

Now you see whether `test.txt` has been made or not — look, `test.txt`, this has been created. Now if you view `test`, then inside it — sorry, `cat test.txt` — inside it will be all those files.

Understood? Did you understand this thing? It was very simple. Let me explain once again a bit, let me clear it: basically, the use of the `tee` command — what is it used for? **To print the output and also redirect it to a file.**

So when we ran this command, why did we use the pipe here? Because `ls`'s output — whatever folders and files are in this present working directory — has to be passed forward as input to the `tee` command. Now the `tee` command started doing its work: what will it do — it will put it into `test.txt` as well, and also print it. That is, it is redirecting as well, and brother, printing [as well].

### `tee -a` for append

Now if you want that "no, I have to append as well" — then simply put one [flag] that there is; with this it will append for you too; `-a` it will do. If you hit enter, then basically what will happen is that it will **append** to this `test`.

Like, now I do `cat test.txt` here — look here, basically what did we do? We didn't do anything else; we appended. The output that came earlier, we sent that same output again, but by **appending** rather than replacing. Finished. That's it; this is how you use it.

---

## `/dev/null` — suppressing output and errors

Now, one thing that I mentioned a little while ago — ours is [`/dev/null`]. [Music] It is basically for capturing... if you have to suppress any kind of output, if you have to suppress it — any kind of output at all — then you can do this job. Okay?

Meaning, how does it work — this is basically used for your **stderr**. The stderr you saw some time ago — for errors, which basically I told you about — I think this one is... no, no, this one is... which one was it, yaar? File descriptor — this one, stderr.

Let me tell you for this, in which manner it can happen. Look: meaning, there is no such file/directory, so it will neither read nor create anything; you didn't give any output, you didn't give anything, so this error came: `cat hello: No such file or directory`.

Now what do I have to do — what do I have to do is I have to [suppress] this error. So what will I do: `cat hello`, I wrote it. Now, if you remember — guys, I had told you the redirect symbol for stderr for this very reason. Look, what was the redirect symbol for stderr, brother? Keep this in mind: **`2>`**.

So what do I have to do: `2> /dev/null` — story over, suppressed it, finished it. Basically, that's ours: we suppressed the error and finished it. Simple.

Graphically... okay, we were inside root, right? Okay, inside root — here it is, `error.txt`; let's look at it visually a bit. Look at this: inside it, this error has come printed — meaning it has come into this. Okay.

### `&>` — redirect both output and errors

Now this redirect — let me also tell you the symbol; the error one, the redirect one for errors — let me tell you a simple thing.

Look, here it is; look here: to redirect **stdout to a file** — if we talk about the file descriptor, then here stdout is a file descriptor; in that we use **`&>1`**... If you [want] the file — stdout is a file descriptor — we call it `&1`, this is yours.

Now what does its job become? Simple: you have to do this — you have to do error capturing as well **and** send the output to a file too. Example: [Music] so to do that...

---

## Full demo: a Bash script, errors, and redirection

Look, right now, for example — suppose, **what I am going to do**: what I do is, first let me open a terminal, and let me zoom it, in this manner. And here let me do `ls` — here are all these files. Come on, good; all these files are here. Okay.

**What I am going to do** — let me do one thing: let me write a small script. A small script that will do something, basically. Basically, if you know it, you can do it in Bash, or you can also take the help of GPT; it's simple, it's not much.

So what do I do: `vim`, and let me — let's make it — a small script for creating directories, in which basically it should show us what is happening, in what manner things [go], so that we should get its output and the errors in it. We have to see something in this manner.

So I have made a script — I am doing a bit of scripting in the script, a small Bash scripting; you call it batch, basically. So we do a small scripting of this. Okay?

So now look, here basically I turned on insert mode here in `vim`. If you don't know, then how to turn on insert mode inside `vim`, all that, sir, will be told to you; don't take tension. Okay?

So let's do the **shebang**, and here — **now what I am going to do** — let's write a small script. A `for` loop, variable `i`. Okay.

Now I need to create directories, so let me create directories; let me create five directories, from `a` to `e`: `a b c d e` — these five directories, brother, we made; we did it here.

Now what has to be done — when from `a` to `e`, then what do you have to do: `do`. Okay, we'll do an `echo` and we'll put anything — "creating directory", let's do it like that. And we make this — because we do any temporary work; right now this is a temporary script, we'll do temporary work; the script is going to create your temporary directories, so we do it in temp: `/tmp`.

And basically what we will do — here you will have to denote `i` with a dollar here, so that it works like a variable, so that repeatedly, when this `for` runs, the loop of yours runs — basically whatever condition we have defined here for the loop, for the `for`: that from `a` to `e` it has to make them. We have not kept it as a `while` loop with `true`, and left it, so that it keeps running and running and running — "it will keep going, it will keep going, it won't stop." Here too, basically, we have used a `for` loop; the condition gives: `a` to `e` — you have to make five directories named `a b c d e` and after that stop. It's a simple thing. Okay?

So what we did: an echo, "creating directory `/tmp`" — you have to create it, which one do you have to make, you have to make the `i` one: `a`, then come `b`, then come `c` — that is why we did that dollar symbol. Okay? The variable has been assigned to you, denoted for you.

Now here with `i` it will make this thing. Let's close this bracket. Now, here we have to make the directory, so `mkdir` — and where do we have to make the directory? In `/tmp`, inside temp. And again the same work: you have to make the directory inside `/tmp`. Okay?

So here, `$i` — again we will give, and that's it. One mistake we made here — what mistake? Here we have to make it inside temp; we'll have to define the full path: `/tmp/`, and after that we have to make the directory. So this thing is done, so that `$i` will denote it there, will tell whichever directory gets made.

So here we wrote this thing, one step, and that's it. Let's do `done` here — done. We prepared a small script.

Now we will check whether it is running or not. So we closed it, saved the script with `:wq`, and that's it.

Now what do we do — we execute the script: `./s.sh`. And right now look, from `a` to `e`... let's do `ls` — there are already files here from `a` to `e`, so let me remove these files: `a b c d e`; let me remove these files. I think they would have been removed — I think, yes, they have been removed. Okay, right?

Let's change it; in this, instead of `a` to `e`, we won't make [those]. We'll do — here we'll do `./` and enter.

### Permission denied → `chmod`

Now as soon as we hit enter — guess — here a problem happened with us. This Linux of ours is saying, "brother, we — like — **we will not execute.**" Why? **There is no permission**, brother, even from root.

Still, if you hit enter here, then you will see that three permissions — you must know the three permissions. Basically there are three permissions: **read, write, execute**. Three things: read, write, execute — for **user, group and other**.

This became your user, this became your group — sorry, this became your group — and this became your **other's** permission.

So, for the user — the dash that is showing you at the start, this denotes a **file**; here if `d` is there, then it will denote a **directory**. It's a simple thing, right?

So now here the user has read-write permission; there is no execute permission. The group has read permission only, and others have read permission.

So we need it for the user, right — for root, we need it. So we have read-write but not `x` permission, not execute permission. So we will give it execute permission: so `chmod` — sorry — read, write, execute permission, we got it. That's it, that's what was needed. So we always got it.

So `./s.sh` — we will execute it. Now as we execute, here in front of you, what output do you get? "Creating directory temp 1 2 3 4 5."

Now let's see with `ls` whether the directory has been made. What is this? Okay, it got made in temp — sorry, it's making them in temp, right, so we'll have to go and look in temp: `cd /tmp`, enter. Do `ls`, enter. Look, brother, whether the directory has been made or not — you will see it here. Simple.

Let's go up. Look at this, look at this, look at this: one, two, three, four, five — these directories got created for you. Simple, clear. The directories we made got made, brother. Very good.

### Second run → errors

So our script is working. Now what do we do — now what do we do: let's go back again and run it again, hit enter.

Now when we ran it again — again — then what is coming? "Creating directory..." Meaning **it already exists**, so we cannot do [it]. Understood?

Now we have to suppress this. **You are going to use `&>1`** — we will use that, because we want it in a file too, and we also have to log the error there; we want the output in the file, and we have to log the error too, brother.

So now what do we do: `./` — I said `dear sir`... `./s.sh`. "Dear search" I'm saying — "there search" I did; it's become a habit. So `./s.sh`, and let's give it an output into some file. [Music] This already... so what do I do, `./s`... and let's give it — this will become confusing — so I come to `defronix.txt`; let's go and put it in there.

And when we put it in, then what will you do — here in front, you go... where are we going to... let's do it. Do you see it? You don't see it? Do you see it? Ah, you don't see it. **Why don't you see it?** Tell me this too — can anyone understand, can anyone tell? Anyone can tell, like — we are not seeing the difference.

Just now we gave the output file above, here; what we wrote here — this is the difference. We did everything correctly, correctly — what's the mistake? **What is the mistake?**

Arre brother, we gave the output redirection **where**? Here, after `./s.sh` we have to give the output redirection — we missed giving this. We do have to give it, brother.

Now take it, now take it — we had given this command; here we gave the output redirection — this one. Now we hit enter.

Meaning, we **suppressed** the errors, completely made them disappear. But now we will do `ls`, and you will get all those here. Everything, everyone — simply, we put the output into a file.

**What did this command come to mean?** Look: we put the output into a file; we put it into that file too, and all the things appeared to us in the file; we suppressed it. Understood?

Now from here you can use `/dev/null` too. Okay? You can use that. This much understood? Was it clear to everyone? Up to now?

---

## Closing

Now, it's time — it got a bit long, but okay, it will do. We'll close here, but **I don't want** that you... I don't want — I mean, I don't want it to be that you didn't understand and then you leave. Although, whatever bit of a basic concept it is, if you repeat it again — if it isn't understood, then repeat it and it will be understood.

Very simply I have tried to explain to you. It's a very [complex] concept — if I tell you truly, it is a complex concept, and it won't be completed in one session. Right now there are a lot of basic things; I have basically focused mostly on the **practical** part and tried to give you a touch of theory too, tried to make you understand.

So it's a **huge topic**; the concept is a thing in itself — it's very big, yaar, these things; there are very many things inside it. But you should have understood a bit, and its... we will try one more session; in that we will try to clear these things. Okay?

Okay, so — okay, so I think, I think this much is enough for today; for today this much is enough. So I think for today we'll stop it right here; right here we complete today's session.

And I hope it became clear to you, you understood, all the things became absolutely clear. And if yours did not become clear, then I will say just one thing: **please, please repeat the video** — whenever the video is on your YouTube; because as soon as the session is over, your video will come onto YouTube; repeat it, and basically your work will be done. That's it. If you repeat it, it's finished; it will become absolutely clear to you; whatever was left to be cleared will become absolutely clear. Okay? Understood?

Come on, in the next session we can continue it; whatever things are left, we'll do those too. Okay?

And — and please maintain the attendance. Please maintain the attendance a bit, and that thing a bit — because the more you maintain in attendance... the fun that is in live, that doesn't come in your recording. I know, I know very well. So please. And share with your friends — like, if you know, like, if you know some person who needs this knowledge, then share it with them, with friends; **it will be very helpful** — and for coming, okay, into our free live capsule course.

And if you want to support, then you can share the video with your friends, on your social media and elsewhere, so that it reaches everywhere. Okay, thank you so much. Good [night].
