# Day-13 — Bash for Bug Bounty ($@ / $* / read / select) — Explained

## Position in the course

Day-13 finishes the **"how does a script get user input?"** section. The full arc now looks like:

| Mechanism | Input style | Covered |
|---|---|---|
| Positional parameters `$1…${n}` | arguments on the command line | Day-12 |
| Special parameters `$#`, `$0` | introspection of the invocation | Day-12 |
| Special parameters `$@`, `$*` | **all** arguments at once | **today** |
| `read` (+ flags) | interactive typed input | **today** |
| `select` (+ `PS3`) | interactive menu choice | **today** |

Next section (Day-14 onward, after the three assignments): **logic** (`if`), then loops, then projects.

## 1. `$@` and `$*` — the whole argument list in one word

Both expand to **all positional parameters at once**. The behavior splits into a 2×2 grid — this is THE exam table for the day:

| Expansion | Result | Word splitting? | Each arg survives as… |
|---|---|---|---|
| `$@` (unquoted) | `$1 $2 $3 … $n` rejoined like any unquoted expansion | **yes — each result word split individually** | nothing guaranteed; multi-word args get shredded |
| `"$@"` | `"$1" "$2" "$3" … "$n"` — **each arg individually quoted** | no | **one word per argument — always exact** |
| `$*` (unquoted) | like unquoted `$@` | yes | same shredding |
| `"$*"` | `"$1<sep>$2<sep>$3…"` — **ONE single word**, separator = **first char of IFS** (default space; e.g. `IFS=,` → `"1,2,3,4"`) | no | one glued string |

His demos make each quadrant concrete:

```bash
echo $@                 # args 1 2 3 4 → prints "1 2 3 4"
touch $@                # creates four files: 1 2 3 4
# script: touch $@ ; invoked: ./s.sh "daily feedback" "monthly reports"
#   → creates FOUR files: daily feedback monthly reports   (unquoted shred)
# script: touch "$@" ; same invocation
#   → creates TWO files: "daily feedback" "monthly reports" (exact)
IFS=, ; touch "$*"      # args 1 2 3 4 → creates ONE file literally named: 1,2,3,4
```

**Rule of thumb:** looping or forwarding args? Use `"$@"` (99% of real code). Need one CSV-ish string? `"$*"` with a chosen `IFS`.

## 2. The assignment — calculator v2 (now with unlimited args)

Spec shown on screen, to be attempted before Day-14: rewrite the Day-12 calculator **replacing positional parameters with special parameters**, so that it (a) works on an **unlimited amount of numbers** instead of the `${2:-0}`…`${10:-0}` ceiling, and (b) can take **more than one operator** between numbers. Conceptually: `echo $(( $* ))` (arg string `$1+$2+$3…` arrives wholesale as arithmetic text — that's why multiple *different* operators now work for free) — the exact solved form comes next class. The pedagogical point stands alone: `${n:-0}` scaffolding was brute force; special parameters make it general.

## 3. `read` — interactive input with guard rails

`read` pauses for a line of input and stores it in a variable.

```bash
read                      # value lands in default var $REPLY
read input1 input2        # space-separated words split across named vars
read name age town        # scripted form
```

Flags demoed (the everyday trio):

| Flag | Effect | Gotcha shown in class |
|---|---|---|
| `-p "Input your first name: "` | inline prompt text (critical UX: otherwise the script just sits there "blank") | without a prompt the user can't know what/when to type |
| `-t 5` | timeout in seconds — after it, read returns, variables stay empty, script continues | paired with defaults elsewhere (e.g. `${var:-0}`) this is "important script must not hang"; his timed-out fields printed empty, which is exactly the behavior to design for |
| `-s` | silent/secret — no echo (passwords; the "dots or nothing" feel of real tools) | put a `echo` after it for a newline, since the user's Enter isn't echoed either |

Pattern worth keeping from the session: friendly front-end = `read -p`; robust front-end = `read -t` + a default; secrets = `read -sp`.

## 4. `select` — instant menus

```bash
#!/bin/bash
PS3="What is the day of the week? "
select day in Monday Tuesday Wednesday Thursday Friday Saturday; do
    echo "The day of the week is $day"
    break          # without this, select loops forever
done
```

Mechanics as taught:

- `select NAME in WORDS… ;` — `in` is **reserved and compulsory**; the space-separated words after it are the menu; the **semicolon ends the option list**.
- User sees a numbered menu (`1) Monday 2) Tuesday …`) and a prompt; they answer with a **number**; the chosen **string** lands in `$NAME`.
- The body between `do` and `done` runs per selection — per-choice logic/conditions go here (each option can have its own branch).
- **`select` loops forever** — exit via Ctrl-C or an explicit `break`.
- **`PS3`** — the reserved prompt variable *for select only*: default is `#?`; set it before the select for a friendly prompt. (Precision footnote to his wording: PS3 stores the *prompt text*; the typed number actually arrives via **`REPLY`**, and bash maps it to the option string that lands in your variable.)
- The explicit parallel he draws: this is exactly the `msfconsole`-style numbered menu UX ("just a number and the selection happens") — now buildable in 6 lines of bash.

## 5. Why this matters for bug-bounty tooling (the connective tissue)

- **Wrapper scripts** that just forward arguments to a tool chain: `subfinder $domain && httpx "$@"` — forwarding **must** be `"$@"` or any quoted argument the user passed (a filename with spaces!) explodes.
- **Menus for internal tools**: pick a target profile, pick a scope file, pick scan intensity — `select` + `PS3` + `break` is the whole implementation.
- **Prompted runs**: `read -p "Target domain: " d` plus `read -t` timeouts for cron-driven recons that should continue unattended with defaults.
- The small-mistake sermon (his mid-class monologue): real-world breakage is overwhelmingly things like IFS=` ` vs `,`, quoted vs unquoted `$@`, a missing `-t` on a hung prompt — all of them sitting in today's table.

## Cheat card

- `$@`/`$*` unquoted: same — all args, each word re-split.
- `"$@"`: each arg its own word — **choice #1 for iteration/forwarding.**
- `"$*"`: ONE word, args joined by first char of `IFS` — the CSV maker.
- `read`, `$REPLY` default; `read a b c` splits; `-p` prompt, `-t` timeout, `-s` silent.
- `select x in … ; do … done` = numbered menu; loops by default → `break`; `PS3` = its prompt string; typed choice enters as number via `REPLY`, string lands in `$x`.
- Assignment due Day-14: calculator v2 on special parameters — unlimited numbers, mixed operators.
