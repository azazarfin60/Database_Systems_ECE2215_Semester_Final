---
title: "T03 · Relational Model, Keys and Integrity · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T02 · E-R and EER Modeling](T02_ER_and_EER_Modeling.md) | [Explanation layer](../Topicwise_answers_explaination/T03_Relational_Model_Keys_and_Integrity.md) | [Next: T04 · Relational Algebra and Calculus →](T04_Relational_Algebra_and_Calculus.md)

---

# T03 · Relational Model, Keys & Integrity

> [!info] Topic card
> **Syllabus:** Unit 3 · **Weight:** 28 final marks (4.4%) in 5/7 papers + 5 CT marks
> **Sources:** Deck 02, Deck 03, Deck 06 · Textbook Ch. 2, Ch. 4
> **Blocks in this file:** 7 final + 1 CT questions (6 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T03.1 | Relation, tuple, attribute, domain; domain vs data type | 2 + 0 | 2018 Q.3(b) | [[#T03.1 · Relation, tuple, attribute, domain; domain vs data type\|Go]] |
| T03.2 | Keys: super / candidate / primary / alternate / composite / foreign | 21 + 0 | 2018 Q.2(a), 2019 Q.6(b), 2020 Q.2(b), 2021 Q.2(b), 2023 Q.3(b) | [[#T03.2 · Keys: super / candidate / primary / alternate / composite / foreign\|Go]] |
| T03.3 | Referential integrity & FK syntax (MySQL) | 5 + 0 | 2021 Q.1(c) | [[#T03.3 · Referential integrity & FK syntax (MySQL)\|Go]] |
| T03.4 | Schema diagrams | 0 + 5 | CT-01 Q.02 | [[#T03.4 · Schema diagrams\|Go]] |

---

## T03.1 · Relation, tuple, attribute, domain; domain vs data type

### 2018 Q.3(b) · 02 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** Differentiate between domain and data type.

**Answer.**

A **domain** is the logical set of all valid values that an attribute can take. It defines real-world meaning and business constraints.  
A **data type** is a physical storage format recognized by the computer hardware and DBMS. It defines memory layout and low-level bit representation.

| Comparison Point | Domain | Data Type |
| :--- | :--- | :--- |
| **Concept Level** | Conceptual and semantic level. It reflects business meaning. | Physical implementation level. It specifies storage layout. |
| **Values Allowed** | Strict set of valid real-world values (for example, letter grades `{'A', 'B', 'C', 'F'}`). | Broad machine-level value range (for example, `CHAR(2)` accepts any two characters). |
| **Constraints** | Carries logical rules and business checks (such as `age >= 18`). | Only restricts memory size and storage category (such as `INT`). |
| **Equivalence** | Two attributes with the same data type can have different domains. | Two attributes share the same data type if their storage format matches. |

*Example:* `student_age` and `monthly_salary` can both use the `INT` data type. But they belong to different domains. Adding an age to a salary makes no logical sense.

---

## T03.2 · Keys: super / candidate / primary / alternate / composite / foreign

### 2023 Q.3(b) · 04 Marks

*Section A · CLO2 · Asked in: 2018 (4 marks), 2021 (CLO1, 3 marks), 2023 (4 marks) · L2 merge*

**Question (2023 Q.3(b)).** Explain the distinctions among the terms-  
(i) Primary key  
(ii) Candidate key  
(iii) Super key  
(iv) Composite key

**Question (2018 Q.2(a)).** Explain the distinctions among the terms primary key, candidate key, and super key with proper example.

**Question (2021 Q.2(b)).** Differentiate among Superkey, Candidate Key and Primary Key with an appropriate example.

**Answer.**

A key is an attribute or set of attributes used to identify rows in a table.

**Distinctions Among Keys:**

| Key Type | Definition | Minimality | NULL Allowed |
| :--- | :--- | :--- | :--- |
| **(i) Primary Key** | The candidate key chosen by the database designer to identify tuples uniquely. | Yes (minimal) | No (never allowed) |
| **(ii) Candidate Key** | A minimal super key. Removing any attribute destroys uniqueness. | Yes (strictly minimal) | Yes (unless constrained `NOT NULL`) |
| **(iii) Super Key** | Any set of attributes that uniquely identifies a row. May contain extra attributes. | No (can have redundant attributes) | No for identifying columns |
| **(iv) Composite Key** | A key that consists of two or more attributes rather than a single attribute. | Can be minimal (candidate) or non-minimal | Depends on whether it is PK or unique |

**Relationship:**
$$
\text{Primary Key} \subseteq \text{Candidate Keys} \subseteq \text{Super Keys}
$$

**Running Example:**  
Consider relation $\text{Student}(\underline{\text{student\_id}}, \text{name}, \text{email}, \text{nid}, \text{dept\_name})$:

| student_id | name | email | nid | dept_name |
| :--- | :--- | :--- | :--- | :--- |
| 101 | Akib | akib@gmail.com | 1999123456 | ECE |
| 102 | Shuvo | shuvo@gmail.com | 2000654321 | ECE |
| 103 | Sakib | sakib@gmail.com | 2001987654 | ETE |

- **Super Key:** Any set containing a candidate key. Examples: $\{\text{student\_id}\}$, $\{\text{email}\}$, $\{\text{student\_id}, \text{name}\}$, $\{\text{email}, \text{dept\_name}\}$.
- **Candidate Key:** Minimal sets with no extra columns: $\{\text{student\_id}\}$, $\{\text{email}\}$, $\{\text{nid}\}$.
- **Primary Key:** The chosen identifier: $\{\text{student\_id}\}$.
- **Composite Key:** In table $\text{Takes}(\underline{\text{student\_id}}, \underline{\text{course\_id}}, \text{grade})$, the combination $\{\text{student\_id}, \text{course\_id}\}$ forms a composite candidate and primary key. Neither column alone identifies an enrollment record.

*Short version for 2018 Q.2(a) (4 marks):* Omit (iv) Composite key. Keep the definitions, distinctions table, and the Student running example for Super Key, Candidate Key, and Primary Key.  
*Short version for 2021 Q.2(b) (3 marks):* Same as 2018 Q.2(a). Present the 3-row distinction table and the Student relation key classification.

---

### 2019 Q.6(b) · 06 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Discuss the different keys in DBMS. Write down the importance and use of foreign key with example.

**Answer.**

**1. Different Keys in DBMS:**
- **Super Key:** An attribute or group of attributes that uniquely identifies each tuple in a table. It can include redundant attributes. Example: $\{\text{student\_id}, \text{name}\}$.
- **Candidate Key:** A minimal super key with no redundant attributes. Removing any attribute breaks uniqueness. Example: $\{\text{student\_id}\}$, $\{\text{email}\}$.
- **Primary Key:** The candidate key selected by the designer to uniquely identify records. It cannot be NULL. Example: $\{\text{student\_id}\}$.
- **Alternate Key (Secondary Key):** Any candidate key that was not chosen as the primary key. Example: $\{\text{email}\}$, $\{\text{nid}\}$.
- **Composite Key:** A key that consists of two or more attributes. Example: $\{\text{student\_id}, \text{course\_id}\}$ in table $\text{Takes}$.
- **Foreign Key:** An attribute in a table that references the primary key of another table.

**2. Importance and Use of Foreign Key:**
- **Referential Integrity:** It guarantees that child rows point to valid parent rows. It prevents orphan or dangling records.
- **Table Relationships:** It links independent tables together without duplicating non-key data. This avoids update anomalies.
- **Automated Consistency:** It supports cascading actions (`CASCADE`, `SET NULL`, `RESTRICT`). When parent records change, child records update or delete automatically.

**Example:**  
Consider two relations:
- Parent table: $\text{Department}(\underline{\text{dept\_name}}, \text{building}, \text{budget})$
- Child table: $\text{Student}(\underline{\text{student\_id}}, \text{name}, \text{email}, \text{dept\_name})$

Here, `dept_name` in $\text{Student}$ is a foreign key referencing `dept_name` in $\text{Department}$.
- **Use:** If student 101 enrolls in `'ECE'`, `'ECE'` must exist in $\text{Department}$.
- **Protection:** If a user tries to insert a student with `dept_name = 'Civil'`, and `'Civil'` is not in $\text{Department}$, the DBMS rejects the insert. This protects database integrity.

---

### 2020 Q.2(b) · 04 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Write short note about: Super Key, Candidate Key, Primary Key, and Foreign Key.

**Answer.**

**1. Super Key:**
- **Definition:** A set of one or more attributes that uniquely identifies a tuple in a relation.
- **Features:** It can have extra attributes. If $K$ is a super key, any superset of $K$ is also a super key.
- **Example:** In $\text{Student}(\underline{\text{student\_id}}, \text{name}, \text{email}, \text{dept\_name})$, both $\{\text{student\_id}\}$ and $\{\text{student\_id}, \text{name}\}$ are super keys.

**2. Candidate Key:**
- **Definition:** A minimal super key. No proper subset can uniquely identify a tuple.
- **Features:** It has zero redundant attributes. A table can have multiple candidate keys.
- **Example:** Both $\{\text{student\_id}\}$ and $\{\text{email}\}$ are candidate keys for $\text{Student}$.

**3. Primary Key:**
- **Definition:** The specific candidate key chosen by the database designer to identify rows.
- **Features:** Must be unique and cannot contain NULL (`NOT NULL`). It should rarely or never change.
- **Example:** $\{\text{student\_id}\}$ is chosen as the primary key of $\text{Student}$.

**4. Foreign Key:**
- **Definition:** An attribute in a referencing table that matches the primary key of a referenced table.
- **Features:** It enforces referential integrity. Every value must match an existing parent key or be NULL.
- **Example:** `dept_name` in $\text{Student}$ is a foreign key referencing $\text{Department}(\text{dept\_name})$.

---

## T03.3 · Referential integrity & FK syntax (MySQL)

### 2021 Q.1(c) · 05 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** How do we achieve referential integrity in DBMS? Provide necessary MySQL query with an appropriate example.

**Answer.**

**1. How Referential Integrity is Achieved in DBMS:**  
Referential integrity ensures that relationships between tables remain consistent. It requires that any foreign key value in a referencing table must exist as a primary key value in the referenced table, or be NULL.  
A DBMS achieves referential integrity through three mechanisms:
1. **Constraint Declaration:** The database designer defines foreign keys in the DDL schema using the `FOREIGN KEY ... REFERENCES` clause.
2. **Active Violation Checking:** The DBMS monitors `INSERT`, `UPDATE`, and `DELETE` commands. It blocks any operation that creates orphan child records.
3. **Automated Referential Actions:** The designer specifies rules for parent modifications:
   - `CASCADE`: Deleting or updating a parent row automatically deletes or updates matching child rows.
   - `SET NULL`: Sets child foreign key columns to NULL when the parent row is deleted or updated.
   - `RESTRICT` / `NO ACTION`: Default rule; rejects parent deletion or update if matching child rows exist.

**2. MySQL DDL Query Example:**

```sql
-- Parent table (Referenced relation)
CREATE TABLE Department (
    dept_name VARCHAR(20) PRIMARY KEY,
    building VARCHAR(20),
    budget DECIMAL(12, 2)
);

-- Child table (Referencing relation)
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept_name VARCHAR(20),
    FOREIGN KEY (dept_name) REFERENCES Department(dept_name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

**3. Operation and Violation Demonstration:**  
Populate a valid parent department:

```sql
INSERT INTO Department VALUES ('ECE', 'Academic Building 2', 500000.00);
INSERT INTO Student VALUES (101, 'Akib', 'ECE'); -- Allowed
```

Now attempt a violating insert with a nonexistent department:

```sql
INSERT INTO Student VALUES (102, 'Shuvo', 'ME');
```

**MySQL System Response:**  
MySQL rejects the insert and raises an integrity violation error:

```text
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`university`.`Student`, CONSTRAINT `student_ibfk_1` FOREIGN KEY (`dept_name`) REFERENCES `Department` (`dept_name`) ON DELETE CASCADE ON UPDATE CASCADE)
```

If `'ECE'` is deleted from `Department`, `ON DELETE CASCADE` automatically deletes student 101. This keeps the database consistent.

---

## T03.4 · Schema diagrams

### CT-01 Q.02 · 05 Marks

*Class Test 01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Draw a schema diagram for ECE, including 5 tables (Students, Courses, Instructors, Classroom, Results).

**Answer.**

**1. Relational Schemas and Keys:**
- $\text{Students}(\underline{\text{student\_id}}, \text{name}, \text{email}, \text{dept\_name})$
- $\text{Instructors}(\underline{\text{instructor\_id}}, \text{name}, \text{dept\_name}, \text{salary})$
- $\text{Classroom}(\underline{\text{building}}, \underline{\text{room\_number}}, \text{capacity})$
- $\text{Courses}(\underline{\text{course\_id}}, \text{title}, \text{credits}, \text{instructor\_id}, \text{building}, \text{room\_number})$
  - $\text{instructor\_id} \rightarrow \text{Instructors}(\text{instructor\_id})$
  - $(\text{building}, \text{room\_number}) \rightarrow \text{Classroom}(\text{building}, \text{room\_number})$
- $\text{Results}(\underline{\text{student\_id}}, \underline{\text{course\_id}}, \underline{\text{semester}}, \text{marks}, \text{grade})$
  - $\text{student\_id} \rightarrow \text{Students}(\text{student\_id})$
  - $\text{course\_id} \rightarrow \text{Courses}(\text{course\_id})$

**2. Relational Schema Diagram:**  
In Silberschatz style, each table is shown as a box with its attributes. Primary keys are underlined. Directed arrows point from foreign key attributes to the referenced primary keys.

![ECE Relational Database Schema Diagram](diagrams/T03_CT01_Q02_ece_schema_diagram.jpg)
*Figure: Relational schema diagram for ECE with 5 tables and foreign key references.*

---

[← Prev: T02 · E-R and EER Modeling](T02_ER_and_EER_Modeling.md) | [Explanation layer](../Topicwise_answers_explaination/T03_Relational_Model_Keys_and_Integrity.md) | [Next: T04 · Relational Algebra and Calculus →](T04_Relational_Algebra_and_Calculus.md)
