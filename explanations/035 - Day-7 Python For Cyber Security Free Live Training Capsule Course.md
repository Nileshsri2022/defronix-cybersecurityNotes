# Python for Cyber Security Day 7 — Capstone: Random Question-Paper Maker (Hinglish Explanation)

**Source transcript:** `transcripts/035 - Day-7 Python For Cyber Security Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Nitesh Singh (Defronix)
**Builds on:** Python Days 1–6 — input, containers, dictionaries, operators, loops, files, functions, exceptions
**Course context:** Python for Cyber Security capsule ka final/capstone session
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai; ye literal translation nahi hai. Project educational/local use ke liye hai. Random question generation ko real exam integrity/privacy requirements ke saath deploy karne se pehle testing chahiye.

---

## 1. Project kyu question-paper maker?

Day 6 poll mein hacking-tool idea discuss hua, but sockets/networking abhi course mein deep nahi the aur live offensive tooling security controls se block ho sakti thi. Isliye trainer aisa project choose karte hain jo har learned Python concept revise kare:

> **Randomized Question-Paper Maker**

Problem:

- Online exam mein same paper se cheating easy.
- Question bank large ho.
- Har student/set ko different questions milen.
- Marks/category aur total marks control hon.
- Manual questions aur file input dono support ho.

Project simple-looking hai, but requirements, data structures, loops, files, functions, exceptions aur `random` all combine karte hain.

---

## 2. Requirements engineering

| Requirement | Python design |
|---|---|
| Questions manually enter | Input/menu loop |
| Questions file se load | File handling |
| Multiple paper sets | Outer loop |
| Random selection | `random` module |
| 1/2/3/4/5/10 marks | Dict of lists |
| Total marks | Arithmetic/calculation |
| User friction low | Minimal required prompts |
| Invalid input crash na kare | `try/except` |
| Output paper files | `open()`/write |

Online paper integrity ke liye randomization alone enough nahi: duplicate avoidance, question difficulty balance, answer-key handling, access controls aur audit logs bhi needed hain.

---

## 3. Question bank design

Dictionary marks categories ko lists se map karegi:

```python
question_bank = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    10: []
}
```

Example:

```python
question_bank[1].append("What is a variable?")
question_bank[5].append("Explain file modes.")
```

Why dict of lists?

- key = marks category,
- value = us category ke questions,
- random selection category-wise easy,
- Day 3 dictionary + Day 2 list revision.

### 3.1 File input

Questions file se lines read karke appropriate marks bucket mein add kiye ja sakte hain. File format/documentation clearly define karo, for example:

```text
1|What is a variable?
5|Explain file modes.
```

Malformed line ko exception/validation se handle karo, silently wrong category mein add nahi.

---

## 4. Input menu loop

Trainer interactive menu idea use karte hain:

```text
1 -> enter a question
anything else -> exit input phase
```

Conceptual code:

```python
while True:
    choice = input("Question enter karna hai? 1=yes: ")
    if choice != "1":
        break

    marks = int(input("Marks: "))
    text = input("Question: ")
    question_bank.setdefault(marks, []).append(text)
```

Production validation:

- marks allowed set mein hai?
- question empty to nahi?
- duplicate question?
- input length limit?
- file encoding?
- user cancellation?

`setdefault()` transcript ke exact code ka claim nahi; safe conceptual helper hai. Class ka focus earlier concepts revise karna hai.

---

## 5. Function refactor: `let_que_take(question_bank)`

Repeated per-category input code ko function mein move kiya jata hai:

```python
def let_que_take(question_bank):
    # input and append logic
    return question_bank
```

Function ke andar banaya variable local hota hai. Existing bank ko parameter pass karo ya return value use karo:

```python
question_bank = let_que_take(question_bank)
```

Day 6 ka argument/parameter/scope lesson yahan practically apply hota hai.

Editor tip transcript mein Shift+Tab se selected block dedent ka mention hai; modern editor shortcut differently behave kar sakta hai.

---

## 6. Selection phase

Each marks category ke liye user se kitne questions chahiye poochna:

```python
for marks, bank in question_bank.items():
    if len(bank) > 0:
        # ask requested count for this category
        pass
```

Important bug:

```python
# Wrong design for independent categories:
if one_mark:
    ...
elif two_mark:
    ...
elif five_mark:
    ...
```

`elif` chain mein ek branch true hote hi baaki categories skip ho sakti hain. Independent categories ke liye separate `if`/loop use karo.

### 6.1 Quantity validation

Requested count bank size se greater ho to random selection error/duplicates ho sakte hain:

```python
if requested > len(bank):
    raise ValueError("Not enough questions in category")
```

User-friendly message do; program silently paper generate na kare.

---

## 7. Total marks

Suppose:

```python
one_mark_count = 2
two_mark_count = 3
five_mark_count = 1
```

Total:

```python
total = (
    one_mark_count * 1
    + two_mark_count * 2
    + five_mark_count * 5
)
```

Agar user ne zero questions enter kiye to empty paper generate nahi karna:

```python
if total > 0:
    generate_paper()
else:
    print("No questions selected")
