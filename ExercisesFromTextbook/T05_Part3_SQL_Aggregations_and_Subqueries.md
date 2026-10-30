---
title: "T05 (Part 3) · SQL: Advanced Aggregations, Extremes & Subqueries"
tags: [ece2215, database-systems, silberschatz-exercises, topic-T05]
topic_id: T05
part: 3
exercise_count: 10
source_chapters: ["Chapter 03", "Chapter 05"]
---

[← Prev: T05 Part 2](T05_Part2_SQL_Clauses_and_Aggregations.md) | [Exam-style T05](../Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T05 Part 4 →](T05_Part4_SQL_MultiTable_Business_Queries.md)

# T05 (Part 3) · SQL: Advanced Aggregations, Extremes & Subqueries

> [!abstract] Topic Overview & Learning Goals
> This practice module covers advanced SQL queries from Silberschatz Chapters 3 and 5. It concentrates on two high-frequency exam areas:
> 1. **Advanced Aggregations & Extremes (Subtopic T05.5)**: Finding extreme values without vendor-specific keywords like `LIMIT` or `TOP`, computing statistical histograms with `NTILE`, calculating moving averages with window frames, and generating multidimensional subtotals with `GROUP BY ROLLUP`.
> 2. **Subqueries & Set Comparisons (Subtopic T05.6)**: Formally proving equivalence of set operators under three-valued logic, applying `NOT IN` versus `NOT EXISTS`, writing correlated subqueries, computing transitive closures iteratively in Java JDBC with cycle detection, and writing recursive Common Table Expressions (`WITH RECURSIVE`).

---

## Exercise Directory & Mapping

| Exercise | Source | Subtopic | Question Type | Focus / Techniques | RUET Relevance |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **Exercise 3.35** | Ch. 03 (Ex 3.35) | T05.5 | Query Writing | Maximum enrollment, `WITH` CTE, avoiding `LIMIT` | Very High (2018 Q7b, 2019 Q7a) |
| **Exercise 5.22** | Ch. 05 (Ex 5.22) | T05.5 | OLAP Query | Equal-width histogram, `NTILE(20)` window function | Medium (Modern SQL:2003 OLAP) |
| **Exercise 5.23** | Ch. 05 (Ex 5.23) | T05.5 | OLAP Query | 3-month moving average, window frames, derived table | High (Windowing theory) |
| **Exercise 5.24** | Ch. 05 (Ex 5.24) | T05.5 | Result Evaluation | `GROUP BY ROLLUP`, hierarchical subtotals & grand total | High (2019 Q8a, OLAP aggregation) |
| **Exercise 3.20** | Ch. 03 (Ex 3.20) | T05.6 | Formal Proof | `<> ALL` identical to `NOT IN`, three-valued logic | Very High (2019 Q8b, 2024 Q6a) |
| **Exercise 3.31** | Ch. 03 (Ex 3.31) | T05.6 | Query Writing | Instructors never giving 'A', `NOT IN` vs `NOT EXISTS` | Very High (2023 Q3a, CT-02 Q1) |
| **Exercise 3.32** | Ch. 03 (Ex 3.32) | T05.6 | Query Writing | Instructors never giving 'A' with other non-null grades | High (Subquery composition) |
| **Exercise 3.33** | Ch. 03 (Ex 3.33) | T05.6 | Query Writing | Comp Sci afternoon courses, `IN` vs `JOIN DISTINCT` | High (Multi-table subqueries) |
| **Practice Ex 5.3**| Ch. 05 (PE 5.3) | T05.6 | Java / JDBC Code | Transitive closure of prerequisites, cycle prevention | Medium-High (Application-level SQL) |
| **Exercise 5.21** | Ch. 05 (Ex 5.21) | T05.6 | Recursive SQL | Prerequisite depth tracking, `WITH RECURSIVE` CTE | High (Advanced recursive queries) |

---

## T05.5 · Advanced Aggregations, Extremes & OLAP

This section addresses aggregate processing beyond basic `GROUP BY` and `HAVING` filters. It focuses on finding extreme values without non-standard SQL keywords, generating equi-depth histogram partitions, calculating rolling temporal averages, and computing hierarchical aggregations using `ROLLUP`.

---

### Exercise 3.35 · Finding Section(s) with Maximum Enrollment

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 3 (*Introduction to SQL*), Regular Exercise 3.35, Page 123.
> - **Subtopic:** T05.5 (Aggregations, Extremes without `LIMIT`).
> - **Target Database:** Standard ANSI SQL:1999 / SQL:2003.
> - **RUET Exam Alignment:** Very High. Exam papers regularly test extreme value queries without `LIMIT` (e.g., 2018 Q.7b, 2019 Q.7a).

**Question (Silberschatz 7e Exercise 3.35).**
Using the university schema, write an SQL query to find section(s) with maximum enrollment. The result columns should appear in the order “courseid, secid, year, semester, num”. (It may be convenient to use the `with` construct.)

#### 1. Core Principles & Concept Overview

The task requires finding the section or sections that contain the greatest number of enrolled students. Two database relations from the university schema are relevant:
- `section(course_id, sec_id, semester, year, building, room_number, time_slot_id)`
- `takes(ID, course_id, sec_id, semester, year, grade)`

The student count for each section comes from counting student IDs in `takes`:

$$
num = \text{count}(ID)
$$

The primary key of `section` is $(course\_id, sec\_id, semester, year)$. Therefore, any aggregation grouping by section must group by all four attributes.

A critical design challenge in relational database exams is handling ties. Multiple sections may share the identical maximum enrollment number. Vendor-specific clauses like `LIMIT 1` (PostgreSQL, MySQL) or `SELECT TOP 1` (SQL Server) return only a single arbitrary row during a tie. In standard database theory and RUET examinations, using `LIMIT` is forbidden. The query must return all sections tied for first place.

The standard solution uses a two-step process:
1. Compute the enrollment count for every section using aggregation and store it in a Common Table Expression (CTE) via the `with` clause.
2. Select all records from this CTE whose count equals the scalar maximum count or is greater than or equal to all counts.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Compute Section Enrollments via CTE
First, create a temporary view `section_enrollment` using the `with` clause. Group `takes` by the four section identifying attributes and compute `count(ID)`.

```sql
with section_enrollment (course_id, sec_id, year, semester, num) as (
    select course_id, sec_id, year, semester, count(ID)
    from takes
    group by course_id, sec_id, year, semester
)
```

