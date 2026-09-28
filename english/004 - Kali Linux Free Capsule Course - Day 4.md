# 004 — Kali Linux Free Capsule Course — Day 4

**Source transcript:** `transcripts/004 - Kali Linux Free Capsule Course - Day 4 [ Hindi ].hi-orig.srt`
**Topics:** Recap of file descriptors (kernel tables) · `head`, `tail`, `less`, `tac` · `wc` · `sed`
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** the auto-captions are heavily garbled in places (`लिरिक्स`/`लाइनेक्स` = "Linux", `करनाल` = "kernel", `फाइल डिस्क्रिप्शन` = "file descriptor", `आई नो टेबल` = "inode table", `शब्द` = "word", `तेल` = `tail`, `सेट`/`एसिडिटी` = `sed`, `वर्क`/`डबल्यू सी` = `wc`, `ली` = `less`, `ईटीसी`/`सीटीसी` = `/etc`, `पास डी`/`फास्ट डी` = `passwd`, `9 लॉगिन` = `nologin`). The intended technical term has been restored where unambiguous.

---

Hello everyone, good evening. Please tell me in the chat. Okay, okay, thank you.

So, before starting today's topic, let's wait one or two more minutes; after that we will continue and start the topic.

My health was bad; I wasn't feeling well, and I don't know [if I could take] the class, because the voice was also barely coming out of my throat. **This is the problem.** One minute — just one minute.

---

## Why a recap is needed

Let me do one thing: in the last class we studied about **input/output redirection**. So I feel that perhaps the concept of the **file descriptor** — when it was discussed there — I feel that there you need a bit of a pickup as well. If I give you a bit of a quick recap, then I feel that the slight issues you would have had in understanding [will go], because it was a new concept for you people, which Sachin had taught you quite well. And perhaps someone has revised it — it's possible some concept is being missed by you.

So let me do a quick recap. Just give me 10 to 15 minutes for a quick [recap] of this concept for you — after that, **it's my 100% guarantee, sir**, that you people too will have that concept cleared up so well; and the input/output redirection practical that was done for you people in the last class on that basis, that will become very clear to you.

One thing: take my 10 to 15 minutes' quick pickup, this thing. After that, what do you have to do — whatever sir had made you do, do one thing: go there and look at it again, after this recap. If there is any doubt after that, then tell me — after that, no doubt is going to come.

So I am going to explain that thing to you right now with the help of the board: how you people are to understand things; let me tell you. Okay? There's a bit of a problem in my throat, so please don't mind if my voice has a problem in between.

---

## Recap: how file descriptors actually work

Look, before that — no, it is very necessary for you to know one thing. First of all it is necessary for you to know one thing, because **whenever any process starts in your system**, any process at all, by default it uses a lot of **libraries**.

Let me show you — whenever any process starts in your system, okay, what does it do? What is a process, what are programs — this basic concept, this much I can assume you people would know.

In class 2 — the Day 2 class — when I told you about the **File System Hierarchy**, there I had discussed one thing: the `/bin` directory, the binary directory. When I discussed that with you people, there I had used one thing, touched upon one thing about commands. Let me recap that again and catch your concept with it.

What had I discussed there? That whether you use the `wc` command on your machine, use the `w` command, use the `cd` command — any command at all that you use — **all of them are programs that get executed.** Whenever these programs get executed, then what happens — when this program executes, from there what gets formed? **A process gets created.**

Now what does this process do? Internally it uses [libraries] — whether these are your libraries, kernel libraries; every single thing in Linux is a **file**. And the libraries that are used in it — consider which files? Open files. The library files which were used in it, Linux considers them as files — and in which condition? In the **open condition**. That is why these are considered in the open condition.

### Why the kernel must track them

Now let me talk further in this. The part in this is that our **Linux kernel** — what does it do — it needs to **monitor** them. Okay? [Music] Why does it need to track them?

[Like a parent] should know about things: "what are my children doing?" Okay? What are their children doing, who is coming into the house, who is going, who is doing what.

In the same way, our kernel is the **biggest member** of this operating system, and also the most **powerful**. Now tell me: if in his own house something is happening, anything at all is happening in his house and he doesn't know about it, then what can happen? That is the worst thing for him — because he has to manage everything, all the power is with him, and he doesn't know what is happening in his house.

