# Explanation — Day 5: `sed` Delete/Insert & `grep` In Depth

**Lecture:** 005 — Kali Linux Free Capsule Course, Day 5
**Translation:** [`english/005 - Kali Linux Free Capsule Course - Day 5.md`](../english/005%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%205.md)
**Builds on:** Day 4 (`sed` printing and substitution)

---

## Part 1 — Finishing `sed`

Day 4 covered `sed` printing (`p`) and substitution (`s`). Day 5 completes the command with **delete** and **insert**.

### 1.1 Delete — `d`

```bash
sed '12,15d' sample.txt      # delete lines 12 through 15
sed '5d' sample.txt          # delete line 5
```

### 1.2 Delete everything EXCEPT — `!`

The **exclamation mark means NOT**:

```bash
sed '12!d' sample.txt        # delete every line EXCEPT line 12
```

Read as: *"for all lines that are not 12, delete."* A neat way to isolate a single line.

### 1.3 Insert before a line — `i`

```bash
sed '57i Hello World' sample.txt      # insert a new line BEFORE line 57
```

### 1.4 On-screen vs in-file — still the same rule

| Form | Effect |
|---|---|
| `sed '...' file` | Output changes appear **on screen only**; file untouched |
| `sed -i '...' file` | Changes are written **permanently into the file** |

```bash
sed -i '12,15d' sample.txt            # permanently delete
sed -i '57i Hello World' sample.txt   # permanently insert
```

> Same safety rule as Day 4: **test on screen first, then add `-i`.**

### 1.5 `sed` operations summary

| Action | Letter | Example |
|---|---|---|
| print | `p` | `sed -n '5p' f` |
| delete | `d` | `sed '5d' f` |
| insert before | `i` | `sed '5i text' f` |
| substitute | `s` | `sed 's/a/b/g' f` |
| negate | `!` | `sed '5!d' f` |

---

## Part 2 — Why `grep` exists: the real-world scenario

Before teaching the command, the trainer frames the problem with a **SOC / log monitoring** scenario:

1. You are doing continuous **log monitoring**.
2. An attacker tries to hit your machine. Their **username** or **IP address** appears.
3. You notice something **anomalous** — behaviour different from the normal daily baseline.
4. You note the IP / username and collect information.
5. Confronted, the user **denies** it.
6. The proof is in the **log file** — but log files are enormous and are **updated every second**.

**Searching such a file manually would take hours and still likely fail.** So instead you give a **pattern** and let `grep` find every line containing it, with line numbers. Now the denial is refuted with evidence.

> Context given: most production servers are Linux; attacking, defending and administration all happen there. These text-processing commands are the daily toolkit.

### Why so many different commands?

Each command has a purpose and then hits its **limitations** — the next command exists to fill that gap:

| Command | Its angle |
|---|---|
| `cat` | dump everything |
| `less` / `more` | page through |
| `head` | from the top only |
| `tail` | from the bottom only |
| `sed` | by **line number** |
| `grep` | by **pattern** |

---

## Part 3 — `grep`

> **`grep` is used to search a pattern in any file, or in the output of any command.**

### Syntax

```
grep [options] pattern filename
command | grep [options] pattern
```

### 3.1 Core flags

| Flag | Name | Effect |
|---|---|---|
| `-n` | line number | Show the **line number** of each match |
| `-c` | count | Print the **total number of matching lines** |
| `-i` | ignore case | Case-**insensitive** match |
| `-o` | only matching | Print **only the matched pattern**, not the whole line |
| `-v` | invert | Print every line **except** those matching |
| `-w` | word | **Exact word** match only |
| `-R` / `-r` | recursive | Search **through all files** under a directory |

```bash
grep -n root demo.txt        # with line numbers
grep -c root demo.txt        # how many lines matched
grep -i dns demo.txt         # matches dns, DNS, Dns
grep -o root demo.txt        # prints just "root" per match
grep -v root demo.txt        # everything WITHOUT root
grep -w manish /etc/passwd   # exact word, not substrings
grep -R pattern /etc         # search recursively
```

**Why `-i` matters:** Linux is **case-sensitive**, so `dns` will not match `DNS`. When hunting through logs you usually cannot assume the case of what you're looking for.

**Why `-w` matters:** without it, searching `manish` would also match longer strings containing it. `-w` forces an exact word boundary.

**Use case for `-v`:** analogy given — an attendance register where you want to list everybody *except* the highlighted entries.

**Use case for `-R`:** you've forgotten which file under a directory contains the pattern. `grep -R` walks every file beneath the path.

### 3.2 Context lines — `-B`, `-A`, `-C`

A match alone often isn't enough; you need the surrounding log entries.

