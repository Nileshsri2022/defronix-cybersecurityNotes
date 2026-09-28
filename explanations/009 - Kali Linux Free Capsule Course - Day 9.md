# Explanation — Day 9: File Security, Permissions & `umask`

**Lecture:** 009 — Kali Linux Free Capsule Course, Day 9
**Translation:** [`english/009 - Kali Linux Free Capsule Course - Day 9.md`](../english/009%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%209.md)
**Builds on:** Day 7–8 (users, groups, privileges)

---

## Part 0 — Housekeeping: take VirtualBox snapshots

Before the topic, a piece of practical advice worth acting on immediately.

### The workflow

1. Install your Kali VM → **take Snapshot 1**.
2. Install a tool, verify it works properly → **take Snapshot 2**, then **delete Snapshot 1**.
3. Repeat after every successful configuration.

### Why it matters

A downloaded tool may contain **malware** that tampers with system settings. Or a configuration followed from YouTube/Google leaves the machine behaving strangely, with no record of what changed.

> Without a snapshot you are stuck with the broken state. With one, you **switch back to a working machine instantly.**

**The cost being avoided:** tools are collected with great difficulty, often over limited internet. Reinstalling the whole machine and re-finding every tool is entirely time-consuming wasted effort.

> **Make this a habit** — especially as a security engineer.

---

## Part 1 — Why file security exists

> Without file security, a malicious thing **can do anything wrong** in your machine. With file security in place, it **cannot**.

Two categories are taught:

| Type | Covered |
|---|---|
| **Basic file permissions** | Day 9 (this session) |
| **Advanced file permissions** | Day 10 |

---

## Part 2 — Reading `ls -l`

```
-rw-r--r--   1   root  root  4096  Sep 28 15:58  file.txt
    │        │    │     │      │        │            │
    │        │    │     │      │        │            └─ name
    │        │    │     │      │        └─ timestamp
    │        │    │     │      └─ size
    │        │    │     └─ group owner
    │        │    └─ owner
    │        └─ number of links
    └─ file type + permissions
```

### 2.1 The inode number

> **Every file and directory has an inode number.** It helps the system **identify the file** — where it is stored and where its data lives.

- A file system has a **limited number of inodes**.
- That limit depends on the **capacity of the disk and file system** — a bigger disk has more inodes, a small machine fewer.
- This connects directly back to the **inode table** from the Day 4 file descriptor lecture.

View with `ls -i`.

### 2.2 File type characters (first column)

| Char | Type |
|---|---|
| `-` | regular file |
| `d` | directory |
| `l` | symbolic link |
| `b` | **block** file — hard disk or hardware part |
| `c` | **character** file |
| `s` | **socket** file |

### 2.3 The permission string

The nine characters after the type split into three groups of three:

```
rw-  r--  r--
 │    │    │
user group others
(owner)
```

---

## Part 3 — The three permissions

**Crucially, `r`, `w` and `x` mean different things on a file versus a directory:**

| Letter | Value | On a **file** | On a **directory** |
|---|---|---|---|
| **`r`** | 4 | read the contents | **list** the contents (`ls`) |
| **`w`** | 2 | **modify** the file | create / delete entries inside |
| **`x`** | 1 | **run** it as a program | **`cd` into** it |

> **The directory `x` bit is the one people forget.** Without execute on a directory you cannot enter it at all — `cd` fails regardless of read permission.

### Octal values

| Octal | Binary | Permission |
|---|---|---|
| 0 | `---` | none |
| 1 | `--x` | execute only |
| 2 | `-w-` | write only |
| 3 | `-wx` | write + execute |
| 4 | `r--` | read only |
| 5 | `r-x` | read + execute |
| 6 | `rw-` | read + write |
| **7** | `rwx` | **all three** (4+2+1) |

---

## Part 4 — Changing ownership

### Who is allowed to do it

> **Two parties can change group ownership:** (1) **root**, and (2) a **user who is a member of that group**.

### The commands

```bash
chown kali file            # change the file OWNER
chgrp kali file            # change the GROUP owner
chown kali:kali file       # change BOTH at once
```

The `owner:group` syntax saves running two commands.

---

## Part 5 — `chmod`: changing permissions

Two methods.

### 5.1 Octal (numeric) method

```bash
chmod 777 file      # rwx rwx rwx
chmod 644 file      # rw- r-- r--
chmod 755 dir       # rwx r-x r-x
```

> ⚠ **`chmod 777` should never be kept** on a real system — it was shown only for practice.

### 5.2 Symbolic (alphabetical) method

**Who:**

| Target | Means |
|---|---|
| `u` | user (owner) |
| `g` | group |
| `o` | others |
| `a` | all |

**Operator:**

| Symbol | Meaning |
|---|---|
| `+` | **add** the permission |
| `-` | **remove** the permission |
| `=` | **replace** entirely — wipes existing and sets exactly this |

```bash
chmod g-x file        # remove execute from group
chmod u+x file        # add execute for user
chmod u=w file        # user now has ONLY write
chmod g+x file        # add execute for group
```

### 5.3 Setting all three at once

```bash
chmod u=rw,g=r,o=r file
```

Comma-separated clauses set user, group and others in a single command.

> **The distinction to internalise:** `+` and `-` **adjust** the existing permissions; `=` **replaces** them wholesale.

---

## Part 6 — `umask`

```bash
umask
# 0022
```

> **The umask value defines what the effective permissions will be for any file or directory created in your system.** Default permissions are decided by this value.

### Reading the four digits

| Position | Represents |
|---|---|
| 1st | special bits (setuid/setgid/sticky) |
| 2nd | the **owner** |
| 3rd | the **group owner** |
| 4th | **other users** |

