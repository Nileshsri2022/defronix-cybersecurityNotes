# 013 — Kali Linux Free Capsule Course — Day 13

**Source transcript:** `transcripts/013 - Kali Linux Free Capsule Course - Day 13 [ Hindi ].hi-orig.srt`
**Topics:** Variables (user-defined & environment) · `export` · `PS1` · File Globbing
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`वेरिएबल`/`वैरियेबल्स` = "variable(s)", `लिरिक्स`/`लाइनेक्स` = "Linux", `सेल`/`शेल` = "shell", `बेस्ट`/`बेस आरसी` = "bash"/`.bashrc`, `ईटीसी`/`ए पीसी` = `/etc`, `को`/`इको` = `echo`, `पोस्ट नाम`/`हाउस नाम` = "hostname", `डॉलर` = `$`, `शब्द` = "character"/"word", `स्टार`/`तार` = `*` (asterisk), `पायल`/`फाइल` = "file", `स्क्वायर राकेट`/`स्क्वायर पैकेट` = "square bracket", `बम` = `vim`, `इस्पात` = `PATH`, `फाइल ग्लोइंग`/`फाइल ग्लोबल` = "file globbing"). The intended technical term has been restored where unambiguous.

---

[Music] It has come. [Music] Hello everyone, very good evening to you, welcome to [Day 13].

[Continuing] what we started some days — 12 days — ago, which was running for you on alternate days. So **two classes more are left**; after that we will [finish it]. [Music] And [you] would have enjoyed it quite a lot, and then [we will] proceed to the next topic announcement.

So tell me once, you people — is my voice audible to all of you properly or not? Tell me once so that I can know whether it's audible to you people or not, [whether you are] with us. Okay, thank you.

Whatever we have studied up to now, whatever has been taught — **does anyone have any doubt?** Up to now you people have not asked us any doubt, so from this I can understand that everything is being understood properly by you people and **your concept is clear.**

So today the topic we are going to study is an interesting topic, quite a good topic; it's a basic topic — this too comes under basics. **You should have knowledge of it**; someone will already have knowledge and someone won't. So we are going to discuss about it, which is very, very important for you.

---

## Part 1 — What is a variable?

[Music] Let me increase [the screen].

**What is a parameter? What is a position? [What is a] value?** *You can manually change* [it] — meaning what?

If you have not heard about variables before this, if you have no knowledge at all about variables — **don't worry, you don't need [prior knowledge]**; I am going to tell you.

### The box analogy

Look, **we can think that in our programs there are small-small boxes.** What can we think — that whenever [we write] our program, that means **you are putting data in the box.**

Now what do you do — in that box, what are you doing, you are **keeping data**; and **that is what we are calling a VARIABLE.**

What does this mean? Let me explain. What I said was: **whenever, in your machine or in your computer, you keep data in some box, and you give that box a name — then that name is what we are calling a variable.** And inside it you put a **value**.

### Assigning vs referencing

> **Assigning a value** = putting data **into** the box.
> **Referencing the variable** = taking the data back **out** of the box.

So when I say: when we took a variable — that box — and **assigned a value into it, kept data in it** — this means **you are keeping that data inside that box**, putting that value inside that box. That is what it means.

**Variable** — if you are **referencing** some variable, what does it mean: that box, whose name you have kept a name — which we are calling a variable — inside it there is a value; **when we refer to that box, it means I am taking the data OUT of that box**, pulling it out. Simple. That is the meaning.

- If I am **putting a value** inside the box — meaning when I am **assigning** a value — it means I am keeping a value inside the box, assigning a value inside that variable.
- If I am taking **out** the data we kept in the box, the values kept inside the box — then **simply it means I am REFERRING to the variable.**

### The medical shop analogy

For example, I can take an example: many times you go to a shop, to a **medical shop** — so what do they do, they keep many **boxes** with them for reference.

What do they do: **whenever they see some medicine's name, they go directly to that box**, and in that direction they take it out and give it. That box — inside which the medicine is kept — **that is the value, that is the data**; and that box has some name or other kept on it, **so that they can identify it directly.**

So these are a small example.

---

## Part 2 — Two types of variable

**There are two types of variables:**

| Type | Also called | Convention |
|---|---|---|
| **System-defined** | **environment variables** | Usually written in **CAPITALS** |
| **User-defined** | created by you | Usually written in **small letters** |

The second — the ones that are created [by you] — **we call them user-defined variables.**

### How to identify them

Simply, in your machine, if you have to identify which are user-defined variables and which are system-defined variables, **there is an easy way to identify them.**