| Flag | Shows |
|---|---|
| `-B n` | **n lines Before** the match |
| `-A n` | **n lines After** the match |
| `-C n` | **n lines both sides** (Context) |

```bash
grep -n -B 4 dns demo.txt    # 4 lines before
grep -n -A 4 dns demo.txt    # 4 lines after
grep -n -C 4 dns demo.txt    # 4 lines either side
```

> This is the single most useful `grep` feature in incident investigation — you see what led up to the event and what followed it.

### 3.3 Patterns containing spaces

A bare space splits the arguments, so `grep` reads the second word as a **filename**:

```bash
grep dns name demo.txt        # WRONG: "name" treated as a file
grep "dns name" demo.txt      # RIGHT: quoted pattern
lscpu | grep -i "model name"  # same rule on piped output
```

**Rule: any pattern containing a space must be quoted.**

### 3.4 Anchors — `^` and `$`

| Anchor | Meaning |
|---|---|
| `^pattern` | Lines **starting with** the pattern |
| `pattern$` | Lines **ending with** the pattern |

```bash
grep '^root' demo.txt        # only lines that BEGIN with root
grep 'nologin$' demo.txt     # only lines that END with nologin
```

Demonstrated contrast: plain `grep root` returned 12–13 lines; `grep '^root'` returned far fewer, because it required the match at position one.

### 3.5 `grep` on command output

```bash
lscpu | grep -i "model name"
```

Practical framing: you need a report but don't want to include the entire output. Grep the relevant parameters, redirect to a file, and hand that over as the report.

---

## Part 4 — `egrep` and `fgrep`

### 4.1 The single-pattern limitation

```bash
grep root ftp dns demo.txt
```

This **fails** — `grep` takes `root` as the pattern and treats `ftp`, `dns` and `demo.txt` all as **filenames**.

### 4.2 `egrep` — multiple patterns

> **The only difference between `grep` and `egrep`: `grep` searches a single pattern, `egrep` can search multiple patterns.** All flags, all behaviour, all output formatting are otherwise identical.

```bash
egrep 'root|ftp|dns' demo.txt
```

The **pipe `|` inside the quotes means OR** (alternation) — it is *not* the shell pipe here.

Modern equivalent (integrated into `grep`):

```bash
grep -E 'root|ftp|dns' demo.txt
```

### 4.3 `fgrep` and multiple files

```bash
fgrep root /etc/passwd /etc/group /etc/shadow
```

Searching one pattern across **several files at once**.

> **Note on modern versions:** `egrep` and `fgrep` functionality has been **merged into `grep`** on current systems, so the separate commands are often unnecessary. Use `grep -E` for extended patterns and `grep -F` for fixed strings.

| Command | Modern equivalent | Purpose |
|---|---|---|
| `grep` | `grep` | single pattern |
| `egrep` | `grep -E` | multiple / extended patterns |
| `fgrep` | `grep -F` | fixed strings, no regex |

---

## Part 5 — Practice question set in class

> Pick any pattern you like between **line number 25 and line number 35**, and display it using `grep`.
>
> **Condition: you may not grep the whole file.** You must restrict the search to lines 25–35 only, and search the pattern within that range.

Answers were invited in the video comments.

*Approach hint:* combine the Day 4 line-addressing tool with the Day 5 pattern tool via a pipe — extract the range first, then search within it.

---

## Part 6 — Doubt session recaps

### 6.1 Public vs Private place (revisited from Day 1)

**Two user types in Linux:**

| User | Privileges |
|---|---|
| **root** (admin / super user) | Everything |
| **normal user** | No privileges; only the work assigned to them |

**Every directory has permissions defined on it.** Your own home directory has all three — **read, write, execute** — for you.

| Place | Which paths | Your rights |
|---|---|---|
| **Private place** | Your own home directory | Full — create, delete, execute anything |
| **Public place** | Everything else | Only what the defined permissions allow |

**Read-only** means you may view and read the contents but may **not** modify or change anything. Only the **admin (root)** can change those defined permissions.

**The extended analogy:**

| Real world | Linux |
|---|---|
| Inside your house — do as you like | Your home directory |
| Step outside → **society's rules** | Public directories |
| On the road → **traffic rules** | System directories with fixed permissions |
| Rules are **forced on you**; you can't rewrite them | Permissions set by root |
| The **government** sets and changes the rules | **root** is the admin |

> The payoff: once this mindset is clear — where you can work and where you can't — you will never hit a confusing permission problem again, because you'll know in advance which directory allows what.

### 6.2 The learning method the trainer recommends

> **Compare every computing concept with things in the world around you.**

