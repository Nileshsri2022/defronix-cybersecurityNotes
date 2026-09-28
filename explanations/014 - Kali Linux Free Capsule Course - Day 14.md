# Explanation — Day 14: `history`, Root Password Recovery, `sort` & `uniq`

**Lecture:** 014 — Kali Linux Free Capsule Course, Day 14
**Translation:** [`english/014 - Kali Linux Free Capsule Course - Day 14.md`](../english/014%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2014.md)
**Note:** Final content session of the Kali Linux capsule course. The **OSINT course** begins next.

---

## Part 1 — The `history` command

> Every command you run is saved. In the background there is a **history file** (`~/.bash_history`) where all of them are stored.

### 1.1 Recalling commands

| Method | Action |
|---|---|
| **↑ / ↓ arrows** | step back and forward through previous commands |
| **`!!`** | re-run the **immediately previous** command |
| **`!string`** | re-run the most recent command **starting with** that string |
| **`!number`** | re-run history entry **by its number** |
| **`Ctrl+R`** | **reverse interactive search** through history |

```bash
!!              # repeat the last command
!to             # repeat the last command starting with "to" (e.g. touch file77)
!1634           # run history entry number 1634
```

**`Ctrl+R`** opens `(reverse-i-search)`. Type any fragment and it finds the matching command; press Enter to run it.

> **`!string` searches your history file.** If you have never run a command starting with that string, nothing is found.

### 1.2 Viewing history

```bash
history          # everything
history 10       # last 10 entries
history 50       # last 50 entries
```

---

## Part 2 — The three history environment variables

| Variable | Controls | Default |
|---|---|---|
| **`HISTFILE`** | **name and location** of the history file | `~/.bash_history` |
| **`HISTSIZE`** | how many commands held **in memory** | **1000** |
| **`HISTFILESIZE`** | how many commands kept **in the file** | 1000 |

```bash
echo $HISTSIZE          # 1000
HISTSIZE=5000           # temporary
```

> **After the limit is reached it starts to overwrite** the oldest entries.

**To make it permanent**, edit `~/.bashrc` and raise `HISTSIZE` there — the same three-level persistence model from Day 13.

---

## Part 3 — ⚠ When history is actually written

> **Today's history is only saved into the history file when you LOG OUT.**
>
> What the `history` command shows you is the **in-memory** history.

**Why this matters:** the file on disk lags behind the live session. Two consequences worth knowing:

- Kill a terminal abruptly and that session's history may never be written.
- In forensics, `~/.bash_history` shows **completed sessions**, not what is happening right now.

---

## Part 4 — Keeping a command out of history

```bash
 date         # note the LEADING SPACE — not recorded
history       # "date" does not appear
```

> **Put a space before a command and it will not go into your history file.**

This works when `HISTCONTROL` includes `ignorespace` (common default). The trainer is honest that it isn't universal: *"there's no guarantee that it will work"* on every system.

**Security relevance:** this is also how someone hides activity — worth knowing from both sides.

---

## Part 5 — Clearing history

```bash
history -c        # clear the entire history
history -d 17     # delete entry number 17
```

> ⚠ **On the trainer's Kali machine `-c` did not work.** His explanation: *"on the latest Kali machines it's possible the `-c` option has been removed… it's possible this has been modified due to security reasons."*
>
> These options **do work on other UNIX systems** — Fedora, Red Hat, CentOS.

---

## Part 6 — ⭐ Resetting a forgotten root password

The promised demonstration, outstanding since Day 8.

### 6.1 The scenario

You power on the machine, reach the login screen, and **you do not know the root password.** The `passwd` command is useless — it requires you to be logged in already.

### 6.2 ⚠ Distribution warning — read first

> **This procedure is for Debian-based systems only — Kali, Debian, Ubuntu.**
>
> **Do NOT try it on Fedora / Red Hat / CentOS.** Those require additional steps because **the security policy works differently**. Without them you get an error and **your machine may not boot at all.**

### 6.3 The procedure

| Step | Action |
|---|---|
| **1** | Power on the machine |
| **2** | At the **GRUB menu**, press **`e`** to edit |
| **3** | Find the line beginning with **`linux`** |
| **4** | Move to the **very end** of that line |
| **5** | **Delete** `ro`, `quiet` and `splash`; replace with **`rw init=/bin/bash`** |
| **6** | Press **`Ctrl+X`** to boot |

```
# before:
linux /boot/vmlinuz-... root=UUID=... ro quiet splash

# after:
linux /boot/vmlinuz-... root=UUID=... rw init=/bin/bash
```

**What this does:** `init=/bin/bash` tells the kernel to launch a **bash shell as PID 1** instead of the normal init system — so you land in a root shell with no login prompt. `rw` mounts the filesystem writable so changes can be saved.

### 6.4 After booting

You land at a prompt showing **`/`** — you are in the **root partition**, not root's home directory.

**Step 7 — Verify the filesystem is writable:**

```bash
mount
```

Check the entry for `/`. It must **not** say `ro`.

> **It should not be READ ONLY.** If you find `ro` there, fix it:

```bash
mount -o remount,rw /
```

**Step 8 — Change the password:**

```bash
passwd
# password updated successfully
```

**Step 9 — Reboot:**

```bash
exec /sbin/init
```

> *"The binary file for rebooting the machine — I am getting that executed."*

The machine reboots normally and you log in with the new password.

### 6.5 ⚠ The security lesson

This procedure requires only **physical access to the machine**. It takes about two minutes and needs no prior credentials.

**This is exactly why Day 8 covered boot-time protections:**