> **It is not a compulsory condition**, but generally what we do in our machine: the **system-defined variables — these environment variables — we keep them in CAPITALS.**
>
> There is no such condition that you must keep them in capitals; [but] we create the [user-defined] variable in **small** [letters], so that we can identify which is a system-defined variable.
>
> **But there is NO condition, NO policy** that you must keep system-defined variables in capitals. No.

---

## Part 3 — Defining a variable

**Syntax:**

```
name=value
```

Variable name, after that the **equals sign**, after that inside it you keep the **value**. This is the syntax for defining any variable.

### ⚠ The critical rule: no spaces

> **Here we have to keep one thing in mind:** whenever we [define] any variable, **we must NOT use a SPACE around the equals sign** — meaning, **before the equals sign and after the equals sign I must not use a space.** I have to define it exactly like that.
>
> **In the case of bash, while defining a variable, you have to keep this thing in mind.**

```bash
practice=sachin        # ✔ correct
practice = sachin      # ✘ WRONG — spaces break it
```

For example, what I kept: I kept the variable's name `practice`; I keep a value inside it — like, I take any name.

---

## Part 4 — Referencing a variable

**If you have to reference it, to pull out the data inside it** — if you want to see what value is inside this variable — **then that too has a syntax:**

```bash
echo $practice
echo ${practice}       # the official/formal syntax
```

As we will do: `echo`, after that what will you do — there is an **official syntax**; you give the name of that variable.

> **This is the [syntax] which you should generally follow.** Otherwise [the simpler one] is [also] a correct way, but [the braces form] is a good way; you can do that.

So what happens: **the value that is inside `practice` — it REPLACES [the reference] with it.** So here you will get `sachin`, and your output appears on your screen.

**The `echo` command's job** is basically to **show the output on your screen.**

---

## Part 5 — Why bother with variables at all?

Now, **what is the benefit of doing all this?**

Look, we could simply have done this too, right — **put that value directly in our commands and used it**; nothing could be easier than that.

> **So its main benefit is seen when we are building, or have built, some SCRIPT.**

Now, [in a] script — it's possible you would have defined a variable. **Simply, what will I do — I will change the value of this variable.**

And where [it is used in] 50 places — even if you have used that variable **1000 times** — then **it will automatically be changed at once**; **you will not need to change it 50 times**, or do Ctrl+F, or do find-and-replace; you won't have to do that much hard work.

> **To deal with such situations, we use variables.**

---

## Part 6 — ⚠ Variable naming rules

Let me tell you one thing:

> **Whenever you define any variable, keep one thing in mind: that variable will NOT start directly with any special character or any number. It will always start with a small or capital ALPHABET.**
>
> **No variable will start directly with a number.**

```bash
practice=sachin      # ✔ starts with a letter
2practice=sachin     # ✘ starts with a number — error
```

For example, I want to see: `2practice=sachin` — what is it saying [an error]. **So when you define a variable, you always have to keep in mind that it will start with an alphabet.**

---

## Part 7 — Temporary vs permanent variables

For example, let me show you an example: I [set] `practice`. **This variable is temporary right now.**

> **To make it permanent, what will you have to do** — if you want to define this variable permanently in your machine, **you will have to make an entry in its PROFILE FILE.**

---

## Part 8 — Environment (system-defined) variables

Now let's talk about **system-defined variables**. System-defined variables — what do we call them? **We can also call them ENVIRONMENT VARIABLES.**

Yes — whatever variables come under system-defined variables, which we get to see in **capital letters** — they come under your environment variables.

### The workplace analogy

Look, for example let me take an example. **Whenever you go anywhere to work in some company** — for example, in any company, whether you are an accountant — **a system environment is set up and given to you.** So they get an environment beforehand, to work in.

After that what do they do — according to that they can definitely change [things], but **beforehand** — when you log into your machine as a user — **you already get [that environment]**: a lot of files you get to see, directories you get to see; it's possible you get to see some **policies** there.

> **So all this is possible because of whom? Because of ENVIRONMENT VARIABLES.** So you can compare it like this with your real life.

---

## Part 9 — Common environment variables

Now let's talk about some common environment variables which **it is very, very necessary for you to know about**; and let me show you practically.

### `$HOME`

```bash
echo $HOME
```

For example, first, `$HOME` — this is a root machine, so **root's home directory — its path**, the **absolute path** — it prints it in front of your screen.

### `$USER`

There is one more variable — **it prints your [username]** out on your screen.

### `$HOSTNAME`

```bash
echo $HOSTNAME
```

And `$HOSTNAME` — **this represents your machine's HOSTNAME.**