##### Step 2: Filter for the Maximum Value
We present two standard methods to filter for the maximum enrollment.

###### Method A: Using a Scalar Subquery (`MAX`)
Compare the enrollment count `num` of each section with the scalar maximum produced by `select max(num) from section_enrollment`.

```sql
with section_enrollment (course_id, sec_id, year, semester, num) as (
    select course_id, sec_id, year, semester, count(ID) as num
    from takes
    group by course_id, sec_id, year, semester
)
select course_id, sec_id, year, semester, num
from section_enrollment
where num = (
    select max(num)
    from section_enrollment
);
```

###### Method B: Using Set Comparison (`>= ALL`)
Compare each section's count against every count in the temporary relation using the `>= all` operator:

```sql
with section_enrollment (course_id, sec_id, year, semester, num) as (
    select course_id, sec_id, year, semester, count(ID) as num
    from takes
    group by course_id, sec_id, year, semester
)
select course_id, sec_id, year, semester, num
from section_enrollment
where num >= all (
    select num
    from section_enrollment
);
```

Both methods are standard SQL. If three sections tie with an enrollment of 45 students, both queries return all three rows.

##### Step 3: Handling Sections with Zero Students
The textbook notes in Exercise 3.34: *"You do not need to output sections with 0 students."* However, if all sections in an empty semester have 0 students, an outer join preserves completeness:

```sql
with section_enrollment (course_id, sec_id, year, semester, num) as (
    select s.course_id, s.sec_id, s.year, s.semester, count(t.ID) as num
    from section s
    left outer join takes t
      on s.course_id = t.course_id
     and s.sec_id = t.sec_id
     and s.year = t.year
     and s.semester = t.semester
    group by s.course_id, s.sec_id, s.year, s.semester
)
select course_id, sec_id, year, semester, num
from section_enrollment
where num = (
    select max(num)
    from section_enrollment
);
```

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Examiner Warning: The `LIMIT` Prohibition
> RUET examiners deduct up to 100% of marks if you write `ORDER BY count(*) DESC LIMIT 1`. The RUET syllabus evaluates formal ANSI SQL. Always use `where num = (select max(num)...)` or `having count(*) >= all (...)`.
>
> Also check the projection attribute order requested in the question:
> `courseid, secid, year, semester, num`
> Notice that `year` is placed before `semester` in the problem statement. Always match the exact column order requested.

---

### Exercise 5.22 · Histogram Generation using NTILE Window Function

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Regular Exercise 5.22, Page 237.
> - **Subtopic:** T05.5 (OLAP Aggregations, Window Functions).
> - **Target Database:** Standard ANSI SQL:2003 / PostgreSQL / Oracle / SQL Server.
> - **RUET Exam Alignment:** Medium. Introduces modern OLAP windowing functions that appear in advanced database questions.

**Question (Silberschatz 7e Exercise 5.22).**
Given relation $s(a, b, c)$, write an SQL statement to generate a histogram showing the sum of $c$ values versus $a$, dividing $a$ into 20 equal-sized partitions (i.e., where each partition contains 5 percent of the tuples in $s$, sorted by $a$).

#### 1. Core Principles & Concept Overview

Histograms approximate data distributions in database query optimizers and data analytics. There are two primary types of histograms:
1. **Equi-width histograms**: Divide the value range $[a_{min}, a_{max}]$ into intervals of identical width.
2. **Equi-depth (equi-count) histograms**: Divide the sorted tuples into partitions containing identical numbers of tuples.

This exercise asks for an equi-depth histogram dividing $s$ into 20 partitions. Each partition holds $5\%$ of the total rows ($100\% / 20 = 5\%$).

SQL:2003 introduced the `ntile(n)` window function specifically for this purpose. The function:
- Sorts rows based on an `order by` clause.
- Distributes rows evenly into $n$ numbered buckets, from $1$ to $n$.
- Assigns bucket 1 to the first $5\%$ of rows, bucket 2 to the next $5\%$, through bucket 20.

Because window functions execute after the `WHERE` and `GROUP BY` phases of a query, assigning bucket numbers requires a subquery or CTE. A subsequent outer query then aggregates each bucket.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Assign Rows to 20 Buckets via `NTILE`
Use a CTE named `partitioned_s` to attach a bucket index from 1 to 20 to each row, ordered by attribute $a$:

```sql
with partitioned_s as (
    select a, b, c,
           ntile(20) over (order by a) as bucket
    from s
)
```

##### Step 2: Aggregate by Bucket in the Outer Query
Group the tuples by `bucket`. For each bucket, compute the boundary values of $a$ and the sum of attribute $c$:

```sql
with partitioned_s as (
    select a, b, c,
           ntile(20) over (order by a) as bucket
    from s
)
select bucket,
       min(a) as a_range_start,
       max(a) as a_range_end,
       sum(c) as sum_c
from partitioned_s
group by bucket
order by bucket;
```

##### Step 3: Mathematical Behavior with Non-Divisible Counts
Suppose relation $s$ contains $N$ rows, and $N$ is not divisible by 20. Let:

$$
N = 20 \cdot q + r \quad (0 \le r < 20)
$$

The SQL standard specifies that each of the first $r$ buckets receives $q + 1$ rows. The remaining $20 - r$ buckets receive $q$ rows. This guarantees that all rows are assigned and partition sizes differ by at most one row.

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Analytical Window Functions vs Group Aggregations
> Students often make the mistake of placing `ntile(20)` directly inside the `group by` clause:
> ```sql
> -- SYNTAX ERROR IN SQL
> select ntile(20) over (order by a), sum(c)
> from s
> group by ntile(20) over (order by a);
> ```
> Window functions cannot appear directly in `GROUP BY` or `WHERE` clauses. You must use a CTE or a derived subquery in the `FROM` clause first, then aggregate the resulting bucket index in the outer query.

---

### Exercise 5.23 · Moving Average of Monthly Dollar Volume

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Regular Exercise 5.23, Page 237.
> - **Subtopic:** T05.5 (Windowing, Moving Aggregates).
> - **Target Database:** Standard ANSI SQL:2003 / PostgreSQL / Oracle / MySQL 8.0+.
> - **RUET Exam Alignment:** High. Windowing questions evaluate understanding of analytic frames and derived subqueries.

**Question (Silberschatz 7e Exercise 5.23).**
Consider the *nyse* relation of Exercise 5.9. For each month of each year, show the total monthly dollar volume and the average monthly dollar volume for that month and the two prior months. (*Hint*: First write a query to find the total dollar volume for each month of each year. Once that is right, put that in the **from** clause of the outer query that solves the full problem. That outer query will need windowing. The subquery does not.)

