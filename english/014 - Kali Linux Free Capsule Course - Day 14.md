# 014 — Kali Linux Free Capsule Course — Day 14

**Source transcript:** `transcripts/014 - Kali Linux Free Capsule Course - Day 14 [ Hindi ].hi-orig.srt`
**Topics:** `history` · Root password reset via GRUB · `sort` · `uniq` · Doubt session
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`हिस्ट्री` = `history`, `लिरिक्स`/`लाइनेक्स` = "Linux", `बेस्ट`/`बेस आरसी` = "bash"/`.bashrc`, `शॉर्ट`/`सोर्स` = `sort`, `यूनिक` = `uniq`, `भूत` = "boot", `एस्केलेशन सिंबल`/`बैंक साइन` = `!` (exclamation mark), `अरा` = "arrow", `इन आईटी` = `init`, `फेडोरा`/`फतोरा` = "Fedora", `सैंटोस` = "CentOS", `डेविन` = "Debian", `कलम` = "column", `शब्द` = "word", `भैंस`/`बेस` = "bash", `टेंडर` = "enter"). The intended technical term has been restored where unambiguous.

---

[Music] Hello, good evening everyone, welcome. Today [the course] is going to [end].

Whatever requirement you had, whatever you had to learn, however much your fundamentals had to be [built] — **I have delivered that to you people.** In security, you have a requirement at the start; otherwise there is a lot more for you to learn, a lot — if you want to go as deep as you want, you can go; there are certificates for it, cloud engineer, all these certificates.

So tell me once — is my voice reaching everyone or not? Tell me, is my voice reaching everyone or not?

Come on then, let's work. So for your kind information, **today will be your last doubt session**, and in it, whatever you have studied up to Day 13 — whatever doubts you have in any commands, up to now, in the syllabus — **you people can ask me; I will answer you.** If you want to take some advice, you can take that too.

---

## Opening appeal

So before starting the post... or even if [there is] someone after the session is over, two days later, five days later — if more people watch our recording session, then accordingly **we will think about [bash scripting] for you people.**

Right now it depends on **how much you people support.** I will teach even better than this, even better, project-based — if I teach — **but for that I need support from you people.**

I am not saying [anything more]. Right now, if I talk about the last Day 13 — in that Day, what did I do — look, in class 13 there aren't even 200 likes yet. **I don't want it like this.**

"Don't worry bro, [I'm] also interested in learning Python, please make a post" — **don't worry**, I have told you from the first day: on our channel, every single thing that you would not even have thought of — but **for that, at the right time, it will come.**

But you people should support. **Our videos — you people have even forgotten to like; comments simply don't happen.** So how will people come to know about us, that we provide the best things for you people? How will people come to know?

You people, please — **just support us once.** Support us and take us to a level. **What do we ask from you? We ask for subscribes, and we ask for views, we ask for likes, and we ask for comments.** We have not asked for anything more than this — not ₹1 from anybody.

If you consider [us] family, then if we talk about family — family should do [this]. If you people support us, we can see.

---

## Today's plan

**One more interesting thing I am going to teach you:** if you **forget the root password of your machine, how can you recover it** — if you want to learn to reset the root password. **Today it will be told, in this very class:** how, if you sit down to turn on your machine and you forgot the password, you can reset the root password.

---

## Part 1 — The `history` command

Now, the whole [history] has a limit. **However many [commands] I have fired up to now — all those commands you will get to see here.**

Up to now I have fired **1672 commands**, so they have gone and got stored in my history file. However many commands I have run, for example — what I did — **you came to know that all the commands go and get saved into the `history` command.**

> **In the background there is a HISTORY FILE; all of them go there and get saved.**

---

### 1.1 Repeating the last command

Come on then, look — let me teach you to operate the `history` command.

For example, what you did — right now, if you [want] the last history, you don't want to fire the command [again by typing]; **I am repeating the last command.**

**So what you have to do — the ARROW symbol; press the [Up] arrow.**

Look — before that I had fired [one], before that I had [run another], before that `history`, then before that `exit`, before that `time`, before that whatever I had fired — **you get to see all these commands.**

So simply what you have to do: with the **Up arrow, Down arrow**, you have to move; after that simply **hit Enter** and your command will be executed.

---

### 1.2 `!!` — repeat the previous command

There is one more way: **if you have to repeat your previous command** — for that there is **the double exclamation mark:**

```bash
!!
```

Now look, it tells you what your previous command was — `history`. **You simply hit Enter.** In this it told you which your previous command was; it was `history`.

---

