# 012 — Kali Linux Free Capsule Course — Day 12

**Source transcript:** `transcripts/012 - Kali Linux Free Capsule Course - Day 12 [ Hindi ].hi-orig.srt`
**Topics:** `locate` · Package Management (`dpkg`, `apt`, `aptitude`, repositories, dependencies) · Control Operators
**Type:** Verbatim English translation of the spoken Hindi/Hinglish session

> **Note on this transcript:** captions are heavily garbled in places (`लॉकेट`/`लोकेट` = `locate`, `लिरिक्स`/`लाइनेक्स` = "Linux", `एप्ट`/`पीपीटी`/`ए पी टी` = `apt`, `डीपी के जी`/`डीपीके` = `dpkg`, `एप्टीट्यूड` = `aptitude`, `रिपोजिटरी`/`रिप्यूट`/`पॉजिटिव`/`रेफ्रिजरेटर` = "repository", `डिपेंडेंसी` = "dependency", `ईटीसी`/`सीटीसी` = `/etc`, `जल`/`जड़` = a deliberately invalid command, `बेस्ट 15`/`बेस्ट स्क्रिप्टिंग` = "bash scripting", `कल` = `cal`, `पीडी` = `pwd`, `सेमी कलर`/`सेमी कोलोन` = "semicolon", `एम परसेंट`/`परसेंट` = ampersand `&`, `और ऑपरेटर` = "AND"/"OR operator"). The intended technical term has been restored where unambiguous.

---

[Music] Hello everyone, good evening to you, welcome. [Music] Let's start the topic; come on then, let's continue.

Again the same thing — let me remind you people once: as soon as our class is over, what you people have to do is — **inside our video description the LinkedIn page is available**; go there, and after going you will get to see our page.

Go there; as soon as the video finishes, after that **Day 12** — with it, our web page will be updated, and you have to go there and **comment out and tell what our topic was today, what we learned today.**

Whoever comments continuously — [thank you]; after this nobody supports, nobody comments out. However many times, that much we will work.

Come on then, let's continue.

**Today our topic is** — let me tell first: one is the **`locate` command**; and second, I will teach you **how packages are installed, how they are listed** — we are going to learn about all that: **how to handle packages in your machine, package management**, at an absolutely basic level.

So that whenever you want to install a package in your machine, [and] some problem related to it comes, then you will come to know: "okay, this problem can happen." And after that, if time is left, we are going to learn about some **[control] operators** today.

---

## Part 1 — The `locate` command

So let's talk; so let's come to our terminal.

**To search a file, and to find out where that file will be in our system, the `locate` command is a very easy way to use** — and it is a very important command for us too.

### How it works

**The first thing that we should know about the `locate` command:** to search, **it uses a LOCAL DATABASE present in our system.**

What happens is that whatever [files] are created, deleted, modified — anything at all that happens — **a local database is maintained.** To find out any file, what it does — your search output, wherever you get output, whatever [paths], **it will print that on your screen.**

### Basic usage

For example, let's see. I do `locate` — the command's name is `locate`; after that what I am doing is **star (`*`)**.

**What does star mean** — it is a **global parameter**; it is used for global. What does this mean: that **at the end there should be `.com`** [or whatever you specify], and **before that there can be anything at all**, anything — any file at all; those have to be located.

But which output should be printed on our screen: all those should be printed which have [that pattern] at the end — that is what you get to see. So **it will print all your [matching] files and show them on the screen.**

### Counting the results

See, however many files [there are] at the end, how many in total — if I count and show you; see, **we can count too**: `wc -l`. Look at this, `1640`.

### `-i` — ignore case

`locate -i` — now look, here, what is it: there is a capital `C`, small `o`, capital `S`, small `f`. **Now it doesn't matter about case sensitivity, because we did `-i`** — meaning **ignore** [case].

### `-n` — limit the number of results

If [you] want to see 10 [results], we can see that too; we can see ten too — **in place of this, we [use] `-n 10`** results.

