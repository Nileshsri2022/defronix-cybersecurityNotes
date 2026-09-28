# 009 — Kali Linux Free Capsule Course — Day 9

**Source transcript:** `transcripts/009 - Kali Linux Free Capsule Course - Day 9 [ Hindi ].hi-orig.srt`
**Topics:** VirtualBox snapshots · File Security · `ls -l` fields · `chown` / `chgrp` · `chmod` (octal & symbolic) · `umask`
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`लिरिक्स`/`लाइनेक्स`/`नेक्स` = "Linux", `क मोड` = `chmod`, `यू मास्क`/`यू मस्त`/`युवक` = `umask`, `आई नो`/`आई नोट`/`एंड्राइड नंबर` = "inode", `रुस`/`रॉक्स` = `rwx`, `स्नैपचैट`/`स्नैप सूट`/`नेटवर्क`/`स्टेप्स` = "snapshot", `आम डॉट करनी` = a filename, `ऑक्टॉल` = "octal", `डिस्कशन` = "discussion"/group name, `गुरु जी`/`गुरु के` = "group"). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone, good evening to you, welcome. Today — so that I'll come to know... hello, hello, is the voice clear? Right now the background setting doesn't feel good, yaar, but okay.

Again we talk about the same thing; once again let me remind you. You people would have forgotten — [about] your first class, my brother: **because I was not available**, I had to go somewhere and my flight [was there], **I am not able to take the class.** For that we are really sorry. So today [we have] planned it.

And talking right now — again let me remind you that as soon as our class is over, **please go to the LinkedIn page of Defronix Cyber Security**, whose link is given below today's class on our YouTube channel. Please go there and look once.

So there, like, here is Day [x] — the class that has already happened in [that] day, **nobody has commented on it yet.** So now I don't understand the meaning of this: the people who come live, at least they could comment. So going there, **at least you can take out 5 minutes for us.**

It's a request to you people: take out 5 minutes as soon as the class ends. At least the people who are coming live with us, the people who watch our class — one or two, three, four, five people, however many there are — please go, take out 5 minutes; on our web page, as soon as it gets updated, after 15 minutes, after 10 minutes — please go and comment and tell **what all we taught, what all was taught in this video**, so that other people come to know.

Now on the new [Day] there is no comment on the channel; on Five there is a comment; on Six there is no comment. So I don't know... those who have commented, on 5 — on 5 there's one; on the seventh there isn't one; **not even one, not even one.**

Now those who come live — whoever has to come will come; then I'll come to know. Good, you have shared in the group, I have seen that. **But at least on our web page — the web page one — comment there.** [Music]

---

## Part 1 — Take VirtualBox snapshots (strong advice)

Do [this] work: whenever you are using Linux, **especially [as] a security engineer** — and whenever you add a new tool in your machine, you installed a new tool, and if that install happened successfully, then do one thing.

Simply what you have to do — these are our **virtual machines**, so what you should do: go into VirtualBox, into the system — like, you would have installed it for the first time; after that do one thing: **right click**, and here, the **Snapshot** option you see — as you click it, then, in whichever condition your machine is presently — whatever its condition is, whatever its user ID is, whatever its password is, whatever applications are in it, whatever its condition — **with that condition your machine becomes [frozen] with a snapshot.** You took [it].

Now, as you continue working — like you installed some tool, you did some configuration and it went well, you installed it, some tool installed — after it's all done nicely, do one thing: **[take a] snapshot.** If it is working well, then simply what to do — go to Snapshot again, **take Snapshot 2, and delete the earlier one** — because the earlier one is running fine, and the second one you took when the machine was working properly in that condition.

### Why it matters

Now, in [the] case [that] anything [happens] — it's possible there is some **malware** in the tool, and as soon as it came into your machine, as soon as it came in the tool, what did it do: it **tampered with some settings** of the machine, and problems got created in the machine, and nobody knew what was behind it.

