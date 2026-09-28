# Explanation — Day 12: `locate`, Package Management & Control Operators

**Lecture:** 012 — Kali Linux Free Capsule Course, Day 12
**Translation:** [`english/012 - Kali Linux Free Capsule Course - Day 12.md`](../english/012%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2012.md)

---

## Part 1 — `locate`

### 1.1 How it differs from `find`

| | `find` (Day 10) | `locate` |
|---|---|---|
| Method | **Walks the file system live** | Queries a **pre-built local database** |
| Speed | Slower | **Much faster** |
| Accuracy | **Always current** | **Only as fresh as the database** |

> **`locate` uses a LOCAL DATABASE present in your system.** Whenever files are created, deleted or modified, that database is maintained.

### 1.2 Usage

```bash
locate "*.conf"            # find by pattern
locate -i "*.CONF"         # ignore case
locate -n 10 "*.conf"      # limit to 10 results
locate -e filename         # only show files that actually EXIST
locate "*.conf" | wc -l    # count the matches
```

**The `*` wildcard** is a global parameter — "anything at all before this, ending with that."

### 1.3 ⚠ The staleness problem

**When does the database actually update?**

| System | Update frequency |
|---|---|
| **Real server** | **Once a day** (servers are never powered off) |
| **Your machine** | **At power-on** |

> **Consequence:** anything happening *in between* — files created, deleted or moved — **is not in the database.**

**The practical failure:** you `locate` a file, the database says it exists, but it was deleted two hours ago. You get a path to a file that is gone.

### 1.4 The fix

> **Always run `updatedb` before relying on `locate`.**

```bash
sudo updatedb        # refresh the database first
locate filename      # now the results are current
```

The `-e` flag is a partial safety net — it checks that each result **actually exists** before printing it.

### 1.5 Why learn several search commands

A deliberate teaching point:

> Multiple commands are shown **so that when you forget one, another comes to mind.** The names themselves are the mnemonic — `locate` locates, `find` finds, `grep` greps.

---

## Part 2 — Package management concepts

Described as **"VERY VERY VERY IMPORTANT"** and something you will use on a daily basis.

### 2.1 Package formats

| Distribution family | Extension | Tools |
|---|---|---|
| **Red Hat / Fedora / CentOS** | **`.rpm`** | `rpm`, `yum`, `dnf` |
| **Debian / Ubuntu / Kali** | **`.deb`** | `dpkg`, `apt`, `aptitude` |

> In Linux, **software is called a "package."**

### 2.2 What a repository is

> **A repository is a centralized collection of software and documents** held on a server.

**The analogy given:** the **Microsoft Store** is, in layman's terms, a repository — Microsoft keeps all supported applications on a centralized server; you search and download from there, and what you can't find, you Google.

Every distribution has its own: Kali has one, Ubuntu has one, and so on. Because Linux is **open source**, a community maintains and updates these packages continuously.

### 2.3 Where the address lives

```
/etc/apt/sources.list
```

The `http://...` lines in this file **are the repository addresses.** They tell your system where to fetch packages from. This is the file people end up editing when package installation breaks.

---

## Part 3 — ⚠ Dependencies: the core argument

This is the most important conceptual content in the session.

### 3.1 What a dependency is

> **Dependency means being dependent on something.** Some packages, in order to install, must first have other packages present.

### 3.2 The manual nightmare — dependency hell

Walk through what happens **without** a repository:

1. You Google a package and **download the `.deb` manually.**
2. You start installing. It says: *"fulfil these **eight** dependencies first."*
3. You Google and download those eight.
4. **Those eight have their own dependencies.**
5. Those have dependencies. And so on.

> **The comparison that makes the point:**
>
> | Method | Time to install ONE package |
> |---|---|
> | **With a repository** | **≈ 1 minute** |
> | **Manually** | **A whole day — possibly two or three** |
>
> And there is no guarantee you finish at all.

### 3.3 How the repository solves it

> **Dependencies get resolved automatically.** You don't even come to know how many there were — the system knows where its repo is, pulls everything needed, and **you didn't even notice when your package got installed.**

### 3.4 The edge case that still bites

Occasionally an **updated package needs a dependency that isn't in the repository.** Then you must resolve that one dependency manually from outside — and only then does it install.

---

## Part 4 — The three tools

| Tool | Level | Source | Resolves dependencies? |
|---|---|---|---|
| **`dpkg`** | low-level | **local `.deb` files** | ❌ **No — manual** |
| **`apt` / `apt-get`** | high-level | **the repository** | ✅ **Yes, automatically** |
| **`aptitude`** | high-level | the repository | ✅ Yes, + safe-upgrade |

