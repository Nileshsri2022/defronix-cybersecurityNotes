# Explained — 065 — Day 10: Bash for Bug Bounty (Globbing ∙ Quote Removal ∙ Redirection — the 5-Step Pipeline Completed)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 10 (~50 min, live Kali; the capstone of the command-line-processing arc).
**Curriculum position:** **END OF THE FIVE STEPS.** Today: globbing (step-3's final expansion) → step-4 quote removal → step-5 redirection (pointed to the Linux series' deep-dive). The next class = a fully practical pipeline revision; the class after = **real scripting begins.** Total course now projected at **35–50 lectures** ("bash hasn't even started yet — we just finished how the command line works").

---

## PART A — Globbing (filename expansion)

### Vocabulary & origin
- **Globbing = filename expansion** — from the **`glob`** program shipped in **Bell Labs Unix, 1969–1975**.
- Definition (his on-screen text, verbatim): *"a program that would replace text containing special pattern symbols with a list of filenames that matches those patterns."*
- **Where it fires:** only on **words** (post-tokenization), and only when pattern characters appear **unquoted** in those words.

### The motivation (his "sachin" parable, distilled)
You remember the file starts with `sachin…` — but not the rest, and not its length: 2 chars? 10? letters or digits? Will you hand-try `sachinA`, `sachinB`,… `sachin9`? Of course not — that's the exact problem globbing automates: **give the remembered fragment + a pattern → the shell tries every combination against the directory and prints the matches.**

### The three special characters (verified in the live lab)

| Char | Name | Meaning | Length rule |
|---|---|---|---|
| `*` | asterisk ("star") | **any run of any characters** | length-**independent** — 0,1,30 chars, anything |
| `?` | question mark | **exactly one** arbitrary char | fixed length = number of `?`s |
| `[…]` | bracket set | **exactly one char from the listed set** | one char, but restricted to your list/range |

**Lab inventory:** `file1.txt … file5.txt`, `filea.txt`, `ABC`, `abc`, `file12th`, `ab`.

```bash
ls *            # → everything in CWD (Desktop Documents Downloads …)
ls *.txt        # → file1.txt file2.txt … (star absorbs any prefix length)
ls *.pdf        # → no match
ls file*        # → file1-5.txt, filea.txt, file12th
ls file1*       # → file1.txt AND file12th  (star proves length-independence)
ls file?.txt    # → file1-5.txt + filea.txt   (ABC, file12th, abc excluded — length≠1)
ls file??.txt-… # → count of ? = exact name length — "neither more nor less"
ls ???          # → ABC, abc
ls file[abc].txt# → filea.txt   (b,c not present — set restriction + still ONE char)
ls file[1a].txt # → file1.txt + filea.txt
ls [a-q]*       # ranges work — must be a real sequence
ls [0-9]*       # digit ranges too (combined with * → file12th style matches)
ls /*           # ★ works on paths, not just CWD — "the power of globbing"
```