```bash
locate "*.conf"           # find by pattern
locate -i "*.CONF"        # ignore case
locate -n 10 "*.conf"     # only the first 10 results
locate "*.conf" | wc -l   # count matches
```

---

## Part 2 — ⚠ The database freshness problem

Now we know that the `locate` command uses a **database** to find out our patterns or files.

> **Now this database of ours is useful only as long as the information inside it is UP TO DATE.**

### When it updates

**By default:**
- On a **real server** — it updates **once a day**, because servers are never turned off.
- On **your machine** — **whenever your machine is powered on**, at that time this database updates.

### What this means

> **Anything happening in the meantime — a file being created, deleted, or moved — does not get logged into the database.**

Meaning: as soon as your database updated, it happened once, [when] your machine [booted]. Now my machine has been on for an hour; so it would have updated [then]; and after that, for the next hour or two that my machine runs, **all the files that got created, all the files that got deleted, updated or newly created — all those files will not have been updated in the database.**

**And until they are updated**, it's possible that we are trying to locate some file [and] **that file has already been deleted** — because in the database it is available, but in the meantime what happened, the file got deleted. **So that can happen too.**

### The fix: `updatedb`

> **So what should we do — always keep one thing in mind:** whenever you are going to use the `locate` command, or whenever you feel you have to search something out, then **simply fire the [`updatedb`] command** [first].

Whatever was linked, unlinked, all of them — what will happen inside it — **they will get updated.**

### `-e` — the safety option

Now, there's one more option — a **safety feature**: an option is used with it. **What does this option do — it's possible that [a file] exists or doesn't exist**; [so it checks].

```bash
sudo updatedb              # refresh the database FIRST
locate -e filename         # only show files that actually EXIST
```

### Why learn multiple search commands

So you would have come to know how to use the `locate` command. And the `locate` command — look, it's possible that at any time you suddenly need to search some file in your machine; then how will you be able to?

**You have the `find` command, and the `locate` command too.** That is why I have **shown you multiple commands, represented them, so that whenever you forget some command, some other command will be remembered** by you.

If you have to find out — meaning, **we can locate**; from the name "locate" itself you will remember `locate`'s work; from the name "find" you'll remember `find`'s job. In this manner, it's possible that... "I am grepping some word" — "yes, `grep` is a command too." **So such commands will stay remembered by you.**

So this was a small command of yours, the `locate` command — **a very important command, a very useful command.**

---

## Part 3 — Package Management: the concepts

Now let's talk — a small intro, a small part which is important for you; **it is very necessary for you to understand**, and you will keep coming face to face with it more than anything; you use it on a **daily basis**, whatever you do in cyber security.

**We call it Package Management. VERY VERY VERY IMPORTANT** — wherever you work.

### 3.1 Package formats per distribution

Now it depends which base operating system you use:

| Distribution family | Package extension |
|---|---|
| **Red Hat / Fedora / CentOS** | **`.rpm`** |
| **Debian / Ubuntu / Kali** | **`.deb`** |

If you use a Red Hat–based [system], then at the end you get to see **`.rpm`**. In a [Debian-based] operating system the extension you get to see at the end will be **`.deb`**.

### 3.2 What a repository is

> **A repository is a collection of software and documents** [held centrally].

Normally [for search] we prefer Google; but for Microsoft, the **Microsoft Store** — if we speak in layman's language, **that is a repository** for it. Because what they did — they have **kept all those applications on a centralized server**, all the ones that Microsoft uses or that can be used with Microsoft, all the things it supports; basically you get to see all of them. So you search and download it; and whatever you don't get, you Google it.

**Similarly in Linux, in Kali Linux** — because Kali has its own repository location, Ubuntu has its own repository location, and even [whatever distro] you have will have its own repository location.

Now what happens is that **they too made a centralized server of their own.**

### 3.3 Where the repository address lives

