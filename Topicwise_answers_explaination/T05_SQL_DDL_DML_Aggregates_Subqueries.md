---
title: "T05 · SQL (DDL, DML, Aggregates, Subqueries) · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T04 · Relational Algebra and Calculus](T04_Relational_Algebra_and_Calculus.md) | [Exam-style layer](../Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T06 · Joins and Views →](T06_Joins_and_Views.md)

---

# T05 · SQL (DDL, DML, Aggregates, Subqueries)

> [!info] Topic card
> **Syllabus:** Unit 4 · **Weight:** 130 final marks (20.4%) in 7/7 papers + 10 CT marks
> **Sources:** Deck 03 (all 62 slides), Deck 04 (Slides 2–15) · Textbook Ch. 3 (§3.2–3.9), Ch. 4 (§4.1–4.4)
> **Blocks in this file:** 23 final + 4 CT questions (22 blocks after 4 L2 merges)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T05.1 | What SQL is; SQL short note | 2 + 0 | 2019 Q.5(a) | [[#T05.1 · What SQL is; SQL short note\|Go]] |
| T05.2 | DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter | 33 + 2 | 2017 Q.4(a), 2018 Q.7(a), 2019 Q.5(c), 2021 Q.3(a), 2023 Q.3(a), 2024 Q.4(b), CT-02 Q.01(a) | [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter\|Go]] |
| T05.3 | Basic query clauses: DISTINCT, ORDER BY, AS, LIKE | 0 + 2 | CT-02 Q.01(b) | [[#T05.3 · Basic query clauses: DISTINCT, ORDER BY, AS, LIKE\|Go]] |
| T05.4 | Aggregate functions (theory) | 7 + 0 | 2019 Q.8(a), 2024 Q.7(a) | [[#T05.4 · Aggregate functions (theory)\|Go]] |
| T05.5 | Aggregation queries: GROUP BY + HAVING, CGPA, extremes without LIMIT | 24 + 3 | 2018 Q.7(b), 2019 Q.7(a), 2024 Q.1(c), CT-02 Q.01(d) | [[#T05.5 · Aggregation queries: GROUP BY + HAVING, CGPA, extremes without LIMIT\|Go]] |
| T05.6 | Subqueries theory ("two examples"): IN, SOME/ALL, EXISTS, scalar, correlated, WITH | 8 + 3 | 2019 Q.8(b), 2024 Q.6(a), CT-02 Q.01(c) | [[#T05.6 · Subqueries theory ("two examples"): IN, SOME/ALL, EXISTS, scalar, correlated, WITH\|Go]] |
| T05.7 | Multi-table business-schema query sets (MySQL): Covid, Company, Insurance, E-commerce | 44 + 0 | 2019 Q.5(b), 2020 Q.3(b), 2020 Q.7(b), 2021 Q.4(a), 2024 Q.5(b) | [[#T05.7 · Multi-table business-schema query sets (MySQL): Covid, Company, Insurance, E-commerce\|Go]] |
| T05.8 | Short notes: ON DELETE CASCADE, GROUP BY, ORDER BY, AS | 10 + 0 | 2019 Q.8(c), 2023 Q.6(c), 2024 Q.7(b) | [[#T05.8 · Short notes: ON DELETE CASCADE, GROUP BY, ORDER BY, AS\|Go]] |
| T05.9 | TRUNCATE vs DELETE | 2 + 0 | 2023 Q.6(a) | [[#T05.9 · TRUNCATE vs DELETE\|Go]] |

---

## T05.1 · What SQL is; SQL short note

### 2019 Q.5(a) · 02 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Write a short note on SQL.

**Answer.**

**What the examiner wants.**  
The formal full name of SQL, its original historical background (IBM System R), its declarative paradigm, and its major sub-languages (DDL, DML, DCL/TCL). The mark split is 1 mark for the core definition and role, and 1 mark for key functional parts.

**Key idea.**  
Unlike procedural programming languages (C, Java) where you write explicit loops to access disk records, SQL is non-procedural (declarative). You describe the desired target relation using set operations and relational predicates. The internal database query processor handles the physical indexing and file scanning.

**Step-by-step solution.**  
**SQL (Structured Query Language)** is the standard declarative computer language used to define, query, and manipulate data in relational database management systems (RDBMS). It was originally developed at IBM in the 1970s for System R.

Key parts of SQL include:
1. **Data Definition Language (DDL):** Defines relation schemas, integrity constraints, and indexes (`CREATE`, `ALTER`, `DROP`).
2. **Data Manipulation Language (DML):** Queries and modifies table tuples (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
3. **Data Control & Transaction Control (DCL/TCL):** Manages user permissions (`GRANT`, `REVOKE`) and transaction boundaries (`COMMIT`, `ROLLBACK`).

SQL is declarative. The user specifies what result is wanted rather than how to calculate it.

**Check.**  
*Quick self-test:*
- Q: What makes SQL declarative rather than procedural?  
  A: Users state the desired result conditions without writing algorithmic loops or index navigation procedures.
- Q: Which SQL component is used to enforce entity integrity?  
  A: DDL, through `PRIMARY KEY` and `NOT NULL` constraints inside `CREATE TABLE`.

> [!warning] Common mistakes
> - Confusing SQL with a general-purpose programming language; pure SQL does not provide branching or iteration without stored procedural extensions.
> - Omitting DDL commands and mentioning only `SELECT`.

**Exam tip.**  
For 2 marks, keep the response under 80 words. Name the language, define its declarative property, and bullet DDL, DML, and DCL/TCL.

**Sources.**  
[Deck 03 · Slides 3–4](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.1–3.2](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter

### 2017 Q.4(a) · 09 Marks

*Section A · Asked in: 2017 · L1 (asked once)*

**Question.** Considering following tables (INFO, MARKS, CREDIT) answer (i),(ii) & (iii).

<table style="border: none; border-collapse: collapse;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 15px;"><b>INFO</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>roll</th><th>name</th></tr></thead><tbody><tr><td>1710001</td><td>Amelia</td></tr><tr><td>1710002</td><td>Oliver</td></tr><tr><td>1710003</td><td>James</td></tr><tr><td>1710004</td><td>Sansa</td></tr></tbody></table></td><td style="border: none; padding-right: 15px;"><b>MARKS</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>roll</th><th>sub_code</th><th>gpa</th></tr></thead><tbody><tr><td>1710001</td><td>ECE 2205</td><td>3.50</td></tr><tr><td>1710001</td><td>ECE 2215</td><td>3.75</td></tr><tr><td>1710002</td><td>ECE 2205</td><td>3.75</td></tr><tr><td>1710002</td><td>ECE 2215</td><td>3.25</td></tr><tr><td>1710003</td><td>ECE 2205</td><td>4.00</td></tr><tr><td>1710003</td><td>ECE 2215</td><td>3.75</td></tr><tr><td>1710004</td><td>ECE 2205</td><td>3.50</td></tr><tr><td>1710004</td><td>ECE 2215</td><td>4.00</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>CREDIT</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>sub_code</th><th>credit</th></tr></thead><tbody><tr><td>ECE 2205</td><td>3.00</td></tr><tr><td>ECE 2215</td><td>3.00</td></tr></tbody></table></td></tr></table>

(i) Write down the SQL query to create the table MARKS.  
(ii) Write down the SQL query to find out subject code and corresponding gpa of the student whose class serial 02.  
(iii) Write the the SQL query to calculate the cgpa of each student using the formula, $cgpa = \frac{\Sigma gpa \cdot credit}{\Sigma credit}$

*(Note: In the original printed question paper, Q.4 contains only sub-question (a) with 09 marks indicated in the margin, leaving a 3-mark deficit from the standard 12 marks).*

**Answer.**

**What the examiner wants.**  
Three distinct SQL capabilities (3 marks each):  
1. DDL relation definition with composite primary key and foreign keys.  
2. Selection query interpreting student class serial from student roll numbers.  
3. Multi-table aggregation calculating a weighted sum ratio grouped by student.

**Key idea.**  
In relational database design, bridge tables like `MARKS` contain foreign keys pointing to independent parent entities (`INFO` and `CREDIT`). Calculating CGPA requires joining grade points with course credits, taking their products, summing them per student, and dividing by total enrolled credit units.

**Step-by-step solution.**  
*(i) Create table MARKS:*

```sql
CREATE TABLE MARKS (
    roll INT,
    sub_code VARCHAR(20),
    gpa DECIMAL(3, 2),
    PRIMARY KEY (roll, sub_code),
    FOREIGN KEY (roll) REFERENCES INFO(roll),
    FOREIGN KEY (sub_code) REFERENCES CREDIT(sub_code)
);
```

*(ii) Subject code and GPA for student with class serial 02:*

*Assumption: In the RUET roll format (e.g., 1710002), the final two digits represent the student's class serial. Class serial 02 identifies student roll 1710002 (Oliver).*

```sql
SELECT sub_code, gpa
FROM MARKS
WHERE roll = 1710002;
```

*(Alternative dynamic filter matching the last two digits:* `WHERE roll % 100 = 2;`*)*

*(iii) Calculate CGPA of each student:*

```sql
SELECT m.roll,
       SUM(m.gpa * c.credit) / SUM(c.credit) AS cgpa
FROM MARKS m
JOIN CREDIT c ON m.sub_code = c.sub_code
GROUP BY m.roll;
```

**Check.**  
*Manual trace for student Oliver (`roll = 1710002`):*
- ECE 2205: $\text{gpa} = 3.75$, $\text{credit} = 3.0 \implies \text{grade points} = 11.25$
- ECE 2215: $\text{gpa} = 3.25$, $\text{credit} = 3.0 \implies \text{grade points} = 9.75$
- $\sum (\text{gpa} \times \text{credit}) = 11.25 + 9.75 = 21.00$
- $\sum \text{credit} = 3.0 + 3.0 = 6.0$
- $\text{CGPA} = 21.00 / 6.0 = 3.50$. The query formula produces exactly this scalar result.

> [!warning] Common mistakes
> - Making `roll` alone the primary key of `MARKS`. A student enrolls in multiple courses, so `(roll, sub_code)` must form a composite primary key.
> - Computing simple average `AVG(gpa)` instead of the weighted formula $\frac{\sum (\text{gpa} \cdot \text{credit})}{\sum \text{credit}}$. When course credits differ, simple average yields incorrect CGPA.

**Exam tip.**  
Explicitly state your interpretation of "class serial 02" in one short assumption line before writing the query.

**Sources.**  
[Deck 03 · Slides 7–10, 18, 30–33](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.2, §3.4, §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2018 Q.7(a) · 04 Marks

*Section B · Asked in: 2018, 2024 (CO2) · L2 merge*

**Question (2018 Q.7(a)).** Write down the SQL queries for following operations.  
(i) Create table for student (<u>roll</u>, Name, <u>Dept</u>)  
(ii) Insert one example entry for student table  
(iii) Modify the student table to student(<u>roll</u>, Name, dept, session)  
(iv) Show the roll and name of the students of ECE department only.

**Question (2024 Q.4(b)).** Write down the SQL queries for following operations:  
i) Create table for student (<u>roll</u>, name, dept)  
ii) Insert one example entry for student tbale  
iii) Modify the student table to student (roll, name, dept, session)  
iv) Show the roll and name of the students of ECE dept only.  
*(Note: "tbale" printed verbatim in original paper; refers to table)*

**Answer.**

**What the examiner wants.**  
Four fundamental SQL operations (1 mark each):  
1. DDL `CREATE TABLE` with underlined attributes as primary key.  
2. DML `INSERT INTO` syntax.  
3. DDL `ALTER TABLE` to append a new column.  
4. DML `SELECT` with projection and equality selection predicate.

**Key idea.**  
Relational tables start with a schema definition (`CREATE`), receive tuples (`INSERT`), adapt to new requirements via schema modification (`ALTER`), and answer inquiries through projection and selection (`SELECT`).

**Step-by-step solution.**  
*(i) Create student table:*

```sql
CREATE TABLE student (
    roll INT,
    name VARCHAR(50),
    dept VARCHAR(20),
    PRIMARY KEY (roll, dept)
);
```

*(ii) Insert one example entry:*

```sql
INSERT INTO student (roll, name, dept)
VALUES (1810001, 'Rahim', 'ECE');
```

*(iii) Modify student table to add session:*

```sql
ALTER TABLE student
ADD session VARCHAR(10);
```

*(iv) Show roll and name of students from ECE:*

```sql
SELECT roll, name
FROM student
WHERE dept = 'ECE';
```

*Variant for 2024 Q.4(b) (4 marks):* The identical queries answer parts (i) through (iv).

**Check.**  
*Schema progression:*
- Initial schema: $\text{student}(\underline{\text{roll}}, \text{name}, \underline{\text{dept}})$ with 3 attributes.
- Post-ALTER schema: $\text{student}(\underline{\text{roll}}, \text{name}, \underline{\text{dept}}, \text{session})$ with 4 attributes; existing tuples receive `NULL` for `session`.
- Selection filter: Evaluates `dept = 'ECE'` and projects only `roll` and `name`.

> [!warning] Common mistakes
> - Writing `ALTER TABLE student MODIFY session ...` instead of `ADD session`. In SQL, `ADD` appends a new attribute; `MODIFY` changes an existing attribute's domain type.
> - Forgetting `PRIMARY KEY (roll, dept)` when both attributes are underlined in the question.

**Exam tip.**  
For 1-mark sub-questions, write standard SQL without superfluous clauses.

**Sources.**  
[Deck 03 · Slides 7–11, 13, 17](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.2, §3.3](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2019 Q.5(c) · 02 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Write down the SQL queries to create the following tables.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

*(Note: Printed as "SQI." and "Parient_ID" in original question paper)*

**Answer.**

**What the examiner wants.**  
Three complete `CREATE TABLE` statements demonstrating correct data type assignment, primary keys, and foreign key references linking dependent tables to the master `Patient` relation.

**Key idea.**  
`Patient` is an independent master relation. `History` and `Report` are dependent relations that track observations and test reports respectively. Because a patient can report symptoms across multiple dates, `History` requires a composite primary key `(Patient_ID, Symptom, Date)`.

**Step-by-step solution.**  
*Assumption: "Parient_ID" in the Report table is a typographical misprint for Patient_ID and serves as a foreign key referencing the Patient table.*

```sql
CREATE TABLE Patient (
    Patient_ID INT PRIMARY KEY,
    Patient_name VARCHAR(50),
    Mobile VARCHAR(15)
);

CREATE TABLE History (
    Patient_ID INT,
    Symptom VARCHAR(50),
    Date DATE,
    PRIMARY KEY (Patient_ID, Symptom, Date),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Report (
    Patient_ID INT PRIMARY KEY,
    Corona_center VARCHAR(50),
    Test_result VARCHAR(20),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);
```

**Check.**  
*Relational integrity verification:*
- Referencing tables (`History`, `Report`) define foreign keys pointing to `Patient(Patient_ID)`.
- Creation order: `Patient` must be created first before child tables execute their foreign key constraints.

> [!warning] Common mistakes
> - Setting `Patient_ID` alone as the primary key of `History`. A single patient can experience multiple symptoms on multiple dates, causing duplicate key violations unless the key is composite.
> - Leaving the printed typo `Parient_ID` unaddressed without an assumption note.

**Exam tip.**  
Always define the parent table before the referencing child tables so foreign key dependencies resolve cleanly.

**Sources.**  
[Deck 03 · Slides 7–9](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.2](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2021 Q.3(a) · 08 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** Consider the following E-comerce database:  
  client (<u>c_no</u>, name, city, state, baldue)  
  product (<u>p_no</u>, description, profit_percent, quantity, sell_price, cost_price)  
  salesman (<u>s_no</u>, name, city, state, sal_amount, target, sold_yearly, remarks)

Now write the appropriate MySql code to execute the following query:  
(i) Change the city of client no "C0005" to "Barishal".  
(ii) Delete all salesmen whose salaries are equal to 35000 Tk.  
(iii) Add a column called "Telephone" of datatype numeric and size = '11' to the client table.  
(iv) Find products whose selling price is more than 500. Calculate a new selling price as original price*15. Rename the new column in the output as new_price.

*(Note: "E-comerce" and "MySql" printed verbatim from original question paper)*

**Answer.**

**What the examiner wants.**  
Four distinct MySQL statements (2 marks each):  
1. `UPDATE` statement with `SET` and targeted `WHERE` clause.  
2. `DELETE FROM` statement with numeric equality comparison.  
3. `ALTER TABLE` statement specifying column name and data type `NUMERIC(11)`.  
4. `SELECT` statement performing arithmetic calculation and renaming using `AS`.

**Key idea.**  
MySQL adheres to ANSI SQL DDL and DML standards for row-level modifications (`UPDATE`, `DELETE`), schema evolution (`ALTER TABLE`), and calculated output expressions (`AS`).

**Step-by-step solution.**  
*(i) Change city of client "C0005" to "Barishal":*

```sql
UPDATE client
SET city = 'Barishal'
WHERE c_no = 'C0005';
```

*(ii) Delete salesmen whose salary is 35000 Tk:*

```sql
DELETE FROM salesman
WHERE sal_amount = 35000;
```

*(iii) Add column "Telephone" of numeric type and size 11 to client table:*

```sql
ALTER TABLE client
ADD Telephone NUMERIC(11);
```

*(iv) Find products with sell_price > 500 and calculate new selling price:*

```sql
SELECT p_no,
       description,
       sell_price,
       sell_price * 15 AS new_price
FROM product
WHERE sell_price > 500;
```

**Check.**  
*Statement validation:*
- Part (i): Filters on primary key `c_no = 'C0005'`, ensuring exactly one record is updated.
- Part (ii): Uses attribute `sal_amount` defined in the schema.
- Part (iii): `NUMERIC(11)` matches the requested numeric type with precision 11.
- Part (iv): Arithmetic expression `sell_price * 15` is evaluated row by row and projected under the alias `new_price`.

> [!warning] Common mistakes
> - Writing `UPDATE client SET city = 'Barishal'` without a `WHERE` clause, which overwrites the city for all clients.
> - Writing `DELETE * FROM salesman`, which is invalid SQL syntax (`DELETE FROM` does not take `*`).

**Exam tip.**  
Double check attribute names against the provided schema (`sal_amount`, not `salary`; `sell_price`, not `price`).

**Sources.**  
[Deck 03 · Slides 11, 14, 20, 54, 58](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.3, §3.4, §3.9](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2023 Q.3(a) · 06 Marks

*Section A · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** Write SQL queries for the following:  
(i) Create a table "Employee" with attributes: EmpID (primary key), Name, Age and Department.  
(ii) Insert a record into this table: EmpID=1, Name='Nafisa', Age=21, department='HR'.  
(iii) Find employees whose salary is greater than the average salary of their department.

**Answer.**

**What the examiner wants.**  
Three progressive SQL queries (2 marks each):  
1. DDL `CREATE TABLE` with primary key declaration.  
2. DML `INSERT INTO` statement with literal values.  
3. Advanced query using a correlated subquery to compare individual employee salary against their department average.

**Key idea.**  
Part (iii) requires comparing each employee's salary to an aggregate computed over a specific group (their own department). Because the inner aggregate depends on the department of the current outer tuple (`e1.Department = e2.Department`), the query must be structured as a correlated subquery.

**Step-by-step solution.**  
*(i) Create table Employee:*

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Department VARCHAR(30)
);
```

*(ii) Insert record into Employee:*

```sql
INSERT INTO Employee (EmpID, Name, Age, Department)
VALUES (1, 'Nafisa', 21, 'HR');
```

*(iii) Find employees earning more than their department's average salary:*

*Assumption: The Employee relation includes an attribute `Salary DECIMAL(10,2)`.*

```sql
SELECT *
FROM Employee e1
WHERE e1.Salary > (
    SELECT AVG(e2.Salary)
    FROM Employee e2
    WHERE e2.Department = e1.Department
);
```

**Check.**  
*Trace of correlated execution:*
- For an employee `e1` in the 'HR' department earning 40,000:
  The inner query computes `AVG(Salary)` for all employees where `Department = 'HR'`.
  If the HR average is 32,000, `40000 > 32000` evaluates to true, and `e1` is included in the output.
- The inner query re-evaluates dynamically for each distinct department encountered in the outer scan.

> [!warning] Common mistakes
> - Writing an uncorrelated subquery `WHERE Salary > (SELECT AVG(Salary) FROM Employee)`. That calculates the company-wide average salary, ignoring departmental differences.
> - Not stating an assumption about the missing `Salary` attribute in the printed schema.

**Exam tip.**  
When an attribute requested by a query is missing from the problem's own schema definition, declare an assumption line immediately.

**Sources.**  
[Deck 03 · Slides 7, 52, 56](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.2, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### CT-02 Q.01(a) · 02 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(a)** Display all students from the ECE department.

**Answer.**

**What the examiner wants.**  
Basic single-relation selection and projection in SQL. Full marks for correct `SELECT *` (or all attributes) and equality filter `WHERE Department = 'ECE'`.

**Key idea.**  
The `WHERE` clause acts as the relational selection operator ($\sigma$), filtering table tuples according to the boolean expression.

**Step-by-step solution.**  
```sql
SELECT *
FROM STUDENT
WHERE Department = 'ECE';
```

**Check.**  
*Execution:* The DBMS scans `STUDENT` and checks each row's `Department` column against the string literal `'ECE'`. Only matching tuples appear in the result table.

> [!warning] Common mistakes
> - Omitting quotes around string literal `'ECE'`. Without quotes, SQL treats `ECE` as an attribute name.

**Exam tip.**  
For simple CT queries, write clean standard SQL without unnecessary clauses.

**Sources.**  
[Deck 03 · Slide 17](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.3](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.3 · Basic query clauses: DISTINCT, ORDER BY, AS, LIKE

*See also:* Finals counted inside [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter]] (2021 Q.3(a)(iv) `AS new_price`), [[#T05.5 · Aggregation queries: GROUP BY + HAVING, CGPA, extremes without LIMIT]] (2019 Q.7(a)(ii) `LIKE 'A%'`), and [[#T05.8 · Short notes: ON DELETE CASCADE, GROUP BY, ORDER BY, AS]] (2024 Q.7(b)(iii–iv) `ORDER BY` and `AS`).

### CT-02 Q.01(b) · 02 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(b)** Display students from the ECE department whose CGPA is greater than 3.50, arranged by CGPA in descending order.

**Answer.**

**What the examiner wants.**  
A multi-condition `WHERE` clause combining department match and numeric threshold using logical `AND`, followed by sorting using `ORDER BY ... DESC`.

**Key idea.**  
SQL evaluates the `WHERE` filter first to select tuples belonging to ECE with CGPA > 3.50. It then processes the `ORDER BY` clause to arrange the surviving tuples from highest to lowest CGPA.

**Step-by-step solution.**  
```sql
SELECT *
FROM STUDENT
WHERE Department = 'ECE' AND CGPA > 3.50
ORDER BY CGPA DESC;
```

**Check.**  
*Trace with candidate records:*
- Student 1: ECE, CGPA = 3.80 $\implies$ passes `WHERE`, placed top in output.
- Student 2: ECE, CGPA = 3.60 $\implies$ passes `WHERE`, placed second in output.
- Student 3: CSE, CGPA = 3.90 $\implies$ rejected by `Department = 'ECE'`.
- Student 4: ECE, CGPA = 3.40 $\implies$ rejected by `CGPA > 3.50`.

> [!warning] Common mistakes
> - Writing `DESCENDING` instead of the SQL keyword `DESC`.
> - Placing `ORDER BY` before the `WHERE` clause (violating SQL grammatical order).

**Exam tip.**  
Remember the strict clause sequence: `SELECT` $\to$ `FROM` $\to$ `WHERE` $\to$ `ORDER BY`.

**Sources.**  
[Deck 03 · Slides 17, 24](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.3, §3.6](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

## T05.4 · Aggregate functions (theory)

### 2019 Q.8(a) · 04 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Discuss about four aggregate functions.

**Answer.**

**What the examiner wants.**  
A clear definition of what an aggregate function is in SQL, followed by four distinct functions (`COUNT`, `SUM`, `AVG`, `MIN`/`MAX`) with their purpose, allowed data types, and a brief SQL example (1 mark per function).

**Key idea.**  
Unlike scalar operations that transform each row independently, aggregate functions collapse an entire column (or group of rows) into a single scalar value. SQL aggregate functions automatically ignore null values, with the single exception of `COUNT(*)`.

**Step-by-step solution.**  
An **aggregate function** takes a collection (multiset) of values from a specified attribute and computes a single summarizing scalar value. SQL ignores null values during aggregation (except for `COUNT(*)`).

Four standard aggregate functions:

1. **`COUNT()`:**  
   Computes the number of tuples or non-null attribute values.
   - `COUNT(*)` counts all rows in the relation, including duplicates and nulls.
   - `COUNT(A)` counts non-null values of attribute $A$.
   - *Example:* Count total instructors:
     ```sql
     SELECT COUNT(*) FROM instructor;
     ```

2. **`SUM()`:**  
   Computes the arithmetic sum of all non-null values in a numeric column.
   - *Example:* Total salary paid to all instructors:
     ```sql
     SELECT SUM(salary) FROM instructor;
     ```

3. **`AVG()`:**  
   Computes the arithmetic mean of all non-null values in a numeric column.
   - *Example:* Average salary of instructors in the ECE department:
     ```sql
     SELECT AVG(salary) FROM instructor WHERE dept_name = 'ECE';
     ```

4. **`MIN()` and `MAX()`:**  
   Finds the minimum and maximum values in a column respectively. They operate on numbers, text strings, and dates.
   - *Example:* Lowest and highest salary in the institution:
     ```sql
     SELECT MIN(salary) AS min_sal, MAX(salary) AS max_sal FROM instructor;
     ```

**Check.**  
*Quick self-test:*
- Q: How does `COUNT(*)` differ from `COUNT(dept_name)`?  
  A: `COUNT(*)` returns the total row count including rows with null values, while `COUNT(dept_name)` counts only rows where `dept_name` is non-null.
- Q: What happens if `AVG(salary)` is applied to an empty table?  
  A: It returns `NULL`.

> [!warning] Common mistakes
> - Stating that `COUNT(*)` ignores null values; `COUNT(*)` counts all tuples regardless of attribute nullability.
> - Trying to apply `SUM()` or `AVG()` to character or string attributes.

**Exam tip.**  
For theory aggregate questions, always write the mathematical purpose and one line of valid SQL for each function.

**Sources.**  
[Deck 03 · Slides 30–31](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2024 Q.7(a) · 03 Marks

*Section B · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** Define aggregated functions.  
EMPLOYEE (EID, Name, Department, Salary)  
SALES (SID, EID, SaleAmount, SaleDate)  
The management wants to reward the top-earing department. Write a SQL query to find the total salary paid per department.  
*(Note: "top-earing" printed verbatim in original paper; refers to top-earning)*

**Answer.**

**What the examiner wants.**  
Formal definition of aggregate functions (1 mark) and a concise `GROUP BY` aggregation query calculating total departmental salary from the `EMPLOYEE` table (2 marks).

**Key idea.**  
When a summary value must be calculated for each category (each department), the query groups records by the category column and applies the `SUM` aggregate function to the grouped partitions.

**Step-by-step solution.**  
**Definition:** An **aggregate function** is a built-in SQL function that takes a collection of values across a column (or within subsets defined by `GROUP BY`) and returns a single summarizing scalar value. Standard SQL provides five primary aggregate functions: `AVG`, `MIN`, `MAX`, `SUM`, and `COUNT`.

**Query:**

```sql
SELECT Department,
       SUM(Salary) AS Total_Salary
FROM EMPLOYEE
GROUP BY Department;
```

**Check.**  
*Trace with sample rows:*
- Employee 1: Dept = 'ECE', Salary = 50,000
- Employee 2: Dept = 'ECE', Salary = 60,000
- Employee 3: Dept = 'CSE', Salary = 70,000  
`GROUP BY Department` forms two partitions:
- 'ECE': `SUM(Salary) = 110,000`
- 'CSE': `SUM(Salary) = 70,000`  
Result matches the desired output.

> [!warning] Common mistakes
> - Including non-aggregated attributes in `SELECT` (such as `Name` or `EID`) without including them in `GROUP BY`.
> - Unnecessarily joining the `SALES` table when the question asks for total salary paid per department (salary resides entirely in `EMPLOYEE`).

**Exam tip.**  
Only join extra tables (`SALES`) if the question explicitly requires attributes from both tables.

**Sources.**  
[Deck 03 · Slides 30–32](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.5 · Aggregation queries: GROUP BY + HAVING, CGPA, extremes without LIMIT

*See also:* 2017 Q.4(a)(iii) in [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter]], 2020 Q.3(b)(i) in [[#T05.7 · Multi-table business-schema query sets (MySQL): Covid, Company, Insurance, E-commerce]], and 2024 Q.7(a) in [[#T05.4 · Aggregate functions (theory)]].

### 2018 Q.7(b) · 08 Marks

*Section B · Asked in: 2018 · L1 (asked once)*

**Question.** Consider the following data tables:

`Product (p_id, p_name, quantity, unit_price)`  
`Customer (c_id, c_name, contact)`  
`Sales (c_id, p_id, quantity)`

Write down SQL expressions for following queries.  
(i) Show the information of those customers who have bought more than five different products.  
(ii) Show the information of those products that were sold more than ten pieces.  
(iii) Show the information of the product with maximum sale (maximum sold amount of money or bought by the maximum customer).  
(iv) Show the product id and corresponding remaining quantity of that product.

**Answer.**

**What the examiner wants.**  
Four complex business queries (2 marks each):  
1. Grouping customers and filtering on distinct product count using `HAVING COUNT(DISTINCT ...) > 5`.  
2. Grouping products and filtering on total quantity sold using `HAVING SUM(quantity) > 10`.  
3. Aggregation query identifying the top-selling product by total monetary value (or customer reach).  
4. Remaining inventory query requiring a `LEFT JOIN` and `COALESCE` to prevent unsold products from disappearing.

**Key idea.**  
`HAVING` filters aggregated groups after `GROUP BY`, whereas `WHERE` filters individual rows prior to grouping. For inventory tracking, unsold products have no matching rows in `Sales`. An inner join drops them, so an outer join (`LEFT JOIN`) with `COALESCE(SUM(s.quantity), 0)` is required to report full starting stock for unsold items.

**Step-by-step solution.**  
*(i) Customers who bought more than five different products:*

```sql
SELECT c.c_id, c.c_name, c.contact
FROM Customer c
JOIN Sales s ON c.c_id = s.c_id
GROUP BY c.c_id, c.c_name, c.contact
HAVING COUNT(DISTINCT s.p_id) > 5;
```

*(ii) Products sold more than ten pieces:*

```sql
SELECT p.p_id, p.p_name, p.quantity, p.unit_price
FROM Product p
JOIN Sales s ON p.p_id = s.p_id
GROUP BY p.p_id, p.p_name, p.quantity, p.unit_price
HAVING SUM(s.quantity) > 10;
```

*(iii) Product with maximum sale:*

*Primary interpretation: Maximum sold amount of money ($\sum (\text{quantity} \times \text{unit\_price})$):*

```sql
SELECT p.p_id, p.p_name, p.quantity, p.unit_price,
       SUM(s.quantity * p.unit_price) AS total_sales_value
FROM Product p
JOIN Sales s ON p.p_id = s.p_id
GROUP BY p.p_id, p.p_name, p.quantity, p.unit_price
ORDER BY total_sales_value DESC
LIMIT 1;
```

*(Alternative subquery without `LIMIT` to return all tied products on top revenue):*

```sql
SELECT p.p_id, p.p_name, p.quantity, p.unit_price
FROM Product p
JOIN Sales s ON p.p_id = s.p_id
GROUP BY p.p_id, p.p_name, p.quantity, p.unit_price
HAVING SUM(s.quantity * p.unit_price) = (
    SELECT MAX(prod_rev)
    FROM (
        SELECT SUM(s2.quantity * p2.unit_price) AS prod_rev
        FROM Sales s2
        JOIN Product p2 ON s2.p_id = p2.p_id
        GROUP BY s2.p_id
    ) AS sub
);
```

*Alternative interpretation: Bought by the maximum number of distinct customers:*

```sql
SELECT p.p_id, p.p_name, p.quantity, p.unit_price,
       COUNT(DISTINCT s.c_id) AS customer_count
FROM Product p
JOIN Sales s ON p.p_id = s.p_id
GROUP BY p.p_id, p.p_name, p.quantity, p.unit_price
ORDER BY customer_count DESC
LIMIT 1;
```

*(iv) Product ID and corresponding remaining quantity:*

```sql
SELECT p.p_id,
       p.quantity - COALESCE(SUM(s.quantity), 0) AS remaining_quantity
FROM Product p
LEFT JOIN Sales s ON p.p_id = s.p_id
GROUP BY p.p_id, p.quantity;
```

**Check.**  
*Trace of part (iv) inventory calculation:*
- Product A: Initial `quantity = 100`. Sold 20 in `Sales`. `SUM = 20`. `Remaining = 100 - 20 = 80`.
- Product B: Initial `quantity = 50`. Never sold. `Sales` row is `NULL`. `COALESCE(NULL, 0) = 0`. `Remaining = 50 - 0 = 50`.
- An inner join would have discarded Product B entirely. The `LEFT JOIN` preserves Product B.

> [!warning] Common mistakes
> - Using `COUNT(s.p_id)` instead of `COUNT(DISTINCT s.p_id)` in part (i); a customer buying the same product 6 times did not buy 5 *different* products.
> - Using an `INNER JOIN` in part (iv); unsold products disappear from the report instead of displaying their intact warehouse quantity.
> - Filtering grouped aggregations in `WHERE` instead of `HAVING` (e.g., `WHERE SUM(quantity) > 10` is an immediate syntax error).

**Exam tip.**  
Whenever an inventory problem asks for remaining quantity, always write a `LEFT JOIN` with `COALESCE` to account for unsold inventory items.

**Sources.**  
[Deck 03 · Slides 32–34, 48–51](../LectureSlides/03_Introduction_to_SQL.md), [Deck 04 · Slides 5–7](../LectureSlides/04_Joining_and_Views.md), [Textbook Ch. 3 §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2019 Q.7(a) · 12 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Considering the following data tables (Student, GPA, Credits) answer (i), (ii), (iii), & (iv).

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Student</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>St Name</th></tr></thead><tbody><tr><td>2010001</td><td>Abdullah</td></tr><tr><td>2010002</td><td>Ahmad</td></tr><tr><td>2010003</td><td>Mohammad</td></tr><tr><td>2010004</td><td>Muaz</td></tr><tr><td>2010005</td><td>Minhaz</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>GPA</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>Sub_Code</th><th>gpa</th></tr></thead><tbody><tr><td>2010001</td><td>ECE-1103</td><td>3.00</td></tr><tr><td>2010002</td><td>ECE-1107</td><td>3.25</td></tr><tr><td>2010004</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010005</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010003</td><td>ECE-1107</td><td>3.75</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Credit</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>Sub_Code</th><th>Credit</th></tr></thead><tbody><tr><td>ECE-1103</td><td>3.00</td></tr><tr><td>ECE-1107</td><td>3.00</td></tr></tbody></table></td></tr></table>  
(i) Write down the SQL query to show the list of students who got the lowest gpa.  
(ii) Write down the SQL query to find out the registered subjects of those students whose name started with "A".  
(iii) Write the SQL query to calculate the cgpa of each student using the formula,

$\displaystyle cgpa = \frac{\sum gpa \cdot Credit}{\sum Credit}$

(iv) Generate a list showing each subject code and corresponding highest gpa.

*(Note: In sub-question (i), printed as "SQI." in original question paper)*

**Answer.**

**What the examiner wants.**  
Four distinct queries testing fundamental SQL patterns (3 marks each):  
1. Extreme value query using a scalar subquery `WHERE gpa = (SELECT MIN(gpa) ...)`.  
2. Pattern matching using `LIKE 'A%'` joined across tables.  
3. Weighted arithmetic average aggregation grouped by student identity.  
4. Simple group aggregation using `MAX(gpa)` grouped by subject code.

**Key idea.**  
Examining extreme values (lowest GPA) without hardcoding requires a subquery to locate the dynamic minimum. Calculating CGPA requires joining three tables (`Student`, `GPA`, `Credit`) so that course credits and grade points align by subject code while grouping by student.

**Step-by-step solution.**  
*(i) List of students who got the lowest GPA:*

```sql
SELECT s.St_ID, s.`St Name`, g.Sub_Code, g.gpa
FROM Student s
JOIN GPA g ON s.St_ID = g.St_ID
WHERE g.gpa = (
    SELECT MIN(gpa)
    FROM GPA
);
```

*(ii) Registered subjects of students whose name starts with "A":*

```sql
SELECT DISTINCT s.St_ID, s.`St Name`, g.Sub_Code
FROM Student s
JOIN GPA g ON s.St_ID = g.St_ID
WHERE s.`St Name` LIKE 'A%';
```

*(iii) Calculate CGPA of each student:*

```sql
SELECT s.St_ID, s.`St Name`,
       SUM(g.gpa * c.Credit) / SUM(c.Credit) AS cgpa
FROM Student s
JOIN GPA g ON s.St_ID = g.St_ID
JOIN Credit c ON g.Sub_Code = c.Sub_Code
GROUP BY s.St_ID, s.`St Name`;
```

*(iv) Each subject code and corresponding highest GPA:*

```sql
SELECT Sub_Code,
       MAX(gpa) AS highest_gpa
FROM GPA
GROUP BY Sub_Code;
```

**Check.**  
*Verification against the provided table data:*
- Part (i): Minimum GPA in the `GPA` table is 3.00. Subquery returns 3.00. Result: `(2010001, 'Abdullah', 'ECE-1103', 3.00)`.
- Part (ii): Students whose name starts with 'A' are Abdullah (`2010001`) and Ahmad (`2010002`). Registered subjects: Abdullah $\implies$ ECE-1103; Ahmad $\implies$ ECE-1107.
- Part (iii): Since each subject carries 3.00 credits, $\frac{gpa \times 3.0}{3.0} = gpa$. CGPA equals individual GPA values.
- Part (iv): For ECE-1103, GPAs are 3.00, 4.00, 4.00 $\implies$ max is 4.00. For ECE-1107, GPAs are 3.25, 3.75 $\implies$ max is 3.75.

> [!warning] Common mistakes
> - Hardcoding `WHERE gpa = 3.00` in part (i); the query must compute dynamically using `(SELECT MIN(gpa) FROM GPA)`.
> - Writing `WHERE s.St_Name = 'A%'` instead of using the `LIKE` operator.
> - Forgetting backticks around attribute names containing spaces (`` `St Name` ``).

**Exam tip.**  
When column names contain spaces in the question paper, wrap them in backticks (`` `St Name` ``) in MySQL to maintain valid syntax.

**Sources.**  
[Deck 03 · Slides 22, 30–33, 35](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.4, §3.7, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2024 Q.1(c) · 04 Marks

*Section A · CO2 · Asked in: 2024 · L1 (asked once)*

**Question.**  
STUDENT (SID, Name, Age, Major)  
COURSE (CID, Title, Credits)  
ENROLLMENT (SID, CID, Grade)  
Using the above schema, write a SQL query to find the average grade for each course.

**Answer.**

**What the examiner wants.**  
A clean SQL aggregation query using `AVG(Grade)` grouped by course identifier (`CID`).

**Key idea.**  
The `ENROLLMENT` table contains both the course identifier (`CID`) and the student's grade (`Grade`). Grouping by `CID` allows `AVG()` to compute the arithmetic mean per course without requiring a join to other relations.

**Step-by-step solution.**  
```sql
SELECT CID,
       AVG(Grade) AS avg_grade
FROM ENROLLMENT
GROUP BY CID;
```

*(If course title is also retrieved by joining COURSE):*

```sql
SELECT c.CID, c.Title,
       AVG(e.Grade) AS avg_grade
FROM COURSE c
JOIN ENROLLMENT e ON c.CID = e.CID
GROUP BY c.CID, c.Title;
```

**Check.**  
*Trace:*
- If CID 'ECE2215' has three enrollment records with grades 3.5, 3.75, and 4.0, `AVG(Grade)` yields $\frac{3.5 + 3.75 + 4.0}{3} = 3.75$.
- Output relation contains `(CID, avg_grade)`.

> [!warning] Common mistakes
> - Joining `STUDENT` unnecessarily; `STUDENT` attributes are not required to compute course averages.
> - Omitting `GROUP BY CID`; without `GROUP BY`, `AVG(Grade)` computes the grand average across all courses combined into a single number.

**Exam tip.**  
Provide the direct single-table query first; append the joined version with `Title` as an alternative if descriptive course names are desired.

**Sources.**  
[Deck 03 · Slides 30–32](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### CT-02 Q.01(d) · 03 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(d)** Display the students having the second-highest CGPA without using LIMIT.

**Answer.**

**What the examiner wants.**  
Querying the second-highest numeric value using subqueries without relying on vendor-specific pagination keywords (`LIMIT` or `TOP`).

**Key idea.**  
The second-highest value in a set is the maximum value strictly less than the overall maximum value. Once that scalar value is determined by a nested subquery, the outer query retrieves all student records matching that CGPA.

**Step-by-step solution.**  
```sql
SELECT *
FROM STUDENT
WHERE CGPA = (
    SELECT MAX(CGPA)
    FROM STUDENT
    WHERE CGPA < (
        SELECT MAX(CGPA)
        FROM STUDENT
    )
);
```

*Note on ties:* This query identifies the unique second-highest distinct CGPA value. If multiple students share this exact second-highest CGPA, all tied students are displayed in the result.

**Check.**  
*Trace with sample values:*
Suppose CGPA values in `STUDENT` are: `{4.00, 4.00, 3.85, 3.85, 3.70}`.
1. Innermost subquery: `SELECT MAX(CGPA) FROM STUDENT` $\implies 4.00$.
2. Intermediate subquery: `SELECT MAX(CGPA) FROM STUDENT WHERE CGPA < 4.00` $\implies 3.85$.
3. Outer query: `SELECT * FROM STUDENT WHERE CGPA = 3.85`.
Both students with CGPA 3.85 are returned. A naive `ORDER BY ... LIMIT 1 OFFSET 1` would have returned the second student with 4.00, failing to locate the true second-highest grade.

> [!warning] Common mistakes
> - Using `LIMIT 1 OFFSET 1` when the prompt explicitly bans `LIMIT`.
> - Writing `WHERE CGPA < (SELECT MAX(CGPA))` without finding the `MAX` of that reduced subset, which would retrieve all students except the top one.

**Exam tip.**  
Nested `MAX` subqueries are the universal, standard-compliant way to find $n$-th highest values without vendor-specific extensions.

**Sources.**  
[Deck 03 · Slides 35, 52](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.7, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.6 · Subqueries theory ("two examples"): IN, SOME/ALL, EXISTS, scalar, correlated, WITH

*See also:* 2023 Q.3(a)(iii) in [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter]] asks for a correlated subquery (*salary > average salary of their department*).

### 2024 Q.6(a) · 04 Marks

*Section B · CO2 · Asked in: 2024, 2019 · L2 merge*

**Question (2024 Q.6(a)).** Explain sub-queries with two suitable examples.

**Question (2019 Q.8(b)).** Write down two examples of using sub-queries.

**Answer.**

**What the examiner wants.**  
A conceptual explanation of what a subquery is in SQL, followed by two well-structured, distinct query examples (e.g., set membership `IN` and scalar aggregate comparison) with explanations of how the inner and outer queries interact (2 marks for theory/structure, 1 mark per example).

**Key idea.**  
A subquery embeds one `SELECT` statement inside another. Instead of writing multiple separate programs to retrieve intermediate data, a subquery passes intermediate sets or single scalar values directly to the outer query's predicates.

**Step-by-step solution.**  
**Explanation:** A **subquery** (or nested query) is a `SELECT` statement embedded inside another SQL statement (the outer query). It can appear in the `WHERE` clause to filter tuples, in the `FROM` clause as a temporary derived relation, or in the `SELECT` clause as a scalar expression. Subqueries allow multi-step data retrieval in a single query.

**Example 1: Set Membership Subquery (`IN`)**  
Find all courses offered in Fall 2017 that were also offered in Spring 2018:

```sql
SELECT DISTINCT course_id
FROM section
WHERE semester = 'Fall' AND year = 2017
  AND course_id IN (
      SELECT course_id
      FROM section
      WHERE semester = 'Spring' AND year = 2018
  );
```

The inner subquery generates the set of courses running in Spring 2018. The outer query checks whether Fall 2017 courses belong to that generated set.

**Example 2: Scalar Comparison Subquery (`AVG`)**  
Find instructors whose salary is higher than the average salary of all instructors:

```sql
SELECT name, salary
FROM instructor
WHERE salary > (
    SELECT AVG(salary)
    FROM instructor
);
```

The inner query computes a single numeric value (the overall average salary). The outer query evaluates the `>` predicate against this scalar value for each instructor.

*Variant for 2019 Q.8(b) (4 marks):* Presenting the two SQL examples with their purpose answers the question.

**Check.**  
*Execution mechanisms:*
- In Example 1 (`IN`), the subquery produces a unary relation $\{c_1, c_2, \dots\}$. The outer query performs membership testing ($t \in R$).
- In Example 2 (`scalar`), the subquery reduces to a single numerical value (e.g., 65,000). The outer query compares each instructor's salary attribute directly against this scalar.

> [!warning] Common mistakes
> - Giving two examples that use the exact same clause (e.g., two `IN` queries); examiners expect diverse constructs (such as `IN` alongside a scalar comparison or `EXISTS`).
> - Forgetting that a scalar subquery must return exactly one column and at most one row when used with comparison operators (`>`, `=`, `<`).

**Exam tip.**  
Pair one set membership example (`IN`) with one aggregate scalar example (`AVG`) to demonstrate broad SQL competence.

**Sources.**  
[Deck 03 · Slides 35–43, 52](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### CT-02 Q.01(c) · 03 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(c)** Find students whose CGPA is greater than the overall average CGPA.

**Answer.**

**What the examiner wants.**  
An uncorrelated scalar subquery using `AVG(CGPA)` in a `WHERE` comparison predicate.

**Key idea.**  
In SQL, aggregate functions cannot be placed directly in a `WHERE` clause (e.g., `WHERE CGPA > AVG(CGPA)` is invalid syntax). The aggregate must be evaluated inside a nested subquery, which computes the table-wide average and supplies it as a scalar value to the outer query.

**Step-by-step solution.**  
```sql
SELECT *
FROM STUDENT
WHERE CGPA > (
    SELECT AVG(CGPA)
    FROM STUDENT
);
```

**Check.**  
*Trace:*
If student CGPA values are $\{3.2, 3.5, 3.8, 3.9\}$, the subquery evaluates:
$\text{AVG(CGPA)} = \frac{3.2 + 3.5 + 3.8 + 3.9}{4} = 3.60$.
The outer query evaluates `CGPA > 3.60`, returning the students with 3.8 and 3.9.

> [!warning] Common mistakes
> - Writing `WHERE CGPA > AVG(CGPA)` directly without `SELECT`; SQL parser throws a syntax error because aggregates are not permitted in `WHERE` predicates of the same query block.

**Exam tip.**  
Wrap the aggregate calculation in a `(SELECT AVG(...) FROM ...)` subquery whenever comparing an attribute to a dataset-wide summary.

**Sources.**  
[Deck 03 · Slides 30, 35, 52](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.7, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.7 · Multi-table business-schema query sets (MySQL): Covid, Company, Insurance, E-commerce

### 2019 Q.5(b) · 08 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Consider the following relational database.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

Now write down the SQL (Not Algebra) to find out the following queries.  
(i) Find the names of those patients who have-fever symptom.  
(ii) Consider that if any patient has high fever symptom he/she will be suspected as corona patient. Find out such maximum number of patients in a date.  
(iii) Find out the mobile numbers of those patients who have provided samples in Rajshahi corona center and their results have become positive.  
(iv) Find out the name of those patients who have high fever symptom but test result have become negative.

*(Note: In the physical question paper, SECTION-B heading and Q.5(a)–(b) appear at the bottom of Page 1; Q.5(c) continues at the top of Page 2)*  
*(Note: Printed as "Parient_ID" in Report schema in original question paper; refers to "Patient_ID")*

**Answer.**

**What the examiner wants.**  
Four relational database queries across medical tracking relations (2 marks each):  
1. String pattern matching (`LIKE '%fever%'`) across joined tables.  
2. Two-level aggregation: first grouping and counting suspected patients per date, then extracting the maximum count using a derived table.  
3. Multi-table join filtering by clinic location and positive test result.  
4. Three-table join identifying patients with high fever symptoms whose laboratory test returned negative.

**Key idea.**  
Part (ii) requires finding the peak daily suspect count. Since standard SQL does not allow nested aggregate functions like `MAX(COUNT(*))`, the daily counts must be computed inside a subquery in the `FROM` clause, after which `MAX()` is applied to the derived column.

**Step-by-step solution.**  
*Assumption: "Parient_ID" in the Report table is a typographical misprint for Patient_ID and joins with Patient.Patient_ID.*

*(i) Names of patients who have fever symptom:*

```sql
SELECT DISTINCT p.Patient_name
FROM Patient p
JOIN History h ON p.Patient_ID = h.Patient_ID
WHERE h.Symptom LIKE '%fever%';
```

*(ii) Maximum number of high-fever patients recorded on a single date:*

```sql
SELECT MAX(daily_count) AS max_patients
FROM (
    SELECT Date, COUNT(DISTINCT Patient_ID) AS daily_count
    FROM History
    WHERE Symptom = 'high fever'
    GROUP BY Date
) AS daily_summary;
```

*(Alternative returning the specific date with the peak count:* `SELECT Date, COUNT(DISTINCT Patient_ID) AS patient_count FROM History WHERE Symptom = 'high fever' GROUP BY Date ORDER BY patient_count DESC LIMIT 1;`*)*

*(iii) Mobile numbers of patients tested in Rajshahi corona center with positive result:*

```sql
SELECT DISTINCT p.Mobile
FROM Patient p
JOIN Report r ON p.Patient_ID = r.Parient_ID
WHERE r.Corona_center = 'Rajshahi'
  AND r.Test_result = 'positive';
```

*(iv) Names of patients with high fever symptom whose test result is negative:*

```sql
SELECT DISTINCT p.Patient_name
FROM Patient p
JOIN History h ON p.Patient_ID = h.Patient_ID
JOIN Report r ON p.Patient_ID = r.Parient_ID
WHERE h.Symptom = 'high fever'
  AND r.Test_result = 'negative';
```

**Check.**  
*Trace with sample medical records:*
- Date '2020-04-01' has 3 distinct patients with 'high fever'.
- Date '2020-04-02' has 5 distinct patients with 'high fever'.
- The inner derived table in part (ii) yields rows `('2020-04-01', 3)` and `('2020-04-02', 5)`.
- The outer `MAX(daily_count)` evaluates to 5.

> [!warning] Common mistakes
> - Writing `SELECT MAX(COUNT(Patient_ID))` directly; nesting aggregate functions inside a single `SELECT` clause is invalid SQL syntax.
> - Forgetting `DISTINCT` in patient name projections; if a patient has multiple fever entries, their name repeats unless `DISTINCT` is specified.

**Exam tip.**  
When an aggregate of an aggregate is needed, wrap the initial `GROUP BY` query in the `FROM` clause with an alias (e.g., `FROM (...) AS daily_summary`).

**Sources.**  
[Deck 03 · Slides 18, 22, 30–32, 48–49](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.4, §3.7, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2020 Q.3(b) · 10 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Consider the following company database schema.  
  employee(<u>ssn</u>, fname, lname, DoB, Address, Sex, Salary, dept_no)  
  department(<u>dnumber</u>, dname, mgr_ssn, mgr_start_date)  
  dept_location(<u>dnumber</u>, <u>dlocation</u>)  
  project(<u>pnumber</u>, pname, dnum)  
  works_on(<u>essn</u>, <u>pno</u>, hours)  
  dependent(<u>essn</u>, <u>dependent_name</u>, Sex, DoB, relationship)  
Now write down the MySQL query for the followings.  
(i) For each department whose average salary is more than \$30,000, retrieve the department_name and the number of employees working for that department.  
(ii) Find the names of all employees who are working on project number "5" and are from the same department.  
(iii) Find the number of dependent people of those employees who are from "H&R" department.

**Answer.**

**What the examiner wants.**  
Three enterprise-schema queries (parts (i) and (ii) worth ~3.5 marks, part (iii) worth ~3 marks):  
1. Grouping by department, counting employees, and filtering with `HAVING AVG(Salary) > 30000`.  
2. Joining employee, assignment (`works_on`), and project tables while enforcing that the employee's department matches the project's controlling department (`dnum`).  
3. Counting dependents across joined tables for employees in a specific named department ('H&R').

**Key idea.**  
Complex relational databases separate entities into normalized tables. Queries require traversing relationships: employee to department via `dept_no = dnumber`, employee to project via `works_on`, and employee to dependents via `essn = ssn`.

**Step-by-step solution.**  
*(i) Department name and employee count for departments with average salary > \$30,000:*

```sql
SELECT d.dname AS department_name,
       COUNT(e.ssn) AS number_of_employees
FROM department d
JOIN employee e ON d.dnumber = e.dept_no
GROUP BY d.dnumber, d.dname
HAVING AVG(e.Salary) > 30000;
```

*(ii) Names of employees working on project 5 who belong to the department controlling project 5:*

*Assumption: "from the same department" means the employee's department matches the department controlling project 5 (e.dept_no = p.dnum).*

```sql
SELECT e.fname, e.lname
FROM employee e
JOIN works_on w ON e.ssn = w.essn
JOIN project p ON w.pno = p.pnumber
WHERE p.pnumber = 5
  AND e.dept_no = p.dnum;
```

*(iii) Total number of dependents for employees in the "H&R" department:*

```sql
SELECT COUNT(dp.dependent_name) AS total_dependents
FROM dependent dp
JOIN employee e ON dp.essn = e.ssn
JOIN department d ON e.dept_no = d.dnumber
WHERE d.dname = 'H&R';
```

**Check.**  
*Trace of part (ii):*
- Employee A (`dept_no = 1`) works on Project 5 (`dnum = 1`). `1 = 1` matches $\implies$ included.
- Employee B (`dept_no = 2`) works on Project 5 (`dnum = 1`). `2 = 1` does not match $\implies$ excluded (working on the project from a different department).
The predicate `e.dept_no = p.dnum` correctly enforces departmental affiliation.

> [!warning] Common mistakes
> - Putting `AVG(e.Salary) > 30000` in the `WHERE` clause instead of `HAVING`.
> - Counting `COUNT(*)` in part (iii) when using a `LEFT JOIN`; if an employee has zero dependents, `COUNT(*)` would count 1 row for that employee. Using `COUNT(dp.dependent_name)` correctly counts 0.
> - Missing the department match condition `e.dept_no = p.dnum` in part (ii).

**Exam tip.**  
When a question says "from the same department" regarding a project, connect the employee's `dept_no` with the project's controlling department attribute `dnum`.

**Sources.**  
[Deck 03 · Slides 18–19, 30–34](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.4, §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2020 Q.7(b) · 08 Marks

*Section B · Asked in: 2020, 2024 (CO2) · L2 merge*

**Question (2020 Q.7(b)).** Define RDMS. Consider the following insurance database where the primary keys are underlined.  
  Person(<u>driver_id</u>, name, address)  
  Car(<u>license</u>, model, year)  
  Accident(<u>report_no</u>, date, location)  
  Owner(driver_id, license)  
  Participated(driver_id, report_no, car, damage_amount)  
Write MySQL for the following queries-  
(i) Find the number of accidents in which the cars belonging to "John Smith" were involved.  
(ii) Add a new accident to the database, assuming any values for required attributes.  
(iii) Update the car "Mazda" belonging to "John".  
(iv) Update the damage amounts \$3000 for the car with license number "YJK-100" in the accident with report number "APR2197".  
*(Note: Printed as "RDMS" in original question paper; refers to "RDBMS")*

**Question (2024 Q.5(b)).** Define RDMS. Consider the following insurance database where the primary keys are underlined.  
Person (<u>driver_id</u>, name, address)  
Car (<u>license</u>, model, year)  
Accident (<u>report_no</u>, data, location)  
Owner (driver_id, license)  
Participated (driver_id, report_no, car, damage_amount)  
Write MySQL for the following queries –  
i) Find the number of accidents in which the cars belonging to “John Smith” were involved.  
ii) Add a new accident to the database, assuming any values for required attributes.  
iii) Update the car “Mazda” belonging to “John”.  
iv) Update the damage amounts \$3000 for the car with license number “YJK-100” in the accident with report number “APR2197”.  
*(Note: "RDMS" and "data" printed verbatim in original paper; refers to RDBMS and date)*

**Answer.**

**What the examiner wants.**  
Definition of RDBMS (printed as "RDMS", ~2 marks) followed by four distinct SQL statements (1.5 marks each in 2020; 1 mark each in 2024):  
1. Aggregation counting distinct accident reports for vehicles registered to John Smith.  
2. `INSERT INTO Accident` statement with sample literals.  
3. Multi-table `UPDATE` statement modifying a vehicle record through an ownership join.  
4. Targeted `UPDATE` statement setting damage amounts on a composite primary key match.

**Key idea.**  
In an insurance database, vehicle ownership (`Owner`) is distinct from accident participation (`Participated`). John Smith's car could be driven by someone else during an accident; joining `Participated.car` to `Owner.license` links accidents back to the car's owner.

**Step-by-step solution.**  
**Definition of RDBMS:** An **RDBMS (Relational Database Management System)** is a database management software based on the relational model of data. It stores information in tables (relations) of rows and columns, enforces data integrity using keys and constraints, and provides a structured declarative query language (SQL) for retrieval and manipulation.

*(i) Number of accidents involving cars owned by "John Smith":*

```sql
SELECT COUNT(DISTINCT p.report_no) AS accident_count
FROM Participated p
JOIN Owner o ON p.car = o.license
JOIN Person per ON o.driver_id = per.driver_id
WHERE per.name = 'John Smith';
```

*(ii) Add a new accident with sample values:*

```sql
INSERT INTO Accident (report_no, date, location)
VALUES ('AR-2024-01', '2024-10-15', 'Dhaka-Rajshahi Highway');
```

*(iii) Update the car "Mazda" belonging to "John":*

*Assumption: The query updates the manufacturing year of John's Mazda to 2022.*

```sql
UPDATE Car c
JOIN Owner o ON c.license = o.license
JOIN Person p ON o.driver_id = p.driver_id
SET c.year = 2022
WHERE p.name = 'John'
  AND c.model = 'Mazda';
```

*(Alternative standard SQL subquery:*
```sql
UPDATE Car
SET year = 2022
WHERE model = 'Mazda'
  AND license IN (
      SELECT o.license
      FROM Owner o
      JOIN Person p ON o.driver_id = p.driver_id
      WHERE p.name = 'John'
  );
```
*)*

*(iv) Update damage amount to \$3,000 for car "YJK-100" in accident "APR2197":*

```sql
UPDATE Participated
SET damage_amount = 3000
WHERE car = 'YJK-100'
  AND report_no = 'APR2197';
```

*Variant for 2024 Q.5(b) (6 marks):* The same RDBMS definition and four queries directly solve the question.

**Check.**  
*Validation of part (i):*
- If John Smith owns a car that was involved in an accident with two other cars, `Participated` has multiple rows with the same `report_no`.
- `COUNT(DISTINCT p.report_no)` counts that accident exactly once rather than overcounting.

> [!warning] Common mistakes
> - Joining `Participated.driver_id` directly to `Person.driver_id` in part (i); that queries accidents where John Smith was the *driver*, whereas the prompt specifically states "cars belonging to John Smith" (ownership).
> - Leaving part (iii) unwritten because the attribute to update is unspecified. Always write an assumption setting a realistic attribute like `year` or `model`.

**Exam tip.**  
MySQL natively supports multi-table `UPDATE ... JOIN ... SET` syntax; showing both the MySQL join update and the standard SQL `IN` subquery covers all grading rubrics.

**Sources.**  
[Deck 03 · Slides 18, 30, 56, 58–59](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.4, §3.9](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).

---

### 2021 Q.4(a) · 12 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** Consider the following E-comerce database:  
  client (<u>c_no</u>, name, city, state, Baldue)  
  product (<u>p_no</u>, description, profit_percent, quantity, sell_price, cost_price)  
  salesman (<u>s_no</u>, name, city, state, sal_amount, target, sold_yearly, remarks)  
  order (<u>order_no</u>, client_no, order_date, delivery_address, salesman_no, del_type, del_date, order_status)  
  order_details (<u>order_no</u>, product_no, quantity_ordered, product_rate)

(i) Find the total value of each product sold.  
(ii) Find the products and their quantities for the orders placed by client no "C0001" and "C0002".  
(iii) Find the product no and description of the products not being sold.  
(iv) Find if the product "Lyera Top" has been ordered by any client and print the client_no, name to whom it was sold.

*(Note: "E-comerce" and "Lyera Top" printed verbatim from original question paper)*

**Answer.**

**What the examiner wants.**  
Four comprehensive queries on a five-table sales database (3 marks each):  
1. Grouped total value calculation ($\sum \text{quantity\_ordered} \times \text{product\_rate}$).  
2. Multi-table join filtering by multiple client keys using `IN ('C0001', 'C0002')`.  
3. Unsold product retrieval using set difference / anti-join (`NOT IN` or `NOT EXISTS`).  
4. Multi-table join across four tables (`client`, `order`, `order_details`, `product`) filtering on a specific product description string.

**Key idea.**  
In MySQL, the table name `order` is a reserved SQL keyword and must be escaped with backticks (`` `order` ``). Unsold products exist in `product` but have zero entries in `order_details`, making `NOT IN` or `NOT EXISTS` the appropriate selection mechanism.

**Step-by-step solution.**  
*(i) Total value of each product sold:*

```sql
SELECT od.product_no,
       p.description,
       SUM(od.quantity_ordered * od.product_rate) AS total_value
FROM order_details od
JOIN product p ON od.product_no = p.p_no
GROUP BY od.product_no, p.description;
```

*(ii) Products and quantities ordered by client "C0001" and "C0002":*

```sql
SELECT o.client_no,
       od.product_no,
       p.description,
       od.quantity_ordered
FROM `order` o
JOIN order_details od ON o.order_no = od.order_no
JOIN product p ON od.product_no = p.p_no
WHERE o.client_no IN ('C0001', 'C0002');
```

*(iii) Product number and description of products not sold:*

```sql
SELECT p_no, description
FROM product
WHERE p_no NOT IN (
    SELECT DISTINCT product_no
    FROM order_details
);
```

*(Alternative using `NOT EXISTS`:*
```sql
SELECT p.p_no, p.description
FROM product p
WHERE NOT EXISTS (
    SELECT 1
    FROM order_details od
    WHERE od.product_no = p.p_no
);
```
*)*

*(iv) Check if "Lyera Top" was ordered and display client number and name:*

```sql
SELECT DISTINCT c.c_no, c.name
FROM client c
JOIN `order` o ON c.c_no = o.client_no
JOIN order_details od ON o.order_no = od.order_no
JOIN product p ON od.product_no = p.p_no
WHERE p.description = 'Lyera Top';
```

**Check.**  
*Trace of part (iii) anti-join:*
- Suppose `product` has keys $\{P01, P02, P03\}$.
- Suppose `order_details` records sales for $\{P01, P02\}$.
- The subquery `SELECT DISTINCT product_no FROM order_details` returns $\{P01, P02\}$.
- `WHERE p_no NOT IN ({P01, P02})` evaluates to true only for $P03$. Product $P03$ is correctly reported.

> [!warning] Common mistakes
> - Writing `FROM order` without backticks in MySQL; `ORDER` is a reserved keyword for `ORDER BY` and triggers a parse error.
> - Using an `INNER JOIN` between `product` and `order_details` in part (iii); an inner join only matches sold products and can never find unsold products.
> - Altering the printed spelling "Lyera Top" in part (iv); keep the exact string literal from the question paper.

**Exam tip.**  
Always escape SQL reserved keywords like `` `order` `` with backticks when used as table or column names in MySQL.

**Sources.**  
[Deck 03 · Slides 18, 30–32, 36, 46](../LectureSlides/03_Introduction_to_SQL.md), [Textbook Ch. 3 §3.4, §3.7, §3.8](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md).


---

## T05.8 · Short notes: ON DELETE CASCADE, GROUP BY, ORDER BY, AS

### 2024 Q.7(b) · 04 Marks

*Section B · CO1 · Asked in: 2024, 2019, 2023 (CLO2) · L2 merge*

**Question (2024 Q.7(b)).** Write short note on the following statements –  
i) ON CASCADE DELETE  
ii) Group By  
iii) Order By  
iv) As

**Question (2019 Q.8(c)).** Write short note on the following statements.  
(i) ON CASCADE DELETE.  
(ii) Group By.

**Question (2023 Q.6(c)).** Write short note on " ON CASCADE DELETE".

**Answer.**

**What the examiner wants.**  
Concise technical descriptions, purpose, and standard SQL syntax/examples for four fundamental SQL clauses and constraint actions (1 mark each).

**Key idea.**  
Each term serves a distinct role in relational data management: `ON DELETE CASCADE` governs referential integrity maintenance; `GROUP BY` partitions data for summary aggregation; `ORDER BY` controls output presentation order; `AS` introduces aliasing for projection expressions and relation names.

**Step-by-step solution.**  
**i) ON DELETE CASCADE (printed as "ON CASCADE DELETE"):**  
A foreign key referential integrity action. When a tuple in the parent table is deleted, the DBMS automatically deletes all corresponding referencing tuples in the child table. This maintains referential integrity and prevents orphaned records.

```sql
CREATE TABLE section (
    course_id VARCHAR(8),
    sec_id VARCHAR(8),
    semester VARCHAR(6),
    year NUMERIC(4, 0),
    PRIMARY KEY (course_id, sec_id, semester, year),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
        ON DELETE CASCADE
);
```

**ii) GROUP BY:**  
An SQL clause used to partition table rows into distinct groups having identical values in specified columns. Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) then compute summary statistics for each individual group.

```sql
SELECT dept_name, AVG(salary) AS avg_sal
FROM instructor
GROUP BY dept_name;
```

**iii) ORDER BY:**  
An SQL clause that sorts query result rows in ascending (`ASC`, default) or descending (`DESC`) order based on one or more attributes. Multiple sort keys break ties sequentially.

```sql
SELECT name, salary
FROM instructor
ORDER BY salary DESC, name ASC;
```

**iv) AS:**  
An SQL keyword used to define an alias (an alternative temporary name). It can rename an attribute or computed expression in the `SELECT` clause for readability, or rename a table in the `FROM` clause to shorten table references and enable self-joins.

```sql
SELECT salary * 1.15 AS revised_salary
FROM employee AS e;
```

*Short version for 2019 Q.8(c) (4 marks):* Provide parts (i) and (ii).  
*Short version for 2023 Q.6(c) (2 marks):* Provide part (i) with definition, syntax, and effect.

**Check.**  
*Referential trace of `ON DELETE CASCADE`:*
- Department 'Biology' exists in parent table `department`.
- Three courses in child table `course` have `dept_name = 'Biology'`.
- Deleting 'Biology' from `department` via `DELETE FROM department WHERE dept_name = 'Biology'` automatically removes the three referencing courses from `course`.

> [!warning] Common mistakes
> - Confusing `ON DELETE CASCADE` with `ON DELETE SET NULL`; cascading drops the entire referencing row, whereas `SET NULL` updates the referencing foreign key column to `NULL`.
> - Assuming `AS` permanently alters attribute names in physical storage; `AS` renames items only within the output result relation.

**Exam tip.**  
For short notes on SQL statements, always supply both the formal definition and a minimal code snippet illustrating syntax.

**Sources.**  
[Deck 03 · Slides 8, 20, 24, 32](../LectureSlides/03_Introduction_to_SQL.md), [Deck 04 · Slide 4](../LectureSlides/04_Joining_and_Views.md), [Textbook Ch. 3 §3.4, §3.6, §3.7](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md), [Textbook Ch. 4 §4.4.5](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md).

---

## T05.9 · TRUNCATE vs DELETE

### 2023 Q.6(a) · 02 Marks

*Section B · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** What is the difference between 'Truncate' and 'Delete' in SQL?

**Answer.**

**What the examiner wants.**  
Direct architectural and operational comparison between `TRUNCATE` and `DELETE` in SQL (especially in MySQL), addressing command category (DDL vs DML), filtering capability, rollback/transaction semantics, triggers, auto-increment counter handling, and performance.

**Key idea.**  
`DELETE` is a row-level DML statement that individually removes tuples, checks constraints, fires triggers, and writes extensive undo logs for each deleted row. `TRUNCATE` is a table-level DDL statement that drops and recreates the data storage pages directly, bypassing row-level trigger logic and running substantially faster with minimal logging.

**Step-by-step solution.**  
Both `TRUNCATE` and `DELETE` remove rows from a relation, but they operate at different architectural levels:

| Feature | `TRUNCATE TABLE` | `DELETE FROM` |
| :--- | :--- | :--- |
| **Command Category** | **DDL** (Data Definition Language) | **DML** (Data Manipulation Language) |
| **Row Filtering (`WHERE`)** | Not supported; always empties the entire table | Supported; deletes specific filtered rows or all rows |
| **Transaction & Rollback** | Executes an implicit `COMMIT` in MySQL; cannot be rolled back | Logged row-by-row; can be rolled back inside a transaction |
| **Triggers** | Does not fire `DELETE` triggers | Fires `BEFORE DELETE` and `AFTER DELETE` triggers for each row |
| **`AUTO_INCREMENT` Counter** | Resets the auto-increment counter back to its starting value (1) | Preserves the current auto-increment counter sequence |
| **Execution Speed** | Extremely fast; deallocates data pages directly | Slower; scans rows and records individual undo/redo logs |

**Check.**  
*Quick self-test:*
- Q: Can you execute `TRUNCATE TABLE student WHERE dept = 'ECE'`?  
  A: No, `TRUNCATE` has no `WHERE` clause; attempting to provide one causes a syntax error.
- Q: If a table has an auto-increment column at 150 and you execute `DELETE FROM table`, what will the next inserted row's ID be?  
  A: 151. If `TRUNCATE TABLE` were used instead, it would reset to 1.

> [!warning] Common mistakes
> - Stating that `TRUNCATE` is a DML statement. In SQL and MySQL, `TRUNCATE` is classified as DDL.
> - Believing that `TRUNCATE` can be undone with `ROLLBACK` in MySQL; MySQL DDL statements execute an immediate implicit commit.

**Exam tip.**  
A concise 6-row comparison table is the fastest, cleanest way to secure full 2/2 marks on this question.

**Sources.**  
[Textbook Ch. 3 §3.9](../Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md), MySQL 8.0 Reference Manual (§13.1.37 `TRUNCATE TABLE`, §13.2.2 `DELETE`).

---

[← Prev: T04 · Relational Algebra and Calculus](T04_Relational_Algebra_and_Calculus.md) | [Exam-style layer](../Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T06 · Joins and Views →](T06_Joins_and_Views.md)
