# Explanation — Day 13: Variables, `export` & File Globbing

**Lecture:** 013 — Kali Linux Free Capsule Course, Day 13
**Translation:** [`english/013 - Kali Linux Free Capsule Course - Day 13.md`](../english/013%20-%20Kali%20Linux%20Free%20Capsule%20Course%20-%20Day%2013.md)
**Course status:** Two classes remaining in the capsule course.

---

## Part 1 — What a variable is

### The box analogy

> Think of variables as **small boxes** in your program. When you write a program, **you are putting data into a box**, and you give that box a **name**. That name is the **variable**.

| Operation | Meaning |
|---|---|
| **Assigning** (`var=value`) | putting data **INTO** the box |
| **Referencing** (`$var`) | taking the data back **OUT** of the box |

### The medical shop analogy

At a medical shop, staff keep many labelled **boxes**. When they see a medicine's name they go **directly to that box** and pull it out.

- The **box** = the variable
- The **medicine inside** = the value / data
- The **label** = the variable name, so it can be **identified directly**

---

## Part 2 — Two types of variable

| Type | Also called | Convention |
|---|---|---|
| **System-defined** | **environment variables** | usually **CAPITALS** |
| **User-defined** | your own | usually **lowercase** |

> ⚠ **This is convention, not rule.** *"There is NO condition, NO policy that you must keep system-defined variables in capitals."* It exists purely so you can tell at a glance which is which.

---

## Part 3 — Defining and referencing

```bash
practice=sachin          # define
echo $practice           # reference -> sachin
echo ${practice}         # the formal/official syntax
```

### ⚠ Rule 1 — No spaces around `=`

```bash
practice=sachin          # ✔
practice = sachin        # ✘ WRONG
```

> **In bash you must NOT use a space before or after the equals sign.** This is the single most common beginner error.

### ⚠ Rule 2 — Must start with a letter

```bash
practice=value           # ✔
2practice=value          # ✘ ERROR
_practice=value          # ✔ (underscore allowed)
```

> **A variable will never start directly with a number or special character** — always a small or capital alphabet.

### What `echo` does

The reference `$practice` is **replaced** by the value before the command runs. `echo`'s job is simply to **show output on your screen**.

---

## Part 4 — Why variables are worth the trouble

The honest question raised in class: *why not just type the value directly into the command?*

> **The main benefit is seen when you are writing a SCRIPT.**

If a value appears in **50 places** — or **1000 times** — across a script:

| Without a variable | With a variable |
|---|---|
| Find-and-replace all 50 occurrences | **Change one line** |
| Ctrl+F, manual edits, risk of missing one | Automatically applied everywhere |

> *"To deal with such situations, we use variables."*

---

## Part 5 — Environment variables

### The workplace analogy

When you join a company, **a system environment is set up and given to you** before you start. You can change things afterwards, but you begin with files, directories and policies already in place.

> **That pre-configured working context is what environment variables provide** to a shell session.

### The common ones

| Variable | Contains |
|---|---|
| **`$HOME`** | absolute path of the current user's home directory |
| **`$USER`** | the username |
| **`$HOSTNAME`** | the machine's hostname (blank if never set) |
| **`$SHELL`** | which shell is in use |
| **`$PWD`** | the present working directory |
| **`$PATH`** | **where the system looks for command binaries** |
| **`$PS1`** | **the prompt's appearance** |

```bash
echo $HOME       # /root
echo $USER
echo $SHELL      # /bin/bash
echo $PWD
echo $PATH
```

---

## Part 6 — `$PATH` — how commands are found ⭐

### The question it answers

> *You type `passwd` and it runs. **How did the system know where its binary file is located?***

**Answer: the `PATH` environment variable.** It holds a colon-separated list of directories the shell searches, in order.

### The search process

1. Shell checks each directory listed in `$PATH`, in order.
2. If the binary is found → it runs.
3. **If it is found in none of them** → the command appears not to exist.

### The consequence

> **If a binary's path is not defined anywhere in `$PATH`, then to execute that command you must give the FULL BINARY PATH.**