### 1.3 `!string` — re-run the last command starting with a string

For example, now what I do:

```bash
touch file77       # create a file
cal                # run calendar
rm file77          # remove the file
```

I fired this many commands, and then again I did [something].

**Now look — I want to create this file again.** Which file? `file77`, I wanted to create it again. **But we don't want to write the command manually.**

So for that, what will we do — what I have to do is an **exclamation mark**; sorry, the **bang sign**, as we can call it. After this I have to **add some string** — meaning, in a way, **it does the work of SEARCHING inside your history file.**

So what you have to do is add some string of that command after this. For example, I do have an idea of the command — which command is it? `touch`. So okay, I did `to`; after that, simply, Enter:

```bash
!to
```

It tells me that your command was `touch file77` — okay, here it is. So you thought `touch file77`; so [I] hit Enter, and again what did it do, **that same command got executed.**

So now if I show you `ls` — `file77` — this would be appearing on your screen.

> **How it works:** the exclamation mark, after that you have to add some string; **which string should it be — it should be the string of that command which you are looking for.** In a way it is doing the work of searching inside that command, the previous commands you have fired up to now.
>
> **If you have not fired that command up to now, then you will not get that information** and it will not appear on your screen. **Basically it searches the command from your history file itself.**

---

### 1.4 Limiting the output

For example — right now I ran `history`; it showed the whole thing, [all] 1684 lines.

**No — I want to limit it; I only want to see the output of 10 commands.** So I can do this too:

```bash
history 10        # last 10 commands
history 50        # last 50
```

H-I-S-T-O-R-Y `history`, after that what do you have to write — `10`. Hit [enter], and only [10 come].

Now see — [with `history 50`] whatever commands there are, look: serial number from 1 onwards... all of them up to [50] it showed on your screen.

---

### 1.5 `!number` — execute a specific history entry

For example, I told you: this `history` is my command; so I said I want to fire this one directly.

**What will you do — if you have to fire something directly, then simply what you have to do** is [use the bang with] its number:

```bash
!1674        # execute history entry number 1674
!1634
```

So in this manner **you can execute any [entry] of your history.** For example, what I have to do — here it is, the `clear` one, `1634`; I have to execute it — so directly I can do `!1634`. **How? With the bang sign.** Okay, I use the bang sign, `!1634`, and it will do it.

---

### 1.6 `Ctrl+R` — reverse search

There is one more way: **how to search in your history file.**

**Simply what you have to do — press `Ctrl+R`.** As soon as you press Ctrl+R, look, here it came: `(reverse-i-search)` — meaning, what is it doing.

Now what you have to do is **provide that alphabet or that string** of the particular command which you want to search.

For example — look, whatever thing you type, after that hit Enter. It [found] `touch` — it created a file, by the name `file77`, which we had already created.

> **In this manner you can search inside your history file too. How? Simply press `Ctrl+R`** — like this it will change — [and type] whatever string there is, the name of the [characters] which you [want to] search.

---

## Part 2 — The three history environment variables

Now, since you are studying the `history` command — **while studying the history command, you should know about three environment variables**, the most important variables.

| Variable | Holds |
|---|---|
| **`HISTFILE`** | **the name and location** of your bash history file |
| **`HISTSIZE`** | **how many commands** can be stored in the in-memory history |
| **`HISTFILESIZE`** | how many commands are kept **in the file** |

### `HISTFILE`

The first environment variable **holds the name and location of your bash history file** — `~/.bash_history`.

### `HISTSIZE`

**How many commands you can store in it** — [it is] defined for normal users too.

```bash
echo $HISTSIZE
```

For example, let me show you — I do `echo $HISTSIZE`; hit enter. [It shows 1000.]

> **What happens after 1000 — it starts to OVERLAP** [i.e. overwrite the oldest entries].

### Changing the size

**You can increase its size too. How can you increase it?** Simply:

```bash
HISTSIZE=5000
```

For example I made it 5000. So its file size will be [increased].

> **But this is TEMPORARY. If you want to make it permanent, then you have to [set it] inside `.bashrc`** — inside those `.bashrc` files — **you have to increase the capacity of the `HISTSIZE` environment variable**, which by default is **1000**, even in a Fedora-based machine.
>
> **But what you have to do: go there** — the file you get to see here — **go inside it**, and the environment variable you find by the name `HISTSIZE`, **increase its capacity**; make it 5000. **Its capacity will be permanently changed.**

---

## Part 3 — ⚠ When history is actually written

