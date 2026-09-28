# Explanation — Day 3: Input/Output Redirection & File Descriptors

**Lecture:** 003 — Kali Linux Free Capsule Course, Day 3
**Trainer:** Nitesh Singh (Founder, Defronix)
**Translation:** [`english/003 - Kali Linux Free Capsule Course - Day 3.md`](../english/003%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%203.md)

---

## 1. The core idea in one line

Every command, by default, **reads input from the keyboard** and **writes output to the screen**. Redirection means changing either of those endpoints — sending output into a file instead of the screen, or feeding a file into a command instead of typing.

That's it. Everything else in this lecture is the machinery that makes it work.

**Where it matters in practice:** error logging, system logging, capturing program errors, saving command output for later analysis — bread-and-butter work in security and administration.

---

## 2. First demonstration

```bash
date                    # prints to screen (stdout)
date > date.txt         # prints nothing; output goes into the file
cat date.txt            # read the file back — the date is in there
```

Then:

```bash
cal > date.txt          # the date output VANISHES — replaced by the calendar
cal > date.txt
date >> date.txt        # now BOTH are in the file
```

| Operator | Name | Behaviour |
|---|---|---|
| `>` | **Overwrite / replace** | Wipes existing content, writes fresh |
| `>>` | **Append** | Keeps existing content, adds to the end |

> ⚠ The single `>` silently destroys whatever was in the file. This is the #1 accidental data-loss operator in shell work.

---

## 3. File descriptors

### Definition

> A **file descriptor** is a **unique, non-negative integer** that identifies an **open file** inside the OS.

An "open file" = any file currently in use by a process.

### The key Linux principle

**In Linux, everything is a file** — including directories, and including the input/output streams themselves. `stdin`, `stdout` and `stderr` are **special files**.

### What the kernel does

When a file is opened, the kernel:

1. Creates an **entry in the global file table**
2. Provides the **location of that entry**
3. Returns that reference (the descriptor number) to the process

### Cross-platform note

| OS | Name for the same idea |
|---|---|
| UNIX (original) | file descriptor |
| Linux | file descriptor |
| Microsoft Windows | **file handle** |

---

## 4. The three standard streams

| Stream | Special file | Descriptor | Default source/target | Redirect form |
|---|---|---|---|---|
| **stdin** | `/dev/stdin` | **0** | keyboard | `0<` or `<` |
| **stdout** | `/dev/stdout` | **1** | screen | `1>` or `>` |
| **stderr** | `/dev/stderr` | **2** | screen | `2>` |

Plus a fourth special file:

| Special file | Nickname | Behaviour |
|---|---|---|
| **`/dev/null`** | the **black hole** | Anything sent into it disappears permanently |

**These files genuinely exist** — you can browse to `/dev` in the file manager and see `stdin`, `stdout`, `stderr` and `null` sitting there. They contain nothing, but they do enormous work.

> **Memory hook: 0 in, 1 out, 2 error.**

---

## 5. The hidden truth about ordinary commands

This is the section the trainer says is normally never taught:

```bash
cat file.txt            # what you're told
cat 0< file.txt         # what is actually happening
cat < file.txt          # the "most standard" explicit form
```

`cat file.txt` isn't magic — you are feeding `file.txt` into `cat`'s **stdin**, and `cat`'s job is to print whatever arrives on its input.

Similarly, these are all equivalent:

```bash
ls > out.txt
ls 1> out.txt
ls > /dev/stdout        # explicit, prints to screen
```

Understanding this reframes the whole shell: commands are just **filters between three streams**.

---

## 6. Four ways to create a file

| Method | Command | Note |
|---|---|---|
| `touch` | `touch a` | Empty file |
| `vim` | `vim b` | Opens an editor |
| GUI | right-click → new file | Graphical |
| `cat` + redirect | `cat > d` | Type content, **Ctrl+D** to finish |

The `cat > d` form is just redirection again — you're giving output into a new file.

---

## 7. The pipe `|`

```bash
ls | grep D
```

> **A pipe makes the first command's OUTPUT become the second command's INPUT.**

`grep` searches for a string / regular expression. In the example, `ls`'s output is piped into `grep`, which filters it down to only entries starting with `D` (Desktop, Documents, Downloads).

**Redirection vs pipe:**
- `>` sends output to a **file**
- `|` sends output to **another command**

---

## 8. The `tee` command

**Problem:** `>` sends output to a file, but then you can't see it on screen. What if you want **both**?

**Solution:** `tee`.

```bash
ls | tee test.txt        # prints on screen AND writes to test.txt
ls | tee -a test.txt     # same, but APPENDS instead of overwriting
```

| Flag | Effect |
|---|---|
| (none) | overwrite the file |
| `-a` | append to the file |

Named after a **T-pipe fitting** — the stream arrives and splits two ways.