```bash
mytool              # command not found
/opt/tools/mytool   # works — full path given
```

This is exactly why you type `./script.sh` rather than `script.sh` — the current directory is **not** in `$PATH` by default, which is itself a deliberate security decision.

---

## Part 7 — `PS1` — customising your prompt

`PS1` controls what your **prompt** looks like — the `root@kali:~#` you see every day.

```bash
export PS1="..."        # apply a new prompt
```

You can include the username, hostname, current directory, the date, the `$`/`#` marker, and literal characters like `@`.

**To make it permanent**, add the `export PS1=...` line to your profile file (`~/.bashrc`).

> *"Why is the `PS1` variable so important — because however you want your prompt, you can MODIFY it."*

---

## Part 8 — `export` and the shell hierarchy ⭐

### The problem demonstrated

```bash
var1=test
echo $var1        # test          ✔

bash              # start a NEW shell
echo $var1        # (nothing)     ✘
```

**Why?** A plain variable belongs **only to the shell that created it.** A child shell knows nothing about it.

### The fix

```bash
export var1
```

> **If you want to access a variable from another shell, you must EXPORT it.**

Now child shells inherit it. **But this is still temporary** — it dies at logout.

---

## Part 9 — The four levels of persistence ⭐

This is the key takeaway of the variable half of the session.

| # | Method | Scope | Survives new shell? | Survives logout? |
|---|---|---|---|---|
| 1 | `var=value` | **current shell only** | ❌ | ❌ |
| 2 | `export var=value` | **+ child shells** | ✅ | ❌ |
| 3 | entry in **`~/.bashrc`** | **that user**, permanently | ✅ | ✅ |
| 4 | entry in **`/etc/profile`** | **ALL users**, permanently | ✅ | ✅ |

### Level 3 — per-user permanent

```bash
vim ~/.bashrc
# add at the end:
export var1=value

source ~/.bashrc       # re-read the file
```

> **`source` is required.** You must *"tell your system once: read this again, I have made some changes inside it."* Otherwise the change only takes effect at your next login.

> ⚠ **This is USER-SPECIFIC** — *"it will only be set for this user; it will not be set for any other user."*

### Level 4 — global

Add `export VARNAME=value` to the **system-wide profile** (`/etc/profile`). Then **any user** on the machine gets it.

### A caution from the session

The trainer's own `.bashrc` threw an error during the live demo: *"something has gone wrong in the file... because we tamper with it a lot."*

> **Practical lesson: back up `~/.bashrc` before editing it.** A syntax error there can break every new shell you open.

---

## Part 10 — `set` and `unset`

```bash
set                    # list variables
unset variablename     # remove a variable (temporarily)
```

---

## Part 11 — File Globbing

> **File globbing = DYNAMIC FILE NAME GENERATION.**
>
> Used to find files **especially when you don't know the full filename.**

### ⚠ It is not a command

> *"Don't think it is some command — it isn't. It is a TECHNIQUE."*

Globbing is expanded **by the shell**, before the command ever runs. It works with `ls`, `find`, `locate`, `grep`, `cp`, `rm` — everything.

### Setup used in the demo

```bash
touch file1 file2 filea fileb filec filed
```

---

### 11.1 `*` — any number of characters

```bash
ls file*         # file1 file2 filea fileb filec filed
ls *ila*         # anything containing "ila", anywhere
```

> **`*` is LENGTH INDEPENDENT.** *"It does not define the length. It's not that where you put the star, only one character [matches]. It will see all of them."*

A **sorted list** works in the background — a–z, small to capital, then 1, 2, 3, 4.

---

### 11.2 `?` — exactly ONE character

```bash
ls file?         # file1 file2 filea  — exactly one char after "file"
ls file??        # exactly TWO chars
ls file???       # exactly THREE chars
```

> **`?` is LENGTH DEPENDENT.** One `?` = one character. Two = two. This is the crucial difference from `*`.

| Wildcard | Characters matched | Length-sensitive? |
|---|---|---|
| `*` | **any number**, including zero | ❌ No |
| `?` | **exactly one** per `?` | ✅ Yes |