### The key mental flip

**umask is subtracted, not granted.** A umask digit is the permission being *withheld*:

| umask digit | Permission removed | Result from 7 |
|---|---|---|
| 0 | nothing | `rwx` |
| 2 | write | `r-x` |
| 7 | everything | `---` |

---

## Part 7 — Calculating effective permissions

### 7.1 The maximum permission rule ⭐

This is the crux of the session:

| Object | Maximum default | Reason |
|---|---|---|
| **File** | **666** (`rw-rw-rw-`) | **Linux never grants execute to a file by default** |
| **Directory** | **777** (`rwxrwxrwx`) | A directory **needs** `x`, otherwise you could never `cd` into it |

> *"If there were no execute permission [on a directory], you would not be able to `cd`."*

### 7.2 The formula

```
Effective permission = Maximum permission − umask
```

### 7.3 Worked examples with umask 022

**File:**
```
666 − 022 = 644      →  rw- r-- r--
```

**Directory:**
```
777 − 022 = 755      →  rwx r-x r-x
```

Which is exactly what you observe on a freshly created file and folder.

---

## Part 8 — The security angle ⭐

This is the most valuable part of the lecture — a genuine attack idea and the kernel policy that defeats it.

### 8.1 The attack idea

1. An attacker writes **malware** that gets onto your machine.
2. Before creating its files, it **changes the umask to `000`**.
3. Every file it creates would then be born with **`777`** — including **execute** permission.
4. The payload becomes directly runnable.

### 8.2 Why it fails

> **You can change the umask value — no issue. But you cannot overpass the policy.**

The system enforces a hard ceiling: **a file can never be created with execute permission by default, no matter what the umask says.**

### 8.3 The demonstration

```bash
umask 000
touch file3
ls -l file3        # 666 — NOT 777. Execute was withheld.

mkdir test
ls -ld test        # 777 — directories DO get full permissions
```

Even with umask `000` explicitly requesting `rwx` for everyone, **the file still comes out without execute.** The directory does get `777`, because directories legitimately need `x`.

> **The common misconception corrected:** people calculate the umask table, set a value, and assume the file will get exactly that. It won't — **the policy caps files at 666 regardless.**

### 8.4 What this forces the attacker to do

Since the umask route is blocked, the attacker **must obtain root** in order to explicitly `chmod +x` the malware. That raises the bar considerably — and is why this default exists.

> A normal user can create files in their own home account, but **to make a payload executable you need privilege** — which loops back to the privilege-escalation material of Day 8.

---

## Part 9 — `mkdir -m`: overriding umask at creation

Instead of creating something with default permissions and then fixing it with `chmod`:

```bash
mkdir -m 700 test3
ls -ld test3        # rwx------ immediately
```

`-m` sets the mode **at creation time**, bypassing the umask-derived default. Useful when a directory must never exist, even briefly, with loose permissions.

---

## Part 10 — Complete cheat sheet

```bash
# Inspect
ls -l              # permissions, links, owner, group, size, time, name
ls -i              # inode numbers
ls -ld dir         # a directory's own permissions, not its contents

# File types:  -  file    d directory   l link
#              b  block   c character   s socket

# Permissions:  r=4  w=2  x=1
#   file:  r read   w modify   x run
#   dir :  r list   w create/delete   x cd into

# Ownership
chown user file
chgrp group file
chown user:group file

# chmod — octal
chmod 644 file
chmod 755 dir
chmod 700 private

# chmod — symbolic
chmod u+x file            # add
chmod g-x file            # remove
chmod o=r  file           # replace
chmod u=rw,g=r,o=r file   # all three at once
chmod a+r file            # everyone

# umask
umask                     # show (e.g. 0022)
umask 027                 # set
# Effective = maximum − umask
#   file:  666 − umask
#   dir :  777 − umask

# Override at creation
mkdir -m 700 dirname
```

---

## Part 11 — Practice question set in class

> Given a file, configure it so the **members of a particular group can read and modify** it.
>
> **Then verify** — log in as one of those group members and confirm they genuinely can modify the file.

Post your answer with a screenshot.

*(Approach: set the file's group owner with `chgrp`, then grant `rw` to the group with `chmod g+rw`, then test as a member.)*

---

## Part 12 — Self-check questions

1. Why should you snapshot a VM after every successful tool install? What does it protect against?
2. What is an inode number, and what determines how many a file system has?
3. Name the six file-type characters and what each indicates.
4. What do `r`, `w`, `x` mean **on a file**? And **on a directory**?
5. Which permission must a directory have for `cd` to work?
6. Give the octal value for `rwx`, `r-x`, `rw-`, `r--`.
7. Who is permitted to change a file's group ownership?
8. Difference between `chown`, `chgrp`, and `chown user:group`.
9. Difference between `+`, `-` and `=` in symbolic `chmod`.
10. Write one command setting user `rw`, group `r`, others `r`.
11. What does umask define? Are its digits granted or withheld?
12. What are the four umask positions?
13. What is the maximum default permission for a **file**? For a **directory**? Why do they differ?
14. Calculate the effective permission of a new file and a new directory with umask `027`.
15. Describe the malware-umask attack and explain precisely why it fails.
16. With `umask 000`, what permissions does a new file get? A new directory? Why the difference?
17. What must an attacker obtain in order to make a payload executable, and why?
18. What does `mkdir -m 700` do differently from `mkdir` followed by `chmod 700`?

---

## Part 13 — Coming up next

**Day 10 — Advanced File Security**, expected to run longer than this session. It covers the special permission bits and what happens to them when a Linux machine is attacked.
