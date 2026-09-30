# SQL Day 5 — `GROUP BY`, `HAVING`, `BETWEEN`, `LIKE` aur `DISTINCT` (Hinglish Explanation)

**Source transcript:** `transcripts/041 - Day-5 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** Day 4 — SELECT/WHERE, logical operators, aggregates and ORDER BY
**Continues:** Day 6 — set operators and `IS NULL`
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Queries lab/authorized data par run karo.

---

## 1. `GROUP BY` — rows se buckets

Aggregate ko categories ke saath use karne ke liye:

```sql
SELECT department, COUNT(*) AS employee_count
FROM emp
GROUP BY department;
```

Meaning:

1. Rows ko same department groups mein collect.
2. Har group par `COUNT` calculate.
3. One summary row per group.

Salary summary:

```sql
SELECT department, AVG(salary) AS avg_salary
FROM emp
GROUP BY department;
```

### 1.1 SQL rule

Non-aggregate selected column generally `GROUP BY` mein appear hona chahiye:

```sql
SELECT department, COUNT(*)
FROM emp
GROUP BY department;
```

`SELECT department, emp_name, COUNT(*)` without grouping `emp_name` engine error/invalid aggregation de sakta hai.

---

## 2. `HAVING` — groups filter

`WHERE` individual rows ko grouping se pehle filter karta hai. `HAVING` grouped/aggregate result ko filter karta hai:

```sql
SELECT department, COUNT(*) AS employee_count
FROM emp
GROUP BY department
HAVING COUNT(*) >= 2;
```

### WHERE vs HAVING

```text
WHERE  -> rows
GROUP BY -> groups
HAVING -> groups
```

Combined:

```sql
SELECT department, AVG(salary) AS avg_salary
FROM emp
WHERE salary > 30000
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## 3. `BETWEEN` inclusive range

```sql
SELECT * FROM emp
WHERE salary BETWEEN 40000 AND 70000;
```

Usually lower and upper boundaries include hoti hain. Date/time range mein boundary/time component carefully check karo.

Equivalent broad logic:

```sql
WHERE salary >= 40000 AND salary <= 70000
```

### Security/reporting caution

Date timestamp mein `BETWEEN '2024-01-01' AND '2024-01-31'` last day ke times miss kar sakta hai depending on data type. Half-open ranges often safer, engine-specific syntax verify.

---

## 4. `LIKE` pattern search

```sql
SELECT * FROM emp
WHERE emp_name LIKE 'A%';
```

Wildcards:

- `%` = zero or more characters.
- `_` = exactly one character.

Examples:

```sql
WHERE emp_name LIKE '%son%'   -- contains son
WHERE emp_name LIKE '_avi'    -- one char + avi
WHERE email LIKE '%@example.test'
```

Case sensitivity/collation database configuration par depend. User-supplied search term parameterized query se bind karo; SQL string concatenate mat karo.

### 4.1 Escaping wildcard

Agar literal `%`/`_` search karna ho to engine-specific `ESCAPE` syntax use karo. Wildcard broad query performance/index impact create kar sakti hai.

---

## 5. `DISTINCT`

Duplicate output remove:

```sql
SELECT DISTINCT department
FROM emp;
```

Multiple columns ka distinct combination hota hai:

```sql
SELECT DISTINCT department, job_title
FROM emp;
```

`DISTINCT` underlying data delete/deduplicate nahi karta; only result set unique banata hai.

---

## 6. Query processing mental model

Simplified conceptual order:

```text
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY
```

Actual optimizer execution different ho sakta hai, but clause relationship samajhne mein helpful:

- row filter before grouping,
- aggregate filter after grouping,
- presentation/order at end.

---

## 7. Security and analytics use-cases

- `GROUP BY` incident counts by severity/host.
- `HAVING` teams with many failed logins.
- `BETWEEN` time/score/port ranges.
- `LIKE` domain/log pattern search.
- `DISTINCT` unique IPs/URLs/categories.

PII or credentials summary query mein unnecessary columns select mat karo.

---

## 8. Common mistakes aur corrections

1. `WHERE` se aggregate condition filter karna.
2. `HAVING` ko row filter samajhna.
3. `BETWEEN` endpoints inclusive bhoolna.
4. Date/time boundary issue ignore karna.
5. `%` aur `_` wildcard difference miss.
6. `LIKE '%term%'` ko case-insensitive guaranteed samajhna.
7. `DISTINCT` ko database deduplication samajhna.
8. Grouped query mein non-aggregated column omit/not group.
9. User search term concatenate karke injection risk.
10. Broad wildcard query se sensitive/full table data expose.

---

## 9. Day 5 self-check questions

1. `GROUP BY department` ka output kya represent karta hai?
2. `WHERE` aur `HAVING` ka difference example se batao.
3. Grouped average par `HAVING` kaise lagayenge?
4. `BETWEEN` boundaries kaise treat hoti hain?
5. Date ranges mein timestamp edge case kya hai?
6. `LIKE` mein `%` aur `_` ka meaning kya hai?
7. `DISTINCT department, job_title` kis type ka duplicate remove karega?
8. `DISTINCT` underlying table ko change kyu nahi karta?
9. SQL clause processing order conceptually likho.
10. Security log analysis mein GROUP BY/LIKE ka safe use-case do.

---

## 10. Continuity

Day 5 ne SQL analytics ko row se group level tak le gaya. Day 6 mein multiple SELECT result sets ko combine karne ke liye `UNION`, `UNION ALL`, `MINUS`, `INTERSECT` aur missing-value `IS NULL` aayega.
