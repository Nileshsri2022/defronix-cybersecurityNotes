# Explanation — Day 6: `cut`, `awk` & Compression

**Lecture:** 006 — Kali Linux Free Capsule Course, Day 6
**Translation:** [`english/006 - Kali Linux Free Capsule Course - Day 6.md`](../english/006%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%206.md)
**Builds on:** Day 5 (`grep`, `sed`)

---

## 0. Course roadmap announced

The trainer checks whether learners are getting bored of back-to-back command sessions and lays out the plan:

| Coming up | Topic |
|---|---|
| Day 7 | **User Management** |
| Then | **Group Management** |
| Then | **File Security & Permissions** |
| After that | **Back to the remaining commands** |

The pause is deliberate — it gives learners time to revise and practise the commands covered so far.

> Rationale repeated throughout: **every command has its own role.** A command is useful up to a point, then hits its **limitations**, and the next command takes over. Day 6 is a live demonstration of exactly that — `cut` hits a wall, and `awk` steps in.

---

## Part 1 — `cut`

> **`cut` is used to cut records using characters and fields, from any file or from any command output.**

### 1.1 Syntax

```bash
cut [options] filename
command | cut [options]
```

### 1.2 The three flags

| Flag | Meaning |
|---|---|
| `-c` | cut by **character** |
| `-f` | cut by **field** |
| `-d` | define the **delimiter** |

### 1.3 Cutting by character — `-c`

```bash
cut -c1-6 file        # characters 1 through 6
cut -c1,3 file        # only characters 1 and 3 (comma = specific picks)
```

| Syntax | Meaning |
|---|---|
| `-c1-6` | a **range** of characters |
| `-c1,3` | **specific** characters |

In the demo, `manish` = 6 characters, so `-c1-6` captures the whole name; `-c1,3` returns just `m` and `n`.

### 1.4 Cutting by field — `-f` needs `-d`

**The critical rule:**

> **Without a delimiter, `cut -f` cannot work.** With no delimiter defined, `cut` treats the *entire line* as one single field — so `-f1` just prints everything.

```bash
cut -f1 file                   # prints the WHOLE line — not what you wanted
cut -d':' -f1 /etc/passwd      # correct: colon-delimited, first field
cut -d':' -f1,3 /etc/passwd    # fields 1 and 3
```

### 1.5 What a delimiter actually is

A **delimiter is a symbol you nominate as the field boundary**. It can be anything — colon, comma, semicolon, `$`, `@`, space.

For `/etc/passwd`, entries look like `name:x:1000:1000::/home/name:/bin/bash`. Declaring `:` as the delimiter means:

```
manish  :  x  :  1001  :  1001  :     :  /home/manish  :  /bin/bash
  f1       f2    f3      f4      f5        f6              f7
```

Note that **empty fields still count** — field 5 above is blank but occupies a position.

### 1.6 Real use case — log extraction

```bash
tail /var/log/messages | cut -d' ' -f1,2
```

Pulls the **month, date, time** and **username** out of log lines — exactly the kind of extract you'd forward to someone who asks for "the latest entries with usernames."

### 1.7 Where `cut` breaks down ⚠

`cut -d' '` splits on a **single space**. Command output such as `df -h` or `ifconfig` is aligned with **variable numbers of spaces**, so:

- Field positions shift line to line
- Runs of spaces create empty fields
- You cannot construct a reliable delimiter

> **This is `cut`'s limitation — and precisely why `awk` exists.**

---

## Part 2 — `awk`

> Described in class as **the most important command in shell scripting.**

### 2.1 The key advantage

**`awk` handles whitespace automatically.** You don't define a space delimiter — it counts and adjusts by itself, regardless of how many spaces separate the columns.

### 2.2 Syntax

```bash
command | awk '{print $1}'
```

Structure: single quotes → curly braces → `print` → `$n` field references.