---

### 11.3 `[ ]` — a defined SET of characters

```bash
ls file[abc]     # filea fileb filec — but NOT filed or file1
```

> Square brackets work **exactly like `?`** — matching **one character** — **but YOU define which characters are acceptable.**

| Form | Matches one character that is… |
|---|---|
| `[abc]` | `a`, `b` **or** `c` |
| `[1-9]` | any digit in the **range** 1–9 |
| `[a-z]` | any lowercase letter |
| `[!2]` | anything **EXCEPT** `2` (negation) |

```bash
ls File*la[123]    # ends in la1, la2 or la3
ls File[!2]*       # second char is NOT 2
```

---

### 11.4 Why globbing matters

> **`find` and `locate` find files. Globbing is the technique that makes your PATTERN easier.**

The realistic use case given:

> *You have a **rough idea** of a filename — you remember the three characters `ila` somewhere in the middle. There could be anything before and anything after.*

```bash
find / -name "*ila*"
```

> *Then every file in your system containing those three characters, wherever it is found, gets printed on your screen.*

Combine globbing with `find`, `locate` or `grep` and **your searching becomes considerably easier.**

---

## Part 12 — Complete cheat sheet

```bash
# ---- variables ----
name=value               # define  (NO spaces around =)
echo $name               # reference
echo ${name}             # formal syntax
# Rules: no spaces around '='; must start with a letter

# ---- persistence ----
var=value                # current shell only
export var=value         # + child shells (still temporary)
vim ~/.bashrc            # permanent, THIS user
  export var=value
source ~/.bashrc         # re-read so it takes effect now
vim /etc/profile         # permanent, ALL users
  export VAR=value

set                      # list variables
unset var                # remove

# ---- environment variables ----
echo $HOME $USER $HOSTNAME $SHELL $PWD $PATH
export PS1="..."         # customise the prompt

# ---- globbing (a shell technique, not a command) ----
ls file*                 # any number of characters
ls *ila*                 # contains "ila"
ls file?                 # EXACTLY one character
ls file??                # exactly two
ls file[abc]             # one char: a, b or c
ls File*la[123]          # ends la1 / la2 / la3
ls File[!2]*             # one char that is NOT 2

find / -name "*ila*"     # globbing + find
```

---

## Part 13 — Self-check questions

1. Explain the box analogy. What is assigning, and what is referencing?
2. What are the two types of variable, and what naming convention distinguishes them? Is it enforced?
3. Write a correct variable assignment. Why does `var = value` fail?
4. Why can't a variable start with a number?
5. Give the real reason variables are worth using, in terms of scripts.
6. What do `$HOME`, `$USER`, `$SHELL`, `$PWD` and `$HOSTNAME` hold?
7. What does `$PATH` do? Trace how the shell finds a command.
8. What must you do to run a binary that isn't in `$PATH`? Why do you type `./script.sh`?
9. What does `PS1` control, and how do you make a change to it permanent?
10. Demonstrate why a plain variable is invisible to a child shell. What fixes it?
11. Name all four levels of variable persistence and their scope.
12. Why is `source ~/.bashrc` necessary after editing the file?
13. Which file makes a variable global to all users?
14. Is globbing a command? What actually performs the expansion?
15. State the crucial difference between `*` and `?`.
16. What does `file??` match that `file?` does not?
17. What do `[abc]`, `[1-9]` and `[!2]` each match?
18. Write a `find` command locating every file containing `ila` anywhere in its name.

---

## Part 14 — Aside: scope of the course

A learner question prompted this clarification:

> *"This is the **Linux capsule course, not the pen testing course.** If this were the pen testing course, we would talk about how to enumerate usernames and passwords, and how to crack them if possible — depending on password strength, your cryptography skills, and how far you can take information gathering on a target."*
>
> *"Password cracking we will not teach here. **But one thing I will teach you: if you forgot root's password, how to change it** — at the end of this course."*

That root-password-reset demonstration remains outstanding, having also been promised on Day 8.