#### 1. Core Principles & Concept Overview

The schema of the New York Stock Exchange relation is:

$$
nyse(\underline{year}, \underline{month}, \underline{day}, shares\_traded, dollar\_volume)
$$

The query requires computing two metrics:
1. Total monthly dollar volume for each year and month.
2. A three-month moving average covering the current month and the two preceding months.

This problem requires two tiers of aggregation:
- An inner aggregation to group daily trading data into monthly totals using `GROUP BY year, month`.
- An outer window function to calculate the rolling three-month mean over those monthly totals.

SQL window frames specify the subset of rows around the current row over which the analytic aggregate operates. The physical frame specification is:

$$
\text{ROWS BETWEEN 2 PRECEDING AND CURRENT ROW}
$$

This frame includes at most 3 rows: the row two steps back, the row one step back, and the current row.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Compute Monthly Total Volume (Subquery)
Group the daily records by `year` and `month`, summing `dollar_volume`:

```sql
select year, month, sum(dollar_volume) as monthly_volume
from nyse
group by year, month;
```

##### Step 2: Apply the Moving Average Window Function (Full Solution)
Following the hint in the exercise, place the monthly aggregation into the `from` clause of the outer query. In the outer `select`, apply `avg()` with the window frame specification:

```sql
select year,
       month,
       monthly_volume,
       avg(monthly_volume) over (
           order by year, month
           rows between 2 preceding and current row
       ) as moving_avg_volume
from (
    select year, month, sum(dollar_volume) as monthly_volume
    from nyse
    group by year, month
) as monthly_nyse
order by year, month;
```

##### Step 3: Alternative CTE Formulation
The query can also be expressed clearly using a `with` clause:

```sql
with monthly_nyse as (
    select year, month, sum(dollar_volume) as monthly_volume
    from nyse
    group by year, month
)
select year,
       month,
       monthly_volume,
       avg(monthly_volume) over (
           order by year, month
           rows between 2 preceding and current row
       ) as moving_avg_volume
from monthly_nyse
order by year, month;
```

##### Step 4: Window Boundary Trace
Consider the first three months of trading data:
- **Month 1 (e.g., 2020-01):** The frame has only 1 row (current row). The moving average equals the volume of Month 1.
- **Month 2 (e.g., 2020-02):** The frame has 2 rows (Month 1 and Month 2). The average is:
  $$
  \frac{\text{vol}_1 + \text{vol}_2}{2}
  $$
- **Month 3 (e.g., 2020-03):** The frame has 3 rows (Month 1, Month 2, Month 3). The average is:
  $$
  \frac{\text{vol}_1 + \text{vol}_2 + \text{vol}_3}{3}
  $$
- **Month 4 onward:** The window shifts forward, always averaging exactly 3 consecutive monthly sums.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Frame Type: `ROWS` vs `RANGE`
> When defining sliding window averages:
> - `ROWS BETWEEN ...` specifies physical row offsets.
> - `RANGE BETWEEN ...` specifies value intervals based on the ordering attribute.
>
> If months are guaranteed contiguous, `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` is the most straightforward and universally supported syntax.
> Also note that nesting aggregate functions directly like `avg(sum(dollar_volume))` in a single query block causes a syntax error. The subquery structure isolates the two aggregation steps properly.

---

### Exercise 5.24 · Hierarchical Aggregation with GROUP BY ROLLUP

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Regular Exercise 5.24, Page 237.
> - **Subtopic:** T05.5 (OLAP Aggregations, `ROLLUP`).
> - **Target Database:** Standard ANSI SQL:1999 / PostgreSQL / Oracle / DB2.
> - **RUET Exam Alignment:** High. RUET 2019 Q.8a specifically asked for short notes on `ROLLUP` and `CUBE`.

**Question (Silberschatz 7e Exercise 5.24).**
Consider the relation, $r$, shown in Figure 5.22. Give the result of the following query:

```sql
select building, room_number, time_slot_id, count(*)
from r
group by rollup (building, room_number, time_slot_id)
```

#### 1. Core Principles & Concept Overview

Figure 5.22 in Silberschatz 7e provides the relation instance $r$:

| building | room_number | time_slot_id | course_id | sec_id |
| :--- | :--- | :--- | :--- | :--- |
| Garfield | 359 | A | BIO-101 | 1 |
| Garfield | 359 | B | BIO-101 | 2 |
| Saucon | 651 | A | CS-101 | 2 |
| Saucon | 550 | C | CS-319 | 1 |
| Painter | 705 | D | MU-199 | 1 |
| Painter | 403 | D | FIN-201 | 1 |

The query uses `group by rollup (building, room_number, time_slot_id)`.

In OLAP operations, `ROLLUP` generates hierarchical subtotals along a specified attribute list $(A_1, A_2, \dots, A_n)$. For $n$ attributes, `ROLLUP` produces $n + 1$ grouping sets by progressively dropping attributes from right to left:
1. $(A_1, A_2, A_3)$ : Full detailed grouping.
2. $(A_1, A_2)$ : Subtotals per $(A_1, A_2)$, setting $A_3$ to `NULL`.
3. $(A_1)$ : Subtotals per $A_1$, setting $A_2$ and $A_3$ to `NULL`.
4. $()$ : Grand total over the whole table, setting all attributes to `NULL`.

For three attributes $(building, room\_number, time\_slot\_id)$, $n = 3$, so there are $3 + 1 = 4$ grouping sets.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Compute Level 3 · Grouping on `(building, room_number, time_slot_id)`
All six tuples in $r$ have distinct combinations of $(building, room\_number, time\_slot\_id)$. Each tuple forms its own group with `count(*) = 1`:
- `(Garfield, 359, A)` $\rightarrow 1$
- `(Garfield, 359, B)` $\rightarrow 1$
- `(Saucon, 651, A)` $\rightarrow 1$
- `(Saucon, 550, C)` $\rightarrow 1$
- `(Painter, 705, D)` $\rightarrow 1$
- `(Painter, 403, D)` $\rightarrow 1$
Total: 6 rows.