| Element | Purpose |
|---|---|
| `'...'` | wraps the awk program |
| `{ }` | the action block |
| `print` | output instruction |
| `$1`, `$2`… | field number |
| `$0` | the whole line |

### 2.3 Examples

```bash
df -h | awk '{print $1}'              # first column (filesystem)
df -h | awk '{print $2}'              # second column (size)
df -h | awk '{print $1,$2,$6}'        # filesystem, size, mount point
```

Comparison with `cut` on the same task:

| | `cut` | `awk` |
|---|---|---|
| Whitespace handling | manual, fragile | **automatic** |
| Variable spacing | breaks | works |
| Syntax for field 2 | `-d' ' -f2` (unreliable) | `'{print $2}'` |

### 2.4 Custom field separator — `-F`

When the separator is **not** whitespace, declare it with **capital `-F`**:

```bash
ifconfig | grep inet | awk -F':' '{print $2}'
```

| Flag | Use |
|---|---|
| (none) | split on whitespace — the default |
| `-F':'` | split on a colon |
| `-F','` | split on a comma |

### 2.5 Chaining it all together

```bash
ifconfig | grep inet | awk '{print $2}'
```

This is the three-step admin workflow from Day 4 in action: one command's output narrowed by `grep`, then sliced by `awk`.

### 2.6 `column -t` — tidy output

When cut/awk output arrives merged or misaligned, pipe it through `column`:

```bash
df -h | awk '{print $1,$2,$6}' | column -t
```

| Flag | Meaning |
|---|---|
| `-t` | create a **table** — arrange output in aligned columns |

> **General tip restated:** whenever a command or flag is unclear, run `command --help`. Everything is documented there in detail.

---

## Part 3 — Practice question set in class

> Using `df -h | awk ...`, the output `25%` was produced.
>
> **Task: modify the command so the output is `25` only — without the `%` sign.**
>
> Answers, with a screenshot, to be posted in the video comments.

*(Hint: you already know two tools that can strip a character — one substitutes, one cuts.)*

---

## Part 4 — Compression

### 4.1 Why compress?

Two real motivations given:

1. **Sharing** — a file is too large to send; compress it first.
2. **Archival** — files not used in a long time but **important enough that they cannot be deleted**. Compress them to reclaim space.

### 4.2 `gzip` family — `.gz`

```bash
gzip demo.txt          # compress   -> demo.txt.gz
zcat demo.txt.gz       # view contents WITHOUT decompressing
gunzip demo.txt.gz     # decompress -> demo.txt
```

### 4.3 `bzip2` family — `.bz2`

```bash
bzip2 demo.txt         # compress   -> demo.txt.bz2
bzcat demo.txt.bz2     # view contents
bunzip2 demo.txt.bz2   # decompress
```

`bzip2` generally achieves better compression, though **on a small file you will not see much difference.**

### 4.4 The families do not mix ⚠

| Extension | View | Decompress |
|---|---|---|
| `.gz` | `zcat` | `gunzip` |
| `.bz2` | `bzcat` | `bunzip2` |

> You **cannot** use `gunzip` on a `.bz2` file, or `zcat` on it. Each format has its own matching tool. Plain `cat` works on neither.

### 4.5 The limitation of both

`gzip` and `bzip2` compress **one file at a time**. They cannot bundle 10, 15 or 20 files into a single archive.

**That is what `tar` is for.**

---

## Part 5 — `tar`

### 5.1 The flags

| Flag | Meaning |
|---|---|
| `-c` | **create** an archive |
| `-x` | e**x**tract an archive |
| `-t` | **list** contents |
| `-v` | **verbose** — show progress on screen |
| `-f` | **file** — the archive's name (must come last among these) |
| `-z` | also compress with **gzip** |
| `-j` | also compress with **bzip2** |

### 5.2 Creating archives

```bash
tar -cvf practice.tar demo.txt sample.txt        # plain archive
tar -czvf practice.tar.gz demo.txt test.txt      # archive + gzip
tar -cjvf practice.tar.bz2 demo.txt test.txt     # archive + bzip2
```

