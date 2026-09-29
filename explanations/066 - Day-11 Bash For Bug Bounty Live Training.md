# Day-11 — Bash for Bug Bounty (Revision: The 5-Step Command-Line Pipeline) — Explained

## What this session is

After ten days of building the machine piece by piece (Day-3 tokens/words/operators → Day-10 the full expansion stack), Day-11 is the **capstone revision class**: no new material, but the entire model re-condensed and then *exercised* on two commands with the precision the trainer has been promising since Day-1: "what happens to a command line between the moment you press Enter and the moment the prompt returns."

The deliverable is a debugging superpower. His thesis, stated explicitly: most people debug scripts by trial-and-error — shuffle the quotes, try again, it works, move on, never knowing *why*. Once you can mentally replay the **5-step pipeline** — **tokenization → command identification → expansion → quote removal → redirection/execution** — every "mysterious" quote/tilde/splitting bug becomes a deterministic diagnosis at a specific step.

This explanation follows the class structure: (A) the condensed model as revised, (B) Example 1 (the clean trace), (C) Example 2 (the analysis), and (D) why this matters for bug-bounty scripting.

---

## A. The model, re-condensed

### Step 1 — Tokenization
Bash scans the raw line for the **ten metacharacters**: `| & ; ( ) < >` plus whitespace ones — **space, tab, newline**. A metacharacter that sits inside quotes or is escaped ("quoted") does **not** count — the scan works on **unquoted** metacharacters only.

Tokens produced:
- **Word** — a token containing **no unquoted metacharacter** (`echo`, `$name`, `"sachin.singh"` — the quotes make the spaces/dots inside part of one word).
- **Operator** — a token containing at least one unquoted metacharacter. Two families:
  - **Control operators** — `|`, `||`, `&`, `&&`, `;`, `;;`, `;&`, `;;&`, `|&`, `(`, `)`, newline — these *terminate/separate* commands.
  - **Redirection operators** — `<`, `>`, `>>`, `<<`, `<<<`, `<>`… these route streams; they do **not** terminate commands.

### Step 2 — Command identification
- **Simple command** — a sequence terminated by a *control operator*; if none is present, the (implicit) newline terminates it, so the whole line is one simple command.
- **Compound command** — delimited by reserved words (`if…fi`, `for…done`, `case…esac`, `(…)`, `{ …; }`, etc.).

### Step 3 — Expansion, in four fixed stages
| Stage | Expansions | Notes |
|---|---|---|
| 1 | **brace expansion** | `{a,b}` → words |
| 2 | **parameter expansion** `$x`, **arithmetic** `$(( ))` *(time to use `bc` when decimals matter)*, **command substitution** `$(…)`/backticks, **tilde** `~`, `~user` | the big middle stage |
| 3 | **word splitting** | runs **only** on the *unquoted output* of stage-2's parameter/arithmetic/command-substitution results; splits at characters listed in **IFS** (default: space, tab, newline — changeable, e.g. `IFS=.`) |
| 4 | **globbing** (pathname expansion) | scans *words* for **unquoted** `*`, `?`, `[ ]` patterns and substitutes matching filenames |

**Two priority laws** (the class restates them verbatim):
1. An **earlier** stage always wins over a later one, regardless of position on the line.
2. **Within** one stage, equal priority resolves **left-to-right**.

