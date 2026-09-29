# Explanation — 037 — Day 1: SQL (Data → DBMS → RDBMS, SQL's command families)

**Source:** `transcripts/037 - Day-1 SQL Free Live Training Capsule Course [ Hindi ].hi-orig.srt`
**Translation:** `english/037 - Day-1 SQL Free Live Training Capsule Course.md`
**Level:** Absolute-beginner SQL, **security-framed** — same trainer (Hardik) and same live-capsule format as the Python capsule (029–035). Day 1 is ~95% theory by design; hands-on querying starts next class.

---

## 0. What this class is

The SQL capsule's foundation day: the concept ladder **data → database → DBMS → RDBMS**, a live **Oracle 10g** install, and the four SQL command families (**DDL / DML / DCL / TCL**) — all framed around the capsule's destination: **SQL injection** (promised as a live lab in the final class). No SQL statements are yet run; the only practical work assigned is installing Oracle and posting a "Connected" screenshot.

## 1. The concept ladder (each rung defined by the one below it)

1. **Data** = the **raw form of information**. Information is the extracted, *useful* part; data is everything lying around it can be extracted from. (His domestic image: the house is full of things; only the useful ones count as "your data.")
2. **Database** = a collection of data (the bookshelf full of books).
3. **DBMS (Database Management System)** = the *system* that manages the database — how items are arranged, found, retrieved (his model: a library as books-management-made-system). It replaced the older **file-based** storage, whose failure mode he lists: opening many files by hand to locate one fact, plus the where/how/arrangement headaches.
4. **Tabular model:** modern DBMSs structure data as **tables** = **columns** (kinds of data) × **rows** (one record each). The college-result-table analogy: find your row, read across. (He even nods to the *3 Idiots* result scene.)
5. **SQL (Structured Query Language)** = the *language* created to manage/query that table-world. A single run instruction is a **query**; the query returns data out of tables. Crucial distinction he draws: **SQL ≠ DBMS** — SQL is the language spoken *to* the system; the DBMS is the whole system.
6. **RDBMS (Relational DBMS)** = DBMS where tables can be **related** to each other. His two-table example encodes a real **foreign-key-style constraint**: the students-table accepts a `course` value **only if** that course exists in the courses-table — the insert-time check *is* the relationship. RDBMS is the current mainstream; older lineage: file systems → DBMS → RDBMS.
7. **Deliberately out of scope:** **normalization** (1NF/2NF…) — flagged as too deep for this capsule's level.

## 2. The why — the cyber-security framing (the class's real payload)

A login form sketch delivers the whole argument:

- A website's login posts **username + password**; the backend runs an SQL **query** asking "does this pair exist in the users table?"; match → logged in, no match → nothing.
- If an attacker can smuggle **malicious SQL into that query** so the database **behaves abnormally**, that's **SQL injection**. The canonical shape of the payload — a condition that is **always true** — is shown by name: **`1 = 1`** (`OR 1=1`-style tautology) → login granted as admin.
- Consequence chain he traces: injection → database **dump** → credential lists — and connects it to **cracking** workflows: use **dorks** to find small vulnerable sites → inject → dump DB → **credential-stuff** the same username/password combos everywhere else. With the explicit warning: **cracking is completely illegal — don't try it.**
- The paired doctrine (verbatim-logic): in security you learn to **break *and* fix** — you can't sanitize against injection you don't understand; "doing a thing isn't important, knowing how it works is." The extended **Maggi** parable: too much salt ruins the noodles — a cook knows how to *reduce* the salt's effect with the other spices. Break-knowledge is what enables fix-knowledge.
- The **script-kiddie** warning: someone who only runs tools/commands without knowing what happens in the backend "doesn't know how the thing works — when it breaks, they can't fix it." Depth is the entire point of the capsule.
- Legitimate career faces of the same knowledge: **DBA** (you own what happens to the data) and **developer** (storing/showing data). He pledges the course reaches **college level**; students can send their college syllabus via Telegram.

## 3. Installation (the day's only practical)

- **Tool: Oracle Database 10g** on **Windows** (link via Telegram / video description; explicitly **not Android**; no Mac guidance). Rationale for choosing a mainstream engine: core **queries run everywhere**; engines differ in small ways (Oracle: slightly different data types, has **PL/SQL**; MySQL: the "normal" one, everywhere nowadays).
- Install walk: download → run installer → accept terms → **next/next** → set **password** — with the big caution: **remember this password**, changing it later is painful (write it down).
- **Connecting:** Start menu → Oracle's **SQL command line** → enter credentials (`system` + password) → success shows **Connected**. Side notes: install can feel slow (the engine stands up local server pieces, databases, its own **port** in the background); heaviness ends after install.
- **Homework/task:** install, get "Connected," post the **screenshot in the video comments** (ID/password may be hidden); problems → Telegram (tag an admin).

