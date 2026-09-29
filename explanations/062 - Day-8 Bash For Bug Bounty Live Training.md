# Explained — 062 — Day 8: Bash for Bug Bounty (Command Substitution, Arithmetic Expansion, `bc`)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 8 (~35 min, live Kali; first graded-task day).
**Curriculum position:** step-3 expansion mechanics continue — **command substitution** ✓ and **arithmetic expansion** ✓ covered; **brace expansion bumped to next class** (paired there with *quote removal* in a 45–50-min session). Of his announced 7 expansions, 4 are now done.
**New ritual:** graded home tasks begin — 6 MCQs due in the comments before the next class.

---

## PART A — Command substitution `$( )`

### The substitution family, side by side

| Expansion | Trigger form | What replaces the whole form |
|---|---|---|
| Parameter | `${name}` / `$name` | the **value** stored in the parameter |
| **Command substitution** | **`$(command)`** | the command's **output** (stdout) |

He teaches it explicitly as "very similar to parameter expansion — one difference: *what* does the replacing."

### The killer feature: capture into a variable

The whole construct is itself a value, so it can be **assigned**:

```bash
#!/bin/bash
time=$(date +%H:%M:%S)          # run `date`, store its output
echo "hello $USER the time right now is $time"
# → Hello kali the time right now is 21:08:14
```

`chmod 744`, run — output identical to a standalone `date +%H:%M:%S`. The stored value is now reusable anywhere in the script "as per requirement."

### You've already used it (Day-2 retention hook)

The Day-2 home-directory **backup script** — `tar` writing to a filename that contained a date-stamp — was command substitution *before you knew the term*. His delayed-teaching promise from Day 2 lands here: "I told you I'd explain it when the concept arrived."

### Why it's the workhorse (his motivation list)

- embedding one command **inside** another (nested automation steps),
- feeding upstream output to downstream logic in your **own tools** — bug-bounty and automation scripts —

> "A second command inside a command, maybe a third inside the second — there you HAVE to use command substitution."

## PART B — Arithmetic expansion `$(( ))`

Syntax: **`$(( expression ))`** — the solved result replaces the whole form.

### Vocabulary

- `+` `−` `/` `*` `%` `**` → **operators**; the numbers → **operands**.

### Verified behaviours from the live demos

```bash
echo $((4 + 2))          # → 6
var1=4; var2=2
echo $(($var1 + $var2))  # → 6 (with $ — parameter expansion feeds arithmetic)
echo $((var1 + var2))    # → 6 (WITHOUT $ — arithmetic auto-dereferences names)
```

The no-`$` form is the "nice feature": inside `$(( ))`, bare names are read as variables. His plumbing note: with the `$` form, **parameter expansion runs first** (per the step-3 sequence) and arithmetic receives resolved values.

### Precedence (as demonstrated)

| Expression | Result | Why |
|---|---|---|
| `$((2 + 4 * 3))` | **14** | `*` beats `+` — standard precedence |
| `$(((2 + 4) * 3))` | **18** | parentheses = highest precedence |
| `$((25 ** 2))` | **625** | `**` = exponentiation (`4 ** 2` → 16 stated) |
| `$((5 % 2))` | **1** | `%` = **remainder**, not quotient |
| `$((5 % 3))` | **2** | and note quotient `5/3` would print `2`, never `2.5` |

A precedence-reference link was promised in the Telegram group.

### ⚠ Whole numbers only — and the `bc` escape hatch

