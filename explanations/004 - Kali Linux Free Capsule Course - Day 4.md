# Explanation — Day 4: File Descriptors Deep Dive & Text-Processing Commands

**Lecture:** 004 — Kali Linux Free Capsule Course, Day 4
**Translation:** [`english/004 - Kali Linux Free Capsule Course - Day 4.md`](../english/004%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%204.md)
**Builds on:** Day 3 (I/O redirection, stdin/stdout/stderr)

---

## Part 1 — File descriptors, properly explained

Day 3 introduced descriptors 0/1/2. Day 4 opens with a deliberate 15-minute recap explaining **why they exist at all**.

### 1.1 The chain: command → program → process → open files

1. Every command you type (`wc`, `w`, `cd`, `ls`…) is a **program** — an executable binary living in `/bin` (covered on Day 2).
2. Running that program **creates a process**.
3. That process internally uses many **libraries** and files.
4. **In Linux everything is a file** — so all those libraries count as files, held in the **open** state.

### 1.2 Why the kernel must track open files

> **Until the kernel can monitor something, it cannot control it.**

The kernel is the most powerful component of the OS and is responsible for managing everything. An entity that manages everything but has no visibility into what is happening inside its own system is in the worst possible position. So the kernel needs a mechanism to **track every open file** — and that mechanism is the **file descriptor**.

*(Analogy used in class: a head of household needs to know who is coming in, who is going out, and what everyone is doing.)*

### 1.3 The three kernel tables

| Table | What it holds |
|---|---|
| **File descriptor table** | Per-process. Maps small integers (0, 1, 2, …) to entries in the global file table. **Hidden** — only the kernel may update it. |
| **Global file table** | System-wide. Holds the reference/address pointing onward to the inode table. |
| **Inode table** | Holds each file's **metadata**: size, timestamps, location, plus a reference to where the file physically lives on the file system. |

**The lookup chain:**

```
process
   │
   ▼
file descriptor (a positive integer)
   │   ← per-process, hidden, kernel-only
   ▼
global file table entry
   │   ← system-wide
   ▼
inode  →  metadata (size, timestamps, permissions, location)
   │
   ▼
actual file on the file system
```

> **Critical point:** a process **cannot** modify its own file descriptor table. Any change must go through the kernel. This is a security boundary, not an inconvenience.

### 1.4 What a file descriptor gives a program

1. **Where the file is stored** on the file system — the address to access it from.
2. **Whether the process may access it** — the specific permissions.

### 1.5 The inode number

Every file — default or user-created, empty or full — is assigned a **unique inode number**. That number, not the filename, is how the system actually identifies the file.

### 1.6 Recommended further reading

The trainer is explicit that this is a surface-level treatment. To go deeper, study **Operating System Architecture**: how processes are created and scheduled, how they are loaded into RAM, how the CPU schedules them.

### 1.7 Tying back to redirection

By default:

| Stream | Descriptor | Default device |
|---|---|---|
| stdin | 0 | **keyboard** |
| stdout | 1 | **screen** |
| stderr | 2 | **screen** |

**Redirection is simply pointing a descriptor somewhere else** — feed a file into stdin instead of the keyboard; send stdout/stderr into a file instead of the screen. That is the entirety of Day 3's topic, now explained from the kernel's side.

---

## Part 2 — Viewing file contents

The problem with `cat`: it dumps the **whole file** at once. For a thousand-line file that is unusable.

### 2.1 `head` — from the top

```bash
head /etc/passwd          # first 10 lines (default)
head -5 /etc/passwd       # first 5 lines
head -15 /etc/passwd      # first 15 lines
command | head -15        # works on piped output too
```

### 2.2 `tail` — from the bottom

```bash
tail /etc/passwd          # last 10 lines (default)
tail -5 /etc/passwd       # last 5 lines
```

| Command | Reads from | Default |
|---|---|---|
| `head` | top | 10 lines |
| `tail` | bottom | 10 lines |

### 2.3 `less` — page-by-page viewer

```bash
less demo.txt
```

Loads the file **page by page** instead of dumping it. Essential for large log files.