##### Step 2: Compute Level 2 · Subtotals on `(building, room_number)`
Here `time_slot_id` is replaced by `null`:
- `(Garfield, 359, null)`: Has 2 tuples (slots A and B) $\rightarrow 2$
- `(Saucon, 651, null)`: Has 1 tuple (slot A) $\rightarrow 1$
- `(Saucon, 550, null)`: Has 1 tuple (slot C) $\rightarrow 1$
- `(Painter, 705, null)`: Has 1 tuple (slot D) $\rightarrow 1$
- `(Painter, 403, null)`: Has 1 tuple (slot D) $\rightarrow 1$
Total: 5 rows.

##### Step 3: Compute Level 1 · Subtotals on `(building)`
Here both `room_number` and `time_slot_id` are replaced by `null`:
- `(Garfield, null, null)`: Total tuples in Garfield $= 2$
- `(Saucon, null, null)`: Total tuples in Saucon $= 2$
- `(Painter, null, null)`: Total tuples in Painter $= 2$
Total: 3 rows.

##### Step 4: Compute Level 0 · Grand Total on `()`
All three attributes are `null`:
- `(null, null, null)`: Total tuples in relation $r = 6$
Total: 1 row.

##### Complete Query Result Table
Summing all grouping sets gives $6 + 5 + 3 + 1 = 15$ result rows:

| building | room_number | time_slot_id | count(*) | Level / Grouping Semantics |
| :--- | :--- | :--- | :---: | :--- |
| Garfield | 359 | A | 1 | Base group |
| Garfield | 359 | B | 1 | Base group |
| Garfield | 359 | *null* | 2 | Subtotal: Garfield, Room 359 |
| Garfield | *null* | *null* | 2 | Subtotal: Garfield building |
| Painter | 403 | D | 1 | Base group |
| Painter | 403 | *null* | 1 | Subtotal: Painter, Room 403 |
| Painter | 705 | D | 1 | Base group |
| Painter | 705 | *null* | 1 | Subtotal: Painter, Room 705 |
| Painter | *null* | *null* | 2 | Subtotal: Painter building |
| Saucon | 550 | C | 1 | Base group |
| Saucon | 550 | *null* | 1 | Subtotal: Saucon, Room 550 |
| Saucon | 651 | A | 1 | Base group |
| Saucon | 651 | *null* | 1 | Subtotal: Saucon, Room 651 |
| Saucon | *null* | *null* | 2 | Subtotal: Saucon building |
| *null* | *null* | *null* | 6 | Grand total across all buildings |

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Technique: ROLLUP vs CUBE
> If this question used `CUBE (building, room_number, time_slot_id)`, it would produce $2^3 = 8$ grouping sets (including combinations like `(room_number, time_slot_id)` without building).
>
> In contrast, `ROLLUP` assumes a hierarchy:
> $$
> \text{building} \longrightarrow \text{room\_number} \longrightarrow \text{time\_slot\_id}
> $$
> It only drops attributes from the right. When tracing `ROLLUP` on an exam script, write the subtotal levels clearly and explicitly mark aggregated positions as `NULL`.

---

## T05.6 · Subqueries, Set Comparisons & Recursive CTEs

Subqueries provide declarative nesting inside SQL expressions. This section covers formal set comparisons (`<> ALL` versus `NOT IN`), existential conditions (`EXISTS` and `NOT EXISTS`), correlated subqueries, application-level iterative fixed-point algorithms in Java JDBC, and recursive CTEs using `WITH RECURSIVE`.

---

### Exercise 3.20 · Equivalence of `<> ALL` and `NOT IN`

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 3 (*Introduction to SQL*), Regular Exercise 3.20, Page 121.
> - **Subtopic:** T05.6 (Set Comparisons, Subquery Theory).
> - **Target Database:** Standard ANSI SQL (Three-Valued Logic).
> - **RUET Exam Alignment:** Very High. Formal comparisons between `SOME`, `ALL`, and `IN` are frequently tested in semester finals (e.g., 2019 Q.8b, 2024 Q.6a).

**Question (Silberschatz 7e Exercise 3.20).**
Show that, in SQL, `<> all` is identical to `not in`.

#### 1. Core Principles & Concept Overview

Let $v$ be a scalar value or tuple, and let $S$ be a multiset produced by a subquery:

$$
S = \{s_1, s_2, \dots, s_n\}
$$

The SQL standard defines the two constructs as follows:
1. **The `IN` construct**:
   The expression $v \text{ IN } S$ is shorthand for the disjunction:
   $$
   (v = s_1) \lor (v = s_2) \lor \dots \lor (v = s_n)
   $$
   Therefore, $v \text{ NOT IN } S$ is defined as the logical negation:
   $$
   \neg (v \text{ IN } S) \equiv \neg \big((v = s_1) \lor (v = s_2) \lor \dots \lor (v = s_n)\big)
   $$
   By De Morgan's laws:
   $$
   v \text{ NOT IN } S \equiv (v \neq s_1) \land (v \neq s_2) \land \dots \land (v \neq s_n)
   $$

2. **The `<> ALL` construct**:
   The construct $v \text{ <comp> ALL } S$ evaluates to `true` if and only if $v \text{ <comp> } s_i$ evaluates to `true` for every element $s_i \in S$. Setting the comparison operator to `<>` (not equal):
   $$
   v \text{ <> ALL } S \equiv (v \neq s_1) \land (v \neq s_2) \land \dots \land (v \neq s_n)
   $$

At a purely syntactic level, both expressions expand into the identical conjunction of inequality tests. But SQL operates under Three-Valued Logic (3VL) with truth values $\{\text{true}, \text{false}, \text{unknown}\}$. We must prove that both constructs produce identical truth values under every possible database state.

#### 2. Detailed Step-by-Step Proof

We evaluate four exhaustive cases.

##### Case 1: Empty Subquery ($S = \emptyset$)
- **For `<> ALL`**: The condition $v \neq s_i$ must hold for all $s_i \in S$. Because no element exists in $S$, the condition is vacuously true. The result is `true`.
- **For `NOT IN`**: The expression $v \text{ IN } \emptyset$ is `false` (no element equals $v$). Therefore, $\neg(\text{false}) = \text{true}$.
- **Result**: Both evaluate to `true`.

##### Case 2: Non-Empty Set Without Nulls, $v \in S$
Assume $S = \{s_1, s_2, \dots, s_n\}$ where $s_i \neq \text{null}$ for all $i$, and $v = s_k$ for some index $k$.
- **For `<> ALL`**: The comparison $v \neq s_k$ evaluates to `false`. A conjunction containing at least one `false` evaluates to `false`.
- **For `NOT IN`**: The term $v = s_k$ is `true`. The disjunction $(v = s_1 \lor \dots \lor v = s_n)$ is `true`. The negation $\neg(\text{true})$ is `false`.
- **Result**: Both evaluate to `false`.

