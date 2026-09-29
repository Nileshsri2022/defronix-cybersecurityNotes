# Explained — 059 — Day 6: Bash for Bug Bounty (Parameter Expansion, part 1: Variables)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 6 (~35–40 min, whiteboard + live Kali terminal — the first hands-on terminal class since Day-2).
**Curriculum position:** inside **STEP 3 (shell expansion)** — the expansion deep-dive series begins with **parameter expansion**. It does *not* finish today: advanced features continue Day-7. Steps 4 & 5 (quote-removal / redirection per his roadmap garble) remain queued behind the expansion tour.
**Why this class is a hinge:** until now "expansion" was an abstract four-stage chart (Day-5). Today one of its citizens gets flesh — and it happens to be the one you'll type ten-thousand times a week: `$VAR`.

---

## Part 1 — the vocabulary ladder (build it exactly in this order)

1. **PARAMETER** — *"any ENTITY that STORES VALUES."* A labeled container inside the shell.
   → purpose of shell parameters: **store data once, REFERENCE it inside scripts/commands as many times as needed.**
2. There are **THREE kinds of shell parameters**:
   | Type | What it is | Today? |
   |---|---|---|
   | **VARIABLE** | a parameter whose value **you can manually change** | ✅ this class |
   | **POSITIONAL parameter** | script arguments by position (`$1`, `$2`…) | later class |
   | **SPECIAL parameter** | shell-maintained read-mostly values | later class |
3. **VARIABLE** — *"parameters whose VALUES you can MANUALLY CHANGE."* The everyday workhorse.

### The box model (recite it until reflexive)

```
STUDENT  ──►  ┌────────────┐
(name)        │  Nitesh    │   ← data lives INSIDE the box
              └────────────┘
ASSIGN    = put data INTO the box        →   STUDENT=Nitesh
REFERENCE = pull data back OUT to use    →   echo ${STUDENT}
```

Everything about variables in any language is these two verbs wearing syntax.

## Part 2 — doing it: the syntax laws

**Assignment (creating/setting):**
```bash
STUDENT=Nitesh
```
- Format: `NAME=VALUE`. **Law: NO spaces around `=`.** (`X = 10` is not an assignment — bash parses `X` as a command with args `=` `10`.)

**Reference (using the value) — two spellings, one right answer:**
```bash
echo ${STUDENT}   ✅ the "professional"/correct way
echo $STUDENT     ⚠️ works for plain reads…
```
…so why the braces? Because **advanced parameter-expansion features (default values, length ops, search-and-replace — the Day-7+ toolkit) ONLY exist inside `${…}`**. `$NAME` is the read-only shortcut. Learn `${NAME}` as the default and `$NAME` as the shorthand you tolerate in legacy code.

### What the shell actually does at `$` time — *parameter expansion defined operationally*

> The shell **finds** the parameter named, **fetches its ENTIRE stored value**, and **TEXTUALLY REPLACES** the `${STUDENT}` token with it — before the command ever runs.

```bash
STUDENT=Nitesh
echo ${STUDENT}        # shell first rewrites the line to:  echo Nitesh   → prints Nitesh
```
That's the "expansion" from Day-5's stage-2 chart — now you see its mechanism: a find-and-replace pass over the line.

### The case for variables — the 25-edits thought experiment

Without variables: a 100-line script using the same target/path/username in **25 places**; requirement changes → **25 manual edits** (miss one → silent bug). With a variable: **one definition**, references everywhere; change the definition once → the whole 2000-line script updates. For bug-bounty work this is literal: `TARGET`, `DOMAIN`, `OUTDIR`, `WORDLIST` at the top of every recon script — one edit re-aims the entire pipeline.

### Persistence — variables are session-born and session-buried

- Values are **TEMPORARY**: **logout/login wipes them** (each shell process owns its own variable store).
- Permanence requires writing the assignment into a **profile file** (`~/.bashrc`/`~/.profile` family — his Linux series covers it; failing that, ask in the group for the promised dedicated video).

## Part 3 — naming RULES (each demonstrated failing or working on Kali)

| Rule | Demo today | Result |
|---|---|---|
| **No special character at the start** | `@STUDENT=Nitesh` | **`command not found`** — bash treats the whole token as a command NAME, not an assignment |
| **No leading digit** | `4STUDENT=Nitesh` | fails identically |
| **Leading underscore is legal** | `_STUDENT=Sachin` | ✅ works |
| **Reserved words are off-limits** | trying to define `echo=…` | forbidden — the word already owns bash semantics |

