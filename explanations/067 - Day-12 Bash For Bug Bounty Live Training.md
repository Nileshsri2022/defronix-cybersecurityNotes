# Day-12 — Bash for Bug Bounty (Positional & Special Parameters) — Explained

## Where we are

Day-11 closed out the "how bash *reads* a command line" half of the course. Day-12 opens the **scripting half**: from now on it's "mostly practical" — build scripts topic by topic, applying the Day-3→11 machinery. The first scripting superpower: **making a script that accepts input from its own command line, like every real tool does.** That requires two things, which are exactly today's two topics:

1. **Positional parameters** — how a script *receives* arguments (`$1`, `$2`…).
2. **Special parameters** — how a script *introspects* its own invocation (`$#`, `$0`, and more to come).

The mental hook he gives: when you run `nmap -sV -Pn --script … target`, *the tool knows* which flag carries which value. That knowledge must be implemented somehow — in shell scripts, the implementation *is* positional parameters.

## 1. Positional parameters — the mechanics

**Definition (as dictated):** *the shell assigns numbers — called positional parameters — to each command-line argument that is entered.* The script name itself is the command; each space-separated word after it becomes `$1`, `$2`, `$3` … automatically.

Given `./pos.sh sachin $HOME red`:

```bash
#!/bin/bash
echo "My name is $1"              # → sachin
echo "My home directory $2"       # → /home/kali  ($2 held the string $HOME, expanded)
echo "My favourite color is $3"   # → red
```

Four properties, each demoed:

| Property | Meaning | Demo |
|---|---|---|
| **Auto-defined** | You never declare them; the shell creates and fills them per invocation. Just pass space-separated values. | whole demo |
| **Numeric & reserved** | They live in the number namespace; **you cannot assign to them.** | `$1=john` → `command not found` (bash parsed `1=john` as a *command name*, since `$1` expanded to empty and no such command exists) |
| **Unbounded** | No cap — two or two hundred, as many as the script's design needs. | Q&A in class |
| **Brace rule ≥ 10** | `${10}`, `${11}`… require curly braces. | `$11` printed **`sachin1`** — bash read `$1` (=`sachin`) then the literal character `1` |

That last pitfall deserves emphasis because it's the day's first "gotcha the 5-step pipeline explains": during *parameter expansion*, bash takes the **longest valid simple name after `$`** — a single digit — so `$11` is `${1}1`. The braces exist precisely to say "the parameter name is `11`". Same family as `${var}_suffix` vs `$var_suffix` later in scripting.

## 2. The `${parameter:-word}` safety net — "default value" expansion

Parameter expansion has assignment-free fallback forms. The one used today:

```
${parameter:-word}
```

> If `parameter` is **unset or empty**, the expansion yields `word` instead. (`parameter` itself is *not* modified; the value is just substituted inline.)

Why it matters: a calculator over *empty input* is never meaningful — if the user supplies fewer arguments than the script references, bare `$7` expands to nothing and the arithmetic line `5 + + 3` becomes a syntax error. With `${7:-0}` the missing slot silently becomes `0` — an identity element that "runs through with default settings without affecting the result," in his words. For **+** and **−**, `0` is the safe default (多加不减). (For **×** the true identity would be `1`, and for **÷** you can't default — that's why this class restricts the demo to +/−.)

This is the first taste of **defensive scripting**: *decide the default*, don't trust the user to always provide complete input.

## 3. Worked assignment — the 10-argument calculator

Spec (read aloud): bash script = basic calculator; arithmetic from the command line; supports addition/subtraction(/multiplication/division later); **max nine numbers** (0–9); **first argument is the operator**; chosen operation applies across all numbers; total ≤ **ten** command-line arguments.

The built script, `calculator.sh`:

```bash
#!/bin/bash
echo $(( ${2:-0} $1 ${3:-0} $1 ${4:-0} $1 ${5:-0} $1 ${6:-0} $1 ${7:-0} $1 ${8:-0} $1 ${9:-0} $1 ${10:-0} ))
```

Read it inside-out:

