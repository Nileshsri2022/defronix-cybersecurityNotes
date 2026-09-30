# SQL Day 9 — Views, Indexes, Sequences aur Users/Privileges (Hinglish Explanation)

**Source transcript:** `transcripts/046 - Day-9 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** SQL Days 1–8 — queries/subqueries, joins, constraints and transactions
**Course context:** SQL capsule ka current final/advanced foundation session; privilege concepts later security work se connect honge.
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai. User/privilege changes isolated lab database par and least privilege ke saath practice karo.

---

## 1. `VIEW` — stored query ka table-like interface

View virtual table jaisi hoti hai; underlying query store hoti hai, usually result data ka independent copy nahi.

```sql
CREATE VIEW public_employee_summary AS
SELECT emp_id, emp_name, department
FROM emp;
```

Use:

```sql
SELECT * FROM public_employee_summary;
```

### 1.1 View benefits

- Complex query simplify.
- Sensitive columns hide.
- Reusable reporting interface.
- Application ko base schema changes se partially decouple.
- Role-based access mein only view grant.

### 1.2 View caution

- Underlying table changes view break kar sakti.
- View security guarantee nahi—underlying permissions/config check.
- `SELECT *` view avoid; explicit columns.
- View se sensitive row/column accidentally expose na karo.

Drop/change syntax engine-specific and destructive; migration review required.

---

## 2. `INDEX` — query accelerator

Index column values ka lookup structure maintain karta hai:

```sql
CREATE INDEX idx_emp_department
ON emp(department);
```

Frequent filter/join/order columns par lookup fast ho sakta hai.

### 2.1 Trade-offs

- SELECT/read faster possible.
- Insert/update/delete par index maintenance overhead.
- Storage use.
- Low-cardinality/wrong column index useless or harmful.
- Query planner/index statistics matter.

Index data access permission nahi deta. Sensitive indexed column still protected via privileges/encryption.

Check query plan/performance only authorized DB:

```sql
EXPLAIN PLAN FOR
SELECT * FROM emp WHERE department = 'Security';
```

Exact display syntax Oracle/engine-specific.

---

## 3. `SEQUENCE` — generated IDs

Oracle-style sequence unique numeric values generate kar sakti hai:

```sql
CREATE SEQUENCE emp_seq
START WITH 1
INCREMENT BY 1;
```

Use:

```sql
INSERT INTO emp (emp_id, emp_name)
VALUES (emp_seq.NEXTVAL, 'Asha');
```

- `NEXTVAL` next number.
- `CURRVAL` current session value after NEXTVAL context.

### Sequence caveats

- Gaps normal: rollback/crash/parallel calls.
- Gapless invoice numbering automatically guarantee nahi.
- Sequence value sensitive business info expose kar sakti if used carelessly.
- Primary key constraint still define.

---

## 4. Users aur privileges

Database accounts ko permissions required work ke according milni chahiye:

```sql
CREATE USER analyst IDENTIFIED BY "strong-lab-password";
GRANT CREATE SESSION TO analyst;
```

Grant only necessary object privilege:

```sql
GRANT SELECT ON emp TO analyst;
```

Remove:

```sql
REVOKE SELECT ON emp FROM analyst;
```

Exact Oracle syntax/password policy environment-specific; admin account se lab only.

### 4.1 Least privilege

Application ko:

- read-only view/select,
- required insert/update only,
- no `DROP`, `GRANT`, unrestricted DELETE
rights dene chahiye.

Transcript girlfriend ke phone/permissions analogy se explain karta hai: trust ke naam par every access mat do; misuse par revoke.

### 4.2 Role-based access

Users ko individual grants ke bajay roles se manage karo:

```sql
CREATE ROLE reporting_role;
GRANT SELECT ON public_employee_summary TO reporting_role;
GRANT reporting_role TO analyst;
```

Role review/offboarding easy. Production database mein admin/system credentials share mat karo.

---

## 5. SQL security connection

Views minimize exposure; indexes performance improve; sequences IDs; privileges access control. Ye separate layers hain:

```text
schema constraints + query safety + authentication + authorization + logging + encryption
```

SQL injection prevention still parameterized queries and secure application code require karti hai. Granting SELECT to a safe view injection risk eliminate nahi karta if application concatenates input.

---

## 6. Common mistakes aur corrections

1. View ko physical secure copy samajhna.
2. View mein `SELECT *` se sensitive columns include.
3. Every column par index create karna.
4. Index ko authorization control samajhna.
5. Sequence ko gapless counter samajhna.
6. Primary key ke bina sequence use.
7. Application ko DBA/admin grant.
8. Password command history/screenshot mein expose.
9. `REVOKE`/offboarding review na karna.
10. Role aur user privilege scope confuse.
11. SQL injection fix ko database grant se complete samajhna.

---

## 7. Day 9 self-check questions

1. View kya store karti hai aur sensitive columns hide karne mein kaise useful?
2. View security ke limitations kya hain?
3. Index read/write/storage trade-off kya hai?
4. Query plan ka use-case kya hai?
5. Sequence `NEXTVAL` ka role kya hai?
6. Sequence gaps normal kyu?
7. User, privilege aur role mein difference kya hai?
8. Application account ko DBA rights dena risky kyu?
9. `GRANT` aur `REVOKE` ka purpose kya?
10. SQL injection prevention aur database privilege ka relation kya?
11. Production DB credentials ko lab screenshots se kaise protect karoge?

---

## 8. SQL block recap

Days 1–9 ne data model, DDL/DML/DCL/TCL, constraints, queries, aggregation, sets, joins, subqueries, views, performance aur access control cover kiya. Ye SQL foundation later web-security/SQL-injection labs mein useful hai, but only authorized training targets par.
