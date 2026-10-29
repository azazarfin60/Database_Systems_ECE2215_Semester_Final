# T05: SQL (DDL, DML, Aggregates, Subqueries) — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 4 | `subtopicwise_list.md` T05 (130 marks · 20.4% · 7/7 · 🔴)  
**Source Pages:** Pages 2–10, 15–17

---

## 1. SQL Syntax Basics & Simple Queries

<!-- Page 2 (Left, Right) -->
<!-- CLASS-01 | 29.06.2024 | HAFSA MAM -->

```sql
SELECT * FROM Customers;
```
* `SELECT` $\rightarrow$ keyword
* `*` $\rightarrow$ All columns/data of table
* `Customers` $\rightarrow$ Table name
* `FROM` $\rightarrow$ Query execution begins here (specifies source relation)

```sql
SELECT Customername FROM Customers;
```

> [!NOTE]
> SQL keywords are **case insensitive** (`SELECT` = `select` = `Select`).

### DISTINCT & COUNT DISTINCT:
* `SELECT DISTINCT` $\rightarrow$ Extracts unique data (removes duplicate rows from the output).
* Default `SELECT` does not remove duplicates (preserves all matching rows).

```sql
-- Extract unique countries
SELECT DISTINCT Country FROM Customers;

-- Count unique countries
SELECT COUNT(DISTINCT Country) FROM Customers;

-- Count unique districts
SELECT COUNT(DISTINCT District) FROM Customers;
```

---

## 2. WHERE Filtering & Comparison Operators

<!-- Page 3 (Left, Right) & Page 4 (Left) -->

The `WHERE` clause specifies search conditions to filter rows:
* **Operators available:** `=`, `>`, `<`, `>=`, `<=`, `<>`, `BETWEEN ... AND ...`, `LIKE`, `IN`

```sql
SELECT * FROM Customers
WHERE Country = 'MEXICO';

SELECT COUNT(DISTINCT District)
FROM Customers
WHERE District = 'DHAKA';

-- BETWEEN operator
SELECT * FROM Products
WHERE Price BETWEEN 50 AND 60;

SELECT Name FROM Students
WHERE CTmarks BETWEEN 10 AND 15;

-- Compound conditions (AND, OR)
SELECT * FROM Customers
WHERE Country = 'GERMAN' AND (City = 'BERLIN' OR City = 'Stuttgart');
```

### Sorting with ORDER BY:
```sql
SELECT * FROM Customers
ORDER BY Price;
```
* **Default order:** Ascending (lowest to highest).
* **Descending order:** Append `DESC`.

```sql
SELECT Name FROM Students
WHERE CTmarks BETWEEN 10 AND 15
ORDER BY Roll;

SELECT * FROM Customers
ORDER BY Price DESC;
```

---

## 3. DDL: Database & Table Creation and Modification

<!-- Page 5 (Left, Right) -->
<!-- CLASS-02 | 27.06.2024 -->

### Creating Databases & Tables:
```sql
CREATE DATABASE school;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    CT1 FLOAT,
    CT2 FLOAT
);

-- Alternative schema discussed in lecture:
-- CREATE TABLE students (
--     student_id INT PRIMARY KEY,
--     name VARCHAR(50),
--     age INT,
--     grade CHAR(2)
-- );
```

### Data Insertion:
```sql
INSERT INTO students (student_id, name, CT1, CT2)
VALUES (35, 'Raidah', 15, 16),
       (36, 'Oishe', 15, 16);
```
* To insert values for all columns in declared order, column names can be omitted.
* *Note:* Since `student_id` is defined as `INT`, standard SQL uses unquoted numeric literals (`35, 36`). If preserving formatted strings with leading zeros (e.g., `'035'`) is desired, declare `student_id` as `VARCHAR(10)` or `CHAR(10)`.

### Altering Table Structures (`ALTER TABLE`):
```sql
-- 1. Add a new column
ALTER TABLE students
ADD COLUMN email VARCHAR(100);

-- 2. Modify an existing column's data type (assumes 'age' column exists from alternative schema)
ALTER TABLE students
MODIFY COLUMN age INT NOT NULL;
-- or:
-- ALTER TABLE students MODIFY COLUMN age FLOAT NOT NULL;

-- 3. Rename a column (assumes 'grade' column exists)
ALTER TABLE students
CHANGE COLUMN grade student_grade CHAR(2);

-- 4. Drop a column
ALTER TABLE students
DROP COLUMN email;
```