### Step 4 — Quote removal
Remaining **unquoted** `\`, `'…'`, `"…"` that **did not result from an expansion** are stripped. Quotes produced *by* an expansion survive. Quoting trio recap: single quotes kill everything; backslash kills one character; **double quotes kill everything *except* `$` and backtick** — which is why parameter expansion works inside `"…"` but tilde expansion does not.

### Step 5 — Redirection, then execution
Connect stdin/stdout/stderr per the redirection operators, then run the command with the final word list.

---

## B. Example 1 — the clean trace

```
name=Sachin
out=demo.txt
echo $name > $out
```

- **Tokenization:** `echo`, `$name`, `$out` → 3 words; `>` → 1 redirection operator; the 3 spaces are separators. `$` is not a metacharacter — no special role here.
- **Command identification:** no control operator anywhere → **one single simple command**, newline-terminated. (`>` is a *redirection* operator, so it cannot terminate.)
- **Expansion:** no braces; **two parameter expansions** in stage-2 → `echo Sachin > demo.txt`. No arithmetic, no command substitution, no tilde. **No word splitting** (the stage-3 trigger fails: expanded values contain no IFS character). **No globbing** (no unquoted `* ? [`).
- **Quote removal:** nothing to do — no quotes present.
- **Redirection & execution:** stdout rerouted from terminal → **`demo.txt`**; `echo` runs; `cat demo.txt` shows `Sachin`.

Purpose: a "nothing goes wrong" baseline so the broken version's divergence points stand out.

---

## C. Example 2 — the beginner's trap and the perfect fix

**The assignment:** write a script that
1. holds `name="sachin.singh"` (dot-separated first/last),
2. sets `IFS="."` so splitting can happen on dots,
3. **splits** the two names,
4. stores **both parts** in a file `out="output.txt"`,
5. located in the **current user's home directory** — for *any* user who runs it.

Script header:

```bash
#!/bin/bash
IFS="."
name="sachin.singh"
out="output.txt"
```

### Version 1 — what a beginner writes (and why it silently fails)

```bash
echo "$name" > "~/$out"
```

Replay the pipeline:

- **Tokenization:** words are `echo`, `"$name"`, `"~/$out"`; operator `>`.
- **Command ID:** one simple command.
- **Step 3, stage 2:** parameter expansion hits **both** `$name` and `$out` — double quotes do **not** block `$` (only `$` and backtick survive). Result so far: `echo "sachin.singh" > "~/output.txt"`.
  - **But the tilde is dead.** Inside double quotes, every metacharacter/special char loses its meaning except `$` and backtick. **Tilde expansion therefore never happens.** The literal characters `~/output.txt` survive — the shell will try to redirect into a path whose first component is a directory literally named `~`. Aim condition (home directory) **failed**.
  - **Step 3, stage 3 — word splitting:** invoked on unquoted stage-2 outputs only. `"sachin.singh"` is **quoted** → **no splitting** → `sachin . singh` stays one glued word. Aim condition (first/last separated) **failed**.
  - His balancing side-note ("one good thing happened, one bad"): quoting the *target side* was accidentally useful — had the path value contained an IFS character, quotes protected it from splitting. Quoting is not inherently wrong; selectively it is.
- **Step 4:** the quotes are hand-written and unquoted themselves → quote removal would strip them, leaving literal `~/output.txt`.
- **Step 5:** redirect succeeds into the wrong place with an unsplit payload.

### Version 2 — the perfect code

```bash
echo $name > "$HOME/$out"
```

The two surgical changes, both justified by the model:

1. **Drop quotes around `$name`** → stage-3 word splitting now *legally* applies to the parameter-expansion output, sees IFS=`.`, and produces the two words `sachin` `singh`. Aim #1 met.
2. **Replace `~` with `$HOME` inside the quoted path** → tilde expansion is stage-2 and quote-sensitive, but **parameter expansion works inside double quotes**, so `"$HOME/$out"` correctly becomes `/home/kali/output.txt` (or any user's home). Bonus: `$HOME` is a system-defined variable per-user — the script becomes portable ("works wherever you run it; the home dir is the one place with guaranteed permissions"). Aim #2 met, portably.
3. Keeping the **quotes on the path side** blocks word splitting from ever tearing the path apart (even if a home path contained spaces — a real-world robustness point the class gestures at).

Final replay of the fixed line:
- Stage-2 → `echo sachin.singh > "$HOME/output.txt"` → **$HOME expands** → `/home/kali/output.txt`.
- Stage-3 word splitting: `sachin.singh` splits on `.` → **two words**; the path arm is quoted → untouched; **no globbing** (no `* ? [`).
- Step-4 quote removal: the arm's quotes are user-written and unquoted → **removed**.
- Final pre-execution words: `echo  sachin  singh  >  /home/kali/output.txt` → step-5 redirects → file written exactly as the aim demanded.

---

## D. Why this matters for the course (and for you)

1. **Deterministic debugging.** Every quote/tilde/split/glob weirdness maps to one stage of the pipeline. When output is wrong, ask in order: Is the token boundary where I think? Did a control operator split my command earlier than I assumed? Which expansions fired at stage-2, and were they quoted? Did IFS bite something? Did a glob pattern leak through unquoted? Were my quotes hand-written (removable) or expansion-produced (kept)? Was the redirect target what I thought?
2. **The three classic beginner bugs, revisited mechanically:**
   - `~`-in-quotes → dead literal `~` (fixed with `$HOME` or unquoting just the tilde),
   - losing word-splitting when you *wanted* it (unquote the expansion),
   - gaining word-splitting when you *didn't* (quote the expansion or sanitize IFS).
3. **Bug-bounty scripting context:** loops that batch-run tools over `$subdomain`, `grep "$pattern" "$f"`, output routed with `> "$BASE/$out"` — every single line of that everyday recon scripting runs through this exact pipeline. The difference between a one-liner that silently corrupts filenames (spaces in paths!) and one that just works is precisely stage-3/stage-4 literacy drilled today.
4. **His promised payoff:** "one extra debugging power" — after today, when a script misbehaves, you no longer google-and-guess; you walk the five steps.

## Key exam-capable facts restated

- Metacharacters (10): `| & ; ( ) < >`, space, tab, newline.
- Word = no unquoted metacharacter; operator = ≥1; operators = control vs redirection.
- Simple commands end at **control operators**; `>` never terminates a command.
- Expansion stages: **brace → (parameter / arithmetic / command-sub / tilde) → word splitting → globbing**; earlier stage beats later; ties break left-to-right.
- Word splitting: only on **unquoted** outputs of parameter/arithmetic/command-substitution; cutting list = **IFS** (default space/tab/newline).
- Glob patterns `* ? […]` must be **unquoted**; applied to words.
- Double quotes preserve **`$`** and **backtick** only — hence tilde dies in `"~"`, but `$HOME` thrives.
- Quote removal strips **unquoted, hand-written** quotes only — never expansion output.
- Environment variable **`$HOME`** = portable home-directory (use it in scripts, not `~` inside quotes, or any hard-coded `/home/kali`).
