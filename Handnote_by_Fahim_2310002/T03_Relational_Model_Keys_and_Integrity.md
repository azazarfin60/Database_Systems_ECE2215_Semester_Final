# T03: Relational Model, Keys & Integrity — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 3 | `subtopicwise_list.md` T03 (28 marks · 4.4% · 5/7)  
**Source Pages:** Page 18 (Terminologies), Page 36 (Keys), Page 37 (Constraints & FK), Page 46–47 (Foreign Key Cascading)

---

<!-- Page 18 -->

### Terminologies

- $\rightarrow$ **Database Schema:** Description of a database. It is just a plan or a layout or a blueprint of the database.
- $\rightarrow$ **Schema Diagram:** Displayed schema.

![Fig_p018_01: Schema diagram displaying the Student relation schema with attributes Name, Roll, Branch, and Address](diagrams/p018_fig01.jpg)
*Figure 18.1 — Schema diagram for Student relation (Page 18)*

- $\rightarrow$ **Schema Construct:** Each object within the schema. Ex. Student, Course etc.

---

<!-- Page 36 -->

## Keys

### Primary Key

* It is a column (or set of columns) in a table that uniquely identifies each row (a unique id).
* There is only 1 primary key & it should be **NOT NULL**.

### Foreign Key

* A foreign key is a column (or set of columns) in a table that refers to the primary key.
* There can be multiple foreign keys.
* Foreign keys can have duplicate & null values.

### Table Relationship Example

![p036_fig01: Student and City tables illustrating Primary Key and Foreign Key relationship](diagrams/p036_fig01.jpg)
*Figure 8 — Primary Key and Foreign Key Relationship (Page 36)*

#### Table 1 — Student

| id (PK) | name | cityId (FK) | city |
| :---: | :--- | :---: | :--- |
| 101 | Fahim | 1 | Dhaka |
| 102 | Shishir | 2 | Jashore |
| 103 | Sneha | 3 | Khulna |
| 104 | Shikta | 1 | Dhaka |

#### Table 2 — City

| id (PK) | city_name |
| :---: | :--- |
| 1 | Dhaka |
| 2 | Jashore |
| 3 | Khulna |

> [!NOTE] বাংলা ব্যাখ্যা (Bengali Explanation)
> Foreign key হলো অন্য একটা table এর Primary key যদি একটা Table এ use হয় সেটা। FK এর value unique হওয়ার প্রয়োজনীয়তা নাই।

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

<!-- Page 46 -->

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