> **Ordering rule hit during the demo:** the `z` (or `j`) option must come **before** `f`. Putting it after produces a syntax error.

### 5.3 Listing before extracting

```bash
tar -tvf practice.tar                # list everything inside
tar -tvf practice.tar demo1.txt      # check for one specific file
```

If the file isn't present you get `not found in archive` followed by `error exit delayed from previous errors`.

> Good practice: **list before you extract**, so you know what will land in your directory.

### 5.4 Extracting

```bash
tar -xvf practice.tar
tar -xzvf practice.tar.gz
tar -xjvf practice.tar.bz2
```

### 5.5 Why `tar` is the one to actually memorise

The trainer is emphatic on this point:

> **Even if you are not a Linux admin — if you are a cyber security engineer, this matters just as much.**

- Packages downloaded from repositories or websites arrive in **zipped format**.
- **Manual installation** requires unpacking them first.
- If you can't unzip, you can't install or use the tool.

`gzip` / `gunzip` are worth knowing but don't need memorising — reach for them when you want higher compression for sharing. **`tar` is non-negotiable**, because packing and unpacking packages runs through it.

---

## Part 6 — Complete cheat sheet

```bash
# cut
cut -c1-6 file                  # characters 1-6
cut -c1,3 file                  # characters 1 and 3
cut -d':' -f1 /etc/passwd       # field 1, colon-delimited
cut -d':' -f1,3 /etc/passwd     # fields 1 and 3
tail /var/log/messages | cut -d' ' -f1,2

# awk
df -h | awk '{print $1}'               # field 1
df -h | awk '{print $1,$2,$6}'         # several fields
awk '{print $0}' file                  # whole line
ifconfig | grep inet | awk '{print $2}'
awk -F':' '{print $1}' /etc/passwd     # custom separator

# tidy output
df -h | awk '{print $1,$2,$6}' | column -t

# gzip family (.gz)
gzip file / zcat file.gz / gunzip file.gz

# bzip2 family (.bz2)
bzip2 file / bzcat file.bz2 / bunzip2 file.bz2

# tar
tar -cvf  archive.tar     f1 f2      # create
tar -czvf archive.tar.gz  f1 f2      # create + gzip
tar -cjvf archive.tar.bz2 f1 f2      # create + bzip2
tar -tvf  archive.tar                # list
tar -xvf  archive.tar                # extract
tar -xzvf archive.tar.gz             # extract gzipped

# help
command --help
column --help
```

---

## Part 7 — Self-check questions

1. What are the three main flags of `cut` and what does each do?
2. Difference between `-c1-6` and `-c1,3`.
3. Why does `cut -f1 file` print the entire line? What's missing?
4. Define "delimiter". Name four characters that could serve as one.
5. In `/etc/passwd` with `:` as delimiter, what is field 1? Do empty fields count as fields?
6. Why does `cut` fail on `df -h` and `ifconfig` output?
7. What is `awk`'s main advantage over `cut`?
8. Write the `awk` syntax to print field 2. What does `$0` mean?
9. When do you need `awk -F`, and what case is the flag?
10. What does `column -t` do, and why pipe into it?
11. Two reasons to compress files in a real environment.
12. Match the tool to the format: `.gz` → view? decompress? `.bz2` → view? decompress?
13. Why can't `gunzip` handle a `.bz2` file?
14. What limitation of `gzip`/`bzip2` does `tar` solve?
15. What do `c`, `x`, `t`, `v`, `f`, `z`, `j` mean in `tar`? Which must come before `f`?
16. Write commands to: create a gzipped tar of two files; list its contents; extract it.
17. Why is `tar` described as the most important of the compression commands, even for non-admins?

---

## Part 8 — Coming up next

**Day 7 — User Management:** creating and deleting users, creating groups, adding passwords, and setting password expiry dates.
