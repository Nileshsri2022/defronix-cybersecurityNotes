# SQL Day 3 — `INSERT`, `SELECT`, `ALTER`, `DROP` aur `TRUNCATE` (Hinglish Explanation)

**Source transcript:** `transcripts/039 - Day-3 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** Days 1–2 — DBMS/RDBMS, command families, types, table creation and constraints
**Continues:** Day 4 — SELECT filtering, UPDATE, aggregates, ordering and DELETE
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. Destructive SQL only disposable lab database par run karo.

---

## 1. Warm-up: DDL vs DML

```text
DDL = structure/schema
DML = rows/data
```

Day 3 mein table banane ke baad rows insert, read, structure alter aur table/data removal commands demonstrate hote hain.

---

## 2. Example `emp` table

Conceptual table:

```sql
CREATE TABLE emp (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(80),
    salary NUMBER,
    department VARCHAR2(40)
);
```

Column names/types actual lab script ke according vary kar sakte hain. Constraints Day 2 se carry forward hote hain.

---

## 3. `INSERT`

### 3.1 Column-list form — preferred

```sql
INSERT INTO emp (emp_id, emp_name, salary, department)
VALUES (1, 'Asha', 50000, 'Security');
```

Column names explicitly dene se order clear aur schema changes ke against safer.

### 3.2 Full-row form

```sql
INSERT INTO emp
VALUES (2, 'Ravi', 45000, 'Network');
```

Ye table ke exact column order/count par depend karta hai; missing/extra/misordered values error ya wrong data create kar sakte hain. Production code mein column-list prefer.

### 3.3 Text/date/NULL

```sql
INSERT INTO emp (emp_id, emp_name, salary)
VALUES (3, 'Zoya', 60000);
```

Omitted optional column default/NULL behavior constraint par depend karta hai. Date literal engine-specific; Oracle mein explicit conversion/format policy use karo.

### 3.4 Commit caution

Oracle transaction mein insert visible/session behavior aur durability commit se related ho sakti hai:

```sql
COMMIT;
```

Lab changes ko commit/rollback intentionally handle karo; production data par blind commit nahi.

---

## 4. `SELECT` ka first taste

```sql
SELECT * FROM emp;
```

- `SELECT` data retrieve.
- `*` all columns.
- `FROM emp` source table.

Specific columns:

```sql
SELECT emp_id, emp_name FROM emp;
```

Production/security reports mein `SELECT *` avoid karke minimum required columns request karo—PII exposure reduce hota hai.

---

## 5. `ALTER`

`ALTER TABLE` structure modify karta hai.

Add column:

```sql
ALTER TABLE emp ADD email VARCHAR2(120);
```

Modify/drop syntax engine-specific; transcript ALTER family ke multiple operations discuss karta hai. Destructive changes se pehle:

- schema backup/migration,
- dependency check,
- rollback plan,
- test environment,
- approval.

DDL often implicit commit behavior engine-specific ho sakta hai, so transaction assumptions verify karo.

---

## 6. `DROP` vs `TRUNCATE`

### `DROP TABLE`

```sql
DROP TABLE emp;
```

Table object/schema and data remove. Recreate/backup may be needed. Highly destructive.

### `TRUNCATE TABLE`

```sql
TRUNCATE TABLE emp;
```

Rows remove, table structure remains. Rollback behavior and logging engine-specific; Oracle mein truncate DDL semantics rakhta hai.

| Command | Structure | Rows | Risk |
|---|---|---|---|
| `DROP` | removed | removed | highest |
| `TRUNCATE` | remains | all removed | very high |
| `DELETE` | remains | selected/all rows | WHERE/transaction controls |

Day 4 mein DELETE detail aayega.

---

## 7. GUI nahi, command line kyu?

Transcript SQL command line par focus karta hai. CLI benefits:

- exact query visible,
- repeatable scripts,
- error message clear,
- automation/remote administration context.

GUI useful ho sakta hai but query understanding hide nahi honi chahiye. Lab query history/source control mein store karo—passwords nahi.

---

## 8. Homework/next flow

- Table mein more rows insert.
- `SELECT` with columns practice.
- ALTER variants research.
- DROP/TRUNCATE difference safely document.
- Output screenshots mein lab-only data.

---

## 9. Common mistakes aur corrections

1. `INSERT` column order mismatch.
2. Values ko quotes/type rules ke bina insert.
3. Full-row insert ko safest samajhna.
4. `SELECT *` se sensitive columns unnecessarily expose.
5. `ALTER` ko data update samajhna.
6. `DROP`/`TRUNCATE` ko rollback-safe assume.
7. Foreign-key dependencies ignore karna.
8. `COMMIT`/implicit DDL transaction behavior verify na karna.
9. Production DB par demo query run karna.
10. CLI error ko read kiye bina random query changes.

---

## 10. Day 3 self-check questions

1. DDL aur DML mein difference kya hai?
2. Column-list `INSERT` full-row insert se safer kyu?
3. `SELECT * FROM emp` ka meaning kya hai?
4. Minimum-column selection security mein kyu useful?
5. `ALTER TABLE ADD` ka example do.
6. `DROP`, `TRUNCATE`, `DELETE` compare karo.
7. `TRUNCATE` ke transaction behavior ko engine docs se verify kyu karna chahiye?
8. SQL CLI learning ke benefits kya hain?
9. Insert/DDL changes ko lab mein safe rakhne ke liye kaunsa workflow use karoge?
10. Constraint violation ko fix karne ke liye data/schema kaise inspect karoge?

---

## 11. Continuity

Day 3 ne rows aur schema changes ka base banaya. Day 4 mein `SELECT ... WHERE`, comparison/logical operators, `UPDATE`, aggregates, `ORDER BY` aur `DELETE` ke through real filtering/reporting aayegi.