**Navigation keys:**

| Key | Action |
|---|---|
| **↓ / ↑** | Move **line by line** |
| **Page Down** | Move **page by page** downward |
| **Page Up** | Move **page by page** upward |
| **End** | Jump to the **end** of the file |
| **Home** | Jump back to the **first** line |

**Searching:**

| Key | Action |
|---|---|
| `/pattern` | Search **forward** (top → bottom). Matches are **highlighted**. |
| `?pattern` | Search **backward** (bottom → top) |
| `n` | Jump to the **next** match |
| `N` (capital) | Jump to the **previous** match |

**Quitting:**

| Key | Action |
|---|---|
| `q` | **Quit** `less` |

> Lowercase `q`, no Shift, Caps Lock off. Do **not** close the terminal to escape `less` — press `q`.

A related command, **`more`**, behaves similarly and was left as self-practice.

### 2.4 `tac` — reverse of `cat`

```bash
tac /etc/passwd
```

Prints the file **bottom to top** — the lines in reverse order. (`tac` is `cat` spelled backwards.)

---

## Part 3 — `wc` (word count)

```bash
wc /etc/passwd
```

Default output is three numbers:

| Position | Meaning |
|---|---|
| 1st | number of **lines** |
| 2nd | number of **words** |
| 3rd | number of **characters/bytes** |

**Flags:**

| Flag | Shows only |
|---|---|
| `-l` | lines |
| `-w` | words |
| `-c` | characters |

**Syntax:** `wc [options] filename`

### Using `wc` on command output

`wc` operates on files, not on other commands directly. To count the output of a command, **pipe it**:

```bash
lscpu | wc -l          # count lines of lscpu output
ls | wc -l             # count entries in a directory
```

This is the Day 3 pipe concept being put to work.

---

## Part 4 — The three-step Linux admin workflow

A genuinely useful mental model given in this session:

| Step | Approach |
|---|---|
| **1** | Try to get the result with the **command** alone. |
| **2** | If not, try the command's **flags/options**. |
| **3** | If still not, **join commands with pipes** (`\|`) and build the output from pieces. |

Reach for complexity only when the simpler level fails.

---

## Part 5 — `sed`, the Stream Editor

Introduced as the first in a planned series of high-value commands: **`sed`, `cut`, `locate`** and more. The pitch: master these and you can extract, filter and reshape any output quickly.

### 5.1 Syntax

```
sed [options] 'action' filename
```

The action goes in **single quotes**.

### 5.2 Key property: `sed` works on LINE NUMBERS

Unlike `head`/`tail`, which think in terms of "from the top" or "from the bottom", **`sed` has no notion of direction — it addresses lines by number.**

Helpful companion for seeing line numbers:

```bash
cat -n /etc/passwd        # print the file WITH line numbers
```

### 5.3 Printing specific lines

The `-n` flag suppresses `sed`'s default behaviour of echoing every line. **Without `-n`, `sed 'Np'` prints the whole file and duplicates line N.**

```bash
sed -n '1p' /etc/passwd        # only line 1
sed -n '1p;5p' /etc/passwd     # lines 1 and 5   (; = separator)
sed -n '1,7p' /etc/passwd      # lines 1 through 7  (, = range)
sed -n '1p;$p' /etc/passwd     # first line and last line  ($ = last)
```

| Symbol | Meaning |
|---|---|
| `p` | print |
| `;` | separator between actions |
| `,` | range (from, to) |
| `$` | the last line |
| `-n` | suppress automatic printing |

### 5.4 Substitution — search and replace

```bash
sed 's/root/sachin/' /etc/passwd
```

Reads as: **s**ubstitute `root` with `sachin`. By default this replaces **only the first occurrence on each line**.

| Form | Effect |
|---|---|
| `s/old/new/` | first occurrence per line |
| `s/old/new/g` | **global** — every occurrence |
| `s/old/new/2` | only the **2nd** occurrence |
| `s/old/new/2g` | from the **2nd occurrence onward**, all of them |
| `1s/old/new/` | only on **line 1** |
| `1,7s/old/new/` | only within **lines 1–7** |