So the problem of not taking a snapshot will be this: now the machine is running with the new settings; they had done some configuration, followed steps from somewhere, from YouTube, from Google — but the problem that happened, their machine is running in some different way.

**So if you had taken a snapshot**, then okay — there's a tool because of which a problem happened; **simply you can [roll back].**

Here, look — here there is a tab; here, the one that appears to you in **orange colour** — as you click here, the snapshots available, 1 2 3 4, **whichever one you want to switch to, your machine will switch at that same time with that snapshot.**

### The benefit

So from this you will get this benefit: if some error came in your machine, or you were configuring some tool, a **virus** came — then because of that problem, your whole machine would be ruined; **so you save your machine from getting ruined.**

Because **with great difficulty you would have collected tools**, with great difficulty, arranging internet, you would have downloaded the tools; and just one such file gets downloaded and [ruins] your machine.

So in this case, this step is such a good feature that **you will bring your machine back to the normal state**, and after that you can try again with that tool. If the tool installed successfully, then that's good; then take its snapshot.

**Make this a good practice.** So I believe that in a Linux machine, especially the virtual machine you are using, you will **never have a problem with your tools** again and again, won't have to search — because you have kept snapshots made.

If any [problem] happens in the machine — they heard that there's some problem — so what is it, **with the help of snapshots you can save your machine, and you can save your time from getting wasted.** Because I know how much time it takes to install tools; and after the whole machine gets installed, then to find that tool again and do it, is totally time consuming, and our time gets wasted, in a way.

> **So this is the best option.** Those who didn't know — please follow this, so that it will always come in useful for you people in future. Because today, as a cyber security engineer, this will help you very much.

Sometimes such challenges will come — like the challenges that came to one of our friends, and that friend really has a big problem; I can't understand [it]. Until now I couldn't help, because I couldn't get time; [but] I understood their condition — **the problem is this, [and] they should have done this.** So from there this problem happened with them.

So that this problem does not happen with anyone else — what you people should do: always, for any machine, whichever machine you use in VirtualBox, **keep a snapshot made of it**, so that you get help.

---

## Part 2 — Introduction to File Security

So now let's go to our continuing topic. Today's topic — after [user management], studying it is very, very important. [Music]

[Without security, anything could go wrong.] And to save from the wrong things, what do we have to do — **we have to maintain some security.** So for this thing — if there is no **file security**, then that wrong thing can do anything wrong in your machine. If there is file security, then that wrong thing **cannot** do anything wrong in your machine.

And today's topic that I will teach — today's topic and tomorrow's topic, **both are important topics.** Today's topic, it's possible we will finish in the whole 1 hour; tomorrow's topic, I hope, will run 1 hour 30 minutes, I hope, and there will be talk about **Advanced File Security**.

[When] you hack a machine, especially a Linux machine, then what are all those things, and what problems happen — then [for] those, file security. [Music]

We learn how to do it; how do we do it? Look, we do file security — **how many types of permissions do we define, which permissions are those** — we are going to study all those things.

So look, about file security — right now let me do [this], let me open a screen for you so you get help in making notes nicely. Okay.

### Two types of file permission

Which we call [**basic file permission**]; so the second way, we call it **Advanced File Permission**. Basically **two types of file permissions** are used.

---

## Part 3 — Reading `ls -l`

Basically you get to see a lot of information here. For example, in a project we do this thing. [Music]

### The inode number

Let's talk. Look — the [`ls -i`] number. Now, **what is an inode number?**

Every single file and directory [has one]. On any file system there are a **limited number of inode numbers**; this depends on the **capacity of the disk and file system**. This helps the system to **identify the file**.

When I taught you the **file descriptor** topic, there the **inode table** was mentioned. There I had said there is a lot of inode numbers — with the help of that inode number you come to know **where my file is stored in our system**, and [what is] inside it; my data stays [there], of that file. I had told all this in my [file descriptor] class.

