# Explained — 058 — Day 5: Bash for Bug Bounty (Command Identification + Expansion's Stage Map)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 5 (~45–50 min, whiteboard-only, no terminal). **Curriculum:** Step 2 of the five-step pipeline — **COMMAND IDENTIFICATION** (simple vs compound commands, in full) — then the **Step-3 stage map: shell expansion's four stages and its two non-negotiable order rules**.
**Where you are:** steps done → **1 tokenisation (D4) · 2 command identification (today) · 3 expansion (map today; deep-dive next class) · 4 & 5 to come.** Today's lecture converts yesterday's word/operator tokens into *commands with boundaries*, and installs the ordering law that decides why `echo {1..$x}` betrays you.

---

## Part 1 — STEP 2: COMMAND IDENTIFICATION

### Commands come in exactly two kinds

| Kind | What it is | DNA |
|---|---|---|
| **SIMPLE command** | a command name + its arguments | everyday stuff: `echo`, `ifconfig`, `nmap` |
| **COMPOUND command** | a programming construct | starts with a **reserved word**, ends with its **corresponding** reserved word: `if … fi` |

### How a SIMPLE command is read

After tokenisation has produced **words and operators**, the interpreter reads a simple command as:

```
echo   1   2   3
└─ word-1: the COMMAND NAME (executed)
   └─ every remaining word: ARGUMENTS / INPUTS to word-1
```

First word = command; rest = arguments. Nothing mystical — but *everything* downstream assumes you can mark this boundary without thinking.

### The terminator rule (the day's key law)

> **Every simple command is TERMINATED by a CONTROL OPERATOR.**

Control operators (rerun from D4): `newline  |  ||  &  &&  ;  ;;  ;&  ;;&  |&  (  )`

**"But I type no operator after `echo 1 2 3`!"** — you do. There is an **invisible NEWLINE character at the end of every command line** whose whole job is terminating that command. That's precisely why a bare line at the prompt executes when you hit Enter: you supplied the control operator manually. Keep this model — it makes pipelines (`|`) and backgrounding (`&`) feel like variations, not exceptions.

### The three walk-throughs (do them at a terminal)

**A) Run-on with no control operator — the line does NOT split:**
```bash
echo 1 2 3 echo A B C D     # instructor's run-on probe (no ';' between the two "echo" parts)
```
Tokenisation: 8 words + spaces. But **space is a metacharacter that is NEITHER a control NOR a redirection operator**. Nothing between the two `echo`s qualifies to end command-1, so bash reads **ONE single simple command**: command name = first `echo`, everything else = its arguments. (Observed output: `1 2 3 echo A B C D` — the second "echo" is *data*, not a verb.)
**Reflex to build:** *spaces split WORDS; only control operators split COMMANDS.*

**B) A redirection operator still doesn't split — it gets absorbed:**
```bash
echo $name > out.txt
```
Tokenisation: 3 words (`echo`, `$name`, `out.txt`) + operator `>`. But `>` is a **redirection** operator, not control ⇒ **still ONE simple command**; the operator is adopted *as part of that command* and — his own micro-detail — **performs its task LAST** (build the command, then wire its stdout into the file). Note also: `$` is **not** one of the 10 metacharacters, so `$name` is just another WORD in step 1; the dollar's time comes in step 3.

**C) A semicolon finally cleaves the line:**
```bash
echo 1 2 3 ; echo A B C
```
`;` IS a control operator ⇒ terminator found ⇒ the line becomes **TWO simple commands**, each with its own word-1-name and argument list. Everything you know about `;`, `&&`, `||`, `|`, `&`, and newline is this one law in different costumes.

### COMPOUND commands

> **Definition (verbatim):** *"each compound command STARTS with a RESERVED word and is TERMINATED by the CORRESPONDING reserved word."*
> **Reserved word** = "a word that has a special MEANING to bash."

His skeleton on the board:

```bash
if <condition> ; then
    echo hello world     # simple commands embedded inside
fi
```

- opens with reserved **`if`**, closes with its mate **`fi`** (if backwards — built so bash can spot the end); `then` fences condition from body.
- same family (name-dropped): `while`, `for` — all of them pair-gated.
- **Purpose:** bash's *programming* — conditions and logic. Nobody writes real scripts as "four-five plain simple commands"; compound commands add decisions/loops and **embed multiple simple commands inside**. His compression: *"a compound command is a COMBINATION of compound + simple commands."* (The `[ … ]` test syntax inside `if` is deferred to next class on purpose.)

## Part 2 — STEP 3 intro: SHELL EXPANSION and its four stages

### Where it bolts onto the pipeline

> *"Once the shell has completed TOKENISATION, it will perform SHELL-EXPANSION **on the WORDS** in the command line."*

Expansion operates on **words only** — operators were already spent deciding boundaries (steps 1–2). Whatever `*`'s, `$…`, `{…}`, `~`, `$((…))`, `$(…)` your words contain now get inflated to what they'll really mean.

### The stage map (memorize as a ladder)