##### Case 3: Non-Empty Set Without Nulls, $v \notin S$
Assume $S = \{s_1, s_2, \dots, s_n\}$ where $s_i \neq \text{null}$ for all $i$, and $v \neq s_i$ for all $i$.
- **For `<> ALL`**: Every comparison $v \neq s_i$ evaluates to `true`. The conjunction of all `true` terms is `true`.
- **For `NOT IN`**: Every equality test $v = s_i$ evaluates to `false`. The disjunction is `false`. Its negation $\neg(\text{false})$ is `true`.
- **Result**: Both evaluate to `true`.

##### Case 4: Non-Empty Set Containing Null Values
Assume $S = \{s_1, \dots, s_{n-1}, \text{null}\}$.

###### Subcase 4a: $v = s_k$ for some non-null element $s_k$
- **For `<> ALL`**: The term $v \neq s_k$ is `false`. In 3VL, $\text{false} \land \text{unknown} = \text{false}$.
- **For `NOT IN`**: The term $v = s_k$ is `true`. In 3VL, $\text{true} \lor \text{unknown} = \text{true}$. Its negation $\neg(\text{true})$ is `false`.
- **Result**: Both evaluate to `false`.

###### Subcase 4b: $v \neq s_i$ for all non-null elements $s_i$
- **For `<> ALL`**: All non-null comparisons $v \neq s_i$ are `true`. But comparing $v \neq \text{null}$ evaluates to `unknown`. The conjunction is:
  $$
  \text{true} \land \text{true} \land \dots \land \text{unknown} = \text{unknown}
  $$
- **For `NOT IN`**: All non-null comparisons $v = s_i$ are `false`. But $v = \text{null}$ evaluates to `unknown`. The disjunction is:
  $$
  \text{false} \lor \text{false} \lor \dots \lor \text{unknown} = \text{unknown}
  $$
  Negating `unknown` yields:
  $$
  \neg(\text{unknown}) = \text{unknown}
  $$
- **Result**: Both evaluate to `unknown`.

##### Summary Truth Table
The following truth table summarizes the proof:

| Condition on $S$ | Relation of $v$ to $S$ | $v \text{ <> ALL } S$ | $v \text{ NOT IN } S$ | Match? |
| :--- | :--- | :---: | :---: | :---: |
| $S = \emptyset$ | Any value $v$ | `true` | `true` | Yes |
| $S$ has no nulls | $v \in S$ | `false` | `false` | Yes |
| $S$ has no nulls | $v \notin S$ | `true` | `true` | Yes |
| $S$ contains null | $v = s_k$ for non-null $s_k$ | `false` | `false` | Yes |
| $S$ contains null | $v \neq s_i$ for all non-null $s_i$ | `unknown` | `unknown` | Yes |

Because both expressions produce identical truth values in all cases, `<> ALL` is identical to `NOT IN` in SQL.

#### 3. RUET Exam Insights & Examiner Notes

> [!caution] The SQL Null Trap with `NOT IN` and `<> ALL`
> In RUET exams, questions frequently ask: *"What unexpected behavior happens when a subquery returns a null value?"*
> As proven in Subcase 4b, if a subquery returns even a single `null`, both `v NOT IN (subquery)` and `v <> ALL (subquery)` evaluate to `unknown` for all non-matching rows.
>
> In a `WHERE` clause, SQL filters out any row where the condition is `unknown`. As a result, the entire outer query returns **zero rows**!
> To avoid this bug in production and exam queries, always add `WHERE attribute IS NOT NULL` inside the subquery, or use `NOT EXISTS`.

---

### Exercise 3.31 · Finding Instructors Who Never Gave an 'A'

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 3 (*Introduction to SQL*), Regular Exercise 3.31, Page 123.
> - **Subtopic:** T05.6 (Nested Subqueries, Negation).
> - **Target Database:** Standard ANSI SQL.
> - **RUET Exam Alignment:** Very High. Negation queries testing `NOT IN` versus `NOT EXISTS` appear frequently (e.g., 2023 Q.3a, CT-02 Q.1c).

**Question (Silberschatz 7e Exercise 3.31).**
Using the university schema, write an SQL query to find the ID and name of each instructor who has never given an A grade in any course she or he has taught. (Instructors who have never taught a course trivially satisfy this condition.)

#### 1. Core Principles & Concept Overview

The university schema links instructors, their teaching assignments, and student grades:
- `instructor(ID, name, dept_name, salary)`
- `teaches(ID, course_id, sec_id, semester, year)`
- `takes(ID, course_id, sec_id, semester, year, grade)`

Notice that `takes.ID` is the student ID, whereas `teaches.ID` is the instructor ID.

The condition requires finding instructors who have *never* awarded an 'A' grade. This is a negative condition. In formal logic:

$$
\{i \in \text{instructor} \mid \neg \exists t \in \text{teaches}, k \in \text{takes} \ (t.\text{ID} = i.\text{ID} \land t.\text{section} = k.\text{section} \land k.\text{grade} = \text{'A'})\}
$$

A common error is writing:
```sql
-- INCORRECT QUERY
select distinct instructor.ID, name
from instructor, teaches, takes
where instructor.ID = teaches.ID
  and teaches.course_id = takes.course_id
  and takes.grade <> 'A';
```
This incorrect query returns any instructor who gave at least one grade that was not an 'A'. If an instructor taught two students and gave one 'A' and one 'B', this query includes that instructor because of the 'B'.

Also, the problem notes: *"Instructors who have never taught a course trivially satisfy this condition."* Because they have given 0 grades, they have never given an 'A'. An inner join would drop them. A negation against the positive condition preserves them.

#### 2. Detailed Step-by-Step Solution

##### Method 1: Set Difference via `NOT IN` (Recommended)
First, identify all instructor IDs who *have* awarded an 'A'. Then select all instructors whose ID is not in that set.

```sql
select ID, name
from instructor
where ID not in (
    select teaches.ID
    from teaches
    join takes
      on teaches.course_id = takes.course_id
     and teaches.sec_id = takes.sec_id
     and teaches.semester = takes.semester
     and teaches.year = takes.year
    where takes.grade = 'A'
);
```

If an instructor has never taught a course, their ID never appears in `teaches`. Thus their ID is not in the subquery result. The condition `ID NOT IN (...)` evaluates to `true`, and they are included in the output.

