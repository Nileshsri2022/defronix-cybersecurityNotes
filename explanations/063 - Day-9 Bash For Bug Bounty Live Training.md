# Explained — 063 — Day 9: Bash for Bug Bounty (Brace Expansion + Word Splitting / IFS)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 9 (~40 min, live Kali; zsh terminal + bash scripts shown side by side).
**Curriculum position:** step-3 expansion mechanics — **brace expansion** ✓ and **word splitting** ✓. Only **globbing** remains in step-3; then step-4 (**quote removal**) and step-5 (**redirection**), then a full 5-stage recap class, then real scripting.
**Emotional weather:** the instructor calls out zero homework submissions from Day 8 — engagement plea is part of this session.

---

## PART A — Brace expansion `{ }`

### Two list types

| List | Form | Order | Example |
|---|---|---|---|
| **String list** | comma-separated anything | none needed — "random" | `echo {a,19,jan,sachin,43}` → `a 19 jan sachin 43` |
| **Range list** | start**..**end | sequence, fixed order | `echo {1..5}` → `1 2 3 4 5` |

Range variants demonstrated:

```bash
{a..z}       # lowercase alphabet
{A..Z}       # uppercase alphabet
{1..100}     # numbers
{1..100..3}  # → 1 4 7 10 13 16 …  (STEP form: {start..end..step})
{01..10}     # zero-padding preserved: 01 02 … 10
```

### The golden rule: **NO spaces inside the braces**

Spaces after `{`, between items, or before `}` make the shell treat it as literal text — brace expansion silently doesn't happen (his live "error" demos). He repeats it three ways: not after opening, not between, not before closing. **`{ a,b }` ≠ brace expansion; `{a,b}` is.**

### What ranges are NOT

- `{1..q}` — mixed number/letter → does not work (prints weirdly / literally).
- `{jan..feb}` — **words can't range** — prints literally `{jan..feb}`.
- Valid: single letters (`a..z`, `A..Z`) and numbers — that's all the range engine knows.

### The workhorse pattern — prefix/suffix + range

```bash
mkdir month{1..12}                 # 12 folders in one breath
month{1..12}day{1..31}.txt         # Cartesian product → every combination
```

He *previews* with `echo` (not `mkdir`) on purpose — "needless folders = memory utilization I don't want" — always dry-run a brace expansion before arming it with `mkdir`/`touch`. Two expansions in one word multiply out; `ls`-style verified: `month12day12 … month12day31`.