---

## Part 5 — `dpkg`

```bash
dpkg -l                    # list ALL installed packages
dpkg -L packagename        # which FILES did this package install?
dpkg -S /path/to/file      # which PACKAGE owns this file?
dpkg -i package.deb        # install a local .deb
dpkg -r packagename        # remove
```

### ⚠ The caveat

> **With `dpkg` you must resolve dependencies MANUALLY.** If the package has no dependencies it installs fine. Otherwise you are back in dependency hell.

**`dpkg -S` is quietly very useful** in security work — given a suspicious file, it tells you which package put it there.

---

## Part 6 — `apt` / `apt-get`

### Core commands

```bash
apt update                       # refresh package LISTS (modern form)
apt-get update                   # older form — "get" no longer needed
apt-get upgrade                  # upgrade installed packages
apt-get install packagename
apt-get remove packagename
apt-get purge packagename
apt-cache search packagename
apt-get clean
```

### What `upgrade` actually does

> Like software updates on your mobile: **it removes the old version and the new version comes in.** `upgrade` brings all installed software to the latest available version.

### Where packages are cached

```
/var/cache/apt/archives/
```

Every downloaded `.deb` lands here. Over time this grows large.

```bash
apt-get clean        # empties the cache
```

### ⚠ `remove` vs `purge` — the distinction that matters

| Command | Removes the package | Removes its config files |
|---|---|---|
| `apt-get remove` | ✅ | ❌ **No — they stay behind** |
| `apt-get purge` | ✅ | ✅ **Yes** |

> **`remove` leaves the configuration files on the system.** If you want a genuinely clean uninstall — nothing left behind — **use `purge`.**

---

## Part 7 — `aptitude`

Must be installed first:

```bash
apt install aptitude
```

It **works exactly like `apt`**:

```bash
aptitude update
aptitude install packagename
aptitude search packagename
aptitude remove packagename
```

### The one genuine extra: `safe-upgrade`

```bash
aptitude update
aptitude safe-upgrade
```

> **You are upgrading your machine in SAFE MODE** — the chances of errors or issues arising are **reduced**. Upgrade can also be thought of as **patching**.

---

## Part 8 — Configuring the repository

```
/etc/apt/sources.list        ← the path where repositories are defined
```

**Two ways to change it:**

1. **Edit the file directly** — open it, cut/copy/paste the correct URLs, enable/disable lines.
2. **Use the command:**

```bash
add-apt-repository <URL>
```

> **Terminal tip given in class:** if a command's name **doesn't change colour** when you type it — it stays plain white — **that command doesn't exist** on your system; the package isn't installed.

**Best source for correct URLs:** the **official Kali website**, which always carries the current repository lines.

---

## Part 9 — Troubleshooting failed package installs

A practical sequence for the single most common beginner problem.

### Step 1 — Check the VM network adapter

In VirtualBox/VMware settings you have: **Bridged, NAT, Host-Only, Custom, LAN**.

> **Bridged mode often stops working.** Switch between **Bridged ↔ NAT** and retry.
>
> ⚠ **Do not use Host-Only** — that is a separate private network with no internet access.

| Result | Diagnosis |
|---|---|
| Works after switching | The original adapter has a **misconfiguration or glitch** in VMware/VirtualBox |
| Still fails | Move to step 2 |

### Step 2 — Check `sources.list`

Is the repository correctly configured? Is there a problem in the file?

### Step 3 — Restart and wait

The repository server may be temporarily down.

### Step 4 — Rebuild the sources list

1. Get your **machine's version**.
2. Go to **Kali's official website**.
3. Copy the **latest repository URL**.
4. Paste it into `sources.list`.

> *"Doing this much, nobody has had a problem till today."*

---

## Part 10 — Control Operators

> **Control operators are used to execute multiple commands at once, and to join one command with another.**

### 10.1 `;` — sequential, unconditional

```bash
date ; cal ; pwd
```

Runs each command **in series, one after another.**

> ⚠ **It does NOT care whether the previous command succeeded or failed.** An error is printed and it moves on to the next command regardless.

```bash
zdate ; cal ; pwd
# error from zdate, then cal runs, then pwd runs
```

### 10.2 `&` — background / parallel

```bash
date & cal & pwd
```

**Runs commands in parallel** — one is pushed to the background while the other proceeds. **Whichever finishes first prints first**, but all outputs appear.

