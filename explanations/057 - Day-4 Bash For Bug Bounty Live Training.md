# Explained — 057 — Day 4: Bash for Bug Bounty (Quoting Redone + Tokenisation, Step 1 of 5)

**Source:** Defronix Bash-for-Bug-Bounty live training, Day 4 (~45 min, full session). Day-3 died mid-demo to a Wi-Fi collapse, so Day-4 has two halves: (1) **quoting — theory replayed + the practicals finally executed live**, (2) the first of the **five pipeline steps dissection: TOKENISATION**.
**Why this class matters most so far:** everything before said *"bash reads each line in a five-step process."* Today you learn where step 1 lives and that it's *governed by quoting* — i.e., the two previous classes were laying rails for this one. Do the unmanaged-metacharacter demos beside them and three days of fog condense into one sentence: **bash splits your line at UNQUOTED metacharacters, and quoting decides which character is still a metacharacter.**

---

## PART A — quoting, the day it finally worked on camera

### Theory (one-breath recap, now normalized as rules)

| Mechanism | Rules of engagement |
|---|---|
| **Backslash `\`** | kills the special meaning of **the very next character only** |
| **Single quotes `'…'`** | kill the special meaning of **every character inside — no exceptions** |
| **Double quotes `"…"`** | kill everything inside **except `$` (variable expansion) and `` ` `` (backtick command substitution)** — *plus flexibility:* a `\` **inside** double quotes can still kill even `$`/`` `  `` selectively (so expansion and literalness can coexist in one string) |

Vocabulary from Day-3 formalized: a character with its meaning removed is **quoted/escaped**; untouched, it's **unquoted**. Keep those two words — step 1 is built *on* them.

### Demo 1 — the ampersand, executed

```bash
echo Sachin & Nitesh        # bash: run `echo Sachin` in BACKGROUND, then run `Nitesh` → command not found
echo Sachin \& Nitesh       # → prints: Sachin & Nitesh
```

`&` = "run preceding command in background" (Linux-class flashback). The backslash rescue re-proven live at last.

### Demo 2 — the Windows-path trap (the day's real teaching)

Goal: store `C:\Users\Nitesh\Documents` in a variable.

```bash
file_path=C:\Users\Nitesh\Documents      # WRONG — each \ escapes the NEXT char; the slashes VANISH
echo $file_path                          # → C:UsersNiteshDocuments   (slashes consumed)
```

**Diagnosis he leads the class to:** the backslash itself is a special character with its own special meaning — if you want it printed literally, its meaning must be *removed too*.

**Fix A — fight it character-by-character (hard mode):**
```bash
file_path=C:\\Users\\Nitesh\\Documents   # every real \ doubled
```

**Fix B — the beginner-grade solution (his explicit recommendation):**
```bash
file_path='C:\Users\Nitesh\Documents'    # single quotes = vault; nothing inside means anything
```

His anti-`\\` argument is reputational: a **long path or long command + lots of backslash juggling** is "a hard part — a hectic part — beginners confuse, errors generate." Single quotes relocate the burden from "get N escapes right" to "wrap once, forget."

### Demo 3 — mixed quoting (the requirement split, live)

Now automate the username. Try the obvious single-quoted upgrade:

```bash
file_path='C:\Users\$USER\Documents'     # $USER stays LITERAL — vault froze the dollar too
echo $file_path                          # → C:\Users\$USER\Documents   (Nitesh would be — nobody)
```

Single quotes can't serve two masters. **Move to double quotes** (the dollar lives there), then re-protect the backslashes inside via the flexibility rule:

```bash
file_path="C:\\Users\\$USER\\Documents"  # double-quoted: \$ would also be killed if you wanted that
echo $file_path                          # → C:\Users\ROOT\Documents   (his user = root)
```

On stream he debugs *with the audience* ("does anyone in chat see why?") before landing it — implementer's reproduction of the mechanics:

- `"` zone: `$USER` **expands** → `ROOT` ✔
- still `"` zone: bare `\` before a *non-special* next char stays literal for *echo-printing*, **but** to be parser-safe inside the assignment he double-escapes the intentional backslashes (`\\`) → single `\` survives ✔
- the `\`-inside-`"…"` clause is also how you'd *kill* a dollar if needed: `"cost: \$5, user: $USER"` → `cost: $5, user: root`.

**The generalized rule (worth the whole lecture):** *decide per fragment* — single-quote what must stay dead-literal (Windows paths, regex, URLs with `&`), double-quote what must expand (`$USER`, `$TARGET`), and use `\` inside double quotes to settle individual disagreements. That *is* the "powerfulness affect every part" they're promised to feel until the series ends.

## PART B — Step 1: TOKENISATION

### The what, in his definitions

- **Metacharacters** — bash's own punctuation set: in his words, *"certain metacharacters that ALLOW IT [bash] TO BREAK UP a command-line INTO CHUNKS KNOWN AS TOKENS."*
- **Token** — *"a SEQUENCE OF CHARACTERS … CONSIDERED AS A SINGLE UNIT BY THE SHELL."* The atom of everything after step 1.
- **Tokenisation** — *"the command is divided into chunks on the basis of metacharacters — the chunks we call tokens."*

### The TEN metacharacters (written out, highlighted, worth memorizing in order)

```
|  &  ;  (  )  <  >  SPACE  TAB  NEWLINE
```

Every edge in your command line is one of these. Note carefully what is *absent*: letters, digits, quotes themselves (quotes work earlier/differently — Day-3's mechanism operates *inside* the scan), `$`, `*`, `\` — those are *expansion-era* citizens, not line-splitters.

### The scan — the crucial qualifier

Bash's first pass finds token boundaries **"ON THE BASIS OF UNQUOTED METACHARACTERS"** — his emphasis repeats three times:

- A **quoted** metacharacter (e.g. `\&`, or `&` inside `'…'`) is **transparent to the splitter** — it contributes ZERO token boundaries; it merges into the surrounding word.
- An **unquoted** metacharacter **breaks the line** — this is the first exact case where yesterday's "quoted/unquoted" vocabulary gets weaponised; his line: *"getting my point? — on the basis of UNQUOTED meta-characters."*
- This pass is only a **rough idea** (his words) — boundaries located, not yet meanings assigned.

### The sorting — WORDS vs OPERATORS

The rough tokens then fall into **two categories**, defined with the very same adjectives:

- **WORD** — a token containing **not even ONE unquoted metacharacter**. (Commands, arguments, filenames, values.)
- **OPERATOR** — a token containing **AT-LEAST-ONE unquoted metacharacter**. (The glue that decides *what is done* with the words.)

### Operators split again: CONTROL vs REDIRECTION

**Control operators** — "they **process / control your commands**" (sequencing, backgrounding, logic, grouping):

```
newline   |   ||   &   &&   ;   ;;   ;&   ;;&   |&   (   )
```

**Redirection operators** — "where does the output **GO** — the terminal, a file, or another command's **input**?":

```
<   >   <<   >>   <&   >|   <>   >&      (stream list per his reading; adjacent forms follow in step-5's class)
```

### The unifying punchline (don't miss it)

> *"Notice something — chahe control operator ho chahe redirection — saare ke saare KISSE bane hain? — META-characters ki help se — **those very TEN**."*

Everything bash ever does to your line is negotiated through the same 10-char alphabet — and since quoting controls which of those chars are *visible*, **quoting controls every subsequent step of the pipeline**. This is the promised loop back: Day-3 taught the tool, Day-4 showed you the machine it drives. His final recap in one breath: *tokenise by unquoted metacharacters → sort into words and operators → operators split into control/redirection → then the task is decided/formed*. Steps 2–5 hang directly off this foundation.

## C) What's deliberately NOT here today

- **No step-1 *practical*** — by design, not truncation: practicals arrive as walking-through-the-pipeline exercises from **step 2 (command identification — next class, "chhota sa, then step-3 starts")** onward; each later step's example goes *"yahan tokenisation hua, yahan expansion, ab step-4…"* — the five lenses are always worn in order. Final full revision: 2–3 examples through **all five steps** once complete.
- **Consequence he makes explicit:** with the pipeline habit, error chances crash ("ERRORs hone ke chances bahut kam honge — tum paanch nazar se apni line dekh loge").

## D) Housekeeping & course map (fresh today)

- Post-class **doubt window = 5 minutes, topic-related only**, solved live; off-syllabus → other classes/courses exist for that. One silent minute = dismissed. (Bye-bye — good-night.)
- Day-3's aborted demos are **fully re-executed**, so losing nothing from the Wi-Fi cut; the font was enlarged "clear even on PHONE screens" — audience reality = mobile viewers.
- **Roadmap spoken aloud:** after the 5 steps → *"asli cheez"* — loops (`for`, `while`), arrays, "bahut kuch", ending in **2–4 real projects** with his design-method walkthrough ("kaise hum project design karte hain"). NetSec readers: these bash classes are queueing up to automate exactly your nmap/NSE recon chains.

## E) Pitfalls formally diagnosed across the two classes

| Symptom | Cause | Cure |
|---|---|---|
| `command not found` on a random word | unquoted `&` / `;` split your line | `\&`, or quote the whole string |
| variable stores a mangled path | backslashes *are themselves* escape-characters | `\\…` or single-quote the literal |
| path with username must auto-fill but prints `$USER` | single-quote vault froze the expansion zone | double quotes (+ `\\` for slashes) |
| "special meaning" bleeding somewhere at all | none — an unquoted metacharacter did its day-job | audit line *as* bash will: which meta is visible unquoted? |
| **foundational** | skipping the rough-idea step's quoting dependency | read every line in the five-step order; decide quoting deliberately |

## F) Cheat card

```
QUOTING (final form):
  \        one-char sniper                     echo Sachin \& Nitesh
  '..'     vault — everything dead             file_path='C:\Users\x\Documents'
  ".."     everything dead except $ and ` `    echo "C:\Users\$USER\D"
           + inside it:  \$ \` \" \\  still killable by backslash
  quoted/escaped = meaning removed · unquoted = meaning ACTIVE

STEP-1 TOKENISATION:
  metacharacters (10):  |  &  ;  (  )  <  >  space tab newline
  shell splits at UNQUOTED ones → rough tokens
  token   = sequence of chars the shell treats as ONE UNIT
  WORD    = token with ZERO unquoted metacharacters
  OPERATOR= token with ≥1 unquoted metacharacter
    CONTROL     : newline | || & && ; ;; ;& ;;& |& ( )      ← process/flow
    REDIRECTION : < > << >> <& >| <> >&                     ← where output goes

golden loop: every operator is BUILT from the 10 ⇒ quoting governs ALL later steps
```

**Next class (announced):** Step 2 — **command identification** ("it's a small one — so step 3 starts the same day"): what a *command name* vs. an argument is, how aliases/keywords/functions/builtins/PATH participate, and from there the pipeline-walks begin in earnest.
