---
title: "T07 · Triggers and Stored Procedures — Textbook Exercise Solutions"
tags: [ece2215, database-systems, silberschatz-exercises, topic-T07]
topic_id: T07
exercise_count: 14
source_chapters: ["Chapter 04", "Chapter 05", "Chapter 09"]
---

[← Prev: T06](T06_Joins_and_Views.md) | [Exam-style T07](../Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) | [Next: T08 Part 1 →](T08_Part1_FDs_and_Armstrong_Axioms.md)

---

# T07 · Triggers and Stored Procedures — Textbook Exercise Solutions

> [!info] Topic Card & Academic Blueprint
> - **Syllabus Unit:** Unit 4 — SQL (DDL, DML, Aggregates, Joins, Views, Triggers, and Stored Procedures)
> - **RUET Exam Weight:** 27 final marks (4.2% historical share; tested in 5 of 7 recent finals: 2017, 2018, 2020, 2023, 2024).
> - **Primary Source Reference:** Silberschatz, Korth, and Sudarshan, *Database System Concepts* (7th Edition, 2019):
>   - **Chapter 04:** Section 4.4.8 (*Complex Check Conditions and Assertions*)
>   - **Chapter 05:** Section 5.1 (*Accessing SQL From a Programming Language: JDBC & ODBC*), Section 5.2 (*Functions and Procedures*), Section 5.3 (*Triggers*)
>   - **Chapter 09:** Section 9.3 & 9.5 (*Web Application Architectures & JDBC Resource Management*)
> - **Pedagogical Objective:** Provide mathematically complete, architecturally sound, and dialect-aware solutions for all assigned textbook exercises. Solutions include complete SQL:1999/PSM, Oracle PL/SQL, PostgreSQL PL/pgSQL, Java JDBC, and C/ODBC implementations, accompanied by RUET-specific exam rubrics and pitfalls.

---

## Exercise Navigation Matrix