```

Marks metadata output mein clearly show karo.

---

## 8. Random selection aur live bug

Transcript `random` library se list se random question choose karta hai:

```python
import random
pick = random.choice(question_bank[marks])
```

Output paper file mein question write hota hai. Multiple sets ke liye outer loop:

```python
for set_number in range(1, total_sets + 1):
    # select and write one paper
    pass
```

### 8.1 Duplicate question bug

Live demo mein same question two sets mein repeat hua. Random choice **with replacement** duplicate de sakta hai.

Homework-style fix concept:

```python
selected = []

while len(selected) < requested:
    pick = random.choice(bank)
    if pick not in selected:
        selected.append(pick)
```

Better standard approach for unique selection:

```python
selected = random.sample(bank, requested)
```

`random.sample` ke liye requested <= bank length ensure karo. Transcript learners ko random library aur duplicate fix research karne ko kehta hai.

### 8.2 Cross-set uniqueness

Within one paper no duplicates aur across papers no repeat—two different requirements hain. Whole exam pool limited ho to all sets globally unique banana mathematically impossible after capacity exhausted. Requirement precisely define karo.

---

## 9. Output paper generation

Output structure:

```text
Institute name
Set number
Total marks

1-mark questions
...

5-mark questions
...
```

File write:

```python
with open(f"paper_set_{set_number}.txt", "w", encoding="utf-8") as f:
    f.write("Question Paper\n")
    f.write(f"Set: {set_number}\n")
    f.write(f"Total Marks: {total}\n")
```

Trainer center alignment ke liye spaces ka “jugaad” use karta hai. Better production option formatting/alignment functions hain; fixed spaces different terminal/fonts mein shift ho sakte hain.

File close automatically `with` block se ho jata hai.

---

## 10. Project mein all concepts ka audit

| Day | Concept | Project use |
|---|---|---|
| 1 | `print`, input, casting | Menu/marks/counts |
| 2 | lists, append, len | Category question banks |
| 3 | dict, keys, membership | Marks → questions |
| 4 | loops, break, if | Input/selection/set loops |
| 5 | open/read/write | Question files/output papers |
| 6 | functions, scope, exceptions | Input helper/error handling |
| New | `random` | Question selection |

Project ka pedagogical point: earlier concepts isolated examples nahi rahe; one complete program mein interact karte hain.

---

## 11. Validation aur exam-integrity improvements

Original classroom project ke beyond production checklist:

- duplicate questions detect,
- question bank backup/versioning,
- answer keys separate protected file,
- random seed policy document,
- secure output permissions,
- student identifiers minimize,
- deterministic test mode for QA,
- audit log without answers/secrets,
- file parsing validation,
- generated paper review before distribution.

Randomness cheating eliminate guarantee nahi; students/sets, answer ordering, difficulty and leaked bank controls bhi matter.

---

## 12. Homework aur course close

1. `random` module ke additional functions research.
2. Duplicate selection fix implement.
3. Requested-count-over-capacity validation add.
4. Code/screenshot/Drive report approved Day 7 LinkedIn post comments mein share.
5. Attempt first, then Telegram doubt/feedback.
6. Course feedback poll; future language/development/networking course community response par depend.

---

## 13. Common mistakes aur corrections

1. One question bank list instead of marks-wise structure.
2. `elif` chain se categories skip karna.
3. Function local variable ko global samajhna.
4. Requested count > available bank allow karna.
5. `random.choice` ko unique selection samajhna.
6. Within-paper vs across-set uniqueness confuse karna.
7. Empty question/invalid marks accept karna.
8. Output path overwrite karna.
9. `f.close()`/context manager ignore karna.
10. Fixed spaces ko reliable centering samajhna.
11. Answer key ko generated paper ke saath expose karna.
12. Random project ko real exam production guarantee samajhna.
13. Student data/identifiers unnecessarily log karna.
14. Generated paper ko review/test kiye bina distribute karna.

---

## 14. Day 7 self-check questions

1. Dict of lists question bank ke liye kyu suitable hai?
2. Manual and file input ko same internal structure mein kaise convert karoge?
3. `let_que_take(question_bank)` mein parameter/scope issue kya hai?
4. Independent categories ke liye `elif` chain bug explain karo.
5. Requested questions bank se zyada hon to kya validation chahiye?
6. `random.choice` duplicates kyu de sakta hai?
7. `random.sample` ka use-case aur precondition kya hai?
8. Within-paper aur cross-set uniqueness ka difference kya hai?
9. Total marks zero hone par empty paper prevent kaise karoge?
10. Project mein Days 1–6 ke concepts map karo.
11. Exam-paper generator ko production-ready banane ke liye security/integrity controls likho.
12. Randomness cheating ko fully eliminate kyu nahi karta?

---

## 15. Python capsule recap

- Python readable scripting language hai.
- Values se containers, dictionaries aur operators tak progression hua.
- Conditions/loops ne decision/repetition diya.
- Files/`os` ne persistence/system interaction diya.
- Functions/exception handling ne reuse/resilience diya.
- Capstone ne all concepts ko one practical project mein combine kiya.

OSINT/security context mein ye foundation future scripts—log processing, report generation, API clients, authorized inventory and defensive automation—ke liye use hogi. Tool banana se pehle scope, authorization, input validation aur safe output design samajhna equally important hai.
