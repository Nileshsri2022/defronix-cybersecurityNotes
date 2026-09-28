# Explanation — Day 10: Advanced File Permissions & `find`

**Lecture:** 010 — Kali Linux Free Capsule Course, Day 10
**Translation:** [`english/010 - Kali Linux Free Capsule Course - Day 10.md`](../english/010%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2010.md)
**Builds on:** Day 9 (standard permissions, `chmod`, `umask`)

---

## Overview

Day 9 covered the **standard** permissions (`rwx` for user/group/other). Day 10 covers the **three advanced permission bits** that sit on top of them, then introduces `find`.

| Bit | Applies to | Purpose |
|---|---|---|
| **Sticky Bit** | directories | only the **file owner** may delete their file |
| **SGID** | directories | new files inherit the **directory's group** |
| **SUID** | executables | run the file **as its owner** (usually root) |

> **Why this matters:** *"People don't know about SUID and SGID — and your privilege escalation happens on the basis of these."*

---

## Part 1 — The Sticky Bit

### 1.1 The problem it solves

A real scenario from the lecture:

1. A company project has **20–30 people** working in one **shared common directory**.
2. Everyone works there because the **manager** reviews all the files in one place.
3. Some team members resent each other. One person produces a good report; another doesn't.
4. The one who couldn't produce a good report **opens the other user's file**, sees the good work, and **deletes it**.
5. The victim logs in the next day — **the file simply isn't there.**

> **The requirement:** no user should be able to delete another user's file, even in a fully shared directory.

### 1.2 What the sticky bit does

> **Whoever owns a file is the only one who can delete it.** Nobody else can, regardless of the directory's permissions.

You already met this on **Day 2** — it is exactly why `/tmp` is world-writable yet safe.

### 1.3 The demonstration

**Without the sticky bit:**

```bash
# as user1
cd /home/common
touch user1.txt          # user1 owns this file

# as user2
whoami                   # user2
ls -l user1.txt          # owner is user1
rm user1.txt             # SUCCEEDS — the file is gone
```

**Applying it:**

```bash
chmod +t /home/common
ls -ld /home/common
# drwxrwxrwt   ← note the 't' in the last position
```

**After:** `user2` can no longer delete `user1`'s file.

### 1.4 Reading the bit

The sticky bit appears **in place of the `x`** in the *others* position:

| Display | Meaning |
|---|---|
| **small `t`** | sticky bit set **AND** execute permission present |
| **capital `T`** | sticky bit set **WITHOUT** execute permission |

> **The capital/lowercase rule applies to all three advanced bits** — capital means the underlying execute bit is missing.

### 1.5 Setting and removing

```bash
chmod +t  /home/common      # add (symbolic)
chmod -t  /home/common      # remove (symbolic)
chmod 1777 /home/common     # add (octal — leading 1)
chmod 0777 /home/common     # remove (octal — leading 0)
```

> **The fourth (leading) octal digit is the advanced permission digit.** `1` = sticky bit.

---

## Part 2 — SGID (Set Group ID)

### 2.1 What it does

> **If SGID is set on a directory, it makes sure that every file or directory created inside it inherits the directory's group owner.**

### 2.2 Why you want it

A project directory is shared by many members. You want **every file created inside it to belong to the project group**, so all members can read each other's work according to the group permissions.

**Without SGID:** a new file gets the *creator's* primary group — so you must **manually change the group ownership again and again**, for every file, forever.

**With SGID:** it happens automatically.

### 2.3 The demonstration

**The problem first:**

```bash
chmod 777 /tmp/project90
chgrp project /tmp/project90     # directory's group = project

cd /tmp/project90
touch testfile.txt
ls -l testfile.txt
# group owner is the CREATOR's group — not "project"
```

**Applying SGID:**

```bash
chmod g+s /tmp/project90
ls -ld /tmp/project90
# drwxrws---   ← 's' replaces 'x' in the GROUP position
```

Now every new file inside inherits the `project` group automatically.

### 2.4 Reading and removing

| Display | Meaning |
|---|---|
| **small `s`** (group position) | SGID set **with** execute |
| **capital `S`** (group position) | SGID set **without** execute |