**Bug-bounty angle (he's aiming there):** one-liners that manufacture candidate filenames/ID spaces (`id{1..1000}`, `admin{dev,test,prod}`) — the recon fuzzer's bread and butter.

## PART B — Word splitting (today's headline)

### The definition (his on-screen text, keep verbatim)

> *"Word splitting is a process that is performed by the shell on the results of SOME of the expansions to separate those results into separate words."*

### WHERE it fires — memorize this gate

Word splitting runs **only** on the results of **unquoted**:

1. **parameter expansion** (`$var`, `${var}`)
2. **command substitution** (`$( )`)
3. **arithmetic expansion** (`$(( ))`)

and **NOT** on tilde-expansion or brace-expansion results. "Unquoted" = no enclosing quotes stripping special meaning (Day-3 quoting paying rent again).

### Why step-2 (command identification) even works

He closes a loop left open since the pipeline lecture: the shell treats the **first word as the command and the rest as arguments** — but *who cut the line into words?* **Word splitting did, on space/newline/tab boundaries.** No splitting → no "words" → no command-vs-argument logic. It's the invisible plumbing under everything since Day 1.

### The reference list: `IFS` (Internal Field Separator)

Tokenization consults a list of *metacharacters*; word splitting consults a list stored in the **`IFS` shell variable**:

- **default contents: space, newline, tab**
- **changeable** — and when you change it, you redefine what a "word" is.
- It's invisible characters, so `echo ${IFS}` shows nothing. The peek trick: **`echo "${IFS@Q}"`** (parameter-transformation `@Q` = display in quoted form). Works in a bash script; **his zsh terminal refused** — he moved into `nano demo` (`#!/bin/bash`, `chmod 744`) and it revealed the tab/newline/space trio. Practical meta-lesson: bash tricks belong in bash scripts.

### The three demos that prove the gate (reproduce these)

```bash
# demo 1 — unquoted ⇒ split on IFS
numbers="1 2 3 4 5"
touch $numbers        # → files: 1 2 3 4 5   (ls -l shows five)
rm {1..5}             # cleanup, using Part A on real work

# demo 2 — quoted ⇒ NO splitting
touch "$numbers"      # → ONE file literally named "1 2 3 4 5"

# demo 3 — unquoted but separator not in IFS ⇒ NO split …
numbers=1,2,3,4,5
touch $numbers        # → ONE file: "1,2,3,4,5"
# … until you redefine "field":
IFS=,
touch $numbers        # → files: 1 2 3 4 5  (comma now splits)
```

Demo 3 is the conceptual payload: *"ALL conditions fulfilled — parameter expansion ✓ unquoted ✓ — yet NO splitting, because the comma wasn't in IFS. Change IFS, behavior flips."*

### Why you care (script-author consequences he pre-sells)

- `for f in $list` relies on word splitting; `"$list"` would hand you **one** giant item.
- Unquoted expansion of attacker-controlled text = argument injection — a real bug class; quoting discipline is the fix, and now you know *why* the quote matters mechanically, not just stylistically.
- Custom `IFS` is the classic CSV-parsing trick (`IFS=,` + read/loop) — he'll build on it.

## PART C — Session mechanics & friction worth keeping

- **Homework accountability moment:** Day-8's six MCQs (plus a 2-day gap) → **zero submissions**; his verbatim disappointment: "not a single person took it seriously. It's okay, up to you bro."
- **To first-timers:** don't drop the present class to chase the backlog — recordings are 25–30 min; do both, front-to-back.
- **Roadmap re-stated at high resolution:** after **globbing** (last expansion) → quote removal → redirection → a consolidated practical recap of all five stages on 1–2 real commands → then scripting proper (if-conditions, logic, assignments) → **3–4 live projects**.
- Selling point for learning the machinery: internalizing the 5 steps lets you predict the effect of every space and quote → "magnificent code with fewer errors."

## D) Pitfall table

| Symptom | Root cause | Cure |
|---|---|---|
| `mkdir { jan,feb }` makes a folder named `{` | spaces inside braces kill brace expansion | `{jan,feb}` — no spaces anywhere inside |
| `{jan..feb}` prints literally | ranges accept letters or numbers, not words | enumerate months in a **string list** or use `{1..12}` |
| `{3..q}` garbage | mixed-type endpoints | keep endpoints the same kind (both letters or both numbers) |
| `echo ${IFS}` prints "nothing" | IFS is invisible characters (space/tab/newline) | `echo "${IFS@Q}"` inside a bash script |
| `touch $numbers` makes ONE file with a weird long name | expansion was **quoted**: `touch "$numbers"` | drop quotes when you *want* splitting |
| `touch $csv` doesn't split on commas | comma ∉ default IFS (space, newline, tab) | set `IFS=,` (then restore it) inside the script |
| splitting tricks "don't work" in the terminal | he demos on **zsh**; behavior differs from bash | always verify inside `#!/bin/bash` script |
| mass-`mkdir` you didn't want | armed brace expansion without a dry run | `echo` the pattern first, then swap in `mkdir`/`touch` |

## E) Cheat card

```
brace expansion { }  : TWO lists — string list {a,19,jan,43} · range list {1..10} {a..z} {A..Z}
   step: {1..100..3} → 1 4 7 10 13…   zero-pad: {01..10}
   LAW: NO spaces inside braces · ranges = letters|numbers ONLY ({jan..feb} ✗)
   power move: month{1..12}day{1..31}.txt = full cartesian product (echo-first!)

word splitting       : shell splits RESULTS into words — ONLY on UNQUOTED
                       parameter expansion / command substitution / arithmetic expansion
                       (NOT tilde, NOT brace results)
   reference list    : IFS variable = Internal Field Separator
                       default = space + newline + tab   (see it: echo "${IFS@Q}" in a bash script)
   demos             : touch $v (5 files) · touch "$v" (1 file) · IFS=, then comma-splits
   why               : it's what makes word1=command, rest=arguments (feeds step-2)

roadmap              : globbing (last expansion) → quote removal → redirection
                       → 5-stage consolidation lab → scripting → 3–4 live projects
```

**Next class (announced):** **globbing**, completing the expansion family, then immediately stepping into quote removal as previously scheduled.