| Stage | Expansion | Nickname it answers to |
|---|---|---|
| **1** | **BRACE** expansion | `{1..10}`, `{a,b,c}` |
| **2** | **PARAMETER** expansion — `$name` · **ARITHMETIC** expansion — `$((1+2))` · **COMMAND SUBSTITUTION** — `$(…)` / `` `…` `` · **TILDE** expansion — `~` | four co-equal members, one stage |
| **3** | **WORD SPLITTING** | re-chunking expansion RESULTS at $IFS |
| **4** | **GLOBBING** | `* ? […]` → filenames |

### NOTE 1 — stage order beats left-to-right

> *"Expansions in the EARLIER stages are performed FIRST"* — regardless of where they physically sit in your command. Stage 1 before stage 2 before stage 3 before stage 4, always.

**The trap that makes the law stick:**
```bash
x=10
echo {1..$x}        # you MEANT 1 2 3 … 10
```
Brace expansion (stage 1) fires **before** parameter expansion (stage 2). At brace-time the text is still `{1..$x}` — `$x` is not digits, no valid range, **no brace expansion happens**; the braces stay literal. *Then* parameter expansion replaces `$x` → terminal prints **`{1..10}`**. Intent: right. Stage-coupling: wrong. His verdict, worth owning: **"ye logic GALAT hai."** (Any fix needs the variable resolved *first* — e.g. `eval`, `seq 1 $x`, or a C-style for-loop — lessons for upcoming classes.)

### NOTE 2 — inside one stage: same priority, left-to-right

> *"Expansions in the SAME stage are given SAME PRIORITY and are performed in the ORDER they are FOUND when the command is read LEFT-TO-RIGHT."*

```bash
echo $name $((1+2))          # both stage-2 → left one first: parameter, then arithmetic

echo $name {1..10} $((1+2)) oranges.
# execution order (he quizzes the room on it):
#   1st: {1..10}      ← stage-1 outranks — middle of the line, still FIRST
#   2nd: $name        ← stage-2, leftmost of its stage
#   3rd: $((1+2))     ← stage-2, rightmost of its stage
```

**The combined algorithm** (engrave it):
```
for each expansion found in the line's WORDS:
    sort by STAGE first (1 < 2 < 3 < 4)
    within the same stage, resolve LEFT-to-RIGHT
apply in that order
```

## C) What this lecture is NOT (scoping notes)

- **No expansion deep-dive yet** — today was the map + the two laws; next class is the seven expansions one-by-one, "theory + practical, but mostly practical."
- **No scripts yet** — the five-stage dissection continues to be the price of admission; after the pipeline closes, 2–4 real projects land (per the Day-4 roadmap).

## D) Course/community notes in today's session

- **Announcement:** Defronix launched their **own Android app (Play Store)** — Udemy-style "low-price, quality" courses; **iOS "soon."**
- Attendance dipped to ~4 live; the post-class talk candidly addresses tool-culture ("hand people a magic tool → million views; hand them brainwork → empty chairs") and guarantees the deserters will be back when labs/interviews demand exactly this ("paid mein yahi sikhaayega — Defronix pe free mein hai"). One student-skipped-Linux, labs-broke-him, came-back-with-notes anecdote doubles as the sales pitch for the channel's 15-day Linux course.

## E) Pitfall table (step-2/3 era)

| Symptom | Root cause | Fix |
|---|---|---|
| `echo 1 2 3 echo a b c` prints the second `echo` as TEXT | no control operator ⇒ one simple command; extra words = args | insert `;`/`&&` if you meant two commands |
| output went to a file "early"/confusing partial redirect reasonings | `>` is part of the single simple command; acts **last** within it | model order: words → operator absorbed → command runs → redirect applied |
| `{1..$x}` prints literal `{1..10}` | stage-1 (brace) ran while the value was still `$x` | resolve the variable first (`seq`, eval, arithmetic loop) |
| "why did the left expansion win?" | same-stage = left-to-right | reorder operands if the product depends on it |
| `~`/`$( )` refusing to fire inside single quotes | quoting (D3/D4) kills the characters step-3 needs | leave expansion zones in double quotes / unquoted |

## F) Cheat card

```
STEP 2 — COMMAND IDENTIFICATION
simple command : word-1 = NAME · rest = ARGS · terminated by a CONTROL operator
                 (every line invisibly ends in NEWLINE — that counts)
space          : splits WORDS, never commands       neither-control-nor-redirection
> < >>         : redirection ops → absorbed INTO the one simple command; act LAST
; | & && || newline  : true terminators → next simple command begins
compound       : STARTS with a reserved word · ENDS with its matching one
                 if … fi  (while … done, for … done belong to this family)
               = bash programming = conditions/logic + embedded simple commands

STEP 3 — SHELL EXPANSION (on WORDS only)
stage 1: brace {1..10}
stage 2: $param   $((arith))   $(cmd sub)   ~tilde      ← four, same stage
stage 3: word splitting
stage 4: globbing  *  ?  […]
law 1: lower stage number ALWAYS expands first (position irrelevant)
law 2: same stage → plain left-to-right
demo:  x=10; echo {1..$x}  → {1..10}      (brace beat the dollar by law 1)
```

**Next class (announced):** the full expansion tour — brace / parameter / arithmetic / command-substitution / tilde / word-splitting / globbing, hands-on ("mostly practical").