##### Method 2: Correlated Subquery with `NOT EXISTS`
Using `not exists` avoids null sensitivity:

```sql
select I.ID, I.name
from instructor I
where not exists (
    select 1
    from teaches T
    join takes TK
      on T.course_id = TK.course_id
     and T.sec_id = TK.sec_id
     and T.semester = TK.semester
     and T.year = TK.year
    where T.ID = I.ID
      and TK.grade = 'A'
);
```

For an instructor who never taught, the subquery returns an empty set. `not exists (empty)` evaluates to `true`.

##### Method 3: Set Difference via `EXCEPT`
Subtract instructors who gave an 'A' from the complete relation of instructors:

```sql
select ID, name
from instructor
except
select I.ID, I.name
from instructor I
join teaches T on I.ID = T.ID
join takes TK
  on T.course_id = TK.course_id
 and T.sec_id = TK.sec_id
 and T.semester = TK.semester
 and T.year = TK.year
where TK.grade = 'A';
```

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Best Strategy for Negative Conditions
> In RUET exam scripts, always formulate negative queries by identifying the **positive condition first** (here: instructors who *did* award an 'A'), and then applying `NOT IN`, `NOT EXISTS`, or `EXCEPT`.
>
> If the grading scheme includes 'A+' or 'A-', clarify your pattern:
> `where takes.grade = 'A' or takes.grade like 'A%'`
> Both forms are accepted by RUET examiners if written consistently.

---

### Exercise 3.32 · Instructors Never Giving 'A' with Non-Null Grades

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 3 (*Introduction to SQL*), Regular Exercise 3.32, Page 123.
> - **Subtopic:** T05.6 (Nested Subqueries, Conjunction of Constraints).
> - **Target Database:** Standard ANSI SQL.
> - **RUET Exam Alignment:** High. Follow-up modification questions test precise constraint composition.

**Question (Silberschatz 7e Exercise 3.32).**
Rewrite the preceding query, but also ensure that you include only instructors who have given at least one other non-null grade in some course.

#### 1. Core Principles & Concept Overview

This exercise adds an affirmative constraint to Exercise 3.31. The instructor must satisfy two simultaneous conditions:
1. **Negative Condition**: Must *never* have awarded an 'A' grade.
2. **Positive Condition**: Must have awarded *at least one non-null grade* (e.g., 'B', 'C', 'D', 'F') in some course taught.

This eliminates two categories of instructors who were previously included:
- Instructors who have never taught any course.
- Instructors who taught courses where all grades are `null` (such as courses currently in progress before final grading).

#### 2. Detailed Step-by-Step Solution

##### Method 1: Dual Subquery with `NOT IN` and `IN`
Combine the negative condition from Exercise 3.31 with an affirmative `IN` subquery that requires at least one non-null grade:

```sql
select ID, name
from instructor
where ID not in (
    select teaches.ID
    from teaches
    join takes
      on teaches.course_id = takes.course_id
     and teaches.sec_id = takes.sec_id
     and teaches.semester = takes.semester
     and teaches.year = takes.year
    where takes.grade = 'A'
)
and ID in (
    select teaches.ID
    from teaches
    join takes
      on teaches.course_id = takes.course_id
     and teaches.sec_id = takes.sec_id
     and teaches.semester = takes.semester
     and teaches.year = takes.year
    where takes.grade is not null
);
```

##### Method 2: Dual Correlated Subqueries with `NOT EXISTS` and `EXISTS`
Use `NOT EXISTS` for the negative check and `EXISTS` for the affirmative grade check:

```sql
select I.ID, I.name
from instructor I
where not exists (
    select 1
    from teaches T
    join takes TK
      on T.course_id = TK.course_id
     and T.sec_id = TK.sec_id
     and T.semester = TK.semester
     and T.year = TK.year
    where T.ID = I.ID
      and TK.grade = 'A'
)
and exists (
    select 1
    from teaches T
    join takes TK
      on T.course_id = TK.course_id
     and T.sec_id = TK.sec_id
     and T.semester = TK.semester
     and T.year = TK.year
    where T.ID = I.ID
      and TK.grade is not null
);
```

##### Method 3: Relational Set Operations (`INTERSECT` and `EXCEPT`)
Express the solution using set operators:

```sql
-- Instructors who gave at least one non-null grade
(select I.ID, I.name
 from instructor I
 join teaches T on I.ID = T.ID
 join takes TK
   on T.course_id = TK.course_id
  and T.sec_id = TK.sec_id
  and T.semester = TK.semester
  and T.year = TK.year
 where TK.grade is not null)
except
-- Instructors who gave an A grade
(select I.ID, I.name
 from instructor I
 join teaches T on I.ID = T.ID
 join takes TK
   on T.course_id = TK.course_id
  and T.sec_id = TK.sec_id
  and T.semester = TK.semester
  and T.year = TK.year
 where TK.grade = 'A');
```

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Teaching vs Grading
> A subtle trap in this question is checking `ID IN (select ID from teaches)`. Merely appearing in `teaches` only proves the instructor was assigned to a section. It does not prove that students enrolled or that final grades were submitted.
> Checking `takes.grade is not null` guarantees that the instructor actively awarded a real student grade.

---

### Exercise 3.33 · Comp Sci Courses with Afternoon Sections

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 3 (*Introduction to SQL*), Regular Exercise 3.33, Page 123.
> - **Subtopic:** T05.6 (Multi-Table Subqueries, Joins vs Subqueries).
> - **Target Database:** Standard ANSI SQL.
> - **RUET Exam Alignment:** High. Tests subqueries connecting course offerings to scheduling tables.

**Question (Silberschatz 7e Exercise 3.33).**
Using the university schema, write an SQL query to find the ID and title of each course in Comp. Sci. that has had at least one section with afternoon hours (i.e., ends at or after 12:00). (You should eliminate duplicates if any.)

#### 1. Core Principles & Concept Overview

Three relations from the university schema are involved:
- `course(course_id, title, dept_name, credits)`
- `section(course_id, sec_id, semester, year, building, room_number, time_slot_id)`
- `time_slot(time_slot_id, day, start_time, end_time)`

The criteria are:
1. Department filter: `course.dept_name = 'Comp. Sci.'`.
2. Schedule condition: Section ends in the afternoon, meaning `time_slot.end_time >= '12:00'`.
3. Duplicate elimination: A popular course may run multiple afternoon sections across different days or years. The output must list each course only once.

