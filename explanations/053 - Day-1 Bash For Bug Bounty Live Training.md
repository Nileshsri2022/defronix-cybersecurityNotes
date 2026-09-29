# Explained — 053 — Day 1: Bash for Bug Bounty (Live Capsule Course)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 1 (~45-minute format class; live chat interactions included).
**Prerequisites (his words):** the academy's free 15-day **capsule course** playlist — Linux fundamentals — before this series; distro doesn't matter for scripting (this class used a **Red Hat** VM because his Ubuntu/Kali images were acting up).
**Series logistics:** sessions get scheduled only after the previous video hits its **1K-view community threshold** (likes/comments/shares — "we want nothing from you except that"); planned length **25+ videos**, each ~35–45 minutes, one topic per class.
**Why it matters for bug bounty:** before Bash becomes an automation weapon (recon pipelines, subdomain sweeping, mass-screenshotting), you need to know exactly *what a shell is*, *what a script file actually is to Linux*, and *why the first line and the permission bits decide whether hours of work run or explode somewhere else*. This class is those three foundations — nothing more, deliberately.

---

## 1) What a shell IS (and where bash fits)

A **shell** is the program that sits between you and the operating system's **kernel**:

```
you type a command → shell INTERPRETS it → hands the instruction to the OS
OS checks your permissions/security policy → performs the task → result returns
```

The lecture's exact framing: the shell "interprets commands" and tells the OS *"the user wants this task done"* — the OS then executes it **according to permissions and security context**. There were/are many shells (Bourne `sh`, C shell, Korn, Zsh…). **Bash** ("Bourne Again SHell") is the modernized Bourne successor — in his words: the old version had issues; bash is the upgraded, **advanced and faster** one, and has become the default everywhere — which is why the whole course targets **bash**.

## 2) What a script IS

A **shell script is a plain text file containing a series of commands**. The shell **reads the file and executes the commands one by one** — that's the entire concept. (His phrases: "a file… inside which commands… we call it a script — basically *containing commands*.") This is why bug-bounty automation is lean: your "tool" can be 40 lines of grep/curl/jq arranged in a text file.

## 3) WHY scripts exist — the admin-of-20-commands story

His motivating fable, worth keeping whole because it names the three failure modes scripts kill:

> You're on **admin duty**. Every week, on a fixed day, at a fixed time, 20 commands must run.
> Failure mode #1 — **memory**: you must *remember* 20 commands forever.
> Failure mode #2 — **typos**: one wrong letter and "the command that had to run… something else ran." Manual repetition invites error.
> Failure mode #3 — **forgetting**: someday you're busy/away — the job simply doesn't run.
>
> Fix: put the 20 commands in a script and **schedule it** — a **cron job** runs the file on that date/time **automatically**. No memorising, no typos, no forgetting. That's automation — "your liberty increased"; the professional word for it: **reliability**.

Bug-bounty translation: recon is exactly "20 commands every program, every week" (subfinder → httpx → nuclei → screenshots → diff). If you're typing them, you're the cron job. Scripts let the machine be the cron job.

## 4) Interpreter, not compiler (the translator analogy)

A short but examinable aside:

- **Compiler** = a translator who first reads the WHOLE speech, understands it, and delivers the full translation at once (translate everything → then run).
- **Interpreter** = a translator who renders **one statement at a time**, immediately: "one statement → machine code → next statement → machine code…"

Bash is an **interpreter* — your script is consumed line-by-line, top to bottom, every time it runs. Practical side-effect: a typo on line 100 doesn't fail the run at startup; it fails *when line 100 is reached*. (And it's why you can also type the very same commands interactively — the shell interprets them identically.)

## 5) The 3-component structure of a bash script

The day's core deliverable — every script he writes on this course will have:

### (1) BEGINNING component — the shebang

```bash
#!/bin/bash
```

- `#!` ("sharp-bang" → **shebang**) must be the **very first bytes of line 1** — **no blank line, no comment, nothing before it**.
- Immediately after: the **full path to the interpreter** that will READ this file — `/bin/bash` because Linux binaries live in `/bin`, and the bash binary sits there.

**Why it matters — what happens without it:** the script *still runs*… but inside **whatever shell the invoking user currently has**. If you wrote bash-specific syntax and your teammate runs it from `sh`/`zsh`/an old Bourne, the features silently misbehave. His war story: *"you wrote the code with effort over 10 days… your colleague runs it in another shell → 'not successful' — wrong output. The mistake was that you skipped the beginning line."* The shebang pins the interpreter regardless of who runs the file, from where.

