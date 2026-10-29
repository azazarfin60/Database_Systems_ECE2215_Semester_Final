---
title: "T03 · Relational Model, Keys and Integrity · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T02 · E-R and EER Modeling](T02_ER_and_EER_Modeling.md) | [Exam-style layer](../Topicwise_answers_exam_style/T03_Relational_Model_Keys_and_Integrity.md) | [Next: T04 · Relational Algebra and Calculus →](T04_Relational_Algebra_and_Calculus.md)

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

**What the examiner wants.**  
A concise conceptual distinction between domain and data type. The mark split is 1 mark for definitions and 1 mark for comparison points with a clear example.

**Key idea.**  
A data type describes how computer hardware stores data in memory (such as integer or text). A domain describes what data means in the real world (such as student age or course grades). Two attributes can share the same data type but belong to totally different domains.

**Step-by-step solution.**  
A **domain** is the logical set of all valid values that an attribute can take. It defines real-world meaning and business constraints.  
A **data type** is a physical storage format recognized by the computer hardware and DBMS. It defines memory layout and low-level bit representation.

| Comparison Point | Domain | Data Type |
| :--- | :--- | :--- |
| **Concept Level** | Conceptual and semantic level. It reflects business meaning. | Physical implementation level. It specifies storage layout. |
| **Values Allowed** | Strict set of valid real-world values (for example, letter grades `{'A', 'B', 'C', 'F'}`). | Broad machine-level value range (for example, `CHAR(2)` accepts any two characters). |
| **Constraints** | Carries logical rules and business checks (such as `age >= 18`). | Only restricts memory size and storage category (such as `INT`). |
| **Equivalence** | Two attributes with the same data type can have different domains. | Two attributes share the same data type if their storage format matches. |

*Example:* `student_age` and `monthly_salary` can both use the `INT` data type. But they belong to different domains. Adding an age to a salary makes no logical sense.

**Check.**  
*Quick self-test:*
- Q: Can two columns have the same data type but different domains?  
  A: Yes. `roll_number` and `bus_fare` can both be `INT`, but comparing them is semantically meaningless.
- Q: Where does a domain operate compared to a data type?  
  A: A domain operates at the logical or conceptual layer. A data type operates at the physical storage layer.

> [!warning] Common mistakes
> - Treating a domain as merely a synonym for an SQL data type. A domain is a broader relational concept that includes semantic constraints.
> - Forgetting that SQL uses `CHECK` constraints and user-defined types to approximate domains.
> - Writing a long essay instead of a 4-row comparison table.

**Exam tip.**  
Use a comparison table with four rows. Always add the age versus salary example to secure the full 2 marks.

**Sources.**  
- [Deck 02 · Slide 4](../LectureSlides/02_Relational_Model.md)  
- [Deck 03 · Slide 6](../LectureSlides/03_Introduction_to_SQL.md)  
- [Textbook Ch. 2 §2.1](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)

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

**What the examiner wants.**  
Precise definitions and clear distinctions among the four key types. The mark split is 1 mark per key type. The examiner expects minimality rules, nullability constraints, and an illustrative relational table.

**Key idea.**  
Think of a super key as any attribute set that uniquely identifies a row. A candidate key is a minimal super key: removing any attribute ruins uniqueness. The primary key is the single candidate key chosen by the database designer. A composite key is any key consisting of two or more attributes.

**Step-by-step solution.**  
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

**Check.**  
*Minimality and closure verification:*
- For $\{\text{student\_id}, \text{name}\}$: It uniquely identifies each tuple, so it is a super key. But its subset $\{\text{student\_id}\}$ is also unique. So it has an extraneous attribute (`name`) and cannot be a candidate key.
- For $\{\text{student\_id}\}$: No proper subset exists (except empty set). So it is strictly minimal and qualifies as a candidate key.

> [!warning] Common mistakes
> - Confusing super keys with candidate keys. A candidate key must be minimal; a super key can have extra attributes.
> - Believing a composite key is a separate fourth category. Any super, candidate, or primary key with multiple attributes is a composite key.
> - Forgetting to state that a primary key prohibits NULL values.

