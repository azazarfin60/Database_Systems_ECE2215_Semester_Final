# T05: SQL (DDL, DML, Aggregates, Subqueries) — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 4 | `subtopicwise_list.md` T05 (130 marks · 20.4% · 7/7)  
**Source Pages:** Pages 31–35, 37–50 (Top), 55 (Bottom), 56–58 (Top), 61

---

<!-- Page 31 -->

## SQL

### Database

* A **Database** is a collection of data in a format that can be easily accessed (Digital).
* A software application used to manage our DB is called **DBMS** (Database Management System).

### Types of Databases

| Relational | Non-relational (NoSQL) |
| :--- | :--- |
| Data stored in tables | Data not stored in tables |
| Examples: MySQL, ORACLE etc. | Examples: MongoDB |

### What is SQL?

* **Structured Query Language**.
* SQL is a programming language used to interact with relational databases.
* It is used to perform **CRUD** operations:
  * **C**reate
  * **R**ead
  * **U**pdate
  * **D**elete

---

<!-- Page 32 -->

### SEQUEL vs. SQL

| SEQUEL | SQL |
| :--- | :--- |
| **S**tructured | **S**tructured |
| **E**nglish | **Q**uery |
| **Q**uery | **L**anguage |
| **E**nglish / **L**anguage | |

*(Historical note: SQL originally developed as SEQUEL — Structured English Query Language)*

### Database Structure

![p032_fig01: Database structure showing Database containing Table 1 and Table 2 with Data](diagrams/p032_fig01.jpg)
*Figure 7 — Database Structure (Page 32)*

* Hierarchy:
  $$\text{Database} \longrightarrow \begin{cases} \text{Table 1} \longrightarrow [\text{Data}] \\ \text{Table 2} \longrightarrow [\text{Data}] \end{cases}$$

### Creating Our First Database

```sql
CREATE DATABASE db_name;

DROP DATABASE db_name;
-- ↓
-- delete
```

---

<!-- Page 33 -->

### Creating Our First Table

```sql
USE db_name;

CREATE TABLE table_name (
    column_name1 datatype constraint,
    column_name2 datatype constraints,
    column_name3 datatype constraint
);
```

#### Example: Student Table

```sql
CREATE TABLE student (
    id INT PRIMARY KEY,       -- not null, unique
    name VARCHAR(50),
    age INT NOT NULL
);

INSERT INTO student VALUES (1, "Fahim", 23);
```

### SQL Datatypes

* `TINYINT UNSIGNED` ($0$ to $255$)
* `TINYINT` ($-128$ to $127$)
* `CHAR` $\to$ string ($0$–$255$), can store characters of fixed length.
* `VARCHAR` $\to$ string ($0$–$255$), can store characters up to given length.
* `BLOB` $\to$ string ($0$–$65535$), can store binary large object.

---

<!-- Page 34 -->

### SQL Datatypes (Continued)

* `INT` $\to$ integer
* `BIGINT` $\to$ large integer
* `BIT` $\to$ can store $M$-bit values, $M$ can range from $1$ to $64$.
* `BOOLEAN` $\to$ Boolean values $0$ or $1$
* `DATE` $\to$ date in format of `YYYY-MM-DD`
* `YEAR` $\to$ Year in 4 digits format ranging from $1901$ to $2155$

### Types of SQL Commands

* **DDL (Data Definition Language):**
  * `CREATE`, `ALTER`, `RENAME`, `TRUNCATE`, `DROP`
* **DQL (Data Query Language):**
  * `SELECT`
* **DML (Data Manipulation Language):**
  * `INSERT`, `UPDATE`, `DELETE`
* **DCL (Data Control Language):**
  * `GRANT`, `REVOKE` (permission to user)
* **TCL (Transaction Control Language):**
  * `START TRANSACTION`, `COMMIT`, `ROLLBACK`

---

<!-- Page 35 -->

### Database-Related Queries

```sql
CREATE DATABASE db_name;

CREATE DATABASE IF NOT EXISTS db_name;

DROP DATABASE db_name;

DROP DATABASE IF EXISTS db_name;

SHOW DATABASES;

SHOW TABLES;
```

### Table-Related Queries

#### Select & View All Columns

```sql
SELECT * FROM table_name;
--     ↑
--    all
```

### Insert Query

