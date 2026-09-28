# Explanation — 035 — Day 7: Capstone Project — The Random Question-Paper Maker

**Source:** `transcripts/035 - Day-7 Python For Cyber Security Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/035 - Day-7 Python For Cyber Security Free Live Training Capsule Course.md`
**Level:** Beginner→Intermediate Python, finale. One full project built live, end-to-end, whose *only* purpose is to force every Day-1…6 concept into one program — plus the deliberate decision to leave a known bug as homework.

---

## 0. What this class is

The graduation build. Rather than a hacking tool (poll debate from Day 6: sockets need networking not yet taught; Windows Defender eats live-built offensive tools), the selected project is a **Randomized Question-Paper Maker** — justified as "boring-sounding but concept-complete." The trainer frames it as deliberately humble: *"this is the LOWEST project — I wrote this in class 11; I'm in second year now"* — inviting students to imagine (and request) bigger builds.

Real-world motivation explained at the whiteboard: in online exams with no invigilation, distributing *one* common paper makes cheating trivial; with a question bank of 100 and randomly different sets per student — **even the person generating the papers cannot predict the contents** — the cheating channel collapses. "Unique" is insisted on as brand: normal makers have been done; "we are Defronix."

## 1. Requirements engineering (fast, but real)

| Requirement | Source | Design consequence |
|---|---|---|
| Enter questions **manually** | client (imagined) | input loop with exit control |
| Accept a **file** of questions too | client | Day-5 file handling; read mode by default, `rb` for images → error-aware |
| Generate **multiple sets** | client | outer loop over set count → one output file per set |
| Anti-cheating randomness | problem domain | `random` library over a bank |
| Marks-categories (1,2,3,4,5,10) | conventional papers | dict-of-lists bank keyed by category |
| Minimise user friction | trainer's UX rule | **"the less you ask the user, the better"** — only set-count is asked up front; categories/totals are self-defined |

## 2. System design (whiteboard → code)

### 2.1 The bank
`question_bank = {}` — a **dictionary keyed by mark value**, each value a list of question strings: `{1:[…], 2:[…], 3:[…], 5:[…], 10:[…]}`. The dict is chosen *because* position-by-category is exactly what the selection phase needs; it revises Day 3 in production.

### 2.2 The interface (input phase)
- A **`while` menu loop**: *"enter a question? press 1 — anything else exits."* Any key ≠ 1 breaks — simple, forgiving.
- Then *"how many marks' question?"* → appends the typed question into `question_bank[marks]` via `list.append` (Day 2) — or ingests a whole file's lines into the right bucket (`f.read()` / split, Day 5).
- All user-facing risk wrapped in **`try/except` with the exception captured into a variable** (Day 6 doctrine: never die in front of users; print the error later in the flow).

### 2.3 Refactoring mid-build: `let_que_take(question_bank)`
The per-category "ask and append" code starts duplicated across the six mark-values; the trainer extracts it into **one function**, then hits the *scope wall* honestly: variables created inside a function are **local** — the bank must arrive as a **parameter** (or be made global). That's Day 6's argument/parameter lecture firing for real in Day 7. Editor tip dropped along the way: **Shift+Tab bulk-unindents** a block after extraction ("don't backspace line by line — hold Shift").

### 2.4 The selection phase
For each category c: **ask "how many c-mark questions?" only when `len(bank[c]) > 0`** — no point asking for 2-mark picks when no 2-mark questions were entered. And the confession-bug:

> He first wrote an `if/elif/elif…` chain — only ONE branch can ever run — so most categories silently got skipped. The fix: **independent `if` blocks** (each category must be checkable). Moral taught transitive-property style: *"if a=b and b=c then a=c — you read this till the 10th"* — equal conditions need equal ranking, not an else-if ladder.

### 2.5 Totals
```python
total = q1*1 + q2*2 + q3*3 + q4*4 + q5*5 + q10*10
if total > 0:      # otherwise the user entered nothing and quit — don't emit an empty paper
    generate()
```