Because — whenever you were configuring [your machine] and a lot of problems were showing up for you — when you [go] inside `/etc`, inside `apt`, you were looking at **`sources.list`**; there you did some configuration, there you put an address with `http`.

> **That address is the repository's address.**

It mentions that for your Linux operating system, for this Kali Linux operating system, **whatever packages you need, or whatever applications/software you need — if you have to download them, you will get them there.**

And this is very big; it's not that... **there is so much software available in it** that we don't even install it in our machine; we install according to the requirement.

```
/etc/apt/sources.list      ← the repository addresses
```

So "repo" means this. And it's not that they stored it once, because its community is very big — because Linux, Kali Linux, is such an operating system that is **open source**; so if you have any problem, somewhere or other you get its solution, and they all do this work. In that community, updating it — if a package is expiring, updating it, updating [things] — and all this, [the community does it].

You update Kali Linux through some command — from where do you update it? **From right there.** Meaning, what: **a centralized collection of your software and documents.** And in Linux, software is what we call **packages**.

---

## Part 4 — ⚠ Dependencies: why repositories matter most

Now let's talk about the requirement for a repo. **Basically the biggest need was to reduce your dependency [problem].**

### What a dependency is

> **Dependency means being dependent on something.**

Now, in our machine there are some packages such that **when they install in your machine, to be installed they too have to depend on something.** That is called a dependency.

### The manual nightmare

**How will the dependency get resolved?** For example, you have to install some software, install some package. Okay:

1. You directly Googled it and **downloaded** it, and **manually unpacked** it and started installing.
2. As soon as you started installing, **it said: "to install me, fulfil these eight dependencies of mine; only then will I install."**
3. Okay, so you [took] those eight, Googled them, and started installing them first.
4. **Now it turned out those eight have their own dependencies too.**

> So now, to install **one** package — **where installing one package with the help of a repository takes you one minute** (if your internet speed is good) — **there it will take you the whole day.** And there's no guarantee you'll manage it in a whole day; it may take you two days, three days, **just to install one package** — resolving dependency after dependency. And until those dependencies are resolved, that package will not install.

### How the repository solves it

When repositories are configured properly, **dependencies get resolved automatically.**

> **You don't even come to know how many [dependencies] there were of that package.** Automatically, from this repository — as soon as you fire the command, from there itself, [the system] knows "here is my repo, and from here all my dependencies get resolved"; **automatically they get installed, and you didn't even come to know when your package got installed.**

**Otherwise, try installing any one package [manually] once in your machine and see — your condition will genuinely become bad**, because you will find so many dependencies you will not be able to wrestle with them.

### The edge case

And sometimes it happens that you find some package that has been updated, so a dependency comes with it **which is not in the repository**; because of that, what you have to do — many times you have to resolve that dependency **from outside**, meaning from Google, and only after that does it install.

So those were some [uses] of repositories.

> **Summary:** what a repository is, what a dependency is, and that in Linux we call software **packages**.

---

## Part 5 — The three package management commands

Now, to manage these [packages] in your machine, **basically three commands are used:**

| Command | Level | Resolves dependencies? |
|---|---|---|
| **`dpkg`** | low-level, works on local `.deb` files | ❌ **No — manual** |
| **`apt` / `apt-get`** | high-level, uses the repository | ✅ **Yes, automatically** |
| **`aptitude`** | high-level, same as apt + extras | ✅ Yes |

---

## Part 6 — `dpkg`

### Listing installed packages

```bash
dpkg -l
```

If I do `dpkg -l`, then I will come to know **how many packages are installed in your machine.** Look, now it is showing 1, 2 — like this; all of these are packages. Look, 34 — there are a lot of pages.

Now this — it opened like the `more`/`less` command. Let me quit. So it showed all those packages in front of you which are installed in your machine.

### Which files did a package install?

If you want to check a package — for example, I have some package; **I want to see which files got installed in our machine because of this package:**

```bash
dpkg -L packagename
```

Now it printed the list of all those files on your screen which got installed in your machine because of this package.