Right now, what is it — we have not set any hostname in our machine, H-O-S-T name, so that's why [nothing shows]. It's possible that in our machine we have not set the hostname up to this time; **that is why its output is not showing anything on screen.**

### Architecture / version

But what happens is: *what type of processor architecture the computer [has]* — if I show with `cat`, inside `/etc` there is [a file]; what is its architecture? Okay, **version**.

### `$SHELL`

```bash
echo $SHELL
```

S-H-E-L-L `SHELL` — **this represents [which shell is in use]**. Let me [check] — one shell; after that what do I do... **it represents [what] is [being used] inside this machine of yours**; this shell's information comes.

### `$PWD`

One more environmental [variable] — one more, `$PWD` — **it represents the directory**; its output comes directly from this environment variable.

---

## Part 10 — `$PATH` — how commands are found

Now let's talk about one more environment variable.

> **This command — how does it execute directly? How did the system come to know where its binary file is located?**

For example, for that there is a command [`which`] — so it told that it has [linked] it, so directly, automatically it found out about it.

**But how did the system come to know** — even [for] `passwd`?

> **All this is possible with the help of whom? With the help of the `PATH` variable** — the `PATH` environment variable. With its help this is possible.
>
> **With the help of this very variable, the system knows where the super user's binary files are located**, where the location of the binary files is.

### The search order