> **Keep one thing in mind: today's history is only SAVED into your history file when you LOG OUT** [of the session].
>
> **Otherwise, the history you get to see in the `history` command is the IN-MEMORY history.**

This is an important distinction: the `history` command shows you memory; the **file** on disk lags behind until the session ends.

---

## Part 4 — Preventing a command from being saved

Now you can do [this]: **if you want that when I fire some command in the system, I want to stop it from being saved in the history** — you can do that too.

> **But I can't say — there's no guarantee that it will work** [on every system]. But there was one method: **you put a SPACE [before the command].**

**Demonstration:**

```bash
 date         # note the LEADING SPACE
history       # the date command does NOT appear
```

Like I fired the `date` command [with a leading space], hit [enter], did my work. If I run the `history` command — **will this work or not? Okay, it worked.**

Meaning: **if before firing any command you give a SPACE, then after that you write the command's name** — I did `ls -al`; let's try one more, `ls -m`; after that I run the history file, hit enter — **okay, it's still showing 1714; after this it is not updating.**

> **What does this mean: if you put a space before a command, then it means you don't want to save that command inside the history file — it will NOT go into your history file.**

---

## Part 5 — Clearing history

**If you have to [clear] your whole history, how can you do it?**

```bash
history -c        # clear
history -d 17     # delete entry number 17
```

`history -c` — **`c` will clean.** Now [I] did it. *[At this point the option did not work on his Kali machine.]*

> **What it is — on the latest Kali machines that are coming, it's possible that the `-c` option has been removed.** But in the sense that — if I fire the `history` command on some other machine, it works.
>
> **So if you have to [clear] your whole history, you can use the `history -c` option**, which I just used, in which it is not working [here], **but it will work on any other UNIX machine.**

**Deleting one entry:** *"I want to delete only [entry] 17."*

```bash
history -d 17
```

> **These options all work on some other UNIX machine. Even if I use it on a Fedora-based, Red Hat–based, or CentOS, then they work in those too. But there's a problem with Kali** — it's possible that in Kali this has been **modified due to security reasons.**

---

## Part 6 — ⭐ Resetting a forgotten root password

Now I am going to teach you the **most important thing.**

### The scenario

For example, let me give [one] — the most important thing. You shut down, you sat down to turn your machine on, to use it — **and what did you do: you forgot your machine's password.**

Like, as soon as I turned it on, the login interface comes where there's the root password, the username password — **I forgot that. Even I forgot root's password.**

Now, up to now I have taught you that with the `passwd` command you can change anyone's password after logging in as the root user. **So when I taught the password management chapter** — I did that with you in [Day] 3 or 4, [or] 5 or 6 — **I have already told you.**

**But now, for example, you don't even know root's password**; you don't know root's password at all, and you logged out of your machine and went outside, and now you have to use the machine.

---

### ⚠ Distribution warning

> **I am telling you especially about Kali.** So I am telling you **only the Debian-based system.**
>
> **Don't try it on any other [distro]** — it will work, but there are some [additional] steps that have to be performed. **If you don't perform those steps, you will get an error, and it's possible your machine won't even BOOT.**
>
> **Don't try it on a Fedora-based [system]; that's why Red Hat — don't try**, because there some other steps are performed; its steps are different for resetting the root password.
>
> **So this is specially only for Kali, [Debian] and [Ubuntu] operating systems** — especially on these three machines you can use it. **Apart from this, don't try it on other machines**, because there some other additional steps have to be done. It would work after performing those steps, **but otherwise your machine will not boot, because there the security policy works differently** — in the case of a Fedora-based system.

---

### The steps

> **The steps I am telling now — understand them very carefully.**

**Step 1 — Power on the machine.** So the machine will start.

**Step 2 — At the GRUB menu, press `e`.** As soon as it comes, simply press `e` here. As soon as you press `e`, you will get to see a lot of options here; **system set parameters** — [this is what] you get to see.

**Step 3 — Find the `linux` line.** Let me zoom in so you can see. So you have to [find] here — a line with `linux` will come; look at the very bottom. **This `linux` line that you see** — where my cursor is moving right now — here it is.

**Step 4 — Go to the end of that line.** So simply what you have to do — go along and **at the very last**, where `amd64` [appears], go further like that; at the very last — **which is this, do you see it?**

**Step 5 — Replace the ending.** At the very last you will get to see three things: at the very last, **`ro`** (read only), **`quiet`** and [`splash`]. **You have to DELETE those three.**

After that what will you take — **in place of `ro`, put `rw`**; a space, `init`, equals sign, after that `/bin/bash`:

```
rw init=/bin/bash
```