### Which package owns a file?

**If I want to see the detail of one file — by which package was this file installed?**

```bash
dpkg -S /path/to/file
```

For example, see, there is a file [in] your machine; so **you can see this too** in your machine — meaning, **who installed it.**

### Installing a local `.deb`

Now, in this, we install those packages which we basically **Google**, [download] from there, and which have the **`.deb`** extension:

```bash
dpkg -i package.deb        # install
dpkg -r packagename        # remove
```

### Removing

If you have to uninstall/remove any package in your machine — if you have to remove it, how will you do it? `dpkg -r`; **in place of `-i` I will use [`-r`]**, meaning remove.

### ⚠ The dpkg caveat

> **Keep one thing in mind: in the case of the `dpkg` command, we will have to resolve the dependencies MANUALLY** — the ones I was talking about, the example I gave.
>
> **If a package has no dependency, then it will install. Otherwise you have to [handle] all its dependencies** [yourself].

---

## Part 7 — `apt` / `apt-get`

### Update and upgrade

Now, **if you have to update your machine, upgrade it** — how will we do it?

```bash
apt-get update      # refresh the package lists
apt update          # modern form — "get" is no longer needed
apt-get upgrade     # upgrade installed packages
```

It used to be used as `apt-get update`, **but nowadays there's no need to put `get`**; `apt update`. Now this will update your machine.

**If you have to upgrade your machine, then we will do `apt-get upgrade`.**

> **What upgrade does:** whatever software you already have, **it updates them to the present [latest version]** — like software updates keep coming in your mobile; it removes the old version and the new version comes. Similarly here; when you upgrade, it starts upgrading with the latest.

### Where downloaded packages are cached

Now what happens: whatever packages get installed or updated in your machine, **those packages [go to] a local location in our machine**; there they get downloaded.

**Where is that location?** Let me do `ls`:

```
/var/cache/apt/archives/
```

`apt`, after that there is `archives` — so there that information stays.

### Cleaning the cache

**If you want to [clear] all the packages**, then what can I use:

```bash
apt-get clean
```

C-L-E-A-N `clean` — I can use it. Now what is this — **it cleared it completely.** That is why here you are getting to see very few packages, because [on] that machine I keep cleaning.

### Searching for a package

**If you had to search inside it** — if you have to perform a search operation, then what do you do:

```bash
apt-cache search packagename
```

`apt-cache search`, after that you have to give that package's name.

### Installing and removing

```bash
apt-get install packagename     # install
apt-get remove packagename      # remove the package ONLY
apt-get purge packagename       # remove package AND its config files
```

### ⚠ `remove` vs `purge` — the key distinction

> **When I did `remove`, it only removed the installed package — its CONFIGURATION FILE has still not been removed.**
>
> **If you want that when you remove a package, its configuration file is removed along with it** — you don't want to keep it, [don't want it] left behind — then you have to use **`purge`**.

`apt-get purge`, after that that package's name — it will remove it **along with the configuration file.**

> **That is the only difference:** `remove` uninstalls the package; **`purge` uninstalls it WITH the configuration files.**

---

## Part 8 — `aptitude`

If we talk about the **third command, `aptitude`** — if you have to use the `aptitude` command, **for that it is necessary that the `aptitude` package is installed in your machine:**

```bash
apt install aptitude
```

Okay, it was already in my machine, so it shows [that].

### It works the same way

**If you use this command, it works exactly the same** — absolutely, just as `apt` works.

```bash
aptitude update
aptitude install packagename
aptitude search packagename
aptitude remove packagename
```

### The one extra: `safe-upgrade`

**One thing with it:** if you want to **safely patch** your machine — you can call upgrade "patching" too —

```bash
aptitude update
aptitude safe-upgrade
```

> **What benefit will that give: the chances of [errors] in your machine will be REDUCED.**
>
> Meaning, **you are upgrading your machine in a SAFE MODE**, from which whatever errors there are, or the chances of some issue happening, **those will be reduced** in your machine.