### Dropping Tables & Databases:
```sql
DROP TABLE students;
DROP DATABASE school;
```

---

## 4. SQL NULL Values, UPDATE & DELETE

<!-- Page 6 (Left, Right) -->

### Handling NULL Values:
* `NULL` represents missing, unknown, or inapplicable values.
* Never use `= NULL`; always use `IS NULL` or `IS NOT NULL`.

```sql
SELECT column_name
FROM table_name
WHERE column_name IS NULL;
```

### Modifying Records (`UPDATE`):
```sql
UPDATE Customers
SET customer_name = 'Raidah', city = 'Mym'
WHERE customerID = 1;
```

### Deleting Records (`DELETE`):
```sql
DELETE FROM table_name
WHERE condition;
```

### Limiting Results:
```sql
-- SQL Server syntax:
SELECT TOP 3 * FROM Customer;

-- MySQL syntax:
SELECT * FROM Customer LIMIT 3;
```

---

## 5. Comprehensive Practice Problem: Employee Database

<!-- Page 7 (Right) through Page 10 (Left) -->
<!-- CLASS-03 | 29.06.2024 -->

### Given Relation: `Employee`
| emp_id (PK) | name | department | salary | city |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Alice | IT | 5000 | Dhaka |
| 2 | Bob | HR | 4000 | Chittagong |
| 3 | Carol | IT | 6000 | Dhaka |
| 4 | David | FINANCE | 7000 | Sylhet |
| 5 | Eva | HR | 4500 | Dhaka |

```sql
-- Q1: Show name and salary of all employees
SELECT name, salary FROM Employee;

-- Q2: Show all employees who work in the IT Dept
SELECT * FROM Employee
WHERE department = 'IT';

-- Q3: Show employees whose salary is greater than 4500
SELECT * FROM Employee
WHERE salary > 4500;

-- Q4: List all employees ordered by salary from highest to lowest
SELECT * FROM Employee
ORDER BY salary DESC;

-- Q5: Update Bob's salary to 4800
UPDATE Employee
SET salary = 4800
WHERE name = 'Bob';

-- Q6: Give all IT department employees a 10% raise
UPDATE Employee
SET salary = salary * 1.10
WHERE department = 'IT';

-- Q7: Delete the employee with emp_id = 1
DELETE FROM Employee
WHERE emp_id = 1;

-- Q8: Add a new employee: Farhan, Finance dept, salary 5500, city Dhaka
-- If emp_id is auto-incrementing:
INSERT INTO Employee (name, department, salary, city)
VALUES ('Farhan', 'Finance', 5500, 'Dhaka');
-- If emp_id requires manual PK specification:
-- INSERT INTO Employee (emp_id, name, department, salary, city)
-- VALUES (6, 'Farhan', 'Finance', 5500, 'Dhaka');

-- Q9: Show all employees in IT dept AND salary > 5000
SELECT * FROM Employee
WHERE department = 'IT' AND salary > 5000;

-- Q10: Show employees who live in Dhaka OR work in Finance
SELECT * FROM Employee
WHERE city = 'Dhaka' OR department = 'Finance';

-- Q11: Show employees whose salary is between 4000 and 6000
SELECT * FROM Employee
WHERE salary BETWEEN 4000 AND 6000;

-- Q12: Show employees whose name starts with 'A' or 'C'
SELECT * FROM Employee
WHERE name LIKE 'A%' OR name LIKE 'C%';

-- Q13: How many employees are in HR dept?
SELECT COUNT(emp_id) FROM Employee
WHERE department = 'HR';

-- Q14: Find average salary across all employees
SELECT AVG(salary) AS avg_salary FROM Employee;

-- Q15: Find maximum and minimum salaries
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM Employee;
-- (or separately: SELECT MAX(salary) FROM Employee; SELECT MIN(salary) FROM Employee;)

-- Q16: Give 500 raise to HR employees earning less than 4500
UPDATE Employee
SET salary = salary + 500
WHERE salary < 4500 AND department = 'HR';

-- Q17: Delete employees in Finance dept who live in Sylhet
DELETE FROM Employee
WHERE department = 'Finance' AND city = 'Sylhet';

-- Q18: Show total salary paid to each department
SELECT department, SUM(salary)
FROM Employee
GROUP BY department;
```