**Canonical law (stated as the day's most important point):** arithmetic expansion works **only with whole numbers** — no decimals.

**Live anomaly, honestly preserved:** on *his* shell `echo $((2 + 1.5))` printed 3.5 — because he demos on **zsh**, whose arithmetic is float-capable. He flagged it himself: "in many machines it does NOT work… this shell has an advanced feature." In real bash the same line throws a syntax error. **Lesson for your scripts: never rely on fractional `$(( ))` unless you control the shell; portable code treats it as integers-only.**

### `bc` — the decimal calculator (basic calculator)

- It's a **programming language** unto itself for number work; not installed by default (`bc: not found` → install).
- Interactive demo: `bc` → `2+3` → 5, `5*9` → 45, `quit`.
- **In scripts you don't open the REPL** — you pipe: `echo "EXPRESSION" | bc`.
- Default output is still whole-number — because of the internal variable **`scale`** (controls how many decimal places the output includes):

```bash
echo "5 / 3" | bc            # → 1
echo "scale=2; 5 / 3" | bc   # → 1.66
echo "scale=2; 5 % 3" | bc   # → 2 (remainder shown at scale 2 as "02"-ish display)
```

**Two unbreakable rules:** `scale=` must come **first** (define-then-express; expression-first fails/errors), and the **semicolon is compulsory** — it separates statements inside the piped mini-program.

## PART C — The home tasks (6 objective questions)

Announced up-front "because by the end everyone disappears." Answers due in the **YouTube comment section** before next class; acceptable in Telegram; **best venue promoted: the Defronix Academy LinkedIn page** (public engagement, others benefit). Unanswered questions get solved by him later. All six are strictly from covered material:

1. How would you create a variable with the name …? *(option values not speech-captured)*
2. What does `$…` do? *(one env-var, token truncated — likely `$PS1`/`$PWD`)*
3. What does `$( )` do?
4. Which form shows a parameter's value all in UPPER case?
5. Which shell variable holds the directories the shell searches for executables? — `$HOME` / `$PS1` / `$HOSTNAME` / **`$PATH` ✅**
6. What information does the `$USER` variable contain? — users directory / host name / **current user's username ✅** / person's real name

(With answers to the two recoverable ones flagged ✅ as taught in Days 7-8 classes.)

Strategic frame he gives: these MCQs are the warm-up for **mini-project assignments** — scripts that use command substitution, parameter expansion, brace expansion — "that's how you eventually build your own tools."

## D) Session mechanics worth keeping

- First genuinely **tasked** class: assignments now precede and will outlive live attendance ("answer in the comments even 5 years later — we'll reply").
- Push for seriousness repeated at open: join Telegram; if you're here for time-pass, feel free to leave.
- Portfolio-ish twist: answering on **LinkedIn** = visible participation.
- Format drift acknowledged: next class stretches to 45–50 min for **brace expansion + quote removal** — "short lectures won't cut it for these two."

## E) Pitfall table

| Symptom | Root cause | Cure |
|---|---|---|
| `$((2 + 1.5))` errors / wrong results across machines | `$(( ))` = whole numbers only (zsh's float math made it *look* fine live) | integers in `$(( ))`; decimals via `bc` |
| `echo "5/3" \| bc` → `1` | default `scale` truncates to whole numbers | `echo "scale=2; 5/3" \| bc` → `1.66` |
| bc expression ignored / error | `scale` defined *after* expression or missing `;` | scale first → semicolon → expression |
| `$((var1 + var2))` "shouldn't work" but does | arithmetic auto-dereferences bare names | legal — but `${var1}`+`-style with `$` also fine (param expansion pre-resolves) |
| `bc: command not found` | not installed by default | install it |
| expecting `5 % 3` to give the quotient | `%` = **remainder**; `/` = quotient | use `%` for mod checks (e.g., even/odd tests later) |
| thinking `$( )` is for assignment only | construction works anywhere a value is legal | embed directly: `tar czf backup-$(date +%F).tar.gz ~` (Day-2 pattern) |

## F) Cheat card

```
command substitution : $(cmd)  → cmd's stdout replaces the form
   capture: time=$(date +%H:%M:%S) ; use it in $time later
   mtuf: day-2 backup filename = $(...) in disguise

arithmetic expansion : $(( expression ))  → solved result (WHOLE NUMBERS ONLY)
   operators + - * / % **   operands auto-include vars: $((var1 + var2))
   precedence: () > ** > * / % > + -
   $((2+4*3))=14   $(((2+4)*3))=18   $((25**2))=625   $((5%2))=1

decimals             : bc = basic calculator (a mini language)
   script form : echo "scale=2; 5/3" | bc   → 1.66
   law: scale FIRST, `;` compulsory; interactive bc → quit

tasks  : 6 MCQs in comments/Telegram/LinkedIn(next-class deadline)
next   : longer class — BRACE EXPANSION + QUOTE REMOVAL
```

**Next class (announced):** the stretched 45–50-minute session — finish the expansion tour with **brace expansion**, then unlock pipeline **step-4: quote removal**.