**Syntax:**
```sql
INSERT INTO table_name
(colname1, colname2)
VALUES
(col1_v1, col2_v1),
(col1_v2, col2_v2);
```

**Example:**
```sql
INSERT INTO student
(rollno, name)
VALUES
(101, "fahim"),
(102, "shishir");
```

---

<!-- Page 37 -->

## Constraints

SQL constraints are used to specify rules for data in a table.

* **NOT NULL:** Columns cannot have a null value $\to$ `col1 INT NOT NULL`
* **UNIQUE:** All values in column are different $\to$ `col2 INT UNIQUE`
* **PRIMARY KEY:** Makes a column unique & not null, but used only for one.
* **FOREIGN KEY:** Prevent actions that would destroy links between tables.

### Foreign Key Constraint Syntax

```sql
CREATE TABLE temp (
    cust_id INT,
    FOREIGN KEY (cust_id) REFERENCES customer(id)
    --            ↓                           ↓
    --        new column                  old column
);
```

![p037_fig01: Foreign key constraint relationship between Temp table (cust_id FK) and customer table (id PK)](diagrams/p037_fig01.jpg)
*Figure 9 — Foreign Key Constraint Relationship (Page 37)*

---

<!-- Page 38 -->

## SQL Constraints (Continued)

### DEFAULT Constraint

* Sets the default value of a column.

```sql
salary INT DEFAULT 25000
--                  ↓
--               def value
```

**Example:**
```sql
CREATE TABLE emp (
    id INT,
    salary INT DEFAULT 25000
);

INSERT INTO emp (id) VALUES (101);
-- salary will automatically be assigned 25000
```

### CHECK Constraint

* It can limit the values allowed in a column.

```sql
CREATE TABLE city (
    id INT PRIMARY KEY,
    city VARCHAR(50),
    age INT,
    CONSTRAINT age_check CHECK (age >= 18 AND city = "Delhi")
);
```

*(Note: In the `CHECK` condition above, `age >= 18 AND city = "Delhi"` specifies that rows are only valid if age is at least 18 and the city is "Delhi".)*

---

<!-- Page 39 -->

Another $\rightarrow$

```sql
CREATE TABLE newTab (
    age INT CHECK (age >= 18)
);
```

## Select in Detail

Used to select any data from the database.

### Basic Syntax
```sql
SELECT col1, col2 FROM table_name;
```

### To Select ALL
```sql
SELECT * FROM table_name;
```

### DISTINCT
Unique value দেয়।

### WHERE Clause
To define some conditions.

```sql
SELECT col1, col2 FROM table_name
WHERE conditions;
```

---

<!-- Page 40 -->

```sql
SELECT * FROM student WHERE marks > 80;

SELECT * FROM student WHERE city = "Dhaka";
```

### Using Operators in WHERE $\rightarrow$

- **Arithmetic Operators:** `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus)
- **Comparison Operators:** `=` (equal to), `!=` (not equal to), `>`, `>=`, `<`, `<=`
- **Logical Operators:** `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `ALL`, `LIKE`, `ANY`
- **Bitwise Operators:** `&` (Bitwise AND), `|` (Bitwise OR)

### Operators

#### AND
*(to check for both conditions to be true)*

```sql
SELECT * FROM student WHERE marks > 80 AND city = "Dhaka";
```

#### OR
*(to check for one of the conditions to be true)*

```sql
SELECT * FROM student WHERE marks > 90 OR city = "DHAKA";
```

---

<!-- Page 41 -->

#### BETWEEN
*(selects for a given range)*

```sql
SELECT * FROM student WHERE marks BETWEEN 80 AND 90;
```

#### IN
*(matches any value in the list)*

```sql
SELECT * FROM student WHERE city IN ("Dhaka", "Khulna");
```

#### NOT
*(to negate the given condition)*

```sql
SELECT * FROM student WHERE city NOT IN ("Dhaka", "Khulna");
```

### LIMIT
Sets an upper limit on number of (tuples) rows to be returned.

```sql
SELECT * FROM student LIMIT 3;
```

> **Syntax:**
> ```sql
> SELECT col1, col2 FROM table_name
> LIMIT number;
> ```

### ORDER BY
To sort in ascending (`ASC`) or descending order (`DESC`).

```sql
SELECT * FROM student
ORDER BY city ASC;
```

---

<!-- Page 42 -->