**Bracket refinements he demonstrated:** **case-sensitive** (`[abc]` won't match `ABC` — list capitals separately); chained brackets = positional slots (`[a…][b…]` = char-1 from first set, char-2 from second).

**Bug-bounty lens:** `*.log`, `*.bak`, `id_rsa*`, `shadow?`, `*.sql` — log-monitoring and loot-hunting on a compromised box is 90% glob fluency; every fuzzing filename list you've written is what glob automates in-place.

## PART B — Step 4: Quote removal

### Recap of the machinery
Day-3: **quoting removes a character's special meaning** — via three tools: **backslash `\`**, **single quotes `'…'`**, **double quotes `"…"`**.

### Why removal exists
Once quoting has done its job, the quotes are dead weight. Step-4 strips them — **but only under both conditions** (his definition, verbatim): *"during quote removal, the shell removes all unquoted backslashes, single quotes and double-quote characters that did not result from shell expansion."*

1. the quote chars must be **unquoted themselves**, and
2. they must **not be the product of a shell expansion**.

### The three demos that make it click

| Command | Output | Which rule decides |
|---|---|---|
| `echo \$HOME` | `$HOME` | backslash was unquoted & hand-typed → **removed**; `$` lost its meaning earlier during quoting |
| `echo '\$HOME'` | `\$HOME` | the single quotes are removed; the backslash **was quoted by them** → survives |
| `name="C:\Users\sachin\documents"` → `echo $name` | `C:\Users\sachin\documents` | those backslashes came **from a parameter-expansion result** → condition 2 fails → **never removed** |

(He visibly bumps into a goofed variant mid-demo — then uses it as the exact illustration of rule 2; the student's imagined "but the quotes were removed, why is it still here?!" is the intended landing.)

**Why this matters to a script author:** backslashes inside variables are data, not syntax — they survive expansion untouched; and Windows-style paths in variables are *safe* to echo/pass.

## PART C — Step 5: Redirection (recap + pointer)

After **tokenization → command identification → expansion → quote removal**, the shell routes bytes:

- **stdin (standard input)** — from keyboard? a file? another command's output?
- **stdout (standard output)** — to terminal? into a file (> / >>)? into the next command (|)?
- **stderr (standard error)** — shown? caught into its own file (`2>`)?

…**then** execution happens and the directed result appears. He **doesn't re-teach** it: assignment is the **Defronix playlist — Day-3/Day-4 "Input-Output Redirection"** videos — "a B.Tech-grade concept; master it once, and you'll never struggle again."

## PART D — Meta content worth keeping

- **Notes shift to Medium:** he began publishing written mirrors of this course on **Medium** (first article = how-bash-processes-the-command-line, already in the group); videos+articles together, copy-paste-friendly as student notes — PPTs retired.
- **Scale honesty:** ~10 lectures in of a projected **35–50**; next class = full practical revision of steps 1–5 on 1–2 real commands; then "the real fight": scripting, logic, loops, statements, automation + mini-project per concept + 2–4 capstone projects (usable by sysadmins and bounty hunters).
- **"No duration course":** ends when syllabus is done *and* doubts are zero *and* you're "masters."
- **Doubt-session FAQ distilled:**
  - *"No programming background?"* — fine; scripting ≠ programming; concepts transfer, only syntax changes.
  - *"Red Hat practice?"* — RHEL has a 1-yr free trial ISO (account at redhat.com), **but prefer CentOS** — a "ditto copy," free/open, no repo-config pain; RHEL-class = industry server OS (what the real targets run), Kali/Parrot = attacker kits; 99% of commands identical, only package management differs.
  - *"Practice from a phone?"* — **No.** "Without a laptop you can't take a single step in this industry — a phone is good for theory only." Cloud free-tier VM is the only sensible no-laptop workaround (free first machine; billing later).

## E) Pitfall table

| Symptom | Root cause | Cure |
|---|---|---|
| glob prints pattern literally ("no matches found" / pattern echoed) | no file matched (or, in quotes, glob disabled entirely) | check pattern vs `ls` reality; know your shell's no-match behavior |
| `[abc]` doesn't match `abc`-the-file | brackets = ONE char, not a string | use `???` or `*` for multi-char names |
| `[a-b]`-style "won't work" | endpoints not a valid sequence | give true ascending ranges: `[a-z]`, `[0-9]`, `[A-Z]` |
| `echo $path` shows backslashes surviving | expansion output is immune to quote removal (rule 2) | that's correct — backslashes in DATA are data |
| `echo '\$HOME'` keeps the backslash | quoted backslash ≠ unquoted backslash (rule 1) | expected; quote removal only eats *unquoted* quotes |
| "my question-mark glob caught only some files" | `?` count = exact name length | one `?` per missing char; two `??` for two, etc. |
| expecting stdout+errors together, errors "lost" | stderr is its own channel | `cmd 2> errors.txt` (Day-3/4 playlist) |

## F) Cheat card

```
GLOBBING (filename expansion · words only · chars must be UNQUOTED)
  *  = any run, any length        : ls file*  → file1, filea, file12th, file1.txt…
  ?  = exactly 1 char             : ls file?.txt → file1.txt filea.txt
  [] = exactly 1 char FROM SET    : ls file[1a].txt → file1.txt filea.txt
     ranges [a-z] [A-Z] [0-9] — must be ascending sequence · CASE-sensitive
     chains = positional: [..][..] ; works on paths: ls /*

QUOTE REMOVAL (step 4) — removes \, ' ' , " "  IFF
  (1) they are UNQUOTED themselves   AND   (2) not the RESULT of an expansion
  echo \$HOME   → $HOME     (unquoted \ removed)
  echo '\$HOME' → \$HOME    (\ was quoted → kept)
  name="C:\u\s\d"; echo $name → C:\u\s\d   (expansion data → kept)

REDIRECTION (step 5) — route of bytes: stdin · stdout · stderr → then EXECUTE
  details: Defronix playlist Day-3/Day-4 (input-output redirection video)

THE 5 STEPS, COMPLETE: tokenization → command identification → expansions
     (brace·tilde·param·cmd-sub·arith·word-split·glob) → quote removal → redirection
```

**Next class (announced):** a purely practical **revision session** — taking 1–2 full commands through all five steps end-to-end — then scripting begins ("the real fight").
