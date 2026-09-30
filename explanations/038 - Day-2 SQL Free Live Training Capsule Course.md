# SQL Day 2 — Data Types, `CREATE TABLE` aur Constraints (Hinglish Explanation)

**Source transcript:** `transcripts/038 - Day-2 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Trainer in transcript:** Hardik Ashirwad
**Builds on:** SQL Day 1 — data/database/DBMS/RDBMS aur command families
**Continues:** Day 3 — insert, select, alter, drop/truncate
**Note:** Ye exact matching Hindi transcript ko context ke saath samajh kar likha gaya hai; ye literal translation nahi hai. Oracle examples isolated lab database ke liye hain.

---

## 1. Data types ka contract

Table column define karte waqt database ko batana hota hai ki value kis type ki hogi. Common Oracle-style types:

| Type | Use |
|---|---|
| `NUMBER` | integers/decimal numeric values |
| `VARCHAR2(n)` | variable-length text |
| `CHAR(n)` | fixed-length text |
| `DATE` | date/time context |
| `CLOB`/large types | large text, engine-specific |

Exact syntax/database engine par depend karti hai. Type choice validation, storage aur query behavior affect karti hai.

Example:

```sql
CREATE TABLE student (
    student_id NUMBER,
    name VARCHAR2(50),
    age NUMBER,
    joined_on DATE
);
```

### 1.1 `CHAR` vs `VARCHAR2`

- `CHAR(n)` fixed-width storage/padding context.
- `VARCHAR2(n)` variable length up to limit.

Names/emails jaise variable text ke liye `VARCHAR2` usually suitable; fixed codes mein `CHAR` consider ho sakta hai.

---

## 2. `CREATE TABLE` practical

General form:

```sql
CREATE TABLE table_name (
    column_name data_type,
    column_name data_type
);
```

Semicolon statement terminate karta hai:

```sql
CREATE TABLE employee (
    employee_id NUMBER,
    employee_name VARCHAR2(100),
    salary NUMBER
);
```

### 2.1 Errors ko read karna

Trainer deliberately wrong statements/errors demonstrate karta hai. Error message ko ignore nahi; line, object name, type spelling, parentheses/comma aur existing-table status check karo.

Typical issues:

- missing comma,
- wrong data type spelling,
- table already exists,
- invalid identifier,
- unmatched parentheses,
- column size/type mismatch.

SQL client output copy karke minimal reproducible query banao. Error ko hide karne ke liye random edits mat karo.

---

## 3. Constraints = database-level validation

Constraints invalid/incomplete data ko entry point par stop karte hain.

### `NOT NULL`

```sql
name VARCHAR2(50) NOT NULL
```

Column value required.

### `UNIQUE`

```sql
email VARCHAR2(120) UNIQUE
```

Duplicate values prevent; `NULL` behavior engine-specific, so test/document.

### `PRIMARY KEY`

```sql
student_id NUMBER PRIMARY KEY
```

Row identity; unique and not-null semantics.

### `FOREIGN KEY`

```sql
course_id NUMBER,
FOREIGN KEY (course_id) REFERENCES course(course_id)
```

Referenced course exist hona chahiye; relational integrity.

### `CHECK`

```sql
age NUMBER CHECK (age >= 0)
```

Condition enforce.

### `DEFAULT`

```sql
status VARCHAR2(20) DEFAULT 'active'
```

Value omit hone par default. Sensitive/security status ka default carefully define karo.

---

## 4. Constraint placement

Inline:

```sql
student_id NUMBER PRIMARY KEY
```

Table-level:

```sql
CONSTRAINT pk_student PRIMARY KEY (student_id)
```

Named constraints later `ALTER`/error diagnosis mein easier ho sakti hain.

Example:

```sql
CREATE TABLE course (
    course_id NUMBER CONSTRAINT pk_course PRIMARY KEY,
    course_name VARCHAR2(80) CONSTRAINT uq_course_name UNIQUE
);
```

---

## 5. Security importance

Constraints business/data integrity controls hain:

- duplicate account IDs prevent,
- missing required identity fields block,
- invalid age/status values reject,
- orphan foreign-key records avoid.

But constraints authorization nahi. Application-level authentication, permission controls, parameterized SQL, audit logs aur least-privilege DB accounts separately required.

### 5.1 Sensitive data design

- Password plaintext store mat karo; proper salted password hashing application layer par.
- Email/phone access scope limit.
- PII screenshots/logs redact.
- Database backup encryption/access controls.

---

## 6. Course method aur troubleshooting

Day 2 ka focus syntax ratna nahi; query run karke error read karna hai:

```text
write -> execute -> observe error/output -> identify cause -> correct -> rerun
```

Same table names ko repeatedly create karoge to existing-object error aayega. Lab reset/drop operation destructive hai; confirm before running.

---

## 7. Common mistakes aur corrections

1. Column name aur datatype ke beech comma/parenthesis miss.
2. `VARCHAR2` size omit/incorrect.
3. `CHAR` ko every text field ke liye use karna.
4. Primary key na define karna.
5. Foreign key parent table se pehle create.
6. `NOT NULL` ko authorization samajhna.
7. Constraint error ko random syntax change se mask karna.
8. Table already exists par blindly `DROP` karna.
9. Password/PII sample data real values se fill karna.
10. Oracle syntax ko MySQL/PostgreSQL universally same samajhna.
11. `CHECK` constraint ko complete validation/security control samajhna.

---

## 8. Day 2 self-check questions

1. `NUMBER`, `VARCHAR2`, `CHAR`, `DATE` kab use karoge?
2. `CHAR` aur `VARCHAR2` ka broad difference kya hai?
3. `CREATE TABLE` ka basic syntax likho.
4. SQL error ko troubleshoot karne ka reproducible workflow kya hai?
5. `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `DEFAULT` explain karo.
6. Table-level named constraint ka benefit kya hai?
7. Foreign key parent/child relationship kaise protect karti hai?
8. Constraints security controls ka replacement kyu nahi?
9. Existing table par destructive command se pehle kya check karoge?
10. Database lab mein real passwords/PII kyu avoid karna chahiye?

---

## 9. Continuity

Day 1 ke command families mein DDL ka practical start `CREATE TABLE` se hua. Day 3 mein isi table par `INSERT`, `SELECT`, `ALTER`, `DROP` aur `TRUNCATE` use honge; constraints ke effects data operations mein visible honge.
