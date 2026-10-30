---
title: "T05 · SQL (Part 2 · Query Clauses, Ordering & Aggregation Queries) — Textbook Exercise Solutions"
tags: [ece2215, database-systems, silberschatz-exercises, topic-T05]
topic_id: T05
part: 2
exercise_count: 12
source_chapters: ["Chapter 03", "Chapter 04", "Chapter 05"]
---

[← Prev: T05 Part 1](T05_Part1_SQL_DDL_DML_Basics.md) | [Index](00_Index.md) | [Next: T05 Part 3 →](T05_Part3_SQL_Aggregations_and_Subqueries.md)

---

# T05 · SQL (Part 2 · Query Clauses, Ordering & Aggregation Queries) — Solutions

[← Prev: T05 Part 1](T05_Part1_SQL_DDL_DML_Basics.md) | [Exam-style T05](../Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T05 Part 3 →](T05_Part3_SQL_Aggregations_and_Subqueries.md)

---

## Topic Card & Overview

| Metadata Item | Specification & Vault Mapping |
| :--- | :--- |
| **Topic ID & Name** | **T05 · SQL (Structured Query Language)** |
| **Document Role** | Part 2: Query Clauses, String Matching, Ordering, Aggregation, GPA Calculations & OLAP |
| **Syllabus Unit** | **Unit 4: Structured Query Language (SQL)** |
| **RUET Exam Weight** | **130 Marks** across 7 Finals (`20.4%` total exam share · Ranked **#1** overall) |
| **Subtopics Covered** | `T05.3` (Query clauses, `LIKE`, `CASE`), `T05.4` (Aggregate theory & NULLs), `T05.5` (Part A · `GROUP BY`, `HAVING`, CGPA, Window Ranking, OLAP) |
| **Textbook Sources** | Silberschatz, Korth & Sudarshan, *Database System Concepts* (7th Ed.): Chapters 03, 04, and 05 |
| **Assigned Exercises** | **12 Problems**: PE 3.2, PE 3.5, PE 3.6, EX 3.11, EX 3.22, EX 3.30, EX 3.34, EX 4.22, PE 5.8, PE 5.9, PE 5.10, PE 5.11 |

---

## Table of Exercises

| # | Exercise Ref | Subtopic | Category / Focus | Key SQL Constructs & Core Concepts |
| :-: | :--- | :---: | :--- | :--- |
| 1 | **PE 3.6** | `T05.3` | String Pattern Matching | `LIKE`, wildcards (`%`, `_`), `LOWER()`, case-insensitive matching |
| 2 | **EX 3.22** | `T05.3` | Predicate Transformation | `UNIQUE` predicate semantics, simulation via `GROUP BY`, `HAVING`, `NOT EXISTS` |
| 3 | **EX 4.22** | `T05.3` | Conditional Expressions | `COALESCE(e1, ..., en)` equivalence via standard `CASE` construct |
| 4 | **EX 3.30** | `T05.4` | Aggregation Theory & NULLs | `AVG(salary)` vs. `SUM(salary)/COUNT(*)`, non-zero discrepancy under NULL values |
| 5 | **PE 3.2** | `T05.5` | University CGPA & NULLs | Weighted average $\frac{\sum(\text{credits} \times \text{points})}{\sum\text{credits}}$, multi-table joins, handling NULL grades |
| 6 | **PE 3.5** | `T05.5` | Categorization & Frequency | Score categorization with `CASE`, frequency distribution with `GROUP BY` |
| 7 | **EX 3.11** | `T05.5` | Departmental Extrema & Sets | `DISTINCT`, temporal set difference (`EXCEPT`/`NOT IN`), departmental `MAX`, minimum of maximums |
| 8 | **EX 3.34** | `T05.5` | Multi-Attribute Grouping | `GROUP BY course_id, sec_id, year, semester`, column aliasing, `COUNT(ID)` vs. `COUNT(*)` |
| 9 | **PE 5.8** | `T05.5` | Window Function Ranking | `RANK() OVER (ORDER BY total DESC)`, handling tied positions at top-$K$ cutoffs |
| 10 | **PE 5.9** | `T05.5` | Time-Series Ranking | `RANK() OVER (ORDER BY shares_traded DESC)` on NYSE records, calculation vs. presentation order |
| 11 | **PE 5.10** | `T05.5` | Multidimensional OLAP | Hierarchical multi-level aggregation using `ROLLUP(year, month, day)` |
| 12 | **PE 5.11** | `T05.5` | OLAP Algebraic Equivalence | Simulating $n$-dimensional `CUBE(a, b, c, d)` via Cartesian product of single-column `ROLLUP`s |

---

## T05.3 · Basic Query Clauses, String Pattern Matching & Conditional Expressions

This section covers the foundational query clauses of SQL that govern filtering, pattern recognition, and conditional branching within single- and multi-table queries.

---

### Exercise 3.6 · Case-Insensitive String Pattern Matching (`LIKE` & `LOWER()`)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Practice Exercise 3.6, Page 117.
> - **Subtopic:** `T05.3` (Basic query clauses: `DISTINCT`, `ORDER BY`, `AS`, `LIKE`).
> - **Primary Schema:** `department(dept_name, building, budget)`.
> - **Target Competency:** String pattern matching, wildcard operators, and functional case normalization.

**Question (Silberschatz 7e Exercise 3.6).**  
The SQL `like` operator is case sensitive (in most systems), but the `lower()` function on strings can be used to perform case-insensitive matching. To show how, write a query that finds departments whose names contain the string “sci” as a substring, regardless of the case.

#### 1. Core Principles & Concept Overview

SQL provides the `LIKE` operator to perform pattern matching on character strings. It relies on two special wildcard characters:
1. **Percent sign (`%`)**: Matches any substring of zero or more characters.
2. **Underscore (`_`)**: Matches any single character.

##### Case Sensitivity Across SQL Engines
- **Standard SQL & Strict Engines (PostgreSQL, Oracle):** String comparisons and `LIKE` predicates are strictly case-sensitive. The character `'s'` does not match `'S'`.
- **MySQL (Default Collation):** In default installations (e.g., `utf8mb4_0900_ai_ci`), string comparisons are case-insensitive by default because of the collation (`_ci` stands for *case-insensitive*).
- **Universal Portability Rule:** To ensure code functions identically across all database management systems (DBMS), case normalization using `LOWER(str)` or `UPPER(str)` is the industry-standard design pattern.

When the string `'sci'` can appear anywhere inside `dept_name` in uppercase, lowercase, or mixed case (e.g., `'Comp. Sci.'`, `'SCIENCE'`, `'Cognitive Science'`, `'Neuroscience'`), converting both the column value and the pattern to lowercase guarantees an exact match.

#### 2. Detailed Step-by-Step Solution

##### SQL Query
```sql
SELECT dept_name
FROM department
WHERE LOWER(dept_name) LIKE '%sci%';
```

##### Alternative Symmetric Implementation
```sql
SELECT dept_name
FROM department
WHERE UPPER(dept_name) LIKE '%SCI%';
```

##### Query Execution Trace & Mechanics
1. **`FROM department`**: Scans the relation `department`.
2. **`WHERE` Evaluation**:
   - For each tuple, the scalar function `LOWER(dept_name)` converts characters to lowercase (e.g., `'Comp. Sci.'` $\to$ `'comp. sci.'`).
   - The pattern `'%sci%'` checks:
     - Leading `%`: Zero or more characters precede `'sci'`.
     - Substring `'sci'`: The exact character sequence `'s'`, `'c'`, `'i'`.
     - Trailing `%`: Zero or more characters succeed `'sci'`.
   - Tuples evaluating to `TRUE` are preserved.
3. **`SELECT dept_name`**: Projects the original, unmodified department name as stored in the database.

> [!tip] Performance & Indexing Consideration
> Evaluating `LOWER(dept_name)` forces a full-table scan (FTS) because a standard B-tree index on `dept_name` cannot be directly searched using a functional transformation. In production environments with high query volumes, a **Function-Based Index** (or Expression Index) is created:
> ```sql
> CREATE INDEX idx_dept_name_lower ON department (LOWER(dept_name));
> ```

#### 3. RUET Exam Insights & Examiner Notes
- **Past RUET Exam Connection:** String filtering appears frequently in RUET semester finals, most notably in **2019 Q.7(a)(ii)**, which requested all students whose name begins with the letter `'A'` (`WHERE St_Name LIKE 'A%'`).
- **Examiner Traps:**
  - Omitting the surrounding `%` signs (e.g., writing `LIKE 'sci'` instead of `LIKE '%sci%'`), which converts a substring search into an exact match for the three-letter word `'sci'`.
  - Confusing SQL equality (`=`) with pattern matching (`LIKE`). The expression `LOWER(dept_name) = '%sci%'` evaluates to false unless the department is literally named `"%sci%"`.

---

### Exercise 3.22 · Expressing `WHERE UNIQUE (...)` Predicate via Standard Constructs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Exercise 3.22, Page 122.
> - **Subtopic:** `T05.3` (Basic query clauses and relational predicates).
> - **Primary Schema:** `course(course_id, title, dept_name, credits)`.
> - **Target Competency:** Relational predicate transformations, quantification, and subquery logic without proprietary or obsolete SQL constructs.

**Question (Silberschatz 7e Exercise 3.22).**  
Rewrite the `where` clause

```sql
where unique (select title from course)
```

without using the `unique` construct.

#### 1. Core Principles & Concept Overview

##### The Standard SQL `UNIQUE` Predicate
In standard SQL, the predicate `UNIQUE (Q)` takes a subquery $Q$ and evaluates to:
- **`TRUE`** if no two tuples in the result of $Q$ are duplicates (i.e., every tuple in $Q$ is unique), or if the result of $Q$ is completely empty ($\emptyset$).
- **`FALSE`** if there exists at least one pair of duplicate tuples in the result of $Q$.

##### The Real-World Implementation Reality
Almost no mainstream commercial relational database (including PostgreSQL, MySQL, SQLite, and Oracle) implements the subquery `UNIQUE (SELECT ...)` predicate. It is an ANSI SQL standard feature that engine developers omitted due to implementation complexity and redundant syntax. Therefore, rewriting this predicate using standard SQL constructs is an essential database systems skill.

#### 2. Detailed Step-by-Step Solution

We present four rigorous methods to express the condition: *"No course title appears more than once in `course`"*.

##### Method A: Aggregative Negation via `GROUP BY` and `HAVING` (Recommended Standard)
A relation has no duplicate titles if and only if there does **not exist** any title whose frequency count exceeds 1.

```sql
WHERE NOT EXISTS (
    SELECT title
    FROM course
    GROUP BY title
    HAVING COUNT(*) > 1
)
```

**Algebraic Proof of Equivalence:**
Let $T = \Pi_{\text{title}}(\text{course})$ be the multiset of course titles.
- The subquery groups identical titles together and computes $n(t) = \text{COUNT}(*)$ for each title $t$.
- The clause `HAVING COUNT(*) > 1` filters for titles where $n(t) \ge 2$.
- If any such title exists, `EXISTS(...)` is `TRUE`, so `NOT EXISTS(...)` is `FALSE`.
- If no title appears more than once, the `HAVING` set is empty, making `NOT EXISTS(...)` evaluate to `TRUE`. This matches the semantics of `UNIQUE`.

##### Method B: Universal Quantification using `<= ALL`
```sql
WHERE 1 >= ALL (
    SELECT COUNT(*)
    FROM course
    GROUP BY title
)
```
If the maximum frequency of any title in the course table is $\le 1$, then no title is duplicated. If the table is empty, the subquery produces zero rows; by standard SQL semantics, `1 >= ALL (\emptyset)` evaluates to `TRUE`, exactly matching `UNIQUE(\emptyset) = TRUE`.

##### Method C: Correlated Self-Join on Primary Key
Two tuples have duplicate titles if they share the same title but possess different primary keys (`course_id`).
```sql
WHERE NOT EXISTS (
    SELECT 1
    FROM course c1
    JOIN course c2 ON c1.title = c2.title
    WHERE c1.course_id <> c2.course_id
)
```

##### Method D: Scalar Cardinality Comparison (Assuming Non-Null Titles)
Compare the total count of titles against the count of distinct titles:
```sql
WHERE (SELECT COUNT(title) FROM course) = (SELECT COUNT(DISTINCT title) FROM course)
```
If every title is unique, the set of distinct titles has the exact same cardinality as the multiset of all titles.

#### 3. RUET Exam Insights & Examiner Notes
- **Academic vs. Practical SQL:** RUET examiners frequently draw theoretical subquery questions from Silberschatz 7e. Because `UNIQUE (SELECT ...)` is covered in Section 3.8.5 of the textbook but unsupported in MySQL/PostgreSQL lab sessions, questions requiring students to eliminate or rewrite `UNIQUE` are premier exam material.
- **Examiner Scoring Preference:** Method A (`NOT EXISTS` with `GROUP BY ... HAVING COUNT(*) > 1`) is the gold standard answer on RUET theory papers. It explicitly demonstrates mastery over aggregation, filtering grouped records, and existential quantification.

---

### Exercise 4.22 · Expressing `COALESCE` via `CASE` Expressions

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Exercise 4.22, Page 180.
> - **Subtopic:** `T05.3` (Query clauses & conditional expressions).
> - **Primary Schema:** Conceptual / Universal SQL syntax.
> - **Target Competency:** Conditional branching, null handling, and syntactic reduction of standard library functions.

**Question (Silberschatz 7e Exercise 4.22).**  
Show how to express the **coalesce** function using the **case** construct.

#### 1. Core Principles & Concept Overview

##### The `COALESCE` Function
`COALESCE(e_1, e_2, \dots, e_n)` is an $n$-ary standard SQL function that returns the first non-null expression from its argument list, evaluated from left to right.
- If $e_1$ is not null, it evaluates to $e_1$.
- If $e_1$ is null but $e_2$ is not null, it evaluates to $e_2$.
- If all arguments $e_1, e_2, \dots, e_n$ are null, it evaluates to `NULL`.

##### The `CASE` Construct
The SQL `CASE` construct provides generalized conditional branching. The searched `CASE` expression has the syntax:
```sql
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ...
    WHEN condition_n THEN result_n
    ELSE default_result
END
```
Execution is strictly sequential: conditions are checked in order, and the result for the first condition evaluating to `TRUE` is returned. Remaining branches are not evaluated (short-circuit evaluation).

#### 2. Detailed Step-by-Step Solution

##### General Formulation for $n$ Expressions
For an arbitrary number of expressions $e_1, e_2, \dots, e_n$, `COALESCE(e_1, e_2, \dots, e_n)` is defined as:

```sql
CASE
    WHEN e1 IS NOT NULL THEN e1
    WHEN e2 IS NOT NULL THEN e2
    WHEN e3 IS NOT NULL THEN e3
    ...
    WHEN en IS NOT NULL THEN en
    ELSE NULL
END
```

##### Binary Specialization ($n = 2$)
For two expressions `COALESCE(e1, e2)`:
```sql
CASE
    WHEN e1 IS NOT NULL THEN e1
    ELSE e2
END
```
*Note on equivalence:* If $e_1$ is not null, the `WHEN` branch returns $e_1$. If $e_1$ is null, control falls through to `ELSE e2`. If $e_2$ is non-null, $e_2$ is returned; if $e_2$ is also null, the expression returns `NULL`. This matches `COALESCE(e1, e2)` in all input states.

##### Short-Circuit Verification Table

| $e_1$ | $e_2$ | $e_3$ | `COALESCE(e1, e2, e3)` | `CASE` Expression Output | Evaluated Branches |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `'Alpha'` | `'Beta'` | `NULL` | `'Alpha'` | `'Alpha'` | Branch 1 only |
| `NULL` | `'Beta'` | `'Gamma'` | `'Beta'` | `'Beta'` | Branches 1 and 2 |
| `NULL` | `NULL` | `'Gamma'` | `'Gamma'` | `'Gamma'` | Branches 1, 2, and 3 |
| `NULL` | `NULL` | `NULL` | `NULL` | `NULL` | Fallthrough to `ELSE NULL` |

#### 3. RUET Exam Insights & Examiner Notes
- **Practical Application in RUET Exams:** In database exams, missing data (e.g., absent bonus, unassigned advisor, in-progress grades) must often be replaced with a default constant like $0$ or `'N/A'`. When proprietary dialect functions such as MySQL's `IFNULL(a, b)` or Oracle's `NVL(a, b)` are prohibited, `COALESCE` or the universal `CASE` statement is mandatory.
- **Examiner Tip:** Always explicitly write `ELSE NULL END`. In SQL-92 and later, if no `ELSE` is specified and no `WHEN` matches, the default is implicitly `NULL`, but writing `ELSE NULL` confirms intentional handling of all-null vectors.

---

## T05.4 · Aggregate Functions Theory & NULL Value Handling in Aggregates

This section examines the formal mathematical definitions of SQL aggregate functions and reveals subtle edge-case behaviors when data sets contain `NULL` values.

---

### Exercise 3.30 · Aggregate Behavior with NULLs: Difference Between `avg(salary)` and `sum(salary)/count(*)`

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Exercise 3.30, Page 123.
> - **Subtopic:** `T05.4` (Aggregate functions theory ♻️).
> - **Primary Schema:** `instructor(ID, name, dept_name, salary)`.
> - **Target Competency:** Aggregate function mechanics, three-valued logic, and semantic divergence between `COUNT(*)` and `COUNT(column)`.

**Question (Silberschatz 7e Exercise 3.30).**  
Consider the following SQL query on the university schema:

```sql
select avg(salary) - (sum(salary) / count(*))
from instructor;
```

We might expect that the result of this query is zero since the average of a set of numbers is defined to be the sum of the numbers divided by the number of numbers. Indeed this is true for the example instructor relation in Figure 2.1. However, there are other possible instances of that relation for which the result would not be zero. Give one such instance, and explain why the result would not be zero.

#### 1. Core Principles & Concept Overview

##### Formal SQL Aggregate Rules on NULLs
1. **Column Aggregates (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT(column)`):**
   - All standard SQL aggregate functions operating on a specific attribute **strictly ignore `NULL` values** in their input multiset.
   - For an attribute $A$, $\text{COUNT}(A)$ denotes the number of tuples where $A \text{ IS NOT NULL}$.
   - $\text{AVG}(A)$ is algebraically defined in the SQL standard as:
     $$
     \text{AVG}(A) = \frac{\text{SUM}(A)}{\text{COUNT}(A)}
     $$
2. **Tuple Count (`COUNT(*)`):**
   - `COUNT(*)` counts the total number of physical rows in the relation (or group), regardless of whether any or all column values in those rows are `NULL`.

##### The Mathematical Discrepancy
Comparing $\text{AVG}(\text{salary})$ with $\frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)}$:
$$
\text{AVG}(\text{salary}) - \frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)} = \frac{\text{SUM}(\text{salary})}{\text{COUNT}(\text{salary})} - \frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)}
$$
If every row has a non-null salary, then $\text{COUNT}(\text{salary}) = \text{COUNT}(*)$, and the difference is exactly $0$.  
However, if **at least one instructor has `salary IS NULL`** (and there is at least one instructor with a non-null salary), then:
$$
\text{COUNT}(*) > \text{COUNT}(\text{salary}) \implies \frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)} < \frac{\text{SUM}(\text{salary})}{\text{COUNT}(\text{salary})}
$$
Consequently, the query yields a strictly positive non-zero result!

#### 2. Detailed Step-by-Step Solution

##### Step 1: Provide a Concrete Counterexample Instance
Consider an instance of the `instructor` relation containing three tuples:

| `ID` | `name` | `dept_name` | `salary` |
| :--- | :--- | :--- | :--- |
| `10101` | Srinivasan | Comp. Sci. | 65000 |
| `12121` | Wu | Finance | 90000 |
| `99999` | Guest | Comp. Sci. | `NULL` |

##### Step 2: Evaluate Each Aggregate Component
1. **Compute `SUM(salary)`:**
   - Ignores `NULL`.
   - $\text{SUM}(\text{salary}) = 65000 + 90000 = 155000$.
2. **Compute `AVG(salary)`:**
   - Ignores `NULL`, divides by count of non-null salaries ($2$).
   - $\text{AVG}(\text{salary}) = \frac{155000}{2} = 77500$.
3. **Compute `COUNT(*)`:**
   - Counts all 3 tuples in the table.
   - $\text{COUNT}(*) = 3$.
4. **Compute $\frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)}$:**
   - $\frac{155000}{3} \approx 51666.67$.

##### Step 3: Compute Query Output
$$
\text{Result} = \text{AVG}(\text{salary}) - \frac{\text{SUM}(\text{salary})}{\text{COUNT}(*)} = 77500 - 51666.67 = 25833.33 \neq 0
$$

##### Step 4: Examination of Boundary Edge Cases
1. **Case: All Salaries are NULL:**
   - If every instructor has `salary = NULL`, $\text{SUM}(\text{salary}) = \text{NULL}$ and $\text{AVG}(\text{salary}) = \text{NULL}$.
   - The expression evaluates to $\text{NULL} - (\text{NULL} / N) = \text{NULL}$. In three-valued logic, `NULL` is not zero.
2. **Case: Relation is Completely Empty ($N = 0$):**
   - $\text{COUNT}(*) = 0$, leading to a division-by-zero condition (which raises an exception or evaluates to `NULL` depending on RDBMS dialect).

#### 3. RUET Exam Insights & Examiner Notes
- **Direct RUET Syllabus & Question Bank Mapping:**
  - Tested repeatedly in RUET theory papers: **2018 Q.7(b)** and **2024 Q.7(a)** require students to define the aggregate functions and explain their behavior when encountering null values.
- **Examiner Scoring Trap:** Students routinely write that "average is sum divided by count" without distinguishing between `COUNT(*)` and `COUNT(column)`. RUET examiners specifically deduct marks if the student fails to emphasize that `COUNT(attribute)` ignores nulls while `COUNT(*)` tallies all physical tuples.

---

## T05.5 · Aggregation Queries, Group By, Having, CGPA Calculation, Window Ranking & Multidimensional OLAP

This section addresses complex grouping, statistical calculations (such as university CGPA), window ranking functions, and advanced online analytical processing (OLAP) aggregations.

---

### Exercise 3.2 · University CGPA Calculation and NULL Grade Handling

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Practice Exercise 3.2, Pages 116–117.
> - **Subtopic:** `T05.5` (Aggregation queries: `GROUP BY` + `HAVING`, CGPA ♻️).
> - **Primary Schema:** `student(ID, ...)`, `course(course_id, credits, ...)`, `takes(ID, course_id, sec_id, semester, year, grade)`, and `grade_points(grade, points)`.
> - **Target Competency:** Weighted aggregations, multi-table joins, CGPA derivation, and graceful degradation under NULL grade states.

**Question (Silberschatz 7e Exercise 3.2).**  
Suppose you are given a relation `grade_points(grade, points)` that provides a conversion from letter grades in the `takes` relation to numeric scores; for example, an “A” grade could be specified to correspond to 4 points, an “A−” to 3.7 points, a “B+” to 3.3 points, a “B” to 3 points, and so on. The grade points earned by a student for a course offering (section) is defined as the number of credits for the course multiplied by the numeric points for the grade that the student received.

Given the preceding relation, and our university schema, write each of the following queries in SQL. You may assume for simplicity that no `takes` tuple has the null value for `grade`.

a. Find the total grade points earned by the student with ID '12345', across all courses taken by the student.  
b. Find the grade point average (GPA) for the above student, that is, the total grade points divided by the total credits for the associated courses.  
c. Find the ID and the grade-point average of each student.  
d. Now reconsider your answers to the earlier parts of this exercise under the assumption that some grades might be null. Explain whether your solutions still work and, if not, provide versions that handle nulls properly.

#### 1. Core Principles & Concept Overview

##### Mathematical Definition of Cumulative GPA (CGPA)
The Cumulative Grade Point Average is a weighted arithmetic mean where each course's numeric grade point $p_i$ is weighted by the course's credit hours $c_i$:
$$
\text{Total Grade Points} = \sum_{i=1}^{n} (c_i \times p_i)
$$
$$
\text{CGPA} = \frac{\sum_{i=1}^{n} (c_i \times p_i)}{\sum_{i=1}^{n} c_i}
$$

##### Relational Navigation Path
To evaluate this formula, tuples from three distinct relations must be synthesized:
1. `takes(ID, course_id, ..., grade)`: Identifies which courses a student took and the letter grade earned.
2. `course(course_id, credits, ...)`: Provides the credit weight $c_i$ for each course.
3. `grade_points(grade, points)`: Maps letter grade $g_i$ to numeric scalar $p_i$.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Total Grade Points for Student '12345'
```sql
SELECT SUM(c.credits * gp.points) AS total_grade_points
FROM takes t
JOIN course c ON t.course_id = c.course_id
JOIN grade_points gp ON t.grade = gp.grade
WHERE t.ID = '12345';
```
*Explanation:* The query joins `takes` with `course` on `course_id`, and with `grade_points` on `grade`. It filters for student `'12345'` and evaluates $\sum (\text{credits} \times \text{points})$.

##### Part (b): Grade Point Average (GPA) for Student '12345'
```sql
SELECT SUM(c.credits * gp.points) / SUM(c.credits) AS GPA
FROM takes t
JOIN course c ON t.course_id = c.course_id
JOIN grade_points gp ON t.grade = gp.grade
WHERE t.ID = '12345';
```
*Explanation:* Both the numerator $\sum (c_i \times p_i)$ and denominator $\sum c_i$ are computed across the exact same set of completed courses.

##### Part (c): ID and GPA for Each Student
```sql
SELECT t.ID,
       SUM(c.credits * gp.points) / SUM(c.credits) AS GPA
FROM takes t
JOIN course c ON t.course_id = c.course_id
JOIN grade_points gp ON t.grade = gp.grade
GROUP BY t.ID;
```
*Explanation:* Grouping by `t.ID` partitions the joined stream by student, calculating the weighted quotient independently for every student enrolled in graded courses.

##### Part (d): Handling NULL Grades (In-Progress / Incomplete Courses)
In real academic databases, a student may be currently registered for courses in the active semester where `takes.grade IS NULL`.

###### Impact Analysis on Earlier Solutions
1. **Behavior of the Inner Join (`JOIN grade_points gp ON t.grade = gp.grade`):**
   - In SQL three-valued logic, `NULL = gp.grade` evaluates to `UNKNOWN`.
   - Because inner joins require the `ON` condition to evaluate to `TRUE`, all tuples with `grade IS NULL` are **automatically excluded** from the joined result.
2. **Assessment of Part (a):**
   - Query (a) **still works correctly**. Incompleted courses have earned zero grade points to date, so excluding them from the numerator sum is mathematically sound.
3. **Assessment of Part (b) and Part (c):**
   - Query (b) and (c) **still work correctly** for any student who has at least one graded course! Because the join eliminates null-grade courses *before* aggregation, `SUM(c.credits)` in the denominator only sums the credits of courses that actually contributed to the numerator.
   - **The Naive Subquery Trap:** If a student had written the denominator using an unjoined subquery:
     ```sql
     -- INCORRECT PITFALL VERSION
     SELECT SUM(c.credits * gp.points) / (SELECT SUM(credits) FROM takes NATURAL JOIN course WHERE ID = '12345') ...
     ```
     That query would include in-progress credits in the denominator while excluding them from the numerator, erroneously depressing the student's GPA!
4. **Where the Earlier Solutions Fail:**
   - **Case 1: Students with ONLY NULL grades:** A first-semester freshman registered for courses has tuples in `takes`, but all have `grade IS NULL`. The inner join produces zero rows. Query (c) completely omits this student from the output.
   - **Case 2: Students who have taken ZERO courses:** Students present in `student` but absent from `takes` are completely omitted.

###### Robust, Universal Solution for Part (d)
To include all students, display `NULL` for students without graded credits, and prevent division-by-zero runtime exceptions:

```sql
SELECT s.ID,
       CASE 
           WHEN SUM(CASE WHEN t.grade IS NOT NULL THEN c.credits ELSE 0 END) = 0 THEN NULL
           ELSE SUM(c.credits * gp.points) / 
                SUM(CASE WHEN t.grade IS NOT NULL THEN c.credits ELSE NULL END)
       END AS GPA
FROM student s
LEFT OUTER JOIN takes t ON s.ID = t.ID
LEFT OUTER JOIN course c ON t.course_id = c.course_id
LEFT OUTER JOIN grade_points gp ON t.grade = gp.grade
GROUP BY s.ID;
```

#### 3. RUET Exam Insights & Examiner Notes
- **Direct RUET Semester Final Questions:**
  - **RUET 2017 Q.4(a)(iii):** Calculate CGPA of each student from `MARKS(roll, sub_code, gpa)` and `CREDIT(sub_code, credit)`.
    ```sql
    SELECT m.roll,
           SUM(m.gpa * c.credit) / SUM(c.credit) AS cgpa
    FROM MARKS m
    JOIN CREDIT c ON m.sub_code = c.sub_code
    GROUP BY m.roll;
    ```
  - **RUET 2019 Q.7(a)(iii):** Given `Student(St_ID, St Name)`, `GPA(St_ID, Sub_Code, gpa)`, `Credit(Sub_Code, Credit)`, calculate the CGPA of each student.
    ```sql
    SELECT s.St_ID, s.`St Name`,
           SUM(g.gpa * c.Credit) / SUM(c.Credit) AS cgpa
    FROM Student s
    JOIN GPA g ON s.St_ID = g.St_ID
    JOIN Credit c ON g.Sub_Code = c.Sub_Code
    GROUP BY s.St_ID, s.`St Name`;
    ```
- **Examiner's Core Rule:** When writing queries for RUET exams, always group by both `ID` and `Name` if `Name` is selected in the projection (`SELECT s.St_ID, s.Name ... GROUP BY s.St_ID, s.Name`), in strict adherence to ANSI SQL-92 grouping integrity rules.

---

### Exercise 3.5 · Score Categorization via `CASE` and Frequency Aggregation with `GROUP BY`

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Practice Exercise 3.5, Page 117.
> - **Subtopic:** `T05.5` (Aggregation queries & conditional grouping).
> - **Primary Schema:** `marks(ID, score)`.
> - **Target Competency:** Score binning, conditional grading schemas, and multi-row aggregation over computed expressions.

**Question (Silberschatz 7e Exercise 3.5).**  
Suppose that we have a relation `marks(ID, score)` and we wish to assign grades to students based on the score as follows: grade F if $score < 40$, grade C if $40 \le score < 60$, grade B if $60 \le score < 80$, and grade A if $80 \le score$. Write SQL queries to do the following:

a. Display the grade for each student, based on the `marks` relation.  
b. Find the number of students with each grade.

#### 1. Core Principles & Concept Overview

##### Binning / Discretization Logic
Transforming continuous or integer numeric metrics (such as exam scores) into discrete categories (letter grades) is performed in SQL via searched `CASE` statements. Because `CASE` evaluations are ordered sequentially, bounds can be specified with concise upper bounds:
- If `score < 40`, grade is `'F'`.
- Else if `score < 60`, grade is `'C'` (since $\ge 40$ is guaranteed by earlier evaluation).
- Else if `score < 80`, grade is `'B'`.
- Else (`score >= 80`), grade is `'A'`.

##### Grouping by Computed Expressions
SQL allows grouping not only on physical table attributes but also on calculated scalar expressions. When grouping by a `CASE` construct, all rows mapping to the same output token form a single equivalence class.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Display Grade for Each Student
```sql
SELECT ID,
       CASE
           WHEN score < 40 THEN 'F'
           WHEN score < 60 THEN 'C'
           WHEN score < 80 THEN 'B'
           ELSE 'A'
       END AS grade
FROM marks;
```

##### Part (b): Number of Students with Each Grade

###### Approach 1: Grouping Directly on the CASE Expression
```sql
SELECT CASE
           WHEN score < 40 THEN 'F'
           WHEN score < 60 THEN 'C'
           WHEN score < 80 THEN 'B'
           ELSE 'A'
       END AS grade,
       COUNT(*) AS num_students
FROM marks
GROUP BY CASE
             WHEN score < 40 THEN 'F'
             WHEN score < 60 THEN 'C'
             WHEN score < 80 THEN 'B'
             ELSE 'A'
         END;
```

###### Approach 2: Using Common Table Expressions (CTE) / Derived Table (Clean Standard SQL)
```sql
WITH student_grades AS (
    SELECT ID,
           CASE
               WHEN score < 40 THEN 'F'
               WHEN score < 60 THEN 'C'
               WHEN score < 80 THEN 'B'
               ELSE 'A'
           END AS grade
    FROM marks
)
SELECT grade, COUNT(*) AS num_students
FROM student_grades
GROUP BY grade
ORDER BY grade ASC;
```

> [!tip] Advanced Grading Distribution: Preserving Zero-Count Grades
> In Approach 1 and 2, if no student scored below 40, the grade `'F'` will simply be absent from the result. If the academic department requires all defined grades (`A`, `B`, `C`, `F`) to appear, even with a count of $0$, a reference table with an outer join is deployed:
> ```sql
> WITH possible_grades(grade) AS (
>     SELECT 'A' UNION ALL SELECT 'B' UNION ALL SELECT 'C' UNION ALL SELECT 'F'
> ),
> student_grades AS (
>     SELECT ID,
>            CASE
>                WHEN score < 40 THEN 'F'
>                WHEN score < 60 THEN 'C'
>                WHEN score < 80 THEN 'B'
>                ELSE 'A'
>            END AS grade
>     FROM marks
> )
> SELECT pg.grade, COUNT(sg.ID) AS num_students
> FROM possible_grades pg
> LEFT OUTER JOIN student_grades sg ON pg.grade = sg.grade
> GROUP BY pg.grade;
> ```

#### 3. RUET Exam Insights & Examiner Notes
- **Relevance:** RUET course grading strictly maps marks to letter grades ($80\%+$ $\to$ A+, etc.). Exam problems frequently ask students to write classification scripts to generate batch grade sheets.
- **Examiner Tip on Aliasing:** In standard SQL, you cannot refer to a column alias defined in the `SELECT` list (`grade`) inside the `GROUP BY` clause of the same query block (though MySQL permits it as an extension). Using Approach 2 (CTE or derived table) is guaranteed full marks across all academic grading panels.

---

### Exercise 3.11 · Departmental Instructor Salaries and Extrema (`GROUP BY`, `HAVING`, Subqueries)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Exercise 3.11, Pages 120–121.
> - **Subtopic:** `T05.5` (Aggregation queries & subqueries) and `T05.3` (`DISTINCT`).
> - **Primary Schema:** `student`, `instructor`, `course`, `takes`.
> - **Target Competency:** Join projection with duplicate suppression, temporal exclusion, departmental aggregation, and nested extremum computation without proprietary `LIMIT` clauses.

**Question (Silberschatz 7e Exercise 3.11).**  
Write the following queries in SQL, using the university schema.

a. Find the ID and name of each student who has taken at least one Comp. Sci. course; make sure there are no duplicate names in the result.  
b. Find the ID and name of each student who has not taken any course offered before 2017.  
c. For each department, find the maximum salary of instructors in that department. You may assume that every department has at least one instructor.  
d. Find the lowest, across all departments, of the per-department maximum salary computed by the preceding query.

#### 1. Core Principles & Concept Overview

- **Part (a):** A student may take multiple Comp. Sci. courses across several semesters. An inner join between `student`, `takes`, and `course` generates one tuple per course enrolled. Duplicate student names/IDs must be eliminated using `DISTINCT`.
- **Part (b):** Requires finding the set complement of students who enrolled in courses with `year < 2017`. This can be expressed via set difference (`EXCEPT`), negative subquery containment (`NOT IN`), or correlated anti-join (`NOT EXISTS`).
- **Part (c):** Straightforward partitioned aggregation using `GROUP BY dept_name` and `MAX(salary)`.
- **Part (d):** Finding the "minimum of maximums". In standard relational algebra and SQL, aggregate functions cannot be directly nested (i.e., `MIN(MAX(salary))` is illegal syntax). The intermediate maximums must be computed in a subquery or CTE, followed by an outer `MIN()` aggregation.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Students Taking at Least One Comp. Sci. Course (No Duplicates)
```sql
SELECT DISTINCT s.ID, s.name
FROM student s
JOIN takes t ON s.ID = t.ID
JOIN course c ON t.course_id = c.course_id
WHERE c.dept_name = 'Comp. Sci.';
```

##### Part (b): Students Who Have Not Taken Any Course Offered Before 2017

###### Method 1: Set Difference via `EXCEPT` (ANSI SQL Standard)
```sql
SELECT ID, name
FROM student
EXCEPT
SELECT s.ID, s.name
FROM student s
JOIN takes t ON s.ID = t.ID
WHERE t.year < 2017;
```

###### Method 2: Uncorrelated Subquery with `NOT IN`
```sql
SELECT s.ID, s.name
FROM student s
WHERE s.ID NOT IN (
    SELECT t.ID
    FROM takes t
    WHERE t.year < 2017
);
```

###### Method 3: Correlated Subquery with `NOT EXISTS`
```sql
SELECT s.ID, s.name
FROM student s
WHERE NOT EXISTS (
    SELECT 1
    FROM takes t
    WHERE t.ID = s.ID 
      AND t.year < 2017
);
```
*Semantic Note on Edge Cases:* Students who have taken **no courses at all** are correctly included by all three formulations because the condition "has not taken any course offered before 2017" is vacuously true for them.

##### Part (c): Maximum Salary of Instructors in Each Department
```sql
SELECT dept_name, MAX(salary) AS max_salary
FROM instructor
GROUP BY dept_name;
```

##### Part (d): Lowest Per-Department Maximum Salary

###### Solution 1: Scalar Aggregate over Derived Table (Universal ANSI SQL)
```sql
SELECT MIN(max_salary) AS lowest_dept_max_salary
FROM (
    SELECT dept_name, MAX(salary) AS max_salary
    FROM instructor
    GROUP BY dept_name
) AS dept_maxima;
```

###### Solution 2: Common Table Expression (`WITH` Clause)
```sql
WITH dept_maxima AS (
    SELECT dept_name, MAX(salary) AS max_salary
    FROM instructor
    GROUP BY dept_name
)
SELECT MIN(max_salary) AS lowest_dept_max_salary
FROM dept_maxima;
```

###### Solution 3: Finding the Department and Value via `<= ALL`
If the examiner asks to identify which department has this lowest maximum salary:
```sql
WITH dept_maxima AS (
    SELECT dept_name, MAX(salary) AS max_salary
    FROM instructor
    GROUP BY dept_name
)
SELECT dept_name, max_salary
FROM dept_maxima
WHERE max_salary <= ALL (SELECT max_salary FROM dept_maxima);
```

#### 3. RUET Exam Insights & Examiner Notes
- **No `LIMIT` Constraint:** In RUET exams (specifically **CT-02 Q.1(d)** and **2024 Q.1(c)**), examiners explicitly penalize the use of MySQL-specific `ORDER BY max_salary ASC LIMIT 1`. Written theory exams demand relational algebra-compliant subqueries or CTEs.
- **`DISTINCT` Placement:** For part (a), writing `SELECT s.ID, DISTINCT s.name` is a syntax error. `DISTINCT` is a query-level modifier that must immediately follow `SELECT` and applies to the entire tuple projection.

---

### Exercise 3.34 · Multi-Attribute Section Enrollment Aggregation with `GROUP BY`

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 03 (*Introduction to SQL*), Exercise 3.34, Page 123.
> - **Subtopic:** `T05.5` (Aggregation queries & multi-column grouping).
> - **Primary Schema:** `takes(ID, course_id, sec_id, semester, year, grade)`.
> - **Target Competency:** Multi-attribute grouping, column aliasing (`AS`), and composite key aggregation.

**Question (Silberschatz 7e Exercise 3.34).**  
Using the university schema, write an SQL query to find the number of students in each section. The result columns should appear in the order “courseid, secid, year, semester, num”. You do not need to output sections with 0 students.

#### 1. Core Principles & Concept Overview

##### Uniquely Identifying a Section Offering
In the university schema, a course offering is uniquely identified by four composite attributes:
`course_id`, `sec_id`, `year`, and `semester`.
To aggregate metrics at the section level, all four attributes must be listed in the `GROUP BY` clause.

##### Counting Section Enrollments
Every row in `takes` represents one student enrolled in one section. Therefore, within each group:
- `COUNT(*)` counts the number of student enrollment rows.
- `COUNT(ID)` or `COUNT(DISTINCT ID)` yields identical results because `(ID, course_id, sec_id, semester, year)` forms the primary key of `takes`.

#### 2. Detailed Step-by-Step Solution

##### SQL Query
```sql
SELECT course_id AS courseid,
       sec_id AS secid,
       year,
       semester,
       COUNT(ID) AS num
FROM takes
GROUP BY course_id, sec_id, year, semester;
```

##### Ordering and Column Verification
- Column 1: `course_id AS courseid`
- Column 2: `sec_id AS secid`
- Column 3: `year`
- Column 4: `semester`
- Column 5: `COUNT(ID) AS num`
The output schema matches the required specification: `(courseid, secid, year, semester, num)`.

> [!tip] Extension Drill: What if Sections with 0 Students Were Required?
> If the problem required including sections that have zero student enrollments, querying `takes` alone would be insufficient because empty sections have no tuples in `takes`. We must query the master `section` relation with a `LEFT OUTER JOIN`:
> ```sql
> SELECT s.course_id AS courseid,
>        s.sec_id AS secid,
>        s.year,
>        s.semester,
>        COUNT(t.ID) AS num
> FROM section s
> LEFT OUTER JOIN takes t 
>   ON s.course_id = t.course_id
>  AND s.sec_id = t.sec_id
>  AND s.year = t.year
>  AND s.semester = t.semester
> GROUP BY s.course_id, s.sec_id, s.year, s.semester;
> ```
> *Crucial Distinction:* Here, we **must use `COUNT(t.ID)`** and not `COUNT(*)`. If `COUNT(*)` were used, a section with zero enrollments would return `1` because the outer join produces a row containing `NULL` for `t.ID`. `COUNT(t.ID)` correctly ignores the `NULL` and reports `0`.

#### 3. RUET Exam Insights & Examiner Notes
- **Exam Aliasing Practice:** RUET **2024 Q.7(b)(iv)** features a dedicated short note on the `AS` clause. Always ensure output aliases match the exam prompt verbatim.
- **Grouping Rule Compliance:** Every non-aggregated attribute appearing in the `SELECT` list must be explicitly enumerated in the `GROUP BY` clause.

---

### Exercise 5.8 · Window Function Ranking (`RANK()`) and Top-K with Tied Final Spots

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Practice Exercise 5.8, Page 235.
> - **Subtopic:** `T05.5` (Window ranking functions & analytical queries).
> - **Primary Schema:** $S(\text{student}, \text{subject}, \text{marks})$.
> - **Target Competency:** `RANK()` vs. `DENSE_RANK()`, window partitioning, and handling ties at rank cutoffs.

**Question (Silberschatz 7e Exercise 5.8).**  
Given a relation $S(\text{student}, \text{subject}, \text{marks})$, write a query to find the top 10 students by total marks, by using SQL ranking. Include all students tied for the final spot in the ranking, even if that results in more than 10 total students.

#### 1. Core Principles & Concept Overview

##### SQL Ranking Window Functions
SQL:1999 introduced analytical window functions that compute row rankings without collapsing the individual tuples into a single aggregated row:
1. **`ROW_NUMBER()`**: Assigns a strictly unique, contiguous integer sequence ($1, 2, 3, 4, \dots$). If two students have identical marks, ties are broken arbitrarily.
2. **`RANK()`**: Assigns identical ranks to tied rows, then skips subsequent ranks by the number of tied positions ($1, 2, 2, 4, \dots$).
3. **`DENSE_RANK()`**: Assigns identical ranks to tied rows, with no gaps in the subsequent numbering ($1, 2, 2, 3, \dots$).

##### The Problem Specification: Tied Final Spot
The requirement explicitly states: *"Include all students tied for the final spot in the ranking, even if that results in more than 10 total students."*
- If we filter by `RANK() <= 10`:
  - If ranks $1$ through $9$ are unique, and $3$ students tie for the $10^{\text{th}}$ position, all three receive `rank = 10`.
  - The query returns all $9 + 3 = 12$ students.
  - The next student would receive `rank = 13`, and is excluded.
- This behavior matches the standard mathematical and academic ranking convention.

#### 2. Detailed Step-by-Step Solution

##### SQL Query using Common Table Expressions (CTE)
```sql
WITH student_totals AS (
    SELECT student,
           SUM(marks) AS total_marks
    FROM S
    GROUP BY student
),
ranked_students AS (
    SELECT student,
           total_marks,
           RANK() OVER (ORDER BY total_marks DESC) AS rk
    FROM student_totals
)
SELECT student, total_marks, rk
FROM ranked_students
WHERE rk <= 10
ORDER BY rk ASC, student ASC;
```

##### Trace and Tie-Break Mechanics
Suppose students achieve the following total marks:

| `student` | `total_marks` | `RANK()` | `DENSE_RANK()` | `ROW_NUMBER()` | Included in `rk <= 10`? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Student 1 | 490 | 1 | 1 | 1 | Yes |
| Student 2 | 485 | 2 | 2 | 2 | Yes |
| ... | ... | ... | ... | ... | Yes |
| Student 9 | 450 | 9 | 9 | 9 | Yes |
| Student 10 | 445 | **10** | **10** | 10 | **Yes (Tied)** |
| Student 11 | 445 | **10** | **10** | 11 | **Yes (Tied)** |
| Student 12 | 445 | **10** | **10** | 12 | **Yes (Tied)** |
| Student 13 | 440 | **13** | 11 | 13 | **No (Excluded)** |

*Result:* Exactly 12 students are returned, satisfying the condition that all students tied for the final spot are included.

#### 3. RUET Exam Insights & Examiner Notes
- **Syllabus Positioning:** Advanced SQL ranking functions belong to Unit 4 and modern relational database practice.
- **Examiner Tip on Where Clause:** Window functions cannot appear directly in a `WHERE` clause (e.g., `WHERE RANK() OVER (...) <= 10` is illegal syntax) because window functions are evaluated *after* `WHERE`, `GROUP BY`, and `HAVING` stages in the SQL conceptual query lifecycle. A CTE or derived table is mandatory.

---

### Exercise 5.9 · Time-Series Ranking of NYSE Trading Days

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Practice Exercise 5.9, Page 235.
> - **Subtopic:** `T05.5` (Window ranking & analytical processing).
> - **Primary Schema:** `nyse(year, month, day, shares_traded, dollar_volume)`.
> - **Target Competency:** Window ordering vs. query output ordering, full-table ranking.

**Question (Silberschatz 7e Exercise 5.9).**  
Given a relation `nyse(year, month, day, shares_traded, dollar_volume)` with trading data from the New York Stock Exchange, list each trading day in order of number of shares traded, and show each day’s rank.

#### 1. Core Principles & Concept Overview

##### Window Ordering vs. Presentation Ordering
In SQL analytical queries, the `ORDER BY` clause appears in two distinct contexts:
1. **Inside the `OVER (...)` Clause:** Determines the ordering of rows for the purpose of computing the mathematical rank.
2. **At the Query Root:** Determines the final physical sorting order of tuples displayed to the user.
Because SQL relations are mathematically unordered multisets, the presence of an `OVER (ORDER BY ...)` does *not* guarantee that the outer result set will be sorted unless an explicit top-level `ORDER BY` clause is appended.

#### 2. Detailed Step-by-Step Solution

##### SQL Query
```sql
SELECT year,
       month,
       day,
       shares_traded,
       dollar_volume,
       RANK() OVER (ORDER BY shares_traded DESC) AS trading_rank
FROM nyse
ORDER BY shares_traded DESC;
```

##### Query Execution Lifecycle
1. **`FROM nyse`**: Reads the relation.
2. **`SELECT ... RANK() OVER (ORDER BY shares_traded DESC)`**:
   - Treats the entire relation as a single window partition (since `PARTITION BY` is omitted).
   - Sorts rows internally by `shares_traded` in descending order.
   - Computes `RANK()`: the highest volume day gets rank 1. Tied days receive equal rank.
3. **`ORDER BY shares_traded DESC`**: Sorts the final output stream so that day rank 1 appears on row 1, rank 2 follows, and so on.

#### 3. RUET Exam Insights & Examiner Notes
- **Exam Precision:** Always write the outer `ORDER BY shares_traded DESC`. RUET examiners deduct marks if a student assumes that `RANK() OVER (ORDER BY ...)` automatically guarantees sorted output presentation.

---

### Exercise 5.10 · Multidimensional Hierarchical Aggregation with `ROLLUP` (Year, Month, Day)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Practice Exercise 5.10, Page 235.
> - **Subtopic:** `T05.5` (Multidimensional OLAP, data cubes, and `ROLLUP`).
> - **Primary Schema:** `nyse(year, month, day, shares_traded, dollar_volume)`.
> - **Target Competency:** Hierarchical summarization, subtotals, grand totals, and super-aggregate representation using NULLs.

**Question (Silberschatz 7e Exercise 5.10).**  
Using the relation from Exercise 5.9, write an SQL query to generate a report showing the number of shares traded, number of trades, and total dollar volume broken down by year, each month of each year, and each trading day.

#### 1. Core Principles & Concept Overview

##### Hierarchical Multidimensional Aggregation
Financial and enterprise reporting requires summarization at multiple levels of granularity:
1. Detailed daily activity.
2. Monthly subtotal across all days in that month.
3. Yearly subtotal across all months in that year.
4. Overall grand total across all years recorded.

##### The SQL `ROLLUP` Construct
`ROLLUP (A, B, C)` generates $n + 1 = 3 + 1 = 4$ levels of aggregation by progressively rolling up attributes from right to left:
1. `(A, B, C)`: Full detail.
2. `(A, B)`: Subtotal across $C$ (where $C$ is represented as `NULL`).
3. `(A)`: Subtotal across $B$ and $C$ (where $B$ and $C$ are `NULL`).
4. `()`: Grand total across all attributes (where $A, B, C$ are all `NULL`).

#### 2. Detailed Step-by-Step Solution

##### Standard SQL Query using `ROLLUP`
```sql
SELECT year,
       month,
       day,
       SUM(shares_traded) AS total_shares_traded,
       COUNT(*) AS number_of_trading_records,
       SUM(dollar_volume) AS total_dollar_volume
FROM nyse
GROUP BY ROLLUP (year, month, day);
```

##### Equivalent Explicit Formulation via `GROUPING SETS`
```sql
SELECT year,
       month,
       day,
       SUM(shares_traded) AS total_shares_traded,
       COUNT(*) AS number_of_trading_records,
       SUM(dollar_volume) AS total_dollar_volume
FROM nyse
GROUP BY GROUPING SETS (
    (year, month, day),  -- Level 1: Daily records
    (year, month),       -- Level 2: Monthly subtotal
    (year),              -- Level 3: Annual subtotal
    ()                   -- Level 4: Grand total across all years
);
```

##### Structure of Output Report

| `year` | `month` | `day` | `total_shares_traded` | `number_of_trading_records` | `total_dollar_volume` | Semantic Meaning |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 2023 | 01 | 03 | 1,200,000 | 1 | \$45,000,000 | Specific Trading Day |
| 2023 | 01 | 04 | 1,150,000 | 1 | \$43,500,000 | Specific Trading Day |
| ... | ... | ... | ... | ... | ... | ... |
| **2023** | **01** | `NULL` | **25,000,000** | **21** | **\$950,000,000** | **January 2023 Monthly Subtotal** |
| ... | ... | ... | ... | ... | ... | ... |
| **2023** | `NULL` | `NULL` | **310,000,000** | **252** | **\$11,800,000,000** | **2023 Annual Subtotal** |
| **`NULL`** | **`NULL`** | **`NULL`** | **950,000,000** | **756** | **\$36,200,000,000** | **Grand Total (All Years)** |

> [!tip] Beautifying Reports with the `GROUPING()` Function
> In production reporting, raw `NULL` values in subtotal rows are replaced with descriptive text using `GROUPING()`:
> ```sql
> SELECT CASE WHEN GROUPING(year) = 1 THEN 'All Years (Grand Total)' ELSE CAST(year AS CHAR) END AS report_year,
>        CASE WHEN GROUPING(month) = 1 THEN 'All Months' ELSE CAST(month AS CHAR) END AS report_month,
>        CASE WHEN GROUPING(day) = 1 THEN 'All Days' ELSE CAST(day AS CHAR) END AS report_day,
>        SUM(shares_traded) AS total_shares_traded,
>        SUM(dollar_volume) AS total_dollar_volume
> FROM nyse
> GROUP BY ROLLUP (year, month, day);
> ```

#### 3. RUET Exam Insights & Examiner Notes
- **Syllabus Mapping:** Unit 8 (Advanced DBMS, Data Warehousing, and OLAP).
- **Examiner's Favorite Comparison:** RUET examiners frequently ask students to compare `ROLLUP` against `CUBE`. Remember: For $n$ attributes, `ROLLUP` produces $n + 1$ groupings, whereas `CUBE` produces $2^n$ groupings.

---

### Exercise 5.11 · Simulating Multidimensional `CUBE` via Single `ROLLUP` Expression

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 05 (*Advanced SQL*), Practice Exercise 5.11, Page 235.
> - **Subtopic:** `T05.5` (OLAP algebra, data cubes, and multidimensional aggregation).
> - **Primary Schema:** Conceptual relation $R(a, b, c, d)$.
> - **Target Competency:** Cartesian product of grouping sets, algebraic reduction of OLAP clauses.

**Question (Silberschatz 7e Exercise 5.11).**  
Show how to express `group by cube(a, b, c, d)` using `rollup`; your answer should have only one **group by** clause.

#### 1. Core Principles & Concept Overview

##### Mathematical Definitions of OLAP Grouping Operators
Let $S = \{a, b, c, d\}$ be a set of four attributes.
1. **The `CUBE` Operator:**  
   `CUBE(a, b, c, d)` generates the entire **power set** $\mathcal{P}(S)$, consisting of all $2^4 = 16$ possible subsets of groupings:
   $$
   |\text{CUBE}(a, b, c, d)| = 2^4 = 16 \text{ grouping sets}
   $$
2. **The `ROLLUP` Operator:**  
   `ROLLUP(x_1, x_2, \dots, x_k)` generates only the $k + 1$ hierarchical prefix groupings:
   $$
   \{(x_1, x_2, \dots, x_k), (x_1, x_2, \dots, x_{k-1}), \dots, (x_1), () \}
   $$
   In particular, for a **single attribute** $x$:
   $$
   \text{ROLLUP}(x) = \{ (x), () \} \quad (2 \text{ grouping sets: the attribute itself, and the grand total})
   $$

##### The Cartesian Product Rule of SQL Grouping Sets
The SQL:1999 standard defines that when multiple grouping operators are concatenated with commas in a single `GROUP BY` clause:
$$
\text{GROUP BY } G_1, G_2, \dots, G_m
$$
the database engine computes the **Cartesian product (cross product)** of the grouping sets generated by each individual operator:
$$
\text{Grouping Sets} = G_1 \times G_2 \times \dots \times G_m
$$

#### 2. Detailed Step-by-Step Solution

##### The Solution Clause
To express `GROUP BY CUBE(a, b, c, d)` using only `ROLLUP` within a single `GROUP BY` clause:

```sql
GROUP BY ROLLUP(a), ROLLUP(b), ROLLUP(c), ROLLUP(d)
```

##### Formal Algebraic Proof of Equivalence
Let each single-column rollup be denoted as:
$$
\mathcal{R}(a) = \text{ROLLUP}(a) = \{ \{a\}, \emptyset \}
$$
$$
\mathcal{R}(b) = \text{ROLLUP}(b) = \{ \{b\}, \emptyset \}
$$
$$
\mathcal{R}(c) = \text{ROLLUP}(c) = \{ \{c\}, \emptyset \}
$$
$$
\mathcal{R}(d) = \text{ROLLUP}(d) = \{ \{d\}, \emptyset \}
$$
The Cartesian product of these four sets is:
$$
\mathcal{R}(a) \times \mathcal{R}(b) \times \mathcal{R}(c) \times \mathcal{R}(d) = \{ \{a\}, \emptyset \} \times \{ \{b\}, \emptyset \} \times \{ \{c\}, \emptyset \} \times \{ \{d\}, \emptyset \}
$$
Evaluating the product term by term:
- From $\mathcal{R}(a)$, we can select either $\{a\}$ or $\emptyset$ ($2$ choices).
- From $\mathcal{R}(b)$, we can select either $\{b\}$ or $\emptyset$ ($2$ choices).
- From $\mathcal{R}(c)$, we can select either $\{c\}$ or $\emptyset$ ($2$ choices).
- From $\mathcal{R}(d)$, we can select either $\{d\}$ or $\emptyset$ ($2$ choices).

Total resulting grouping sets:
$$
2 \times 2 \times 2 \times 2 = 16 \text{ distinct grouping sets}
$$

##### Enumeration of All 16 Generated Grouping Sets
1. **Subset of size 4 ($1$ set):**
   - $(a, b, c, d)$
2. **Subsets of size 3 ($4$ sets):**
   - $(a, b, c)$
   - $(a, b, d)$
   - $(a, c, d)$
   - $(b, c, d)$
3. **Subsets of size 2 ($6$ sets):**
   - $(a, b)$
   - $(a, c)$
   - $(a, d)$
   - $(b, c)$
   - $(b, d)$
   - $(c, d)$
4. **Subsets of size 1 ($4$ sets):**
   - $(a)$
   - $(b)$
   - $(c)$
   - $(d)$
5. **Subset of size 0 ($1$ set):**
   - $()$ (Grand Total)

Because this collection is precisely the power set $\mathcal{P}(\{a, b, c, d\})$, it is strictly and identically equivalent to `CUBE(a, b, c, d)`.

> [!warning] Common Student Mistakes
> - **Attempting to concatenate in one rollup:** Writing `GROUP BY ROLLUP(a, b, c, d)` only produces $4 + 1 = 5$ grouping sets (`(a,b,c,d)`, `(a,b,c)`, `(a,b)`, `(a)`, `()`), completely missing the other 11 combinations like `(b, c)` or `(d)`.
> - **Using `UNION ALL`:** Writing 16 separate `SELECT ... GROUP BY` queries connected via `UNION ALL` produces the right data but **violates the explicit question constraint** specifying *"your answer should have only one group by clause"*.

#### 3. RUET Exam Insights & Examiner Notes
- **Theoretical Elegance:** This exercise tests whether a student understands the algebraic foundations of SQL's query processor. RUET external examiners from BUET/RUET frequently select this exact question for high-mark conceptual testing.
- **Examiner Scoring Key:** An answer that provides the one-line clause `GROUP BY ROLLUP(a), ROLLUP(b), ROLLUP(c), ROLLUP(d)` accompanied by the Cartesian product cardinality calculation ($2 \times 2 \times 2 \times 2 = 16 = 2^4$) earns $100\%$ marks immediately.


---

[← Prev: T05 Part 1](T05_Part1_SQL_DDL_DML_Basics.md) | [Index](00_Index.md) | [Next: T05 Part 3 →](T05_Part3_SQL_Aggregations_and_Subqueries.md)