---

## 9. Suppressing errors with `/dev/null`

```bash
cat hello
# cat: hello: No such file or directory     ← error on stderr
```

To make that error disappear:

```bash
cat hello 2> /dev/null
```

Read it as: *take file descriptor 2 (stderr) and dump it into the black hole.*

You can also **save** errors rather than discard them:

```bash
cat hello 2> error.txt     # error text is written into error.txt
```

---

## 10. Redirecting both stdout and stderr

```bash
./script.sh &> output.txt       # both streams into one file
./script.sh > out.txt 2>&1      # the classic equivalent form
```

`2>&1` means "send descriptor 2 to wherever descriptor 1 is currently pointing." The `&` before the `1` says *"1 is a file descriptor, not a file named 1."*

---

## 11. Full worked demo — the Bash script

A small script was written in `vim` to demonstrate output *and* errors:

```bash
#!/bin/bash
for i in a b c d e
do
    echo "creating directory /tmp/$i"
    mkdir /tmp/$i
done
```

Points made while building it:

- `#!/bin/bash` — the **shebang**, declares the interpreter.
- `$i` — the `$` **denotes a variable**; without it, `i` is just a letter.
- A **`for` loop with a fixed list** terminates on its own — unlike `while true`, which "will keep going and going and won't stop."
- Full paths matter: `mkdir /tmp/$i`, not `mkdir $i`.
- Save and exit vim with `:wq`.

### Run 1 — permission denied

```bash
./s.sh
# bash: ./s.sh: Permission denied
```

Even root cannot execute a file lacking the execute bit. Checking with `ls -l`:

```
-rw-r--r--   1 root root ...  s.sh
│ └┬┘└┬┘└┬┘
│  u   g   o
└─ file type: '-' = file, 'd' = directory
```

| Position | Who | Permissions in demo |
|---|---|---|
| chars 2–4 | **user** | `rw-` — read, write, **no execute** |
| chars 5–7 | **group** | `r--` — read only |
| chars 8–10 | **other** | `r--` — read only |

The three permissions are **read (r), write (w), execute (x)**, for **user, group, other**.

Fix:

```bash
chmod +x s.sh      # grant execute
./s.sh
# creating directory /tmp/a ... /tmp/e
```

Verified with `cd /tmp && ls` — directories `a` through `e` exist.

### Run 2 — errors appear

Running it a second time produces `mkdir: cannot create directory: File exists` for every iteration, because the directories already exist. This gives real errors to redirect.

### Run 3 — capture everything

```bash
./s.sh &> defronix.txt
```

Screen is now silent — both the echo output and the `mkdir` errors were captured into the file. The trainer's own mistake during the demo is instructive: the redirection must come **after** the command, attached to it.

Alternatively, to discard the errors entirely while keeping normal output on screen:

```bash
./s.sh 2> /dev/null
```

---

## 12. Complete cheat sheet

```bash
# Output redirection
cmd > file            # overwrite
cmd >> file           # append
cmd 1> file           # explicit stdout

# Input redirection
cmd < file            # feed file as stdin
cmd 0< file           # explicit stdin
cat < file.txt        # the "standard" way to read a file

# Error redirection
cmd 2> file           # errors to a file
cmd 2> /dev/null      # discard errors

# Both streams
cmd &> file           # both to one file
cmd > file 2>&1       # classic equivalent

# Pipes and tee
cmd1 | cmd2           # output of cmd1 -> input of cmd2
ls | grep D           # filter
ls | tee file         # screen AND file
ls | tee -a file      # screen AND append to file

# Permissions
ls -l                 # inspect
chmod +x script.sh    # make executable
./script.sh           # run
```

---

## 13. Self-check questions

1. What are the default input and output devices for a command?
2. Difference between `>` and `>>`. Which one loses data?
3. Define a file descriptor. What kind of number is it?
4. Name the three standard streams, their `/dev` paths and their descriptor numbers.
5. What does the kernel do when a file is opened?
6. What are file descriptors called in Windows?
7. Rewrite `cat file.txt` in its fully explicit redirection form.
8. What is `/dev/null` and why is it called a black hole?
9. How do you discard only errors but keep normal output visible?
10. Two ways to send both stdout and stderr into the same file.
11. Difference between `|` and `>`.
12. What problem does `tee` solve, and what does `-a` change?
13. Four different ways to create a file.
14. In `-rw-r--r--`, who has what? Why did the script fail to run?
15. What does `$` do in `$i`, and what does `#!/bin/bash` declare?

---

## 14. Note from the trainer

This is a **huge topic** and could not be finished in one session — the delimiter concept, heredocs and more advanced descriptor manipulation were deferred. The session deliberately weighted **practical demonstration** over theory, with a promise to revisit. Learners were advised to rewatch the recording if any part was unclear.
