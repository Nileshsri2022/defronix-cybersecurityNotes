# Explanation — 039 — Day 3: SQL (DROP/TRUNCATE, INSERT, first SELECT, ALTER family)

**Source:** `transcripts/039 - Day-3 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/039 - Day-3 SQL Free Live Training Capsule Course.md`
**Level:** Beginner, hands-on. Day 3 is the first real write-day: building a constrained `emp` table, putting rows in, seeing them, and then mutating/destroying the structure — with the command-line-only doctrine made explicit.

---

## 0. What this class is

Day 3 converts Day 2's read-only schema literacy into **change-making**: first DML (`INSERT`), first retrieval (`SELECT *`), and the full **ALTER** toolbox (ADD / DROP / MODIFY / RENAME), capped by the destruction pair **DROP TABLE** (structure+data gone) vs **TRUNCATE** (structure survives, all rows gone, **no rollback**). A set of homework tasks gates the next class.

## 1. Warm-up retrieval

- **Structure vs data (hammered in again):** `DESC emp` shows the **schema** — column names/types — *not* data. The entered names/numbers are the data (DML's world, "coming ahead").
- **Recap recital of constraints** with the class: UNIQUE (phone-number example), NOT NULL (address/name can't be blank), DEFAULT (fires only when the user gives nothing), PRIMARY KEY (unique+not-null), FOREIGN KEY (defines the between-tables relationship), and **CHECK** — admitted honestly as the one he himself hasn't internalized yet; parked for later ("like history: some things you just have to do").

## 2. The day's build: `emp`

Fresh table with live-chosen constraints: `name VARCHAR2(...)` (**NOT NULL**), `contact_number` (**UNIQUE**), `state VARCHAR2(...) DEFAULT 'Rajasthan'`. The default demo is precise about trigger semantics: **typing anything (even "rs") suppresses the default; the default fills only an omitted value.**

## 3. INSERT — the two canonical forms

| Form | Shape | Rule he drills |
|---|---|---|
| **Full-sequence** | `INSERT INTO emp VALUES (v1, v2, …)` | must give **every** column, **in the table's column order** |
| **Named-columns** | `INSERT INTO emp (col_a, col_b, col_c) VALUES (…)` | values map to the **named** columns only; order among them is free; unspecified columns take NULL/**DEFAULT** |

The named form is presented as the answer to "why did the default fire?": inserting a row that **omits `state`** and then `SELECT *`-ing shows `Rajasthan` filled in — constraints become visible, answering students' "the rule doesn't show on the front" doubt.

## 4. SELECT — deliberately just a taste

Only `SELECT * FROM emp;` — star = "everything/every column." Its role today is *verification* (see inserted rows, see the default). The deep dive is scheduled: "**SELECT alone will run for two full days**," starting next class.

## 5. ALTER — the modification family (all shown or tasked)

| Operation | Shape | Teaching note |
|---|---|---|
| **ADD column** | `ALTER TABLE emp ADD salary NUMBER(10);` | new column appears in DESC instantly; old rows have nothing there; joke: "hope your salaries need >10 digits" |
| **DROP column** | `ALTER TABLE emp DROP COLUMN department;` | **any** column may be dropped — not just the newest; don't pattern-match "last added only" |
| **MODIFY column** | `ALTER TABLE … MODIFY <col> <new type/size or constraint>;` | e.g. widen to 15 digits; new error shapes appear when types/values collide |
| **RENAME table** | `ALTER TABLE emp RENAME TO employee;` | afterwards the old name errors: **"table does not exist"** — instant quiz (student "Mewati" answered: renamed) |
| **RENAME column** | — | **left as homework**: "contact number TO phone — how, through ALTER? You tell me." |

**Doctrine attached to ALTER:** do schema surgery **freshly after table creation**; once data is in, alterations can force data fixes — and sometimes the database will **refuse** the alteration outright. "After the last data input — don't alter."

## 6. Destruction pair — DROP vs TRUNCATE

- **`DROP TABLE student;`** — structure **and** data gone; the prior RENAME even surfaces as `object STUDENT is not a table`.
- **`TRUNCATE TABLE …;`** — table **stays**, **every row** is wiped; proven live by `SELECT` returning **"no rows selected."**
- **The irreversibility is the lesson:** TRUNCATE **cannot be rolled back** — recall the bank/UPI rollback story from Day 1; here there is no going back to the previous state. His operational rule, verbatim-logic: *use TRUNCATE only when you're on extremely good terms with your company.*

## 7. Environment doctrine — why no GUI

Student asks why not a friendlier SQL GUI. Answer (verbatim-logic): interfaces won't exist **everywhere** — real work happens **on servers**, where you install the SQL server and connect by command line; panels like phpMyAdmin-style helpers aren't guaranteed; building the **CLI habit is the point**. (He also bows to feedback: deliberately speaking slower than Day 1's pace — beginners couldn't keep up.)

## 8. Homework & flow to Day 4

Tasks (repeat across Day-2/Day-3 LinkedIn-post comments as **command + DESC screenshot**):
1. **Add a PRIMARY KEY to an existing table via ALTER.**
2. **Add some column via ALTER** and show it.
3. Discover **ALTER … RENAME COLUMN** yourself ("tell me how").
4. Effectively: experience TRUNCATE's one-shot wipe (warned).
Next class: **SELECT begins for real** (multi-day). Web development tie-in acknowledged: a website reaches SQL by connecting to the SQL server and sending commands — scheduled for the development stage.

## 9. Concept map

```
DESC ≠ SELECT  →  DESC = schema (columns) · SELECT = data (rows)
CONSTRAINTS recited: UNIQUE · NOT NULL · DEFAULT(fires only when omitted) · PK · FK · CHECK(parked)
INSERT
  full : VALUES for ALL columns, table order
  named: (cols…) VALUES… → only those cols · order free · rest = NULL/DEFAULT  ⇒ demo: state → 'Rajasthan'
SELECT * FROM …  (taste only — star = everything; deep dive = next 2 days)
ALTER TABLE
  ADD col · DROP COLUMN col (any col!) · MODIFY col · RENAME TO … · RENAME COLUMN … = HOMEWORK
  doctrine: alter FRESH, before data — after data, changes may be forced or refused
DESTRUCTION
  DROP     → table + data gone
  TRUNCATE → rows gone, table stays · NO ROLLBACK · "only if you're great friends with your company"
ENV: CLI-first — servers have no GUI; command-line habit is the real skill
```

## 10. Self-check prompts

1. Insert into `emp` without column names vs with `(name, contact_number)` — state which constraints/defaults decide what fills `state` in each form.
2. A teammate ran TRUNCATE "to clear test rows"; your boss asks you to recover one record. Answer, citing this class.
3. Reproduce both Day-3 errors from memory: renaming mid-script ("table does not exist") and yesterday's missing-comma phantom — and name Oracle's `*` marker's meaning.
4. Write, in plain words, the ALTER-early doctrine and the two failure reasons it prevents.
5. Homework answers: give the **exact** ALTER syntax you'd expect for (a) adding a PRIMARY KEY, (b) renaming `contact_number` to `phone`.
6. Why does DEFAULT 'Rajasthan' *not* fire when the user types "rs"? What does fire then?