- **`$1`** appears between every pair of terms — it's the operator (`+` or `-`). Positional params expand *inside* arithmetic expansion, so `$((…))` ends up evaluating e.g. `7 + 9 + 5 + 0 + 0 + 0 + 0 + 0 + 0`.
- **`${2:-0}`…`${10:-0}`** — the nine number slots, each defaulting to 0. Only three given? Six harmless `+ 0`s close the chain.
- **No conditionals, no loops** yet — it's deliberately brute-force long-form. He explicitly forecasts: "later this length automatically shrinks" (loops, Day-x).

Demo runs:

```bash
chmod 744 calculator.sh
./calculator.sh + 7 9 5   # → 21
./calculator.sh - 9 5     # → 4
```

Walking the first invocation through expansion (his on-screen trace): `7`, `+`, `9`, `+`, `5`, then since args 4–10 were never given, each `${n:-0}` collapses to `+ 0 … + 0` → 21. And `${10:-0}` — note the **braces + default form compose freely**, pairing both of today's rules in one token.

## 4. Special parameters — `$#` and `$0`

**Definition (as dictated):** *parameters to which bash gives a special meaning.* Like shell variables, but with one inversion: **their values are computed FOR you — "based on what is happening or has happened in the current script" — and you cannot change them.** Two consequences he draws: (a) they're situation-reactive **shortcuts**, and (b) they're trustworthy — since no one (not even a buggy line in your own script) can overwrite them, their reading is always **accurate**.

### `$#` — argument count
Expands to the **number of positional parameters** given. Append `echo $#` to `pos.sh`, run with 11 args → prints `11`; add two more → `13`. Uses: arity checks, loop bounds, detecting "ran with no input".

### `$0` — invocation name
Deliberately "weird/flexible": *where* you use it decides what it means.
- At an interactive prompt, `echo $0` → the **current shell** (`bash` / `-bash`).
- Inside a script → **the name the script was invoked with** (`./pos.sh`).

Proof of liveness, his `mv` trick:

```bash
mv special.sh veryspecial.sh
./veryspecial.sh one-arg        # usage line now prints:
# Usage: ./veryspecial.sh { file1 file2 }
```

The usage string updated itself because `$0` is not a baked constant — perfect for self-describing error messages in tools that get renamed, symlinked, or wrapped. (Sneakily, this is also why `$0` is the base of *arg 0 poisoning* trivia and why setUID wrapper lore references it — not his point today.)

### The usage-message pattern — `$#` + `$0` combined

```bash
#!/bin/bash
if [ $# -ne 2 ]; then
    echo "You didn't enter exactly two parameters"
    echo "Usage: $0 { file1 file2 }"
    exit 1
fi
```

Behaviour: `./special.sh 1 2` → silence (falls through, no body yet); `./special.sh 1` → the error + usage, exit status 1. This **is** the mechanism behind every "Usage: tool <opts>" you ever triggered by fat-fingering a flag — and now you can build it deliberately. The `if [ … -ne … ] … fi` syntax is intentionally used-today/explained-next-class (Day-13 territory), as is `exit 1` (error-state exit status).

## 5. Pitfalls & cheat card

| # | Mistake | Symptom | Fix |
|---|---|---|---|
| 1 | `$11` for the 11th arg | prints `${1}` + literal `1` (`sachin1`) | `${11}` — braces mandatory ≥10 |
| 2 | Trying `$1=…` to override | `command not found` | you *can't*; copy into your own var if needed (`x=$1`) |
| 3 | Referencing args the user might skip | empty slots → broken arithmetic / dangling tokens | `${n:-default}` |
| 4 | Hard-coding your script's name in usage text | wrong help after rename/symlink | `"Usage: $0 …"` |
| 5 | Assuming arg count | script misfires silently | gate with `if [ $# -ne N ]` |

**One-liner recall:**
- Positional params = auto-numbered args (`$1…${10}…`); reserved, read-only, unlimited.
- `${p:-w}` = "if empty, use `w`."
- `$#` = how many args; `$0` = who am I (shell at prompt, script name inside); both read-only, computed live.
- Pattern: `$#` guards the gate, `$0` names the tool in the usage line — the exact UX every CLI tool gives you.