**Exam tip.**  
Write down the subset formula $\text{Primary Key} \subseteq \text{Candidate Keys} \subseteq \text{Super Keys}$ right above your example. This gives the examiner an instant visual proof of your grasp.

**Sources.**  
- [Deck 02 · Slide 7](../LectureSlides/02_Relational_Model.md)  
- [Deck 06 · Slides 11–13](../LectureSlides/06_DBMS_Normalization.md)  
- [Textbook Ch. 2 §2.3](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)

---

### 2019 Q.6(b) · 06 Marks

*Section B · Asked in: 2019 · L1 (asked once)*

**Question.** Discuss the different keys in DBMS. Write down the importance and use of foreign key with example.

**Answer.**

**What the examiner wants.**  
A comprehensive answer covering all major DBMS key types (~3 marks) and a detailed discussion of foreign key role, importance, cascading actions, and an example (~3 marks).

**Key idea.**  
Keys organize tables and preserve database integrity. The foreign key links independent relations together. It prevents orphan records by requiring every referenced value to exist in a parent relation.

**Step-by-step solution.**  
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

**Check.**  
*Referential integrity trace:*
- Parent record: `Department('ECE', 'Academic Building 2', 500000.00)`.
- Valid insert: `Student(101, 'Akib', 'akib@gmail.com', 'ECE')` succeeds because `'ECE'` exists in `Department`.
- Invalid insert: `Student(102, 'Shuvo', 'shuvo@gmail.com', 'Civil')` fails if `'Civil'` is absent from `Department`.

> [!warning] Common mistakes
> - Leaving out Alternate Key or Composite Key when asked to discuss different keys.
> - Stating that foreign keys can only reference other foreign keys. Foreign keys reference a primary key or candidate key.
> - Failing to provide a concrete two-table example showing referenced and referencing roles.

**Exam tip.**  
Divide your answer into two clear sections: "1. Different Keys in DBMS" and "2. Importance and Use of Foreign Key". This matches the two questions in the prompt.