If your file sizes are more, [inodes] will be more; if you have a small machine, then after that they will be fewer.

### The fields of `ls -l`

Second, what you will get to see — the one you get to see, **we call this the file type and permissions.** Inside it, what is it: one, you come to know **what the type of the file is** from this; and from this you come to know **which permissions are on that file** — for the **owner**, for the **group**, and for the **others**. Okay.

And the two/number you are seeing — look, this shows **how many links there are**; it shows the **number of links**.

After that, this information is the **owner of the file**; this is the **group owner** of the file; this is the **size**.

```
-rw-r--r--   1   root  root  4096  Sep 28 15:58  file.txt
    │        │    │     │      │        │            │
permissions  │  owner group  size   timestamp      name
         link count
```

Basically, [these are] the numbers. Now we are going to discuss about this. Basically, what is mine — there is a bit of a concept about this itself.

---

## Part 4 — File type characters

Come on, now here it is; let me [take] this. Ctrl+[C]. We are going to study about this.

Now the **first entry** that you would be seeing — let me separate it out once. **What does it represent to you? It represents the type of file.** [Then the rest] represents your **file permissions**.

Now in this too, what is it — now in this, the **first three entries**, the first three entries — let me copy — [are] **permissions for the owner**; [then] permissions for the **group** — the permissions you get to see are for [the group]; [then] for the **others**.

| Character | File type |
|---|---|
| `-` | a **normal/regular file** |
| `d` | a **directory** |
| `l` | a **symbolic link** |
| `b` | a **block file** — a hard disk attached, or some hardware part |
| `c` | a **character file** |
| `s` | a **socket file** |

Now let's talk next. If you get to see **`b`** — what does `b` mean? `b` means it is a **block file**; block means some hard disk is attached, or it's some hardware part.