- If your **binary files** — the ones you fire as commands — **if they are not found in the super user['s locations]**, after that what it does: **the remaining ones that are left — `/usr/local/games` and so on — it tries to find out inside those.**
- If it is found inside those, then [fine].
- **If the file's path is neither in the normal user's [locations], nor in the normal location, nor is it defined inside any of the paths defined in [`$PATH`]** — then what will happen?

> **To execute that command, what will you have to do — you will have to give the FULL BINARY PATH.**

For example, if I have to execute this same command, then how will I do it? **If its entry is not inside that file, then you will have to give the full binary path.**

---

## Part 11 — `PS1` — customising the prompt

Now, `$PS1` — what does it mean? **You would have seen it in a lot of places.**

**P-R-O-M-P-T** — the **prompt** from the Linux terminal. Let me zoom in; you will get to see.

For example, for example... my Ctrl+C. **How can you [customise it]?** And here we keep this — Ctrl+Shift — [it] will come in useful for us; and `$`. Okay, let me start again.

### Making it permanent

> **So if you want to set it permanently** — if you want to set this variable permanently, **then simply what will you do: make its entry in its profile file.**

Which profile is it? I have to [use] `vim`, now simply **`.bashrc`** — `.bashrc`. You would be getting to see it below, `.bashrc`.

I will hit enter, and at the very end — I'll go to the very last, and **in its entry I'll put it at the very end**; as [I] said, below it I will make its entry. **So this will become permanently set.**

### Why `PS1` matters

> **So you would have come to know why the `PS1` variable is so important** — because **however you want [your prompt], you can MODIFY it.**

In many places you get to see that here `root@kali` is seen. **You can set it however you want**; it will help you a lot.

Look, it [previews] it too and shows: **the username will come; okay; after that, [the day]** — so the line, you will get to see it like this.

**If you want to add some extra characters**, want to do `@`, after that what you do; basically [then] what is it — **the path, [the] current directory**. Okay, you will get to see it like that. After that you [can have] the `$` sign along with it — so **you will get to see it like this**; like this your output will be seen on screen.

```bash
export PS1="..."      # apply
```

**Simply, if you export it, it will become permanent** — `export PS1=...` — **this will happen; it will work directly.**

---

## Part 12 — `set` and `unset`

Now, whatever environment variables there are, or whatever we have set — **how can we see them?**

You can **set and unset** any variable — **but temporarily.** If you have to unset some variable temporarily, how can you do it — you can do that too; and how you can do it, I will tell you.

```bash
set                   # list variables
unset variablename    # remove a variable
```

**Simply, to unset — what will you do**: simply, you can do `unset` and the variable's name; **it will get unset.** So you can set [and unset].

---

## Part 13 — `export` — sharing variables with child shells

Let me teach you one thing — **a very interesting thing: how to EXPORT variables.**

### The problem

For example:

```bash
var1=test
echo $var1        # works — shows "test"

bash              # open a NEW shell
echo $var1        # NOTHING — the value is not there
```

`var1`'s value — **your value did not come on your screen, because the shell changed.**

### The solution

> **If you have to access [a variable] from any other shell, then what will you have to do — you will have to EXPORT it.**

```bash
export var1
```

**But this works temporarily.** `export` [and] the variable's name — I export the variable's name, `$`. Now what I did — I do [this]; and I have already told about `$`. I exit. If [I open] a shell, then you can [access it].

> **So temporarily you can EXPORT or SET any variable like this.**

---

## Part 14 — The three levels of persistence ⭐

This is the key summary of the variable section.

### Level 1 — Temporary, current shell only

```bash
var1=value
```

Lost when you close the shell or open a new one.

### Level 2 — Temporary, but available to child shells

```bash
export var1=value
```

Available in shells started from this one, but still lost on logout.

### Level 3 — Permanent, per user

Put the entry in the **user's own profile file**:

```bash
vim ~/.bashrc
# add at the end:
export var1=value
```

Then you must tell the system to **re-read** the file:

```bash
source ~/.bashrc
```

> **What do I have to do — you will have to `source` it.** What you have to do is **tell your system once: "read this again, I have made some changes inside it."** How? **S-O-U-R-C-E `source`, after that `.bashrc`.**

*(At this point in the session the trainer hit an error in his own `.bashrc`: "some error is coming, something has gone wrong in the file... because we tamper with it a lot. It's possible my machine is having some glitch." He moved on.)*

> **But this is USER-SPECIFIC** — *"it will only be set for this user; it will not be set for any other user."*

### Level 4 — Permanent, global (all users)

> **If you want to set any environment variable GLOBALLY, for all users, then what will you have to do:** you will have to go to the [system-wide profile file] — inside it you will have to **`export`** that environment variable's name.

```bash
# in /etc/profile  (or /etc/bash.bashrc)
export VARNAME=value
```

**So this will become global**; for that machine that environment variable will get set. **Then you can access the environment variable from any user.**

### Summary table

| Method | Scope | Survives new shell? | Survives logout? |
|---|---|---|---|
| `var=value` | current shell only | ❌ | ❌ |
| `export var=value` | + child shells | ✅ | ❌ |
| entry in `~/.bashrc` | **that user**, permanently | ✅ | ✅ |
| entry in `/etc/profile` | **ALL users**, permanently | ✅ | ✅ |

> **So I told three ways:** one temporary, which was shell-specific; one temporary via `export`; second, permanently user-specific — for that you make the entry in [the profile] file.

---

## Part 15 — File Globbing

Come on, let's study one small topic.

> **What does file globbing mean — DYNAMIC FILE NAME GENERATION.**
>
> We use file globbing **to find out files, especially in the case where we don't know the full name of the file.**

**Don't think it is some command** — it isn't; but it is a technique that you use too. It's a way in which you can find out files.

### The setup

```bash
touch file1 file2 filea fileb filec filed
```

I did `touch`; `file1`, `file2`, after that `file` a, b, c, d.

**Now the condition is: how will you find out?** You know this much — that yes, there are some files, with the name starting `fil...` — you have an idea. **So now how will you find out?**

---

### 15.1 The asterisk `*` — any number of characters

> **A SORTED LIST works in the background** — alphabetically: a, b, ... to z, small to capital; after that 1, 2, 3, 4.
>
> **And it does NOT define the length either.** It's not that where you put the star, only one word, one character [matches]. **No — it will see all of them**, however many are found matching.

```bash
ls file*
```

So simply, [I] hit enter, and it showed: `file1`, `file2`, `filea`, `fileb`... — **all those files starting with the name `file`, it showed them all in front of your screen.**

### Wildcards on both sides

Now what if — **I don't remember the filename; I only remember that `ila` comes [in it].** I remember `ila`; I remember that yes, the file I had to search has `i`, `l`, `a` inside it.

**So what will I do — I will put a star in front too**; okay, in front there can be anything, [but] `ila` must definitely be in the middle; and at the end too there can be something. Enter.

```bash
ls *ila*
```

Now what it did: **whichever files had the characters `i`, `l`, `a` — it matched all three and showed all those files on your screen**, whether they were in capitals or whether they were in small [letters].

---

### 15.2 The question mark `?` — EXACTLY one character

Now let's talk about one more — **there is a character which is used, the QUESTION MARK.**

**What does [the asterisk] do — it uses the whole sorted list, a, b, c, d; however many are found matching that pattern, it will print them all out.**

**But in the question mark, what is it:**

```bash
ls file?
```

For example, what I did — `file`, [then] it will match from the front; **at the end there is a question mark. What does this mean — it will find out ONLY ONE CHARACTER, whatever it may be. Only one.**

```bash
ls file??        # exactly TWO characters
ls file???       # exactly THREE characters
```

> **If you used the question mark twice, what does this mean — it will search only files with TWO characters** [in that position]. **If you used three characters, it means only three.**
>
> **So it is DEPENDENT ON LENGTH.** It is with conditions here — **it is not like the star.** If I had used a star in place of this, then it would give all of them as output on your screen. **But it's not like that; if you used a single question mark, it will match only one character; two, then two characters; three, then three characters.**

| Wildcard | Matches |
|---|---|
| `*` | **any number** of characters (including zero) — **length independent** |
| `?` | **exactly ONE** character — **length dependent** |

---

### 15.3 Square brackets `[ ]` — a specific set of characters

Apart from this, one more thing is used, which **we call SQUARE BRACKETS.**

> **What happens with square brackets — it says: "yes, I am also length-dependent. Wherever you put me [I match one character]."**

```bash
ls file[abc]
```

For example, I did `ls` and `file`, after that I used square [brackets].

**Now the square bracket is saying: "yes, I will also search out that pattern for you, will find that pattern — but tell me which characters to find out in that pattern."**

So it said, "okay — in that pattern, what you have to do: one, you have to find `a`; second, what do you have to find out, `b`" — just these three characters.

> **Meaning it is saying: "file — I will also find it out for you, BUT ONLY ONE CHARACTER; and which ones will I look for? Only a, b [and c] — these three characters."** Whichever files match these three characters [it shows]; look, in this it did not print [the others].

**It works absolutely exactly like the question mark** — but in this, **you DEFINE the characters** that you are going to look for.

### Matching a set at the end

For example, what do I have to do — **I have to find that file whose last [character] is `a`, `b` or `c`.**

```bash
ls file[abc]
```

For example, it can be [`a`], it can be `2`, it can be `b`. [Music] After `file`, `abc` — it found it out and gave it; apart from this there is none.

So if I do `touch` and I made a file, and I kept the file's name `a2b` — if I kept it like that, then if I ran this again, then what it does — **it showed it in the output.**

### Ranges

**One more thing you can do.** Okay, fine — what I do: `ls`, capital `F` — it's starting with capital `F`; okay, [the file] is starting with capital `F`, and I don't remember what's after it; I only remember that `la` is at the end.

And after that what I have to do — I also know this much: **at the end, what will the character be — it can be `1`, it can also be [something], it can be `2`, and it can also be `3`.**

```bash
ls File*la[123]
```

So it showed all these, 1, 2, 3, on the screen in front.

### 15.4 Negation with `!`

**But you can also use them like this.** I want to search such a file which **starts with capital `File`**, but **inside which there should NOT be a `2`** — inside which there should not be a 2; after that there should not be anything [of that sort].

```bash
ls File[!2]*
```

**You can do it like this too**, [for the] present directory.

| Form | Matches |
|---|---|
| `[abc]` | exactly one character: `a`, `b` **or** `c` |
| `[1-9]` | exactly one character in the **range** 1 to 9 |
| `[!2]` | exactly one character that is **NOT** `2` |

---

## Part 16 — Why globbing matters

So this one thing I wanted to explain to you people: **what file globbing is.**

> **In this manner you can use it with the `find` command, or with the `locate` command, or `grep` with a pattern** — **using these three things, your searching will become even easier.**

Look — **`find` does the work of finding a file**; the other commands I taught, `find` or `locate`, what do they do — **they find the file.** But **file globbing is a TECHNIQUE, using which you can make your pattern a bit easier.**

**What you basically learn here:** you have a **rough idea** of some file's name, and you have to search the file in your system — **so how can you search?**

Like I just told — you remember three characters, `ila`, in the middle of the file; after that what you have to do is search. So it's possible there can be any characters in front too, and however many behind. **And what you did — you put `ila`, put a star in front, put a star behind.**

**So in your system, with the `find` command, if you use it like this — then in your system, however many files with the three characters `ila` you get to see, wherever they are found, it will print them out on your screen.**

---

## Closing

So today our topic is finished. We will do only this much today. So please, **2 minutes for your doubt session** — if anyone has a doubt, then please ask.

Okay, come on then, let's get the session over; today's is done.

So bye bye, good night, take care. See you in the next session. Bye bye, good night.

---

## Aside from the session — on password cracking

> *"Keep in mind this is the **Linux capsule course, not the pen testing course.** If this were the pen testing course, then we would talk about how to enumerate usernames and passwords, how to try to crack it if possible" — [depending on] whether your password is strong, what your cryptography skills are like, and to what extent you can do information gathering about any target.*
>
> *"Password cracking we will not teach [here]. But one thing I will teach you: if you turn on your machine and you forgot root's password, then how can you change it — you can change it. I will teach you that, don't worry, at the end of this course."*