### Searching

If you have to search some package, for that too you can do:

```bash
aptitude search packagename
```

**Where will it search? Inside your repository.** If you don't know whether that package is in your repository or not, then for that, simply — the package's name, a small bit of a word that you think might be its name — write that and hit enter, and it will search and show you.

Like I just [searched] `http`; [you get] the information of what to install. Quite a lot of information you get to see.

---

## Part 9 — Configuring the repository

And this is the **repository's location.**

If there's confusion, then do one thing: look at mine and do it. Otherwise, if you want a straightforward option — **simply what you have to do is [search for] the Kali Linux repository file.** Look, in this, whatever is the latest.

**One way** is: if you have to configure — in your machine, if you are using the `apt` command, have to install some package, update, upgrade, [and] some problems are coming, then **you can do it like this**; you can get to see it here.

**Second**, many times you get to see it outside too. For example, if I show — **on Kali's official page you will get the best information**; you get to see it there. So from there too you have to cut/copy/paste, and what you have to do — **you can enable/disable it.**

Okay, this is your way of configuring the repository, [for] whoever had some issue.

```
/etc/apt/sources.list      ← the path where your system's repositories are located
```

Here, what — **that path is given where your system's, your machine's, repositories are located.**

**Either simply what you have to do — you can open this file directly and edit it, cut/copy/paste; otherwise, you can also do it through some commands.** How? Let me write the command and tell:

```bash
add-apt-repository <URL>
```

A-D-D `apt` R-E-P-O-S-I-T-O-R-Y — there is a command. **If that command's colour does not change** [in the terminal], if it stays only white, **then it means that command doesn't exist**; the package is not in your machine.

So `add-apt-repository`, after that what you have to do — simply write the **URL of the repository**.

---

## Part 10 — Troubleshooting package installation

So in this manner you can manage packages in your machine.

Okay, so now what can you do: **if you have to install packages, uninstall them, search — you can do it in three ways: one is the local command `dpkg`, [second] `apt`, and [third] `aptitude`.** And you would have come to know where your repository file is configured.

### If packages won't install

**If any issue happens** — what you have to do: **if packages are not installing or anything at all is coming up**, then what you can do — **check whether the repository is [configured] or not**, whether it is configured correctly.

### The VirtualBox / VMware network adapter check