### 10.3 `$?` — the exit status

```bash
pwd
echo $?        # 0   -> success

zcallo
echo $?        # 127 -> failure
```

| Value | Meaning |
|---|---|
| **0** | the previous command **succeeded** |
| **non-zero** | the previous command **failed** (the specific number varies) |

`$?` is a **system-defined variable** holding the exit status of the last command.

> **This is very helpful in BASH SCRIPTING** — it is how a script detects that a command did not execute, and is the basis of error handling.

### 10.4 `&&` — logical AND

```bash
pwd && cal        # both run
zls && cal        # zls fails -> cal NEVER runs
```

> **Run the second command ONLY IF the first succeeded.**

| Cond 1 | Cond 2 | Result |
|---|---|---|
| true | true | **TRUE** |
| true | false | false |
| **false** | — | **false — second never executes** |

### 10.5 `||` — logical OR

```bash
pwd  || cal       # first succeeds -> cal NEVER runs
zdate || cal      # first fails    -> cal RUNS
```

> **Run the second command ONLY IF the first FAILED.** Read it as: *"this — or, if not this, then that."*

### 10.6 Combining them

```bash
command && echo "SUCCESS" || echo "FAILED"
```

The classic success/failure idiom — the foundation of conditional logic in shell scripts.

---

## Part 11 — Complete cheat sheet

```bash
# ---- locate ----
sudo updatedb              # ALWAYS refresh first
locate "*.conf"
locate -i pattern          # ignore case
locate -n 10 pattern       # limit results
locate -e pattern          # only existing files

# ---- dpkg (local .deb, NO dependency resolution) ----
dpkg -l                    # list installed
dpkg -L package            # files installed by a package
dpkg -S /path/to/file      # which package owns a file
dpkg -i package.deb        # install
dpkg -r package            # remove

# ---- apt (repository, automatic dependencies) ----
apt update                 # refresh lists
apt-get upgrade            # upgrade everything
apt-get install package
apt-get remove package     # leaves config files  ⚠
apt-get purge  package     # removes config too   ✔
apt-cache search package
apt-get clean              # empty /var/cache/apt/archives/

# ---- aptitude ----
apt install aptitude
aptitude update
aptitude safe-upgrade      # upgrade in SAFE MODE
aptitude search package

# ---- repository config ----
/etc/apt/sources.list
add-apt-repository <URL>

# ---- control operators ----
cmd1 ;  cmd2               # sequential, regardless of outcome
cmd1 &  cmd2               # parallel / background
echo $?                    # 0 = success, non-zero = failure
cmd1 && cmd2               # run cmd2 ONLY IF cmd1 succeeded
cmd1 || cmd2               # run cmd2 ONLY IF cmd1 failed
cmd && echo OK || echo FAIL
```

---

## Part 12 — Self-check questions

1. How does `locate` differ from `find` in method, speed and accuracy?
2. When does the `locate` database update on a server? On your laptop?
3. Describe the failure mode caused by a stale database. What command prevents it?
4. What does `-e` do, and what problem does it partially address?
5. Which package extension belongs to Red Hat systems? To Debian/Kali?
6. Define "repository." What everyday analogy was used?
7. What is the path to the repository configuration file?
8. Define "dependency." Walk through why manual installation becomes dependency hell.
9. Contrast the time taken to install one package with and without a repository.
10. Name the three package tools and state which does **not** resolve dependencies.
11. Which `dpkg` flag tells you which package a given file came from? Why is that useful in security work?
12. What is the exact difference between `apt-get remove` and `apt-get purge`?
13. Where are downloaded packages cached, and how do you clear it?
14. What does `aptitude safe-upgrade` offer over a plain upgrade?
15. What does it mean if a command's name doesn't change colour in the terminal?
16. Give the four-step troubleshooting sequence for packages that won't install. Which adapter mode should you avoid, and why?
17. State the behaviour of `;`, `&`, `&&` and `||`, and the difference between them.
18. What values can `$?` take and what do they mean? Why does it matter in scripting?
19. Write a one-liner that prints "SUCCESS" if a command works and "FAILED" if it doesn't.

---

## Part 13 — Course status

**Three days remain** in the capsule course. Topics still to come:

- The **`ss`** command
- The **`history`** command
- Remaining networking material

The trainer's closing note invites negative feedback openly, and states the teaching philosophy: detail over speed, *"because wherever you go to do a course, you will not get to see this much detail anywhere."*
