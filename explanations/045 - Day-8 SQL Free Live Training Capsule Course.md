# Explanation — 045 — Day 8: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/045 - Day-8 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/045 - Day-8 SQL Free Live Training Capsule Course.md`
**Level:** Beginner SQL, Day 8 (trainer **Hardik**). The "query inside a query" day: **subqueries** — single-value, nested, and the multi-row operators **ANY / ALL / EXISTS / NOT EXISTS**.

---

## 0. Framing

He opens by deferring the usual topic-review: today starts from **the problems students hit** — specifically the wall everyone meets after aggregates (`MAX`, `MIN`…): *"I can get the max salary, but the moment I also ask for the employee's NAME in the same SELECT, it breaks."* The answer is the whole day's topic: the **subquery**.

## 1. The subquery pattern (single value)

```sql
SELECT *                         -- or name + details
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

- The **inner (lower) query runs first** and produces **one value**; that value is substituted into the outer WHERE, and the outer query runs on that base.
- This is why `SELECT name, MAX(salary) FROM employees` doesn't give you "the name of the max earner" — the aggregate knows the number, not the row. The subquery separates the two jobs: **inner gets the number, outer fetches the row**.
- Teaching style note: he promises to go slow because "today is important *and* hard" and explicitly asks students to watch rather than struggle alongside.

## 2. The interview classic — second-highest salary

```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

- Take everything **below** the max, then take the **max of that remainder** → second-highest.
- His key didactic point: **you can't hard-code `< 95000`** — when you build a table you don't know what values the application/company will insert later (the "company owner sets ₹1 lakh" scenario). The threshold must itself be **computed by a nested subquery**, so the query stays correct as data changes. Then the full-row version (`SELECT * …` around the same predicate) returns the actual person.

## 3. Interlude — LEFT OUTER JOIN, 10-second revision

A regular (Mohammad Paras) asks for yesterday's LEFT OUTER recap: **all rows of the LEFT table show up, with the matching right-table data attached where it exists** (NULLs where it doesn't). Plus a running joke about group members who talk a lot but never do the tasks.

## 4. When the subquery returns MANY rows — ANY and ALL

`=` only works when the subquery yields **one** value. If it yields a list (a "multiple-rows subquery"), you need quantified comparison:

- **`ANY`** (a.k.a. `SOME`): the comparison must hold against **at least one** value in the list.
  `salary > ANY (80000, 80000, 60000)` → everything above the *smallest* of the list qualifies (demo: > 85000 works, > 95000 [the max itself] returns nothing).
  Mental model: **"bigger than any one of these"** = bigger than the minimum.
- **`ALL`**: the comparison must hold against **every** value.
  `salary > ALL (subquery)` → only values above the *largest* of the list qualify.
  Mental model: **"bigger than them all"** = bigger than the maximum.
- The operators slot into the familiar comparison signs (`>`, `<`, `=`, `>=`…) — he calls these the "logical operations."
- He struggles a bit to verbalise ANY and openly re-explains two or three times ("maybe I'm not explaining well — tell me"); the distilled rule he lands on: *ANY checks with each value of the list and passes if any single check succeeds; ALL demands the check succeed with every value.*

## 5. EXISTS / NOT EXISTS — row-level presence testing

Question posed: **which courses have students enrolled — and which have NO students at all?**

```sql
SELECT ...
FROM course c
WHERE EXISTS (SELECT 1 FROM student s WHERE s.course_id = c.course_id);
```

- **`EXISTS`** doesn't care *what* the inner query returns, only **whether it returns anything**: the inner query is re-evaluated per outer row (a correlated subquery); if ≥1 row comes back, the outer row is kept.
- **`NOT EXISTS`** inverts it → precisely the **courses with zero enrolled students** (demo pivot: once course **50** gains students, it leaves the NOT-EXISTS result).
- He warns this is the hardest piece of the day: "watch it three times, and run the commands yourselves — building the logic yourself is how it clicks" (a recurring piece of advice he says he's given in personal messages too).

## 6. Concepts-to-drill checklist

1. Single-value subquery in `WHERE` (max/min/avg extraction of the full row).
2. Second-highest salary via **nested** subquery — never hard-code the threshold.
3. `= ANY (…)` ≡ `IN` semantics; `<> ALL (…)` ≡ `NOT IN` — worth deriving once by hand.
4. `EXISTS` for "has children / has no children" questions between related tables — the relational complement of LEFT JOIN … `IS NULL`.
5. Run each demo twice: once with the literal list, once with the subquery that generates the list.

## 7. Logistics

Tasks/screenshots via the academy's **LinkedIn company post** (task date appears there; if it doesn't show yet, check **Telegram**); remaining links in the video description. Tomorrow continues from here.
