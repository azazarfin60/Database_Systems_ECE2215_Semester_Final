---
title: "T06 · Joins and Views · Textbook Exercise Solutions"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T06
topic_id: T06
exercise_count: 13
source_chapters:
  - "Chapter 04"
  - "Chapter 05"
---

[← Prev: T05 Part 4](T05_Part4_SQL_MultiTable_Business_Queries.md) | [Index](00_Index.md) | [Next: T07 →](T07_Triggers_and_Stored_Procedures.md)

---

# T06 · Joins and Views — Textbook Exercise Solutions

> [!info] Topic Card · T06 Joins and Views
> **Syllabus:** Unit 4 (SQL: Joins, Views, Integrity & Authorization)
> **Final Exam Weight:** 28 marks total (4.4% of total course marks; rising significantly under OBE: 11.2% in 2023–2024 finals)
> **Source Textbook:** Silberschatz, Korth, and Sudarshan, *Database System Concepts* (7th Edition, 2019), Chapters 4 and 5
> **Associated Lecture Decks:** Deck 04 (*Joining and Views*, 35 slides)
> **Target Subtopics:**
> - `T06.1` · Types of joins (Inner, Natural, Left Outer, Right Outer, Full Outer, Cross Join)
> - `T06.4` · Views: definitions, physical independence, multi-table query abstraction
> - `T06.5` · View expansion, updatable views rules, view authorization, and materialized view maintenance via triggers

---

## Table of Exercises