| Exercise | Source Chapter & Page | Subtopic Mapping | Title / Core Competency | Exam Significance |
| :--- | :--- | :---: | :--- | :--- |
| **[Exercise 4.8](#exercise-48--complex-cross-table-integrity-constraints-and-assertions)** | Ch. 04, p. 178 | T07.1 | Complex Cross-Table Integrity Constraints & Assertions | High (Conceptual Root of Triggers) |
| **[Exercise 5.5](#exercise-55--enforcing-cross-relation-schedule-constraints-via-triggers)** | Ch. 05, p. 233 | T07.1 | Enforcing Cross-Relation Schedule Constraints via Triggers | Very High (RUET 2023/2024 Trigger Parallels) |
| **[Exercise 5.7](#exercise-57--conditional-referential-cleanup-and-cascades-via-triggers)** | Ch. 05, p. 234 | T07.1 | Conditional Referential Cleanup & Cascades via Triggers | High (Referential Integrity Automation) |
| **[Exercise 5.19](#exercise-519--implementing-on-delete-cascade-using-the-trigger-mechanism)** | Ch. 05, p. 236 | T07.1 | Implementing `ON DELETE CASCADE` using the Trigger Mechanism | Very High (ECA Mechanics & Cascade Emulation) |
| **[Exercise 5.20](#exercise-520--trigger-nesting-limits-cascading-depth-and-recursion-control)** | Ch. 05, p. 236 | T07.1 | Trigger Nesting Limits, Cascading Depth & Recursion Control | Critical (System Stability & RUET Theory) |
| **[Exercise 5.1](#exercise-51--analyzing-hierarchical-transitive-closure-in-jdbc)** | Ch. 05, p. 232 | T07.3 | Analyzing Hierarchical Transitive Closure in JDBC | High (Code Reading & Programmatic Closure) |
| **[Exercise 5.2](#exercise-52--dynamic-tabular-result-set-formatting-via-jdbc-metadata)** | Ch. 05, p. 232 | T07.3 | Dynamic Tabular Result Set Formatting via JDBC Metadata | Very High (JDBC Architecture & Schema Reflection) |
| **[Exercise 5.12](#exercise-512--comprehensive-university-teaching-record-application-in-java-jdbc)** | Ch. 05, p. 235 | T07.3 | Comprehensive University Teaching Record Application in Java JDBC | Exceptional (End-to-End Enterprise CLI Application) |
| **[Exercise 5.13](#exercise-513--generic-schema-agnostic-table-display-class-metadisplay-in-java)** | Ch. 05, p. 235 | T07.3 | Generic Schema-Agnostic Table Display Class (`MetaDisplay`) | High (Metadata Querying & Generic Programming) |
| **[Exercise 5.14](#exercise-514--generic-tabular-relation-display-in-c-using-odbc)** | Ch. 05, p. 235 | T07.3 | Generic Tabular Relation Display in C using ODBC | High (Low-Level C ABI, Handles, & ODBC Reflection) |
| **[Exercise 5.15](#exercise-515--stored-function-for-departmental-average-salary-and-conditional-selection)** | Ch. 05, p. 235 | T07.3 | Stored Function for Average Salary & Conditional Selection | Very High (SQL/PSM vs PL/SQL Stored Functions) |
| **[Exercise 5.17](#exercise-517--bill-of-materials-bom-total-cost-computation-via-client-side-recursion-in-jdbc)** | Ch. 05, p. 236 | T07.3 | Bill-of-Materials (BOM) Total Cost Computation via JDBC Recursion | Exceptional (Algorithmic Graph Traversal in DBMS) |
| **[Exercise 5.18](#exercise-518--server-side-stored-procedure-for-university-teaching-records)** | Ch. 05, p. 236 | T07.3 | Server-Side Stored Procedure for University Teaching Records | Very High (Database-Tier vs Application-Tier Logic) |
| **[Exercise 9.5](#exercise-95--resource-management-and-leak-prevention-with-try-with-resources-in-jdbc)** | Ch. 09, p. 455 | T07.3 | Resource Management & Leak Prevention with Try-With-Resources | Critical (Connection Pool Safety & Architecture) |

---


## T07.1 · Trigger Concepts, Event-Condition-Action (ECA) Model, and Integrity Constraints

---

### Exercise 4.8 · Complex Cross-Table Integrity Constraints and Assertions

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.4.8 (*Complex Check Conditions and Assertions*), Page 178.
> - **Subtopic Mapping:** `T07.1` — What a trigger is, its purposes, and its syntax (ECA architecture, constraints vs triggers).
> - **Key Concepts:** Table-level `CHECK` constraints, Inter-relational Assertions (`CREATE ASSERTION`), ECA Trigger alternatives, Computational complexity of multi-table integrity validation.
> - **Difficulty & RUET Relevance:** Theoretical foundation for why triggers are indispensable in modern relational database management systems.

**Question (Silberschatz 7e Exercise 4.8).**
> As discussed in Section 4.4.8, we expect the constraint “an instructor cannot teach sections in two different classrooms in a semester in the same time slot” to hold.
> 
> **a.** Write an SQL query that returns all (instructor, section) combinations that violate this constraint.  
> **b.** Write an SQL assertion to enforce this constraint (as discussed in Section 4.4.8, current generation database systems do not support such assertions, although they are part of the SQL standard).

---

#### 1. Core Principles & Concept Overview

In relational database systems, integrity constraints ensure data validity and business rule adherence. Constraints are classified hierarchically by their enforcement scope:

1. **Attribute and Tuple Constraints:** Enforced on a single column (`NOT NULL`, `CHECK (salary > 0)`) or across columns within a single row.
2. **Referential Integrity Constraints:** Foreign keys (`FOREIGN KEY ... REFERENCES`) that enforce parent-child consistency across two relations.
3. **General Assertions (`CREATE ASSERTION`):** Declarative predicates expressed in standard SQL that span arbitrary numbers of relations and tuples. If an assertion predicate evaluates to `FALSE`, the triggering transaction is rejected.
4. **Active Triggers:** Event-Condition-Action (ECA) procedures executed imperatively by the database engine in response to specific data modification events (`INSERT`, `UPDATE`, `DELETE`).

##### The University Enterprise Schema
The relevant relations from the standard university schema are:
- $\text{teaches}(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}})$
- $\text{section}(\underline{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{building}, \text{room\_number}, \text{time\_slot\_id})$
- $\text{instructor}(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{salary})$

##### The Architectural Dilemma: Assertions vs. Triggers
The SQL standard provides `CREATE ASSERTION <name> CHECK (<condition>)`. In theory, assertions represent the ideal declarative mechanism for multi-table invariants. However:
- An assertion condition must be re-evaluated whenever **any** of the referenced tables (`teaches` or `section`) undergoes an `INSERT`, `UPDATE`, or `DELETE`.
- Checking an assertion involving an inter-table join requires scanning or probing large index structures on every commit, introducing an $O(|T| \times |S|)$ or $O(N \log N)$ computational overhead across the entire database workload.
- Consequently, **no major commercial database system** (including Oracle, PostgreSQL, MySQL, and Microsoft SQL Server) supports general assertions.
- As a direct engineering consequence, **triggers** are employed to emulate assertions selectively and efficiently, firing only on explicit modification events at the row level.

---

#### 2. Detailed Step-by-Step Solution

##### Part a. SQL Query Detecting Violating Combinations

To detect all `(instructor, section)` combinations where an instructor teaches two sections in different classrooms during the same semester, year, and time slot, we perform a self-join of the cross-product between `teaches` and `section`.

Let $T_1, S_1$ represent the first section taught by instructor $\text{ID}$, and $T_2, S_2$ represent a second section taught by the same instructor. A violation occurs if and only if:
1. $T_1.\text{ID} = T_2.\text{ID}$ (identical instructor),
2. $T_1.\text{semester} = T_2.\text{semester}$ and $T_1.\text{year} = T_2.\text{year}$ (same academic term),
3. $S_1.\text{time\_slot\_id} = S_2.\text{time\_slot\_id}$ (temporal collision),
4. $(S_1.\text{building} \neq S_2.\text{building} \lor S_1.\text{room\_number} \neq S_2.\text{room\_number})$ (spatial disparity),
5. $(T_1.\text{course\_id} \neq T_2.\text{course\_id} \lor T_1.\text{sec\_id} \neq T_2.\text{sec\_id})$ (distinct course sections).

```sql
-- Solution for Part (a): Detecting constraint violations
SELECT DISTINCT 
    T1.ID AS instructor_id,
    T1.course_id,
    T1.sec_id,
    T1.semester,
    T1.year,
    S1.building AS classroom_building,
    S1.room_number AS classroom_room,
    S1.time_slot_id
FROM 
    teaches T1
    JOIN section S1 
      ON T1.course_id = S1.course_id 
     AND T1.sec_id = S1.sec_id 
     AND T1.semester = S1.semester 
     AND T1.year = S1.year
    JOIN teaches T2 
      ON T1.ID = T2.ID 
     AND T1.semester = T2.semester 
     AND T1.year = T2.year
    JOIN section S2 
      ON T2.course_id = S2.course_id 
     AND T2.sec_id = S2.sec_id 
     AND T2.semester = S2.semester 
     AND T2.year = S2.year
WHERE 
    S1.time_slot_id = S2.time_slot_id
    AND (S1.building <> S2.building OR S1.room_number <> S2.room_number)
    AND (T1.course_id <> T2.course_id OR T1.sec_id <> T2.sec_id);
```

*Query Mechanics:*
- The `DISTINCT` keyword eliminates duplicate reports resulting from the symmetric pair matching $(T_1, T_2)$ and $(T_2, T_1)$.
- If an instructor teaches Section $A$ in Taylor 310 and Section $B$ in Painter 100 during time slot `F`, both rows appear in the output, pinpointing the conflicting schedules.

##### Part b. SQL Assertion Formulation

An SQL assertion must evaluate to `TRUE` for all valid database states. We specify that there must **not exist** any instructor who teaches conflicting sections:

```sql
-- Solution for Part (b): Standard SQL Assertion
CREATE ASSERTION instructor_classroom_conflict CHECK (
    NOT EXISTS (
        SELECT T1.ID
        FROM 
            teaches T1 
            JOIN section S1 
              ON T1.course_id = S1.course_id 
             AND T1.sec_id = S1.sec_id 
             AND T1.semester = S1.semester 
             AND T1.year = S1.year,
            teaches T2 
            JOIN section S2 
              ON T2.course_id = S2.course_id 
             AND T2.sec_id = S2.sec_id 
             AND T2.semester = S2.semester 
             AND T2.year = S2.year
        WHERE 
            T1.ID = T2.ID
            AND T1.semester = T2.semester 
            AND T1.year = T2.year
            AND S1.time_slot_id = S2.time_slot_id
            AND (S1.building <> S2.building OR S1.room_number <> S2.room_number)
            AND (T1.course_id <> T2.course_id OR T1.sec_id <> T2.sec_id)
    )
);
```

*Assertion Semantics:*
- The database system evaluates the `CHECK` clause before committing any transaction that modifies either `teaches` or `section`.
- If the inner subquery returns one or more tuples, the condition `NOT EXISTS (...)` evaluates to `FALSE`, causing the entire transaction to abort and roll back.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Strategy & Rubric Breakdown
> - **The "Assertion vs. Trigger" Theory Question:** RUET examiners frequently ask: *"Why are triggers used instead of assertions in modern database applications?"* (e.g., related to RUET 2018 Q.8(a) and 2020 Q.8(a)). The answer must highlight:
>   1. **Performance Cost:** Assertions require global re-evaluation on all modifying operations across all participating tables.
>   2. **Vendor Support:** Assertions are part of ANSI SQL-92/SQL:1999 standard but are omitted by Oracle, PostgreSQL, and MySQL.
>   3. **Imperative Control:** Triggers allow localized, row-level checking (`BEFORE INSERT OR UPDATE`) with immediate termination and detailed diagnostic messages.
> - **Common Student Pitfalls:**
>   - *Pitfall 1:* Forgetting to match `semester` and `year`. An instructor teaching in Painter 100 in Fall 2024 and Taylor 310 in Spring 2025 at time slot `F` is **not** a conflict!
>   - *Pitfall 2:* Neglecting the condition `(T1.course_id <> T2.course_id OR T1.sec_id <> T2.sec_id)`. Joining a section with itself would compare identical classrooms and satisfy equality, but checking `<>` prevents trivial self-comparisons.

---

### Exercise 5.5 · Enforcing Cross-Relation Schedule Constraints via Triggers

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.3 (*Triggers*), Page 233.
> - **Subtopic Mapping:** `T07.1` — What a trigger is, its purposes, and its syntax (ECA architecture, cross-relation integrity).
> - **Key Concepts:** `BEFORE INSERT OR UPDATE` triggers, Event-Condition-Action (ECA) model, Mutating table problem, Transition variables (`NEW` / `OLD`).
> - **Difficulty & RUET Relevance:** Direct mirror to RUET semester final design problems (e.g., RUET 2023 Q.6(b), 2024 Q.6(b)).

**Question (Silberschatz 7e Exercise 5.5).**
> Show how to enforce the constraint “an instructor cannot teach two different sections in a semester in the same time slot.” using a trigger (remember that the constraint can be violated by changes to the *teaches* relation as well as to the *section* relation).

---

#### 1. Core Principles & Concept Overview

##### Violation Vector Analysis
The constraint states:
$$
\forall t_1, t_2 \in \text{teaches}, \quad (t_1.\text{ID} = t_2.\text{ID} \land t_1.\text{semester} = t_2.\text{semester} \land t_1.\text{year} = t_2.\text{year} \land t_1 \neq t_2) \implies \text{slot}(t_1) \neq \text{slot}(t_2)
$$

This invariant can be compromised along two distinct mutation paths:
1. **Mutation on `teaches`:**
   - An `INSERT` adds a teaching assignment for an instructor whose new section coincides with an existing section already assigned to that instructor in the same term.
   - An `UPDATE` modifies the instructor `ID` or the section keys (`course_id`, `sec_id`, `semester`, `year`) of an existing assignment.
2. **Mutation on `section`:**
   - An `UPDATE` changes the `time_slot_id` of an existing section, creating a temporal overlap with another section already taught by an instructor assigned to that section.
   - (An `INSERT` on `section` alone cannot violate the constraint because no instructor is assigned to that new section until an insertion occurs in `teaches`).

##### Trigger Execution Phase: `BEFORE` vs. `AFTER`
A `BEFORE` row-level trigger is architecturally superior for constraint validation:
- It intercepts invalid data **before** disk writes, page splits, or index leaf insertions occur.
- If a collision is detected, calling `RAISE EXCEPTION` or `SIGNAL SQLSTATE '45000'` immediately aborts the SQL statement, eliminating the overhead of rolling back persistent database changes.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Trigger on the `teaches` Relation

When an assignment is inserted or updated in `teaches`, we verify that the instructor does not already teach another section during the time slot of the assigned section.

###### ANSI SQL / PostgreSQL PL/pgSQL Implementation:

```sql
-- Step 1A: Validation function for teaches
CREATE OR REPLACE FUNCTION check_instructor_teaches_overlap()
RETURNS TRIGGER AS $func$
DECLARE
    v_time_slot_id VARCHAR(10);
    v_conflict_count INTEGER;
BEGIN
    -- 1. Retrieve the time_slot_id of the section being assigned
    SELECT time_slot_id 
    INTO v_time_slot_id
    FROM section
    WHERE course_id = NEW.course_id
      AND sec_id    = NEW.sec_id
      AND semester  = NEW.semester
      AND year      = NEW.year;

    -- If the section has no assigned time slot, no schedule conflict can occur
    IF v_time_slot_id IS NULL THEN
        RETURN NEW;
    END IF;

    -- 2. Count existing sections taught by this instructor in the same term and time slot
    SELECT COUNT(*)
    INTO v_conflict_count
    FROM teaches T
    JOIN section S 
      ON T.course_id = S.course_id
     AND T.sec_id    = S.sec_id
     AND T.semester  = S.semester
     AND T.year      = S.year
    WHERE T.ID        = NEW.ID
      AND T.semester  = NEW.semester
      AND T.year      = NEW.year
      AND S.time_slot_id = v_time_slot_id
      -- Exclude the current row if this is an UPDATE operation
      AND NOT (T.course_id = NEW.course_id 
               AND T.sec_id = NEW.sec_id 
               AND T.semester = NEW.semester 
               AND T.year = NEW.year);

    -- 3. If a conflict exists, abort the transaction
    IF v_conflict_count > 0 THEN
        RAISE EXCEPTION 'Schedule Conflict: Instructor % already teaches a section in time slot % for % %.',
            NEW.ID, v_time_slot_id, NEW.semester, NEW.year;
    END IF;

    RETURN NEW;
END;
$func$ LANGUAGE plpgsql;

-- Step 1B: Create the trigger on teaches
CREATE TRIGGER trg_check_teaches_schedule
BEFORE INSERT OR UPDATE OF ID, course_id, sec_id, semester, year
ON teaches
FOR EACH ROW
EXECUTE FUNCTION check_instructor_teaches_overlap();
```

##### Step 2: Trigger on the `section` Relation

When a section's schedule is rescheduled (`UPDATE` of `time_slot_id`), we must ensure that no instructor currently assigned to teach this section has another section in that same new time slot.

```sql
-- Step 2A: Validation function for section time_slot changes
CREATE OR REPLACE FUNCTION check_section_timeslot_overlap()
RETURNS TRIGGER AS $func$
DECLARE
    v_conflict_count INTEGER;
    v_instructor_id VARCHAR(5);
BEGIN
    -- Check only if the time_slot_id has actually changed
    IF NEW.time_slot_id IS DISTINCT FROM OLD.time_slot_id THEN
        
        -- Identify any instructor teaching this section who has another section at NEW.time_slot_id
        SELECT COUNT(*), MIN(T1.ID)
        INTO v_conflict_count, v_instructor_id
        FROM teaches T1
        JOIN teaches T2 
          ON T1.ID = T2.ID 
         AND T1.semester = T2.semester 
         AND T1.year = T2.year
        JOIN section S2 
          ON T2.course_id = S2.course_id 
         AND T2.sec_id = S2.sec_id 
         AND T2.semester = S2.semester 
         AND T2.year = S2.year
        WHERE T1.course_id = NEW.course_id
          AND T1.sec_id    = NEW.sec_id
          AND T1.semester  = NEW.semester
          AND T1.year      = NEW.year
          AND S2.time_slot_id = NEW.time_slot_id
          -- Exclude self-matching section
          AND NOT (T2.course_id = NEW.course_id 
                   AND T2.sec_id = NEW.sec_id 
                   AND T2.semester = NEW.semester 
                   AND T2.year = NEW.year);

        IF v_conflict_count > 0 THEN
            RAISE EXCEPTION 'Schedule Conflict: Instructor % teaching this section has a conflicting section in time slot %.',
                v_instructor_id, NEW.time_slot_id;
        END IF;

    END IF;

    RETURN NEW;
END;
$func$ LANGUAGE plpgsql;

-- Step 2B: Create the trigger on section
CREATE TRIGGER trg_check_section_timeslot
BEFORE UPDATE OF time_slot_id
ON section
FOR EACH ROW
EXECUTE FUNCTION check_section_timeslot_overlap();
```

##### Step 3: Dialect-Specific Note — The Oracle Mutating-Table Constraint
In Oracle Database, executing a row-level trigger on table `teaches` that queries `teaches` raises:
`ORA-04091: table TEACHES is mutating, trigger/function may not see it`.

*Solution in Oracle PL/SQL:*
Oracle resolves this using a **Compound Trigger** (`FOR EACH ROW` captures the modified keys into an in-memory PL/SQL collection, and `AFTER STATEMENT` performs the validation query against the finalized table).

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Examiner Scoring Criteria
> 1. **Multi-Table Coverage (50% of Marks):** The single most prevalent blunder in RUET final scripts is writing a trigger solely on `teaches`. The problem explicitly reminds: *(remember that the constraint can be violated by changes to the teaches relation as well as to the section relation)*. Full marks require writing **both** triggers.
> 2. **Correct Trigger Timing (`BEFORE`):** Using `BEFORE` allows immediate rejection without cascading rollbacks.
> 3. **Proper Exception Signaling:** Examiners look for standard error signaling syntax (`RAISE EXCEPTION`, `SIGNAL SQLSTATE '45000'`, or Oracle's `RAISE_APPLICATION_ERROR(-20001, '...')`).

---

### Exercise 5.7 · Conditional Referential Cleanup and Cascades via Triggers

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.3 (*Triggers*), Page 234.
> - **Subtopic Mapping:** `T07.1` — What a trigger is, its purposes, and its syntax (referential integrity, automatic cascades).
> - **Key Concepts:** `AFTER DELETE` triggers, Referential integrity simulation, Conditional cascading deletion, Business logic automation.
> - **Difficulty & RUET Relevance:** Core question illustrating how triggers automate complex referential garbage collection.

**Question (Silberschatz 7e Exercise 5.7).**
> Consider the bank database of Figure 5.21. Write an SQL trigger to carry out the following action: On delete of an account, for each customer-owner of the account, check if the owner has any remaining accounts, and if she does not, delete her from the *depositor* relation.

---

#### 1. Core Principles & Concept Overview

##### Schema Analysis (Figure 5.21)
The banking database relations involved are:
- $\text{account}(\underline{\text{account\_number}}, \text{branch\_name}, \text{balance})$
- $\text{depositor}(\underline{\text{customer\_name}, \text{account\_number}})$
- $\text{customer}(\underline{\text{customer\_name}}, \text{customer\_street}, \text{customer\_city})$

##### Disambiguation of Textbook Wording
In standard relational database design:
- The `depositor` table is a junction table storing the $(M:N)$ relationship between `customer` and `account`.
- When an account tuple is deleted, any tuple in `depositor` referencing `OLD.account_number` must be removed immediately to preserve foreign key referential integrity.
- If a customer holds **no other accounts** at the bank, removing them from `depositor` leaves them with 0 accounts. In enterprise practice, if a customer has no remaining accounts or loans, they are also removed from `customer`.
- We provide the exact solution implementing the literal textbook requirement (deleting remaining orphan associations from `depositor`), and demonstrate the standard cascade extension to `customer`.

##### Trigger Mechanics
- **Event:** `AFTER DELETE ON account`
- **Granularity:** `FOR EACH ROW`
- **Transition Variable:** `OLD.account_number` contains the identifier of the deleted account.
- **Timing:** `AFTER DELETE` ensures that the row has been purged from `account`, allowing subqueries to evaluate remaining account counts cleanly.

---

#### 2. Detailed Step-by-Step Solution

##### Implementation in Standard SQL / PostgreSQL PL/pgSQL

```sql
-- Step 1: Create the cleanup function
CREATE OR REPLACE FUNCTION clean_orphan_depositors()
RETURNS TRIGGER AS $func$
DECLARE
    cust_rec RECORD;
    v_remaining_accounts INTEGER;
BEGIN
    -- Loop over all customers who were associated with the deleted account
    FOR cust_rec IN 
        SELECT customer_name 
        FROM depositor 
        WHERE account_number = OLD.account_number
    LOOP
        -- First, delete the association for the deleted account
        DELETE FROM depositor
        WHERE customer_name = cust_rec.customer_name
          AND account_number = OLD.account_number;

        -- Check if this customer owns any OTHER accounts
        SELECT COUNT(*)
        INTO v_remaining_accounts
        FROM depositor
        WHERE customer_name = cust_rec.customer_name;

        -- If the customer has no remaining accounts, purge any orphaned depositor records
        -- (and optionally clean from customer table)
        IF v_remaining_accounts = 0 THEN
            -- In strict adherence to textbook phrasing:
            DELETE FROM depositor
            WHERE customer_name = cust_rec.customer_name;
            
            -- Enterprise extension: Remove customer from master entity table
            -- DELETE FROM customer WHERE customer_name = cust_rec.customer_name;
        END IF;

    END LOOP;

    RETURN OLD;
END;
$func$ LANGUAGE plpgsql;

-- Step 2: Attach the trigger to the account relation
CREATE TRIGGER trg_account_delete_cleanup
AFTER DELETE ON account
FOR EACH ROW
EXECUTE FUNCTION clean_orphan_depositors();
```

##### ANSI SQL:1999 Standard Trigger Formulation

```sql
CREATE TRIGGER account_delete_depositor_cleanup
AFTER DELETE ON account
REFERENCING OLD ROW AS old_account
FOR EACH ROW
BEGIN
    -- Delete the specific deleted account entry from depositor
    DELETE FROM depositor
    WHERE account_number = old_account.account_number;

    -- Delete any customer from depositor who now has zero accounts in the bank
    DELETE FROM depositor
    WHERE customer_name IN (
        SELECT D.customer_name
        FROM depositor D
        WHERE D.customer_name NOT IN (
            SELECT D2.customer_name
            FROM depositor D2
            JOIN account A ON D2.account_number = A.account_number
        )
    );
END;
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Examiner Scoring Rubric
> - **Looping over Joint Accounts:** An account can have multiple joint owners (e.g., Alice and Bob share account `A-101`). A single `DELETE FROM account WHERE account_number = 'A-101'` affects multiple customers. Top-scoring solutions must handle multiple owners via a cursor, loop, or set-based `IN` subquery.
> - **Timing (`AFTER` vs `BEFORE`):** Always specify `AFTER DELETE`. If executed `BEFORE DELETE`, the account still exists in `account`, so counting remaining accounts returns an inaccurate tally unless explicit exclusion logic (`account_number <> OLD.account_number`) is coded.

---

### Exercise 5.19 · Implementing `ON DELETE CASCADE` using the Trigger Mechanism

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.3 (*Triggers*), Page 236.
> - **Subtopic Mapping:** `T07.1` — What a trigger is, its purposes, and its syntax (cascading actions, foreign key simulation).
> - **Key Concepts:** Referential integrity enforcement, Declarative vs Imperative constraints, `AFTER DELETE` triggers, Transition variable `OLD`.
> - **Difficulty & RUET Relevance:** Classic textbook problem frequently adapted into RUET theoretical and practical exam questions.

**Question (Silberschatz 7e Exercise 5.19).**
> Suppose there are two relations $r$ and $s$, such that the foreign key $B$ of $r$ references the primary key $A$ of $s$. Describe how the trigger mechanism can be used to implement the **on delete cascade** option when a tuple is deleted from $s$.

---

#### 1. Core Principles & Concept Overview

##### Declarative Referential Integrity
In SQL DDL, declarative referential integrity is established as:
```sql
CREATE TABLE r (
    ...
    B VARCHAR(20),
    FOREIGN KEY (B) REFERENCES s(A) ON DELETE CASCADE
);
```
Under declarative cascading deletion:
- When a tuple $t_s \in s$ is deleted, the DBMS storage engine automatically deletes all child tuples $\{t_r \in r \mid t_r.B = t_s.A\}$.

##### Simulating Declarative Semantics with Triggers
When declarative foreign keys are unsupported, disabled, or require supplemental processing (such as logging audit trails or cascading across distributed partitions), an active ECA trigger can emulate this behavior.

##### ECA Architectural Breakdown
- **Event:** `DELETE ON s` (the parent relation).
- **Condition:** None (unconditional cascade) or `WHERE r.B = OLD.A`.
- **Action:** Execute `DELETE FROM r WHERE r.B = OLD.A`.
- **Granularity:** `FOR EACH ROW` — required because the primary key value $A$ must be extracted individually for each deleted parent tuple.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Trigger Specification in Standard SQL:1999

```sql
CREATE TRIGGER trg_cascade_delete_s_to_r
AFTER DELETE ON s
REFERENCING OLD ROW AS old_parent
FOR EACH ROW
BEGIN
    DELETE FROM r
    WHERE r.B = old_parent.A;
END;
```

##### Step 2: Production Implementations Across Major Dialects

###### PostgreSQL PL/pgSQL:
```sql
CREATE OR REPLACE FUNCTION fn_cascade_s_to_r()
RETURNS TRIGGER AS $func$
BEGIN
    DELETE FROM r WHERE r.B = OLD.A;
    RETURN OLD;
END;
$func$ LANGUAGE plpgsql;

CREATE TRIGGER trg_cascade_s_to_r
AFTER DELETE ON s
FOR EACH ROW
EXECUTE FUNCTION fn_cascade_s_to_r();
```

###### Oracle PL/SQL:
```sql
CREATE OR REPLACE TRIGGER trg_cascade_s_to_r
AFTER DELETE ON s
FOR EACH ROW
BEGIN
    DELETE FROM r
    WHERE r.B = :OLD.A;
END;
/
```

###### MySQL:
```sql
DELIMITER //
CREATE TRIGGER trg_cascade_s_to_r
AFTER DELETE ON s
FOR EACH ROW
BEGIN
    DELETE FROM r
    WHERE r.B = OLD.A;
END //
DELIMITER ;
```

##### Step 3: Comparative Architectural Analysis

| Dimension | Declarative `ON DELETE CASCADE` | Trigger-Based Emulation |
| :--- | :--- | :--- |
| **Execution Layer** | Kernel storage engine (C/C++ core). | Procedural SQL engine / Interpreter. |
| **Performance** | Maximum throughput; bulk index-level deletes. | Higher overhead due to context switches and per-row invocation. |
| **Customizability** | None (all-or-nothing deletion). | Full (can record audit logs, archive rows, or conditionally cascade). |
| **Multi-Tier Cascades** | Automatically resolved by DBMS dependency graph. | Subject to trigger nesting limits and recursion constraints. |

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Answering Blueprint
> When answering this question in a RUET final:
> 1. Explicitly state the **triggering event** (`DELETE ON s`).
> 2. Specify the **granularity** (`FOR EACH ROW`).
> 3. State why `OLD.A` is referenced (the deleted parent key).
> 4. Present the complete `CREATE TRIGGER` statement.
> 5. Mention timing: `AFTER DELETE` ensures that if deletion of the parent fails (e.g., due to check constraints or locks), child records are not erroneously deleted.

---

### Exercise 5.20 · Trigger Nesting Limits, Cascading Depth, and Recursion Control

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.3 (*Triggers*), Page 236.
> - **Subtopic Mapping:** `T07.1` — What a trigger is, its purposes, and its syntax (cascading triggers, execution stack, infinite recursion).
> - **Key Concepts:** Direct vs Indirect trigger recursion, Call stack overflow, Transaction lock exhaustion, Halting problem, Vendor nesting limits.
> - **Difficulty & RUET Relevance:** Fundamental system-architecture question explaining transactional stability in high-concurrency database engines.

**Question (Silberschatz 7e Exercise 5.20).**
> The execution of a trigger can cause another action to be triggered. Most database systems place a limit on how deep the nesting can be. Explain why they might place such a limit.

---

#### 1. Core Principles & Concept Overview

##### Cascading and Recursive Triggers
When a trigger action executes an `INSERT`, `UPDATE`, or `DELETE`, that action is itself a database event that may fire another trigger. This phenomenon is known as **trigger cascading** or **chained execution**.

Two distinct forms of trigger recursion exist:
1. **Direct Recursion (Self-Triggering):**
   - An `AFTER UPDATE` trigger on table $T$ executes an `UPDATE` on the same table $T$:
   $$
   T \xrightarrow{\text{UPDATE}} \text{Trigger}_T \xrightarrow{\text{UPDATE}} T \xrightarrow{\text{UPDATE}} \text{Trigger}_T \to \dots
   $$
2. **Indirect Recursion (Mutual / Cyclic Triggering):**
   - A trigger on table $A$ modifies table $B$, whose trigger in turn modifies table $A$:
   $$
   A \xrightarrow{\text{UPDATE}} \text{Trigger}_A \xrightarrow{\text{INSERT}} B \xrightarrow{\text{INSERT}} \text{Trigger}_B \xrightarrow{\text{UPDATE}} A \to \dots
   $$

```text
Direct Recursion:
[Table A] ---> (Trigger A) ---> [Table A] ---> (Trigger A) ---> ... [Infinite Loop]

Indirect / Cyclic Recursion:
[Table A] ---> (Trigger A) ---> [Table B] ---> (Trigger B) ---> [Table A] ---> ...
```

---

#### 2. Detailed Step-by-Step Solution

##### The Four Engineering Justifications for Nesting Limits

Database management systems impose strict limits on nesting depth for four critical technical reasons:

###### 1. Prevention of Infinite Recursion and Process Freezes
- In procedural languages, detecting whether an arbitrary sequence of nested triggers will eventually terminate is reducible to Turing's **Halting Problem** (undecidable at compile-time).
- In the absence of an execution depth bound, buggy or cyclic business logic triggers an infinite loop, freezing the worker thread indefinitely.

###### 2. Execution Stack Protection & Memory Exhaustion
- Each nested trigger invocation allocates an in-memory activation record (call stack frame) on the database process stack.
- Each stack frame stores:
  - Local procedural variables and parameter bindings.
  - Snapshot transaction identifiers and sub-transaction savepoints.
  - Active cursor descriptors and query plan contexts.
- Unbounded nesting exhausts the process stack, triggering a fatal OS kernel fault (`SIGSEGV` or Stack Overflow Exception) that crashes the entire database server process.

###### 3. Transaction Log Bloat and Concurrency Convoy
- In relational DBMSs, all actions within a trigger cascade run within the parent transaction's ACID boundary.
- Uncommitted cascading operations accumulate exclusive row and page write locks (`X-locks`) without releasing them.
- Deep cascades exhaust the system's lock table and write massive volumes of uncommitted undo/redo log records to disk, stalling other concurrent transactions and precipitating system-wide deadlocks.

###### 4. Determinism, Debuggability, and Semantic Sanity
- Deeply nested cascades obscure transaction side effects, making enterprise audit trails and debugging intractable. Restricting nesting forces software engineers to design clean, predictable batch procedures rather than opaque recursive triggers.

##### Vendor-Specific Nesting Implementations

| Database System | Default Nesting Depth Limit | Behavior When Exceeded | Configuration / Control Mechanism |
| :--- | :---: | :--- | :--- |
| **Oracle Database** | **32 levels** | Throws `ORA-00036: maximum number of recursive SQL levels (50) exceeded`. | Enforced internally via kernel call stack. |
| **Microsoft SQL Server** | **32 levels** | Error `217: Maximum stored procedure, function, trigger, or view nesting level exceeded (limit 32)`. | `sp_configure 'nested triggers', 0/1;`<br>`ALTER DATABASE ... SET RECURSIVE_TRIGGERS OFF;` |
| **PostgreSQL** | Constrained by `max_stack_depth` (default 2 MB). | Server terminates transaction with `ERROR: stack depth limit exceeded`. | `SET max_stack_depth = '4MB';` |
| **MySQL** | Direct recursion prohibited on row triggers. | Throws `ERROR 1442: Can't update table in stored function/trigger because it is already used`. | Strict compile-time validation on target table mutation. |

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Quick-Scoring Bullet Points for RUET
> If asked in Section B of a RUET final (e.g., as a 3 to 5 mark question):
> - **Definition:** Define trigger cascading ($T_1 \to T_2$) and direct/indirect recursion.
> - **Draw a 2-node cycle diagram:** Table A $\leftrightarrow$ Table B.
> - **Four Key Drivers:** State: (1) Infinite loop avoidance, (2) Stack overflow prevention, (3) Transaction lock/log saturation, (4) Debuggability.
> - **Specific Limit:** Mention the industry standard ceiling of **32 levels** (Oracle and SQL Server).



## T07.3 · Stored Procedures, Functions, and Application Database Programming (SQL/PSM, PL/SQL, JDBC, ODBC)

---

### Exercise 5.1 · Analyzing Hierarchical Transitive Closure in JDBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 232.
> - **Subtopic Mapping:** `T07.3` — Implement a trigger / stored procedure (programmatic queries, hierarchy traversal, transitive closure).
> - **Key Concepts:** JDBC programmatic execution, Dynamic query looping, Hierarchical / recursive data traversal, Transitive closure.
> - **Difficulty & RUET Relevance:** Excellent code-reading exercise demonstrating how client applications simulate recursive queries when SQL recursion is unavailable.

**Question (Silberschatz 7e Exercise 5.1).**
> Consider the following relations for a company database:
> - `emp (ename, dname, salary)`
> - `mgr (ename, mname)`
> 
> and the Java code in Figure 5.20, which uses the JDBC API. Assume that the userid, password, machine name, etc. are all okay. Describe in concise English what the Java program does. (That is, produce an English sentence like “It finds the manager of the toy department,” not a line-by-line description of what each Java statement does.)

---

#### 1. Core Principles & Concept Overview

##### Schema and Hierarchy Representation
The `mgr` relation models a directed acyclic hierarchy (tree) of corporate supervision:
- Each tuple $(\text{ename}, \text{mname})$ asserts that $\text{mname}$ is the direct manager of employee $\text{ename}$.
- A top-level executive (e.g., the CEO or Managing Director) has no entry in `mgr` as an employee, or their `mname` is `NULL`.

##### Decompilation of the Java Control Flow (Figure 5.20)
The code executes the following sequence:
1. Opens a JDBC connection to an Oracle database.
2. Prepares the parameterized query: `SELECT mname FROM mgr WHERE ename = ?`.
3. Sets the initial search variable: `empName = "dog"`.
4. Enters a `do-while` loop:
   - Binds `empName` to placeholder `1`.
   - Executes the query, retrieving `result`.
   - Advances cursor with `more = result.next()`.
   - If a manager tuple exists (`more == true`):
     - Reads `empName = result.getString("mname")`.
     - Prints the manager's name: `System.out.println(empName)`.
     - Loops back using the manager's name as the new employee name.
   - The loop terminates when `result.next()` returns `false` (no supervisor exists for the current person).

---

#### 2. Detailed Step-by-Step Solution

##### Concise English Description
> **The program prints the complete upward chain of management (all direct and indirect managers) for the employee named "dog", tracing sequentially up the corporate hierarchy until reaching the top executive who has no manager.**

##### Algorithmic Comparison: Client-Side Traversal vs. Recursive SQL

###### 1. Client-Side Programmatic Traversal (Figure 5.20)
- **Mechanics:** The client initiates an independent database network round-trip for each tier of the management tree.
- **Network Latency:** If the hierarchy depth is $H$, the application incurs $H$ sequential round-trip times (RTTs).
- **Complexity:** $O(H)$ network transactions.

###### 2. Modern Database-Tier Equivalent (SQL:1999 Recursive CTE)
Instead of repetitive client-server round-trips, the identical transitive closure can be evaluated entirely within the database kernel in a single round-trip:

```sql
WITH RECURSIVE ManagerChain(mname, level) AS (
    -- Anchor member: Direct manager of 'dog'
    SELECT mname, 1
    FROM mgr
    WHERE ename = 'dog'
    
    UNION ALL
    
    -- Recursive member: Managers of managers
    SELECT M.mname, MC.level + 1
    FROM mgr M
    JOIN ManagerChain MC ON M.ename = MC.mname
)
SELECT mname 
FROM ManagerChain 
ORDER BY level;
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Code Reading Exam Rubric
> In RUET final exams, when asked to describe what a code segment does:
> - **Never write a statement-by-statement translation:** Avoid writing *"Line 1 imports java.sql, Line 4 opens a connection, Line 8 prepares a statement..."* (Examiners award zero marks for line-by-line regurgitation).
> - **State the Business Function:** State clearly: *"Finds all transitive superiors (ancestors in the management tree) of employee 'dog'."*
> - **Highlight the Loop Termination:** State that the loop terminates when a top manager without a supervisor is reached.

---

### Exercise 5.2 · Dynamic Tabular Result Set Formatting via JDBC Metadata

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 232.
> - **Subtopic Mapping:** `T07.3` — Stored procedures and application interfaces (JDBC metadata inspection, generic query processing).
> - **Key Concepts:** `ResultSetMetaData`, Dynamic schema inspection, 1-based indexing convention, Formatted console output.
> - **Difficulty & RUET Relevance:** Core practical question for database programming and laboratory examinations.

**Question (Silberschatz 7e Exercise 5.2).**
> Write a Java method using JDBC metadata features that takes a `ResultSet` as an input parameter and prints out the result in tabular form, with appropriate names as column headings.

---

#### 1. Core Principles & Concept Overview

##### Schema Introspection in JDBC
When executing dynamic queries whose projected attributes and types are unknown at compile-time, the JDBC application must inspect runtime metadata:
- Calling `rs.getMetaData()` returns an instance of `ResultSetMetaData`.
- **Key Inspection Methods:**
  - `rsmd.getColumnCount()`: Returns the total number of projected attributes ($N$).
  - `rsmd.getColumnLabel(int i)`: Returns the display title/alias for column $i$.
  - `rsmd.getColumnTypeName(int i)`: Returns the database data type name.
  - `rsmd.getColumnDisplaySize(int i)`: Returns the nominal character display width.

##### Crucial Implementation Rule: 1-Based Indexing
In JDBC, column indices range from $1$ to $N$, **not** $0$ to $N-1$. Accessing index $0$ throws an `SQLException: Column index out of range`.

---

#### 2. Detailed Step-by-Step Solution

##### Complete Java Implementation

```java
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class TabularPrinter {

    /**
     * Prints any JDBC ResultSet in dynamic, formatted tabular format.
     * 
     * @param rs The active, open ResultSet positioned before the first row.
     * @throws SQLException If database metadata or data extraction fails.
     */
    public static void printResultSet(ResultSet rs) throws SQLException {
        if (rs == null) {
            System.out.println("ResultSet is null.");
            return;
        }

        // 1. Extract metadata from the ResultSet
        ResultSetMetaData rsmd = rs.getMetaData();
        int columnCount = rsmd.getColumnCount();

        if (columnCount == 0) {
            System.out.println("Query returned 0 columns.");
            return;
        }

        // 2. Determine column labels and initialize dynamic display widths
        String[] headers = new String[columnCount];
        int[] columnWidths = new int[columnCount];

        for (int i = 1; i <= columnCount; i++) {
            // Prefer getColumnLabel over getColumnName to support SQL aliases (AS)
            String label = rsmd.getColumnLabel(i);
            headers[i - 1] = (label != null) ? label : ("Col_" + i);
            columnWidths[i - 1] = Math.max(headers[i - 1].length(), 10);
        }

        // 3. Buffer rows in memory to compute optimal column alignment widths
        List<String[]> rows = new ArrayList<>();
        while (rs.next()) {
            String[] rowData = new String[columnCount];
            for (int i = 1; i <= columnCount; i++) {
                String val = rs.getString(i);
                if (rs.wasNull() || val == null) {
                    val = "NULL";
                }
                rowData[i - 1] = val;
                columnWidths[i - 1] = Math.max(columnWidths[i - 1], val.length());
            }
            rows.add(rowData);
        }

        // 4. Construct the horizontal divider line (+-------+-------+)
        StringBuilder divider = new StringBuilder("+");
        for (int w : columnWidths) {
            divider.append("-".repeat(w + 2)).append("+");
        }
        String separatorLine = divider.toString();

        // 5. Print the Table Header
        System.out.println(separatorLine);
        System.out.print("|");
        for (int i = 0; i < columnCount; i++) {
            System.out.printf(" %-" + columnWidths[i] + "s |", headers[i]);
        }
        System.out.println();
        System.out.println(separatorLine);

        // 6. Print all buffered data rows
        if (rows.isEmpty()) {
            System.out.println("| (0 rows returned) ".concat(" ".repeat(separatorLine.length() - 21)).concat("|"));
        } else {
            for (String[] row : rows) {
                System.out.print("|");
                for (int i = 0; i < columnCount; i++) {
                    System.out.printf(" %-" + columnWidths[i] + "s |", row[i]);
                }
                System.out.println();
            }
        }
        System.out.println(separatorLine);
        System.out.println("Total Rows: " + rows.size());
    }
}
```

##### Handling Edge Cases
- **Null Values:** Explicitly inspected using `rs.wasNull()` or checking for Java `null`, printed safely as `"NULL"` to avoid `NullPointerException`.
- **Empty Result Sets:** Displays header metadata cleanly with a `(0 rows returned)` status row.
- **Column Aliases:** Utilizes `rsmd.getColumnLabel(i)` rather than `rsmd.getColumnName(i)` so that SQL expressions like `SELECT COUNT(*) AS total` display as `total` rather than internal engine names.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] High-Yield Scoring Checklist
> 1. Calling `rs.getMetaData()` to obtain `ResultSetMetaData`.
> 2. Using `rsmd.getColumnCount()` to determine row length dynamically.
> 3. Iterating columns using **1-based indexing** (`for (int i = 1; i <= colCount; i++)`).
> 4. Displaying headers using `getColumnLabel(i)` or `getColumnName(i)`.
> 5. Iterating rows with `while (rs.next())`.

---

### Exercise 5.12 · Comprehensive University Teaching Record Application in Java JDBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 235.
> - **Subtopic Mapping:** `T07.3` — Database application programming (interactive CLI, query parameterization, authentication, input validation).
> - **Key Concepts:** Secure login loop, Parameterized queries (`PreparedStatement`), SQL injection immunity, Aggregation with outer joins, Exception recovery.
> - **Difficulty & RUET Relevance:** Full-scale database application development task demonstrating enterprise JDBC design.

**Question (Silberschatz 7e Exercise 5.12).**
> Write a Java program that allows university administrators to print the teaching record of an instructor.
> 
> **a.** Start by having the user input the login ID and password; then open the proper connection.  
> **b.** The user is asked next for a search substring and the system returns (ID, name) pairs of instructors whose names match the substring. Use the `like ('%substring%')` construct in SQL to do this. If the search comes back empty, allow continued searches until there is a nonempty result.  
> **c.** Then the user is asked to enter an ID number, which is a number between 0 and 99999. Once a valid number is entered, check if an instructor with that ID exists. If there is no instructor with the given ID, print a reasonable message and quit.  
> **d.** If the instructor has taught no courses, print a message saying that. Otherwise print the teaching record for the instructor, showing the department name, course identifier, course title, section number, semester, year, and total enrollment (and sort those by `dept_name`, `course_id`, `year`, `semester`).
> 
> Test carefully for bad input. Make sure your SQL queries won’t throw an exception. At login, exceptions may occur since the user might type a bad password, but catch those exceptions and allow the user to try again.

---

#### 1. Core Principles & Concept Overview

##### Application Architecture
The program implements an interactive terminal interface communicating with the university relational database:
1. **Authentication Tier (Part a):** Secure connection retry loop.
2. **Fuzzy Search Tier (Part b):** Name filtering using SQL `LIKE ?` with parameterized wildcards (`%` + input + `%`).
3. **Validation Tier (Part c):** Integer boundary check ($0 \le \text{ID} \le 99999$) and relational existence verification.
4. **Analytical Query Tier (Part d):** Multi-table join across `teaches`, `section`, `course`, and `takes`.
   - To correctly capture sections that have **zero enrolled students**, we employ a `LEFT OUTER JOIN` against `takes`. Using an inner join would omit empty classes entirely!

---

#### 2. Detailed Step-by-Step Solution

##### Complete Java Program

```java
import java.sql.*;
import java.util.Scanner;

public class InstructorTeachingRecord {

    private static final String DB_URL = "jdbc:postgresql://localhost:5432/university";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Connection conn = null;

        // =====================================================================
        // Part (a): Secure Connection Loop with Authentication Retry
        // =====================================================================
        while (conn == null) {
            System.out.println("=== University Administration Portal Login ===");
            System.out.print("Enter Database Username: ");
            String user = scanner.nextLine().trim();
            System.out.print("Enter Database Password: ");
            String password = scanner.nextLine().trim();

            try {
                conn = DriverManager.getConnection(DB_URL, user, password);
                System.out.println("Authentication successful! Connected to database.\n");
            } catch (SQLException e) {
                System.err.println("Login failed: " + e.getMessage());
                System.out.println("Please check your credentials and try again.\n");
            }
        }

        try {
            // =================================================================
            // Part (b): Instructor Substring Search Loop
            // =================================================================
            String searchSql = "SELECT ID, name FROM instructor WHERE name LIKE ? ORDER BY name";
            try (PreparedStatement searchStmt = conn.prepareStatement(searchSql)) {
                boolean foundResults = false;

                while (!foundResults) {
                    System.out.print("Enter instructor name search substring: ");
                    String sub = scanner.nextLine().trim();

                    if (sub.isEmpty()) {
                        System.out.println("Search string cannot be empty. Please retry.");
                        continue;
                    }

                    // Bind wildcard search safely to prevent SQL injection
                    searchStmt.setString(1, "%" + sub + "%");

                    try (ResultSet rs = searchStmt.executeQuery()) {
                        int matchCount = 0;
                        System.out.println("\nMatching Instructors:");
                        System.out.printf("%-10s | %-30s%n", "ID", "Name");
                        System.out.println("------------------------------------------");
                        
                        while (rs.next()) {
                            matchCount++;
                            System.out.printf("%-10s | %-30s%n", rs.getString("ID"), rs.getString("name"));
                        }

                        if (matchCount > 0) {
                            foundResults = true;
                            System.out.println("Found " + matchCount + " matching instructor(s).\n");
                        } else {
                            System.out.println("No instructors matched '" + sub + "'. Please try a different search.\n");
                        }
                    }
                }
            }

            // =================================================================
            // Part (c): Instructor ID Validation & Existence Check
            // =================================================================
            String selectedId = null;
            while (selectedId == null) {
                System.out.print("Enter Instructor ID (0 to 99999): ");
                String inputId = scanner.nextLine().trim();

                try {
                    int numericId = Integer.parseInt(inputId);
                    if (numericId < 0 || numericId > 99999) {
                        System.out.println("Invalid range! ID must be between 0 and 99999.");
                        continue;
                    }
                    selectedId = inputId;
                } catch (NumberFormatException e) {
                    System.out.println("Invalid format! Please enter an integer number.");
                }
            }

            // Verify existence of instructor ID in database
            String checkSql = "SELECT name, dept_name FROM instructor WHERE ID = ?";
            try (PreparedStatement checkStmt = conn.prepareStatement(checkSql)) {
                checkStmt.setString(1, selectedId);
                try (ResultSet rs = checkStmt.executeQuery()) {
                    if (!rs.next()) {
                        System.out.println("Error: Instructor with ID " + selectedId + " does not exist in the database.");
                        System.out.println("Terminating program.");
                        return;
                    }
                    System.out.println("Selected Instructor: " + rs.getString("name") + " (" + rs.getString("dept_name") + ")\n");
                }
            }

            // =================================================================
            // Part (d): Retrieve Teaching Record & Enrollment Statistics
            // =================================================================
            String recordSql = 
                "SELECT S.dept_name, S.course_id, C.title, S.sec_id, S.semester, S.year, " +
                "       COUNT(T.ID) AS total_enrollment " +
                "FROM teaches TC " +
                "JOIN section S " +
                "  ON TC.course_id = S.course_id AND TC.sec_id = S.sec_id " +
                " AND TC.semester = S.semester   AND TC.year = S.year " +
                "JOIN course C " +
                "  ON S.course_id = C.course_id " +
                "LEFT JOIN takes T " +
                "  ON S.course_id = T.course_id AND S.sec_id = T.sec_id " +
                " AND S.semester = T.semester   AND S.year = T.year " +
                "WHERE TC.ID = ? " +
                "GROUP BY S.dept_name, S.course_id, C.title, S.sec_id, S.semester, S.year " +
                "ORDER BY S.dept_name, S.course_id, S.year, S.semester";

            try (PreparedStatement recordStmt = conn.prepareStatement(recordSql)) {
                recordStmt.setString(1, selectedId);

                try (ResultSet rs = recordStmt.executeQuery()) {
                    if (!rs.isBeforeFirst()) {
                        // isBeforeFirst() returns false if the cursor contains 0 rows
                        System.out.println("Instructor with ID " + selectedId + " has taught no courses.");
                    } else {
                        System.out.println("=== Teaching Record for Instructor ID: " + selectedId + " ===");
                        System.out.printf("%-15s | %-10s | %-30s | %-6s | %-8s | %-6s | %-10s%n",
                                "Dept Name", "Course ID", "Course Title", "Sec", "Semester", "Year", "Enrollment");
                        System.out.println("---------------------------------------------------------------------------------------------------------");

                        int totalSections = 0;
                        while (rs.next()) {
                            totalSections++;
                            System.out.printf("%-15s | %-10s | %-30s | %-6s | %-8s | %-6d | %-10d%n",
                                    rs.getString("dept_name"),
                                    rs.getString("course_id"),
                                    rs.getString("title"),
                                    rs.getString("sec_id"),
                                    rs.getString("semester"),
                                    rs.getInt("year"),
                                    rs.getInt("total_enrollment"));
                        }
                        System.out.println("---------------------------------------------------------------------------------------------------------");
                        System.out.println("Total Sections Taught: " + totalSections);
                    }
                }
            }

        } catch (SQLException e) {
            System.err.println("Database execution error: " + e.getMessage());
            e.printStackTrace();
        } finally {
            if (conn != null) {
                try { conn.close(); } catch (SQLException e) { /* suppress */ }
            }
            scanner.close();
        }
    }
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Crucial Architecture Checks
> - **Outer Join for Enrollment:** Using `INNER JOIN takes` is a fatal flaw because sections with 0 enrolled students vanish from the report. Always use `LEFT JOIN takes`.
> - **SQL Injection Prevention:** Never construct SQL using string concatenation (`"WHERE name LIKE '%" + sub + "%'"`). Examiners deduct marks for unsafe string interpolation. Always use `PreparedStatement` with `setString(1, "%" + sub + "%")`.
> - **Input Validation:** Checking numeric range ($0 \le \text{ID} \le 99999$) via `try { Integer.parseInt(...) }` demonstrates defensive programming.

---

### Exercise 5.13 · Generic Schema-Agnostic Table Display Class (`MetaDisplay`) in Java

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 235.
> - **Subtopic Mapping:** `T07.3` — Application interfaces (dynamic schema reflection, metadata extraction).
> - **Key Concepts:** Metadata-driven architecture, `ResultSetMetaData`, Dynamic SQL execution, SQL Injection defense for identifiers.
> - **Difficulty & RUET Relevance:** Classic object-oriented database design question testing reflection and generic query rendering.

**Question (Silberschatz 7e Exercise 5.13).**
> Suppose you were asked to define a class `MetaDisplay` in Java, containing a method `static void printTable(String r)`; the method takes a relation name $r$ as input, executes the query “select * from r”, and prints the result out in tabular format, with the attribute names displayed in the header of the table.
> 
> **a.** What do you need to know about relation $r$ to be able to print the result in the specified tabular format?  
> **b.** What JDBC methods(s) can get you the required information?  
> **c.** Write the method `printTable(String r)` using the JDBC API.

---

#### 1. Core Principles & Concept Overview

##### Part a. Required Structural Knowledge
To dynamically render any arbitrary relational table $r$ without prior schema definitions, the application must discover:
1. **Degree of the Relation (Column Count):** The exact number of attributes $N$ present in the projection.
2. **Attribute Identifiers (Column Labels):** The textual column headers to display in the table heading.
3. **Attribute Types and Display Sizes:** The column width requirements to align vertical separators and ensure text columns are not truncated.
4. **Tuple Cardinality and Content:** The data values for each tuple, including identification of `NULL` states.

##### Part b. Essential JDBC Introspection Methods
The necessary metadata is retrieved through the following JDBC API methods:
- `Connection.createStatement()`: Creates a statement handle.
- `Statement.executeQuery(String sql)`: Returns an open `ResultSet`.
- `ResultSet.getMetaData()`: Returns a `ResultSetMetaData` object.
- `ResultSetMetaData.getColumnCount()`: Returns the number of columns ($N$).
- `ResultSetMetaData.getColumnLabel(int column)`: Returns column display name.
- `ResultSetMetaData.getColumnDisplaySize(int column)`: Returns maximum character display width.
- `ResultSet.next()`: Advances the tuple cursor.
- `ResultSet.getString(int column)` and `ResultSet.wasNull()`: Extracts cell data.

##### The Parameter Marker Restriction
A common misconception is attempting to write `SELECT * FROM ?` using a `PreparedStatement`.
> [!important] Crucial Rule on SQL Parameter Markers
> In the SQL standard and JDBC API, parameter placeholders (`?`) can **only** be used for literal data values (e.g., strings, numbers, dates). **Placeholders cannot be used for SQL identifiers** such as relation names, column names, or SQL keywords. Therefore, the query must be constructed via dynamic SQL (`"SELECT * FROM " + r`), requiring identifier sanitization.

---

#### 2. Detailed Step-by-Step Solution

##### Complete Implementation of `MetaDisplay.java`

```java
import java.sql.*;

public class MetaDisplay {

    // Assumes an existing connection factory or ambient connection
    private static Connection connection;

    public static void setConnection(Connection conn) {
        connection = conn;
    }

    /**
     * Executes 'select * from r' and prints the result in tabular format.
     * 
     * @param r The name of the relation to display.
     */
    public static void printTable(String r) {
        if (connection == null) {
            System.err.println("Error: Database connection is not established.");
            return;
        }

        // 1. Sanitize relation identifier to prevent SQL injection
        if (r == null || !r.matches("^[a-zA-Z_][a-zA-Z0-9_]*$")) {
            System.err.println("Error: Invalid relation name '" + r + "'. Only alphanumeric characters allowed.");
            return;
        }

        String sql = "SELECT * FROM " + r;

        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            // 2. Discover metadata
            ResultSetMetaData rsmd = rs.getMetaData();
            int colCount = rsmd.getColumnCount();

            if (colCount == 0) {
                System.out.println("Table '" + r + "' contains no columns.");
                return;
            }

            // 3. Determine column display widths
            int[] colWidths = new int[colCount];
            String[] colNames = new String[colCount];

            for (int i = 1; i <= colCount; i++) {
                colNames[i - 1] = rsmd.getColumnLabel(i);
                int displaySize = rsmd.getColumnDisplaySize(i);
                // Clamp display width between header length and max 40 chars for readability
                colWidths[i - 1] = Math.max(colNames[i - 1].length(), Math.min(displaySize, 40));
            }

            // 4. Build horizontal boundary line
            StringBuilder divider = new StringBuilder("+");
            for (int w : colWidths) {
                divider.append("-".repeat(w + 2)).append("+");
            }
            String line = divider.toString();

            // 5. Print Table Header
            System.out.println(line);
            System.out.print("|");
            for (int i = 0; i < colCount; i++) {
                System.out.printf(" %-" + colWidths[i] + "s |", colNames[i]);
            }
            System.out.println();
            System.out.println(line);

            // 6. Iterate and print data rows
            int rowCount = 0;
            while (rs.next()) {
                rowCount++;
                System.out.print("|");
                for (int i = 1; i <= colCount; i++) {
                    String val = rs.getString(i);
                    if (rs.wasNull() || val == null) {
                        val = "NULL";
                    }
                    // Truncate overly long text strings to avoid breaking column formatting
                    if (val.length() > colWidths[i - 1]) {
                        val = val.substring(0, colWidths[i - 1] - 3) + "...";
                    }
                    System.out.printf(" %-" + colWidths[i - 1] + "s |", val);
                }
                System.out.println();
            }
            System.out.println(line);
            System.out.println("Table: " + r + " (" + rowCount + " rows)");

        } catch (SQLException e) {
            System.err.println("Database execution error while querying relation '" + r + "': " + e.getMessage());
        }
    }
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Theory vs Code Distribution
> When this multi-part question appears in semester finals:
> - **Part (a) [2 Marks]:** Explicitly list the four knowledge elements: column count, column names/labels, data types/display widths, and row values.
> - **Part (b) [2 Marks]:** Write the exact method signatures (`rs.getMetaData()`, `getColumnCount()`, `getColumnLabel()`, `next()`, `getString()`).
> - **Part (c) [4 Marks]:** Code the method cleanly using try-with-resources. Do **not** use a parameterized query for the table name!

---

### Exercise 5.14 · Generic Tabular Relation Display in C using ODBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 235.
> - **Subtopic Mapping:** `T07.3` — Application interfaces (ODBC API, C language integration, low-level handles).
> - **Key Concepts:** ODBC handle architecture (`SQLHENV`, `SQLHDBC`, `SQLHSTMT`), `SQLDescribeCol`, Return codes (`SQLRETURN`), Low-level memory buffers.
> - **Difficulty & RUET Relevance:** Tests knowledge of procedural, non-garbage-collected database access APIs in C/C++.

**Question (Silberschatz 7e Exercise 5.14).**
> Repeat Exercise 5.13 using ODBC, defining `void printTable(char *r)` as a function instead of a method.

---

#### 1. Core Principles & Concept Overview

##### The ODBC Architecture in C
Unlike Java’s object-oriented JDBC driver model, the Open Database Connectivity (ODBC) standard is a procedural C Application Binary Interface (ABI):
- All operations operate upon opaque pointer handles:
  1. `SQLHENV`: Environment handle (allocates driver resources).
  2. `SQLHDBC`: Connection handle (manages connection state and credentials).
  3. `SQLHSTMT`: Statement handle (executes SQL commands and binds cursor data).
- Functions return status codes of type `SQLRETURN`:
  - `SQL_SUCCESS` ($0$), `SQL_SUCCESS_WITH_INFO` ($1$), `SQL_NO_DATA` ($100$), `SQL_ERROR` ($-1$).

##### Metadata and Fetch Functions in ODBC
1. `SQLNumResultCols(hstmt, &colCount)`: Discovers column count.
2. `SQLDescribeCol(...)`: Retrieves column name, data type, precision, and scale.
3. `SQLFetch(hstmt)`: Advances cursor to the next tuple.
4. `SQLGetData(...)`: Converts and streams column data into a C character buffer.

---

#### 2. Detailed Step-by-Step Solution

##### Complete C Implementation using ODBC 3.x

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sql.h>
#include <sqlext.h>

#define MAX_COLS 128
#define MAX_COL_NAME_LEN 64
#define BUFFER_SIZE 256

// Assumes an active global or externally managed connection handle
extern SQLHDBC global_hdbc;

/**
 * Generic tabular relation printer in C using the ODBC API.
 * 
 * @param r Name of the relation to query.
 */
void printTable(char *r) {
    if (global_hdbc == SQL_NULL_HDBC) {
        fprintf(stderr, "Error: ODBC Connection handle is uninitialized.\n");
        return;
    }

    SQLHSTMT hstmt = SQL_NULL_HSTMT;
    SQLRETURN ret;

    // 1. Allocate a Statement Handle
    ret = SQLAllocHandle(SQL_HANDLE_STMT, global_hdbc, &hstmt);
    if (!SQL_SUCCEEDED(ret)) {
        fprintf(stderr, "Error: Failed to allocate statement handle.\n");
        return;
    }

    // 2. Build and Execute 'SELECT * FROM r'
    char query[256];
    snprintf(query, sizeof(query), "SELECT * FROM %s", r);

    ret = SQLExecDirect(hstmt, (SQLCHAR *)query, SQL_NTS);
    if (!SQL_SUCCEEDED(ret)) {
        fprintf(stderr, "Error executing query: %s\n", query);
        SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
        return;
    }

    // 3. Determine Number of Columns
    SQLSMALLINT numCols = 0;
    ret = SQLNumResultCols(hstmt, &numCols);
    if (!SQL_SUCCEEDED(ret) || numCols == 0) {
        printf("Table '%s' returned 0 columns or does not exist.\n", r);
        SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
        return;
    }

    if (numCols > MAX_COLS) {
        numCols = MAX_COLS;
    }

    // 4. Retrieve Column Names and Print Header Row
    SQLCHAR colNames[MAX_COLS][MAX_COL_NAME_LEN];
    SQLSMALLINT colNameLens[MAX_COLS];
    SQLSMALLINT colDataTypes[MAX_COLS];
    SQLULEN colSizes[MAX_COLS];
    SQLSMALLINT colDecimalDigits[MAX_COLS];
    SQLSMALLINT colNullables[MAX_COLS];

    printf("+");
    for (int i = 1; i <= numCols; i++) {
        ret = SQLDescribeCol(hstmt, (SQLUSMALLINT)i,
                             colNames[i - 1], MAX_COL_NAME_LEN,
                             &colNameLens[i - 1], &colDataTypes[i - 1],
                             &colSizes[i - 1], &colDecimalDigits[i - 1],
                             &colNullables[i - 1]);
        printf("----------------------+");
    }
    printf("\n|");

    for (int i = 1; i <= numCols; i++) {
        printf(" %-20s |", colNames[i - 1]);
    }
    printf("\n+");
    for (int i = 1; i <= numCols; i++) {
        printf("----------------------+");
    }
    printf("\n");

    // 5. Fetch Rows and Extract Data Dynamically
    char dataBuffer[BUFFER_SIZE];
    SQLLEN indicator;
    int rowCount = 0;

    while ((ret = SQLFetch(hstmt)) == SQL_SUCCESS || ret == SQL_SUCCESS_WITH_INFO) {
        rowCount++;
        printf("|");
        for (int i = 1; i <= numCols; i++) {
            // Retrieve cell value converted to string (SQL_C_CHAR)
            ret = SQLGetData(hstmt, (SQLUSMALLINT)i, SQL_C_CHAR,
                             dataBuffer, sizeof(dataBuffer), &indicator);

            if (ret == SQL_SUCCESS || ret == SQL_SUCCESS_WITH_INFO) {
                if (indicator == SQL_NULL_DATA) {
                    printf(" %-20s |", "NULL");
                } else {
                    printf(" %-20.20s |", dataBuffer);
                }
            } else {
                printf(" %-20s |", "ERR");
            }
        }
        printf("\n");
    }

    printf("+");
    for (int i = 1; i <= numCols; i++) {
        printf("----------------------+");
    }
    printf("\nTotal Rows: %d\n", rowCount);

    // 6. Release Statement Resources
    SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Comparing JDBC vs ODBC in Examination Papers
> RUET examiners frequently ask for a direct architectural comparison between JDBC and ODBC:
> 
> | Dimension | JDBC (Java) | ODBC (C / C++) |
> | :--- | :--- | :--- |
> | **Type Safety** | High (Strongly typed objects, garbage collected). | Low (Raw pointers, void pointers, manual memory). |
> | **Error Handling** | Structured exceptions (`try / catch SQLException`). | Return status codes (`SQLRETURN` return checks). |
> | **Resource Management** | `AutoCloseable` (Deterministic close via garbage collector). | Explicit handle destruction (`SQLFreeHandle`). |
> | **Null Representation** | Method check `rs.wasNull()` or Java `null`. | Sentinel indicator variable (`indicator == SQL_NULL_DATA`). |

---

### Exercise 5.15 · Stored Function for Departmental Average Salary and Conditional Selection

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.2 (*Functions and Procedures*), Page 235.
> - **Subtopic Mapping:** `T07.3` — Implement a trigger / stored procedure (stored functions, SQL/PSM, scalar functions in queries).
> - **Key Concepts:** User-defined functions (`CREATE FUNCTION`), Return types, Scalar subqueries, Procedural SQL (SQL/PSM).
> - **Difficulty & RUET Relevance:** Fundamental stored function design problem, directly applicable to RUET database programming questions.

**Question (Silberschatz 7e Exercise 5.15).**
> Consider an employee database with two relations
> ```text
> employee (employee_name, street, city)
> works (employee_name, company_name, salary)
> ```
> where the primary keys are underlined. Write a function `avg_salary` that takes a company name as an argument and finds the average salary of employees at that company. Then, write an SQL statement, using that function, to find companies whose employees earn a higher salary, on average, than the average salary at “First Bank”.

---

#### 1. Core Principles & Concept Overview

##### Stored Functions vs. Stored Procedures
- A **Stored Function** returns a single scalar value (or table) through a `RETURNS` clause and can be embedded directly within SQL DML expressions (`SELECT`, `WHERE`, `HAVING`).
- A **Stored Procedure** executes procedural workflows and returns results via output parameters (`OUT`, `INOUT`) or result sets, invoked using `CALL proc_name()`.

##### Procedural Architecture
1. The function `avg_salary(comp_name)` encapsulates the aggregation `SELECT AVG(salary) FROM works WHERE company_name = comp_name`.
2. The outer query invokes `avg_salary(company_name)` for each candidate company and filters against the scalar benchmark `avg_salary('First Bank')`.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Defining the `avg_salary` Stored Function

###### Standard SQL (SQL/PSM Syntax):
```sql
CREATE FUNCTION avg_salary(comp_name VARCHAR(50))
RETURNS NUMERIC(10, 2)
BEGIN
    DECLARE v_avg_sal NUMERIC(10, 2);
    
    SELECT AVG(salary)
    INTO v_avg_sal
    FROM works
    WHERE company_name = comp_name;
    
    RETURN v_avg_sal;
END;
```

###### PostgreSQL (PL/pgSQL Syntax):
```sql
CREATE OR REPLACE FUNCTION avg_salary(comp_name VARCHAR)
RETURNS NUMERIC AS $func$
DECLARE
    v_avg_sal NUMERIC;
BEGIN
    SELECT AVG(salary)
    INTO v_avg_sal
    FROM works
    WHERE company_name = comp_name;
    
    RETURN v_avg_sal;
END;
$func$ LANGUAGE plpgsql;
```

###### Oracle (PL/SQL Syntax):
```sql
CREATE OR REPLACE FUNCTION avg_salary(comp_name IN VARCHAR2)
RETURN NUMBER IS
    v_avg_sal NUMBER;
BEGIN
    SELECT AVG(salary)
    INTO v_avg_sal
    FROM works
    WHERE company_name = comp_name;
    
    RETURN v_avg_sal;
END;
/
```

##### Step 2: The SQL Query Utilizing the Function

```sql
SELECT DISTINCT company_name
FROM works
WHERE avg_salary(company_name) > avg_salary('First Bank');
```

##### Step 3: Comparative Analysis — Function Call vs. Pure Declarative SQL

While the stored function provides modular encapsulation, calling a user-defined function in a `WHERE` clause can cause a performance penalty ($O(N)$ scalar function invocations). The equivalent pure declarative query is:

```sql
SELECT company_name
FROM works
GROUP BY company_name
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM works
    WHERE company_name = 'First Bank'
);
```

*Optimization Insight:*
The declarative `HAVING` formulation allows the query optimizer to perform a single-pass hash aggregate, whereas the procedural function invocation may force row-by-row nested subquery execution unless the query optimizer can inline the function body.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Rubric Points
> - **Return Keyword:** Ensure the function header uses `RETURNS` (plural) in ANSI/PostgreSQL and `RETURN` (singular) in Oracle PL/SQL.
> - **Distinct Filtering:** Remember to include `DISTINCT company_name` in the outer query; otherwise, the company name repeats for every employee in `works`!
> - **Scalar Return in `WHERE`:** Point out that `avg_salary('First Bank')` evaluates to a scalar constant, allowing clean relational comparison.

---

### Exercise 5.17 · Bill-of-Materials (BOM) Total Cost Computation via Client-Side Recursion in JDBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.1 (*Accessing SQL From a Programming Language*), Page 236.
> - **Subtopic Mapping:** `T07.3` — Database application programming (algorithmic graph traversal, recursive BOM processing).
> - **Key Concepts:** Bill-of-Materials (BOM) graph, Directed Acyclic Graph (DAG) traversal, Client-side recursion, Cycle detection.
> - **Difficulty & RUET Relevance:** Advanced practical problem combining graph theory, recursion, and relational database queries.

**Question (Silberschatz 7e Exercise 5.17).**
> Consider the relational schema from Exercise 5.16:
> ```text
> part (part_id, name, cost)
> subpart (part_id, subpart_id, count)
> ```
> where the primary-key attributes are underlined. A tuple $(p_1, p_2, 3)$ in the *subpart* relation denotes that the part with *part_id* $p_2$ is a direct subpart of the part with *part_id* $p_1$, and $p_1$ has 3 copies of $p_2$. Note that $p_2$ may itself have further subparts. Write a JDBC function using nonrecursive SQL to find the total cost of part “P-100”, including the costs of all its subparts. Be sure to take into account the fact that a part may have multiple occurrences of a subpart. You may use recursion in Java if you wish.

---

#### 1. Core Principles & Concept Overview

##### Mathematical Formulation of Bill-of-Materials (BOM) Cost
Let $P$ be the set of parts. The assembly hierarchy is represented as a directed graph where:
- A vertex $u \in P$ has an intrinsic direct manufacturing or base assembly cost: $\text{cost}(u)$.
- A directed edge $(u, v) \in \text{subpart}$ with multiplicity $k = \text{count}(u, v)$ indicates that assembly $u$ directly incorporates $k$ units of subpart $v$.

The **Total Cost** of an assembly part $p$ is defined by the recurrence relation:
$$
\text{TotalCost}(p) = \text{cost}(p) + \sum_{(p, s, k) \in \text{subpart}} k \times \text{TotalCost}(s)
$$

##### Termination and Base Cases
1. **Leaf Parts (Atomic Components):** If part $p$ has no entries in `subpart`, the summation evaluates to $0$, and $\text{TotalCost}(p) = \text{cost}(p)$.
2. **Cycle Prevention:** A valid physical manufacturing BOM must be a **Directed Acyclic Graph (DAG)**. If a cyclic relationship exists (e.g., $A$ contains $B$ and $B$ contains $A$), naïve recursion causes an infinite loop (`StackOverflowError`). Robust code must track visited nodes along the recursion path.

---

#### 2. Detailed Step-by-Step Solution

##### Complete Java Implementation with Client-Side Recursion

```java
import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class BillOfMaterialsCalculator {

    /**
     * Recursively computes the total cost of a part and all its subparts.
     * 
     * @param partId The root part identifier (e.g., "P-100").
     * @param conn   An active JDBC database connection.
     * @return The aggregated total cost.
     * @throws SQLException If a database access error occurs.
     */
    public static double computeTotalCost(String partId, Connection conn) throws SQLException {
        Set<String> callStack = new HashSet<>();
        return computeCostHelper(partId, conn, callStack);
    }

    private static double computeCostHelper(String partId, Connection conn, Set<String> callStack) 
            throws SQLException {
        
        // 1. Cycle detection guard
        if (callStack.contains(partId)) {
            throw new IllegalStateException("Cyclic dependency detected in BOM hierarchy for part: " + partId);
        }
        callStack.add(partId);

        double totalCost = 0.0;

        // 2. Query the intrinsic base cost of the part itself
        String partSql = "SELECT cost FROM part WHERE part_id = ?";
        try (PreparedStatement partStmt = conn.prepareStatement(partSql)) {
            partStmt.setString(1, partId);
            try (ResultSet rs = partStmt.executeQuery()) {
                if (rs.next()) {
                    totalCost += rs.getDouble("cost");
                } else {
                    System.err.println("Warning: Part '" + partId + "' not found in 'part' table. Assuming 0 cost.");
                }
            }
        }

        // 3. Query all direct subparts and their quantities
        String subpartSql = "SELECT subpart_id, count FROM subpart WHERE part_id = ?";
        try (PreparedStatement subStmt = conn.prepareStatement(subpartSql)) {
            subStmt.setString(1, partId);
            try (ResultSet rs = subStmt.executeQuery()) {
                while (rs.next()) {
                    String subpartId = rs.getString("subpart_id");
                    int quantity = rs.getInt("count");

                    // Recursive step: compute cost of subpart and multiply by count
                    double subpartCost = computeCostHelper(subpartId, conn, callStack);
                    totalCost += (quantity * subpartCost);
                }
            }
        }

        // Backtrack: Remove part from call stack
        callStack.remove(partId);

        return totalCost;
    }

    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/manufacturing_db";
        String user = "db_user";
        String pass = "db_pass";

        try (Connection conn = DriverManager.getConnection(url, user, pass)) {
            String targetPart = "P-100";
            double totalCost = computeTotalCost(targetPart, conn);
            System.out.printf("Total hierarchical cost of part '%s' = $%.2f%n", targetPart, totalCost);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Crucial Algorithmic Observations
> - **Multiplication by Count:** A critical error is omitting the `count` multiplier. If an assembly contains 4 wheels, the cost of the wheel sub-assembly must be multiplied by 4!
> - **Prepared Statement Scoping:** Notice that inside the recursive function, `PreparedStatement` and `ResultSet` objects are closed within each activation frame (using try-with-resources) to prevent cursor leakage on deep recursion trees.
> - **Server-Side vs Client-Side:** In an exam, state that while client recursion works, an alternative server-side approach using `WITH RECURSIVE` eliminates the $O(|V|)$ individual query round-trips.

---

### Exercise 5.18 · Server-Side Stored Procedure for University Teaching Records

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Section 5.2 (*Functions and Procedures*), Page 236.
> - **Subtopic Mapping:** `T07.3` — Implement a trigger / stored procedure (stored procedures, server-side cursors, PL/SQL).
> - **Key Concepts:** Database-tier stored procedures, Cursor iteration, Error signaling, Server output buffers (`DBMS_OUTPUT`).
> - **Difficulty & RUET Relevance:** Re-implementation of Exercise 5.12 inside the database engine; fundamental to RUET stored procedure questions.

**Question (Silberschatz 7e Exercise 5.18).**
> Redo Exercise 5.12 using the language of your database system for coding stored procedures and functions. Specifically, write a procedure that takes an instructor ID as an argument and produces printed output in the format specified in Exercise 5.12, or an appropriate message if the instructor does not exist or has taught no courses. (For a simpler version of this exercise, rather than providing printed output, assume a relation with the appropriate schema and insert your answer there without worrying about testing for erroneous argument values.)

---

#### 1. Core Principles & Concept Overview

##### Database-Tier vs. Application-Tier Execution
In Exercise 5.12, the business logic resided in the client application (Java Virtual Machine), issuing queries across the network.
In this exercise, the entire application workflow is packaged into a **Server-Side Stored Procedure**:
1. **Network Efficiency:** Zero intermediate data travels over the network; filtering, joining, and aggregation execute directly inside the database memory space.
2. **Encapsulation:** The procedure is compiled and stored in the database catalog, providing a centralized interface.

---

#### 2. Detailed Step-by-Step Solution

##### Implementation in Oracle PL/SQL

```sql
CREATE OR REPLACE PROCEDURE print_instructor_teaching_record (
    p_instructor_id IN VARCHAR2
) IS
    -- Variable to verify instructor existence
    v_instructor_name instructor.name%TYPE;
    v_dept_name       instructor.dept_name%TYPE;
    v_record_count    INTEGER := 0;

    -- Cursor to retrieve the teaching record with outer join for student enrollment
    CURSOR c_teaching_record IS
        SELECT 
            S.dept_name,
            S.course_id,
            C.title,
            S.sec_id,
            S.semester,
            S.year,
            COUNT(T.ID) AS total_enrollment
        FROM teaches TC
        JOIN section S 
          ON TC.course_id = S.course_id 
         AND TC.sec_id    = S.sec_id 
         AND TC.semester  = S.semester 
         AND TC.year      = S.year
        JOIN course C 
          ON S.course_id = C.course_id
        LEFT JOIN takes T 
          ON S.course_id = T.course_id 
         AND S.sec_id    = T.sec_id 
         AND S.semester  = T.semester 
         AND S.year      = T.year
        WHERE TC.ID = p_instructor_id
        GROUP BY S.dept_name, S.course_id, C.title, S.sec_id, S.semester, S.year
        ORDER BY S.dept_name, S.course_id, S.year, S.semester;

BEGIN
    -- 1. Check if the instructor exists in the database
    BEGIN
        SELECT name, dept_name 
        INTO v_instructor_name, v_dept_name
        FROM instructor
        WHERE ID = p_instructor_id;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('Error: Instructor with ID ' || p_instructor_id || ' does not exist.');
            RETURN;
    END;

    -- 2. Print Header Information
    DBMS_OUTPUT.PUT_LINE('=========================================================================================');
    DBMS_OUTPUT.PUT_LINE('Teaching Record for: ' || v_instructor_name || ' (ID: ' || p_instructor_id || ', Dept: ' || v_dept_name || ')');
    DBMS_OUTPUT.PUT_LINE('=========================================================================================');
    DBMS_OUTPUT.PUT_LINE(
        RPAD('Dept Name', 15) || ' | ' ||
        RPAD('Course ID', 10) || ' | ' ||
        RPAD('Course Title', 28) || ' | ' ||
        RPAD('Sec', 5) || ' | ' ||
        RPAD('Semester', 8) || ' | ' ||
        RPAD('Year', 6) || ' | ' ||
        RPAD('Enrollment', 10)
    );
    DBMS_OUTPUT.PUT_LINE('-----------------------------------------------------------------------------------------');

    -- 3. Loop through cursor records
    FOR rec IN c_teaching_record LOOP
        v_record_count := v_record_count + 1;
        DBMS_OUTPUT.PUT_LINE(
            RPAD(rec.dept_name, 15) || ' | ' ||
            RPAD(rec.course_id, 10) || ' | ' ||
            RPAD(SUBSTR(rec.title, 1, 28), 28) || ' | ' ||
            RPAD(rec.sec_id, 5) || ' | ' ||
            RPAD(rec.semester, 8) || ' | ' ||
            RPAD(TO_CHAR(rec.year), 6) || ' | ' ||
            LPAD(TO_CHAR(rec.total_enrollment), 10)
        );
    END LOOP;

    DBMS_OUTPUT.PUT_LINE('-----------------------------------------------------------------------------------------');

    -- 4. Check if the instructor has taught no courses
    IF v_record_count = 0 THEN
        DBMS_OUTPUT.PUT_LINE('Instructor with ID ' || p_instructor_id || ' has taught no courses.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('Total Sections Taught: ' || v_record_count);
    END IF;

END print_instructor_teaching_record;
/
```

##### Implementation in PostgreSQL PL/pgSQL

```sql
CREATE OR REPLACE PROCEDURE print_instructor_teaching_record(p_instructor_id VARCHAR)
LANGUAGE plpgsql AS $func$
DECLARE
    v_name VARCHAR;
    v_rec RECORD;
    v_count INTEGER := 0;
BEGIN
    -- 1. Existence check
    SELECT name INTO v_name FROM instructor WHERE ID = p_instructor_id;
    IF NOT FOUND THEN
        RAISE NOTICE 'Error: Instructor with ID % does not exist.', p_instructor_id;
        RETURN;
    END IF;

    RAISE NOTICE 'Teaching Record for: % (ID: %)', v_name, p_instructor_id;
    RAISE NOTICE '------------------------------------------------------------------------------------';

    -- 2. Query and iterate
    FOR v_rec IN 
        SELECT S.dept_name, S.course_id, C.title, S.sec_id, S.semester, S.year, COUNT(T.ID) AS enrollment
        FROM teaches TC
        JOIN section S ON TC.course_id = S.course_id AND TC.sec_id = S.sec_id AND TC.semester = S.semester AND TC.year = S.year
        JOIN course C ON S.course_id = C.course_id
        LEFT JOIN takes T ON S.course_id = T.course_id AND S.sec_id = T.sec_id AND S.semester = T.semester AND S.year = T.year
        WHERE TC.ID = p_instructor_id
        GROUP BY S.dept_name, S.course_id, C.title, S.sec_id, S.semester, S.year
        ORDER BY S.dept_name, S.course_id, S.year, S.semester
    LOOP
        v_count := v_count + 1;
        RAISE NOTICE '% | % | % | Sec % | % % | Enrollment: %',
            v_rec.dept_name, v_rec.course_id, v_rec.title, v_rec.sec_id, v_rec.semester, v_rec.year, v_rec.enrollment;
    END LOOP;

    IF v_count = 0 THEN
        RAISE NOTICE 'Instructor with ID % has taught no courses.', p_instructor_id;
    ELSE
        RAISE NOTICE 'Total Sections Taught: %', v_count;
    END IF;
END;
$func$;
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Scoring Breakdown for Stored Procedures
> 1. **Parameter Passing:** Clearly specify input parameter `p_instructor_id IN VARCHAR2`.
> 2. **Exception Handling:** Demonstrate `WHEN NO_DATA_FOUND` or `IF NOT FOUND` to detect nonexistent instructors.
> 3. **Cursor / FOR-IN Loop:** Using a `FOR rec IN cursor_name LOOP` construct is the standard, elegant pattern expected by RUET examiners.

---

### Exercise 9.5 · Resource Management and Leak Prevention with Try-With-Resources in JDBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.3 & 9.5, Page 455.
> - **Subtopic Mapping:** `T07.3` — Application interfaces (resource safety, connection pooling, exception handling).
> - **Key Concepts:** `AutoCloseable`, Socket/Cursor resource leakage, Connection pool starvation, Exception suppression.
> - **Difficulty & RUET Relevance:** Fundamental software engineering question for high-availability enterprise database backends.

**Question (Silberschatz 7e Exercise 9.5).**
> Why is it important to open JDBC connections using the try-with-resources (`try (…){ … }`) syntax?

---

#### 1. Core Principles & Concept Overview

##### Operating System and DBMS Resources in JDBC
A JDBC `Connection` is not merely an in-memory Java object; it encapsulates heavy native resources:
1. **Network Sockets & File Descriptors:** Each connection maintains an active TCP/IP socket with assigned operating system file descriptors on both client and database server hosts.
2. **Server-Side Session State:** The DBMS allocates a server process or dedicated thread, PGA memory, lock structures, temporary tablespace segments, and undo segments for each active connection.
3. **Child Resources (`Statement`, `ResultSet`):** Open statements maintain server-side cursor descriptors and query plan handles in the database cache.

##### The Failure Modes of Legacy `try-finally` Blocks
Prior to Java 7, resource disposal required manual closing in a `finally` block:

```java
// Antipattern: Fragile legacy try-finally resource management
Connection conn = null;
Statement stmt = null;
ResultSet rs = null;
try {
    conn = DriverManager.getConnection(url);
    stmt = conn.createStatement();
    rs = stmt.executeQuery(sql);
    // process data
} catch (SQLException e) {
    e.printStackTrace();
} finally {
    // If rs.close() throws an SQLException, stmt.close() and conn.close() NEVER RUN!
    try { if (rs != null) rs.close(); } catch (SQLException e) { /* ignored */ }
    try { if (stmt != null) stmt.close(); } catch (SQLException e) { /* ignored */ }
    try { if (conn != null) conn.close(); } catch (SQLException e) { /* ignored */ }
}
```

*Critical Defects of Legacy Management:*
1. **Exception Masking / Suppression:** If an error occurs in the `try` block, and `conn.close()` in the `finally` block also throws an exception, the secondary closing exception **overwrites and obliterates** the original root-cause exception!
2. **Boilerplate Fragility:** Forgetting a nested `try-catch` inside `finally` causes unhandled exceptions to abort the block, stranding open sockets.

---

#### 2. Detailed Step-by-Step Solution

##### The Four Reasons Why Try-With-Resources is Critical

The `try-with-resources` construct (`try (Resource r = ...) { ... }`) solves these issues deterministically:

###### 1. Guaranteed Deterministic Cleanup
- Any class implementing `java.lang.AutoCloseable` or `java.io.Closeable` is automatically closed upon leaving the `try` block.
- Cleanup occurs regardless of whether the block exits normally, returns early, or aborts due to an unhandled `SQLException` or `RuntimeException`.

###### 2. Prevention of Connection Pool Starvation
- In enterprise applications, database connections are managed by a **Connection Pool** (such as HikariCP or Apache DBCP).
- Calling `conn.close()` on a pooled connection does not sever the physical TCP link; it returns the logical handle to the pool.
- If a connection is not closed due to a leak, it remains checked out indefinitely. Over time, the pool runs dry (**connection starvation**), causing incoming HTTP requests to block, queue up, and crash the web server with gateway timeout errors (`HTTP 504`).

###### 3. Proper Exception Suppression Architecture
- If both the `try` block and the automated `close()` method throw exceptions, Java preserves the **primary exception** from the `try` block.
- The exception from `close()` is attached to the primary exception as a **suppressed exception** (`Throwable.addSuppressed()`), accessible via `e.getSuppressed()`. The developer never loses the diagnostic root cause.

###### 4. Correct Reverse-Order Disposal
- Resources declared within the `try(...)` header are closed in **reverse order of their declaration**:

$$
\text{ResultSet} \xrightarrow{\text{closed first}} \text{Statement} \xrightarrow{\text{closed second}} \text{Connection} \xrightarrow{\text{closed last}}
$$

- This prevents invalid operations, such as attempting to close a parent connection while child cursor locks remain active.

##### Exemplary Try-With-Resources Pattern

```java
// Optimal Architecture: Automatic, robust, reverse-order cleanup
try (Connection conn = dataSource.getConnection();
     PreparedStatement stmt = conn.prepareStatement(sql);
     ResultSet rs = stmt.executeQuery()) {

    while (rs.next()) {
        // Safe processing
    }
} // rs, stmt, and conn are GUARANTEED to be closed in reverse order here!
catch (SQLException e) {
    logger.error("Database operation failed", e);
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Key Takeaway for RUET Students
> If this question appears in Section B of the exam:
> 1. Mention `AutoCloseable` interface.
> 2. State that it eliminates resource leaks (TCP sockets, server cursors).
> 3. Explain the connection pool starvation disaster (HikariCP pool exhaustion).
> 4. Mention **exception suppression** (preserving the real business error).

