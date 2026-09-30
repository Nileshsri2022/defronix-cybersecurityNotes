# SQL Day 8 — Subqueries, Second-Highest Salary, `ANY`, `ALL`, `EXISTS` (Hinglish Explanation)

**Source transcript:** `transcripts/045 - Day-8 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** SQL Days 1–7 — filtering, aggregation, set operators, joins and foreign keys
**Continues:** Day 9 — views, indexes, sequences and privileges
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Queries isolated lab tables par run karo.

---

## 1. Subquery kya hai?

Query ke andar query ko subquery/nested query kehte hain:

```sql
SELECT emp_name, salary
FROM emp
WHERE salary = (
    SELECT MAX(salary)
    FROM emp
);
```

Inner query value/result banati hai; outer query us result ko filter/display karti hai.

Logical flow:

```text
inner query -> result -> outer query
```

### 1.1 Single-value subquery

`=` ke saath subquery ko exactly one value return karna chahiye. Agar inner query multiple rows return kare, “single-row subquery returns more than one row” type error aa sakta hai.

Use `MAX`, `MIN`, `COUNT` ya appropriate filter se one value ensure karo.

---

## 2. Second-highest salary classic

Maximum salary nikalne ke baad usse less salaries mein maximum:

```sql
SELECT emp_name, salary
FROM emp
WHERE salary = (
    SELECT MAX(salary)
    FROM emp
    WHERE salary < (
        SELECT MAX(salary)
        FROM emp
    )
);
```

Alternative `ORDER BY`/analytic functions engine-specific ho sakte hain. Duplicate highest/second-highest salaries ke business semantics define karo: second distinct salary ya second row?

### 2.1 Why hard-code nahi

Table values runtime par change hoti hain. `95000` hard-code karne ke bajay nested query current maximum/second maximum derive karti hai.

---

## 3. LEFT OUTER JOIN revision

Day 7 connection:

```sql
SELECT s.name, c.course_name
FROM student s
LEFT OUTER JOIN course c
  ON s.course_id = c.course_id;
```

Left table ke all records; right matching values; missing right = `NULL`. Subquery aur joins same result problem ke different solutions ho sakte hain; data size/readability/performance compare karo.

---

## 4. Multiple-row subqueries: `ANY` and `ALL`

Inner query multiple salaries de sakti hai:

```sql
SELECT emp_name, salary
FROM emp
WHERE salary > ANY (
    SELECT salary
    FROM emp
    WHERE department = 'Security'
);
```

- `> ANY` = at least one returned value se greater.
- `< ALL` = all returned values se less.

Broad interpretation:

```text
ANY -> one or more comparison satisfy
ALL -> every comparison satisfy
```

Exact operator semantics and NULL behavior engine docs se verify. `IN` often equality-any style use-case mein clearer.

---

## 5. `EXISTS` / `NOT EXISTS`

`EXISTS` check karta hai ki correlated subquery at least one row return karti hai ya nahi:

```sql
SELECT s.name
FROM student s
WHERE EXISTS (
    SELECT 1
    FROM course c
    WHERE c.course_id = s.course_id
);
```

`NOT EXISTS` orphan/missing relation:

```sql
SELECT s.name
FROM student s
WHERE NOT EXISTS (
    SELECT 1
    FROM course c
    WHERE c.course_id = s.course_id
);
```

`SELECT 1` value important nahi; existence only check. Correlation `c.course_id = s.course_id` outer row se inner query connect karti hai.

### 5.1 Security/data use

- Accounts with at least one active role.
- Assets with an owner record.
- Students with valid course.
- Hosts with findings.

Existence result identity/authorization proof nahi until source/constraints/policy verified.

---

## 6. Subquery mistakes

1. `=` with multi-row result.
2. Correlation condition miss karke uncorrelated all/none result.
3. `NULL` comparison ignore.
4. Second-highest duplicate semantics unclear.
5. Sensitive columns inside subquery unnecessarily select.
6. Query performance on large table test na karna.

Use `EXPLAIN PLAN` only authorized/local database, and least data projection.

---

## 7. Query design checklist

```text
What result do I need?
Single value or multiple rows?
Can a JOIN express it more clearly?
What happens with NULL/duplicates?
Do I need distinct rank or row order?
Which columns are safe to return?
```

---

## 8. Self-check questions

1. Subquery aur outer query ka flow explain karo.
2. `=` subquery ko single value kyu chahiye?
3. Second-highest salary nested query se kaise derive karoge?
4. Duplicate second-highest salaries ka meaning define karo.
5. `ANY` aur `ALL` ka difference kya hai?
6. `EXISTS` mein `SELECT 1` kyu use hota hai?
7. Correlated subquery ka relation outer row se kaise banta hai?
8. `NOT EXISTS` se orphan records kaise find karoge?
9. Subquery vs JOIN choose karte waqt kya factors dekho?
10. SQL query mein unnecessary sensitive columns kyu avoid karne chahiye?

---

## 9. Continuity

Day 8 ne query ke andar query aur relationship-existence logic add kiya. Day 9 mein reusable views, query-performance indexes, auto-number sequences aur database users/privileges cover honge.