Let me tell you again: you will come to the `linux` line, go to the very last; there you will get to see three things at the very end — `ro` (read only), `quiet` and [`splash`]. **Delete all three of them.** After that, in place of `ro` put `rw`, space, `init=/bin/bash`.

**Step 6 — Press `Ctrl+X`.** And simply after that, what you have to do — **Ctrl+X.** As soon as you do Ctrl+X, **your machine will start to boot.** It depends; it can take time.

---

### After booting into the shell

Okay, so now on your screen something like this will come; you will get to see `root@...` with a **forward slash** — now, **you are inside the ROOT PARTITION**, not in root's home account.

**Step 7 — Verify the filesystem is writable.**

```bash
mount
```

Now here you have to confirm one thing: M-O-U-N-T `mount`; simply hit [enter]. As soon as you enter, **you have to check at the very last** — let me show you again — at the very last you have to check that `/dev/sda1 on /`.

**Here it is, the forward slash** — you see the forward slash. **So this root partition one that you get to see — is it mounted?**

> **Before [proceeding], you have to see: it should NOT be `ro`.** What should it not be here? **It should not be READ ONLY. What should it be here? It should be [read-write].**

**If you find `ro` here**, then simply what you have to do — let me write the command:

```bash
mount -o remount,rw /
```

`mount`, after that **remount**, after that you have to write **`rw`**. **You have to fire this command if `ro` is seen here.** But right now we don't need to do it.

**Step 8 — Change the password.**

Now after this, what can you do — the command we used for changing the password; simply, [if] you want to change root's password:

```bash
passwd
```

[Enter the new password twice.] **`password updated successfully`** — this means my password got changed, got reset.

**Step 9 — Reboot.**

Now simply what do I have to do — **reboot this machine.** So what will I do:

```bash
exec /sbin/init
```

`/sbin`, after that `init` — I-N-I-T. Do this and simply — look carefully, **execute**. `init` — what to do — this is also [a way of] rebooting.

> Now what I am [doing] — **the binary file for rebooting the machine, I am getting that executed.** Otherwise, if you write `reboot` too it will work... **so this is [the way]: `exec /sbin/init`.**

Now your machine will start rebooting, **with the new [credentials] which you have reset**, and you can successfully [log in].

Look — now I wrote `root` and after that I put in whatever I had just reset. **[That] is how the password is reset**, of your own machine.

Tell me, everyone — tell me, tell me. Everyone, in the chat: yes or no? **Did everyone learn to reset the password or not?**

---

## Part 7 — `sort`

So there are one or two more commands which it is very necessary for me to tell you. So which commands are those? After that we will take your doubt session.

Let me have a minute. Okay, okay, let me zoom in.

> **One is `sort` — it sorts ALPHABETICALLY.**

For example [I ran it]; inside it there are a lot of [benefits]. Look, this is already sorted, so let me do one thing — let me make them unsorted.

For example, what I do — inside this... and for this what I am doing... okay. And I will sort. Simply hit [enter].

I have repeated something in it — what did I do; let me repeat something in it. For example, here I again did `sachin`; next, what did I do, `nitesh`, and again `nitesh`, and again I wrote `anil` — A-N-I-L, I wrote `anil` — and I save it again.

Now what do I do — okay, I will sort. **I sorted this file.**

> **`sort` basically has to sort alphabetically** the keywords of files, which it sorts.

### Sorting by column

**If there are [multiple columns] in it, then you can sort according to COLUMNS too. How?**

For example, what I did — if I want to sort, after that what do I want to do; after sorting, what I want is that **only according to the FIRST COLUMN** — I want my file sorted according to the first column:

```bash
sort -k1 filename.txt        # sort by column 1
sort -k2 filename.txt        # sort by column 2
```

`sort -k1`, after that the file name `.txt` — it will do it. Next, if I am saying only **according to column 2**, whatever I want to sort according to — so this is done; it will sort according to the column.

**If I want to sort it alphabetically, I can do that too. In this manner also you can use the `sort` command.**

---

## Part 8 — `uniq`

Now there is one more command, whose name is **`uniq`** — U-N-I-Q.

> **What does `uniq` mean — the DUPLICATE words, delete them.** Delete the duplicate [entries].

### ⚠ The critical prerequisite

> **And keep one thing in mind: `uniq` [works on adjacent duplicates].** Meaning, what you have to do — **first use the `sort` command and sort your file; after that run the `uniq` command, then de-duplication will work.**

### Doing it in one line

**And if you feel "no brother, I won't do that much hard work" — simply, do one thing:**