### 2.6 Generation
- For each set (loop over the requested count): compose the paper — institute header **center-aligned by jugaad** (`f.write(" "*N + title)` — "Python ships no centering; we're jugaadu people"), set number, total marks, then section headers ("Following are 1-mark questions: …") with the **random picks** written under each.
- `import random` — **pick a random element from a list** (`random.choice`-style) — the trainer uses only this one facility and assigns the *rest of the library as research*.
- `f.close()` called out for hygiene after each write.

### 2.7 The live failure → the homework
On the demo run, **the same question landed in both sets** — random sampling *with replacement*. The trainer narrates the fix but deliberately **does not type it**:

> Keep a `selected` list. For every new pick: `if pick not in selected:` → write it + `selected.append(pick)`; else re-pick — possibly inside `while True:`. Also guard the pathological case: requesting more questions from a category than the bank holds (asking 11 of 10) — "I know exactly which flaws remain in my program; completing them is your work."

This is the same pedagogy as Days 22–24's withheld set-topic: the last 10% is the part that teaches.

## 3. Concept-coverage audit (why this project was really chosen)

| Day | Concept | Where it fires in the build |
|---|---|---|
| 1 | `print`, input/cast | the whole menu |
| 2 | lists, `append`, `len` | bank buckets + selection guards |
| 3 | dict, key access, `in` | `question_bank[marks]`, `pick not in selected` |
| 4 | `while`, `break`, independent `if`s, comparisons | menu loop, per-category guards, the elif-bug lesson |
| 5 | `open`, modes, read/write, `str()` casting for writes | file ingestion + paper files |
| 6 | functions, parameters vs locals, try/except-with-captured-error | `let_que_take`, every protected block |
| (new) | `random` | selection engine (rest = homework) |

The trainer says the quiet part aloud: *"nothing in this is actually new — that's why I pushed this project hard: every single earlier thing is getting revised."*

## 4. Homework & course close

1. **Study the whole `random` library** (beyond the one function used) and report.
2. **Implement the no-duplicates fix** + close the remaining known flaws (e.g., over-request guard); post code/screenshots or a Google-Drive link under the **Day-7 LinkedIn post**. Protocol: attempt first → show your attempt on Telegram → *then* get the block.
3. **7-day feedback poll** on Telegram — good response ⇒ a next course (another language or development), plus the standing offer: request any tool "that doesn't exist anywhere," and Defronix will try to build it. Candid production note: Day 1 was rushed (he was unwell), smoothed out from Day 2. Sign-off: "Jai Hind, Vande Mataram."

## 5. Concept map

```
Bank         : question_bank = {1:[…], 2:[…], …}   (dict keyed by marks)
Input        : while menu (1=add, else break) → category → append · or file-ingest (r / rb)
Protection   : try/except → store error in e → print human line → program LIVES
Refactor     : let_que_take(question_bank) — locals are local: PASS it in (Shift+Tab to dedent)
Selection    : per-category ask ONLY if len(list)>0 — independent ifs, NOT an elif chain!
Totals       : Σ(qi × i) — total>0 guard before generating
Generation   : random pick from category list → write paper file per set (space-padded centering = jugaad)
Known bug    : same question in two sets ⇒ selected-list + not-in + re-pick (HOMEWORK, by design)
Homework     : (1) random library, (2) implement fix + flaw-guards → Day-7 LinkedIn comments
```

## 6. Self-check prompts

1. Why was a **dict** (not a single list) chosen for the question bank, and what does its key encode?
2. Reproduce the `if/elif` bug: why would separate categories get skipped, and what structural fix restores them?
3. In `let_que_take(qb)`, why couldn't the function just see the bank freedom-style — name the Python rule and the two escape routes (the chosen one and the lazy one).
4. Trace what happens when the user enters zero questions and exits — which guard prevents nonsense output?
5. State the duplicate-pick problem and write the pseudocode for the `selected`-list fix (before peeking at the gloss).
6. Which parts of the build demonstrate the trainer's "never terminate in front of the user" rule from Day 6?
7. What is left of `random` as homework, and why does leaving it unexplained serve the course?