Duplicate elimination can be achieved in two ways:
- Using `DISTINCT` with an inner join.
- Using an `IN` or `EXISTS` subquery, which naturally preserves the uniqueness of outer tuples.

#### 2. Detailed Step-by-Step Solution

##### Method 1: Subquery using `IN` (Cleanest)
The subquery selects all `course_id` values that have an afternoon section. Because the outer query selects directly from `course`, each matching course appears exactly once without needing `distinct`:

```sql
select course_id, title
from course
where dept_name = 'Comp. Sci.'
  and course_id in (
      select section.course_id
      from section
      join time_slot
        on section.time_slot_id = time_slot.time_slot_id
      where time_slot.end_time >= '12:00'
  );
```

##### Method 2: Correlated Subquery using `EXISTS`
Use `exists` to test for the presence of a matching afternoon section:

```sql
select C.course_id, C.title
from course C
where C.dept_name = 'Comp. Sci.'
  and exists (
      select 1
      from section S
      join time_slot T
        on S.time_slot_id = T.time_slot_id
      where S.course_id = C.course_id
        and T.end_time >= '12:00'
  );
```

##### Method 3: Multi-Table Join with `DISTINCT`
Join all three tables and apply `distinct` to remove duplicate rows:

```sql
select distinct C.course_id, C.title
from course C
join section S on C.course_id = S.course_id
join time_slot T on S.time_slot_id = T.time_slot_id
where C.dept_name = 'Comp. Sci.'
  and T.end_time >= '12:00';
```

##### Variation for Oracle Time Schema
In Appendix A.2, the textbook notes that Oracle does not have a native standard `time` type. In the Oracle version of `time_slot`, hours and minutes are separate integer columns:

$$
\text{timeslot}(time\_slot\_id, day, start\_hr, start\_min, end\_hr, end\_min)
$$

For that schema, replace `end_time >= '12:00'` with:
```sql
where T.end_hr >= 12
```

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Why Subqueries Outperform Joins for Existence
> When a problem asks to find entities that have "at least one" associated event, writing `WHERE ID IN (...)` or `WHERE EXISTS (...)` is cleaner than writing an inner join with `DISTINCT`.
> The subquery stops scanning as soon as the first matching section is found. An inner join generates all combinations and then sorts them to remove duplicates.

---

### Practice Exercise 5.3 · Iterative Prerequisite Transitive Closure in JDBC

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Practice Exercise 5.3, Page 232.
> - **Subtopic:** T05.6 (Application-Level Transitive Closure, Cycle Prevention).
> - **Target Language / API:** Java 8+ / JDBC (`java.sql.*`).
> - **RUET Exam Alignment:** Medium-High. Past exams often ask for JDBC connectivity steps, SQL parameter binding, and iterative traversal.

**Question (Silberschatz 7e Practice Exercise 5.3).**
Suppose that we wish to find all courses that must be taken before some given course. That means finding not only the prerequisites of that course, but prerequisites of prerequisites, and so on. Write a complete Java program using JDBC that:
- Takes a `course_id` value from the keyboard.
- Finds prerequisites of that course using an SQL query submitted via JDBC.
- For each course returned, finds its prerequisites and continues this process iteratively until no new prerequisite courses are found.
- Prints out the result.

For this exercise, do not use a recursive SQL query, but rather use the iterative approach described previously. A well-developed solution will be robust to the error case where a university has accidentally created a cycle of prerequisites (that is, for example, course A is a prerequisite for course B, course B is a prerequisite for course C, and course C is a prerequisite for course A).

#### 1. Core Principles & Concept Overview

Course prerequisites form a directed graph $G = (V, E)$, where each directed edge $(u, v) \in E$ denotes that course $v$ is a prerequisite for course $u$. The relation in the university schema is:

$$
prereq(\underline{course\_id}, \underline{prereq\_id})
$$

Finding all prerequisites of a course requires computing the transitive closure of this graph starting from a root node.

Standard non-recursive SQL cannot express transitive closure over an arbitrary depth because relational algebra operations cannot perform unbounded looping. Therefore, applications solve this at the programming layer (e.g., in Java via JDBC) using an iterative fixed-point search algorithm.

##### Cycle Prevention Mechanics
If the prerequisite data contains a directed cycle (e.g., $A \rightarrow B \rightarrow C \rightarrow A$), a naive iterative search loops forever.
To guarantee termination, the algorithm maintains two collections:
1. `Set<String> allPrereqs`: Tracks all unique prerequisite courses found so far.
2. `Queue<String> workQueue`: Holds newly discovered prerequisite courses whose own prerequisites have not yet been queried.

When a prerequisite course $p$ is returned:
- If $p$ is already in `allPrereqs`, it is skipped.
- If $p$ is new, it is added to both `allPrereqs` and `workQueue`.

Because the set of courses $V$ is finite, each course is enqueued at most once. The loop terminates when `workQueue` becomes empty, even in the presence of cycles.

#### 2. Detailed Step-by-Step Solution