If you use a **virtual machine**, then sometimes this shows up — these boxes, or VMware, and sometimes [it's] working on some adapter.

For example, you will get to see: when you right click, or go into Settings, and here the **network settings** — here **Bridged, NAT, Host-Only, Custom, LAN**.

> **So among these, many times it's possible that in BRIDGED mode it stops working.** So what you have to do: **simply try changing to NAT mode, or try changing Host-Only.**
>
> Among these three cases, **don't do Host-Only** — that talks about a separate private network. **So shift between these two [Bridged and NAT] and see.**

**What if it still doesn't work?** It means either the [repository] server has gone down a bit; wait a little.

**If after shifting between these it works**, it means the [adapter] above is not working properly, **because there is some misconfiguration, some glitch** inside it, inside VMware — either something happened from updating it, or whatever.

### The troubleshooting sequence

1. **Check the two adapter modes** (Bridged ↔ NAT).
2. **Check your `sources.list`** — is there a problem in it?
3. **Restart once or twice and wait a bit.**
4. If it still doesn't work: **take your machine's version**, then go to **Kali's official website**, take whatever the **latest URL** is, cut/copy/paste it, and perform [the configuration]. **Then your machine will very likely start working.**

> **Doing this much, nobody has had a problem till today.** If anyone does, then we'll see; but so far nobody has had a problem in this chain.

So you can configure packages in your machine like this.

So today's topic was this. Did you understand today's topic? Tell me — up to now, both of these, `locate` command and package management — understood or not? Tell me.

---

## Part 11 — Control Operators

Come on, let's do a bit — a 10-minute topic; we are going to learn about some **control operators.**

### What they are for

> **Why do we use control operators? Control operators are used to EXECUTE MULTIPLE COMMANDS AT ONCE, to join one command with another command.**

Understood? **The basic purpose of a control operator: you have to fire multiple commands at once, so you can use a control operator.**

---

### 11.1 The semicolon `;` — sequential, unconditional

First let's talk about the first control operator, whose name is the **semicolon** control operator.

Now, what happens is that many times we have to execute multiple commands at once; so in such a case we have to execute the commands **serially** — meaning **one after another, serially.**

For example, what I did: there's the `date` command — you saw the `date` command; then `pwd`; okay, this tells [that]. Now [the] `cal` command tells the calendar. These are three commands.

**What can I do — I can use them at once**, [rather] than typing again and again:

```bash
date ; cal ; pwd
```

I took `date`, after that... after that `cal`, after that a **semicolon**, after that I did `pwd`. Simply hit [enter], and it did: first the `date` command, [then the next] command.

### ⚠ The key property

> **Now keep one thing in mind: it definitely operates [each one], but IT DOESN'T MATTER whether the first command failed or passed.**
>
> What it does: **if its output is an error, it will show the error on screen; and if it is successful, the successful output — it will show that too.** Meaning **it doesn't care whether the first command executed or not; it does not depend on that.** But **it works in series** — first, then second; it works like that.

**Demonstration:**

```bash
zdate ; cal ; pwd
```

For example I [typed] `zdate` — there's no such command — and after that `cal`, after that `pwd`.

See: since `zdate` is not a command, **it showed the error on your screen; after that the calendar's output, after that this output.**

---

### 11.2 The ampersand `&` — background / parallel

The next operator that comes — let's talk about the **second operator**, the **ampersand `&`** operator.

**This too comes in useful for executing multiple commands**, but **what it does — it works in PARALLEL.**

```bash
date & cal & pwd
```

For example, how — I did `date &`. **What does this mean: the command that executes first — it puts one in the BACKGROUND and does the other in parallel, alongside.** But **whichever one's output comes first will be shown on screen; but both of their outputs will come.**

For example, what I did — `date` command, and okay; `date &`, [and] two commands I'll do; let me see the third, it'll work: `date & cal`, `date & pwd`.

So what I did — like, it put the first two [in the background], and after that its [output] came at the same time on screen; after that the calendar's output was going to come, after that when `date`'s output came, after that the second one.

> **In this manner it gets commands executed together.**

---

### 11.3 `$?` — the exit status

But the **third** control [operator]... after that let's do — that is the **question mark**; it's your `$?`. [Music]

**The control operator [tells you] whether [the previous command] executed successfully or not.** Basically, what we do — we call it [the exit status]; how they are created, we will learn that too in this.

| Value of `$?` | Meaning |
|---|---|
| **0** | the previous command was **SUCCESSFUL** |
| **non-zero** (1, 127, any random value) | the previous command **FAILED** |

We will learn: **either it is zero** — [if] your previous command was successful, then **its value will be 0.** If your previous command did not execute successfully, then **what value will come — 1, or any random value will come; depends on the machine.**

**Demonstration:**

```bash
pwd
echo $?        # 0 — success
```

For example, how — what I did: I did `echo`; I gave `$?`. **`$?` is a variable, a system-defined variable**, whose [value] comes from here. Look, this is a variable — because it is a variable.

So it's fine, we start. [The command] was successful, that's why it showed the result.

```bash
zcallo         # not a command
echo $?        # 127 — failure
```

Now I said `z-c-a-l-l-o`; I fired some random command; hit enter. **Now this command was not successful.** Okay, I do `echo $?` — this is **127**.

I said, any random value — **what does it mean: my previous command's output, if it came other than zero, it means it was not successful.**

> **Now this — IT IS VERY HELPFUL IN BASH SCRIPTING**: that your command did not execute — **for tracking all these things it is quite helpful**, in our bash scripting.

---

### 11.4 `&&` — logical AND

Now let's talk about our **fourth** operator, which is the one we call the **AND operator**.

**Or, we can say** — as all of you have passed [class] 12, you'd have seen [truth tables] there — **what does AND mean: condition1 AND condition2.**

| Condition 1 | Condition 2 | Result |
|---|---|---|
| true | true | **TRUE** — command runs |
| true | false | false |
| false | — | **false — second never runs** |

So we take two conditions: **if both conditions are true, then their output will be TRUE**, so the command will show your successful output. **If out of condition 1 and 2 any output is false, then what will happen — the final output will be FALSE.**

**I repeat again:** if condition 1 is true, and if condition 2 is also true — **if both conditions are true — it means it will be true. If out of the two conditions any one condition is false, then FALSE will come.** This is the AND operator.

**Demonstration:**

```bash
pwd && cal        # both run — condition1 true AND condition2 true
```

For example, what I did first — because condition 1 was true, and condition 2 was also true.

```bash
zls && cal        # condition1 FAILS
```

Now what I did: condition 1, I made it `zls`; hit enter. **Now what it said — because condition 2 was true, but condition 1 was false, therefore it showed the error in its output**, showed the problem.

---

### 11.5 `||` — logical OR

**The next operator you have — we call it the LOGICAL OR operator.** [Which] we use — you know, in logical OR any one condition [suffices].

> **What happens in logical OR: if your FIRST condition became true, then it will NOT go to the second condition** — it will show the first condition's output.
>
> **Meaning: "this — or if not this, then that."** That is what it means.

**Demonstration:**

```bash
pwd || cal        # first succeeds -> second never runs
```

Look, I did the double pipe. Now see one thing — the first output happened.

```bash
zdate || cal      # first FAILS -> second runs
```

**If I made the first condition wrong** — what did it do: it showed on the screen "brother, the `zdate` command of yours is wrong, this is its error"; **and after that what it did — it showed the whole second [output] on the screen.**

> **It will go into the second condition only when your first condition became FALSE.** That is the story of the OR operator.

---

### 11.6 Combining them

Now what happens is that **we can use both these operators together.** To use them — for example, [if a file] exists, I made a conditional statement; it fails because the condition [was not] fulfilled.

```bash
command1 && echo "SUCCESS" || echo "FAILED"
```

---

## Part 12 — Summary of control operators

| Operator | Name | Behaviour |
|---|---|---|
| `;` | semicolon | Run **sequentially**, regardless of success or failure |
| `&` | ampersand | Run in **parallel** / background |
| `$?` | exit status | **0** = previous command succeeded; **non-zero** = failed |
| `&&` | logical AND | Run the second **ONLY IF** the first **succeeded** |
| `\|\|` | logical OR | Run the second **ONLY IF** the first **failed** |

---

## Closing

I hope — we had three topics to clear, ours are done: **control operators**; and after that I gave the **introduction to package management**, a bit of how to do package management; **third, what I told you people, about the `locate` command.**

[In the] capsule course **we have three days left.** There are some topics left, among which the most important — I will tell you about the [`ss`] command, and one more topic is left, in this itself, the **`history` command**. And in those two or three days we will do it quite well.

So we will use that [time]; our capsule course [will finish]. And I hope you are enjoying the course.

**If you people have a complaint, if you feel that our course is not good, "not good for you", or "not the content", "there's no content in it, there's nothing in it" — then you are very open, free to comment; negative comment, I have no problem.**

I am providing my 100%, because at [whatever] level a security engineer should provide to you at this time — **I am providing more than the rest of the people**; as much as you should know, as much detail as should be told — **because wherever you go to do a course, you will not get to see this much detail anywhere.**

Anywhere, it isn't [more than] three classes; your [course] is finished. **But I don't do it this type of way; my method is different.** I taught like this so that you get to learn — [rather] than to pass the time.

Anyway, gradually our live classes [attendance] — no matter; it won't make a difference to me.

So — bye bye, good night, take care.