---

## 6. Advanced SQL: Types, Patterns & Set Operations

<!-- Page 15 (Left, Right) -->
<!-- CLASS-06 | 15.07.2024 & CLASS-08 | 25.07.2024 -->

### Domain Types:
* `numeric(p, d)`: Precision $p$ specifies total digits; scale $d$ specifies digits after decimal.
  * E.g., `numeric(5, 2)` can store `700.50` ($3$ integer digits, $2$ decimal digits).

### String Matching with `LIKE`:
* `%` matches any substring.
* `_` matches any single character.
* **Escaping wildcards:** To match a literal `'100%'`, specify an escape character:
```sql
SELECT * FROM table_name
WHERE column_name LIKE '100\%' ESCAPE '\';
```

### Set Operations:
* `UNION` / `UNION ALL`: Combines relations (Union-compatible). `UNION ALL` retains duplicate tuples.
* `INTERSECT` / `INTERSECT ALL`: Set intersection.
* `EXCEPT` / `EXCEPT ALL`: Set difference.

### Aggregates with `HAVING`:
* `HAVING` specifies conditions on entire aggregate groups (applied **after** `GROUP BY`, unlike `WHERE` which filters individual tuples before grouping).

### Nested Subqueries (`SOME` / `ALL`):
* `> SOME (...)`: True if condition holds for at least one element.
* `> ALL (...)`: True only if condition holds for all elements.

---

## 7. Correlated Subqueries & EXISTS

<!-- Page 16 (Left) -->

Given `section` relation:
| course_id | sec_id | semester | year |
| :--- | :--- | :--- | :--- |
| 101 | 1 | Fall | 2017 |
| 102 | 1 | Fall | 2017 |
| 103 | 1 | Fall | 2017 |
| 104 | 1 | Spring | 2017 |
| 101 | 1 | Spring | 2018 |
| 105 | 1 | Spring | 2018 |
| 103 | 1 | Spring | 2018 |

Find courses taught in both Fall 2017 and Spring 2018:
```sql
SELECT course_id FROM section AS S
WHERE semester = 'Fall' AND year = 2017 AND
EXISTS (
    SELECT * FROM section AS T
    WHERE semester = 'Spring' AND year = 2018 AND S.course_id = T.course_id
);
```
* **Evaluation logic:**
  1. Outer query iterates through `section AS S` for `semester = 'Fall' AND year = 2017` (courses `101`, `102`, `103`).
  2. For each outer row, the inner correlated query searches `section AS T` for `semester = 'Spring' AND year = 2018 AND S.course_id = T.course_id`.
  3. `EXISTS` returns `TRUE` if the inner subquery returns at least one tuple:
     - For `course_id = 101`: Match exists in Spring 2018 $\implies$ **`TRUE`** (Selected).
     - For `course_id = 102`: No match in Spring 2018 (course 102 was not offered in Spring 2018) $\implies$ **`FALSE`** (Discarded).
     - For `course_id = 103`: Match exists in Spring 2018 $\implies$ **`TRUE`** (Selected).
  4. Final selected courses: **`(101, 103)`**.

---

## 8. Universal Quantification with NOT EXISTS & EXCEPT

<!-- Page 16 (Right) -->

Find all students who have taken all courses offered in the Biology department:
```sql
SELECT S.ID, S.name
FROM student AS S
WHERE NOT EXISTS (
    (SELECT course_id FROM course WHERE dept_name = 'Biology')
    EXCEPT
    (SELECT T.course_id FROM takes AS T WHERE T.ID = S.ID)
);
```

