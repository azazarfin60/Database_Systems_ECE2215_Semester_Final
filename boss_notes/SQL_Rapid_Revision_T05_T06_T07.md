[← Master Index](00_Index.md) | [📐 Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md)

---

# ⚡ SQL Rapid Revision Sheet (T05, T06, T07)

> **Scope:** Complete Unit 4 SQL (`T05` DDL/DML/Aggregates/Subqueries + `T06` Joins & Views + `T07` Triggers & Stored Procedures)  
> **Exam Weight:** **185 Final Marks (`29.0%` of the entire course)**. Guaranteed 2 to 3 full questions every year.  
> **Target Reading Time:** ~12 minutes. Zero fluff, 1 solved RUET PYQ per concept.

---

## ⏱️ 60-Second Exam Pattern Index (Where to Jump)

| Exam Prompt / Keyword | Jump to Section | 1-Line SQL Pattern to Write |
| :--- | :--- | :--- |
| **"Write a short note on SQL / RDBMS"** | §1 | Declarative ("what, not how"), IBM *Sequel*, 4 sublanguages (DDL, DML, DCL, TCL). |
| **Two underlined columns `(roll, Dept)`** | §2 | Put `PRIMARY KEY (roll, Dept)` at the bottom of `CREATE TABLE`. |
| **"Modify table to add `session`"** | §2 | `ALTER TABLE student ADD session VARCHAR(10);` (not `MODIFY`). |
| **"Short note: `ON CASCADE DELETE`, `GROUP BY`, `ORDER BY`, `AS`"** | §3 | `ON DELETE CASCADE` deletes child rows when parent is deleted; `ORDER BY` defaults to `ASC`. |
| **"Define aggregate functions / total salary per dept"** | §4 | 5 functions (`COUNT, SUM, AVG, MIN, MAX`). Ignore `NULL`s except `COUNT(*)`. Watch for decoy tables! |
| **"Bought $>5$ different products" / "Remaining quantity"** | §5 | `HAVING COUNT(DISTINCT p_id) > 5` and `LEFT JOIN` + `p.qty - COALESCE(SUM(s.qty), 0)`. |
| **"Calculate CGPA" / "Lowest or 2nd-highest without `LIMIT`"** | §6 | `SUM(gpa * credit) / SUM(credit)` and `WHERE col = (SELECT MIN/MAX(col) ...)`. |
| **"Explain subqueries" / "Salary $>$ own dept average"** | §7 | Give 1 `IN` query + 1 `AVG` correlated query (`WHERE e2.dept = e1.dept`). |
| **"Maximum patients in a date" / "Insurance" / "Unsold products"** | §8 | Derived table `FROM (SELECT Date, COUNT(...) GROUP BY Date) AS t`, Owner join, `NOT IN`. |
| **"`TRUNCATE` vs `DELETE`"** | §9 | `TRUNCATE` is DDL, no `WHERE`, no `ROLLBACK`, no triggers, resets `AUTO_INCREMENT` to `1`. |
| **"Inner vs Outer Join" / "`Courses` & `Teacher` join outcomes"** | §10 | Natural & Left = 4 rows; Right & Full = 5 rows (`T4` padded with `NULL`). MySQL Full = `LEFT UNION RIGHT`. |
| **"Benefits of `VIEW`" / "`CREATE VIEW` for salary $> 55000$"** | §11 | Virtual table (stores query only). 4 benefits + 4 updatable view rules (`1` table, no aggregates/grouping). |
| **"What is triggering?" / "Security before & after breach"** | §12 | ECA model. Before breach = `BEFORE` trigger + `SIGNAL`. After breach = `AFTER` trigger + `audit_log`. |
| **"Stored procedure for order + stock trigger + send email"** | §13 | Lock stock with `FOR UPDATE`; triggers cannot send SMTP directly, so insert into `email_queue`. |

---

## 1. SQL Overview & RDBMS (`T05.1`, `T05.7b`)

