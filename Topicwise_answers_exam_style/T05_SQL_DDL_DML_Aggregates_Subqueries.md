---
title: "T05 · SQL (DDL, DML, Aggregates, Subqueries) · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T04 · Relational Algebra and Calculus](T04_Relational_Algebra_and_Calculus.md) | [Explanation layer](../Topicwise_answers_explaination/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T06 · Joins and Views →](T06_Joins_and_Views.md)

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

**SQL (Structured Query Language)** is the standard declarative computer language used to define, query, and manipulate data in relational database management systems (RDBMS). It was originally developed at IBM in the 1970s for System R.

Key parts of SQL include:
1. **Data Definition Language (DDL):** Defines relation schemas, integrity constraints, and indexes (`CREATE`, `ALTER`, `DROP`).
2. **Data Manipulation Language (DML):** Queries and modifies table tuples (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
3. **Data Control & Transaction Control (DCL/TCL):** Manages user permissions (`GRANT`, `REVOKE`) and transaction boundaries (`COMMIT`, `ROLLBACK`).

SQL is declarative. The user specifies what result is wanted rather than how to calculate it.


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

---

### 2019 Q.5(c) · 02 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Write down the SQL queries to create the following tables.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

*(Note: Printed as "SQI." and "Parient_ID" in original question paper)*

**Answer.**

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

---

### 2023 Q.3(a) · 06 Marks

*Section A · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** Write SQL queries for the following:  
(i) Create a table "Employee" with attributes: EmpID (primary key), Name, Age and Department.  
(ii) Insert a record into this table: EmpID=1, Name='Nafisa', Age=21, department='HR'.  
(iii) Find employees whose salary is greater than the average salary of their department.

**Answer.**

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

---

### CT-02 Q.01(a) · 02 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(a)** Display all students from the ECE department.

**Answer.**

```sql
SELECT *
FROM STUDENT
WHERE Department = 'ECE';
```


---

## T05.3 · Basic query clauses: DISTINCT, ORDER BY, AS, LIKE

*See also:* Finals counted inside [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter]] (2021 Q.3(a)(iv) `AS new_price`), [[#T05.5 · Aggregation queries: GROUP BY + HAVING, CGPA, extremes without LIMIT]] (2019 Q.7(a)(ii) `LIKE 'A%'`), and [[#T05.8 · Short notes: ON DELETE CASCADE, GROUP BY, ORDER BY, AS]] (2024 Q.7(b)(iii–iv) `ORDER BY` and `AS`).

### CT-02 Q.01(b) · 02 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(b)** Display students from the ECE department whose CGPA is greater than 3.50, arranged by CGPA in descending order.

**Answer.**

```sql
SELECT *
FROM STUDENT
WHERE Department = 'ECE' AND CGPA > 3.50
ORDER BY CGPA DESC;
```

---

## T05.4 · Aggregate functions (theory)

### 2019 Q.8(a) · 04 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Discuss about four aggregate functions.

**Answer.**

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

---

### 2024 Q.7(a) · 03 Marks

*Section B · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** Define aggregated functions.  
EMPLOYEE (EID, Name, Department, Salary)  
SALES (SID, EID, SaleAmount, SaleDate)  
The management wants to reward the top-earing department. Write a SQL query to find the total salary paid per department.  
*(Note: "top-earing" printed verbatim in original paper; refers to top-earning)*

**Answer.**

**Definition:** An **aggregate function** is a built-in SQL function that takes a collection of values across a column (or within subsets defined by `GROUP BY`) and returns a single summarizing scalar value. Standard SQL provides five primary aggregate functions: `AVG`, `MIN`, `MAX`, `SUM`, and `COUNT`.

**Query:**

```sql
SELECT Department,
       SUM(Salary) AS Total_Salary
FROM EMPLOYEE
GROUP BY Department;
```


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

---

### 2019 Q.7(a) · 12 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Considering the following data tables (Student, GPA, Credits) answer (i), (ii), (iii), & (iv).

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Student</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>St Name</th></tr></thead><tbody><tr><td>2010001</td><td>Abdullah</td></tr><tr><td>2010002</td><td>Ahmad</td></tr><tr><td>2010003</td><td>Mohammad</td></tr><tr><td>2010004</td><td>Muaz</td></tr><tr><td>2010005</td><td>Minhaz</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>GPA</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>Sub_Code</th><th>gpa</th></tr></thead><tbody><tr><td>2010001</td><td>ECE-1103</td><td>3.00</td></tr><tr><td>2010002</td><td>ECE-1107</td><td>3.25</td></tr><tr><td>2010004</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010005</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010003</td><td>ECE-1107</td><td>3.75</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>Credit</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>Sub_Code</th><th>Credit</th></tr></thead><tbody><tr><td>ECE-1103</td><td>3.00</td></tr><tr><td>ECE-1107</td><td>3.00</td></tr></tbody></table></td></tr></table>  
(i) Write down the SQL query to show the list of students who got the lowest gpa.  
(ii) Write down the SQL query to find out the registered subjects of those students whose name started with "A".  
(iii) Write the SQL query to calculate the cgpa of each student using the formula,

$\displaystyle cgpa = \frac{\sum gpa \cdot Credit}{\sum Credit}$

(iv) Generate a list showing each subject code and corresponding highest gpa.

*(Note: In sub-question (i), printed as "SQI." in original question paper)*

**Answer.**

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

---

### 2024 Q.1(c) · 04 Marks

*Section A · CO2 · Asked in: 2024 · L1 (asked once)*

**Question.**  
STUDENT (SID, Name, Age, Major)  
COURSE (CID, Title, Credits)  
ENROLLMENT (SID, CID, Grade)  
Using the above schema, write a SQL query to find the average grade for each course.

**Answer.**

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

---

### CT-02 Q.01(d) · 03 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(d)** Display the students having the second-highest CGPA without using LIMIT.

**Answer.**

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


---

## T05.6 · Subqueries theory ("two examples"): IN, SOME/ALL, EXISTS, scalar, correlated, WITH

*See also:* 2023 Q.3(a)(iii) in [[#T05.2 · DDL + DML warm-up: CREATE, INSERT, ALTER ... ADD, UPDATE, DELETE, rename, filter]] asks for a correlated subquery (*salary > average salary of their department*).

### 2024 Q.6(a) · 04 Marks

*Section B · CO2 · Asked in: 2024, 2019 · L2 merge*

**Question (2024 Q.6(a)).** Explain sub-queries with two suitable examples.

**Question (2019 Q.8(b)).** Write down two examples of using sub-queries.

**Answer.**

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

---

### CT-02 Q.01(c) · 03 Marks

*CO2 · Asked in: CT-02 · L1 (asked once)*

**Question.** Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(c)** Find students whose CGPA is greater than the overall average CGPA.

**Answer.**

```sql
SELECT *
FROM STUDENT
WHERE CGPA > (
    SELECT AVG(CGPA)
    FROM STUDENT
);
```


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

---

## T05.9 · TRUNCATE vs DELETE

### 2023 Q.6(a) · 02 Marks

*Section B · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** What is the difference between 'Truncate' and 'Delete' in SQL?

**Answer.**

Both `TRUNCATE` and `DELETE` remove rows from a relation, but they operate at different architectural levels:

| Feature | `TRUNCATE TABLE` | `DELETE FROM` |
| :--- | :--- | :--- |
| **Command Category** | **DDL** (Data Definition Language) | **DML** (Data Manipulation Language) |
| **Row Filtering (`WHERE`)** | Not supported; always empties the entire table | Supported; deletes specific filtered rows or all rows |
| **Transaction & Rollback** | Executes an implicit `COMMIT` in MySQL; cannot be rolled back | Logged row-by-row; can be rolled back inside a transaction |
| **Triggers** | Does not fire `DELETE` triggers | Fires `BEFORE DELETE` and `AFTER DELETE` triggers for each row |
| **`AUTO_INCREMENT` Counter** | Resets the auto-increment counter back to its starting value (1) | Preserves the current auto-increment counter sequence |
| **Execution Speed** | Extremely fast; deallocates data pages directly | Slower; scans rows and records individual undo/redo logs |

---

[← Prev: T04 · Relational Algebra and Calculus](T04_Relational_Algebra_and_Calculus.md) | [Explanation layer](../Topicwise_answers_explaination/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Next: T06 · Joins and Views →](T06_Joins_and_Views.md)