| Defence | Prevents |
|---|---|
| **GRUB password** | editing the boot parameters at step 2 |
| **BIOS/UEFI password** | changing boot order to bypass GRUB |
| **Full disk encryption** | reading the filesystem at all |
| **Physical security** | reaching the machine in the first place |

> Without these, **anyone with physical access owns the machine.** Knowing the attack is what justifies the defence.

---

## Part 7 — `sort`

```bash
sort filename.txt           # alphabetical sort
sort -k1 filename.txt       # sort by column 1
sort -k2 filename.txt       # sort by column 2
```

| Flag | Effect |
|---|---|
| (none) | sort alphabetically |
| `-k1`, `-k2` | sort by a specific **column** |
| `-r` | reverse |
| `-n` | numeric sort |
| `-u` | sort and remove duplicates in one step |

---

## Part 8 — `uniq`

> **`uniq` deletes DUPLICATE entries.**

### ⚠ The prerequisite everyone forgets

> **`uniq` only removes ADJACENT duplicates.** You must **`sort` first**, otherwise duplicates scattered through the file are never noticed.

### The one-liner

```bash
cat tmp.txt | sort | uniq
```

Breaking it down — a direct application of Day 3's redirection material:

1. `cat tmp.txt` produces the file's contents
2. `|` makes that the **input** of `sort`
3. `sort` groups identical lines together
4. `|` makes *that* the **input** of `uniq`
5. `uniq` removes the now-adjacent duplicates

> **This works ON SCREEN only** — redirect to a file if you want to keep the result:

```bash
cat tmp.txt | sort | uniq > cleaned.txt
sort -u tmp.txt > cleaned.txt          # shorter equivalent
```

---

## Part 9 — Pipe recap

A learner asked what `|` actually does. The answer, restated:

> **The pipe takes the OUTPUT of the first command and makes it the INPUT of the second.** "Piping" is exactly that — joining.

**Why it was needed here:** `sort` expects a **filename**. In `cat tmp.txt | sort`, no filename is given — so `sort` takes its input **from the pipe** instead.

> Learners who find this unclear were directed back to **Day 3 and Day 4** on input/output redirection.

---

## Part 10 — Complete cheat sheet

```bash
# ---- history ----
history                 # all entries
history 10              # last 10
!!                      # repeat previous command
!string                 # repeat last command starting with "string"
!1634                   # run entry number 1634
Ctrl+R                  # reverse interactive search
history -c              # clear all
history -d 17           # delete entry 17
 command                # LEADING SPACE = not saved to history

echo $HISTSIZE          # in-memory limit (default 1000)
echo $HISTFILE          # ~/.bash_history
HISTSIZE=5000           # temporary; put in ~/.bashrc to persist

# ---- root password reset (Debian/Kali/Ubuntu ONLY) ----
# 1. power on -> GRUB menu -> press 'e'
# 2. find the "linux" line, go to the end
# 3. delete:  ro quiet splash
# 4. add:     rw init=/bin/bash
# 5. Ctrl+X to boot
mount                          # verify / is NOT mounted 'ro'
mount -o remount,rw /          # only if it is
passwd                         # set the new password
exec /sbin/init                # reboot

# ---- sort & uniq ----
sort file.txt
sort -k2 file.txt              # by column 2
sort -r / -n / -u
cat file.txt | sort | uniq     # remove duplicates
sort -u file.txt               # shorter equivalent
```

---

## Part 11 — Self-check questions

1. Where is command history stored? What is the default `HISTSIZE`?
2. Give four ways to recall a previous command without retyping it.
3. What does `!to` do? What happens if you've never run a command starting with `to`?
4. What does `Ctrl+R` open?
5. Name the three history environment variables and what each controls.
6. When is history actually written to the file? Why does that matter in forensics?
7. How do you stop a single command from being recorded? Why is this relevant to security from both sides?
8. Which distributions is the GRUB password-reset procedure safe on? What happens if you try it elsewhere?
9. List the six GRUB steps. What exactly do you replace at the end of the `linux` line?
10. What does `init=/bin/bash` do, and why is `rw` needed?
11. After booting, which directory are you in? What must you verify with `mount`, and what's the fix?
12. Why do you run `exec /sbin/init` rather than just rebooting?
13. What prerequisite does the entire procedure have? Name four defences against it.
14. What does `sort -k2` do?
15. Why must you `sort` before `uniq`? What happens if you don't?
16. Explain `cat file | sort | uniq` step by step. Give the shorter equivalent.
17. Restate what the pipe symbol does in one sentence.

---

## Part 12 — What comes next

### The OSINT course

> **Starting tomorrow at 6 PM: Open Source Intelligence.**

| Aspect | Detail |
|---|---|
| **What it is** | *"Information gathering's part itself"* — OSINT = **Open Source Intelligence** |
| **Prerequisites** | **None.** *"Technical, non-technical, IT, non-IT — anyone can come, because this is general knowledge; it is a general-purpose course."* |
| **Length** | *"Comfortably a 10 to 12 hour course"* |

> The trainer's view: *"Every single person should know how to do Open Source Intelligence, because if ever someone gets stuck in some trouble, they can get out of such a situation."*

This is why transcripts 015 and 017–020 belong to a different series interleaved with the remaining Kali sessions.

### Possible future content

**Bash scripting** and **Python** were floated as possibilities, explicitly conditional on channel engagement.

### Advice for newcomers

> *"Start watching our videos from the beginning. You will get each and every step in detail. Watch one video daily; if you have more time, watch two."*