## 4. SQL's four command families (the day's core theory)

He frames the families as: *what kinds of meddling can be done with data* — the extras/extensions all live inside these mains.

| Family | Full name | Scope ("whose business") | Commands he names | His teaching image |
|---|---|---|---|---|
| **DDL** | Data **Definition** Language | the **schema** — table structure: how many columns, what each column holds (number/string/date…) | **CREATE · ALTER · DROP** | "DDL uncle" dictates the structure; humans err → ALTER fixes schema mistakes; DROP = the (joked-about) rage-quit "drop everything on your last day" — **with an explicit never-do-this warning**; real use = genuinely retiring unneeded tables |
| **DML** | Data **Manipulation** Language | the **data rows inside** the table | **SELECT · INSERT · UPDATE · DELETE** | profile edits as the everyday example (a user changing their own name/email = an UPDATE); **warns**: textbooks often split SELECT off separately — he'll own the correction next class if needed |
| **DCL** | Data **Control** Language | **permissions** — who may do what | **GRANT · REVOKE** | king-and-pawns model: admin = king; junior devs/services = pawns; a website typically gets insert-only rights ("you can put data in, not delete it"); REVOKE = snatching misused powers back (the mother image) |
| **TCL** | **Transaction** Control Language | making changes **final / undoable**; production-grade | **COMMIT · ROLLBACK** | commit ≈ git commit (finalize globally; no going back) → rollback = return to the previous state. Living example: **UPI payment at a shop** — stuck "processing," failed transfer, or debited-but-not-received → system rolls back; refund lands within ~30 days |

**DDL-vs-DML confusion is explicitly banned** (his words): DDL touches the table's *scheme*; DML touches the *data inside* it.

## 5. Course logistics stated in this session

- **No fixed commitment** on series length (no "7 days / 20 days"); it scales with audience support and demanded topics; big standalone topics may get dedicated videos.
- Sessions stay short for now; depth ramps when DML starts — "**for SELECT alone we'll spend one-two full days**."
- Feedback loop: Telegram (links, troubleshooting — tag any admin), comments (homework screenshots), session reviews; he even asks for mic purchase advice (₹5000 budget) after the class's audio issues.

## 6. Concept map

```
DATA      : raw form of information → extract the useful part
DATABASE  : organized collection (bookshelf)
DBMS      : the system managing the database (library) — replaces ad-hoc FILES
TABLE     : columns (kinds) × rows (records) — the college result sheet
SQL       : Structured Query Language — queries run against tables;  SQL ≠ DBMS
RDBMS     : tables RELATED to tables (insert-time course check ≈ foreign-key idea)
            lineage: files → DBMS → RDBMS (today's mainstream); normalization deferred
WHY SECURITY CARES
  login → backend query → smuggled always-TRUE condition (1=1) ⇒ SQL INJECTION
  injection → DB dump → credential lists → cracking/credential-stuffing (ILLEGAL — warned)
  doctrine: learn to break ⇄ learn to fix; concepts > tools (anti script-kiddie)
COMMAND FAMILIES
  DDL (schema): CREATE ALTER DROP     — "DDL uncle"; don't rage-DROP on exit
  DML (rows)  : SELECT INSERT UPDATE DELETE — the profile-edit everyday case
  DCL (rights): GRANT REVOKE          — king/pawns; website gets insert-only
  TCL (finality): COMMIT ROLLBACK     — git-like; the UPI-payment rollback story
```

## 7. Self-check prompts

1. Place these in a sentence each such that each defines the next: data, database, DBMS, SQL, RDBMS.
2. Two tables: `courses` and `students`. Describe the insert-time check that makes their relationship "relational."
3. Trace a website login to its SQL query; now describe what an always-true injected condition (1=1) changes, and name the attack.
4. Sort these commands into families and *state the scope of each family*: COMMIT, DROP, REVOKE, UPDATE, ALTER, GRANT, SELECT, ROLLBACK, INSERT, CREATE.
5. Recite the DDL-vs-DML rule in one line each ("DDL uncle owns ___; DML uncle owns ___").
6. Re-tell the shop/UPI story as a COMMIT/ROLLBACK narrative: which events trigger a rollback, and why does that protect the user?
7. What made file-based data handling painful enough to invent the DBMS? Why is SQL not the same thing as the DBMS?