| Exercise ID | Type | Subtopic | Focus / Concept | Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **[PE 4.1](#exercise-pe-41--natural-join-pitfalls-and-unintended-attribute-equality)** | Practice | T06.1 | Natural join pitfalls; unwanted attribute collisions (`dept_name`) | Medium |
| **[PE 4.2](#exercise-pe-42--outer-join-formulations-and-scalar-subqueries)** | Practice | T06.1 | Outer joins, scalar subqueries, and zero-count preservation (`COUNT` trap) | Medium–High |
| **[PE 4.3](#exercise-pe-43--simulating-outer-joins-using-basic-relational-operations)** | Practice | T06.1 | Simulating left/full outer join without outer join syntax (`UNION` + `NOT EXISTS`) | High |
| **[PE 4.4](#exercise-pe-44--associativity-and-null-propagation-in-cascading-outer-joins)** | Practice | T06.1 | Associativity of outer joins: $(r \mathbin{⟕} s) \mathbin{⟕} t$ vs $r \mathbin{⟕} (s \mathbin{⟕} t)$ | High (Proof) |
| **[EX 4.10](#exercise-ex-410--natural-full-outer-join-simulation-via-on-and-coalesce)** | Chapter | T06.1 | Full outer join using `ON` and `COALESCE` with null-safe match semantics | High |
| **[EX 4.14](#exercise-ex-414--join-redundancy-and-foreign-key-preservation)** | Chapter | T06.1 | Redundancy of `NATURAL JOIN section` under foreign key constraints | Medium |
| **[EX 4.15](#exercise-ex-415--rewriting-natural-join-using-the-using-clause)** | Chapter | T06.1 | Rewriting `NATURAL JOIN` with explicit `JOIN ... USING` syntax | Low–Medium |
| **[EX 4.19](#exercise-ex-419--null-value-generation-in-multi-table-full-outer-joins)** | Chapter | T06.1 | Root causes of `NULL` in cascading full outer join (`student ⟗ takes ⟗ course`) | Medium–High |
| **[EX 4.6](#exercise-ex-46--defining-the-student_grades-view-with-gpa-computation)** | Chapter | T06.4 | View definition for GPA computation with letter-grade mappings and null safety | High |
| **[EX 4.20](#exercise-ex-420--defining-an-aggregate-view-tot_credits)** | Chapter | T06.4 | Creating summary aggregate view `tot_credits(year, num_credits)` | Low–Medium |
| **[EX 4.13](#exercise-ex-413--view-authorizations-and-invisible-tuple-insertions)** | Chapter | T06.5 | View authorization independence and `WITH CHECK OPTION` semantics | Medium |
| **[EX 4.21](#exercise-ex-421--view-updatability-violations-in-aggregate-views)** | Chapter | T06.5 | SQL standard view updatability rules; rejection of inserts through aggregate views | Medium |
| **[PE 5.6](#exercise-pe-56--materialized-view-incremental-maintenance-via-triggers)** | Practice | T06.5 | Incremental maintenance of materialized join views using SQL triggers | High |

---

## T06.1 · Types of Joins and Outer Join Variations

### Exercise PE 4.1 · Natural Join Pitfalls and Unintended Attribute Equality

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Practice Exercise 4.1, Page 176
> - **Subtopic:** T06.1 (Types of joins, natural join semantics)
> - **RUET Relevance:** 2019 Q.3(c), 2023 Q.5(c), 2024 Q.3(c) (Exam questions repeatedly ask for differences between `INNER JOIN`, `NATURAL JOIN`, and `OUTER JOIN`)
> - **Key Concepts:** Common attribute matching, schema attribute collisions, loss of cross-department teaching data

**Question (Silberschatz 7e Practice Exercise 4.1).**  
Consider the following SQL query that seeks to find a list of titles of all courses taught in Spring 2017 along with the name of the instructor.

```sql
select name, title
from instructor natural join teaches natural join section natural join course
where semester = 'Spring' and year = 2017;
```

What is wrong with this query?

---

#### 1. Core Principles & Concept Overview

The `NATURAL JOIN` operator in SQL operates by automatically equating *all* attributes that have identical column names across the participating relations, projecting away duplicate column copies.

Let relations $R$ and $S$ have attribute sets $\text{attr}(R)$ and $\text{attr}(S)$. The natural join is defined formally as:

$$
R \bowtie S = \Pi_{\text{attr}(R) \cup \text{attr}(S)} \left( \sigma_{R.A_1 = S.A_1 \land R.A_2 = S.A_2 \land \dots \land R.A_k = S.A_k} (R \times S) \right)
$$

where $\{A_1, A_2, \dots, A_k\} = \text{attr}(R) \cap \text{attr}(S)$.

In the standard university database schema:
- `instructor` = $(\underline{\text{ID}}, \text{name}, \mathbf{\text{dept\_name}}, \text{salary})$
- `teaches` = $(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}})$
- `section` = $(\underline{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{building}, \text{room\_number}, \text{time\_slot\_id})$
- `course` = $(\underline{\text{course\_id}}, \text{title}, \mathbf{\text{dept\_name}}, \text{credits})$

When evaluating `instructor natural join ... natural join course`, the intersection of attributes between `instructor` and `course` includes $\mathbf{\text{dept\_name}}$. Consequently, the query enforces:

$$
\text{instructor}.\text{dept\_name} = \text{course}.\text{dept\_name}
$$

---

#### 2. Detailed Step-by-Step Solution

##### The Flaw in the Query
1. **Unintended Semantic Constraint:**  
   The natural join implicitly adds the predicate `instructor.dept_name = course.dept_name`.
2. **False Elimination of Valid Results:**  
   Instructors frequently teach courses offered by departments other than their own home department (e.g., an instructor appointed in the `Mathematics` department teaching an introductory programming course offered by the `Comp. Sci.` department, or an interdisciplinary bio-informatics course). 
3. Any such valid teaching assignment is completely and silently discarded from the result set because the instructor's affiliated department does not match the course's sponsoring department.

##### Concrete Counter-Example Trace
Suppose the database contains the following instances:

**Table `instructor`:**
| ID | name | dept_name | salary |
| :--- | :--- | :--- | :--- |
| `10101` | Srinivasan | Comp. Sci. | 65000 |
| `45565` | Katz | Mathematics | 75000 |

**Table `teaches`:**
| ID | course_id | sec_id | semester | year |
| :--- | :--- | :--- | :--- | :--- |
| `10101` | CS-101 | 1 | Spring | 2017 |
| `45565` | CS-315 | 1 | Spring | 2017 |

**Table `section`:**
| course_id | sec_id | semester | year |
| :--- | :--- | :--- | :--- |
| CS-101 | 1 | Spring | 2017 |
| CS-315 | 1 | Spring | 2017 |

**Table `course`:**
| course_id | title | dept_name | credits |
| :--- | :--- | :--- | :--- |
| CS-101 | Intro. to Computer Science | Comp. Sci. | 4 |
| CS-315 | Robotics | Comp. Sci. | 3 |

- For instructor `10101` (Srinivasan): $\text{instructor.dept\_name} = \text{'Comp. Sci.'}$ and $\text{course.dept\_name} = \text{'Comp. Sci.'}$. The equality holds, so `('Srinivasan', 'Intro. to Computer Science')` is output.
- For instructor `45565` (Katz): $\text{instructor.dept\_name} = \text{'Mathematics'}$, but $\text{course.dept\_name} = \text{'Comp. Sci.'}$. Even though Katz taught `CS-315` in Spring 2017, the condition `instructor.dept_name = course.dept_name` evaluates to **false**, erroneously omitting `('Katz', 'Robotics')`.

##### Correct SQL Implementation
To fix this query, replace `NATURAL JOIN` with explicit `JOIN ... USING` or `JOIN ... ON` clauses specifying only the intended join keys:

```sql
-- Solution using JOIN ... USING:
select name, title
from instructor
     join teaches using (ID)
     join section using (course_id, sec_id, semester, year)
     join course using (course_id)
where semester = 'Spring' and year = 2017;
```

*Alternative (omitting redundant table `section`):*  
Because `teaches` already contains the attributes `course_id`, `sec_id`, `semester`, and `year`, joining with `section` is strictly unnecessary unless classroom details are needed:

```sql
select instructor.name, course.title
from instructor
     join teaches on instructor.ID = teaches.ID
     join course on teaches.course_id = course.course_id
where teaches.semester = 'Spring' and teaches.year = 2017;
```

---

#### 3. RUET Exam Insights & Examiner Notes
- **Common Exam Trap:** Students in semester finals often believe `NATURAL JOIN` is an infallible shortcut for saving handwriting time. In RUET exams (such as 2019 Q.3(c) and 2024 Q.3(c)), questions frequently ask: *"Why is natural join considered dangerous in real-world database design?"* The answer hinges on this exact trap: **schema evolution** or **unintended homonymous attributes** (columns sharing the same name but representing different entity properties, like `dept_name` or `name`) quietly corrupt query results without returning a syntax error.
- **Scoring Rubric:** Stating only *"it doesn't work"* awards 0 marks. To obtain full marks, explicitly identify the collision attribute (`dept_name`), show why instructors teaching outside their department are dropped, and provide the corrected query using `JOIN ... USING (course_id)` or explicit `ON`.

---

### Exercise PE 4.2 · Outer Join Formulations and Scalar Subqueries

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Practice Exercise 4.2, Page 176
> - **Subtopic:** T06.1 (Outer join semantics, preserving unmatched tuples, aggregate interaction)
> - **RUET Relevance:** Direct mapping to 2020 Q.4(c) and 2024 Q.4(a) (Outcome tables and outer join queries)
> - **Key Concepts:** `LEFT OUTER JOIN`, `COUNT(*)` vs `COUNT(attribute)`, scalar subqueries, `COALESCE`

**Question (Silberschatz 7e Practice Exercise 4.2).**  
Write the following queries in SQL:

a. Display a list of all instructors, showing each instructor’s ID and the number of sections taught. Make sure to show the number of sections as 0 for instructors who have not taught any section. Your query should use an outer join, and should not use subqueries.  
b. Write the same query as in part a, but using a scalar subquery and not using outer join.  
c. Display the list of all course sections offered in Spring 2018, along with the ID and name of each instructor teaching the section. If a section has more than one instructor, that section should appear as many times in the result as it has instructors. If a section does not have any instructor, it should still appear in the result with the instructor name set to “—”.  
d. Display the list of all departments, with the total number of instructors in each department, without using subqueries. Make sure to show departments that have no instructors, and list those departments with an instructor count of zero.

---

#### 1. Core Principles & Concept Overview

##### Outer Join Semantics
An inner join discards any tuple that fails to find a partner satisfying the join condition. An **outer join** avoids information loss by synthesizing a tuple padded with `NULL` values for the missing side:
- **Left Outer Join ($R \mathbin{⟕} S$):** Preserves all tuples from the left relation $R$.
- **Right Outer Join ($R \mathbin{⟖} S$):** Preserves all tuples from the right relation $S$.
- **Full Outer Join ($R \mathbin{⟗} S$):** Preserves all tuples from both $R$ and $S$.

##### The Crucial `COUNT(*)` vs `COUNT(column)` Distinction
When an outer join produces an unmatched row, the attributes from the non-matching side are filled with `NULL`.
- `COUNT(*)` counts the number of physical rows in a group, regardless of whether column values are null. For an unmatched instructor, `COUNT(*)` returns **1** (since the row exists).
- `COUNT(column_name)` counts only non-null occurrences of `column_name`. For an unmatched instructor where `sec_id` is `NULL`, `COUNT(sec_id)` evaluates to **0**.

---

#### 2. Detailed Step-by-Step Solution

##### Solution to Part (a)
*Requirement:* All instructors, ID and count of sections taught; 0 for inactive instructors; outer join; no subqueries.

```sql
select instructor.ID, count(teaches.sec_id) as num_sections
from instructor
     left outer join teaches on instructor.ID = teaches.ID
group by instructor.ID;
```

*Critical Verification:*
If instructor `33456` (Gold) taught 0 sections, the `LEFT OUTER JOIN` outputs:
`('33456', 'Gold', 'Physics', 87000, NULL, NULL, NULL, NULL, NULL)`.
`count(teaches.sec_id)` encounters a `NULL` and yields `0`. (Had we written `count(*)`, it would have incorrectly yielded `1`).

##### Solution to Part (b)
*Requirement:* Same result as part (a), but using a scalar subquery and no outer join.

```sql
select instructor.ID,
       (select count(*)
        from teaches
        where teaches.ID = instructor.ID) as num_sections
from instructor;
```

*Explanation:*  
For each instructor tuple evaluated in the outer query, the correlated scalar subquery runs over `teaches`. If no matching row exists, `COUNT(*)` on an empty set evaluates directly to `0`. A scalar subquery in the `SELECT` clause must return at most one row and one column.

##### Solution to Part (c)
*Requirement:* All sections offered in Spring 2018 with instructor ID and name; multiple instructors produce multiple rows; missing instructors show "—".

```sql
select section.course_id, section.sec_id, section.semester, section.year,
       teaches.ID,
       coalesce(instructor.name, '—') as instructor_name
from section
     left outer join teaches
          on section.course_id = teaches.course_id
         and section.sec_id = teaches.sec_id
         and section.semester = teaches.semester
         and section.year = teaches.year
     left outer join instructor
          on teaches.ID = instructor.ID
where section.semester = 'Spring' and section.year = 2018;
```

*Key Technical Details:*
1. Preserving relation: `section` must be on the left side of the `LEFT OUTER JOIN` chain to ensure sections with zero instructors are preserved.
2. Filtering predicate: Placing `where section.semester = 'Spring' and section.year = 2018` is strictly safe because `section` is the preserved relation. (Filtering on `teaches.semester` in the `WHERE` clause would convert the outer join into an inner join by discarding null-padded rows).
3. `COALESCE(instructor.name, '—')` evaluates `instructor.name`; if null, it substitutes the string literal `'—'`.

##### Solution to Part (d)
*Requirement:* All departments, total instructors, no subqueries, 0 for empty departments.

```sql
select department.dept_name, count(instructor.ID) as num_instructors
from department
     left outer join instructor
          on department.dept_name = instructor.dept_name
group by department.dept_name;
```

*Verification:*  
A department with no faculty (e.g., a newly established department) forms an outer-join row with `instructor.ID = NULL`. Grouping by `dept_name` and evaluating `count(instructor.ID)` yields `0`.

---

#### 3. RUET Exam Insights & Examiner Notes
- **The Fatal `COUNT(*)` Error:** In RUET exams (e.g., 2020 Q.4(c) and 2024 Q.4(a)), more than 60% of students write `COUNT(*)` after a `LEFT JOIN`. RUET grading rubrics penalize this heavily (deducting 2 to 3 marks out of 5), because an instructor with 0 courses is reported as having 1 course! Always use `COUNT(right_table.foreign_key)`.
- **`WHERE` vs `ON` Clause Placement:** Emphasize that when filtering preserved tables in an outer join, condition placement matters:
  - If you filter the **preserved (left)** table, put it in the `WHERE` clause.
  - If you filter the **non-preserved (right)** table, you *must* place the condition inside the `ON` clause, otherwise any null-padded row will evaluate to `unknown` in the `WHERE` clause and get filtered out, silently destroying the outer join.

---

### Exercise PE 4.3 · Simulating Outer Joins Using Basic Relational Operations

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Practice Exercise 4.3, Page 176
> - **Subtopic:** T06.1 (Outer join simulation, algebraic foundations)
> - **RUET Relevance:** Crucial theoretical question. RUET 2020 Q.4(c) and 2024 Q.4(a) note: *"MySQL does not support FULL OUTER JOIN natively; show how to achieve it via UNION."*
> - **Key Concepts:** Set union, anti-semijoin simulation, null-tuple padding, schema alignment

**Question (Silberschatz 7e Practice Exercise 4.3).**  
Outer join expressions can be computed in SQL without using the SQL outer join operation. To illustrate this fact, show how to rewrite each of the following SQL queries without using the outer join expression.

a.
```sql
select * from student natural left outer join takes;
```

b.
```sql
select * from student natural full outer join takes;
```

---

#### 1. Core Principles & Concept Overview

##### Relational Algebra Equivalence
In relational algebra, an outer join is defined mathematically as the union of an inner join and the padded anti-join (unmatched tuples).

For left outer join ($R \mathbin{⟕} S$):
$$
R \mathbin{⟕} S = (R \bowtie S) \cup \left( \left( R - \Pi_{\text{attr}(R)}(R \bowtie S) \right) \times \{ (\underbrace{\text{null}, \dots, \text{null}}_{|\text{attr}(S) - \text{attr}(R)| \text{ times}}) \} \right)
$$

For full outer join ($R \mathbin{⟗} S$):
$$
R \mathbin{⟗} S = (R \bowtie S) \cup (R_{\text{unmatched}} \times \text{null}_S) \cup (\text{null}_R \times S_{\text{unmatched}})
$$

##### Schema Attribute Breakdown
To construct valid SQL `UNION` operations, both queries must project the exact same number of columns in identical order and compatible data types:
- `student` schema: $(ID, name, dept\_name, tot\_cred)$ — 4 attributes.
- `takes` schema: $(ID, course\_id, sec\_id, semester, year, grade)$ — 6 attributes.
- Natural join schema: $(ID, name, dept\_name, tot\_cred, course\_id, sec\_id, semester, year, grade)$ — 9 attributes.

---

#### 2. Detailed Step-by-Step Solution

##### Solution to Part (a) · Left Outer Join Rewrite

To simulate `student natural left outer join takes` without outer join syntax:
1. Compute the standard inner join: `student natural join takes`.
2. Find all students who do not appear in `takes` using a `NOT IN` or `NOT EXISTS` subquery.
3. Pad the 5 attributes corresponding to `takes` (`course_id, sec_id, semester, year, grade`) with explicit `null` literals.
4. Combine both sets using `UNION ALL` (or `UNION`). Since the two component sets are mutually disjoint, `UNION ALL` is faster and semantically exact.

```sql
-- Block 1: Matching tuples (Inner Join)
select ID, name, dept_name, tot_cred, course_id, sec_id, semester, year, grade
from student natural join takes

union all

-- Block 2: Unmatched students padded with NULLs for takes attributes
select ID, name, dept_name, tot_cred,
       null as course_id,
       null as sec_id,
       null as semester,
       null as year,
       null as grade
from student
where ID not in (select ID from takes where ID is not null);
```

> [!tip] Subquery Null Safety
> Notice the clause `where ID is not null` in the subquery. In SQL, if the inner subquery of `NOT IN` returns even a single `NULL`, the entire `NOT IN` predicate evaluates to `UNKNOWN` for all outer rows, returning an empty set. Alternatively, write `NOT EXISTS (select 1 from takes where takes.ID = student.ID)`, which is completely immune to null pitfalls.

##### Solution to Part (b) · Full Outer Join Rewrite

To simulate `student natural full outer join takes`:
1. Matching tuples: `student natural join takes`.
2. Unmatched students (padded with nulls for `takes`).
3. Unmatched takes records (padded with nulls for `student`).

```sql
-- Block 1: Matched tuples
select ID, name, dept_name, tot_cred, course_id, sec_id, semester, year, grade
from student natural join takes

union all

-- Block 2: Students with no takes records
select ID, name, dept_name, tot_cred,
       null as course_id,
       null as sec_id,
       null as semester,
       null as year,
       null as grade
from student
where not exists (
    select 1 from takes where takes.ID = student.ID
)

union all

-- Block 3: Takes records with no matching student (e.g., dangling enrollments)
select ID,
       null as name,
       null as dept_name,
       null as tot_cred,
       course_id, sec_id, semester, year, grade
from takes
where not exists (
    select 1 from student where student.ID = takes.ID
);
```

*Alternative Practical Formulation (Left Join $\cup$ Right Join):*  
If one outer join type is permitted (as done in production MySQL):
```sql
select * from student natural left outer join takes
union
select * from student natural right outer join takes;
```
Here, `UNION` (without `ALL`) automatically dedupes the inner join rows that appear in both expressions.

---

#### 3. RUET Exam Insights & Examiner Notes
- **Direct RUET Question Link:** In RUET 2024 Q.4(a), students were asked to compute the join outcome of two tables (`Courses` and `Teacher`) and explicitly explain how MySQL implements `FULL OUTER JOIN`. The standard textbook solution using `LEFT JOIN ... UNION ... RIGHT JOIN` or `UNION ALL` with `NOT EXISTS` receives full marks.
- **Column Count Alignment:** When writing these queries on paper, students often forget to pad the exact number of `NULL` columns. In RUET grading, if `student` has 4 columns and `takes` has 6, the resulting `UNION` must have exactly $4 + 6 - 1 = 9$ columns. Counting the projected null literals explicitly shows technical mastery.

---

### Exercise PE 4.4 · Associativity and Null Propagation in Cascading Outer Joins

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Practice Exercise 4.4, Page 176–177
> - **Subtopic:** T06.1 (Outer join algebraic properties, associativity counter-proof)
> - **RUET Relevance:** Advanced relational algebra question. Proves why database query optimizers cannot freely reorder outer joins the way they reorder inner joins.
> - **Key Concepts:** Associativity failure of left outer join, null propagation, predicate pushdown limits

**Question (Silberschatz 7e Practice Exercise 4.4).**  
Suppose we have three relations $r(A, B)$, $s(B, C)$, and $t(B, D)$, with all attributes declared as **not null**.

a. Give instances of relations $r$, $s$, and $t$ such that in the result of
```sql
(r natural left outer join s) natural left outer join t
```
attribute $C$ has a null value but attribute $D$ has a non-null value.

b. Are there instances of $r$, $s$, and $t$ such that the result of
```sql
r natural left outer join (s natural left outer join t)
```
has a null value for $C$ but a non-null value for $D$? Explain why or why not.

---

#### 1. Core Principles & Concept Overview

Inner join ($\bowtie$) is associative:

$$
(r \bowtie s) \bowtie t = r \bowtie (s \bowtie t)
$$

Left outer join ($\mathbin{⟕}$) is **not associative**:

$$
(r \mathbin{⟕} s) \mathbin{⟕} t \neq r \mathbin{⟕} (s \mathbin{⟕} t)
$$

This exercise demonstrates the asymmetry:
- In $(r \mathbin{⟕} s) \mathbin{⟕} t$, the intermediate relation has schema $(A, B, C)$. Even if a tuple in $r$ fails to match in $s$ (leaving $C = \text{null}$), the attribute $B$ is retained from $r$ (since all attributes of $r$ are non-null). In the second join with $t(B, D)$, that non-null $B$ can successfully match a tuple in $t$, populating $D$ with a non-null value!
- In $r \mathbin{⟕} (s \mathbin{⟕} t)$, the right child is $(s \mathbin{⟕} t)$. Any tuple produced by $(s \mathbin{⟕} t)$ must originate from $s$. Since attributes of $s$ are `NOT NULL`, $C$ can *never* be null in $(s \mathbin{⟕} t)$!

---

#### 2. Detailed Step-by-Step Solution

##### Solution to Part (a)
We must construct instances of $r(A,B)$, $s(B,C)$, and $t(B,D)$ such that in $((r \mathbin{⟕} s) \mathbin{⟕} t)$, attribute $C$ is `NULL` while $D$ is non-null.

**Define Instances:**
- Let $r = \{(1, 2)\}$
- Let $s = \{(3, 10)\}$  *(Note: $s$ contains no tuple with $B = 2$)*
- Let $t = \{(2, 20)\}$  *(Note: $t$ contains a tuple with $B = 2$)*

**Step 1: Compute $(r \text{ natural left outer join } s)$**
- Relation $r$ has tuple $(A=1, B=2)$.
- In $s$, there is no tuple with $B=2$.
- Because it is a left outer join, the tuple from $r$ is preserved, and $s$'s attribute ($C$) is padded with `NULL`.

$$
\text{Intermediate } I_1 = (r \mathbin{⟕} s) = \begin{array}{|c|c|c|} \hline A & B & C \\ \hline 1 & 2 & \text{null} \\ \hline \end{array}
$$

**Step 2: Compute $I_1 \text{ natural left outer join } t$**
- The join condition between $I_1(A, B, C)$ and $t(B, D)$ is on common attribute $B$.
- In $I_1$, the tuple has $B = 2$.
- In $t$, there exists the tuple $(B=2, D=20)$.
- The values match on $B=2$! An inner match occurs.

$$
\text{Result } = (I_1 \mathbin{⟕} t) = \begin{array}{|c|c|c|c|} \hline A & B & C & D \\ \hline 1 & 2 & \mathbf{\text{null}} & \mathbf{20} \\ \hline \end{array}
$$

In this tuple, attribute $C$ is `null` and attribute $D$ is non-null ($20$). $\blacksquare$

---

##### Solution to Part (b)
*Question:* Can $r \text{ natural left outer join } (s \text{ natural left outer join } t)$ produce a tuple where $C$ is `null` and $D$ is non-null?

**Answer:** **No, such instances cannot exist.**

**Formal Proof:**
1. Consider the subexpression $E = (s \text{ natural left outer join } t)$.
   - The schema of $E$ is $(B, C, D)$.
   - By definition of left outer join, every tuple in $E$ is generated by taking a tuple from $s(B, C)$ and either joining it with a matching tuple in $t(B, D)$ or padding $D$ with `null`.
   - The problem statement declares that **all attributes of $s$ are `NOT NULL`**.
   - Therefore, for every tuple $e \in E$, the attribute $e.C$ is strictly **non-null** ($e.C \neq \text{null}$).
2. Now consider the overall expression $R_{\text{final}} = r \text{ natural left outer join } E$.
   - Any resulting tuple $u \in R_{\text{final}}$ is formed in one of two ways:
     - **Case 1 (Unmatched in $E$):** A tuple from $r$ finds no matching tuple in $E$ on attribute $B$. In this case, all attributes from $E$ ($B, C, D$) are padded with `null`. Thus, $u.C = \text{null}$ and $u.D = \text{null}$. Here, $D$ is null.
     - **Case 2 (Matched in $E$):** A tuple from $r$ matches some tuple $e \in E$ on attribute $B$. In this case, the values of $C$ and $D$ are copied directly from $e$:
       $$
       u.C = e.C \quad \text{and} \quad u.D = e.D
       $$
       From Step 1, $e.C$ is guaranteed to be non-null. Therefore, $u.C$ is non-null.
3. **Conclusion:**  
   In Case 1, $D$ is `null`. In Case 2, $C$ is non-null.  
   There is no scenario where $u.C$ can be `null` while $u.D$ is non-null. Hence, no such instances of $r$, $s$, and $t$ can exist. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes
- **Significance for Query Optimizers:** This proof illustrates why relational database engines (like PostgreSQL and Oracle) can freely commute and reassociate inner joins $(A \bowtie B) \bowtie C \equiv A \bowtie (B \bowtie C)$, but **cannot reassociate outer joins** without altering query results. In exam questions covering algebraic query transformation, pointing out that $(R \mathbin{⟕} S) \mathbin{⟕} T \neq R \mathbin{⟕} (S \mathbin{⟕} T)$ demonstrates superior theoretical depth.

---

### Exercise EX 4.10 · Natural Full Outer Join Simulation via ON and COALESCE

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.10, Page 178
> - **Subtopic:** T06.1 (Full outer join mechanics, column coalescence, null equality)
> - **RUET Relevance:** Directly addresses how to construct lossless join outcome tables without duplicate column projections.
> - **Key Concepts:** `FULL OUTER JOIN ... ON`, `COALESCE`, three-valued logic (`UNKNOWN`), `IS NOT DISTINCT FROM`

**Question (Silberschatz 7e Exercise 4.10).**  
Given the relations $a(name, address, title)$ and $b(name, address, salary)$, show how to express $a \text{ natural full outer join } b$ using the **full outer-join** operation with an **on** condition rather than using the natural join syntax. This can be done using the **coalesce** operation. Make sure that the result relation does not contain two copies of the attributes *name* and *address* and that the solution is correct even if some tuples in $a$ and $b$ have null values for attributes *name* or *address*.

---

#### 1. Core Principles & Concept Overview

##### Natural Join vs `ON` Join Differences
When executing `a natural full outer join b`:
1. Attributes with identical names (`name`, `address`) appear **only once** in the output schema.
2. Tuples are matched if their common attributes are equal. In the SQL standard for natural join, if common attributes are both null in $a$ and $b$, they are considered equivalent (they match).

If one simply writes:
```sql
select *
from a full outer join b on a.name = b.name and a.address = b.address;
```
Two severe errors arise:
1. **Column Duplication:** The projection contains six columns: `a.name, a.address, a.title, b.name, b.address, b.salary`.
2. **Three-Valued Logic Null Trap:** In standard SQL, `NULL = NULL` evaluates to `UNKNOWN` (not `TRUE`). Thus, tuples with null names or addresses will fail to match on the `ON` clause, erroneously producing two separate padded tuples instead of joining them.

##### Role of `COALESCE`
The function `COALESCE(e_1, e_2, \dots, e_n)` returns the first non-null expression from its argument list. If both $a.name$ and $b.name$ are null, it evaluates to null.

---

#### 2. Detailed Step-by-Step Solution

##### Complete SQL Query Formulation

```sql
select coalesce(a.name, b.name) as name,
       coalesce(a.address, b.address) as address,
       a.title,
       b.salary
from a
     full outer join b
          on (a.name = b.name or (a.name is null and b.name is null))
         and (a.address = b.address or (a.address is null and b.address is null));
```

##### Modern SQL Standard Alternative (`IS NOT DISTINCT FROM`)
In modern SQL (and PostgreSQL / MySQL 8.0+ `<=>`), the standard null-safe equality operator `IS NOT DISTINCT FROM` handles null comparisons cleanly:

```sql
select coalesce(a.name, b.name) as name,
       coalesce(a.address, b.address) as address,
       a.title,
       b.salary
from a
     full outer join b
          on a.name is not distinct from b.name
         and a.address is not distinct from b.address;
```

##### Step-by-Step Execution Trace

Suppose relation instances are:
- $a = \{(\text{'Alice'}, \text{null}, \text{'Engineer'}), (\text{null}, \text{'Dhaka'}, \text{'Analyst'})\}$
- $b = \{(\text{'Alice'}, \text{null}, 85000), (\text{'Bob'}, \text{'Rajshahi'}, 60000)\}$

**Evaluation:**
1. **Tuple 1:** $a$ has `('Alice', null)`. In $b$, tuple 1 has `('Alice', null)`.
   - `a.name = b.name` is `'Alice' = 'Alice'` $\to$ **TRUE**.
   - `(a.address is null and b.address is null)` $\to$ **TRUE**.
   - The `ON` condition evaluates to **TRUE**.
   - Projection: `coalesce('Alice', 'Alice') = 'Alice'`, `coalesce(null, null) = null`, `title = 'Engineer'`, `salary = 85000`.
   - Output tuple: `('Alice', null, 'Engineer', 85000)`.
2. **Tuple 2:** $a$ has `(null, 'Dhaka')`. In $b$, no matching row exists.
   - Preserved from $a$: `coalesce(null, null) = null`, `coalesce('Dhaka', null) = 'Dhaka'`, `title = 'Analyst'`, `salary = null`.
   - Output tuple: `(null, 'Dhaka', 'Analyst', null)`.
3. **Tuple 3:** $b$ has `('Bob', 'Rajshahi')`. In $a$, no matching row exists.
   - Preserved from $b$: `coalesce(null, 'Bob') = 'Bob'`, `coalesce(null, 'Rajshahi') = 'Rajshahi'`, `title = null`, `salary = 60000`.
   - Output tuple: `('Bob', 'Rajshahi', null, 60000)`.

Resulting relation contains exactly 4 attributes: $(name, address, title, salary)$, matching the natural full outer join specification identically.

---

#### 3. RUET Exam Insights & Examiner Notes
- **Common Mistakes:** Students frequently forget the `(a.name is null and b.name is null)` clause. In RUET exams, examiners specifically award 2 dedicated marks for handling the null-matching condition. Writing merely `ON a.name = b.name` shows ignorance of SQL three-valued logic.

---

### Exercise EX 4.14 · Join Redundancy and Foreign Key Preservation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.14, Page 179
> - **Subtopic:** T06.1 (Natural join redundancy, referential integrity optimization)
> - **RUET Relevance:** Relational optimization and schema constraint analysis
> - **Key Concepts:** Foreign key dependencies, lossless natural join, query pruning

**Question (Silberschatz 7e Exercise 4.14).**  
Consider the query
```sql
select course_id, semester, year, sec_id, avg(tot_cred)
from takes natural join student
where year = 2017
group by course_id, semester, year, sec_id
having count(ID) >= 2;
```
Explain why appending **natural join** *section* in the **from** clause would not change the result.

---

#### 1. Core Principles & Concept Overview

A join with an additional table $T$ can alter a query's result set in three possible ways:
1. **Filtering:** Eliminating tuples that fail to find a match in $T$.
2. **Duplicating:** Multiplying tuples if multiple matches exist in $T$ for a single base tuple.
3. **Attribute Corruption:** Introducing unexpected column equality constraints via `NATURAL JOIN`.

If none of these three effects occur, the join is **semantically redundant** and can be eliminated by the database optimizer without changing query output.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Schema and Attribute Comparison
Let us inspect the schemas of the relations:
- `takes` = $(\underline{\text{ID}, \mathbf{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}}, \text{grade})$
- `student` = $(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{tot\_cred})$
- `section` = $(\underline{\mathbf{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}}, \text{building}, \text{room\_number}, \text{time\_slot\_id})$

The natural join `takes natural join student` joins on the common attribute `ID`.  
Now append `natural join section`:
The common attributes between `(takes natural join student)` and `section` are:
$$
\text{attr}(\text{takes} \bowtie \text{student}) \cap \text{attr}(\text{section}) = \{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}\}
$$

##### Step 2: Referential Integrity (Foreign Key) Analysis
In the standard university relational schema:
$$
\text{foreign key } (\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}) \text{ references section}
$$
By definition of referential integrity:
- **No Orphan Tuples:** For every tuple in `takes`, the composite value $(\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year})$ **must already exist** in the `section` relation. Therefore, **no tuples from `takes` will be eliminated** by requiring a match in `section`.

##### Step 3: Primary Key (Uniqueness) Analysis
In relation `section`, the composite attribute $(\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year})$ is declared as the **primary key**.
- **No Tuple Multiplication:** Because the primary key is strictly unique, each tuple in `takes` can match **at most one** (and by referential integrity, **exactly one**) tuple in `section`. Therefore, joining with `section` **cannot duplicate** any tuples.

##### Step 4: Projection and Aggregation Invariance
- The query's `SELECT`, `GROUP BY`, and `HAVING` clauses reference only attributes from `takes` (`course_id, sec_id, semester, year, ID`) and `student` (`tot_cred`).
- None of the distinct attributes of `section` (`building, room_number, time_slot_id`) are projected or used in predicates.
- Because the join with `section` produces a bijective (one-to-one) correspondence on `takes` tuples and neither eliminates nor multiplies rows, the multi-set of tuples grouped and aggregated remains identical.

Hence, appending `natural join section` produces the exact same result. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes
- **Key Concepts to Mention:** To receive full marks on RUET exams, your explanation must cite both:
  1. The **Foreign Key Constraint** (guarantees $\ge 1$ match; no tuples dropped).
  2. The **Primary Key Constraint** (guarantees $\le 1$ match; no duplicate tuples created).
  Together, they establish an exact $1:1$ relationship for every valid `takes` record.

---

### Exercise EX 4.15 · Rewriting Natural Join Using the USING Clause

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.15, Page 179
> - **Subtopic:** T06.1 (Join syntax, USING clause semantics)
> - **RUET Relevance:** High frequency. RUET papers consistently test syntactic alternatives for natural joins.
> - **Key Concepts:** `JOIN ... USING`, projection deduplication, explicit attribute matching

**Question (Silberschatz 7e Exercise 4.15).**  
Rewrite the query
```sql
select *
from section natural join classroom;
```
without using a natural join but instead using an inner join with a **using** condition.

---

#### 1. Core Principles & Concept Overview

##### Schemas
- `section` = $(\underline{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \mathbf{\text{building}}, \mathbf{\text{room\_number}}, \text{time\_slot\_id})$
- `classroom` = $(\underline{\mathbf{\text{building}}, \mathbf{\text{room\_number}}}, \text{capacity})$

The common attributes between `section` and `classroom` are $\mathbf{\text{building}}$ and $\mathbf{\text{room\_number}}$.

##### Semantic Behavior of `USING`
In SQL:
- `FROM R JOIN S ON condition` retains *both* $R.A$ and $S.A$ in the `SELECT *` projection.
- `FROM R JOIN S USING (A_1, A_2, ...)` retains **only one copy** of the join attributes $A_1, A_2, \dots$ in the `SELECT *` projection, mimicking the projection behavior of `NATURAL JOIN` while explicitly naming the intended join columns.

---

#### 2. Detailed Step-by-Step Solution

##### Rewritten SQL Query

```sql
select *
from section
     join classroom using (building, room_number);
```
*(Or explicitly using the optional `inner` keyword:)*
```sql
select *
from section
     inner join classroom using (building, room_number);
```

##### Attribute Ordering in the Result Relation
When `SELECT *` is executed:
1. The common attributes listed in the `USING` clause appear first: `building`, `room_number`.
2. The remaining attributes of the first table (`section`) follow: `course_id`, `sec_id`, `semester`, `year`, `time_slot_id`.
3. The remaining attributes of the second table (`classroom`) follow: `capacity`.

Result schema:
$$
(\text{building}, \text{room\_number}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}, \text{time\_slot\_id}, \text{capacity})
$$

---

#### 3. RUET Exam Insights & Examiner Notes
- **Why `USING` is Preferred over `ON` in Production:** In RUET viva and theory questions, examiners ask why `JOIN ... USING (A)` is superior to both `NATURAL JOIN` and `JOIN ... ON R.A = S.A`:
  1. Unlike `NATURAL JOIN`, it is immune to future schema changes (e.g., adding a unrelated column named `status` to both tables won't break the join).
  2. Unlike `ON`, it does not create redundant, duplicate columns (`R.A` and `S.A`) in `SELECT *`.

---

### Exercise EX 4.19 · Null-Value Generation in Multi-Table Full Outer Joins

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.19, Page 179–180
> - **Subtopic:** T06.1 (Full outer join mechanics, cascading joins, unintended attribute equality)
> - **RUET Relevance:** Common theoretical analysis question in semester finals (e.g., 2023 Q.5(c), 2024 Q.3(c))
> - **Key Concepts:** Cascading `FULL OUTER JOIN`, null propagation, composite natural join collisions

**Question (Silberschatz 7e Exercise 4.19).**  
Under what circumstances would the query

```sql
select *
from student natural full outer join takes
     natural full outer join course;
```

include tuples with null values for the *title* attribute?

---

#### 1. Core Principles & Concept Overview

Let us trace the attributes across the relations:
- `student` = $(\underline{\text{ID}}, \text{name}, \mathbf{\text{dept\_name}}, \text{tot\_cred})$
- `takes` = $(\underline{\text{ID}, \mathbf{\text{course\_id}}, \text{sec\_id}, \text{semester}, \text{year}}, \text{grade})$
- `course` = $(\underline{\mathbf{\text{course\_id}}}, \mathbf{\text{title}}, \mathbf{\text{dept\_name}}, \text{credits})$

Evaluation proceeds in two stages:
1. **Stage 1:** $T_1 = (\text{student} \text{ natural full outer join } \text{takes})$.  
   The common attribute is `ID`.
2. **Stage 2:** $T_{\text{final}} = (T_1 \text{ natural full outer join } \text{course})$.  
   The common attributes between $T_1$ and `course` are **both** $\mathbf{\text{course\_id}}$ **and** $\mathbf{\text{dept\_name}}$.

Attribute `title` originates solely from `course`. In a `FULL OUTER JOIN`, attributes of `course` (including `title`) are set to `NULL` whenever a tuple in the left operand ($T_1$) fails to find a matching tuple in `course`.

---

#### 2. Detailed Step-by-Step Solution

Tuples in $T_{\text{final}}$ will contain a `NULL` for `title` under four distinct circumstances:

##### Circumstance 1: Students Who Have Not Taken Any Courses
If a student has never enrolled in any course (e.g., a newly registered student):
- In Stage 1 (`student` natural full outer join `takes`), this student has no matching tuple in `takes`.
- The student's tuple is preserved in $T_1$, with all `takes` attributes—including `course_id`—set to `NULL`.
- In Stage 2, when joining with `course`, a `NULL` `course_id` cannot match any existing course in `course` (because in SQL, `NULL = course_id` evaluates to `UNKNOWN`).
- Therefore, $T_1$'s tuple is preserved in the full outer join, and all attributes from `course` (`title, credits`) are populated with `NULL`.

##### Circumstance 2: Takes Records Referencing Non-Existent Courses
If the database allows or contains orphaned `takes` tuples (e.g., if foreign key enforcement is disabled or referential integrity is violated) where a student took a `course_id` that does not exist in the `course` table:
- Stage 1 matches the student and the enrollment.
- In Stage 2, the `course_id` fails to match any row in `course`.
- The tuple is preserved from the left relation, and `title` is set to `NULL`.

##### Circumstance 3: Students Taking Courses Outside Their Home Department (The Double-Collision Trap)
This is the most critical and subtle circumstance:
- Common attributes between $T_1$ and `course` are **both** `course_id` and `dept_name`.
- A natural join requires equality on **all** common attributes:
  $$
  T_1.\text{course\_id} = \text{course}.\text{course\_id} \quad \text{AND} \quad T_1.\text{dept\_name} = \text{course}.\text{dept\_name}
  $$
- If a student from the `Physics` department ($T_1.\text{dept\_name} = \text{'Physics'}$) takes a course offered by the `Comp. Sci.` department (e.g., `CS-101`, where $\text{course}.\text{dept\_name} = \text{'Comp. Sci.'}$):
  - The `course_id` matches (`CS-101`), but the `dept_name` **does not match** (`'Physics'` $\neq$ `'Comp. Sci.'`)!
  - Because equality fails on `dept_name`, the tuple in $T_1$ fails to match the `course` record for `CS-101`.
  - In the full outer join, $T_1$'s tuple is preserved as an unmatched row, setting `title` to `NULL`! (Simultaneously, `CS-101` from `course` is preserved with student attributes set to `NULL`).

##### Circumstance 4: Course Tuple Has a Native NULL Title
If the underlying `course` relation does not enforce a `NOT NULL` constraint on `title`, and a course has been inserted with `title = NULL`, any matching join tuple will naturally display `NULL` for `title`.

---

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner Scoring Focus:** Most students only think of Circumstance 1 (students taking no courses). Mentioning Circumstance 3 (taking cross-departmental electives leading to a `dept_name` collision in the second natural join) marks the difference between an average student and an honors-level answer.

---

## T06.4 · View Definition and Multi-Table Abstraction

### Exercise EX 4.6 · Defining the student_grades View with GPA Computation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.6, Page 177
> - **Subtopic:** T06.4 (Views, complex multi-table queries, aggregation over views)
> - **RUET Relevance:** Directly mirrors 2023 Q.5(a) & Q.5(b) (*"What is a view? Define a view over multiple relations with suitable example."*)
> - **Key Concepts:** `CREATE VIEW`, GPA calculation formula, weighted average, null grade handling, division by zero avoidance

**Question (Silberschatz 7e Exercise 4.6).**  
Show how to define the view *student_grades* ($ID$, $GPA$) giving the grade-point average of each student, based on the query in Exercise 3.2; recall that we used a relation *grade_points*(*grade*, *points*) to get the numeric points associated with a letter grade. Make sure your view definition correctly handles the case of null values for the *grade* attribute of the *takes* relation.

---

#### 1. Core Principles & Concept Overview

##### Mathematical Definition of GPA
The Grade Point Average (GPA) is a credit-weighted average of numeric points:

$$
\text{GPA} = \frac{\sum_{i=1}^n (\text{credits}_i \times \text{points}_i)}{\sum_{i=1}^n \text{credits}_i}
$$

##### Relevant Relational Schemas
- `student` = $(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{tot\_cred})$
- `takes` = $(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{grade})$
- `course` = $(\underline{\text{course\_id}}, \text{title}, \text{dept\_name}, \text{credits})$
- `grade_points` = $(\underline{\text{grade}}, \text{points})$

##### Edge Cases to Handle
1. **Null Grades:** A student currently enrolled in a course has `takes.grade = NULL`. These ongoing courses must not contribute to either the numerator ($\sum \text{credits} \times \text{points}$) or the denominator ($\sum \text{credits}$).
2. **Division by Zero:** If a student has taken 0 courses, or all their taken courses have `NULL` grades, $\sum \text{credits} = 0$ or `NULL`. Dividing by zero causes a database runtime exception.
3. **Students with No Courses:** To include *every* student in `student_grades`, a `LEFT OUTER JOIN` starting from `student` is required.

---

#### 2. Detailed Step-by-Step Solution

##### SQL View Definition (Comprehensive & Production-Grade)

```sql
create view student_grades (ID, GPA) as
select student.ID,
       case
           -- If student has no graded credits, GPA is NULL (or 0.0)
           when sum(case when takes.grade is not null then course.credits else 0 end) = 0 
           then null
           else
               sum(course.credits * grade_points.points) /
               sum(case when takes.grade is not null then course.credits end)
       end as GPA
from student
     left outer join takes on student.ID = takes.ID
     left outer join course on takes.course_id = course.course_id
     left outer join grade_points on takes.grade = grade_points.grade
group by student.ID;
```

##### Clean Standard Formulation (Filtering Incomplete Grades in Sub-Join)
An alternative, clean SQL structure pre-filters valid grades before joining:

```sql
create view student_grades (ID, GPA) as
select student.ID,
       case
           when sum(course.credits) is null or sum(course.credits) = 0 then null
           else sum(course.credits * grade_points.points) / sum(course.credits)
       end as GPA
from student
     left outer join (
         takes join course on takes.course_id = course.course_id
               join grade_points on takes.grade = grade_points.grade
         where takes.grade is not null
     ) as graded_records on student.ID = graded_records.ID
group by student.ID;
```

##### Minimal Formulation (For Students with At Least One Completed Grade)
If the view is only required for students who have earned at least one completed grade:

```sql
create view student_grades (ID, GPA) as
select takes.ID,
       sum(course.credits * grade_points.points) / sum(course.credits) as GPA
from takes
     join course on takes.course_id = course.course_id
     join grade_points on takes.grade = grade_points.grade
where takes.grade is not null
group by takes.ID;
```

---

#### 3. RUET Exam Insights & Examiner Notes
- **Connection to RUET Exam Questions:** In 2023 Q.5(b) (5 marks), students were asked: *"Explain how views provide data independence and write a query to create a view over two tables."* Presenting this exact `student_grades` view demonstrates real-world SQL engineering, handling joins, aggregates, and null safety.
- **Credit Weighting Trap:** Many students write `AVG(grade_points.points)`! This is fundamentally incorrect because courses have different credit weights (e.g., a 4-credit course has double the impact of a 2-credit course). You must use $\sum(\text{credits} \times \text{points}) / \sum(\text{credits})$.

---

### Exercise EX 4.20 · Defining an Aggregate View tot_credits

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.20, Page 180
> - **Subtopic:** T06.4 (View definition, multi-table aggregation)
> - **RUET Relevance:** Common short-note question: *"How do views simplify complex aggregate reporting?"*
> - **Key Concepts:** Aggregate view, `GROUP BY`, credit summation per academic calendar year

**Question (Silberschatz 7e Exercise 4.20).**  
Show how to define a view *tot_credits* (*year*, *num_credits*), giving the total number of credits taken in each year.

---

#### 1. Core Principles & Concept Overview

##### Schema Requirements
- `takes` = $(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \mathbf{\text{year}}}, \text{grade})$
- `course` = $(\underline{\text{course\_id}}, \text{title}, \text{dept\_name}, \mathbf{\text{credits}})$

To compute the total number of credits taken in each year across the entire university:
1. Join `takes` with `course` on `course_id` to obtain the credit weight of each course taken.
2. Group the tuples by academic `year`.
3. Apply the aggregate function `SUM(credits)`.

---

#### 2. Detailed Step-by-Step Solution

##### SQL View Definition

```sql
create view tot_credits (year, num_credits) as
select takes.year, sum(course.credits) as num_credits
from takes
     join course on takes.course_id = course.course_id
group by takes.year;
```

*(Using natural join syntax:)*
```sql
create view tot_credits (year, num_credits) as
select year, sum(credits) as num_credits
from takes natural join course
group by year;
```

##### Handling Years with Zero Enrollments
If the university administration maintains an academic calendar table `years(year)` and desires that years with zero course registrations display `0` rather than being omitted:

```sql
create view tot_credits (year, num_credits) as
select y.year, coalesce(sum(course.credits), 0) as num_credits
from (select distinct year from section) as y
     left outer join (takes join course using (course_id)) using (year)
group by y.year;
```

---

#### 3. RUET Exam Insights & Examiner Notes
- **Simplicity and Directness:** For 3-mark questions in Section B of RUET semester finals, the standard 4-line `CREATE VIEW` query using `takes JOIN course GROUP BY year` is completely sufficient. Ensure column aliases `(year, num_credits)` are specified in the view header.

---

## T06.5 · View Updatability, Authorization, and Materialized Views

### Exercise EX 4.13 · View Authorizations and Invisible Tuple Insertions

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.13, Page 178–179
> - **Subtopic:** T06.5 (View authorization decoupling, update anomaly, WITH CHECK OPTION)
> - **RUET Relevance:** Core theory question on database security and authorization mechanisms (Unit 4 & Unit 8)
> - **Key Concepts:** Decoupled view privileges, principle of least privilege, view insertion anomalies, `WITH CHECK OPTION`

**Question (Silberschatz 7e Exercise 4.13).**  
Consider a view $v$ whose definition references only relation $r$.

- If a user is granted select authorization on $v$, does that user need to have select authorization on $r$ as well? Why or why not?
- If a user is granted update authorization on $v$, does that user need to have update authorization on $r$ as well? Why or why not?
- Give an example of an insert operation on a view $v$ to add a tuple $t$ that is not visible in the result of **select** $*$ **from** $v$. Explain your answer.

---

#### 1. Core Principles & Concept Overview

##### Decoupled View Authorization
A fundamental design goal of the relational database security architecture is **data abstraction and column/row-level security**.
- If granting access to a view required granting access to the underlying table $r$, views could *never* hide sensitive data! (e.g., if a clerk needed access to employee phone numbers via a view, giving them access to the base `employee` table would leak salaries).
- SQL enforces authorization decoupling: The **creator** of the view must possess the required authorizations on relation $r$. Once created, the database system checks permissions on $v$ alone for end-users.

---

#### 2. Detailed Step-by-Step Solution

##### Part 1: SELECT Authorization Analysis
- **Answer:** **No.** The user does not need `SELECT` authorization on $r$.
- **Reason:**  
  The view mechanism is specifically intended to provide **access control and security filters**. For instance, a university may create a view `faculty_public` displaying `(ID, name, dept_name)` from the base relation `instructor(ID, name, dept_name, salary)`, deliberately omitting `salary`. If users required direct `SELECT` privileges on `instructor`, they could bypass the view and query salaries directly, nullifying security. The view creator needs `SELECT` privileges on $r$ to define the view; subsequent query callers only need `SELECT` privileges on $v$.

##### Part 2: UPDATE Authorization Analysis
- **Answer:** **No.** The user does not need `UPDATE` authorization on $r$.
- **Reason:**  
  By the exact same security rationale, views allow restricted modification rights. For example, a department head may be granted `UPDATE` authorization on a view that exposes only instructors within their specific department (`WHERE dept_name = 'Comp. Sci.'`). If the department head had direct `UPDATE` privileges on base relation `instructor`, they could modify salaries across all departments. The view limits the update scope to authorized rows and columns without exposing the base relation.

##### Part 3: Example of an Invisible Tuple Insertion

Let base relation $r$ be `instructor(ID, name, dept_name, salary)`.  
Define view $v$ as:

```sql
create view biology_instructors as
select ID, name, dept_name, salary
from instructor
where dept_name = 'Biology';
```

Now execute an insert through the view:

```sql
insert into biology_instructors values ('98324', 'Feynman', 'Physics', 95000);
```

**What Happens and Explanation:**
1. View $v$ is updatable (it queries a single relation, projects primary key `ID` and attributes without aggregation).
2. The database translates the insert into an insert on the base table `instructor`:
   `('98324', 'Feynman', 'Physics', 95000)` is physically inserted into `instructor`.
3. However, when the user subsequently executes:
   ```sql
   select * from biology_instructors;
   ```
   The query expands to:
   ```sql
   select ID, name, dept_name, salary
   from instructor
   where dept_name = 'Biology';
   ```
4. The newly inserted tuple has `dept_name = 'Physics'`. It fails the `WHERE dept_name = 'Biology'` predicate and is **omitted from the view result**!

##### Prevention via `WITH CHECK OPTION`
To prevent users from inserting or updating tuples through a view into states that violate the view's `WHERE` clause, SQL provides the `WITH CHECK OPTION` clause:

```sql
create view biology_instructors as
select ID, name, dept_name, salary
from instructor
where dept_name = 'Biology'
with check option;
```

With this clause enabled, the previous insert is rejected with an SQL integrity exception.

---

#### 3. RUET Exam Insights & Examiner Notes
- **Key Exam Takeaways:** In RUET exams, questions on SQL authorization frequently ask: *"How does a DBMS implement column-level and row-level security without storing separate permissions per cell?"* The answer is: **Views combined with decoupled GRANT SELECT/UPDATE**.

---

### Exercise EX 4.21 · View Updatability Violations in Aggregate Views

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 4 (*Intermediate SQL*), Exercise 4.21, Page 180 *(Referring to Exercise 4.20 errata in 7e print)*
> - **Subtopic:** T06.5 (Updatable views, SQL standard updatability criteria)
> - **RUET Relevance:** High probability theoretical question on view limitations
> - **Key Concepts:** SQL:1999 updatability rules, aggregation non-invertibility, missing primary keys

**Question (Silberschatz 7e Exercise 4.21).**  
For the view of Exercise 4.20 [*tot_credits* (*year*, *num_credits*)], explain why the database system would not allow a tuple to be inserted into the database through this view.

*(Note: The textbook print references Exercise 4.18, which is an erratum in the 7th edition; the intended reference is the `tot_credits` aggregate view defined in Exercise 4.20).*

---

#### 1. Core Principles & Concept Overview

##### The Inverse Mapping Problem
When an `INSERT`, `UPDATE`, or `DELETE` statement is issued against a view $V$, the DBMS must translate that operation into a sequence of equivalent operations on the underlying base relations $R_1, \dots, R_k$.

For an insert to be well-defined, there must exist a **unique, unambiguous inverse translation** from the view tuple to base relation tuples.

---

#### 2. Detailed Step-by-Step Solution

Recall the view definition from Exercise 4.20:
```sql
create view tot_credits (year, num_credits) as
select year, sum(credits)
from takes natural join course
group by year;
```

The database system completely disallows inserting a tuple (e.g., `INSERT INTO tot_credits VALUES (2025, 450);`) for three fundamental theoretical and practical reasons:

##### 1. Non-Invertibility of Aggregate Functions (`SUM`)
An aggregate function maps a set of multiple values into a single scalar value. There are infinitely many combinations of individual student course enrollments whose credits sum to 450 (e.g., 150 students taking one 3-credit course, or 100 students taking 4.5 credits, etc.). The database has no semantic basis to decide which base-table rows to manufacture.

##### 2. Violation of Formal SQL Standard Updatability Criteria
Under the ISO/IEC SQL standard (SQL:1999 and SQL:2003 onwards), a view $V$ is updatable **if and only if** all of the following conditions are met:
1. The `FROM` clause contains **exactly one** base relation (not a join or union).
2. The `SELECT` clause contains only simple attribute names (no expressions, arithmetic, or aggregate functions like `SUM`, `AVG`, `COUNT`).
3. The `SELECT` list does not contain `DISTINCT`.
4. The query does not contain a `GROUP BY` or `HAVING` clause.
5. Any attribute of the underlying base relation that is not listed in the view's `SELECT` clause must either allow `NULL` values or possess an explicit `DEFAULT` value.

View `tot_credits` violates almost every single rule:
- It joins **two** base relations (`takes` and `course`).
- It uses the aggregate function `SUM(credits)`.
- It contains a `GROUP BY` clause.

##### 3. Absence of Primary Key Attributes
The primary keys of the base relations are:
- `course`: `course_id`
- `takes`: `(ID, course_id, sec_id, semester, year)`

Neither `ID`, `course_id`, nor `sec_id` appear in `tot_credits`. Inserting `(2025, 450)` would require inserting rows into `takes` with `NULL` for `ID` and `course_id`, violating entity integrity (`PRIMARY KEY` columns cannot be null).

---

#### 3. RUET Exam Insights & Examiner Notes
- **Summary Checklist for Full Marks:** When asked why an insert on an aggregate view is rejected, RUET examiners look for three points:
  1. The inverse translation is mathematically ambiguous (infinitely many combinations sum to the same number).
  2. SQL updatability rules strictly forbid `GROUP BY`, aggregates, and joins in updatable views.
  3. Base table primary keys (`takes.ID`, `course_id`) are missing, violating entity integrity.

---

### Exercise PE 5.6 · Materialized View Incremental Maintenance via Triggers

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Practice Exercise 5.6, Page 234
> - **Subtopic:** T06.5 (Materialized views, incremental view maintenance, ECA triggers)
> - **RUET Relevance:** Advanced Unit 4/Unit 8 synthesis question; connects SQL views directly to SQL Triggers (Topic T07)
> - **Key Concepts:** Materialized views, incremental view maintenance (IVM), delta queries, row-level triggers

**Question (Silberschatz 7e Practice Exercise 5.6).**  
Consider the bank database of Figure 5.21:
- `branch(branch_name, branch_city, assets)`
- `customer(customer_name, customer_street, customer_city)`
- `loan(loan_number, branch_name, amount)`
- `borrower(customer_name, loan_number)`
- `account(account_number, branch_name, balance)`
- `depositor(customer_name, account_number)`

Let us define a view `branch_cust` as follows:

```sql
create view branch_cust as
select branch_name, customer_name
from depositor, account
where depositor.account_number = account.account_number;
```

Suppose that the view is materialized; that is, the view is computed and stored. Write triggers to maintain the view, that is, to keep it up-to-date on insertions to *depositor* or *account*. It is not necessary to handle deletions or updates. Note that, for simplicity, we have not required the elimination of duplicates.

---

#### 1. Core Principles & Concept Overview

##### Materialized Views and the Maintenance Problem
A standard view is a **virtual relation** recomputed upon each query execution. A **materialized view** physically stores the computed tuples on disk to accelerate frequent read-heavy reporting queries.

However, when underlying base tables are modified, the materialized copy becomes stale. Recomputing the entire view from scratch is computationally prohibitive. Databases utilize **Incremental View Maintenance (IVM)**:

For a join view $V = R \bowtie S$:
When an insertion occurs on $R$ ($\Delta R$), the change to the view is:

$$
\Delta V = \Delta R \bowtie S
$$

When an insertion occurs on $S$ ($\Delta S$), the change to the view is:

$$
\Delta V = R \bowtie \Delta S
$$

In database systems without automated engine-level IVM, this is implemented using **ECA (Event-Condition-Action) triggers**.

---

#### 2. Detailed Step-by-Step Solution

Let the materialized view be represented by a physical table:
```sql
create table branch_cust (
    branch_name varchar(50),
    customer_name varchar(50)
);
```

We must write two row-level triggers:
1. `maintain_branch_cust_on_depositor`: Fires after an insertion into `depositor`.
2. `maintain_branch_cust_on_account`: Fires after an insertion into `account`.

##### Trigger 1: On Insertion to `depositor`

When a new row `new_dep` is inserted into `depositor(customer_name, account_number)`:
- We search the `account` table for all accounts matching `account_number = new_dep.account_number`.
- For each matching account found, insert `(account.branch_name, new_dep.customer_name)` into `branch_cust`.

```sql
create trigger trig_depositor_insert
after insert on depositor
referencing new row as new_dep
for each row
when (new_dep.account_number is not null)
begin
    insert into branch_cust (branch_name, customer_name)
    select account.branch_name, new_dep.customer_name
    from account
    where account.account_number = new_dep.account_number;
end;
```

##### Trigger 2: On Insertion to `account`

When a new row `new_acc` is inserted into `account(account_number, branch_name, balance)`:
- We search the `depositor` table for all customers matching `account_number = new_acc.account_number`.
- For each matching customer found, insert `(new_acc.branch_name, depositor.customer_name)` into `branch_cust`.

```sql
create trigger trig_account_insert
after insert on account
referencing new row as new_acc
for each row
when (new_acc.account_number is not null)
begin
    insert into branch_cust (branch_name, customer_name)
    select new_acc.branch_name, depositor.customer_name
    from depositor
    where depositor.account_number = new_acc.account_number;
end;
```

##### Verification and Execution Trace

Suppose initial tables are empty.
1. Insert account: `INSERT INTO account VALUES ('A-101', 'Downtown', 500);`
   - Trigger `trig_account_insert` fires.
   - Searches `depositor` for `account_number = 'A-101'`. None found. No rows added to `branch_cust`.
2. Insert depositor: `INSERT INTO depositor VALUES ('Johnson', 'A-101');`
   - Trigger `trig_depositor_insert` fires.
   - Searches `account` for `account_number = 'A-101'`. Finds `('A-101', 'Downtown', 500)`.
   - Inserts `('Downtown', 'Johnson')` into `branch_cust`.
3. Materialized table `branch_cust` now holds `('Downtown', 'Johnson')`, exactly matching the view definition!

---

#### 3. RUET Exam Insights & Examiner Notes
- **Bridge Between Topics T06 and T07:** This problem frequently appears in advanced questions exploring the boundary between **Views (T06)** and **Triggers (T07)**. In RUET semester finals, questions often ask: *"What is a materialized view? How can SQL triggers be utilized to keep a materialized view synchronized with base relations?"*
- **Syntax Variations:** While Oracle uses `:NEW.account_number` and MySQL uses `NEW.account_number`, the standard SQL syntax presented above with `referencing new row as new_row` is standard Silberschatz textbook syntax and receives 100% marks across all exam evaluators.

---

## Summary and Key Formulae Reference for Exam Preparation

> [!tip] Quick Review Summary for RUET Finals
> 
> 1. **Outer Join Operator Algebra:**
>    - Left outer join preserves left relation: $R \mathbin{⟕} S = (R \bowtie S) \cup ((R - \Pi_R(R \bowtie S)) \times \{\text{null}\})$
>    - Right outer join preserves right relation: $R \mathbin{⟖} S = (R \bowtie S) \cup (\{\text{null}\} \times (S - \Pi_S(R \bowtie S)))$
>    - Full outer join preserves both: $R \mathbin{⟗} S = (R \mathbin{⟕} S) \cup (R \mathbin{⟖} S)$
> 2. **Associativity Trap:**
>    - Inner join is associative: $(A \bowtie B) \bowtie C \equiv A \bowtie (B \bowtie C)$.
>    - Outer join is **not associative**: $(A \mathbin{⟕} B) \mathbin{⟕} C \not\equiv A \mathbin{⟕} (B \mathbin{⟕} C)$.
> 3. **The Outer Join Aggregate Trap:**
>    - **Never** write `COUNT(*)` after an outer join if counting preserved records.
>    - **Always** write `COUNT(right_table.key)` to ensure unmatched rows containing nulls evaluate to `0`.
> 4. **Natural Join Danger:**
>    - Automatically matches all columns with the same name. Unintended attribute name collisions (such as `dept_name` across `instructor` and `course`) quietly eliminate valid data without syntax errors.
> 5. **SQL Standard Updatability Checklist:**
>    - A view is updatable ONLY IF:
>      - 1 single base relation in `FROM`.
>      - No aggregates (`SUM, AVG, COUNT, MIN, MAX`).
>      - No `GROUP BY` or `HAVING`.
>      - No `DISTINCT`.
>      - Base table primary keys and `NOT NULL` columns without defaults are preserved.


---

[← Prev: T05 Part 4](T05_Part4_SQL_MultiTable_Business_Queries.md) | [Index](00_Index.md) | [Next: T07 →](T07_Triggers_and_Stored_Procedures.md)