```bash
chmod g+s dir       # add
chmod g-s dir       # remove
chmod 2777 dir      # octal — leading 2 = SGID
```

---

## Part 3 — SUID (Set User ID)

### 3.1 The puzzle that motivates it

A normal user has no privileges — yet:

```bash
passwd          # a normal user CAN change their own password
```

But changing a password means **writing to `/etc/shadow`**, which (from Day 8) **only root can access.**

**How is that possible?**

### 3.2 The answer

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x  1 root root ...
#    ↑ 's' in the USER position — SUID is set
```

> **SUID means the file is executed as if its own owner had executed it.** Since `/usr/bin/passwd` is owned by **root**, it runs **as root** no matter who launches it.

The same applies to **`sudo`** — SUID is set on it too, which is how it can elevate at all.

### 3.3 Reading and setting

| Display | Meaning |
|---|---|
| **small `s`** (user position) | SUID set **with** execute |
| **capital `S`** (user position) | SUID set **without** execute |

```bash
chmod u+s file      # add
chmod u-s file      # remove
chmod 4755 file     # octal — leading 4 = SUID
```

### 3.4 ⚠ The security significance

SUID is the single most abused mechanism in **Linux privilege escalation**:

- A SUID root binary runs **with root's power**.
- If that binary can be made to run arbitrary commands, **the attacker becomes root**.
- Hence the classic enumeration step: **find every SUID binary on the system** and check it against known exploits.

```bash
find / -perm -4000 -type f 2>/dev/null     # find all SUID binaries
find / -perm -2000 -type f 2>/dev/null     # find all SGID binaries
```

---

## Part 4 — The three bits summarised

| Bit | Octal | Symbolic | Position shown | Set on | Effect |
|---|---|---|---|---|---|
| **SUID** | **4** | `u+s` | **user** `x` → `s` | executables | run as the **file's owner** |
| **SGID** | **2** | `g+s` | **group** `x` → `s` | directories | new files inherit the **directory's group** |
| **Sticky** | **1** | `+t` | **others** `x` → `t` | directories | only the **owner** may delete their files |

```bash
chmod 4755 file     # SUID
chmod 2775 dir      # SGID
chmod 1777 dir      # Sticky
chmod 7777 x        # all three (4+2+1)
```

> Lowercase letter = the execute bit is also present. **Uppercase = execute is missing.**

---

## Part 5 — The `find` command

> Described as a **very important command** — necessary knowledge whatever you go on to do.

### 5.1 Basic search

```bash
find .                      # everything under the current directory
find . -name "*.txt"        # by name, with wildcard
find / -name "testfile.txt" # search the whole file system
```

### 5.2 `-type` — restrict what you match

```bash
find . -type f -name "test.txt"    # files only
find . -type d -name "tmp"         # directories only
```

| Value | Matches |
|---|---|
| `f` | regular files |
| `d` | directories |
| `l` | symbolic links |

### 5.3 `-iname` — case-insensitive

Linux is case-sensitive, so `-name "test*"` will **not** match `Test.txt`.

```bash
find . -type f -iname "test*"      # matches both test.txt and Test.txt
```

> **`-iname` is `-name` with the case sensitivity bypassed.**

### 5.4 `-perm` — search by permission

```bash
find / -perm 774 -print       # exactly these permissions
find / ! -perm 077 -print     # NOT these — the ! negates
```

The **`!`** operator inverts any test.

### 5.5 `-user` — search by owner

```bash
find . -user root
```

> Lets you find out **which files were created by a particular user** anywhere in your machine — directly useful in forensics and in the Day 7 orphaned-file scenario.

### 5.6 `-empty` — find empty files

```bash
find /tmp -type f -empty
find /    -type f -empty
```

### 5.7 `-size` — search by size

```bash
find / -size 50M      # files of 50 MB
find / -size +100M    # larger than 100 MB
find / -size -10M     # smaller than 10 MB
```

---

## Part 6 — `-exec`: the most important feature ⭐

### 6.1 The problem

You find 200 files matching a criterion. Now you need to change all their permissions.

**The slow way:** find them, read the output, then `chmod` each one **one by one by one**.

### 6.2 The solution

> **`find` can both locate the files AND fire a further command on every result — in one step instead of two or three.**

```bash
find / -perm 2644 -exec chmod 2777 {} \;
```

### 6.3 The syntax, piece by piece

| Part | Meaning |
|---|---|
| `-exec` | **execute** the following command |
| `chmod 2777` | the command and its arguments |
| `{}` | placeholder — **substituted with each file found** |
| `\;` | **terminator — mandatory** |

> **The `{}` and the `\;` at the end are not optional.** Omitting the terminator produces `find: missing argument to '-exec'` — exactly the error hit live in the lecture.

**Also note:** everything must be **space-separated**, including before `{}` and before `\;`.

### 6.4 More examples

```bash
find . -name "*.tmp" -exec rm {} \;              # delete all matches
find . -type f -perm 777 -exec chmod 644 {} \;   # fix loose permissions
find . -name "*.log" -exec grep "ERROR" {} \;    # search inside matches
find . -user olduser -exec chown newuser {} \;   # reassign ownership
```

> **Why it matters: your time is saved.** This is the difference between a one-line fix and an afternoon of manual work.

---

## Part 7 — Complete cheat sheet

```bash
# ---- Advanced permission bits ----
# SUID = 4 (user), SGID = 2 (group), Sticky = 1 (others)