(Contributes the mental model: valid names ≈ letters/digits/underscore **not starting with a digit**, steering clear of bash's reserved vocabulary.)

## Part 4 — SYSTEM-DEFINED = environment variables

**Definition (verbatim-shaped):** *"an environment variable is a DYNAMIC NAME-VALUE pair that may be USED by ONE OR MORE programs running."*

Plain version: the OS pre-populates dozens of variables for every login; together they ARE your session's "environment" — every process inherits and consults them. Every user login gets **its own** environment (this is exactly how corporate desktops greet you with your name, your permissions, your do's-and-don'ts banner — *you* defined none of it).

**Convention (social, not syntactic):** system/env variables in **ALL-CAPS** (`$HOME`); user variables in **lowercase** — so a glance separates what the machine owns from what you own.

### The six demos from his Kali box

| Command | His output | Meaning |
|---|---|---|
| `echo $HOME` | `/home/kali` | absolute path of the logged-in user's home dir |
| `echo $USER` | `kali` → after `su` → **`root`** | current username; genuinely dynamic per identity |
| `echo $HOSTNAME` | *(empty)* | machine's name — **undefined here; expands to empty string, NOT an error** until someone sets it |
| `echo $HOSTTYPE` | *(empty)* | normally CPU architecture (his VM leaves it blank) |
| `echo $SHELL` | `/usr/bin/bash` | the active shell binary; becomes `/usr/bin/zsh` if you switch shells |
| `echo $PWD` | current dir | present working directory |

**The `$HOSTNAME` lesson is bigger than the variable:** an unset parameter expands to **nothing, silently** — in a script, `results_$HOSTNAME.txt` quietly becomes `results_.txt`. Remember this when hunts misfire.

## C) What today is NOT

- **Not the whole of parameter expansion** — explicitly deferred: **advanced features** ("jo advanced features hain, next class") + **more system-defined variables** continue in Day-7. Positional & special parameters = further classes.
- **No new pipeline step** — still inside Step 3; steps 4 (redirection family) & 5 (quote removal) start only after braces/arithmetic/command-substitution/tilde/word-splitting/globbing are toured ("step-four pe jaane waala nahi, usse pehle in stages ko padhaunga").

## D) Session sociology (compact log)

- Live count at open: **7** (≈2 = his own team); two self-declared first-timers ("Fact-Number-One", "King") get the standing advice: **stay live AND backfill Days 1–5** ("30–35 min each, back-to-back basics, motivation included").
- Product plugs repeated: **Defronix Android app** (Play-Store listing shown — free live classes, paid cohorts "bahut saste," offline downloads), **LinkedIn page** (daily posts; the **five-step command-line ROADMAP picture lives there** — the course is literally following that diagram), full-course **PDFs promised** soon.
- Two anecdotes aired: the Telegram group scoffers who can't answer the in-group basics ("dekhte nahi … bakwaas"), and a real success — a student who cleared a **Linux-admin interview** off the 15-day Linux playlist alone (comment read aloud; "maine comment karwaya nahi — apne dil se likha").
- **Gurneet's Telegram doubt** → the trigger for today's env-variable list (resolved in-class).

## E) Pitfalls table

| Symptom | Root cause | Cure |
|---|---|---|
| `command not found` on an assignment attempt | name started with special char / digit | start with letter or `_`; letters+digits+`_` only |
| `bash: X: command not found` where `X = 1` typed | **spaces around `=`** — bash ran `X` as a command | `X=1`, glued |
| `${x}` expands in one script, silently empty in another | variables don't persist across sessions | re-export via profile file if needed permanently |
| `results_.txt`-style clobbered filenames | unset env-var ($HOSTNAME) expanded to **empty** | quote + default-guard: `${HOSTNAME:-unknown}` *(Day-7 feature)* |
| `$var x` glued text misparses | brace-less form makes fuzzier token boundaries | `${var}x` — another reason braces are "the right way" |

## F) Cheat card

```
parameter   = any entity that stores a value
3 kinds     = VARIABLE · POSITIONAL · SPECIAL
variable    = parameter whose value YOU can manually change

create:     NAME=VALUE            ← NO spaces around =
use:        echo ${NAME}          ← braces = correct form (advanced features need them)
            echo $NAME            ← plain-read shortcut

parameter expansion = shell finds the parameter → fetches its ENTIRE value
                    → replaces ${NAME} in the line → THEN runs the command

rules: no leading digit · no leading special char · leading _ OK · no reserved words
life : variables die at logout → permanence = profile file
style: ENV/system vars = ALL-CAPS · user vars = lowercase (convention, not rule)

common env vars: $HOME $USER $SHELL $PWD $HOSTNAME $HOSTTYPE
unset var ⟹ expands to EMPTY STRING (silently!)  — remember at 2 a.m.
```

**Next class (announced):** parameter expansion CONTINUES — remaining system-defined variables + the **advanced features** (`${var:-default}` family), staying within the 35–40-minute format the community voted for.
