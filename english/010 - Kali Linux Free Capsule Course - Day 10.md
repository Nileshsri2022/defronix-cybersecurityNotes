# 010 — Kali Linux Free Capsule Course — Day 10

**Source transcript:** `transcripts/010 - Kali Linux Free Capsule Course - Day 10 [ Hindi ].hi-orig.srt`
**Topics:** Advanced File Permissions (Sticky Bit · SGID · SUID) · the `find` command
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`सेट`/`स्टिकी बीट`/`सिक्किम` = "sticky bit", `सेट जी आई दी`/`सीजी आईडी`/`एसजीआईडी`/`सीआईडी एचडी` = `SGID`, `एस यू आईडी`/`हा यूआइडीएआइ` = `SUID`, `क मोड` = `chmod`, `लिरिक्स` = "Linux", `रुस` = `rwx`, `पार्ट डी`/`पास डी` = `passwd`, `छोड़ो`/`सुडोकू` = `sudo`, `आम डायरेक्टरी` = a shared/common directory, `डेप्थ्रॉनिक्स`/`डिप्लोनिक्स`/`नेफ्रॉनिक्स` = `defronix`, `ल एस दी`/`एलर्जी`/`एलईडी`/`एल्डर आईटी` = `ls -ld`, `एक्स सी`/`एक्सिस` = `-exec`, `हैप्पी डॉट टी एक्स टी` = a filename). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone, good evening to you, welcome to [the continuation] of this free capsule course. Tell me once, you people, whether my voice is reaching you all. Everyone — [today's] topic. Okay, very good.

Alright, so tell me this — so again, let me tell you again: as soon as the class is over, today's class will get [posted], Day [10]. So what you have to do: simply, in our video's description there is our **LinkedIn page**; what you have to do is go to our web page, where our **Defronix Cyber Security** web page is.

There, what to do — as soon as the day's class is over, the Day [10] class will be updated for you. So please, you people — whether you watch the recording session or whether you watch the live session — as you finish the session, you watch the video once. **So please, it's a request to you people:** however it felt to you, whether you liked it or found it [difficult], then like it there, or unlike, or comment.

So please, [go] to the session, you can like it; **what you people understood, what you didn't understand**, what you people feel — you can tell the trainer.

So today's main topic is a continuation of [file] security. We had studied a bit in the last class — we studied about the **standard permissions**. But what we are going to study today is related to ours: **Advanced Permissions, File Security.**

So let's continue. Those who had to come have come. So come on, let me zoom in once. Zoom in, zoom in. Okay, okay.

---

## Types of Advanced File Permissions

**Types of advanced file permissions.** In this, first of all, the first is: **SUID**, **SGID**, [and the] **Sticky Bit** — file permissions.

Okay, so let's talk. Now let's understand about these next; let's understand **with practical**.

---

## Part 1 — The Sticky Bit

So first of all we are going to discuss which of our permissions is first — let's discuss about this. First of all we [do the] sticky bit.

> **What it does:** [In a directory with the sticky bit set,] whatever files are inside it — **apart from [the owner], nobody can delete that file**; no other user can delete [it].

### The scenario that motivates it

Look — for example, let me take a small example, let me give a [scenario]:

In some company a project was running, and in that project **20 or 30 people** — let's take the example of 20 people — they are working. So the project has a **common directory**; some name was given to the project, [and] it's a common directory. All of them have to do their work right there, because their **manager**, their boss, is right there too; and to check the work status of all of them who are working, they open each file and look at it.

After that, what is it — there will be some people who have a problem with each other. Someone will have a problem with someone else: **someone made a good project, someone made a good report; someone would not have been able to make a good report.**

Now, the one who couldn't make a good report — what did they do: they opened and looked at the other user's files: "this person has made this report." Now they had a problem [with that]; what did they do — **they deleted that file.** They deleted that file.

[The victim] turned on their machine, they looked — **the file simply isn't there.** What did [the attacker] do — they deleted some other file too.

Now all these things, problems, were going on. **We had to find a solution for this: that no one user should be able to delete another user's file.**

### The solution

So to find that solution, what was done: the project that was running, in which 20 people were working — **if you set [the sticky bit] on that project [directory]**, then its meaning is that those 20 people who are working inside the project, who are project members, **they work in their own files, and after working they close the file — but one user cannot delete another user's file.**

> **Meaning: whoever is the file owner of a file, only they can delete it.**

### The practical demonstration

**Setting up users:**

I did `useradd` and a new one — D-E-F-R-O-N-I-X, hit enter; `defronix`. Its password I kept [as something].

Next I created one whose name was `user2`, hit enter. [Then] I am doing `useradd` and what I did — enter; for that I defined the password `defronix`, D-E-F-R-O-N-I-X. I set this password on [them]. So all three users' password is [the same].

**Setting up the directory:**

Now what I did — in my root partition, what I do: once, `cd /home`, I go [there]. Okay. Okay, I go into [the common directory], do `ls`.

Now here what I did — it's okay, it'll work. Let me check the permission on it beforehand: `777` — and the directory `/home/common`, I gave it **full privileges**.

**Demonstrating the problem:**

Now what I did — I switch. I did `su -` permanently, into `user1`. Inside, what did I do — created a file named `user1.txt`; a file has been created by that name.

If we read the data inside it, then inside it you will get to see a calendar. Okay. So `user1` [created a file].

Now I come out of this; I switch from `user1` — I switched into `user2`. Now let me show with `pwd`. Right now I am inside root, so let me `cd`; [the directory] you get. If I `cat`, I can see the data inside it.

**[user2] deleted it.** Although — who? This one. If I do one thing before deleting and show you, you will get to see that **its file owner is `user1`**; and who is the one deleting? If I show with `whoami`, this is **`user2`**.

So now, in this, what did it remove — `user1.txt` — this is what it was doing; **it removed it.** Now do I have to remove it — and okay, yes; now it removed it.

I do `ls`, so here — `user1.txt`, **you don't get to see the file.**

> **Now here the sticky bit is not set, that is why such a problem happened.**

**Applying the sticky bit:**

```bash
chmod +t /home/common
```

`+t`, and after that, on it — what I [did]. Now here you will get to see: here you will find **`t`**.

**What does this mean** — it is seen **in place of the `x`**, where the execute permission stays.

> **⚠ Keep one thing in mind here:** if you get to see a **small `t`**, its meaning is that the [sticky bit] is set [and execute is also present]. If you get to see a **capital `T`**, then its meaning is [that the sticky bit is set **without** execute permission].

**Verifying it works:**

Let me `pwd`; now inside it I `pwd`. So now what I do — I create `user1.txt` by that name again.

You will get to see: **[the sticky bit] is set, so you cannot delete its file.** Okay.

> **What it says:** the file — whoever created it, whoever the **owner of that file** is, **only they can delete it**; apart from them, **nobody can delete it.**

That is a live example in front of you. So this is your **sticky bit**.

### Removing / setting via octal

If you have to remove it, how can you remove it? Let me exit once; I exit.

If, in another way, you have to set the sticky bit by the **octal method**, then for that — [it] is already set; you had got to see [it]. Like, here too, what is it — this is done to set your **advanced permission**. Therefore **1** means [the sticky bit].

```bash
chmod 1777 /home/common     # octal: leading 1 = sticky bit
chmod +t   /home/common     # symbolic: add
chmod -t   /home/common     # symbolic: remove
```

If you have to remove [it] — now let me show with `ls -ld`, so you get to see it. If I show you by adding it — again, there is one way; one is this, the way of adding, by which I added it; `ls -ld` showed it — the sticky bit will be set.

Now what I do — if there's a way of removing, that is `chmod`, after that **`-t`**. And if you [want the octal]... So these are two or three ways of removing the sticky bit.

---

## Part 2 — SGID (Set Group ID)

Now let's talk about the next one; let's talk about **SGID**.

> **What is SGID?** If we set SGID on some directory, then its meaning is that **it makes sure that whatever files or directories are created inside it, their group owner will be [the directory's group]** — you all know who a group owner is.

### The demonstration

[Let me create a directory] whose name was — right now we are working on a project, `project`. This project — I [set] permission `777`, and on whom — on `project90`.

Now let's look with `ls -ld` — its permissions; I have full permission. I had said I gave it to `project90`.

Now, my group — the group I had added — so what I do: `usermod`, `-aG` (hyphen small a, hyphen capital G). Now what is my group's name? My group's name, which I had added, was the one I had made.

Now what we do — we change its ownership; normally it's `root`. I want to keep `project` — P-R-O-J-E-C-T, I set `project`. Whose project? `90`'s. This is `10`'s.

Now what I do — let me show with `ls -ld`. You will get to see `90`; here, what — you get to see the project's **group owner** [set].

### Why you want this

Now what we do — now **we want that whatever files or sub-directories are created inside this, their group should by default be this `project` itself.** It should be `project` only.

**Why did we want to do this?** For example, we are working on some project; it has a lot of members — like, right now I have members — they are working on that project.

Now they want that **whatever files are created in the [directory], their group owner should be the project**, so that [all the members] can read the files inside it — according to the permission inside it.

[Without SGID] what will you do — **again and again you will have to change its group ownership.** But instead of doing that, what can you do — **you can set [SGID] on it.**

### Showing the problem first

Let me show with `pwd` — inside `/tmp`; let me `cd`; after that, inside `/tmp`, which one do I go into — into `project90`. Let me show with `pwd`. Inside it there's nothing.

Here what did we do — I'm deleting a file, I'm creating a file: T-O-U-C-H `touch`, `testfile.txt`.

Now here you would be getting to see: its file [group] and its user...

Now, what did it need? **It should have been `project` — its group owner should have been `project`**, if it is a member [of it]; otherwise not. So here the trick — **up to now SGID is not set, that is why it didn't happen by default.**

### Applying SGID

Now what I do — let me exit, and let me show by setting SGID:

```bash
chmod g+s /tmp/project90
```

So I did `chmod`, and what do I do — to set SGID, what do I do: **`g`** — it is applied **on the group**, this SGID — **`+s`** after that; then I want to set it on `project90`.

If you look with `ls -ld`, then here you will get to see `rws` — **`s` in place of `x`**; the one I highlighted — **in place of the execute permission you get to see `s`.**

**Basically, what does this mean:** that now, on this directory, **[SGID] is set.**

> **And if you get to see a capital `S`, then that is without execute permission**; [with] small `s` you will get to see [that execute is also present].

Now, `touch` [a new file] — and now, what... if you `pwd`. Like, if I exit and what I did — I switch into `user1`/`user2`, and what I do — `cd`, enter.

### Removing SGID

How will yours be — for removing:

```bash
chmod g-s /tmp/project90
```

After that, what to do — `project`, `project90`. Now look with `ls -ld` — here your [SGID] will be **removed**. This is the way of removing.

---

## Part 3 — SUID (Set User ID)

Next let me tell you — we were talking; now we are talking about number three: **SUID**.

Now, what happens — a normal user [has] read-write [only], so how is it possible? But still, how can we [do it]? `rwx` — **here it is already set: SUID.**

### The `passwd` example

Now, this means it is a **binary file** whose help [is needed]... That is why here you get to see **SUID**, because look — **its main user/owner is `root`**, but sometimes what happens — **the `passwd` command, you are able to fire it even from a normal user.**

Okay, you will say — but look at `sudo`; if [you look], on the `sudo` command too, **SUID is set.**

### The definition

> **What does the SUID bit mean:** that it **executes a command — or whichever file it is set on — as if its own owner had executed it.**
>
> For example, in front of you is **root**; so it gets it executed as **root**.

That is what SUID means.

**Okay, okay, okay.** [That] was the concept. I started from the last Day Nine, and in [today's] Day I [completed] it for you.

> **This was a very important concept, because people don't know about SUID and SGID — and your [privilege] escalation happens on the basis of these.**

Okay, so you understood about **standard and advanced permissions.** So comment out to me once whether you people understood this or not — **what [the sticky bit] is.**

Let's move ahead. This concept of ours, **File Security, is complete.**

---

## Part 4 — The `find` command

[Let's] use the command; let's learn about it. **It's a very important command** — the one I just used in front of you, the **`find` command**.

Let's learn about this: how it works. **And it is very, very necessary for you to have knowledge of it.** Whatever you do at all, these commands that I am telling you about — it is very, very necessary for you to have knowledge of them.

So — now, [you] would be getting interested; so from interest, what did we do — we cleared some of our concepts again; and some [command] knowledge you have to learn in between.

So the command we are going to learn today — we are going to learn about the **`find` command** [for] our system: that **in your whole file system, anywhere at all, you can search any [file]** — sorry, you can search any file, [and] on the basis of the command you can search anything.

### Basic usage

`find .` means — in the **current working directory** we can [search]. Meaning, whatever the name is that you want to search.

After that — "I have no idea", so I used a **star** (`*`). After that, look, it told you: your [file] with location `.txt` [is] inside [that directory]. Okay.

```bash
find .                  # everything in the current directory
find . -name "*.txt"    # by name, with wildcard
```

### `-type` — restrict to files or directories

Now what can I do — **I can give `type` too.** I want to search **only a particular file, not a directory**:

```bash
find . -type f -name "test.txt"     # files only
find . -type d -name "tmp"          # directories only
```

Okay, `-type f`; after that what are you doing — `-name`; what will its name be? For example.

Okay, right now it's not working with this; what I did — okay, right now I want to test **where that file is** in the file system: `testfile.txt`.

Now in this, what is it — it showed it. But it should have worked before too; **but it was not working.** For example, where is it, what is the particular location — so `test1.txt`; it went inside. Now it searched in it.

### `-iname` — case-insensitive search

But **it did not show the one with the capital `T`. Why? Because [Linux] is case-sensitive.**

If what you want to do is **bypass the case sensitivity** — you want to make it **case-insensitive** — then what will you do?

```bash
find . -type f -iname "test*"
```

The `find` command, after that [`.`], after that what is it — the **current working directory**; `-type`, after that **`-iname`** [instead of `-name`].

[Now] it showed both on your screen — this capital `T` first, [and] small `t`; both on the screen. In this, what did it do — **it showed [both].**

### Searching only directories

Now let's talk, let's move on. **If I have to search only directories** — only directories — how can I do it?

Okay, what I did — once I `cd` into root; and what am I doing — inside here, what do I do: once `mkdir` inside `/tmp`. [Music]

What do I have to do — **I don't know where it is**; the name I want to keep, `-name` [with a wildcard]. Okay, `/tmp`.

If I want like this, then I could also do it like this; if I want, I can do this too.

Meaning, `cd` — I did `find`, and the **root partition**; `-type f`, the full partition, I do; [search] it. Enter. **Right now too it is working.**

> So in this manner, **you can perform your search / find operation on any file, any directory, with any extension** — multiple [files]; but you remember some keyword, and according to that you can search inside your whole file system.
>
> **It is very fast**; it is working very quickly.

### Searching by permission

For example, what do I have to do — **on the basis of any permissions**, what I want to say is that I want to search. Right now I can do it.

```bash
find / -perm 774 -print
```

So I did `find`, full, inside root, `-perm 774`, `-print` — [do it]. On this, what is it: `77` permissions — you get to see [them]. Everything, okay.

### Negating a search with `!`

Now this much you came to know; you can do anything.

**If I want [to find everything] except this permission** — I want to find NOT this permission, leaving aside all the `077` permissions; **leaving those aside, all the rest, what do I want to do — I want to print them:**

```bash
find / ! -perm 077 -print
```

P-R-I-N-T `print`. The system works **very fast**, yaar — very fast; it showed [the result].

### Searching by group / user

If you have to search — **you can search on the basis of group ID too**; on the basis of group ID. You know, [and on the basis of] permission, anything at all, you can keep.

Now let me tell you — if on the basis of [ownership], if I show you...

### Searching by permission, worked example

So okay. For example, what I did — I have a file; I did T-O-U-C-H `touch`, `happy.txt`; then `chmod`, [and] I kept **`2644`** permissions on it. Okay, you will get to see.

**I want to `find` on the basis of permissions too**; you can find out a particular file, [find] a particular directory — look, you can find out.

---

## Part 5 — `-exec`: the most important feature ⭐

Now **the most important thing I am going to teach you:**

**If you want to find a particular file and change the file's permission**, [then]:

What I did — `2644`, this file has these permissions. What I want is that **I want to change its permissions too, at the same time** — how? **Right now, with the help of the `find` command**, we can do that.

Because I found it out, and **I can apply the change I want on it according to me.** It's not that you found it now and after that you'll change its permission — **instead of doing that in two or three steps, we can do it in one step.**

### How

What I did — `find`; you can give [the path] in front of you too. After that, what will you do — [the command] I want to fire on this particular file, however many files will be found with this permission, `2644`. Whatever you will print, whatever command had to be fired on it —

For example, I want to `chmod` the file; `chmod` — I want to keep the permission `2777`; I want to keep this permission on it.

After that, what you have to do — this is the **syntax**: first the brackets, open-close; after that a **forward slash**, [and] after that a **semicolon**. This will be its syntax.

```bash
find / -perm 2644 -exec chmod 2777 {} \;
```

This `-exec` — [means] you have to execute. Here you have to write the **command's name**, and **at the end you must keep the curly brackets open and close, after that a backslash and a semicolon.**

> **You must keep it, definitely.**

I hit enter. [It said] "missing argument"... okay. What is the meaning [of the error]? [Music] Okay, it's okay, [there was a] problem.

[Take a file] whose permission is `2644` permissions. Now what I [wanted] — I want to change its permission; **however many files will be found, what do I want to apply on them — I want to apply `2777` permissions**, SGID. Okay, so we can do it.

After that, after `-exec` — what to do: `exec` means **execute**. Inside it, what command will you write — **here you have to keep it space-separated.** I was making a mistake there — this and this; open it and close it; you [need] the forward slash, after that this.

Now if I show you — let me show with `ls -l`: whichever had the `6xx` permission, `happy.txt`'s permission will have changed.

> **With the `find` command you can now both find any file and fire any further command you want on those files**, on the result — you can fire further commands, **with the help of one option: `-exec`, the execute option.**

---

## Part 6 — More `find` options

### Finding empty files

So, about the next [option]: if I want to see this — **if I want to list out** that my [directory], the `/tmp` directory — I want to find, inside the directory, I want to find out **how many empty files** there are; I had to find out empty files.

For that there is [`-empty`]; you can see that too. Simply, `-d`, inside this — inside a particular directory.

**If I want to look in the whole file system**, then I can see that too:

```bash
find / -type f -empty
```

`find`, full root partition, after that what is [needed] — I want to see files that are empty, **`-empty`**; `/tmp` [etc.] — `800` empty, it's empty. Look, it will be a bigger list; you would be getting to see a view.

### Finding by owner

**If you want to search a particular owner's file**, we can do that too. How? For example, I want to `find` in the current working directory; `-user`, for that you will use the flag U-S-E-R **`-user`**, after that — with which user's name do I want to search?

```bash
find . -user root
```

It's very biggest, yaar — it's a very big list, a very very big list. If, for example, [it's] not [there] — if you look at root's, then they'll be found.

> So **on the basis of any particular user too you can [search] with the help of the `find` command**; you can find out **which files have been created by this particular user** inside your machine.

### Finding by size

So this was [it]; and there is [more], but I think this much is enough for today, and **knowing this much about the `find` command is enough for you people**; more than this you don't need to know, if I tell you.

Let me tell you one more thing: **if you want to search in the `find` command by size** — if you want to search a file by size:

```bash
find / -size 50M
```

I want to `find`, full, inside root, and **`-size`** of whichever — however much the file's size [is]; if it's 50 MB, all those that are 50 MB size, [I] wanted to search: that in my whole [system], inside it, whichever files' size is 50 MB, list them out.

[Run it and] tell me — so it will tell you. Right now it is giving permission [errors]; okay, with the partition. Right now it hasn't found any yet. If I keep **10 MB**, will it be found?

`cp`, `ls -l`, after that Ctrl+[C].

---

## Why `-exec` matters

> **The `find` command is going to help you a lot — especially its `-exec`, the execution option, is quite helpful.**

Because otherwise, **again and again what will you do**: first you will find and print, you will search in your output; after that, however many files you will be making some change on, you would have to **change them one by one by one by one.**

**Instead of that, what can you do** — [apply] whatever change you want on all those files [at once] — **from which your time will be saved.**

---

## Closing

So for you — I hope — tell me once whether **today's session is clear to everyone.** If it's clear, tell me once in the chat. If it's clear, then take out 2 minutes for it; there are this many people, two minutes is enough for them. Tell me. [Music]