```sql
SELECT col1, col2 FROM table_name
ORDER BY col_name(s) ASC;
```

### Aggregate Functions

Aggregate functions perform a calculation on a set of values, and return a single value.

- `COUNT()`
- `MAX()`
- `MIN()`
- `SUM()`
- `AVG()`

#### Examples:

- **Get maximum marks:**
  ```sql
  SELECT max(marks)
  FROM student;
  ```

- **Get average marks:**
  ```sql
  SELECT avg(marks)
  FROM student;
  ```

---

<!-- Page 43 -->

## GROUP BY

Groups rows that have the same values into summary rows.  
It collects data from multiple records and groups the result by one or more column.  
* Generally we use group by with some aggregation function.

### Count number of students in each city
```sql
SELECT city, count(name)
FROM student
GROUP BY city;
```

### Count number of students according to grades
```sql
SELECT grade, count(rollno)
FROM student
GROUP BY grade
ORDER BY grade;
```

---

<!-- Page 44 -->

### HAVING Clause
*(Group এ condition দেওয়া)*

Similar to `WHERE` i.e. applies some condition on rows.  
Used when we want to apply any condition after grouping.

- **Count number of students in each city where max marks cross 90:**
  ```sql
  SELECT city, count(rollno)
  FROM student
  GROUP BY city
  HAVING MAX(marks) > 90;
  ```

### General Order

```sql
SELECT column(s)
FROM table_name
WHERE condition
GROUP BY column(s)
HAVING condition
ORDER BY column(s) ASC;
```

> **Comparison:**
> - `WHERE` condition $\rightarrow$ applies to **rows**
> - `HAVING` condition $\rightarrow$ applies to **columns** (aggregated groups)

---

<!-- Page 45 -->

## Table Related Queries

### UPDATE
*(to update existing rows)*

> **Syntax:**
> ```sql
> UPDATE table_name
> SET col1 = val1, col2 = val2
> WHERE condition;
> ```

**Example:**
```sql
UPDATE student
SET grade = "O"
WHERE grade = "A";
```

> [!NOTE]
> এইভাবে Update করলে Error আসতে পারে Safe mode এর জন্য, তাই safe mode off করা লাগবে, তার জন্য command $\rightarrow$
> ```sql
> SET SQL_SAFE_UPDATES = 0;
> ```

---

<!-- Page 46 -->

### DELETE
*(To delete existing rows)*

> **Syntax:**
> ```sql
> DELETE FROM table_name
> WHERE condition;
> ```

**Example:**
```sql
DELETE FROM student
WHERE marks < 33;
```

### Foreign Key

```sql
CREATE TABLE dept (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE teacher (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES dept(id)
);
```

---

<!-- Page 47 -->

### Cascading for FK

#### ON DELETE CASCADE
When we create a foreign key using this option, it deletes the referencing rows in the child table when the referenced row is deleted in the parent table which has a primary key.

#### ON UPDATE CASCADE
When we create a foreign key using UPDATE CASCADE the referencing rows are updated in the child table when the referenced row is updated in the parent table which has a primary key.

#### Code:
```sql
CREATE TABLE student (
    id INT PRIMARY KEY,
    courseID INT,
    FOREIGN KEY (courseID) REFERENCES course(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
```

---

<!-- Page 48 -->

## Table Related Queries

### ALTER (to change the schema)

1. **ADD column:**
   ```sql
   ALTER TABLE table_name
   ADD COLUMN column_name datatype constraint;
   ```

2. **DROP COLUMN:**
   ```sql
   ALTER TABLE table_name
   DROP COLUMN column_name;
   ```

3. **RENAME table:**
   ```sql
   ALTER TABLE table_name
   RENAME TO new_table_name;
   ```

4. **CHANGE Column (rename):**
   ```sql
   ALTER TABLE table_name
   CHANGE COLUMN old_name new_name new_datatype new_constraint;
   ```

5. **MODIFY Column (modify datatype/constraint):**
   ```sql
   ALTER TABLE table_name
   MODIFY col_name new_datatype new_constraint;
   ```

---

<!-- Page 49 -->

### Examples of ALTER TABLE

- **ADD column:**
  ```sql
  ALTER TABLE student
  ADD COLUMN age INT NOT NULL DEFAULT 19;
  ```

- **DROP column:**
  ```sql
  ALTER TABLE student
  DROP COLUMN stu_age;
  ```