For this same reason, the Linux kernel had to **track these files, monitor them**. Why is monitoring necessary? **Until it monitors something, it cannot control it.** That's the simple meaning.

Now, to monitor these open files, what did Linux have to do? It had to use a concept, and that concept's name is the **file descriptor**. Okay? To monitor these open files, the concept came: the file descriptor.

Let me make it a bit clearer. A small recap — basically I can say that your file descriptor, we can use it [Music] — okay — today, the file system, we can use this concept for **managing open files**.

### The three tables

Now what happens is that in Linux, or in any operating system, **different types of tables** are used. Some of those tables are what I am going to discuss with you right now, to understand the file descriptor concept — because until I explain those tables, you will not be able to understand the concept of the file descriptor.

So I will try to explain to you with a scenario, with a diagram. But first let me tell you which tables I am going to discuss right now. First of all, let's talk about which tables I am going to talk about:

1. First I can say — the **inode table**. Inode table.
2. The second I am going to talk about — the **global file table**.
3. The third I am going to talk about — the **file descriptor table**. It is a special type of table.

Now one more thing about this can be updated — the important point is this: the process that was created — inside the processes, **the file descriptor is not even known to [the process] itself**, because this is a **hidden table**. This is a hidden table which **only the kernel can update**.

The process whose file descriptor table it is — it cannot update it; it cannot make any change in it. If it has to get any change made, if it has to do anything, then that is possible only **through the kernel**. Because updating things, modifying, changing values, doing everything — [the process] doesn't do it.

Now the question came up here: how is this table so important? Come on, you people will have this question in your mind — "that's why they came up with a new concept, increased work for no reason." It's not like that. Look, this alone has to be used; work has to happen in it, so for that the file has to be open. Okay?

### Two more things the file descriptor does

So now there are one or two more important points about this, which let me tell you now. What was it doing — the program, your program, when the process was created — **it helps that process too**. How does it help it? Let me tell you. **How it helps a program**, or we can say a process. How? Look, what does it do:

1. First, it does [the identification] work.
2. Second, what does it do — **on the file system, where the file is stored.** One: it helps programs understand where on our file system this file is stored, where it has been kept, from where I have to access it.
3. Second, it gives the information: **can I access this file?** Meaning, "can" — what does it mean — it tells about the **specific permissions**: do I have permission to access this or not? This thing too you come to know through it.

How is that known? Now let me explain to you how that is known.

What did I say at the start — you people, if anyone has to take a screenshot, take it. If you feel that later you need to understand it — if you want to take a screenshot of this once, then take it on your machine, **so that it helps you easily in making notes.** You would have taken the screenshot. Come on.

### The chain of tables

On executing, the process gets created. And this one on the side — what is this? It is the **file descriptor number** of yours; it is a **positive integer**. You people would have understood this. Its **reference** is obtained here. Here — what can be here? Any binary number, an address can be here, inside this table.

Now what is this — in this, it referred, gave us a reference — of what? Now this is your **global file table**. Look, this is also of this kind. Okay?

Now look, this is on top of your global file, and we can call it — the address that was in this gives you a **reference — a reference to the inode table**. The address given in this... for a particular file, that is the information. Okay:

- Its **size**
- Its **timestamp**
- Its **location**

All these things come under the **metadata**. So any file's metadata is this — that information you will get here. Along with that, here it will give a reference: **where this file is stored on the file system** — it will refer an address of the file system, [saying] "you go there inside the file system and search for this file, look at it"; from here your work will get done.

Basically, this was your concept of the **file descriptor**. [Music]

Tell me — if this has to be repeated, tell me. Arre, everyone tell me in the chat whether it's clear.

Look, what did I do — I told you people that when a program was created, the program executed, the program created a process; when the process has to use some file, then [there is] a small concept behind it — I have told you that.