If someone is giving you **conceptual knowledge** and you **correlate** it with ordinary everyday experience, the subject becomes genuinely interesting — and interest is what sustains learning. Without that correlation you get bored and abandon it.

### 6.3 stdin / stdout / stderr (revisited from Days 3–4)

**A file descriptor** is the kernel's **table for tracking open files**. It also helps a process know which file it is accessing/opening. The process itself cannot modify the table — only the kernel can.

**The first three entries exist in every process:**

| Stream | Descriptor | Default | Why it exists |
|---|---|---|---|
| **stdin** | 0 | **keyboard** | You type a command; input comes from the keyboard |
| **stdout** | 1 | **screen** | You wait for a result — how else would you know the work happened? |
| **stderr** | 2 | **screen/terminal** | If an error occurs it must be **visible**; otherwise you sit waiting for hours for something that already failed |

**The reasoning for stderr is the memorable part:** if an error occurred and was never shown, you'd have no idea — you'd keep waiting for output that is never coming. So errors get their own stream, also defaulting to the screen.

### Redirection in practice

| Goal | How |
|---|---|
| Take input from a file instead of the keyboard | `<` |
| Make one command's output another's input | `\|` |
| Save output to a file instead of the screen | `>` |
| Redirect **errors** | `2>` |

> **Why you must write `2>` but not `0<` or `1>`:** descriptors **0 and 1 are the defaults** attached to `<` and `>` automatically. Descriptor **2 is not the default**, so it must be stated explicitly.

### Study advice given

Revise the file descriptor concept once or twice, then rewatch Day 3 (Nitesh sir's session) — **skip the first part** and focus on the command explanations of input/output redirection. Correlating the two makes both click.

The trainer notes that even final-year B.Tech students often have no exposure to file descriptors; the available material is scarce and confusing, because going deep requires real operating-system architecture knowledge. For now, the basic concept correlated with commands and scripting is sufficient.

---

## Part 7 — Complete cheat sheet

```bash
# sed — delete and insert
sed '12,15d' file            # delete range
sed '5d' file                # delete one line
sed '12!d' file              # delete all EXCEPT line 12
sed '57i text' file          # insert before line 57
sed -i '...' file            # apply permanently

# grep — core
grep pattern file
grep -n pattern file         # line numbers
grep -c pattern file         # count matching lines
grep -i pattern file         # ignore case
grep -o pattern file         # only the match
grep -v pattern file         # invert (exclude)
grep -w pattern file         # exact word
grep -R pattern /path        # recursive

# grep — context
grep -B 4 pattern file       # 4 before
grep -A 4 pattern file       # 4 after
grep -C 4 pattern file       # 4 both sides

# grep — anchors and spaces
grep '^root' file            # starts with
grep 'nologin$' file         # ends with
grep "dns name" file         # pattern with a space (quote it)

# grep — on command output
lscpu | grep -i "model name"

# multiple patterns / files
egrep 'root|ftp|dns' file    # OR
grep -E 'root|ftp|dns' file  # modern equivalent
fgrep root /etc/passwd /etc/group
grep -F root file1 file2     # modern equivalent
```

---

## Part 8 — Self-check questions

1. Write `sed` commands to: delete lines 12–15; delete everything except line 12; insert a line before line 57.
2. What does `!` do in a `sed` address?
3. Which flag makes `sed` changes permanent, and what should you always do first?
4. Describe the log-monitoring scenario that motivates `grep`. Why is manual searching impractical?
5. Why does each text command (`cat`, `head`, `tail`, `sed`, `grep`) exist separately?
6. Give the flag for: line numbers, count, ignore case, only-match, invert, exact word, recursive.
7. Why is `-i` essential when hunting in logs?
8. Difference between `-B`, `-A` and `-C`. Why is context so valuable in an investigation?
9. Why does `grep dns name file` fail, and how do you fix it?
10. What do `^` and `$` do? Write a command for lines ending in `nologin`.
11. Why does `grep root ftp dns demo.txt` not search three patterns?
12. State the one difference between `grep` and `egrep`. What is the modern equivalent of each of `grep`, `egrep`, `fgrep`?
13. What does `|` mean *inside* an `egrep` pattern versus *outside* it in the shell?
14. Define private place and public place, and map each to its real-world analogy.
15. What does read-only permission allow, and who can change it?
16. Name the three standard streams with their descriptors and defaults.
17. Why must errors have their own stream? What goes wrong without one?
18. Why do you write `2>` but never need `1>` or `0<`?

---

## Part 9 — Coming up next

The **`cut`** command, which was planned for this session but deferred. The stated goal of this whole command series: given a file of hundreds of thousands of lines, be able to extract exactly the fields, columns and keywords you need **in seconds** rather than opening an editor and cutting and pasting by hand.