### Detailed Evaluation Mechanism:
* Outer subquery computes: $( \text{All Biology courses} )$.
* Inner subquery computes: $( \text{Courses taken by current student } S )$.
* Set difference: $( \text{Biology courses} ) - ( \text{Courses taken by } S )$.
* **Case 1 (Student Rahim):** Rahim has taken all Biology courses.
  $$\text{Biology courses} - \text{Rahim's courses} = \emptyset \quad (\text{Empty / NULL set})$$
  * `NOT EXISTS` receives an empty set and evaluates to **`TRUE`** $\rightarrow$ **Rahim is selected!**
* **Case 2 (Student Karim):** Karim missed at least one Biology course.
  $$\text{Biology courses} - \text{Karim's courses} \neq \emptyset$$
  * `NOT EXISTS` receives a non-empty set and evaluates to **`FALSE`** $\rightarrow$ **Karim is NOT selected.**
* **General Rule:** `NOT EXISTS` selects a tuple only when the inner subquery returns an empty set.

---

## 9. Set Containment & Complex Queries

<!-- Page 17 (Left, Right) -->

* **Set Containment Principle:**
  $$X - Y = \emptyset \iff X \subseteq Y$$
* **`UNIQUE` Construct:** Evaluates to true if no duplicate tuples exist in the subquery result.

### Practice Schema:
**Student:**
| student_ID | name | dept | semester |
| :--- | :--- | :--- | :--- |
| 101 | Rahim | CSE | 3 |
| 102 | Karim | EEE | 4 |
| 103 | Nabila | CSE | 5 |
| 104 | Sumaiya | ECE | 3 |
| 105 | Hasan | EEE | 5 |
| 106 | Rafi | CSE | 4 |

**Enrollment:**
| student_ID | course_ID | course_name | Marks |
| :--- | :--- | :--- | :--- |
| 101 | C101 | DS | 82 |
| 102 | E101 | CT | 75 |
| 103 | C101 | DS | 81 |
| 104 | E102 | DE | 78 |
| 105 | E101 | CT | 88 |
| 106 | C102 | OS | 85 |

```sql
-- 1. Find the name and student ID of the student who obtained the highest marks:
-- (a) Using JOIN:
SELECT S.name, S.student_ID
FROM Student AS S
JOIN Enrollment AS E ON S.student_ID = E.student_ID
WHERE E.Marks = (SELECT MAX(Marks) FROM Enrollment);

-- (b) Alternative using Nested Subquery (without JOIN):
-- SELECT name, student_ID
-- FROM Student
-- WHERE student_ID IN (
--     SELECT student_ID FROM Enrollment
--     WHERE Marks = (SELECT MAX(Marks) FROM Enrollment)
-- );

-- 2. Find the ID and name of students whose marks are greater than average of all:
-- Note: DISTINCT avoids duplicate student rows if a student scored above average in multiple courses.
SELECT DISTINCT S.student_ID, S.name
FROM Student AS S
JOIN Enrollment AS E ON S.student_ID = E.student_ID
WHERE E.Marks > (SELECT AVG(Marks) FROM Enrollment);

-- Alternative using Subquery:
-- SELECT student_ID, name
-- FROM Student
-- WHERE student_ID IN (
--     SELECT student_ID FROM Enrollment
--     WHERE Marks > (SELECT AVG(Marks) FROM Enrollment)
-- );

-- 3. Find the name and dept of students enrolled in the course 'DS':
SELECT DISTINCT S.name, S.dept
FROM Student AS S
JOIN Enrollment AS E ON S.student_ID = E.student_ID
WHERE E.course_name = 'DS';

-- Alternative using Subquery:
-- SELECT name, dept
-- FROM Student
-- WHERE student_ID IN (
--     SELECT student_ID FROM Enrollment
--     WHERE course_name = 'DS'
-- );

-- 4. Find ID, course name and marks of students with marks greater than ID 102:
-- Note: In this instance, student 102 has only one course (Marks = 75).
SELECT student_ID, course_name, Marks
FROM Enrollment
WHERE Marks > (SELECT Marks FROM Enrollment WHERE student_ID = 102);

-- Robust General Form:
-- If student 102 is enrolled in multiple courses, a single scalar comparison would cause
-- a runtime error. Use '> ALL' or '> (SELECT MAX(...))':
-- WHERE Marks > ALL (SELECT Marks FROM Enrollment WHERE student_ID = 102);
-- or:
-- WHERE Marks > (SELECT MAX(Marks) FROM Enrollment WHERE student_ID = 102);
```