**Sources.**  
- [Deck 02 · Slide 7](../LectureSlides/02_Relational_Model.md)  
- [Deck 06 · Slides 11–13](../LectureSlides/06_DBMS_Normalization.md)  
- [Textbook Ch. 2 §2.3](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)  
- [Textbook Ch. 4 §4.4.5](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

### 2020 Q.2(b) · 04 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Write short note about: Super Key, Candidate Key, Primary Key, and Foreign Key.

**Answer.**

**What the examiner wants.**  
Four distinct short notes. The mark split is 1 mark per key. Each short note must provide a definition, its core technical property, and a concrete example.

**Key idea.**  
Do not write long essays for short notes. Provide a clean structure for each key: Definition, Key Property, and Example using a single table.

**Step-by-step solution.**  
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

**Check.**  
*Self-test check:*
- Can a candidate key contain NULL values? Yes, in SQL unique columns, unless constrained `NOT NULL`.
- Can a primary key contain NULL values? Never. Relational theory and SQL standards forbid NULLs in primary keys.
- Can a foreign key be NULL? Yes, indicating an unassigned or optional relationship.

> [!warning] Common mistakes
> - Writing unstructured text blocks with missing examples.
> - Defining candidate key vaguely instead of emphasizing the minimality condition.
> - Forgetting to mention that foreign keys connect child tables to parent primary keys.

**Exam tip.**  
Spend about 2.5 minutes per note. Keep all examples rooted in the same `Student` table to save precious exam time.

**Sources.**  
- [Deck 02 · Slide 7](../LectureSlides/02_Relational_Model.md)  
- [Deck 06 · Slide 11](../LectureSlides/06_DBMS_Normalization.md)  
- [Textbook Ch. 2 §2.3](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)

---

## T03.3 · Referential integrity & FK syntax (MySQL)

### 2021 Q.1(c) · 05 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** How do we achieve referential integrity in DBMS? Provide necessary MySQL query with an appropriate example.

**Answer.**

**What the examiner wants.**  
An explanation of how a DBMS enforces referential integrity (~2 marks) plus valid, executable MySQL DDL and DML queries showing table creation, constraints, violating insert behavior, and cascading options (~3 marks).

**Key idea.**  
Referential integrity prevents orphan child records. In MySQL, you define it using `FOREIGN KEY ... REFERENCES ...`. When someone attempts to insert a child row pointing to a nonexistent parent row, MySQL blocks the command with Error 1452.

**Step-by-step solution.**  
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

**Check.**  
*MySQL execution trace:*
- `INSERT INTO Department VALUES ('ECE', ...)`: Row added.
- `INSERT INTO Student VALUES (101, 'Akib', 'ECE')`: Check verifies that `'ECE'` exists in `Department.dept_name`. Insertion succeeds.
- `INSERT INTO Student VALUES (102, 'Shuvo', 'ME')`: Check discovers `'ME'` is absent from `Department.dept_name`. Transaction halts with `ERROR 1452`.

> [!warning] Common mistakes
> - Creating the referencing table before the referenced table. The referenced table must be created first.
> - Omitting the column list in `REFERENCES Department(dept_name)`. MySQL requires the explicit referenced column.
> - Forgetting to demonstrate what happens during an integrity violation.

**Exam tip.**  
Write both the `CREATE TABLE` statements and the violating `INSERT` statement. Quoting MySQL Error 1452 shows genuine practical database expertise.

**Sources.**  
- [Deck 03 · Slides 8–10](../LectureSlides/03_Introduction_to_SQL.md)  
- [Textbook Ch. 4 §4.4.5](../Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)

---

## T03.4 · Schema diagrams

### CT-01 Q.02 · 05 Marks

*Class Test 01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Draw a schema diagram for ECE, including 5 tables (Students, Courses, Instructors, Classroom, Results).

**Answer.**

**What the examiner wants.**  
A complete Silberschatz-style relational schema diagram containing the five designated ECE tables: `Students`, `Courses`, `Instructors`, `Classroom`, and `Results`. The examiner looks for:
1. One rectangular box per table with attributes listed inside.
2. Primary keys clearly underlined.
3. Directed arrows connecting referencing foreign key attributes to referenced primary keys.

**Key idea.**  
A relational schema diagram provides a complete architectural map of a relational database. It displays tables as boxes, underlines primary keys, and uses arrows to indicate foreign key dependencies.

**Step-by-step solution.**  
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

**Check.**  
*Schema design audit:*
- All 5 specified tables are included: `Students`, `Courses`, `Instructors`, `Classroom`, `Results`.
- Every table has at least one underlined primary key.
- All foreign key relationships point to existing primary keys:
  - `Courses.instructor_id` $\rightarrow$ `Instructors.instructor_id`
  - `Courses.(building, room_number)` $\rightarrow$ `Classroom.(building, room_number)`
  - `Results.student_id` $\rightarrow$ `Students.student_id`
  - `Results.course_id` $\rightarrow$ `Courses.course_id`
- The relations form a fully connected, coherent schema graph.

> [!warning] Common mistakes
> - Drawing an Entity-Relationship (ER) diagram with diamonds and ellipses instead of a relational schema diagram with rectangular boxes.
> - Reversing arrow directions. In Silberschatz schema diagrams, arrows must originate at the child foreign key and point to the parent primary key.
> - Forgetting that `Classroom` uses a composite primary key consisting of both `building` and `room_number`.

**Exam tip.**  
Write out the relational schema text lines first ($\text{Students}(\dots)$) to organize the primary and foreign keys in your head. Then draw the table boxes and connect the arrows.

**Sources.**  
- [Deck 02 · Slide 8](../LectureSlides/02_Relational_Model.md)  
- [Textbook Ch. 2 §2.4](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)

---

[← Prev: T02 · E-R and EER Modeling](T02_ER_and_EER_Modeling.md) | [Exam-style layer](../Topicwise_answers_exam_style/T03_Relational_Model_Keys_and_Integrity.md) | [Next: T04 · Relational Algebra and Calculus →](T04_Relational_Algebra_and_Calculus.md)
