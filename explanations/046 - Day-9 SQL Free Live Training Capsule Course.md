# Explanation — 046 — Day 9: SQL (Free Live Training Capsule Course)

**Source:** `transcripts/046 - Day-9 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/046 - Day-9 SQL Free Live Training Capsule Course.md`
**Level:** Beginner SQL, Day 9 (trainer **Hardik**) — the schema-objects day: **VIEW · INDEX · SEQUENCE · USER/GRANT/REVOKE**, run on Oracle-flavoured SQL (`system`, `dual`, `currval`/`nextval`).

---

## 0. The one law that organises the day

> **Whatever is born from `CREATE` dies by `DROP`.**

Tables aren't the only creatable things — views, indexes, sequences, procedures, functions, and users all follow the same CREATE → DROP lifecycle. This single law is the day's skeleton; each object type is then one section.

## 1. VIEW — a stored query wearing a table costume

**Motivation:** yesterday's subqueries stack output-on-output (extract from a table → put more conditions on that output → extract again). Re-typing the inner query every time is clumsy, so you bottle it:

```sql
CREATE VIEW emp_v AS
SELECT col1, col2 FROM employees WHERE <conditions>;

SELECT * FROM emp_v;           -- the whole output behind one name
```

Key properties he drills:

- A view is a **virtual table** — feels exactly like a table, but **only the query text is stored, never the output**.
- Consequence: **edit the base table and the view's results change too** (it re-runs the stored query every time).
- You can wrap further conditions around a view (`SELECT … FROM emp_v WHERE …`) — output-on-output, now readable.
- **You cannot INSERT into it** — it's not a real table.
- Cleanup: `DROP VIEW emp_v;` (the CREATE/DROP law).

## 2. INDEX — the invisible accelerator

**Motivation:** pulling output from a table can "give much trouble" (slow) once data grows.

```sql
CREATE INDEX idx_name ON employees(emp_id);   -- or on (name)
```

- The index is **purely internal** — you can't see it, "can't see the induction"; the system uses it silently.
- Lookups through a **primary-keyed/indexed column become very fast**; on the demo's small table you feel nothing — **in big data you'll feel the change**.
- Non-goals stated plainly: "index — no work at all" beyond retrieval speed; it's created with CREATE and dropped with DROP like everything else.

## 3. SEQUENCE — ids that assign themselves

**Motivation:** hand-writing 102, 103, 104…109 into every INSERT is misery (and collides with the `UNIQUE` constraint if you slip).

```sql
CREATE SEQUENCE emp_seq
  START WITH 160          -- next id after the existing 109
  INCREMENT BY 1
  MINVALUE … / MAXVALUE 1999
  NOCYCLE;                -- don't wrap to the start at the end
```

- After wiring it into inserts (`emp_seq.NEXTVAL` for the id), you stop supplying numbers — names/data only.
- **Checking where it's at:** the `dual` table — Oracle's built-in one-row empty table for exactly such tests:
  ```sql
  SELECT emp_seq.CURRVAL FROM dual;   -- 111 … after the next insert, 112
  ```
- His workplace rationale: when a **developer/DB changes, the newcomer needs to see "what's currently running"** — sequences + `currval` answer that.
- `NOCYCLE` vs cycling: after the max sequence either stops or restarts from the beginning (you can also re-start manually).

## 4. USERS & PRIVILEGES — the girlfriend's-phone saga

**Scenario:** you're connected as `system` (the admin). You want a separate user for your assistant: he logs in as himself, does his own work, but **must not touch your main tables** without permission.

```sql
CREATE USER bhai IDENTIFIED BY <pw>;       -- exists, but…
-- first login attempt fails: "user bhai lacks CREATE SESSION privilege"
GRANT CREATE SESSION TO bhai;              -- now he can connect
CONNECT bhai/<pw>;
SELECT * FROM system.employees;            -- "table does not exist"
GRANT SELECT ON employees TO bhai;         -- now SELECT works
-- INSERT / UPDATE attempts likewise fail until granted
REVOKE SELECT ON employees FROM bhai;      -- take it back
DROP USER bhai;                            -- delete him entirely
```

Lessons embedded in the comedy (disconnected session showing **"not connected"**, the trust rant "your DBA doesn't even trust you," taking back the "Instagram password"):

- A fresh user **can't even open a session** until `CREATE SESSION`/`CONNECT` is granted.
- Privileges are **granular** — SELECT, INSERT, UPDATE are separate gates; **missing SELECT shows up as "table does not exist," which isn't the honest story** — the table exists, *you* don't have the privilege.
- **GRANT gives, REVOKE takes** — single privilege, multiple, or **ALL** at once; and `DROP USER` is the "delete all the photos" endgame (CREATE ⇒ DROP law again).

## 5. Announcements (course logistics)

- **Defronix internship:** a live **Python + cyber-security mini-project** — build in a group sitting together (individual path possible), trainer participates, **certificate for the CV**, details and updates **only on the Telegram channel** — spread it to friends/groups.
- **Reward carrot:** if the series gets a strong response, he'll stream a **live SQL injection against their own database** plus the **lab setup** — i.e., everything learned so far weaponised in a live demo.
- Website plug: the Defronix toolkit (per-domain cyber-security tools, manuals, news, workshops); feedback/improvement requests welcome; new tools may come out of the internship itself.

## 6. Study pointers

1. Write a view over one of your Day-7 joined queries; then UPDATE a base-table row and re-select the view — see the change flow through (query stored, not output).
2. Create a sequence with `START WITH`/`INCREMENT BY`/`MAXVALUE`/`NOCYCLE`, insert three rows using `NEXTVAL`, and read `CURRVAL FROM dual` between inserts.
3. Create a second user; verify each denial (no session → no select → no insert), then grant each right one at a time; finish with `REVOKE` + `DROP USER`.
4. Recite the CREATE ⇒ DROP census: table, view, index, sequence, procedure, function, user.
5. Revise the full SQL series (his homework) — Days 1–9 — since the promised finale (SQL injection) builds on all of it.
