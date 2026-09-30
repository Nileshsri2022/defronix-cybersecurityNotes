# SQL Day 4 — `SELECT`, `WHERE`, `UPDATE`, Aggregates, Ordering aur `DELETE` (Hinglish Explanation)

**Source transcript:** `transcripts/040 - Day-4 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** Days 1–3 — tables, constraints, insert/select/alter/drop/truncate
**Continues:** Day 5 — `GROUP BY`, `HAVING`, `BETWEEN`, `LIKE`, `DISTINCT`
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Update/delete examples only disposable lab data par run karo; SQL injection content defensive learning ke liye hai.

---

## 1. `SELECT` projection

```sql
SELECT emp_name, salary
FROM emp;
```

`SELECT` batata hai kaunse columns output mein; `FROM` source table.

```sql
SELECT * FROM emp;
```

All columns convenient but security/reporting mein unnecessary PII expose kar sakta hai. Minimum fields request karo.

---

## 2. `WHERE` row filtering

```sql
SELECT emp_id, emp_name
FROM emp
WHERE department = 'Security';
```

`WHERE` rows filter karta hai; projection columns select karta hai.

Comparison operators:

```sql
=  !=  <>  >  <  >=  <=
```

Text/date/number comparison syntax engine/data type ke according use karo.

Examples:

```sql
SELECT * FROM emp WHERE salary >= 50000;
SELECT * FROM emp WHERE emp_name <> 'Ravi';
```

---

## 3. SQL injection awareness

Login/query input agar unsafe string concatenation se SQL statement mein insert ho, attacker query logic alter kar sakta hai. Transcript always-true condition `1=1` style conceptual reading repeats.

Unsafe anti-pattern:

```python
query = "SELECT * FROM users WHERE name='" + user_input + "'"
```

Preferred application defense:

- parameterized/prepared statements,
- strict input handling,
- least-privilege DB account,
- generic error messages,
- logging and tested secure code.

Real website/login par payload try mat karo. Authorized local lab mein only instructor scope/ROE follow karo.

---

## 4. `UPDATE` — data repair/change

```sql
UPDATE emp
SET salary = 55000
WHERE emp_id = 1;
```

**`WHERE` mandatory habit**. Without it:

```sql
UPDATE emp SET salary = 55000;
```

all rows update ho sakte hain.

Safe workflow:

```sql
SELECT * FROM emp WHERE emp_id = 1;
UPDATE emp SET salary = 55000 WHERE emp_id = 1;
SELECT * FROM emp WHERE emp_id = 1;
```

Transaction/backup/approval policy follow karo; accidental update rollback guarantee nahi.

---

## 5. Aggregate functions

```sql
SELECT COUNT(*) FROM emp;
SELECT SUM(salary) FROM emp;
SELECT AVG(salary) FROM emp;
SELECT MIN(salary) FROM emp;
SELECT MAX(salary) FROM emp;
```

Aggregates multiple rows ko summary mein convert karte hain.

### 5.1 `NULL` law

`NULL` = unknown/missing, zero ya empty string necessarily nahi. Aggregates generally NULL values ignore kar sakte hain (except `COUNT(*)` behavior), so business meaning check karo.

```sql
SELECT COUNT(email) FROM emp;
SELECT COUNT(*) FROM emp;
```

Dono counts different ho sakte hain if email NULL.

---

## 6. `AS` aliases

```sql
SELECT AVG(salary) AS average_salary
FROM emp;
```

Alias output readable banata hai. Alias permanent schema rename nahi.

---

## 7. `ORDER BY`

```sql
SELECT emp_name, salary
FROM emp
ORDER BY salary DESC;
```

- `ASC` default ascending.
- `DESC` descending.

Sensitive reports mein deterministic secondary ordering useful:

```sql
ORDER BY salary DESC, emp_name ASC;
```

Without order database result order guaranteed nahi samjho.

---

## 8. `AND` / `OR`

```sql
SELECT * FROM emp
WHERE department = 'Security'
AND salary >= 50000;
```

Both conditions true.

```sql
SELECT * FROM emp
WHERE department = 'Security'
OR department = 'Network';
```

Either condition.

Parentheses use karo:

```sql
WHERE department = 'Security'
  AND (salary >= 50000 OR emp_id = 1)
```

Precedence ambiguity se wrong rows update/delete/report ho sakte hain.

---

## 9. `DELETE`

```sql
DELETE FROM emp
WHERE emp_id = 1;
```

Again, missing `WHERE` all rows delete kar sakta hai:

```sql
-- dangerous in a real database
DELETE FROM emp;
```

Pre-check:

```sql
SELECT * FROM emp WHERE emp_id = 1;
```

Transaction/backup/change approval use karo. Lab reset only disposable database.

---

## 10. Query review checklist

Before `UPDATE`/`DELETE`:

1. Correct database/schema?
2. `WHERE` present?
3. `SELECT` preview same predicate?
4. Expected row count?
5. Backup/transaction policy?
6. Authorization/change ticket?
7. Audit log?

SQL errors and result count record karo.

---

## 11. Common mistakes aur corrections

1. `SELECT *` everywhere use karna.
2. `WHERE` miss karke all rows update/delete.
3. SQL injection payload ko real target par test.
4. `NULL` ko zero/empty samajhna.
5. `COUNT(*)` aur `COUNT(column)` same samajhna.
6. `AS` ko schema rename samajhna.
7. `ORDER BY` absent result ko naturally sorted samajhna.
8. `AND`/`OR` precedence bina parentheses.
9. SQL query string concatenate karna.
10. DML change par transaction/backup policy ignore.

---

## 12. Day 4 self-check questions

1. Projection aur filtering mein difference kya hai?
2. `SELECT *` security reporting mein risky kyu?
3. `WHERE` clause ka role kya hai?
4. SQL injection ka root coding mistake kya hota hai?
5. Parameterized query ka purpose kya hai?
6. `UPDATE`/`DELETE` mein WHERE preview workflow likho.
7. `COUNT(*)` aur `COUNT(email)` kab differ karenge?
8. `AS` alias kya karta hai?
9. `ORDER BY salary DESC` ka output order kya hoga?
10. `AND`/`OR` parentheses kyu important?
11. Query execution se pehle authorization kyu check karoge?

---

## 13. Continuity

Day 4 ne SQL ko useful reporting aur controlled modification language banaya. Day 5 aggregation groups (`GROUP BY`/`HAVING`) aur pattern/range filters (`BETWEEN`, `LIKE`, `DISTINCT`) add karega.