Here is the complete Java program with JDBC connectivity, `PreparedStatement` parameterization, Breadth-First Search (BFS) traversal, and cycle protection:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class FindAllPrerequisites {

    // Database connection parameters
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/university";
    private static final String DB_USER = "dbuser";
    private static final String DB_PASS = "dbpass";

    public static void main(String[] args) {
        // Read starting course_id from user keyboard
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter target course_id (e.g., CS-347): ");
        String startCourse = scanner.nextLine().trim();

        if (startCourse.isEmpty()) {
            System.out.println("Course ID cannot be empty.");
            return;
        }

        // Data structures for iterative BFS and cycle prevention
        Set<String> allPrereqs = new HashSet<>();
        Queue<String> workQueue = new ArrayDeque<>();

        // Parameterized query to fetch direct prerequisites
        String sql = "SELECT prereq_id FROM prereq WHERE course_id = ?";

        try (
            Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);
            PreparedStatement stmt = conn.prepareStatement(sql)
        ) {
            // Initialize traversal with the starting course
            workQueue.add(startCourse);

            while (!workQueue.isEmpty()) {
                String currentCourse = workQueue.poll();

                // Bind parameter and execute JDBC query
                stmt.setString(1, currentCourse);
                try (ResultSet rs = stmt.executeQuery()) {
                    while (rs.next()) {
                        String prereq = rs.getString("prereq_id");

                        // Cycle prevention check:
                        // If prereq was not previously seen and is not the starting course
                        if (!prereq.equalsIgnoreCase(startCourse) && !allPrereqs.contains(prereq)) {
                            allPrereqs.add(prereq);
                            workQueue.add(prereq);
                        }
                    }
                }
            }

            // Print the final result set
            System.out.println("\nAll prerequisite courses required before " + startCourse + ":");
            if (allPrereqs.isEmpty()) {
                System.out.println("  (No prerequisites found for this course.)");
            } else {
                for (String p : allPrereqs) {
                    System.out.println("  - " + p);
                }
                System.out.println("Total prerequisite courses: " + allPrereqs.size());
            }

        } catch (SQLException e) {
            System.err.println("Database error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

##### Algorithmic Complexity Analysis
Let $|V|$ be the number of courses and $|E|$ be the number of edges in `prereq`:
- Each course enters `workQueue` at most once.
- The `PreparedStatement` runs at most $|V|$ times.
- Total database query operations are bounded by $O(|V| + |E|)$.
- Space complexity is $O(|V|)$ to store the `allPrereqs` hash set.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Standard JDBC Exam Questions
> RUET theory exams often ask students to list the 5 standard steps of JDBC access:
> 1. Load database driver (`Class.forName` or automatic SPI registration).
> 2. Establish connection (`DriverManager.getConnection`).
> 3. Create prepared statement (`conn.prepareStatement`).
> 4. Execute query and retrieve result set (`stmt.executeQuery`).
> 5. Iterate through results (`rs.next()`) and close resources.
>
> In oral or written exams, emphasizing that `Set.add()` or `Set.contains()` prevents infinite loops when cycles exist is key to receiving full marks.

---

### Exercise 5.21 · Recursive CTE for Prerequisite Depths

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 5 (*Advanced SQL*), Regular Exercise 5.21, Page 236.
> - **Subtopic:** T05.6 (Recursive Queries, Common Table Expressions).
> - **Target Database:** Standard ANSI SQL:1999 (`WITH RECURSIVE`).
> - **RUET Exam Alignment:** High. Advanced questions examine the mechanics of recursive CTEs and fixed-point evaluation.

**Question (Silberschatz 7e Exercise 5.21).**
Modify the recursive query in Figure 5.16 to define a relation
```text
prereq_depth(course_id, prereq_id, depth)
```
where the attribute depth indicates how many levels of intermediate prerequisites there are between the course and the prerequisite. Direct prerequisites have a depth of 0. Note that a prerequisite course may have multiple depths and thus may appear more than once.

#### 1. Core Principles & Concept Overview

Figure 5.16 in Silberschatz 7e defines the basic recursive query for prerequisite transitive closure:

```sql
with recursive rec_prereq(course_id, prereq_id) as (
    select course_id, prereq_id
    from prereq
  union
    select rec_prereq.course_id, prereq.prereq_id
    from rec_prereq, prereq
    where rec_prereq.prereq_id = prereq.course_id
)
select *
from rec_prereq;
```

A recursive view consists of two parts joined by a `UNION` or `UNION ALL`:
1. **Base Query**: The non-recursive anchor query that initializes the view.
2. **Recursive Query**: An iterative query that references the view itself to generate additional tuples until a fixed point is reached.

This exercise requires adding an attribute `depth` that counts intermediate prerequisite levels:
- A direct prerequisite has 0 intermediate levels: $\text{depth} = 0$.
- If course $A$ requires $B$ at depth $d$, and $B$ directly requires $C$, then $C$ is a prerequisite of $A$ at:
  $$
  \text{depth} = d + 1
  $$

The question notes that if course $A$ requires $C$ directly (depth 0) and also requires $B$ which requires $C$ (depth 1), both $(A, C, 0)$ and $(A, C, 1)$ should appear in the result relation.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Define the Base Query
Direct prerequisites from `prereq` have an intermediate depth of 0:

```sql
select course_id, prereq_id, 0 as depth
from prereq
```

##### Step 2: Define the Recursive Query
Join the recursive view `prereq_depth` with `prereq`. Increment the `depth` attribute by 1:

```sql
select rec.course_id, p.prereq_id, rec.depth + 1 as depth
from prereq_depth rec
join prereq p on rec.prereq_id = p.course_id
```

##### Step 3: Complete SQL Recursive Query
Combine the base and recursive queries inside the `with recursive` clause:

```sql
with recursive prereq_depth(course_id, prereq_id, depth) as (
    -- Base Query: Direct prerequisites have depth 0
    select course_id, prereq_id, 0 as depth
    from prereq

    union

    -- Recursive Step: Add 1 to depth for each intermediate level
    select rec.course_id, p.prereq_id, rec.depth + 1 as depth
    from prereq_depth rec
    join prereq p
      on rec.prereq_id = p.course_id
)
select course_id, prereq_id, depth
from prereq_depth;
```

##### Step 4: Trace with Sample Data
Consider three courses:
- `BIO-301` directly requires `BIO-201`
- `BIO-201` directly requires `BIO-101`
- `BIO-301` also directly requires `BIO-101`

Let us trace the fixed-point evaluation:
- **Iteration 0 (Base Query):**
  - `(BIO-301, BIO-201, 0)`
  - `(BIO-201, BIO-101, 0)`
  - `(BIO-301, BIO-101, 0)`
- **Iteration 1 (First Recursive Step):**
  - Join `(BIO-301, BIO-201, 0)` with `(BIO-201, BIO-101)` $\rightarrow$ produces `(BIO-301, BIO-101, 1)`.
- **Iteration 2 (Second Recursive Step):**
  - No new prerequisites found. The fixed point is reached.

The final relation contains both `(BIO-301, BIO-101, 0)` and `(BIO-301, BIO-101, 1)`. Because their depth values differ (0 vs 1), `UNION` retains both tuples.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Fixed-Point Semantics and Monotonicity
> A recursive query in SQL must be **monotonic**. That means adding rows to the recursive view cannot cause previously derived rows to disappear.
>
> For this reason, SQL standard forbids the following inside the recursive step:
> - Aggregation functions (`COUNT`, `SUM`, `MAX`) on the recursive view.
> - `NOT EXISTS` referencing the recursive view.
> - Set difference (`EXCEPT`) where the recursive view appears on the right side.
>
> If a database contains cycles, an unbounded recursive CTE will run indefinitely until memory is exhausted. Standard SQL:2008 introduced the `CYCLE` clause to prevent infinite loops:
> `CYCLE prereq_id SET is_cycle USING path`
> In exams, adding a safety condition like `WHERE rec.depth < 20` shows good awareness of cycle handling.

---