If you get to see **`c`** here, `c` means some **character file**. [If it's] some **socket file**, then it is a socket file.

So basically here you will get to see these types of marks. [If it's `-`] this is a **normal file**.

---

## Part 5 — The three permissions

Now let's talk about permissions. Now, **what are `r`, `w`, `x`?** We are going to study about `rwx`.

| Letter | Name | On a **file** | On a **directory** |
|---|---|---|---|
| **`r`** | read | You can **read** the file — see the data inside it | You can **list** its contents |
| **`w`** | write | You can **modify** the file | You can **create/delete** inside it |
| **`x`** | execute | You can **run** this program | You can **`cd` into** it |

Basically `r` means — what can you do... let it be that much for now: **you can read**. If you have to read a file, [to see] what's inside it, to see that data, you can [read] it.

Now let's talk about `w`. `w` — **write permission**. For a file, what does it mean — **you can modify**; you can modify it.

[And `x`] — you can **run this program**; that's what it means.

This same thing for a **directory** — let me show it on screen for you: you can write [in it]. For example, for [entering] you will have to give **execute permission** [on a] directory.

[We'll see] how permission works on a file, and how read/execute permission works on a directory.

---

## Part 6 — Numeric (octal) values

Now let's talk about permission in **numerical form**.

| Permission | Letter | Numeric value |
|---|---|---|
| read | `r` | **4** |
| write | `w` | **2** |
| execute | `x` | **1** |

The **read** permission, which we can write — the `r`, we write `r`; in numeric value it's **four**; for this a four is counted, for `r`. And for **write** — the write permission; for [that] permission, the `w` [is **2**, and execute is **1**].

**What can the maximum permissions be** — permission for a file or directory? [**7** = 4+2+1 = `rwx`.]

| Octal | Binary | Permission |
|---|---|---|
| 0 | `---` | none |
| 1 | `--x` | execute only |
| 2 | `-w-` | write only |
| 3 | `-wx` | write + execute |
| 4 | `r--` | read only |
| 5 | `r-x` | read + execute |
| 6 | `rw-` | read + write |
| **7** | `rwx` | **all three** |

---

## Part 7 — Changing ownership: `chown` and `chgrp`

Till then, let's talk about: **if I have to change the owner or group of any file, how will we do it?**

If you have to change the group ownership of any file or directory, **two people can do that**:

1. **root** can do it
2. the **user who is a member of that group** can do it

For example, what do I have to do — in place of this `kali`, what is it... So if you have to do this work — if for any file you have to change the group, change the group ownership, or you have to change your file ownership — for that we use a command; let me show you by doing it.

For example, what do I have to do — is there some user in our machine? One minute, let me do it. `/root/Downloads/test`. [Music] `kali` — there is [a group] in it.

If you see this — the group/file owner we have — so how will I do it? `kali`, after that enter.

### Doing both at once

**If you want, you can do both jobs together**; so you can do that too.

For example, `chown` — the owner; what do I want to say: first, the `kali` that is there, `kali` — what do I want to keep as its [owner]; **along with that I want to keep its group owner as `kali` too.** Simply, together:

```bash
chown kali file            # change file OWNER
chgrp kali file            # change GROUP owner
chown kali:kali file       # change BOTH at once
```

The information that came is of your **file owner** — the name of the file owner. After that, if I tell you what it is — after that, here you write the **group owner**, the group information.

---

## Part 8 — Changing permissions: `chmod`

So how can you change permissions? How can you change [them]? Okay. [Music]

You are getting to see [the current ones]. Now what do I do — let me check its permissions. You get to see `rw-`, read, [etc.] — these are the permissions on this file.

If what I have to do is **change its permissions** — I want to do [that] — look at its permissions.

**If you want to change the permissions of any file, then two methods work there:**

1. **The first method** is [**numeric / octal**]
2. **The second** is **alphabetical** (symbolic)

The numeric method — [and] in alphabetical we write [letters].

### 8.1 The octal method

So first let me teach you. For example, what I did — I have to keep its permission [as such]; I want to tell you. So for read I can say:

```bash
chmod 777 file
```

`chmod`, after that what I want to do — **seven seven seven**; after that... **this we should never keep**; we are practising, that's why I'm showing you.

So you will get to see that the file type — this is a normal file — **read write execute, read write execute, read write execute.** Okay, the permission is this. **This is the octal method.**

For any [file] — for example, if you want, I can give some permission to a file. I did `chmod`, used it, and I want to remove this permission.

### 8.2 The symbolic (alphabetical) method

What I want to do — let's talk about the **alphabetical method**. How will we do the alphabetical method?

**Removing with `-`:**

What I have to do is: my **group owner** — I [want to] remove the execute permission from here. So how will I do it? `chmod`, and I am saying `g` for group, `g`, **minus sign** — meaning **I have to remove** — after that I am saying the **execute** permission has to be [removed] from this file:

```bash
chmod g-x file.txt
```

And what am I saying — [the file name]. Enter.

Now if you check again, [you'll] get that **I removed it from the group owner.**

If what I have to do... then I can do that too. `chmod` — let me show you — in this manner. Now the execute permission is gone from here.

**Adding with `+`:**

Now what is it — that was the way of **removing** permission. **If you have to add** permission for the user, or add execute permission for the group owner, then the way is:

```bash
chmod u+x file
```

`chmod`, after that, what I want to say — if for the **user**, you have to use the **plus sign**; simply what you have to do: plus sign, **execute**, simply; and what you have to do is then the file's name.

[Minus] will remove that permission; **plus means you are adding** the [permission].

**Replacing with `=`:**

One more thing is used; it is used in this. `chmod` — I did — and if my **group owner** is [the target], what do I want to give in its permission: I want to give **only write permission**; for this file, to this file owner.

Okay, [you] can give. So for whom — for the user; what do I have to give — **only which one**. **Equals sign** — I'll write `w`.

**What does the equals sign mean — it will replace the whole permission entirely.**

Until now, what did plus/minus mean — simply, on this file it was **adding or removing** permission; **but this one [`=`] will [replace]** — because if here I do only `-w`, [it removes] write permission; if I do `+w`, [it adds] only write permission.

Now here, the permission that would be — like, here read permission is there; if I have to give execute permission on this, then simply what was I doing — `chmod`, and what did I have to do: `g` — the group owner — I had to do plus on it.

So inside, what am I doing: I wrote `g`, group owner, for the group owner; after that what did I say — I wrote **only `x`**; after that the file name. Enter.

Now see what difference you will get to see. Simply, [it] did it.

```bash
chmod g-x file      # REMOVE execute from group
chmod u+x file      # ADD execute for user
chmod u=w file      # REPLACE user's permissions with write only
chmod g+x file      # ADD execute for group
```

### 8.3 Doing all three at once

Meaning, **if you want to do all together, how will you do it?** You can do that too.

For example, what do I have to do: I want to keep a permission that there is **read-write permission for the file owner**, and for the **group owner** read [permission], and read permission [for others] — and like that, only [that] is to be written.

After that, for the group, what permission you want to keep; after that, [a] **comma**; after that, what you want to do — **only read permission**; after that the [file's] name.

```bash
chmod u=rw,g=r,o=r file
```

You will see that **it changed the permissions for all three at once according to you** — user, group owner, [others].

You can use the [`a`] symbol too, but I wanted you to understand the differentiation: what the **plus** symbol means, what the **minus** symbol means, and what the **equals** symbol means. Okay.

| Symbol | Meaning |
|---|---|
| `+` | **add** the permission |
| `-` | **remove** the permission |
| `=` | **replace** entirely with exactly this |

| Target | Who |
|---|---|
| `u` | user (owner) |
| `g` | group |
| `o` | others |
| `a` | all |

So this was about one thing.

---

## Part 9 — `umask`

Come on, okay. When you create a file — whenever you create a file; for example I did `touch` and after that I created a file — [Music] **there is a value.**

> **This value defines what the effective permissions will be for any file or directory created in your system.** What permissions [they get] by default is decided by this very value.

And simply, if you do `umask` and hit [enter], then here you get to see **`0022`**. This you get to see here. Okay, this you get to see — `umask`.

So what value of umask do you get to see: `0022`.

### Reading the four digits

If what you do — [it makes] four values: [Music]

**What does `022` mean?** Inside it:

| Digit | Represents |
|---|---|
| 1st (`0`) | special/setuid bits |
| 2nd (`0`) | the **owner's** permission |
| 3rd (`2`) | the **group owner's** permission |
| 4th (`2`) | the **other users'** permission |

[The first] represents the owner's permission. Group owner — G-R-O-U-P, group owner — permission; whoever the group owner is, permission. Okay. And next, the one that represents — **the other users**; other user permission — it represents other users' permissions.

### Can we change the umask value?

Now, **can we change the umask value?** Will it be right or not? And **how is it calculated** — there is a table for it. But look at this table once.

In the table, what does **zero** mean? In the table, what zero means is **read write and execute**. [Then] its meaning is your **write only**... **six** means **execute only**; its meaning is execute only.

You will get to see — its meaning is... in this, zero's meaning [in umask] is **no permission [subtracted]**; here zero means **read [full] permission**. This is that table of umask which is [used].

> **Note:** the umask value is **subtracted** from the maximum, so a umask digit of `0` = full permission granted, and `7` = no permission granted.

If you have to do [something] — for example, what do I have to do for some owner — then **zero and seven**, meaning for the rest there is no permission; so you can define **`077`** as the umask value.

---

## Part 10 — How effective permissions are calculated

Now, **how is this calculated? How is it done?** There is a logic in it; I will explain that logic to you.

> And if today you understood this logic, [you'll understand] how much high-security permission works, [and] how the umask value is calculated. [Music]

### The maximum permission rule

I'm talking about permission — how it is calculated. For that: the **maximum permission** which you don't set [manually]...

But now, **why `666`?** Look, what happens: [execute] is not given. **That's why, by default, the maximum permission you can give to any file is read-write, read [-write]; you cannot give execute permission.**

That's why you get to see — [not] `777`; your system can [only] give **`666`**.

| Object | Maximum default permission | Why |
|---|---|---|
| **File** | **666** (`rw-rw-rw-`) | **Linux never gives execute to a file by default** |
| **Directory** | **777** (`rwxrwxrwx`) | A directory **needs** execute so you can `cd` into it |

### The formula

So now, **how do we calculate?** Come — **to calculate effective permission**, how can we do it?

So let's talk. What you have to do is simply: **[subtract] the umask value from the maximum permission.**

```
Effective permission = Maximum permission − umask
```

### Worked example — a file

```
666 − 022 = 644      →  rw- r-- r--
```

### Worked example — a directory

Next, if I show you one thing — let's talk about **directories**. If I did `mkdir` and [created] some directory — now look here.

Now you'll say, "for a file, okay, understood" — [but for a] directory it's **755**; so how was 755 calculated here?

**So a logic is working in this too**; how is it calculated? Look.

Okay, now the **maximum permissions** that there are — the maximum permissions for any directory — **for a directory it is `777`**, meaning read-write-execute.

**What's the need?** So when a folder gets created, [you need execute] — **[otherwise] where will you go?** But if there were no execute permission, **you would not be able to `cd`.** So [that's what happens] in the case of a directory.

And **in the case of a file, 6 is counted, because by default in Linux execute permission is not given to a file** — but in a directory execute permission is given.

Now let's talk. So how to calculate umask here? So it's the same: **how to calculate effective permission** — how is effective permission calculated. Okay, let's do it simply here.

Okay, it's exactly the same scene, absolutely. So here what happened:

```
777 − 022 = 755      →  rwx r-x r-x
```

And here you will get **755**, which you get to see.

---

## Part 11 — The security policy that caps umask

Now here, **how did the security [aspect] come in?** Look, for example —

Now take the example that **[an attacker] will change the umask value**. Then automatically, if I made some **virus** or made some **malware** — what will it do: it will enter into your machine, will create a file.

And in that file, first of all what will I do — **I change its umask value, so that all my files will get execute permission.** You have the table.

**So first of all, in their malware, they changed the umask value.** Understood?

### But the policy stops it

**According to the security policy** — okay, "we are giving you the umask facility, **but our policy is this**: for any file — fine, you change the umask value to anything — **but we can give a maximum permission [of 666] to any file.**" Here the condition is defined, the default one.

So do it and see. Many people, accordingly, what they do is: they calculate the table and accordingly decide the umask value; so they think that on this file, by default, this permission will be seen. **But the thing is, here the problem is [different].**

> **You can change the umask value — no issue.** I decide the umask value according to me. **But you cannot overpass the policy.** And what does that policy say? That the permissions for a file — **you can give 666 [at most].**

### The demonstration

So therefore, if here, for anyone — for example, what I did: I changed the umask value:

```bash
umask 000
```

`umask` — we can change; I made it `000`.

Now I'm doing one thing — 5 minutes. I did `touch` and I did `test`, I made a file, `file3`. Enter — and it gives you **[664/666]**.

Although you gave `000`, meaning **you defined read-write-execute, read-write-execute, execute in the umask.**

If here what I do is `mkdir`, after that `test`, after that [it] gave test — let me do [`ls`] now. Look, in this it gave full [`777`]; here you can see the **directory got full [permissions]**.

**But according to the security policy you cannot give execute permission to a file.** Therefore, you may set the umask value to anything at all, **but you will have to work conditionally.**

Okay, you [set] the umask value, "but brother, I'll do one thing: **I will take along your umask value, but you will have to consider my policy.**" According to this, then, considering the conditions, I will define the permission for creating any incoming file.

**So that's why** — you people feel that "I'll set anything at all as the umask value and I'll change it there." **It's not like that.** An attacker could think like that too — they changed it, but what will they do? **Because your policy says that it can give [at most] 666**; more than that, by default, it will not do.

### What the attacker must therefore do

So what will the attacker have to do? **The attacker will have to become [a privileged] user.** To become [that] user, what will they have to do — **they will have to become the root user.**

Any file — a normal user can also [create]; but [only] in their home account they were working. **But if you become the root user, then you will have to give execute permission** — inside the malware; after that you can attack inside the machine.

Because what happens is that in any machine, in a Linux machine, some process — **through them too you enter inside the system**, [in the] Linux [privilege] escalation.

> So this is that thing, **the game of umask**, which you would have understood. Please tell me once in the chat. **This is the very reason** [it matters].

I will repeat it — I have started it; look at it once. If I promise... if you don't understand then, I will ask you in the class tomorrow — [in] my next class, which is Day [x], I will ask you first whether it became clear to you or not.

**Please, my humble request:** do one thing once — **revise the video**; listen to it again carefully, all of it; listen not once but twice. After that, if you don't understand, then **I will definitely repeat it**, no issue, I will do it; it makes no difference to me — like, we'll take 5 minutes more, no problem. **Your concept should be clear.** So please, this is my request.

Okay, if you don't understand tomorrow — but you promised — **you will have to watch the video.** It's not that you come directly and ask again "I didn't understand anything", because I explained the concept in such [simple] language, quite a lot, and it will become quite clear to you. That's the concept for now.

---

## Part 12 — `mkdir -m` — overriding umask at creation

And if you [ask] one thing, let me tell you. Okay, so come on:

If what I want to do — you did `umask 022`; now for example, okay, that you have defined the umask value for us, [and] the biggest permissions have come. **But what you want is: "no, when I [create] any file or directory, [only] then I'll put the permission on that directory/file according to me"** — rather than applying the default permission and then [changing it] afterwards.

So how can you do it? Like, I was creating a directory: I'm doing `mkdir test3`, `test3`, `-d` — I am creating a directory.

Now what I have to do — **I don't want to accept the default permissions; I want to override.** So you can do it:

```bash
mkdir -m 700 test3
```

**`-m`** means **I have to modify** — modify permission; what do I want to give — I want to give **`700`** permissions.

And now the permissions you will get to see, `ls -l` — now it will give you **700** permission.

So you can do this: [instead of] getting the default one, **if you create a file or directory and you want to define [the permission] yourself, then you can do it.** This is one way; this is what I wanted to tell you.

---

## Recap

So what I taught today:

- **What file permissions are**
- **How you can change the ownership** of any file
- **How you can change the permissions**
- **What the umask concept was**, and how the umask value totally depends [on the policy]

That is one of the reasons for making you [secure]. I think the concept would have become clear to you.

---

## Practice question

And I feel that let's do this much today. Or — for you people, if I want to tell one thing: **if you people [want] a task**, what will you do? Shall I give you people a practice question? **Do you people promise that you will do it** and write it and send [it on] the page? Tell me.

> **First, today's practice question will be:** [there is] a file whose file name will be [a given name]. [Music]
>
> After that, simply what you have to do: [make it so that the members of a group can] **read and modify the file** — modify the file, on file [`xyz`].
>
> And in the first step, what you have to do is **verify** whether the members who are [in that group] can make modifications in this file or not.

You would have become clear. **Is it clear or not?** And I hope that those who are right now attending our live — [do the] question, and check the recording, the recording section.

Next time what I will do — I will record it and send it to you; I will directly upload it.

What you studied today — **please mention it**; it's a humble request, **so that other people get your help.**

Good night, see you [in the] next session.