```bash
cat tmp.txt | sort | uniq
```

What I did — I did `cat tmp.txt`, after that the **pipe** symbol, after that what did I do — I **sorted** it; after sorting, what did I do, I gave its output into `uniq`, U-N-I-Q.

**So what did this do — whatever were duplicates, it REMOVED them, and showed your output in front of your screen.**

> **Because this is working ON SCREEN** — after that you will have to save it [if you want to keep it].

**So in this manner the `sort` command and `uniq` command work.**

So these were some of our commands which you should know about, because **whenever you are [working], you need sorting the most**; and you should know about the `uniq` command too.

---

## Part 9 — Doubt session

So this was today's session, and after that we will [not] end the session yet. **You have a 15-minute doubt session**; whatever I have taught you up to [Day] 13, you can ask anything related to that.

### Appeal: LinkedIn

So take out 5 minutes and go to our page, our **official LinkedIn page** — go there; you will get the link of this video there; **like and comment there** so that people come to know [what] you people [studied] today.

**Just mention the topic's name** — we don't want anything more than that. **Only the topic names**, mention them there; apart from that we don't want anything, because **other people get [the benefit] from it.**

And it's a request to those people too who watch the recording session later, who prefer to watch the recording and don't like coming to the live session — **please, you too take out 1 minute**; you can do this much for us.

### Why you should have a LinkedIn profile

**If you don't have a LinkedIn profile, make one.** Let me tell you its benefit:

> **LinkedIn is one such thing where your profile is monitored.** When you go to work in any company, **the company first checks: does this person have a LinkedIn profile or not?**
>
> **The benefit of having a profile on LinkedIn:** whatever skill you are gaining, whatever certificate you are doing — **immediately after completing a certification, [add it]. Use your LinkedIn profile like a RESUME**; add your qualifications to it.
>
> Because **all the companies operate on LinkedIn**; from there they search, and from there **requests can come for you too.**
>
> If you did any project, put it on LinkedIn. If you completed a graduation, add that qualification. **Anyone getting information about you — either from your social media, or a resume** — so use that too; it will be very beneficial for you.
>
> **Creating a profile [matters] in future, because today or tomorrow you are going to need a LinkedIn profile.** So it's better to make it now and use it for good things.

---

### Q: What does the pipe symbol do?

Okay, let me explain [again].

> **What does the pipe symbol do: the output of the FIRST command, it makes it the INPUT of the SECOND command** which comes after the pipe symbol. **Meaning, joining — "piping" is exactly that.**

[In the example,] the first command — you can't [just] give it, because `sort` needed a file name. So simply I put the pipe symbol and said: "do one thing — `cat tmp.txt`, the text file, whatever output is coming from it, **put it into the `sort` command's input.**"

So okay — what did it do? **This is input/output redirection, which you people would have studied**; it was discussed in two classes.

> **If you have not studied input/output redirection — Day 3 and Day 4 — revise both once and it will become clear to you.**

So the output that came from this — **it made it the input for [`sort`]**, because with the pipe symbol it joined them, **because the `sort` command needed a file name to work with.** Here I have given nothing — so **where will it take input from? It is taking input from here**, working on that.

After that again I put a pipe, **so that the output that came — now I made that output the input [of `uniq`] too.**

So tell me whether you understood or not. It would have become clear. Thank you bro.

---

## Part 10 — Announcement: the OSINT course

Tell me, is there any other doubt up to now, does anyone want to ask something?

[Someone asks about the next course.] Okay — **[it's] information gathering's part itself. [OSINT] means OPEN SOURCE INTELLIGENCE.** What is its work — that same work; you can [keep it] in information gathering.

> **So tomorrow at 6 o'clock in the evening it is going to start.** So everybody, please attend, and along with [yourself] take the other people too.
>
> **There is no condition in it** — technical, non-technical, IT, non-IT, anyone can come, **because this is general knowledge; it is a general-purpose course. Anyone can learn it.**
>
> And I even say that **every single person should know how to do Open Source Intelligence**, because if ever someone gets stuck in some trouble, so that they can get out of such a situation.

I don't think [it will be] 2 hours, 3 hours — **it's comfortably a 10 to 12 hour [course].**

### Advice for newcomers

If this is your first time joining — **I would recommend that you, along with the live sessions, do one thing: start watching our videos from the beginning.** You will get each and every step in detail.

**If you want to learn, then watch one video daily**; if you have more time, watch two. Do that, **and you will be [a] security [professional].**

Okay, bye bye, good night. [End of] session.