### 5.5 Case sensitivity

**Linux is case-sensitive**, so `nologin` and `NOLOGIN` are different strings — a substitution for one will not touch the other.

To make the match **case-insensitive**, add the `i` flag:

```bash
sed 's/nologin/sachin/gi' /etc/passwd
```

| Flag | Meaning |
|---|---|
| `g` | global (all occurrences) |
| `i` | ignore case |
| `gi` | both |

### 5.6 Multiple substitutions in one command

```bash
sed 's/nologin/network/g; s/root/sachin/g' /etc/passwd
```

Separate the actions with a **semicolon**. The `-e` flag is an alternative way to chain expressions.

### 5.7 `-i` — editing the file in place

By default **`sed` only changes the output on screen; the original file is untouched.** To modify the file permanently:

```bash
sed -i 's/nologin/petrol/g' sample.txt
```

### ⚠ Safety rule stated in class

> **Always run your `sed` task on screen first and check the result. Never go straight to `-i` on the real file.**

In the demo the trainer deliberately worked on a **copy** (`cp` to `sample.txt`) before using `-i`, precisely because `/etc/passwd` was the original. Follow that pattern.

---

## Part 6 — Homework question set in class

> Using the `/etc/passwd`-style file shown on screen, produce an output containing **line numbers 1–5, 11–15, and up to 25**, with a further selection at line 50.

Answers were invited in the video comments. A workable approach:

```bash
sed -n '1,5p;11,15p;25p;50p' filename
```

---

## Part 7 — Complete cheat sheet

```bash
# Viewing
head file              # first 10 lines
head -5 file           # first 5
tail file              # last 10
tail -5 file           # last 5
cmd | head -15         # on piped output
tac file               # reversed, bottom to top
cat -n file            # with line numbers

# Paging
less file              # page-by-page
  ↓ ↑          line by line
  PgDn PgUp    page by page
  Home / End   first / last line
  /pattern     search forward
  ?pattern     search backward
  n / N        next / previous match
  q            quit

# Counting
wc file                # lines, words, characters
wc -l file             # lines only
wc -w file             # words only
wc -c file             # characters only
ls | wc -l             # count via pipe

# sed — stream editor
sed -n '1p' file               # print line 1
sed -n '1p;5p' file            # lines 1 and 5
sed -n '1,7p' file             # lines 1-7
sed -n '1p;$p' file            # first and last
sed 's/old/new/' file          # first match per line
sed 's/old/new/g' file         # all matches
sed 's/old/new/2' file         # 2nd occurrence only
sed 's/old/new/2g' file        # 2nd onward
sed '1s/old/new/' file         # only line 1
sed 's/old/new/gi' file        # case-insensitive
sed 's/a/b/g; s/c/d/g' file    # multiple actions
sed -i 's/old/new/g' file      # EDIT THE FILE (careful!)
```

---

## Part 8 — Self-check questions

1. Trace the path from typing a command to an open file being tracked by the kernel.
2. Why must the kernel monitor open files? State the rule in one sentence.
3. Name the three kernel tables and what each holds.
4. Why can a process not edit its own file descriptor table?
5. What is an inode number and what is unique about it?
6. Which metadata lives in the inode table?
7. Default line counts for `head` and `tail`, and how to change them.
8. In `less`: how do you search forward, search backward, go to the next match, jump to the end, and quit?
9. What does `tac` do?
10. Interpret the three numbers `wc` prints. Which flag gives only words?
11. Why does `wc` need a pipe to count a command's output?
12. State the three-step Linux admin workflow.
13. Why does `sed -n` matter when printing a line?
14. Write `sed` commands for: line 3 only; lines 2–8; first and last line.
15. Difference between `s/a/b/`, `s/a/b/g`, `s/a/b/3`, and `s/a/b/3g`.
16. How do you make a `sed` substitution case-insensitive, and why is it needed?
17. What does `-i` do, and what is the safety rule around it?

---

## Part 9 — Coming up next

The announced **command series** continues with **`cut`**, **`locate`** and further text-processing tools — the toolkit for slicing any command output into exactly the fields you need.