If you absolutely want to study about it — how every book works, how this thing works — for that, my friends, my brothers, what will you have to do? **You will have to study the architecture of the operating system.** This is absolutely from the top-top level; I have tried to explain it in [layman's] language, because this concept is very big.

If you [want to] know about the **global file table**, know about the **inode table** — what is an **inode number**? A unique number: **all the files that get created — whether they are there by default or you create them, whether empty, whatever kind — for every single one a unique number is decided.** It is with the help of this that it is recognized. This is that concept — because whenever you open any file, every process has to open a file.

Okay, so if you want to study deeper, then you can study. Go, refer a book: **Operating System and Architecture** — how a process works, how a process is created, how it is scheduled from above, how it is loaded into RAM, how the CPU schedules it. All these things you will first get in the basic knowledge of operating systems; after that, when you study its architecture, you will get information related to the hardware parts. Otherwise, for understanding, for you the file descriptor won't be [a problem].

---

## Back to the first three descriptors

Now let's move a bit ahead in this. What was the main topic? Okay, so what I did — what I told about the file descriptor, how the file descriptor table works. Now, what we had to learn — what we now have to learn — is this part.

The file descriptor — let's say that **the first three entries**, we are concerned with these; you will get to see them in a process. Which entries are these — let me tell you. These are the entries that were told to you in the last class:

| Stream | Descriptor |
|---|---|
| **stdin** | **0** |
| **stdout** | **1** |
| **stderr** | **2** |

These were in the last class; in that, an attempt was made to tell you — which I felt I had to tell you a bit more.

Tell me one thing: which is our input device? **The keyboard.** For every program the standard input device is the keyboard. And by default our standard output device — what is it? [The screen]. You get to see it in the [descriptor] table. [Music]

### Where redirection comes in

Now here, what happens — a condition came: what do I have to do — for some process, for a program, I **don't want to use this default keyboard**. I don't want to use the default keyboard; I want that instead of input I use some **file**; use it in that process, do the processing, and the output that came from it — what do I want to do with it? I want to give it as input to something.

Or, what do I want: whatever output comes of mine, of **stdout** or of **stderr** [Music] — I want to share it into some file; I don't want to show what output comes.

That is what we studied in the last class: **input and output redirection**. This is that very concept which you studied in the last class.

Because — as much as we do it practically and show you — this is your concept. [If you feel] "this concept is boring", or "we didn't understand this concept", or "this went over our heads" — so in **layman's language** I am telling you this concept. In Hindi you are not going to find [this] on YouTube about file descriptors; in absolutely easy language I have done this. If anyone feels [otherwise], tell me. By the way, you haven't got to see this, [I'm] confident, because this is such a concept.

If today this became clear to you, at least — whoever gets it cleared, good; whoever wants to clear it right now, after their class — as soon as the video is uploaded, after 2 minutes, after just one minute, then you can review it once again, that 2–25 minutes of it. Then I'm telling you, even any command you use, whatever examples were made for you in class — now, after understanding this concept once, after watching the video once, [it will click]. That's what the concept was.

Okay, so this is the concept; there is no need to talk [more], because once I have cleared your basic concept here, now you should do the practical yourself — the one that happened in the last class. **Please go through it.**

Give me a minute's time; let me switch the screen, and after that we'll continue. We have some more important topics too which are about to start now, and they are starting gradually. I'll have to keep an eye on your chat a bit too, so let me also have a look once.

Okay, let me zoom my terminal a bit. Tell me — is the black screen visible live?

---

## `head` and `tail`

Come on, look — what had I done in the last class? I had told you about the `cat` command; I had told you about a lot of commands. Let's start the series of commands again from the beginning.

Look, what is it — when I told you about the `cat` command, then the `cat` command's output — how does it come? **It displays the whole thing.** Can we do something such that our output appears in a way that "I want to see this much from the top, this much from the bottom, or this much from the middle"?

So, to do something like that — if I have to see output like that — what will I have to do for it? For that I will have to use another command, because in the `cat` command there is no such option; in it there is no such [feature].

Refresh — it's working fine. Okay.

[`tail`] shows your output from the **bottom**. And `h-e-a-d`, there is a **`head`** command.

For example, there is a file inside `/etc`, the `passwd` file. Now I did [`head /etc/passwd`] — so what did it do? Let me switch my machine once. My file — okay.

If I have to [see] — your `head` command, but by default it showed **10 lines**. If you want to see more than 10 lines, how can you see that? Let me tell you that too.

I want to see [15], so `-15`, and after that what do you have to do — you write the name of that file. Or, if you want to see the output of some program, what will you have to do? First you will have to write its program, its name; after that, using the **pipe symbol**, what will you have to do — you will have to give its output as the input of this `head` command.

In this, what is it — it showed the **top 15 lines** here; here, 1 2 3 4 5 6 7 8 9...

If I show you with `cat` — then what do I have to do: `cat /etc/passwd`. Now what is this — it's a lot of output; it would fill the screen. But what do you have to do — you need **only 10 lines**; you can see 10 lines. If you have to see only the **top 5 lines**, for that you can use: `head -5`, after that that file's name, `/etc/passwd` — it will show the output of 5 lines.

Now what do I have to do — I have to see the output from the **bottom**, but from the last line. For that there is the command **`tail`**. `tail`, after that I do `/etc/passwd`.

The `tail` command — it takes the bottom 10, the number of 10 lines, and shows their output on the screen. In this too there are options like that: if you have to show more output than the default, you can do that too; to show less, you can do that too.

`tail`, for that — `tail`, and after that what you have to do is simply use the number of lines you have to see. If you have to see five from the bottom, then you can see that too. So let's see: `tail -5 /etc/passwd` — it will show.

So this was the information about `head` and `tail`, which you should have known.

---

## `less`

After that, if I continue — there is one more command with which you can list out the contents of your file. Which command is that? [Music] **`less`**.

What is this thing? Let me give a bit of info about it. It is used to **read the contents of a text file**, and it shows your output **page by page**. It's not like `cat`, which showed the entire output on your whole screen, and then you have to scroll down.

Now this is a very small file, its output is very small; if there are **thousands of lines**, then while you keep doing [scrolling], a lot of your time will get wasted. So for this, what is there — you can use the `tail` command, you can use the `head` command. Now there is also the `less` command, so how can we use it? Let me show you.

What I did — I had a demo file, so what I am doing: `less demo.txt`. This is that file. Now what do I have to do — on the screen it will load page by page.

Now tell me one thing: whenever you read the contents of any file, what do you do for it? Line by line... no — you read the whole page, and important [parts] will be visible to you only then. So what will you do — you will read line by line.

**Navigation in `less`:**

- Now what do you have to do — you have to read it out; I have to go **top to bottom**. For that what will I do — **simply press the Down arrow.** You know the arrow on the keyboard, the Down one. Okay? So simply, as I keep pressing the Down arrow, look, it will keep running **line by line**; if you keep pressing continuously, it will go further and further.
- If you have to go from **bottom to top**, meaning you have to go up, for that you have to use the **Up arrow**. Now this [moves] line by line.
- If you have to go **page by page** — what do you have to do, you have to step out, you have to go from one page to the second page, from the second page to the third page — then for that you have to press on the keyboard **Page Up**. Page Up, which is a key; you have to press it. On the keyboard, **Page Up** — look, now it will shift the whole thing page by page. Now look, it will go to the top.
- If you have to go from **top to bottom**, to go down page by page, then what do you have to do — **Page Down.** Look, this Page Down will take you down page by page. If you have to go up page by page, for that **Page Up** — you have to use this key. If you have to go down, then Page Down. This will move you page by page. If you have to move **line by line**, for that you have to use the **Down arrow and Up arrow**.

**Searching in `less`:**

- If you have to **search something** inside this file — and how, **top to bottom**? You know how top to bottom is; here it is, like this. If you have to search in this file top to bottom, then for that simply you have to press first **forward slash `/`**. Pay attention here — right now look, what I am highlighting, here it was; pay attention here. So here, what do I do — as soon as you press [`/`], after that what do you have to do: give the name of that pattern, or the name of that keyword which you had to search inside it, **so that** it becomes easy for you.

  What do I want to search — [`sshd`]. So I simply did this. Now what did it do — wherever it matched that pattern, it **highlighted** it.

- Now what do I have to do — I have to go top to bottom, so what do I have to do? Now it is showing you top to bottom. Then I have to go down; now I'm going to the next highlighted keyword, because in the space only this much is visible. For that what do you have to do — **simply press `n`**, the `n` of November; you have to press it. [For the reverse:] **capital `N`**.

- Here it is — if you have to search like that [bottom to top], then simply what do you have to do — for that you have to use the **question mark `?`**. Look, the question mark I pressed with Shift — because if you use it with the forward-slash [key], above it is the question mark. So question mark, and after that write the name of that pattern.

  So what did I say — I am searching a pattern in it: `system`, S-Y-S-T-E-M, `system`, and hit enter. Now look, `system` got highlighted above, because right now what it did was search like this. Now what do I have to do — I have to go to the next; so simply press `n`. Press `n` — look, it will go pattern by pattern. Now look, again I [pressed] next.

**Jumping to the ends:**

- Now what do you have to do — if your cursor is somewhere and you have to go to the **end** of this file, then simply you have to press on your keyboard the keyword **`End`**. Press it. Now look, you are at its end; it is even showing on the screen at the bottom that yes, you are at the end.
- Now if from here you have to [go back] — either you will go page by page, line by line; otherwise, if you directly want to go to the **front line**, to the first line, the starting — you'll have to press **`Home`**. Now as soon as I pressed Home, where am I? I'm at the very top page, the very first page, [it] loaded.

So this was something about the `less` command, about using it, **so that** you become familiar with it. Look, whoever is making notes alongside — whatever I said, what I used, what its purpose is — make notes of all of it.

**Quitting `less`:**

- And if I have to go out of this, what do I have to do — I have to get out, quit. So simply what will happen — you don't have to cut the terminal, [thinking] "brother, I'm seeing a straight arrow, let me cut it." **No.** You simply have to press **`q`** — small `q`, without Shift and without Caps Lock on. Okay?

  So what do you have to do — press `q`. Why do we press it? You will come out of this command; it has quit.

Like this there is one **`more`** command; the `more` command also does some work like this, so you can practise that yourself.

---

## `tac` — reverse output

Now I want to tell you something else, about some other commands.

Now, for example, up to now you see the output top to bottom — `cat`'s output. There is one more command; what does that command do — your output, it shows it **bottom to top**, meaning it shows it reversed, upside down.

If you want to see it upside down, want to **reverse** it — along with the file's name, `/etc/passwd`, then this is your [command: **`tac`**]; hit enter.

Now what is it doing? If I show you its output — look at this. Now this is [it]; if I show you — look, now what is in it? And at the bottom what was there? `root` was there. Meaning, what is this file — so in it [Music] it's like that.

Meaning, for the basics what you have to do: **how to read the content of a file** — this you would have come to know.

---

## `wc` — word count

Now look, what do you have to do — the next topic we are going to study: if you want to **count**, in a file, how many number of lines there are, how many number of words there are, how many number of characters there are, inside some particular file's content — any file, like the `/etc` file — inside it how many words there are, how many number of lines there are...

If you want to keep a count of them, want to count them, then what will you do? You won't sit there like that. For that there is the command **`wc`**.

And how is its syntax? You will use `wc` — we call it **word count** — after that you [give] options. Okay? After that, after the options, you will use the **file name**.

Now let me show you how to use it. Look, what I did: `wc /etc/passwd`, hit enter.

Now what did it do — this file that was `/etc/passwd`, inside it [the output is three numbers]. Meaning, the first thing you see shows your **number of lines**; this is the **number of words**, 97 words; and [the third] is showing you [the characters].

If you want — only... inside it, if you want to see only the words, then for that there is a flag: `wc -w` — this will show the number of words. If you want to see only characters, then `wc -c` will show.

But keep one thing in mind: the `wc` command **never runs on top of your command** [directly]. [For example] there is an `lscpu` command — `lscpu` provides some information about the architecture. Now `lscpu` — it's not like [you can just append it].

Now I have already explained to you the concept of the file descriptor, up to input/output redirection, so now how to catch this, you people should know well.

Now what is this — what did it do — whose output was it? Whose input will I make it? Of the `wc` command. After that, what am I doing — inside it there are 38 lines, [and] 286/604 characters are inside it.

So this was something about which command? About the **word count command**, about the `wc` command.

---

## The three-step workflow of a Linux admin

Now one thing — when you are working, there is one thing that every Linux admin follows, every user follows. What is that thing?

1. **First**, we try that whatever work we have to do, whatever output we need — we try that it gets done **with the command** [itself]. First, this is what we do.
2. **Second attempt**: we try that using whatever **flags** are available on that command, if our work gets done, then we will try that.
3. If using the command you cannot do that work, and nor can you do that work using the options — then what do you do? You start **joining commands**. To join, you use the **pipe symbol**. Like just now, what I did — I joined these two commands; I joined these two commands. In this manner.

So after that, what do you do — once you have followed the first step, followed the second step, [then in the] third step you start joining commands; by joining, you try to extract your output.

---

## Introducing the command series

So now let's talk about such a topic — as I was saying in class, we had talked about it in the announcement too. The most interesting topic for me was that you should understand the **file descriptor**, know the descriptor. Second, look —

The commands I am now going to use, the series of commands that I am going to start, for you to understand — whether it's any Linux admin, or your Linux speed, meaning you have to write a script, do anything — it will be told. That series — I'm saying it's a **very interesting series**.

Whoever has missed [classes], okay — start attending the full classes, because next time when you do revision, when you watch the class again, then think about it: it means you are remembering that thing. If you just sit listening, then too there's a problem; otherwise, you are watching a completely recorded session, so just don't do only [that].

So now, the series I am going to talk about — it is quite an interesting series, which we are going to discuss. Let me first list it out and show you a list of how we are going to discuss inside this series. Quite good things are coming, of commands. Let me zoom in and show you once; let's delete this.

**First of all we will study about:**
- `sed` command
- Third, we are going to study in detail about the `cut` command
- About the `locate` command

This is the series — because it's a very important series. Meaning, all of these — **such important commands**; come on, such important commands — if you learn to use them, then with any output you can very easily **play**. "Play" meaning: how you have to show it so quickly — that if you are told "I have to capture this output out of these files, I have to catch it, I have to find it out" — [it becomes] very, very easy.

Because this is the best [approach]; otherwise there's no benefit in studying, whatever work you do.

---

## `sed` — Stream Editor

First of all we are going to discuss — let's start. What is `sed`? We call it the **stream editor**.

**Syntax:**

```
sed 'action' filename
```

After that we use **single quotes**; inside the single quotes we [put] what we have to do — the action — after that the file name.

**What does it do?**

1. **Printing** — meaning it does the work of printing your output. Printing in [a formatted] manner. Okay.
2. Third, it does the work of **deleting**.
3. After [that], you can **print the line number**; we used to help with this command.

### Demo

And here is the demo file — look, inside it there is a lot of output that I have pulled out for you people; log files go inside it.

So now, how will I use `sed`? For this, first `sed`, after that single quotes; inside the single quotes what do I have to do — first, what do I have to do: I have to **print its first line**.

After that, what do I do — you have to use a **flag** with it. If you don't use that flag — okay — then it printed the entire file and showed it. So if you have to work properly with it, in printing [you use `-n`].

```
sed -n '1p' /etc/passwd
```

Inside it, `1p` means the **first line**; after that, what do you have to do — that file's name, `/etc/passwd`. Hit enter. Now what did it do — it printed **only the first line**; it printed only the first line.

### Important: `sed` works on line numbers

Now, one thing — about this command, we forgot to tell one thing; let me tell you. Look, up to now, all the commands I have taught — `head`, `tail` — [they work differently]. This command that works — **it always works on line numbers**.

Now everyone knows how line numbers work: **top to bottom**. But what does the `sed` command do — for it, top-to-bottom / bottom-to-top doesn't make sense; **it works only on line numbers**. Okay?

Now [if] I'm not giving a line number... look, what I'm saying is, I'm showing output — so `-n`. I have to print the first line.

Now let me say: let me show you an output once — let me show with `cat`. With `-n` I'll look:

```
cat -n /etc/passwd
```

Then it will push your file **with numbering**, `/etc/passwd`, [and understanding will] become very easy. Let me split this once. Okay.

Now what do I do — if you look at the right side, what I did, I hit enter. Now what it is doing — let me zoom out a bit so your answer is visible... [it] printed it **with line numbers**.

Now what do I have to do: the first line is this one, this one is the first line, and this is the fifth line. I'm looking at its output — meaning I have to print exactly this. So how will I do it?

```
sed -n '1p;5p' /etc/passwd
```

For that, single quote; I'll do `1`, after that `1p` — [I] have to print that line; after that, **semicolon**. The semicolon's meaning is a **separator**, in a way. After that, the fifth line's [instruction]. After that, what am I doing — give the name of that file, `/etc/passwd`.

Now what did it do — only these; look for yourself, look, the `root` line — it printed exactly this.

Now what do I have to do — no, I need up to [line] 7. If you use a **comma**, then after that `7`, after that what to do — `p`; after that what do you have to do — give the file's name, `/etc/passwd`:

```
sed -n '1,7p' /etc/passwd
```

And [for] the last line directly, what did it do — it printed it. Okay, it printed the last line.

If I have to print the **first and last line**, we'll do that too. How? `sed`, after that `-n`, after that single quote; after that what is this — okay, `1p`, after that **semicolon**, after that `$p` — okay, we'll do this too — `/etc/passwd`. It printed that line.

### Question for you

Now what do I have to do — that too I will do. So here let me give a question: to all who come live, or after this — whoever watches our video later — there's a question for everyone, and you can give its answer here in the comments section.

What do I have to do — this is the same file, the one in front of you people on the left. I need an output from it. What do I have to do — let me comment it out and show:

> **Need the line numbers from 1 to 5, and 11 to 15, and [1 to] 25** — and I need, if it becomes 50 after that — so what do I have to do; you need it in the output... after finishing, meaning...

Let me do it like this. Now actually I'm not going to [reveal] its answer, but it's okay. Let me [go] back to — okay, no issue. [Music] To clear it up.

### `-i` — in-place editing

Okay, meaning: the second option we have is **in-file**. Meaning, now what do I have to do — I don't want the change on the screen; I want it, meaning I want to perform the change operation **with the file itself**.

So these are the **two options** with this command: [on-screen and in-file] replace. Okay?

### Substitution: search and replace

So how — now what do I do, in `cd`... let me show you with `cat`: `cat /etc/passwd`.

**Substitute** — meaning what will it do: first it will **search** it, and after that what will it do — it will **replace** it.

`s`, and [slash], after that here you have to give the name of that keyword which we have to search. I have to search **`root`** — okay, `root`. After that, replace with what — meaning, this word `root`, with what has it to be replaced? **`sachin`** — okay. But you [need] the file name, file name.

```
sed 's/root/sachin/' /etc/passwd
```

Here, in the first line, **only the first `root`** got replaced with the name `sachin`. Why so? Because if you have to change **all** the `root` words in your file, then what will you have to do — for that there's an option with this itself; let me tell you.

Otherwise, only the **first occurrence** will [change]. Wherever `root` comes first, if you have to replace it with this name — that's the [default] way. Otherwise, if wherever there is `root` in the whole file you have to change it, for that what do you have to do — with `s`, at the end you simply have to put **`g`**, meaning **global**:

```
sed 's/root/sachin/g' /etc/passwd
```

"Wherever there is `root`, I want [to make it] `sachin`." But what is this — the work is happening **on screen**; in the main file no work is happening. Look, you came to know. Now this you came to know.

### Restricting substitution to one line

Now what do I have to do — what will I use with this? `1`:

```
sed '1s/root/sachin/' /etc/passwd
```

**Only in this line** the `root` that was there — it replaced it with `sachin`. Apart from this it will not replace anyone.

### Case sensitivity

Now let's talk. Now let me show you. Now what do I have to do — no, right now I'll have to find some word: **`nologin`**. I want to replace these with `sachin`, first, from lines 1 to 7 — line number 1 to 7... after that what do I do — substitute — which keyword? `nologin`. After that, with what do I have to replace it? Replace it [with something]. After that I'll have to give... the one that comes first is 7.

After that, what is it — it **did not replace** `nologin`. Let me do this with the `sed` command — and what did I do, `nologin` — what did I do, **I made it capital**.

Now everyone knows that **Linux is case-sensitive**. So I hit enter. Now what will it do — **it will not replace it.** Why did it not replace? **Because Linux is a case-sensitive operating system.** So here, small and capital are considered different. Since they are considered different, now what will it do — wherever it finds the one with a capital `N`, only that it will replace; otherwise it will not replace. Okay?

Now what can I do to this — **we can bypass it.** Meaning, how can we do it? What does bypass mean — how can we make it **case-insensitive**? For that there is a flag.

That is, I want that my `sed` command should work **case-insensitively** — meaning, overall, override it. It works case-sensitively, so [to tell] it not to do that, simply with `g` you use **`i`**:

```
sed 's/nologin/sachin/gi' /etc/passwd
```

After that, hit enter, and now you will get to see the change. Definitely — it's showing; here it is, `sachin`, `sachin` — you will get to see.

So you made the case-sensitive [behaviour] **case-insensitive**; it will ignore case sensitivity. [Music]

### Replacing a specific occurrence

After that, we are going to finish this; by 10:30 your concept will be finished.

What do I have to do — if I only have to change my **second occurrence**, the second occurrence, the particular one — if I have to change this, then how will I do it?

To change that, simply I will use `sed`, after that single quote; inside it what do I have to do — `s`, after that what is mine — it was `root`, `root`; after that, `root` I wanted to change to something. I want to change the name — okay, I want to correct my name: `s-a-c-h-i-n`, `sachin`.

After that I want to say — after that, **`2`**:

```
sed 's/root/sachin/2' /etc/passwd
```

Simply, **only the second occurrence** is what it will replace. And its name, the file's name, `/etc/passwd`.

Now if you check in your output, then what will happen — only the second one, it will change that too. Look, apart from that, all the `root`s that are there, you will get to see them as it is.

### From the Nth occurrence onwards

If I want that **after that, all of them** should be [changed] — for that what will you have to use? For that you can use, with this at the end, **`g`** along with it:

```
sed 's/root/sachin/2g' /etc/passwd
```

So what will this do — in place of `2`, what do I do... and what do I want to do, in place of `root` — one minute — [Music] you will get to see [it] with `root`.

I did — after that I did `sachin`; now what do I do — after `2` I do `g`. If [I do this], everyone will get to see... okay. Now just this much: wherever there is `root`, in all of them you will get to see `sachin`.

"Don't know, brother, it's not working there" — you people, maybe...

### Multiple patterns at once

Now after this, what does it do — if you have to **search multiple patterns at once**? If you have to search multiple patterns at once, then how can you do it? For that too there are options. How?

For example, to search multiple patterns: `nologin`; after that, `nologin` — with what do I want to [replace it]? With `network`, with `network`. After that, [make] it **global**; separate it [with a semicolon]. After that what to do — one more **substitute**; after that `root` — `root`, how do I want it? `sachin`; after that **global**, `g`:

```
sed 's/nologin/network/g; s/root/sachin/g' /etc/passwd
```

Then it replaced it, and wherever there was `root`, what did it do — it made it `sachin`.

So one was this method. If you have to [do] multiple patterns, you'll use **`-e`**; simply after this you can replace once more.

### In-place editing (`-i`) — permanent change

But if you have to — I am not showing the change, because this is my **original file**. Let me show it [on a copy]; one minute. `cp`, after that let me save it — it came inside a file. What did I do — save.

It's the multiple-commands one. If I'm going to use multiple commands too — and this is my file. Okay, which file will it be? `cat sample.txt`.

And if I do:

```
sed -i 's/nologin/petrol/g' sample.txt
```

`sed -i` — [without `-i`] it will not work on the [file itself].

So what will you have to do — look, all the files that had `nologin`, all the `nologin` keywords that you had, you will get to see them **replaced with `petrol` permanently**.

### ⚠ Safety advice

So let me tell you one thing about this: if you don't know how to use it — how to use it on screen, [versus] in the main file — then otherwise what do you have to do?

**Always, first of all** — whether you are doing it with your own machine — first of all, **perform your task on screen and see it. Do not do it directly in the main file**, otherwise you will be trying to do something and something else will happen, because of which... so that you don't have to face a problem in future.

---

## Closing

So I hope quite a lot of time has passed, so right now let's do more sessions. On the side there should be two or three things, for you as well and for us as well. So you people tell me in the chat. Okay.