**His proof trick (memorable):** edit the first line to `#!/usr/bin/python`, then run `file our-script.sh` — `file` now reports **a python script**. Linux/`file` literally identifies the interpreter from the shebang bytes. (Bonus: this is also why `#!/usr/bin/env bash` exists — a portable lookup — but his course pins `/bin/bash` for clarity.)

### (2) MIDDLE component — the actual work

The commands themselves — 1 line or 1000 lines. His demo middle was a single `echo "This is my first script"`. This is "the task you want the OS/automation to perform."

### (3) END component — the exit status

- Every command/program finishes with an **exit-status code from 0 to 255**.
- **0 = success.** Any **non-zero (1–255) = failure**.
- You do NOT have to write `exit 0` — **the script's final exit status automatically becomes the exit status of its LAST command** ("the shell takes care of it"): last command fails ⇒ script reports failure; last command passes ⇒ success. This inheritance matters enormously in pipelines and cron monitoring (`./run.sh || mail me` works because of it).

## 6) Running the script — dots, slashes, permissions

```bash
mkdir bash-project && cd bash-project
vim our-script.sh           # content:
                              #   #!/bin/bash
                              #   echo "This is my first script"
chmod +x our-script.sh      # demo: grant execute
./our-script.sh             # run it
# → This is my first script
```

Anatomy of `./our-script.sh` — because he asked "why the dot?":
- **`.`** represents the **current working directory**.
- **`/`** is the **directory separator** (a lone `/` = the filesystem root).
- So `./our-script.sh` literally reads "[current-dir][separator]file" — compare `pwd` output + `cd`. (Root cause of the classic "command not found" puzzle: `.` is usually NOT in `$PATH`, so the bare filename isn't enough; `./` forces the explicit path. He demonstrates the *must have execute permission* part: without `+x` the kernel refuses to run it, no matter the shebang.)

**The permission rule (the day's most quotable line):**
> **Every script gets `chmod 744`** — owner gets **full (read/write/execute)**, group and everyone else get **read-only**. Give permission bits *special* attention: no one outside the owner should be able to modify or run it at will.

Translate: scripts are code — code is attack surface (and, in team servers, shared-surface). `744` is the safe default; `777`/wildcard `+x` on shared boxes is how "someone just ran it" incidents happen. (Also note `chmod +x` from the demo is a convenience — the *standard* he sets is `744`.)

## 7) The whole class in one recap (his own closing inventory)

Shell → its purpose → bash → script → why scripts (admin/cron reliability) → structure (beginning/middle/end) → why shebang → what an interpreter is → middle = commands → exit status (0–255, 0=success, inherits last command) → permissions (`+x` to run, **`744` as the rule**).

## 8) Pitfalls & security-tinted details worth keeping

- **Shebang-less scripts are context bombs**: correct on your shell, wrong on someone else's. Pin `#!/bin/bash`, always — it's also self-documentation (`file` shows it).
- **Nothing may precede `#!`** — one invisible blank line (or a BOM) and you've handed execution to the caller's current shell.
- **Exit-status inheritance** cuts both ways: if your last line is a cosmetic `echo "done"`, a failing script *reports success*. In real recon scripts, end with a meaningful command or an explicit `exit "$?"`/guards — later classes' scripts hinge on `$?`.
- **`744` is mandatory hygiene** he repeats twice; in shared labs people who `chmod 777` hand their tooling (and credentials-in-scripts) to everyone.
- **Interpreter one-statement-at-a-time** → long scripts fail *late*; put `set -euo pipefail` at the top in later, serious tooling (not covered today, flagged for future notes).
- **Drosophila of live classes:** mic checks, music glitches, view-count housekeeping — all preserved in the translation; the teaching arc itself is clean and ends exactly on the structure+permissions recap.
- **What's deliberately absent:** variables, loops, input, `read`, `$1` arguments, grep pipelines — "next class we create scripts one by one." Expect Day-2 to move from shape to muscle.

## 9) Stick-it-to-the-monitor card

```
shell  = interpreter between YOU and the OS (checks perms, does the task)
bash   = upgraded Bourne shell — the default
script = text file of commands; shell executes them line by line
why    = cron + script ⇒ no memory, no typos, no forgetting  (reliability)

structure:
  #!/bin/bash        ← BEGINNING: nothing before it; /bin = where binaries live
  echo "..."         ← MIDDLE: the actual commands (1..1000 lines)
  (exit status)      ← END: 0..255; 0=success; auto-inherited from LAST command

run it:  chmod 744 script.sh        # rule: owner full, others read-only
         ./script.sh                # . = cwd, / = separator; needs +x or exec fails

proof:   sed -i '1s|.*|#!/usr/bin/python|' s.sh; file s.sh  → "a python script"
```

**Next class (announced):** build real scripts, one-by-one, hands-on — the practical sprint that starts turning this skeleton into recon tooling.
