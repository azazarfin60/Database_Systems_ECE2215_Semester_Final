---
title: "T06 · Joins and Views · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T05 · SQL DDL, DML, Aggregates & Subqueries](T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Exam-style layer](../Topicwise_answers_exam_style/T06_Joins_and_Views.md) | [Next: T07 · Triggers and Stored Procedures →](T07_Triggers_and_Stored_Procedures.md)

---

# T06 · Joins and Views

> [!info] Topic card
> **Syllabus:** Unit 4 · **Weight:** 28 final marks (4.4%) in 4/7 papers + 0 CT marks
> **Sources:** Deck 04 · Textbook Ch. 4 §4.1–4.2, Ch. 16 §16.2
> **Blocks in this file:** 7 final questions (6 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T06.1 | Types of joins | 11 + 0 | 2019 Q.3(c), 2023 Q.5(c), 2024 Q.3(c) | [[#T06.1 · Types of joins\|Go]] |
| T06.2 | Join outcome tables | 11 + 0 | 2020 Q.4(c), 2024 Q.4(a) | [[#T06.2 · Join outcome tables\|Go]] |
| T06.3 | Outer-join algebra | 0 + 0 | No questions | [[#T06.3 · Outer-join algebra\|Go]] |
| T06.4 | Views and CREATE VIEW | 6 + 0 | 2023 Q.5(a), 2023 Q.5(b) | [[#T06.4 · Views and CREATE VIEW\|Go]] |
| T06.5 | View expansion, updatable and materialized views | 0 + 0 | No questions | [[#T06.5 · View expansion, updatable and materialized views\|Go]] |

---

## T06.1 · Types of joins

### 2019 Q.3(c) · 05 Marks

*Section A · Asked in: 2019, 2023 (Sec B, CLO2) · L2 merge*

**Question (2019 Q.3(c)).** What is joining? Discuss each type of joining between two data tables with example.

**Question (2023 Q.5(c)).** Define joining. Discuss different types of joining with suitable example.

**Answer.**

**What the examiner wants.**  
A formal definition of a join operation in relational database systems (1 mark), followed by descriptions and examples of the main join types: Inner join, Left outer join, Right outer join, Full outer join, and Cross join (4 marks, approximately 1 mark per join type).

**Key idea.**  
A join operation combines tuples from two tables into a single result relation. It checks matching values in specified columns. An inner join keeps only matching rows. An outer join retains matching rows plus unmatched rows from one or both tables by padding empty attributes with `NULL`. A cross join pairs every row from the first table with every row from the second table.

**Step-by-step solution.**

**Definition of Joining:**  
A join operation takes two relations and combines them into one relation based on a matching condition. It acts as a Cartesian product followed by a selection predicate and projection.

![Summary of SQL join types and join conditions](../LectureSlides/diagrams/L04_p04_fig01.jpg)
*Figure: Join types and join conditions (Deck 04, Slide 4)*

**Example Base Tables:**

Table `course`:

| course_id | title | dept_name | credits |
| :--- | :--- | :--- | :--- |
| BIO-301 | Genetics | Biology | 4 |
| CS-190 | Game Design | Comp. Sci. | 4 |
| CS-315 | Robotics | Comp. Sci. | 3 |

Table `prereq`:

| course_id | prereq_id |
| :--- | :--- |
| BIO-301 | BIO-101 |
| CS-190 | CS-101 |
| CS-347 | CS-101 |

---

#### 1. Inner Join (and Natural Join)
Retains only tuples that satisfy the join condition in both tables. Unmatched rows are dropped.

```sql
SELECT course.course_id, title, dept_name, prereq_id
FROM course
INNER JOIN prereq ON course.course_id = prereq.course_id;
```

Relational algebra:
$$
\text{course} \bowtie \text{prereq}
$$

**Result:**

| course_id | title | dept_name | prereq_id |
| :--- | :--- | :--- | :--- |
| BIO-301 | Genetics | Biology | BIO-101 |
| CS-190 | Game Design | Comp. Sci. | CS-101 |

---

#### 2. Left Outer Join
Preserves every row from the left table (`course`). Fills right-table attributes with `NULL` when no match exists.

```sql
SELECT course.course_id, title, dept_name, prereq_id
FROM course
LEFT JOIN prereq ON course.course_id = prereq.course_id;
```

Relational algebra:
$$
\text{course} \mathbin{⟕} \text{prereq}
$$

**Result:**

| course_id | title | dept_name | prereq_id |
| :--- | :--- | :--- | :--- |
| BIO-301 | Genetics | Biology | BIO-101 |
| CS-190 | Game Design | Comp. Sci. | CS-101 |
| CS-315 | Robotics | Comp. Sci. | `NULL` |

---

#### 3. Right Outer Join
Preserves every row from the right table (`prereq`). Fills left-table attributes with `NULL` when no match exists.

```sql
SELECT prereq.course_id, title, dept_name, prereq_id
FROM course
RIGHT JOIN prereq ON course.course_id = prereq.course_id;
```

Relational algebra:
$$
\text{course} \mathbin{⟖} \text{prereq}
$$

**Result:**

| course_id | title | dept_name | prereq_id |
| :--- | :--- | :--- | :--- |
| BIO-301 | Genetics | Biology | BIO-101 |
| CS-190 | Game Design | Comp. Sci. | CS-101 |
| CS-347 | `NULL` | `NULL` | CS-101 |

---

#### 4. Full Outer Join
Retains all rows from both tables. It pairs matching rows and fills missing values with `NULL`. MySQL emulates it using `UNION`.

```sql
SELECT course.course_id, title, dept_name, prereq_id
FROM course
LEFT JOIN prereq ON course.course_id = prereq.course_id
UNION
SELECT prereq.course_id, title, dept_name, prereq_id
FROM course
RIGHT JOIN prereq ON course.course_id = prereq.course_id;
```

Relational algebra:
$$
\text{course} \mathbin{⟗} \text{prereq}
$$

**Result:**

| course_id | title | dept_name | prereq_id |
| :--- | :--- | :--- | :--- |
| BIO-301 | Genetics | Biology | BIO-101 |
| CS-190 | Game Design | Comp. Sci. | CS-101 |
| CS-315 | Robotics | Comp. Sci. | `NULL` |
| CS-347 | `NULL` | `NULL` | CS-101 |

---

#### 5. Cross Join (Cartesian Product)
Combines each row of the first table with every row of the second table without any condition.

```sql
SELECT *
FROM course
CROSS JOIN prereq;
```

Relational algebra:
$$
\text{course} \times \text{prereq}
$$

It returns $3 \times 3 = 9$ rows.

*Variant for 2023 Q.5(c) (4 marks):* The same definition and four outer and inner join examples answer the question.

**Check.**  
*Quick self-test:*
- Q: What happens to a course with no prerequisites in an INNER JOIN?  
  A: It is dropped from the result relation because no matching tuple exists in `prereq`.
- Q: How does a FULL OUTER JOIN handle tuples present in only one table?  
  A: It retains both tuples and pads the missing columns from the other relation with `NULL`.
- Q: Does MySQL support the SQL standard `FULL OUTER JOIN` syntax directly?  
  A: No. MySQL does not have native `FULL OUTER JOIN` syntax, so we combine `LEFT JOIN` and `RIGHT JOIN` with `UNION`.

> [!warning] Common mistakes
> - Writing that MySQL supports native `FULL OUTER JOIN` syntax directly.
> - Confusing Natural Join with Inner Join: Natural Join automatically equates all common column names, whereas Inner Join uses an explicit condition.
> - Omitting `NULL` values when drawing outer join result tables.

**Exam tip.**  
Use one small pair of 3-row tables across all join types. This saves drawing time and lets the examiner verify row counts instantly.

**Sources.**  
- [Deck 04 · Slides 3–13, 20–23](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.1](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

### 2024 Q.3(c) · 02 Marks

*Section A · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** Differentiate between inner joining and outer joining.

**Answer.**

**What the examiner wants.**  
A concise, structured comparison highlighting the differences between inner joins and outer joins for 2 marks. Examiners look for tuple retention, handling of missing values, and query syntax.

**Key idea.**  
An inner join is strict: it only outputs rows where both tables satisfy the join condition. An outer join is inclusive: it preserves non-matching rows from one or both tables by padding empty columns with `NULL`.

**Step-by-step solution.**

| Feature | Inner Join | Outer Join |
| :--- | :--- | :--- |
| **Tuple Retention** | Keeps only matching tuples from both relations. Drops non-matching rows. | Preserves matching rows plus unmatched rows from one or both relations. |
| **Missing Values** | Never produces `NULL` values to represent missing relationship data. | Pads missing attributes of unmatched tuples with `NULL`. |
| **Information Loss** | Loses dangling records that fail the join predicate. | Prevents information loss by keeping all records from preserved relations. |
| **Forms / Syntax** | Theta join, equijoin, and natural join (`INNER JOIN`, `JOIN`). | Left outer, right outer, and full outer join (`LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`). |

**Check.**  
*Quick self-test:*
- Q: If table A has 5 rows and table B has 0 matching rows, how many rows does an inner join return?  
  A: 0 rows.
- Q: Under the same condition, how many rows does a left outer join return?  
  A: 5 rows, each padded with `NULL` for attributes of table B.

> [!warning] Common mistakes
> - Writing unstructured prose paragraphs instead of a clear comparison table.
> - Forgetting to mention that outer joins prevent loss of information by using `NULL` values.

**Exam tip.**  
For a 2-mark distinction question, write a 3 to 4 row comparison table. It takes under two minutes and secures full marks.

**Sources.**  
- [Deck 04 · Slides 4–5](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.1](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

## T06.2 · Join outcome tables

### 2020 Q.4(c) · 05 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.**
Consider the following tables:

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 25px;"><b>Courses</b><br><table border="1" style="border-collapse: collapse; text-align: center; margin-top: 4px;"><thead><tr><th style="padding: 3px 8px;">Code</th><th style="padding: 3px 8px;">Series</th><th style="padding: 3px 8px;">t code</th></tr></thead><tbody><tr><td>ECE 2215</td><td>2017</td><td>T1</td></tr><tr><td>ECE 4127</td><td>2016</td><td>T2</td></tr><tr><td>ECE 1203</td><td>2019</td><td>T3</td></tr><tr><td>ECE 2219</td><td>2017</td><td>T2</td></tr></tbody></table></td><td style="border: none;"><b>Teacher</b><br><table border="1" style="border-collapse: collapse; text-align: center; margin-top: 4px;"><thead><tr><th style="padding: 3px 8px;">t code</th><th style="padding: 3px 8px;">Designation</th></tr></thead><tbody><tr><td>T1</td><td>Head</td></tr><tr><td>T2</td><td>Professor</td></tr><tr><td>T3</td><td>Lecturer</td></tr><tr><td>T4</td><td>Lecturer</td></tr></tbody></table></td></tr></table>  
What will happen when the following actions will be performed on these two relations?  
(i) Natural Join  
(ii) Left Outer Join  
(iii) Right Outer Join  
(iv) Full Outer Join

**Answer.**

**What the examiner wants.**  
The exact resulting relations for all four join operations on the given instance (about 1.25 marks per sub-question). Examiners verify correct attributes, accurate row counts, and proper `NULL` values.

**Key idea.**  
Both relations share the join attribute `t code`. In Courses, the teacher codes are T1, T2, and T3 (T2 appears twice). In Teacher, the codes are T1, T2, T3, and T4. Every course has a matching teacher. But teacher T4 has no courses assigned. Natural and left joins produce 4 rows. Right and full joins preserve T4 with `NULL` in the course columns, giving 5 rows.

**Step-by-step solution.**

*Assumption: The attribute "t code" is the common join key between Courses and Teacher.*

The common attribute is `t code`. In SQL statements, it is written as `` `t code` ``.

#### (i) Natural Join
Matches tuples where `t code` is identical and outputs one copy of `t code`.

Relational algebra:
$$
\text{Courses} \bowtie \text{Teacher}
$$

MySQL query:
```sql
SELECT Code, Series, `t code`, Designation
FROM Courses
NATURAL JOIN Teacher;
```

**Outcome Table (4 rows):**

| Code | Series | t code | Designation |
| :--- | :--- | :--- | :--- |
| ECE 2215 | 2017 | T1 | Head |
| ECE 4127 | 2016 | T2 | Professor |
| ECE 1203 | 2019 | T3 | Lecturer |
| ECE 2219 | 2017 | T2 | Professor |

*Explanation:* Every course has a matching teacher. T4 in Teacher has no course, so it is omitted.

---

#### (ii) Left Outer Join
Preserves all rows from the left table (**Courses**). Missing right attributes get `NULL`.

Relational algebra:
$$
\text{Courses} \mathbin{⟕} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Courses.`t code`, Teacher.Designation
FROM Courses
LEFT JOIN Teacher ON Courses.`t code` = Teacher.`t code`;
```

**Outcome Table (4 rows):**

| Code | Series | t code | Designation |
| :--- | :--- | :--- | :--- |
| ECE 2215 | 2017 | T1 | Head |
| ECE 4127 | 2016 | T2 | Professor |
| ECE 1203 | 2019 | T3 | Lecturer |
| ECE 2219 | 2017 | T2 | Professor |

*Explanation:* All `t code` values in Courses (T1, T2, T3) exist in Teacher. No `NULL` padding is needed. The result matches the Natural Join.

---

#### (iii) Right Outer Join
Preserves all rows from the right table (**Teacher**). Unmatched rows get `NULL` in Courses columns.

Relational algebra:
$$
\text{Courses} \mathbin{⟖} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Teacher.`t code`, Teacher.Designation
FROM Courses
RIGHT JOIN Teacher ON Courses.`t code` = Teacher.`t code`;
```

**Outcome Table (5 rows):**

| Code | Series | t code | Designation |
| :--- | :--- | :--- | :--- |
| ECE 2215 | 2017 | T1 | Head |
| ECE 4127 | 2016 | T2 | Professor |
| ECE 2219 | 2017 | T2 | Professor |
| ECE 1203 | 2019 | T3 | Lecturer |
| `NULL` | `NULL` | T4 | Lecturer |

*Explanation:* Teacher T4 has no matching course. It appears with `NULL` for `Code` and `Series`.

---

#### (iv) Full Outer Join
Retains all rows from both tables. Missing attributes from either side are padded with `NULL`.

Relational algebra:
$$
\text{Courses} \mathbin{⟗} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Courses.`t code`, Teacher.Designation
FROM Courses
LEFT JOIN Teacher ON Courses.`t code` = Teacher.`t code`
UNION
SELECT Courses.Code, Courses.Series, Teacher.`t code`, Teacher.Designation
FROM Courses
RIGHT JOIN Teacher ON Courses.`t code` = Teacher.`t code`;
```

**Outcome Table (5 rows):**

| Code | Series | t code | Designation |
| :--- | :--- | :--- | :--- |
| ECE 2215 | 2017 | T1 | Head |
| ECE 4127 | 2016 | T2 | Professor |
| ECE 2219 | 2017 | T2 | Professor |
| ECE 1203 | 2019 | T3 | Lecturer |
| `NULL` | `NULL` | T4 | Lecturer |

*Explanation:* Combines all matching rows plus unmatched teacher T4 with `NULL` values.

**Check.**  
*Tuple count verification:*
- Courses has 4 tuples; Teacher has 4 tuples.
- Matched pairs on `t code`: (ECE 2215, T1), (ECE 4127, T2), (ECE 2219, T2), (ECE 1203, T3). Total = 4 matched tuples.
- Unmatched Courses tuples: 0.
- Unmatched Teacher tuples: 1 (T4).
- Natural Join rows = 4.
- Left Outer Join rows = $4 + 0 = 4$.
- Right Outer Join rows = $4 + 1 = 5$.
- Full Outer Join rows = $4 + 0 + 1 = 5$.

> [!warning] Common mistakes
> - Writing empty spaces instead of explicit `NULL` for missing attributes.
> - Repeating `t code` twice in the Natural Join output table.
> - Omitting the second row for teacher T2 (ECE 2219). Both course rows must appear.

**Exam tip.**  
Always count the tuples before drawing the tables. If all left tuples find a match, the Left Outer Join result is identical to the Natural Join.

**Sources.**  
- [Deck 04 · Slides 5–11, 14–18](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.1](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

### 2024 Q.4(a) · 06 Marks

*Section A · CO2 · Asked in: 2024 · L1 (asked once)*

**Question.**
Consider the following tables:

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Courses</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">Code</th><th style="padding: 4px 10px;">Series</th><th style="padding: 4px 10px;">t_code</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">E_2215</td><td style="padding: 4px 10px;">2020</td><td style="padding: 4px 10px;">T1</td></tr><tr><td style="padding: 4px 10px;">E_4127</td><td style="padding: 4px 10px;">2021</td><td style="padding: 4px 10px;">T2</td></tr><tr><td style="padding: 4px 10px;">E_1203</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">T3</td></tr><tr><td style="padding: 4px 10px;">E_2219</td><td style="padding: 4px 10px;">2021</td><td style="padding: 4px 10px;">T3</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>Teacher</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">t_code</th><th style="padding: 4px 10px;">Designation</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">T1</td><td style="padding: 4px 10px;">Head</td></tr><tr><td style="padding: 4px 10px;">T2</td><td style="padding: 4px 10px;">AP</td></tr><tr><td style="padding: 4px 10px;">T3</td><td style="padding: 4px 10px;">AP</td></tr><tr><td style="padding: 4px 10px;">T4</td><td style="padding: 4px 10px;">Lecturer</td></tr></tbody></table></td></tr></table>  
Discuss the outcome when the following actions will be performed on these two relations.  
i) Natural Join  
ii) Left Outer Join  
iii) Right Outer Join  
iv) Full Outer Join

**Answer.**

**What the examiner wants.**  
Step-by-step derivation of each join outcome with schema names, row counts, explanation of matching tuples, and resulting Markdown tables (1.5 marks per operation).

**Key idea.**  
The common attribute is `t_code`. Here, teacher T3 teaches two courses (E_1203 and E_2219). Teacher T2 and T1 each teach one course. Teacher T4 has no course. All rows in Courses match a teacher, so left join produces 4 rows. Right and full outer joins append T4 with `NULL` values to produce 5 rows.

**Step-by-step solution.**

The common attribute between Courses and Teacher is `t_code`.

#### i) Natural Join
Matches tuples with equal `t_code` values and retains one copy of `t_code`.

Relational algebra:
$$
\text{Courses} \bowtie \text{Teacher}
$$

MySQL query:
```sql
SELECT Code, Series, t_code, Designation
FROM Courses
NATURAL JOIN Teacher;
```

**Outcome Table (4 rows):**

| Code | Series | t_code | Designation |
| :--- | :--- | :--- | :--- |
| E_2215 | 2020 | T1 | Head |
| E_4127 | 2021 | T2 | AP |
| E_1203 | 2022 | T3 | AP |
| E_2219 | 2021 | T3 | AP |

*Explanation:* T1, T2, and T3 have matches in Teacher. T3 matches twice because two courses share T3. Teacher T4 has no course match and is omitted.

---

#### ii) Left Outer Join
Preserves all tuples from the left relation (**Courses**). Unmatched right-side fields are set to `NULL`.

Relational algebra:
$$
\text{Courses} \mathbin{⟕} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Courses.t_code, Teacher.Designation
FROM Courses
LEFT JOIN Teacher ON Courses.t_code = Teacher.t_code;
```

**Outcome Table (4 rows):**

| Code | Series | t_code | Designation |
| :--- | :--- | :--- | :--- |
| E_2215 | 2020 | T1 | Head |
| E_4127 | 2021 | T2 | AP |
| E_1203 | 2022 | T3 | AP |
| E_2219 | 2021 | T3 | AP |

*Explanation:* Every course row has an assigned `t_code` present in Teacher. No `NULL` padding is needed. The outcome is identical to the Natural Join.

---

#### iii) Right Outer Join
Preserves all tuples from the right relation (**Teacher**). Unmatched left-side fields are filled with `NULL`.

Relational algebra:
$$
\text{Courses} \mathbin{⟖} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Teacher.t_code, Teacher.Designation
FROM Courses
RIGHT JOIN Teacher ON Courses.t_code = Teacher.t_code;
```

**Outcome Table (5 rows):**

| Code | Series | t_code | Designation |
| :--- | :--- | :--- | :--- |
| E_2215 | 2020 | T1 | Head |
| E_4127 | 2021 | T2 | AP |
| E_1203 | 2022 | T3 | AP |
| E_2219 | 2021 | T3 | AP |
| `NULL` | `NULL` | T4 | Lecturer |

*Explanation:* Teacher T4 has no matching course row. T4 appears with `NULL` for `Code` and `Series`.

---

#### iv) Full Outer Join
Retains all records from both relations. Non-matching fields are filled with `NULL`.

Relational algebra:
$$
\text{Courses} \mathbin{⟗} \text{Teacher}
$$

MySQL query:
```sql
SELECT Courses.Code, Courses.Series, Courses.t_code, Teacher.Designation
FROM Courses
LEFT JOIN Teacher ON Courses.t_code = Teacher.t_code
UNION
SELECT Courses.Code, Courses.Series, Teacher.t_code, Teacher.Designation
FROM Courses
RIGHT JOIN Teacher ON Courses.t_code = Teacher.t_code;
```

**Outcome Table (5 rows):**

| Code | Series | t_code | Designation |
| :--- | :--- | :--- | :--- |
| E_2215 | 2020 | T1 | Head |
| E_4127 | 2021 | T2 | AP |
| E_1203 | 2022 | T3 | AP |
| E_2219 | 2021 | T3 | AP |
| `NULL` | `NULL` | T4 | Lecturer |

*Explanation:* All courses find a teacher match. The unmatched teacher T4 is preserved with `NULL` for `Code` and `Series`.

**Check.**  
*Tuple count verification:*
- Courses: 4 tuples (all matched).
- Teacher: 4 tuples (3 matched, 1 unmatched: T4).
- Natural Join rows = 4.
- Left Outer Join rows = 4.
- Right Outer Join rows = $4 + 1 = 5$.
- Full Outer Join rows = $4 + 0 + 1 = 5$.

> [!warning] Common mistakes
> - Assuming the 2024 data is identical to the 2020 paper. In 2024, T3 teaches two courses, whereas in 2020, T2 taught two courses.
> - Leaving attribute cells blank instead of explicitly writing `NULL`.

**Exam tip.**  
Include the relational algebra expression alongside each MySQL query. It shows strong mastery and helps lock in full marks.

**Sources.**  
- [Deck 04 · Slides 5–11, 14–18](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.1](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

## T06.3 · Outer-join algebra

*No questions from past finals or class tests.*

*See also:* [[#T06.2 · Join outcome tables]] (2020 Q.4(c), 2024 Q.4(a))

---

## T06.4 · Views and CREATE VIEW

### 2023 Q.5(a) · 03 Marks

*Section B · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** What are the benefits of VIEW?

**Answer.**

**What the examiner wants.**  
A concise definition of what a view is, followed by four clear benefits of using views in database systems (about 0.75 marks per benefit).

**Key idea.**  
A view is a saved query that acts like a virtual table. It does not duplicate table data on disk. Instead, it creates a custom window into the database. It improves security by hiding columns, simplifies complex SQL, and gives logical data independence.

**Step-by-step solution.**

A view is a virtual relation defined by an SQL query. The database does not store the view data on disk. Instead, it stores the query definition and executes it when referenced.

**Key Benefits of Views:**
1. **Security and Access Control:** Views hide sensitive columns and rows from unauthorized users. For example, a view can display employee names and departments while hiding salary data.
2. **Query Simplicity:** Views hide complex joins, unions, and aggregate calculations behind a single virtual table name. Users run simple `SELECT` queries on the view.
3. **Logical Data Independence:** If base tables are restructured, split, or renamed, the administrator updates only the view query. Applications using the view continue running without changes.
4. **Consistent and Standardized Data Representation:** Views provide uniform business calculations across multiple users and departments. This avoids duplicate and conflicting query logic.

**Check.**  
*Quick self-test:*
- Q: Does creating a view duplicate table data on disk?  
  A: No. A standard view stores only the query definition. The query is evaluated when referenced.
- Q: How does a view provide logical data independence?  
  A: When the underlying schema changes, modifying the view definition keeps existing application queries valid.

> [!warning] Common mistakes
> - Confusing standard virtual views with materialized views (standard views do not store physical rows on disk).
> - Stating vague benefits like "makes queries faster" instead of precise database concepts like "logical data independence" and "access security".

**Exam tip.**  
Include a concrete security example, such as hiding instructor salaries from students. This convinces the examiner immediately.

**Sources.**  
- [Deck 04 · Slides 24–26](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.2](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

### 2023 Q.5(b) · 03 Marks

*Section B · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.**
Create a VIEW using SQL query that shows the EmployeeName, DepartmentName and salary for employees who earn a salary of more than 55,000.

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>E.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">EmployeeID</th><th style="padding: 4px 10px;">EmployeeName</th><th style="padding: 4px 10px;">Department ID</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">Jhon</td><td style="padding: 4px 10px;">D01</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">Jane</td><td style="padding: 4px 10px;">D02</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">Alice</td><td style="padding: 4px 10px;">D01</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">Bob</td><td style="padding: 4px 10px;">D03</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>D.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">DepartmentID</th><th style="padding: 4px 10px;">DepartmentName</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">D01</td><td style="padding: 4px 10px;">Sales</td></tr><tr><td style="padding: 4px 10px;">D02</td><td style="padding: 4px 10px;">HR</td></tr><tr><td style="padding: 4px 10px;">D03</td><td style="padding: 4px 10px;">IT</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>S.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">EmployeeID</th><th style="padding: 4px 10px;">Salary</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">50,000</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">60,000</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">55,000</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">70,000</td></tr></tbody></table></td></tr></table>

**Answer.**

**What the examiner wants.**  
Accurate SQL DDL using `CREATE VIEW view_name AS SELECT ...` that joins tables to retrieve `EmployeeName`, `DepartmentName`, and `Salary`, filtered by `Salary > 55000` (2 marks for syntax and joins, 1 mark for the filter).

**Key idea.**  
The query joins relations on matching keys (`DeptID` or `DepartmentID` and `EmployeeID`), projects the required three attributes, and filters rows where `Salary > 55000`.

**Step-by-step solution.**

*Assumption: Schema consists of Employee(EmpID, EmployeeName, Salary, DeptID) and Department(DeptID, DepartmentName).*

**SQL Query (Standard 2-Table Schema):**
```sql
CREATE VIEW High_Salary_Employees AS
SELECT Employee.EmployeeName, Department.DepartmentName, Employee.Salary
FROM Employee
JOIN Department ON Employee.DeptID = Department.DeptID
WHERE Employee.Salary > 55000;
```

**Alternative SQL Query (Using Printed Tables E, D, and S):**
Joining table **E**, table **D**, and table **S**:
```sql
CREATE VIEW High_Salary_Employees AS
SELECT E.EmployeeName, D.DepartmentName, S.Salary
FROM E
JOIN D ON E.`Department ID` = D.DepartmentID
JOIN S ON E.EmployeeID = S.EmployeeID
WHERE S.Salary > 55000;
```

**View Output:**

| EmployeeName | DepartmentName | Salary |
| :--- | :--- | :--- |
| Jane | HR | 60,000 |
| Bob | IT | 70,000 |

*(Note: Employees Jhon with 50,000 and Alice with 55,000 are excluded because their salaries do not exceed 55,000).*

**Check.**  
*Tuple-by-tuple trace on printed data:*
- EmpID 101: Jhon, Dept D01 (Sales), Salary 50,000. Filter `50000 > 55000` is False. Excluded.
- EmpID 102: Jane, Dept D02 (HR), Salary 60,000. Filter `60000 > 55000` is True. Included: (Jane, HR, 60,000).
- EmpID 103: Alice, Dept D01 (Sales), Salary 55,000. Filter `55000 > 55000` is False. Excluded because the condition is strictly greater than.
- EmpID 104: Bob, Dept D03 (IT), Salary 70,000. Filter `70000 > 55000` is True. Included: (Bob, IT, 70,000).

> [!warning] Common mistakes
> - Using `>= 55000` instead of `> 55000`. The question specifies "more than 55,000", which excludes Alice.
> - Omitting backticks around `Department ID` in MySQL when referencing the printed attribute with a space.
> - Projecting all attributes (`SELECT *`) instead of only the three requested columns.

**Exam tip.**  
State an explicit schema assumption if the question wording does not specify table structure. Also show the resulting tuples to verify the query output.

**Sources.**  
- [Deck 04 · Slides 24–28](../LectureSlides/04_Joining_and_Views.md)  
- [Textbook Ch. 4 §4.2](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

## T06.5 · View expansion, updatable and materialized views

*No questions from past finals or class tests.*

---

[← Prev: T05 · SQL DDL, DML, Aggregates & Subqueries](T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Exam-style layer](../Topicwise_answers_exam_style/T06_Joins_and_Views.md) | [Next: T07 · Triggers and Stored Procedures →](T07_Triggers_and_Stored_Procedures.md)
