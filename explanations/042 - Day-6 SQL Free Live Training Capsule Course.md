# SQL Day 6 — Set Operators: `UNION`, `UNION ALL`, `MINUS`, `INTERSECT` aur `IS NULL` (Hinglish Explanation)

**Source transcript:** `transcripts/042 - Day-6 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** Days 1–5 — tables, SELECT/WHERE, aggregation, grouping and pattern filters
**Continues:** Day 7 — joins/foreign keys
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Set operations authorized lab tables par practice karo.

---

## 1. Set operators ka idea

Do compatible `SELECT` result sets ko combine/compare karna set operators ka purpose hai. Both queries generally:

- same number of columns,
- compatible data types,
- corresponding column order
return karein.

Example tables:

```text
employee_a
employee_b
```

---

## 2. `UNION`

```sql
SELECT emp_name FROM employee_a
UNION
SELECT emp_name FROM employee_b;
```

Both results combine hote hain aur duplicate rows remove hoti hain.

Concept:

```text
A union B = A + B, unique result
```

Duplicate removal output-level behavior hai; source tables change nahi.

---

## 3. `UNION ALL`

```sql
SELECT emp_name FROM employee_a
UNION ALL
SELECT emp_name FROM employee_b;
```

All rows, including duplicates. Faster ho sakta hai because deduplication nahi.

Use when:

- duplicate occurrence meaningful,
- append-like report,
- source tables known distinct.

Duplicate sensitive records report mein include karne se pehle purpose check karo.

---

## 4. `MINUS`

Oracle-style:

```sql
SELECT emp_name FROM employee_a
MINUS
SELECT emp_name FROM employee_b;
```

A mein present but B mein absent rows. Set difference direction-sensitive hai.

```text
A MINUS B != B MINUS A
```

Some databases equivalent `EXCEPT` use karte hain; SQL engine syntax verify.

---

## 5. `INTERSECT`

```sql
SELECT emp_name FROM employee_a
INTERSECT
SELECT emp_name FROM employee_b;
```

Only common rows. Duplicate handling/database semantics check; generally set-style unique result.

Use case:

- two allowlists ka overlap,
- common assets,
- two evidence sources mein same identifier.

Common output match hona identity/authenticity proof nahi; source quality and context verify.

---

## 6. Operator comparison

| Operator | Result |
|---|---|
| `UNION` | A+B unique |
| `UNION ALL` | A+B including duplicates |
| `MINUS`/`EXCEPT` | A-only |
| `INTERSECT` | common A∩B |

Order/columns:

```sql
SELECT id, name FROM a
UNION
SELECT id, name FROM b;
```

`SELECT id FROM a UNION SELECT id,name FROM b` invalid due column count mismatch.

---

## 7. `NULL` aur `IS NULL`

SQL `NULL` means unknown/missing—not zero, false or ordinary empty string.

Wrong:

```sql
WHERE phone = NULL
```

Correct:

```sql
WHERE phone IS NULL
WHERE phone IS NOT NULL
```

Reason: `NULL` comparison three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`) follow karti hai; `=` se expected matching nahi.

### 7.1 Example

```sql
SELECT * FROM customer
WHERE phone IS NULL;
```

KYC/contact completion audit ke liye missing fields identify ho sakte hain. PII data ko report mein mask/minimize karo.

---

## 8. Data quality/security use

Set operators help:

- asset inventory A vs B compare,
- employee/allowlist overlap,
- stale accounts identify,
- duplicate source records understand.

`NULL` reports:

- missing MFA enrollment,
- missing owner/contact,
- incomplete KYC/asset inventory.

A missing value is not automatically a vulnerability. Context, policy and remediation priority required.

---

## 9. Housekeeping/course philosophy

Transcript query syntax ko examples se practice karne aur previous concepts revise karne par focus karta hai. SQL ko copy-paste command list nahi; result-set reasoning samjho:

```text
What is source A?
What is source B?
Do I need duplicate rows?
Am I checking overlap, difference, or missing data?
```

---

## 10. Common mistakes aur corrections

1. Set queries mein different column counts.
2. Incompatible data types combine.
3. `UNION` aur `UNION ALL` duplicate behavior confuse.
4. `MINUS` direction reverse.
5. `MINUS` ko MySQL/PostgreSQL universal syntax samajhna.
6. `INTERSECT` result ko person identity proof samajhna.
7. `= NULL` use karna.
8. NULL ko zero/empty string treat karna.
9. PII set result public report mein full expose.
10. Source table modify hone ka false assumption—set operators output only.

---

## 11. Day 6 self-check questions

1. Set operator use karne ke liye SELECT outputs mein kya compatible hona chahiye?
2. `UNION` aur `UNION ALL` compare karo.
3. `A MINUS B` ka meaning kya hai?
4. `INTERSECT` ka security inventory use-case do.
5. `MINUS`/`EXCEPT` engine difference kya hai?
6. `NULL` ko `= NULL` se kyu nahi check karte?
7. `IS NULL` aur `IS NOT NULL` queries likho.
8. Missing phone number ko security report mein kaise minimize karoge?
9. Duplicate results meaningful ho to kaunsa operator choose karoge?
10. Set result ko independent source se verify kyu karna chahiye?

---

## 12. Continuity

Day 6 ne independent result sets ka relationship sikhaya. Day 7 mein relational tables ko actual columns/foreign keys ke through join karna aayega—`INNER`, outer, cross aur self joins.