chmod u+s file      /  chmod 4755 file    # SUID  -> rws------
chmod g+s dir       /  chmod 2775 dir     # SGID  -> ---rws---
chmod +t  dir       /  chmod 1777 dir     # Sticky-> ------rwt

chmod u-s file / chmod g-s dir / chmod -t dir     # remove

ls -ld dir          # inspect a directory's own bits
# lowercase s/t -> bit set WITH execute
# UPPERCASE S/T -> bit set WITHOUT execute

# Enumeration (privilege escalation)
find / -perm -4000 -type f 2>/dev/null    # all SUID binaries
find / -perm -2000 -type f 2>/dev/null    # all SGID binaries

# ---- find ----
find .                          # everything here
find / -name  "file.txt"        # by name
find / -iname "file.txt"        # case-insensitive
find . -type f / -type d / -type l
find / -perm 774 -print
find / ! -perm 077 -print       # negate
find . -user root               # by owner
find . -group project           # by group
find / -type f -empty           # empty files
find / -size 50M / +100M / -10M # by size

# -exec  (note the {} and the mandatory \; )
find / -perm 2644 -exec chmod 2777 {} \;
find . -name "*.tmp" -exec rm {} \;
```

---

## Part 8 — Self-check questions

1. Describe the shared-project scenario. What problem does the sticky bit solve?
2. Which system directory uses the sticky bit by default, and why?
3. Where does `t` appear in the permission string? What is the difference between `t` and `T`?
4. What does SGID do when set on a directory? What tedious task does it eliminate?
5. Where does `s` appear for SGID versus SUID?
6. How can a normal user change their own password when only root can write to `/etc/shadow`?
7. Define SUID in one sentence. Name two SUID binaries mentioned in class.
8. Give the octal digit for each of SUID, SGID and sticky. What is `chmod 7777`?
9. What is the general rule for lowercase versus uppercase in the advanced bits?
10. Why is SUID central to Linux privilege escalation? Write the command to enumerate all SUID binaries.
11. Difference between `-name` and `-iname`, and why it matters on Linux.
12. What does `!` do in a `find` expression?
13. Write commands to find: all directories named `tmp`; all empty files; all files owned by root; all files over 100 MB.
14. Explain each part of `find / -perm 2644 -exec chmod 2777 {} \;`.
15. What does `{}` stand for? What happens if you omit `\;`?
16. Why is `-exec` preferable to finding files and then acting on them separately?

---

## Part 9 — Where the course stands

**File Security is now complete** — standard permissions (Day 9) and advanced permissions (Day 10), plus `find` as the tool that ties permission auditing together.

The recurring thread across Days 7–10: **users and groups → privileges → permissions → the bits that bend those permissions → the tool that audits them all.** Every one of these is a privilege-escalation surface, which is why the trainer treats them as foundational for security work rather than as administration trivia.