- **MODIFY Column:**
  ```sql
  ALTER TABLE student
  MODIFY age VARCHAR(2);
  ```

- **RENAME Table:**
  ```sql
  ALTER TABLE student
  RENAME TO stu;
  ```

- **CHANGE Column (rename):**
  ```sql
  ALTER TABLE student
  CHANGE age stu_age INT;
  ```

---

<!-- Page 50 -->

### TRUNCATE
*(To delete table's data)*

```sql
TRUNCATE TABLE table_name;
```

#### DROP vs. TRUNCATE

| Command | Action |
| :--- | :--- |
| **DROP** $\swarrow$ | Deletes Table (schema + data) |
| **Truncate** $\downarrow$ | Deletes table data (retains schema structure) |

---

<!-- Page 55 -->

## Union

It is used to combine the result-set of two or more `SELECT` statements. Gives **UNIQUE** records.

### To use it:

- Every `SELECT` should have same no. of columns.
- Columns must have similar data types.
- Columns in every `SELECT` should be in same order.

### Syntax

```sql
SELECT column(s) FROM tableA
UNION
SELECT column(s) FROM tableB;
```

> [!NOTE] UNION vs UNION ALL
> - **UNION** $\to$ Duplicate রাখে না (eliminates duplicates)
> - **UNION ALL** $\to$ Duplicate রাখে (retains duplicates)

---

<!-- Page 56 -->

## SQL Sub Queries

A subquery, inner query, or nested query is a query within another SQL query.
It involves 2 select statements.

> [!NOTE] Subquery লেখার ৩টি সাধারণ স্থান:
> 1. `SELECT`
> 2. `FROM`
> 3. `WHERE` (Popular / basic)

### Syntax

```sql
SELECT column(s)
FROM table_name
WHERE col_name operator (subquery);
```

![Fig_p056_01: Conceptual nested query diagram showing Sub Query enclosed within Main Query](diagrams/p056_fig01.jpg)
*Figure 3 — Nested Query Structure (Page 56)*

### Example

**Question:** Get names of all students who scored more than class average.

- **Step 1:** Find the average of class
- **Step 2:** Find the names of students with marks > average

```sql
SELECT name, marks
FROM student
WHERE marks > (SELECT AVG(marks) FROM student);
```

---

<!-- Page 57 -->

### Example: Find the names of all students with even roll numbers

- **Step 1:** Find the even roll number
- **Step 2:** Find the names of students with even roll no.

#### Stepwise (Manual / Static Approach)

```sql
SELECT rollno
FROM student
WHERE rollno % 2 = 0;

SELECT name, rollno
FROM student
WHERE rollno IN (102, 104, 106);
```

> [!WARNING]
> This is **not a dynamic process** because values are hardcoded manually.

#### Using Subquery (Dynamic Approach)

```sql
SELECT rollno, name
FROM student
WHERE rollno IN (
    SELECT rollno
    FROM student
    WHERE rollno % 2 = 0
);
```

---

<!-- Page 58 -->

### Example with FROM Clause Subquery

**Problem:** Find the max marks from the students of Delhi.

- **Step 1:** Find the students of Delhi
- **Step 2:** Find their max marks using the sublist in step 1

```sql
SELECT MAX(marks)
FROM (SELECT * FROM student WHERE city = "Delhi") AS temp;
```

---

<!-- Page 61 -->

## LIKE Command (Pattern Matching)

### Given Table: `Emp`

| ID | Name |
| :--- | :--- |
| 1 | Varun |
| 2 | Arun |
| 3 | Karina |
| 4 | Amrit |
| 5 | Ranjeet |
| 6 | Ajeet |

### Queries

#### 1) Find Employee detail whose name starting with 'A'

```sql
SELECT * FROM Emp WHERE name LIKE 'A%';
```

#### 2) Find Emp detail whose name ending with 'n'

```sql
SELECT * FROM Emp WHERE name LIKE '%n';
```

#### 3) Whose name contains 'ee'

```sql
SELECT * FROM Emp WHERE name LIKE '%ee%';
```

#### 4) Whose name contains 'a' in second place

```sql
SELECT * FROM Emp WHERE name LIKE '_a%';
```

#### 5) Whose name contains 'a' in second place and name should contain total five characters

```sql
SELECT * FROM Emp WHERE name LIKE '_a___';
```