- **RDBMS (`2020 Q.7b`, `2024 Q.5b`):** Database software based on E.F. Codd's relational model that stores data in 2D tables (rows/tuples and columns/attributes), enforces integrity via primary and foreign keys, and uses SQL for querying and transactions.
- **Declarative Language:** In SQL, you state **what** data you want, and the DBMS query optimizer decides **how** to fetch it.
- **Four Sublanguages:**
  1. **DDL (Data Definition):** Builds/alters schemas (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`). Auto-commits immediately.
  2. **DML (Data Manipulation):** Queries/edits rows (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). Can be undone with `ROLLBACK`.
  3. **DCL (Data Control):** Manages permissions (`GRANT`, `REVOKE`).
  4. **TCL (Transaction Control):** Manages atomic transactions (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).
- **Core Data Types:** `INT`, `NUMERIC(p, d)` / `DECIMAL(p, d)` (exact decimals like GPA/money), `CHAR(n)` (fixed length), `VARCHAR(n)` (variable length), `DATE`.

> [!example] PYQ Example: `2019 Q.5(a)` (2 Marks) Short note on SQL
> **SQL (Structured Query Language)** is the standard declarative language for relational databases, originally developed at IBM as *Sequel* for the System R project. Because it is declarative, users specify *what* data is needed while the DBMS optimizer chooses *how* to retrieve it. It has four sublanguages:
> 1. **DDL:** Defines schemas and constraints (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`).
> 2. **DML:** Queries and modifies table rows (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
> 3. **DCL:** Controls user access rights (`GRANT`, `REVOKE`).
> 4. **TCL:** Manages transaction boundaries (`COMMIT`, `ROLLBACK`).

---

## 2. DDL & DML Essentials (`T05.2a`, `T05.2b`)

- **Composite Primary Key Rule:** When two or more columns are underlined (like `roll` and `Dept`), declare `PRIMARY KEY (roll, Dept)` at the bottom of `CREATE TABLE`. Writing `PRIMARY KEY` inline on two separate columns is a syntax error.
- **Foreign Key Creation Order:** Always `CREATE` the parent table (e.g., `Patient`) before child tables (`History`, `Report`) that reference it.
- **Adding a Column (`ALTER TABLE`):** Use `ALTER TABLE tbl ADD col datatype;`. Existing rows automatically get `NULL` in the new column.
- **Row Updates & Deletions:**
  - `UPDATE tbl SET col = val WHERE condition;` (Omitting `WHERE` updates **every** row!).
  - `DELETE FROM tbl WHERE condition;` (**Trap:** Never write `DELETE * FROM`).

> [!example] PYQ Example: `2018 Q.7(a)` = `2024 Q.4(b)` (4 Marks) & `2021 Q.3(a)` (8 Marks)
> ```sql
> -- 1. Create student(roll, Name, Dept) with composite key (2018 Q.7a-i)
> CREATE TABLE student (
>     roll INT,
>     Name VARCHAR(50),
>     Dept VARCHAR(20),
>     PRIMARY KEY (roll, Dept)
> );
> 
> -- 2. Insert one example entry (2018 Q.7a-ii)
> INSERT INTO student (roll, Name, Dept) VALUES (1810001, 'Rahim', 'ECE');
> 
> -- 3. Add a column: session (2018 Q.7a-iii) / numeric(11) Telephone (2021 Q.3a-iii)
> ALTER TABLE student ADD session VARCHAR(10);
> ALTER TABLE client ADD Telephone NUMERIC(11);
> 
> -- 4. Update city of client "C0005" to "Barishal" (2021 Q.3a-i)
> UPDATE client SET city = 'Barishal' WHERE c_no = 'C0005';
> 
> -- 5. Delete salesmen with salary 35000 Tk (2021 Q.3a-ii)
> DELETE FROM salesman WHERE sal_amount = 35000;
> 
> -- 6. Products with sell_price > 500 and sell_price * 15 renamed as new_price (2021 Q.3a-iv)
> SELECT p_no, description, sell_price, sell_price * 15 AS new_price
> FROM product
> WHERE sell_price > 500;
> ```

---

## 3. Basic Clauses & SQL Short Notes (`T05.3`, `T05.8`)

- **Execution Order:** `FROM` $\to$ `WHERE` $\to$ `GROUP BY` $\to$ `HAVING` $\to$ `SELECT` $\to$ `ORDER BY`.
  - Since `WHERE` runs before `SELECT`, you **cannot** use `SELECT` column aliases inside `WHERE`.
- **`DISTINCT` vs `ALL`:** SQL keeps duplicates by default (`ALL`). Write `SELECT DISTINCT` to strip duplicates.
- **`LIKE` Wildcards:** `%` matches $0$ or more characters (`'A%'` = starts with A; `'%fever%'` = contains "fever"); `_` matches exactly $1$ character (`'___'` = 3 characters).
- **Backtick Rule:** Wrap identifiers containing spaces or MySQL reserved words in backticks: `` `St Name` ``, `` `Department ID` ``, `` `t code` ``, `` `order` ``.

> [!example] PYQ Example: `2024 Q.7(b)` (4 Marks) Short Notes (`ON CASCADE DELETE`, `GROUP BY`, `ORDER BY`, `AS`)
> 1. **`ON CASCADE DELETE` (Standard SQL: `ON DELETE CASCADE`):** Foreign key rule where deleting a parent row automatically deletes all matching child rows in the referencing table, preventing orphan records:
>    ```sql
>    FOREIGN KEY (dept_name) REFERENCES department(dept_name) ON DELETE CASCADE
>    ```
> 2. **`GROUP BY`:** Splits rows sharing the same column values into summary buckets so aggregates (`COUNT`, `SUM`, `AVG`) calculate one summary row per group:
>    ```sql
>    SELECT dept_name, AVG(salary) AS avg_sal FROM instructor GROUP BY dept_name;
>    ```
> 3. **`ORDER BY`:** Sorts final output rows in ascending (`ASC`, default) or descending (`DESC`) order:
>    ```sql
>    SELECT * FROM STUDENT WHERE Department = 'ECE' AND CGPA > 3.50 ORDER BY CGPA DESC;
>    ```
> 4. **`AS` (Rename):** Gives a temporary alias to an output column or table (mandatory for self-joins):
>    ```sql
>    SELECT T.name FROM instructor AS T, instructor AS S WHERE T.salary > S.salary;
>    ```

---

## 4. Aggregate Functions & `NULL` Rules (`T05.4`)

- **Five Standard Functions:** `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`. (In extended relational algebra: ${}_{G}\gamma_{F}(E)$).
- **Two Golden `NULL` Rules:**
  1. **Ignore Rule:** `SUM`, `AVG`, `MIN`, `MAX`, and `COUNT(col)` **ignore `NULL` values** (so `AVG` divides only by the number of non-null rows). Only `COUNT(*)` counts all rows including `NULL`s.
  2. **Empty Table Rule:** On $0$ rows (or all `NULL`s), `COUNT` returns `0`, whereas `SUM`, `AVG`, `MIN`, and `MAX` return `NULL`.
- **Decoy Table Trap:** Before joining tables, check if all needed attributes are already in one table. Joining a detail table (`SALES`) multiplies rows and corrupts `SUM(Salary)`.

> [!example] PYQ Example: `2019 Q.8(a)` (4 Marks) & `2024 Q.7(a)` (3 Marks) Aggregates & Dept Salary
> **Schemas (`2024 Q.7a`):** `EMPLOYEE(EID, Name, Department, Salary)`, `SALES(SID, EID, SaleAmount, SaleDate)`  
> **Answer:** An **aggregate function** takes a multiset of values from a column across multiple rows and returns a single summary scalar (`COUNT` counts rows/values, `SUM` totals numbers, `AVG` finds the arithmetic mean, and `MIN`/`MAX` find extremes).  
> *(Since both `Department` and `Salary` are in `EMPLOYEE`, do not join decoy table `SALES`):*
> ```sql
> SELECT Department, SUM(Salary) AS Total_Salary
> FROM EMPLOYEE
> GROUP BY Department;
> ```

---

## 5. `GROUP BY` & `HAVING` (`T05.5a`)

- **Cardinal Rule of `GROUP BY`:** Every column in `SELECT` that is **not** inside an aggregate function **must** appear in `GROUP BY`.
- **`WHERE` vs `HAVING`:**
  - `WHERE` filters **individual rows** *before* `GROUP BY`. Never put aggregates in `WHERE` (`WHERE SUM(qty) > 10` is a syntax error).
  - `HAVING` filters **summary groups** *after* `GROUP BY` (`HAVING SUM(qty) > 10`).
- **Remaining Inventory Rule:** Always use `LEFT JOIN` + `COALESCE(SUM(s.quantity), 0)` so products with zero sales are still shown with their full initial quantity.

> [!example] PYQ Example: `2018 Q.7(b)` (8 Marks) E-Commerce `GROUP BY`, `HAVING` & Remaining Stock
> **Schemas:** `Product(p_id, p_name, quantity, unit_price)`, `Customer(c_id, c_name, contact)`, `Sales(c_id, p_id, quantity)`
> ```sql
> -- (i) Customers who bought more than 5 DIFFERENT products
> SELECT c.c_id, c.c_name, c.contact
> FROM Customer c
> JOIN Sales s ON c.c_id = s.c_id
> GROUP BY c.c_id, c.c_name, c.contact
> HAVING COUNT(DISTINCT s.p_id) > 5;
> 
> -- (ii) Products sold more than 10 pieces
> SELECT p.p_id, p.p_name, p.quantity, p.unit_price
> FROM Product p
> JOIN Sales s ON p.p_id = s.p_id
> GROUP BY p.p_id, p.p_name, p.quantity, p.unit_price
> HAVING SUM(s.quantity) > 10;
> 
> -- (iii) Product with maximum sale (highest total revenue)
> SELECT p.p_id, p.p_name, SUM(s.quantity * p.unit_price) AS total_sales_value
> FROM Product p
> JOIN Sales s ON p.p_id = s.p_id
> GROUP BY p.p_id, p.p_name
> ORDER BY total_sales_value DESC
> LIMIT 1;
> 
> -- (iv) Product ID and remaining quantity (LEFT JOIN preserves unsold products)
> SELECT p.p_id,
>        p.quantity - COALESCE(SUM(s.quantity), 0) AS remaining_quantity
> FROM Product p
> LEFT JOIN Sales s ON p.p_id = s.p_id
> GROUP BY p.p_id, p.quantity;
> ```

---

## 6. Weighted CGPA & Extremes Without `LIMIT` (`T05.5b`)

- **Why `AVG(gpa)` Fails for CGPA:** Courses have different credits ($3.00$ vs $1.50$). You must weight each course's GPA by its credit:
  $$
  \text{CGPA} = \frac{\sum (\text{gpa} \times \text{credit})}{\sum \text{credit}} \implies \texttt{SUM(g.gpa * c.Credit) / SUM(c.Credit)}
  $$
- **Why Examiners Ban `LIMIT`:** `LIMIT` is non-standard ANSI SQL and drops tied students. Use scalar `MIN`/`MAX` subqueries instead:
  - **1st Lowest / Highest:** `WHERE gpa = (SELECT MIN(gpa) FROM GPA)`
  - **2nd Highest (Runner-Up):** Highest value strictly less than the overall maximum: `WHERE CGPA = (SELECT MAX(CGPA) FROM STUDENT WHERE CGPA < (SELECT MAX(CGPA) FROM STUDENT))`

> [!example] PYQ Example: `2019 Q.7(a)` (12 Marks) = `2017 Q.4(a)` & `CT-02 Q.01(d)` (3 Marks)
> **Schemas (`2019 Q.7a`):** `Student(St_ID, St Name)`, `GPA(St_ID, Sub_Code, gpa)`, `Credit(Sub_Code, Credit)`
> ```sql
> -- (i) Students who got the lowest GPA (dynamic subquery; never hardcode 3.00!)
> SELECT s.St_ID, s.`St Name`, g.Sub_Code, g.gpa
> FROM Student s
> JOIN GPA g ON s.St_ID = g.St_ID
> WHERE g.gpa = (SELECT MIN(gpa) FROM GPA);
> 
> -- (ii) Registered subjects of students whose name starts with "A"
> SELECT DISTINCT s.St_ID, s.`St Name`, g.Sub_Code
> FROM Student s
> JOIN GPA g ON s.St_ID = g.St_ID
> WHERE s.`St Name` LIKE 'A%';
> 
> -- (iii) Weighted CGPA of each student
> SELECT s.St_ID, s.`St Name`,
>        SUM(g.gpa * c.Credit) / SUM(c.Credit) AS cgpa
> FROM Student s
> JOIN GPA g ON s.St_ID = g.St_ID
> JOIN Credit c ON g.Sub_Code = c.Sub_Code
> GROUP BY s.St_ID, s.`St Name`;
> 
> -- (iv) Each subject code and corresponding highest GPA
> SELECT Sub_Code, MAX(gpa) AS highest_gpa
> FROM GPA
> GROUP BY Sub_Code;
> 
> -- CT-02 Q.01(d): Students with 2nd-highest CGPA without using LIMIT
> SELECT * FROM STUDENT
> WHERE CGPA = (
>     SELECT MAX(CGPA) FROM STUDENT
>     WHERE CGPA < (SELECT MAX(CGPA) FROM STUDENT)
> );
> ```

---

## 7. Subqueries: `IN`, `SOME`, `ALL`, `EXISTS` & Correlated (`T05.6`)

- **Uncorrelated vs Correlated:**
  - **Uncorrelated:** Inner query runs **once** globally (`WHERE CGPA > (SELECT AVG(CGPA) FROM STUDENT)`).
  - **Correlated:** Inner query uses an outer table alias (`WHERE e2.Department = e1.Department`) and re-evaluates **for each outer row** (needed for *"greater than their own department's average"*).
- **Set Comparison Shortcuts:**
  - `= SOME` $\equiv$ `IN` | `<> ALL` $\equiv$ `NOT IN` (**Trap:** `<> SOME` $\not\equiv$ `NOT IN`).
  - `> ALL` means $>$ maximum | `> SOME` means $>$ minimum.
- **The `NOT IN` + `NULL` Trap:** If the subquery returns even one `NULL`, `x NOT IN (10, NULL)` evaluates to `UNKNOWN` and returns **0 rows**. `NOT EXISTS` is always safe.

> [!example] PYQ Example: `2024 Q.6(a)` = `2019 Q.8(b)` (4 Marks) & `2023 Q.3(a)(iii)` (2 Marks)
> **Answer (`2024 Q.6(a)`: Explain subqueries with 2 suitable examples):**  
> A **subquery** is a `SELECT-FROM-WHERE` query nested inside an outer query (`WHERE`, `FROM`, or `SELECT`) to perform multi-step filtering.
> ```sql
> -- Example 1: Set Membership Subquery using IN (Uncorrelated)
> SELECT DISTINCT course_id
> FROM section
> WHERE semester = 'Fall' AND year = 2017
>   AND course_id IN (
>       SELECT course_id FROM section WHERE semester = 'Spring' AND year = 2018
>   );
> 
> -- Example 2: Correlated Scalar Subquery (2023 Q.3(a)(iii): salary > own dept average)
> SELECT *
> FROM Employee e1
> WHERE e1.Salary > (
>     SELECT AVG(e2.Salary)
>     FROM Employee e2
>     WHERE e2.Department = e1.Department
> );
> ```

---

## 8. High-Frequency Multi-Table Schemas (`T05.7a`, `T05.7b`)

Memorize these **4 exam traps** across RUET's favorite multi-table schemas:
1. **Covid DB (`2019 Q.5b`):** Standard SQL forbids `MAX(COUNT(*))`. To find the peak daily count, group by `Date` inside a **derived table** in `FROM (...) AS daily_summary` (MySQL requires an alias on every derived table!) and take `MAX(daily_count)` in the outer query. Also note the printed typo `Parient_ID` in `Report`.
2. **Company DB (`2020 Q.3b`):** "Working on project 5 and from the **same department**" requires matching the employee's department to the project's controlling department: `AND e.dept_no = p.dnum`.
3. **Insurance DB (`2020 Q.7b` = `2024 Q.5b`):** "Accidents involving cars **belonging to** John Smith" must join `Person` $\to$ `Owner` $\to$ `Participated` (`ON p.car = o.license`), **not** `Participated.driver_id = Person.driver_id` (someone else might have been driving John's car!).
4. **E-Commerce DB (`2021 Q.4a`):** Enclose table `` `order` `` in backticks (reserved word). To find **unsold products**, never use `INNER JOIN`; use an anti-join (`WHERE p_no NOT IN (SELECT DISTINCT product_no FROM order_details)`).

> [!example] PYQ Example 1: `2019 Q.5(b)` (8 Marks) Covid Tracking Database
> **Schemas:** `Patient(Patient_ID, Patient_name, Mobile)`, `History(Patient_ID, Symptom, Date)`, `Report(Parient_ID, Corona_center, Test_result)`
> ```sql
> -- (i) Names of patients with fever symptom
> SELECT DISTINCT p.Patient_name FROM Patient p
> JOIN History h ON p.Patient_ID = h.Patient_ID WHERE h.Symptom LIKE '%fever%';
> 
> -- (ii) Maximum number of high-fever patients in a single date (Derived Table!)
> SELECT MAX(daily_count) AS max_patients
> FROM (
>     SELECT Date, COUNT(DISTINCT Patient_ID) AS daily_count
>     FROM History WHERE Symptom = 'high fever' GROUP BY Date
> ) AS daily_summary;
> 
> -- (iii) Mobile numbers tested in 'Rajshahi' with 'positive' result
> SELECT DISTINCT p.Mobile FROM Patient p
> JOIN Report r ON p.Patient_ID = r.Parient_ID
> WHERE r.Corona_center = 'Rajshahi' AND r.Test_result = 'positive';
> 
> -- (iv) Names of patients with 'high fever' but 'negative' test result
> SELECT DISTINCT p.Patient_name FROM Patient p
> JOIN History h ON p.Patient_ID = h.Patient_ID
> JOIN Report r ON p.Patient_ID = r.Parient_ID
> WHERE h.Symptom = 'high fever' AND r.Test_result = 'negative';
> ```

> [!example] PYQ Example 2: `2020 Q.3(b)` (10 Marks) Company Database
> **Schemas:** `employee(ssn, fname, lname, Salary, dept_no)`, `department(dnumber, dname)`, `project(pnumber, pname, dnum)`, `works_on(essn, pno, hours)`, `dependent(essn, dependent_name)`
> ```sql
> -- (i) Dept name & employee count for depts with average salary > $30,000
> SELECT d.dname, COUNT(e.ssn) AS num_employees
> FROM department d JOIN employee e ON d.dnumber = e.dept_no
> GROUP BY d.dnumber, d.dname HAVING AVG(e.Salary) > 30000;
> 
> -- (ii) Employees on project 5 who belong to the SAME department controlling project 5
> SELECT e.fname, e.lname
> FROM employee e
> JOIN works_on w ON e.ssn = w.essn
> JOIN project p ON w.pno = p.pnumber
> WHERE p.pnumber = 5 AND e.dept_no = p.dnum;
> 
> -- (iii) Number of dependents of employees in "H&R" department
> SELECT COUNT(dp.dependent_name) AS total_dependents
> FROM dependent dp
> JOIN employee e ON dp.essn = e.ssn
> JOIN department d ON e.dept_no = d.dnumber
> WHERE d.dname = 'H&R';
> ```

> [!example] PYQ Example 3: `2020 Q.7(b)` = `2024 Q.5(b)` (8 Marks) Insurance Database
> **Schemas:** `Person(driver_id, name, address)`, `Car(license, model, year)`, `Accident(report_no, date, location)`, `Owner(driver_id, license)`, `Participated(driver_id, report_no, car, damage_amount)`
> ```sql
> -- (i) Number of accidents involving cars belonging to "John Smith"
> SELECT COUNT(DISTINCT p.report_no) AS accident_count
> FROM Participated p
> JOIN Owner o ON p.car = o.license
> JOIN Person per ON o.driver_id = per.driver_id
> WHERE per.name = 'John Smith';
> 
> -- (ii) Add a new accident (Note: 2024 paper misprints 'date' as 'data')
> INSERT INTO Accident (report_no, date, location)
> VALUES ('AR-2024', '2024-10-15', 'Rajshahi');
> 
> -- (iii) Update the car "Mazda" belonging to "John" (Assumption: set year = 2023)
> UPDATE Car c
> JOIN Owner o ON c.license = o.license
> JOIN Person p ON o.driver_id = p.driver_id
> SET c.year = 2023
> WHERE p.name = 'John' AND c.model = 'Mazda';
> 
> -- (iv) Update damage amount to $3000 for car "YJK-100" in accident "APR2197"
> UPDATE Participated SET damage_amount = 3000
> WHERE car = 'YJK-100' AND report_no = 'APR2197';
> ```

> [!example] PYQ Example 4: `2021 Q.4(a)` (12 Marks) E-Commerce 5-Table Queries
> **Schemas:** `client(c_no, name, ...)`, `product(p_no, description, ...)`, `order(order_no, client_no, ...)`, `order_details(order_no, product_no, quantity_ordered, product_rate)`
> ```sql
> -- (i) Total value of each product sold
> SELECT od.product_no, p.description,
>        SUM(od.quantity_ordered * od.product_rate) AS total_value
> FROM order_details od JOIN product p ON od.product_no = p.p_no
> GROUP BY od.product_no, p.description;
> 
> -- (ii) Products and quantities ordered by C0001 and C0002 (backticks on `order`!)
> SELECT o.client_no, od.product_no, p.description, od.quantity_ordered
> FROM `order` o
> JOIN order_details od ON o.order_no = od.order_no
> JOIN product p ON od.product_no = p.p_no
> WHERE o.client_no IN ('C0001', 'C0002');
> 
> -- (iii) Product no and description of products NOT being sold (Anti-Join)
> SELECT p_no, description FROM product
> WHERE p_no NOT IN (SELECT DISTINCT product_no FROM order_details);
> 
> -- (iv) Client no and name who ordered "Lyera Top"
> SELECT DISTINCT c.c_no, c.name
> FROM client c
> JOIN `order` o ON c.c_no = o.client_no
> JOIN order_details od ON o.order_no = od.order_no
> JOIN product p ON od.product_no = p.p_no
> WHERE p.description = 'Lyera Top';
> ```

---

## 9. `TRUNCATE` vs `DELETE` (`T05.9`)

> [!example] PYQ Example: `2023 Q.6(a)` (2 Marks) Difference between `TRUNCATE` and `DELETE`
>
> | Feature | `TRUNCATE TABLE` | `DELETE FROM` |
> | :--- | :--- | :--- |
> | **SQL Category** | **DDL** (Data Definition Language) | **DML** (Data Manipulation Language) |
> | **`WHERE` Filtering** | Not allowed (always empties entire table) | Allowed (can delete specific rows) |
> | **Transaction Rollback** | Cannot be rolled back in MySQL (auto-commits) | Can be undone using `ROLLBACK` |
> | **Trigger Execution** | Does **not** fire row-level `DELETE` triggers | Fires `BEFORE/AFTER DELETE` triggers per row |
> | **`AUTO_INCREMENT`** | Resets counter back to `1` | Keeps existing counter value |
> | **Speed & Mechanism** | Very fast (drops and recreates data pages) | Slower (locks, deletes, and logs row by row) |

---

## 10. SQL Joins & Join Outcome Tables (`T06.1`, `T06.2`, `T06.3`)

- **Inner Join vs Outer Join (`2024 Q.3c`: 2 Marks):**
  - **Inner Join ($\bowtie$):** Keeps **only matching rows** between both tables; drops unmatched rows (causes information loss) and never introduces `NULL` padding. Subtypes: Theta join, Equijoin, Natural join.
  - **Outer Join ($\mathbin{⟕}, \mathbin{⟖}, \mathbin{⟗}$):** Keeps all matching rows **plus unmatched ("dangling") rows** from the left ($\mathbin{⟕}$), right ($\mathbin{⟖}$), or both ($\mathbin{⟗}$) tables, padding missing attributes with `NULL` to prevent information loss.
- **Natural Join ($\bowtie$):** Matches rows on **all** identically named columns and outputs shared columns **only once**. *(Trap: If two tables share an unrelated column name like `dept_name`, `NATURAL JOIN` equates that too! Use `JOIN ... USING (col)` to avoid this.)*
- **MySQL `FULL OUTER JOIN` Emulation:** MySQL lacks `FULL OUTER JOIN`; always write `LEFT JOIN ... UNION ... RIGHT JOIN`.
- **Outer Joins in Basic Relational Algebra ($r(R), s(S)$):**
  $$
  r \mathbin{⟕} s = (r \bowtie s) \cup \big((r - \Pi_R(r \bowtie s)) \times \{(\text{null}, \dots, \text{null})\}\big)
  $$
  $$
  r \mathbin{⟖} s = (r \bowtie s) \cup \big(\{(\text{null}, \dots, \text{null})\} \times (s - \Pi_S(r \bowtie s))\big), \qquad r \mathbin{⟗} s = (r \mathbin{⟕} s) \cup (r \mathbin{⟖} s)
  $$

> [!example] PYQ Example: `2024 Q.4(a)` (6 Marks) = `2020 Q.4(c)` (5 Marks) Join Outcome Tables
> **Given Tables (`2024 Q.4a`):** *(Note: In `2020 Q.4c`, the join column is printed with a space as `` `t code` ``)*  
> `Courses(Code, Series, t_code)` = `{(E_2215, 2020, T1), (E_4127, 2021, T2), (E_1203, 2022, T3), (E_2219, 2021, T3)}`  
> `Teacher(t_code, Designation)` = `{(T1, Head), (T2, AP), (T3, AP), (T4, Lecturer)}`  
> **Block Check:** All 4 courses match `T1, T2, T3` (0 left-dangling rows). Teacher `T4` has no course (1 right-dangling row).
>
> **(i) Natural Join (`SELECT Code, Series, t_code, Designation FROM Courses NATURAL JOIN Teacher;`)** &  
> **(ii) Left Outer Join (`SELECT c.Code, c.Series, c.t_code, t.Designation FROM Courses c LEFT JOIN Teacher t ON c.t_code = t.t_code;`):**  
> *(Both produce the exact same **4 rows** because every course has a matching teacher):*
>
> | Code | Series | t_code | Designation |
> | :--- | :---: | :---: | :--- |
> | E_2215 | 2020 | T1 | Head |
> | E_4127 | 2021 | T2 | AP |
> | E_1203 | 2022 | T3 | AP |
> | E_2219 | 2021 | T3 | AP |
>
> **(iii) Right Outer Join (`... FROM Courses c RIGHT JOIN Teacher t ON c.t_code = t.t_code;`)** &  
> **(iv) Full Outer Join (`LEFT JOIN ... UNION ... RIGHT JOIN`):**  
> *(Both produce the exact same **5 rows**, preserving unmatched teacher `T4` with `NULL` padding):*
>
> | Code | Series | t_code | Designation |
> | :--- | :---: | :---: | :--- |
> | E_2215 | 2020 | T1 | Head |
> | E_4127 | 2021 | T2 | AP |
> | E_1203 | 2022 | T3 | AP |
> | E_2219 | 2021 | T3 | AP |
> | `NULL` | `NULL` | T4 | Lecturer |

---

## 11. SQL Views, Updatability & Materialized Views (`T06.4`, `T06.5`)

- **View (Virtual Relation):** A virtual table defined by a saved query (`CREATE VIEW v AS <query>`). Stores only the query text in the system catalog, consuming zero disk space for rows. When queried, the DBMS performs **view expansion** (substituting the saved query into `FROM`).
- **4 Benefits of Views (`2023 Q.5a`: 3 Marks):**
  1. **Security & Access Control:** Hides confidential columns (like salary) and restricts visible rows per user.
  2. **Query Simplicity:** Hides complex multi-table joins and aggregates behind a simple virtual table name.
  3. **Logical Data Independence:** Shields application code when base tables are split or restructured.
  4. **Standardized Calculations:** Codes business formulas (like CGPA) once so all reports stay consistent.
- **4 SQL Standard Conditions for an Updatable View:**
  1. `FROM` clause has **only 1 base table** (no joins, unions, or subqueries).
  2. `SELECT` list has **only simple column names** (no aggregates, arithmetic expressions, or `DISTINCT`).
  3. Omitted base-table columns allow `NULL` (or have a `DEFAULT`).
  4. Query has **no `GROUP BY` or `HAVING`**.
  - *(Appending `WITH CHECK OPTION` rejects any `INSERT`/`UPDATE` through the view that violates the view's `WHERE` filter.)*
- **Materialized View:** Precomputes and stores view rows physically on disk for fast OLAP reads; requires view maintenance (immediate, lazy, or periodic refresh) when base tables change.

> [!example] PYQ Example: `2023 Q.5(b)` (3 Marks) `CREATE VIEW` Across 3 Tables
> **Tables:** `E(EmployeeID, EmployeeName, Department ID)`, `D(DepartmentID, DepartmentName)`, `S(EmployeeID, Salary)`  
> **Task:** Create a VIEW showing `EmployeeName`, `DepartmentName`, and `Salary` for employees earning **more than 55,000**.
> ```sql
> CREATE VIEW High_Salary_Employees AS
> SELECT E.EmployeeName, D.DepartmentName, S.Salary
> FROM E
> JOIN D ON E.`Department ID` = D.DepartmentID
> JOIN S ON E.EmployeeID = S.EmployeeID
> WHERE S.Salary > 55000;
> ```
> *(Strict `> 55000` excludes Jhon [50,000] and Alice [55,000], returning `(Jane, HR, 60000)` and `(Bob, IT, 70000)`.)*

---

## 12. Triggers: ECA Model, Purpose & Security (`T07.1`, `T07.2`)

- **Trigger & Triggering (`2018 Q.8a`, `2020 Q.8a`):** A trigger is a stored SQL program that executes automatically when an `INSERT`, `UPDATE`, or `DELETE` modifies a table. Governed by the **ECA (Event-Condition-Action)** model.
- **4 Purposes:** (1) Enforce complex cross-table integrity rules, (2) Automatic security audit logging, (3) Keep derived/summary columns (like stock) in sync, (4) Automate alert/queue workflows.
- **Transition Variables (`FOR EACH ROW`):** `INSERT` has `NEW` only | `UPDATE` has both `OLD` and `NEW` | `DELETE` has `OLD` only.
- **Dual-Phase Database Security (`2017 Q.8b`, `2024 Q.2a`):**
  1. **Before a Breach (`BEFORE` Trigger for Prevention):** Acts as a security gatekeeper. Inspects incoming values/time (`CURRENT_TIME()`) before disk write and aborts illegal modifications with `SIGNAL SQLSTATE '45000'`, rolling back the change.
  2. **After a Breach (`AFTER` Trigger for Auditing & Forensics):** Acts as a tamper-evident flight recorder. Automatically logs `OLD` values, `NEW` values, `USER()`, and `NOW()` into a separate `audit_log` table so DBAs can trace the attacker and restore damaged rows using `OLD`.

> [!example] PYQ Example: `2017 Q.8(b)` = `2024 Q.2(a)` (5 Marks) & `2018 Q.8(a)` = `2020 Q.8(a)` (5 Marks)
> ```sql
> DELIMITER //
> 
> -- Phase 1: BEFORE Breach (Proactive Prevention + General Trigger Syntax)
> CREATE TRIGGER trg_prevent_unauthorized_salary
> BEFORE UPDATE ON employees
> FOR EACH ROW
> BEGIN
>     IF CURRENT_TIME() NOT BETWEEN '09:00:00' AND '17:00:00'
>        OR NEW.salary > (OLD.salary * 1.50) THEN
>         SIGNAL SQLSTATE '45000'
>             SET MESSAGE_TEXT = 'Security Alert: Office-hour or salary limit violated.';
>     END IF;
> END //
> 
> -- Phase 2: AFTER Breach (Reactive Forensics & Recovery Log)
> CREATE TRIGGER trg_audit_salary_change
> AFTER UPDATE ON employees
> FOR EACH ROW
> BEGIN
>     IF OLD.salary <> NEW.salary THEN
>         INSERT INTO salary_audit_log (emp_id, old_sal, new_sal, changed_by, changed_at)
>         VALUES (OLD.emp_id, OLD.salary, NEW.salary, USER(), NOW());
>     END IF;
> END //
> 
> DELIMITER ;
> ```

---

## 13. Stored Procedures & Workflow Triggers (`T07.3`)

- **Stored Procedure vs Trigger:** A procedure is called explicitly (`CALL proc(args)`), takes `IN`/`OUT` parameters, and can manage transactions (`START TRANSACTION`, `COMMIT`, `ROLLBACK`). A trigger takes no parameters and fires automatically on table DML.
- **Preventing Race Conditions:** Always lock inventory rows using `SELECT stock INTO v_stock ... FOR UPDATE` inside order procedures so two concurrent buyers cannot purchase the last unit at the same time.
- **The Email Notification Rule (`2024 Q.6b`):** A database trigger **cannot** directly open network sockets to send SMTP emails (it would freeze row locks and cannot be undone if the transaction rolls back). Instead, the trigger inserts a job row into an `email_queue` table, and an external background worker sends the email after commit.

> [!example] PYQ Example 1: `2023 Q.6(b)` (6 Marks) Order Placement Stored Procedure + Stock Audit Trigger
> **Schemas:** `Products(product_id, name, stock, price)`, `Orders(order_id, product_id, quantity, order_date)`, `Auditlog(log_id, product_id, old_stock, new_stock, changed_at)`
> ```sql
> DELIMITER //
> 
> -- (i) Stored Procedure to place order considering stock availability
> CREATE PROCEDURE PlaceOrder (
>     IN p_product_id INT,
>     IN p_quantity INT
> )
> BEGIN
>     DECLARE v_stock INT;
>     START TRANSACTION;
> 
>     SELECT stock INTO v_stock
>     FROM Products WHERE product_id = p_product_id FOR UPDATE;
> 
>     IF v_stock IS NULL OR v_stock < p_quantity THEN
>         ROLLBACK;
>         SIGNAL SQLSTATE '45000'
>             SET MESSAGE_TEXT = 'Error: Insufficient stock or invalid product.';
>     ELSE
>         INSERT INTO Orders (product_id, quantity, order_date)
>         VALUES (p_product_id, p_quantity, NOW());
> 
>         UPDATE Products SET stock = stock - p_quantity
>         WHERE product_id = p_product_id;
> 
>         COMMIT;
>     END IF;
> END //
> 
> -- (ii) Trigger on Products to log every stock update in Auditlog automatically
> CREATE TRIGGER trg_log_stock_update
> AFTER UPDATE ON Products
> FOR EACH ROW
> BEGIN
>     IF OLD.stock <> NEW.stock THEN
>         INSERT INTO Auditlog (product_id, old_stock, new_stock, changed_at)
>         VALUES (OLD.product_id, OLD.stock, NEW.stock, NOW());
>     END IF;
> END //
> 
> DELIMITER ;
> ```

> [!example] PYQ Example 2: `2024 Q.6(b)` (4 Marks) E-Commerce Trigger for Stock Update & Email Queue
> **Schemas:** `products(product_id, name, stock)`, `orders(order_id, product_id, quantity, customer_email, order_date)`, `email_queue(queue_id, recipient, subject, body, queued_at)`
> ```sql
> DELIMITER //
> 
> CREATE TRIGGER trg_after_order_insert
> AFTER INSERT ON orders
> FOR EACH ROW
> BEGIN
>     -- 1. Deduct ordered quantity from product stock
>     UPDATE products
>     SET stock = stock - NEW.quantity
>     WHERE product_id = NEW.product_id;
> 
>     -- 2. Enqueue email job for background mailer worker (DB cannot send SMTP directly)
>     INSERT INTO email_queue (recipient, subject, body, queued_at)
>     VALUES (
>         NEW.customer_email,
>         'Order Confirmation',
>         CONCAT('Order #', NEW.order_id, ' confirmed for qty ', NEW.quantity),
>         NOW()
>     );
> END //
> 
> DELIMITER ;
> ```

---

[← Master Index](00_Index.md) | [📐 Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md)
