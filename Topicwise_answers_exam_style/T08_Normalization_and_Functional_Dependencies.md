---
title: "T08 · Normalization and Functional Dependencies · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T07 · Triggers and Stored Procedures](T07_Triggers_and_Stored_Procedures.md) | [Explanation layer](../Topicwise_answers_explaination/T08_Normalization_and_Functional_Dependencies.md) | [Next: T09 · Transactions, ACID, and Anomalies →](T09_Transactions_ACID_and_Anomalies.md)

---

# T08 · Normalization and Functional Dependencies

> [!info] Topic card
> **Syllabus:** Unit 5 · **Weight:** 75 final marks (11.8%) in 7/7 papers + 20 CT marks
> **Sources:** Deck 06 · Textbook Ch. 7 (§7.1–7.5, §7.8)
> **Blocks in this file:** 16 final + 6 CT questions (19 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T08.1 | Why normalize: redundancy and insert/update/delete anomalies | 18 + 3 | 2018 Q.4(a), 2019 Q.6(a), 2021 Q.6(c), 2023 Q.2(b), CT-03 Q.02 | [[#T08.1 · Why normalize: redundancy and insert/update/delete anomalies\|Go]] |
| T08.2 | FDs: trivial, full/partial, transitive; prime vs non-prime attributes | 0 + 4 | CT-03 Q.01(b–c) | [[#T08.2 · FDs: trivial, full/partial, transitive; prime vs non-prime attributes\|Go]] |
| T08.3 | Armstrong's axioms | 0 + 0 | No questions | [[#T08.3 · Armstrong's axioms\|Go]] |
| T08.4 | Attribute closure X+, F+, finding candidate keys | 4 + 4 | 2021 Q.5(b), CT-03 Q.01(a) | [[#T08.4 · Attribute closure X+, F+, finding candidate keys\|Go]] |
| T08.5 | Canonical cover Fc (and how it differs from normalization) | 8 + 0 | 2021 Q.6(a), 2021 Q.6(b) | [[#T08.5 · Canonical cover Fc (and how it differs from normalization)\|Go]] |
| T08.6 | Define normalization (and its importance) & 1NF / 2NF / 3NF | 14 + 3 | 2017 Q.3(a), 2017 Q.8(c), 2018 Q.4(c), 2019 Q.3(a), CT-03 Q.03 | [[#T08.6 · Define normalization (and its importance) & 1NF / 2NF / 3NF\|Go]] |
| T08.7 | 2NF test from an FD set | 4 + 0 | 2021 Q.5(c) | [[#T08.7 · 2NF test from an FD set\|Go]] |
| T08.8 | Normalize an unnormalized table → 1NF → 2NF → 3NF | 27 + 0 | 2017 Q.3(b), 2020 Q.8(b), 2023 Q.2(a), 2024 Q.3(a) | [[#T08.8 · Normalize an unnormalized table → 1NF → 2NF → 3NF\|Go]] |
| T08.9 | BCNF; 3NF vs BCNF; highest normal form | 0 + 6 | CT-03 Q.01(d), CT-03 Q.04 | [[#T08.9 · BCNF; 3NF vs BCNF; highest normal form\|Go]] |
| T08.10 | Pros/cons of normalization; denormalization | 0 + 0 | No questions | [[#T08.10 · Pros/cons of normalization; denormalization\|Go]] |
| T08.11 | Lossless-join decomposition & dependency preservation | 0 + 0 | No questions | [[#T08.11 · Lossless-join decomposition & dependency preservation\|Go]] |

---

## T08.1 · Why normalize: redundancy and insert/update/delete anomalies

### 2018 Q.4(a) · 04 Marks

*Section A · Asked in: 2018, CT-03 · L2 merge*

**Question (2018 Q.4(a)).** What problem may occur if databases are used without normalization? Discuss with proper example.

**Question (CT-03 Q.02).** Mention the problems caused by an unnormalized relation.

**Answer.**

Using databases without normalization causes four major problems:

1. **Data Redundancy:** The same facts are stored repeatedly in multiple rows. This wastes disk storage and slows down query processing.
2. **Update Anomaly:** If a piece of data is stored in multiple records, modifying it requires updating all those records. If any row is missed, the database enters an inconsistent state.
3. **Insertion Anomaly:** New data cannot be recorded unless unrelated data is also present. For instance, a new course cannot be inserted without enrolling a student if the primary key includes the student ID.
4. **Deletion Anomaly:** Deleting one fact unintentionally erases another valid fact. For example, deleting the only student enrolled in a course deletes the course itself.

#### Example

Consider an unnormalized table storing student enrollment and instructor data:

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 01711... |
| S01 | Riad | AI | Dr. Abdullah | 01811... |
| S02 | Zoha | DBMS | Dr. Hasan | 01711... |

- **Redundancy:** The instructor name and phone for "DBMS" are stored twice.
- **Update Anomaly:** If Dr. Hasan changes his phone number, we must update both rows. If we update row 1 but miss row 3, Dr. Hasan has two different phone numbers.
- **Insertion Anomaly:** Suppose the university introduces a new course "ML" taught by Dr. Kamal. If no student has enrolled yet, we cannot insert this course because `Student_ID` is part of the primary key and cannot be `NULL`.
- **Deletion Anomaly:** If student S01 drops the "AI" course and row 2 is deleted, all information about Dr. Abdullah and the AI course is completely lost.

*Short version for CT-03 Q.02 (3 marks):* State the four problems (data redundancy, update anomaly, insertion anomaly, deletion anomaly). Give a brief two-line explanation and one table row example showing an inconsistent update.

---

### 2019 Q.6(a) · 06 Marks

*Section B · Asked in: 2019*

**Question.** Consider the following data tables.

**Student**  
<table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>Roll</th><th>Name</th><th>Dept</th><th>Sub Code</th><th>Sub Grade</th><th>Reg Sub Code</th></tr></thead><tbody><tr><td>1710001</td><td>Mr. A</td><td>ECE</td><td>ECE-2103</td><td>A+</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710002</td><td>Mr. B</td><td>ECE</td><td>ECE-2107</td><td>A</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710003</td><td>Mr. C</td><td>ECE</td><td>ECE-2103</td><td>A-</td><td>ECE-2103</td></tr><tr><td>1710004</td><td>Mr. D</td><td>ECE</td><td>ECE-2107</td><td>A+</td><td>ECE-2107</td></tr><tr><td>1710001</td><td>Mr. A</td><td>ECE</td><td>ECE-2107</td><td>A-</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710002</td><td>Mr. B</td><td>ECE</td><td>ECE-2103</td><td>A+</td><td>ECE-2103<br>ECE-2107</td></tr></tbody></table>  
Now,  
(i) Carefully notice the entries and point out your opinion regarding space efficiency.  
(ii) What will happen if you update any particular information?  
(iii) What will happen if you are asked to delete 'ECE-2107' from the registered course list preserving all other information?

**Answer.**

#### (i) Space Efficiency

The table is highly space-inefficient for three reasons:

1. **Repetitive Student Attributes:** The attributes `Name` ("Mr. A", "Mr. B") and `Dept` ("ECE") are repeated across multiple rows for the same `Roll`.
2. **Multi-valued and Redundant List:** The attribute `Reg Sub Code` contains multi-valued lists (e.g., `ECE-2103, ECE-2107`). Storing this composite list in every row for a student wastes substantial storage.
3. **Violation of First Normal Form:** Storing multiple course codes in a single cell violates 1NF atomicity. This requires extra variable-length string storage and complex string parsing during queries.

#### (ii) Consequences of Updating Information

Updating any student-level or course-level attribute causes an **update anomaly**:

- If student 1710001 changes his name or transfers to another department, all rows with Roll `1710001` must be updated.
- If a student registers for a new course, the multi-valued field `Reg Sub Code` must be modified across every row for that student.
- If any row is updated while another is missed, the database becomes inconsistent. For example, Roll `1710001` could end up with different department names or conflicting registered course lists in different rows.

#### (iii) Deleting 'ECE-2107' from Registered Course List

If asked to delete 'ECE-2107' from the registered course list while preserving all other data:

1. **For students with multiple registered courses (1710001, 1710002):** The database cannot simply delete rows. It must parse the multi-valued text in `Reg Sub Code` across all their records and strip 'ECE-2107'. This is slow and error-prone.
2. **For student 1710004 (Mr. D):** His only registered course is 'ECE-2107'. If 'ECE-2107' is removed:
   - Setting `Reg Sub Code` to `NULL` leaves an incomplete record.
   - If the business rule or primary key requires a valid course, deleting the row causes a **deletion anomaly**. It deletes Mr. D's roll number, name, department, and his grade for that course.

---

### 2021 Q.6(c) · 04 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Consider the following table:

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;"><u>st_id</u></th><th style="padding: 4px 10px;">Name</th><th style="padding: 4px 10px;">Course</th><th style="padding: 4px 10px;">Session</th><th style="padding: 4px 10px;">Fee</th><th style="padding: 4px 10px;">Dept</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">Devi</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">Sona</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">Varun</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">Satish</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">105</td><td style="padding: 4px 10px;">Amisha</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr></tbody></table>  
Is there any data redundancy in the above table? What kinds of problems/ anomalities it will produce for this table in future?

*(Note: "problems/ anomalities" printed verbatim from original question paper)*

**Answer.**

#### 1. Presence of Data Redundancy

**Yes, significant data redundancy exists.**

The attributes `Course` ("DBMS"), `Session` ("2022"), `Fee` ("90k"), and `Dept` ("CS") are duplicated across all 5 rows. In this schema, `Fee` and `Dept` depend on `Course`, not on the primary key `st_id`. Storing course-level attributes in every student record creates column-level duplication.

#### 2. Future Problems and Anomalies

1. **Storage Overhead:** Storing identical strings ("DBMS", "2022", "90k", "CS") for hundreds of students in the same course wastes physical storage.
2. **Update Anomaly:** If the fee for the DBMS course increases from 90k to 95k, every student record enrolled in DBMS must be updated. If one row is missed, students enrolled in the exact same course see conflicting fees.
3. **Insertion Anomaly:** If the department introduces a new course (e.g., "AI", Session "2022", Fee "85k") before any student enrolls, this course cannot be entered into the database. The primary key `st_id` cannot be `NULL` due to the Entity Integrity constraint.
4. **Deletion Anomaly:** If all students (101 to 105) complete the term or cancel their enrollment, deleting their records removes all 5 rows. This accidentally deletes all records of the DBMS course, its fee, and its department.

---

### 2023 Q.2(b) · 04 Marks

*Section A · CLO4 · Asked in: 2023*

**Question.** What are the anomalies that normalization aims to eliminate? Provide examples of insertion, deletion and update anomalies.

**Answer.**

Normalization aims to eliminate three modification anomalies caused by data redundancy and undesirable functional dependencies:

1. **Insertion Anomaly**
2. **Deletion Anomaly**
3. **Update Anomaly**

#### Example Table: `EMP_DEPT`

Consider an unnormalized table where employee and department facts share one relation:

| Emp_ID | Emp_Name | Dept_ID | Dept_Name | Location |
| :--- | :--- | :--- | :--- | :--- |
| E01 | Alice | D10 | IT | Building A |
| E02 | Bob | D20 | HR | Building B |
| E03 | Charlie | D10 | IT | Building A |

**Primary Key:** `Emp_ID`

#### 1. Insertion Anomaly
- **Problem:** We cannot insert information about a new department unless at least one employee is assigned to it.
- **Example:** The company opens a new department `D30` (Finance, Building C). Because `Emp_ID` is the primary key, it cannot be `NULL`. We cannot record department `D30` until an employee is hired.

#### 2. Deletion Anomaly
- **Problem:** Deleting an entity record accidentally deletes an unrelated entity.
- **Example:** Employee `E02` is the only person working in department `D20` (HR). If Bob resigns and we delete his row (`E02`), the fact that department `D20` is HR located in Building B is permanently erased.

#### 3. Update Anomaly
- **Problem:** Changing a single real-world fact requires modifying multiple records.
- **Example:** If the IT department (`D10`) moves to "Building D", we must update both rows E01 and E03. If the system updates E01 but fails on E03, department D10 has two conflicting locations.

---

## T08.2 · FDs: trivial, full/partial, transitive; prime vs non-prime attributes

### CT-03 Q.01(b-c) · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(b)** Identify the prime and non-prime attributes. `[02 Marks]`  
**(c)** Identify the partial and transitive dependencies. `[02 Marks]`

**Answer.**

First, we determine the Candidate Key.

Attributes $\text{StudentID}$ and $\text{CourseID}$ never appear on the right-hand side of any functional dependency. Therefore, every candidate key must contain both attributes.

Computing the closure:
$$
\begin{aligned}
\{\text{StudentID}, \text{CourseID}\}^+ &= \{\text{StudentID}, \text{CourseID}, \text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}\}
\end{aligned}
$$

Because no proper subset is a superkey, the unique Candidate Key is:
$$
\text{Candidate Key} = \{\text{StudentID}, \text{CourseID}\}
$$

#### (b) Prime and Non-Prime Attributes

- **Prime Attributes:** Attributes that belong to at least one Candidate Key.
$$
\text{Prime Attributes} = \{\text{StudentID}, \text{CourseID}\}
$$
- **Non-Prime Attributes:** Attributes that do not belong to any Candidate Key.
$$
\text{Non-Prime Attributes} = \{\text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}\}
$$

#### (c) Partial and Transitive Dependencies

- **Partial Dependencies:** Occur when a non-prime attribute depends on a proper subset of a composite candidate key:
  1. $\text{StudentID} \rightarrow \text{StudentName}$ (the non-prime attribute $\text{StudentName}$ depends only on $\text{StudentID}$).
  2. $\text{CourseID} \rightarrow \text{CourseName}$ (the non-prime attribute $\text{CourseName}$ depends only on $\text{CourseID}$).
  3. $\text{CourseID} \rightarrow \text{InstructorID}$ (the non-prime attribute $\text{InstructorID}$ depends only on $\text{CourseID}$).

- **Transitive Dependencies:** Occur when a non-prime attribute depends on another non-prime attribute:
$$
\text{InstructorID} \rightarrow \text{InstructorName}
$$
  Here, $\text{InstructorID}$ is a non-prime attribute that determines the non-prime attribute $\text{InstructorName}$. From the primary key, we have $(\text{StudentID}, \text{CourseID}) \rightarrow \text{InstructorID} \rightarrow \text{InstructorName}$.

---

## T08.3 · Armstrong's axioms

*No questions from past finals or class tests.*

*See also:* [[#T08.4 · Attribute closure X+, F+, finding candidate keys]] (2021 Q.5(b))

---

## T08.4 · Attribute closure X+, F+, finding candidate keys

### 2021 Q.5(b) · 04 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Compute the closure of the following set F of functional dependencies for relational schema r (A, B, C, D, E).

  $A \to BC$  
  $CD \to E$  
  $B \to D$  
  $E \to A$

List the candidate Keys for R.

**Answer.**

#### 1. Closure of Functional Dependencies ($F^+$)

The complete closure $F^+$ contains over one hundred trivial and non-trivial dependencies, which is too large to write out fully.

We compute the attribute closures of each single attribute and pair under $F$:

1. **$A^+$:**
   - Initial: $\{A\}$
   - Using $A \rightarrow BC$: $\{A, B, C\}$
   - Using $B \rightarrow D$: $\{A, B, C, D\}$
   - Using $CD \rightarrow E$: $\{A, B, C, D, E\}$
   - Result: $A^+ = \{A, B, C, D, E\}$

2. **$B^+$:**
   - Initial: $\{B\}$
   - Using $B \rightarrow D$: $\{B, D\}$
   - Result: $B^+ = \{B, D\}$

3. **$C^+$:**
   - No FD has $C$ on the LHS alone.
   - Result: $C^+ = \{C\}$

4. **$D^+$:**
   - No FD has $D$ on the LHS alone.
   - Result: $D^+ = \{D\}$

5. **$E^+$:**
   - Initial: $\{E\}$
   - Using $E \rightarrow A$: $\{E, A\}$
   - Since $A^+ = \{A, B, C, D, E\}$: $\{A, B, C, D, E\}$
   - Result: $E^+ = \{A, B, C, D, E\}$

6. **Key Two-Attribute Closures:**
   - $BC^+$: Using $B \rightarrow D$, we get $\{B, C, D\}$. Using $CD \rightarrow E$, we get $\{B, C, D, E\}$. Using $E \rightarrow A$, we get $\{A, B, C, D, E\}$. So $BC^+ = \{A, B, C, D, E\}$.
   - $CD^+$: Using $CD \rightarrow E$, we get $\{C, D, E\}$. Using $E \rightarrow A$, we get $\{A, C, D, E\}$. Using $A \rightarrow BC$, we get $\{A, B, C, D, E\}$. So $CD^+ = \{A, B, C, D, E\}$.

**Key Non-Trivial Functional Dependencies in $F^+$ (derived using Armstrong's Axioms):**
- $A \rightarrow D$ (by Decomposition of $A \rightarrow BC$ to $A \rightarrow B$, then Transitivity with $B \rightarrow D$).
- $A \rightarrow E$ (by Transitivity from $A \rightarrow CD$ and $CD \rightarrow E$).
- $E \rightarrow B, E \rightarrow C, E \rightarrow D$ (by Transitivity from $E \rightarrow A$ and $A \rightarrow BCDE$).
- $BC \rightarrow E$ (by Augmentation of $B \rightarrow D$ to $BC \rightarrow CD$, then Transitivity with $CD \rightarrow E$).
- $CD \rightarrow A, CD \rightarrow B$ (by Transitivity from $CD \rightarrow E$, $E \rightarrow A$, and $A \rightarrow B$).

#### 2. Candidate Keys for $R$

A candidate key is a minimal set of attributes whose closure contains all attributes $\{A, B, C, D, E\}$.

- $A^+ = \{A, B, C, D, E\} \implies \{A\}$ is a candidate key.
- $E^+ = \{A, B, C, D, E\} \implies \{E\}$ is a candidate key.
- $BC^+ = \{A, B, C, D, E\}$, while neither $B^+$ nor $C^+$ is a superkey $\implies \{BC\}$ is a candidate key.
- $CD^+ = \{A, B, C, D, E\}$, while neither $C^+$ nor $D^+$ is a superkey $\implies \{CD\}$ is a candidate key.

$$
\text{Candidate Keys} = \{A\}, \{E\}, \{BC\}, \{CD\}
$$

---

### CT-03 Q.01(a) · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(a)** Identify all the possible candidate key of the relation.

**Answer.**

To find all candidate keys, we analyze the attributes that must appear in every key.

1. **Attributes not on any RHS:**
   Examining the right-hand sides of the given functional dependencies:
   - $\text{RHS} = \{\text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}\}$
   - Attributes $\text{StudentID}$ and $\text{CourseID}$ never appear on any right-hand side.
   - Therefore, $\{\text{StudentID}, \text{CourseID}\}$ must be present in every candidate key.

2. **Compute the Attribute Closure of $\{\text{StudentID}, \text{CourseID}\}$:**
   - **Step 1 (Initial):**  
     $X^+ = \{\text{StudentID}, \text{CourseID}\}$
   - **Step 2 (Apply $\text{StudentID} \rightarrow \text{StudentName}$):**  
     $X^+ = \{\text{StudentID}, \text{CourseID}, \text{StudentName}\}$
   - **Step 3 (Apply $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$):**  
     $X^+ = \{\text{StudentID}, \text{CourseID}, \text{StudentName}, \text{CourseName}, \text{InstructorID}\}$
   - **Step 4 (Apply $\text{InstructorID} \rightarrow \text{InstructorName}$):**  
     $X^+ = \{\text{StudentID}, \text{CourseID}, \text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}\}$
   - **Step 5 (Apply $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$):**  
     $X^+ = \{\text{StudentID}, \text{CourseID}, \text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}\}$

3. **Check for Minimality:**
   We check proper subsets of $\{\text{StudentID}, \text{CourseID}\}$:
   - $\{\text{StudentID}\}^+ = \{\text{StudentID}, \text{StudentName}\} \neq R$
   - $\{\text{CourseID}\}^+ = \{\text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}\} \neq R$

Neither proper subset determines all attributes. Therefore, $\{\text{StudentID}, \text{CourseID}\}$ is minimal.

$$
\boxed{\text{Candidate Key} = \{\text{StudentID}, \text{CourseID}\}}
$$

This is the only candidate key for the relation.

---

## T08.5 · Canonical cover Fc (and how it differs from normalization)

### 2021 Q.6(a) · 03 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Differentiate between normalization and canonical cover in DBMS.

**Answer.**

| Parameter | Normalization | Canonical Cover ($F_c$) |
| :--- | :--- | :--- |
| **Definition** | The process of decomposing relation schemas to eliminate redundancy and update/delete/insert anomalies. | A minimal, non-redundant set of functional dependencies equivalent to the original FD set ($F_c \equiv F$). |
| **Primary Goal** | Design high-integrity tables that eliminate anomalies and avoid data duplication. | Simplify the set of integrity constraints so DBMS updates can be validated with minimal overhead. |
| **Input** | A relation schema $R$ and its functional dependencies $F$. | A set of functional dependencies $F$. |
| **Output** | A collection of decomposed relations $\{R_1, R_2, \dots, R_k\}$ in a desired normal form (e.g., 3NF, BCNF). | A simplified functional dependency set $F_c$ with no extraneous attributes and unique left-hand sides. |
| **Level of Operation** | Operates on the schema design level (splitting tables and foreign keys). | Operates purely on the mathematical dependency level (simplifying FDs). |

---

### 2021 Q.6(b) · 05 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Define Functional dependency. Consider the following functional dependency set:

  $\text{FD} = \{$  
    $A \to BC,$  
    $CD \to E,$  
    $B \to D,$  
    $E \to A$  
  $\}$

Find the canonical form of the FD set.

**Answer.**

#### 1. Definition of Functional Dependency

A **functional dependency** (FD) is a constraint between two sets of attributes in a relation schema $R$.

Let $\alpha \subseteq R$ and $\beta \subseteq R$. The functional dependency:
$$
\alpha \rightarrow \beta
$$
holds on $R$ if, in every legal relation instance $r(R)$, whenever any two tuples $t_1$ and $t_2$ have the same values for attributes in $\alpha$, they must also have the same values for attributes in $\beta$:
$$
\text{If } t_1[\alpha] = t_2[\alpha] \implies t_1[\beta] = t_2[\beta]
$$

We say $\alpha$ functionally determines $\beta$.

#### 2. Finding the Canonical Cover ($F_c$)

A canonical cover $F_c$ satisfies two conditions:
1. No functional dependency contains an extraneous attribute (on the LHS or RHS).
2. Each left-hand side of a functional dependency is unique.

**Step 1: Apply the Union Rule to combine identical LHS**  
In the given set $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$, the left-hand sides are $A, CD, B, E$. All left-hand sides are already unique.

**Step 2: Test for Extraneous Attributes**

1. **Check $A \rightarrow BC$:**
   - **Test attribute $B$ (on RHS):**  
     Form $F' = \{A \rightarrow C, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.  
     Compute $A^+$ under $F'$:  
     $A^+ = \{A, C\}$.  
     $A^+$ does not contain $B$. Therefore, $B$ is **not extraneous**.
   - **Test attribute $C$ (on RHS):**  
     Form $F' = \{A \rightarrow B, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.  
     Compute $A^+$ under $F'$:  
     $A^+ = \{A, B, D\}$ (via $A \rightarrow B$ and $B \rightarrow D$).  
     $A^+$ does not contain $C$. Therefore, $C$ is **not extraneous**.

2. **Check $CD \rightarrow E$:**
   - **Test attribute $C$ (on LHS):**  
     Check if $D \rightarrow E$ holds under $F$.  
     Compute $D^+$ under $F$: $D^+ = \{D\}$.  
     $D^+$ does not contain $E$. Therefore, $C$ is **not extraneous**.
   - **Test attribute $D$ (on LHS):**  
     Check if $C \rightarrow E$ holds under $F$.  
     Compute $C^+$ under $F$: $C^+ = \{C\}$.  
     $C^+$ does not contain $E$. Therefore, $D$ is **not extraneous**.

3. **Check $B \rightarrow D$:**  
   Both LHS and RHS have a single attribute. Neither can be removed without dropping the dependency entirely.

4. **Check $E \rightarrow A$:**  
   Both LHS and RHS have a single attribute. Neither can be removed.

**Step 3: Resulting Canonical Cover**  
Since there are no extraneous attributes, the canonical cover is:

$$
\boxed{F_c = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}}
$$

*(Note: In minimal cover form with singleton right-hand sides, the equivalent set is $\{A \rightarrow B, A \rightarrow C, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$. Both representations are correct.)*

---

## T08.6 · Define normalization (and its importance) & 1NF / 2NF / 3NF

### 2017 Q.3(a) · 03 Marks

*Section A · Asked in: 2017, CT-03 · L2 merge*

**Question (2017 Q.3(a)).** What do you mean by normalization? Why normalization is important for database?

**Question (CT-03 Q.03).** Define normalization and state its main objective.

**Answer.**

#### 1. What is Normalization?

**Normalization** is a formal, systematic technique for designing relational database schemas. It decomposes relations with anomalies into smaller, well-structured relations to reduce data redundancy and ensure data integrity.

#### 2. Importance of Normalization (Main Objectives)

Normalization is essential for relational databases because it:

1. **Eliminates Unnecessary Data Redundancy:** Prevents storing the same facts repeatedly across multiple records, which conserves physical storage.
2. **Prevents Database Anomalies:** Completely removes insertion, deletion, and update anomalies that corrupt data during modifications.
3. **Ensures Data Consistency and Integrity:** Guarantees that an update applied to one record keeps all related facts accurate and consistent.
4. **Preserves Data Dependencies:** Ensures all real-world business constraints and functional dependencies can be enforced efficiently without complex cross-table joins.

*Short version for CT-03 Q.03 (3 marks):* Define normalization as the systematic decomposition of relations to minimize redundancy and eliminate anomalies. State the main objective: to produce well-structured tables free of insertion, update, and deletion anomalies while maintaining data consistency.

---

### 2017 Q.8(c) · 03 Marks

*Section B · Asked in: 2017*

**Question.** What is 1NF, 2NF and 3NF?

**Answer.**

1. **First Normal Form (1NF):**  
   A relation is in 1NF if and only if every attribute domain contains only **atomic (indivisible) values**, and each cell contains exactly one value. It strictly disallows multi-valued attributes, composite attributes, and repeating groups.

2. **Second Normal Form (2NF):**  
   A relation is in 2NF if and only if:
   - It is already in 1NF.
   - It contains **no partial functional dependencies**. Every non-prime attribute must be fully functionally dependent on the entire candidate key, rather than on a proper subset of it.

3. **Third Normal Form (3NF):**  
   A relation is in 3NF if and only if:
   - It is already in 2NF.
   - It contains **no transitive dependencies**. A non-prime attribute must not depend on another non-prime attribute. Formally, for every non-trivial functional dependency $X \rightarrow Y$, either $X$ is a superkey, or $Y$ consists entirely of prime attributes.

---

### 2019 Q.3(a) · 04 Marks

*Section A · Asked in: 2018, 2019 · L2 merge*

**Question (2019 Q.3(a)).** What is normalization? Discuss 1NF and 2NF.

**Question (2018 Q.4(c)).** Explain the rules of 1NF and 2NF with a proper example.

**Answer.**

#### 1. What is Normalization?

**Normalization** is the process of decomposing a relation schema into smaller schemas to minimize data redundancy and prevent insertion, deletion, and update anomalies.

#### 2. First Normal Form (1NF)

**Rules:**
- Every attribute must hold only atomic (single, indivisible) values.
- No multi-valued attributes or repeating groups are permitted.
- Each column must contain values of the same domain, and each row must be uniquely identifiable.

**Example:**

*Violating 1NF:*

| Student_ID | Name | Phone |
| :--- | :--- | :--- |
| S01 | Fahim | 01711, 01822 |
| S02 | Noor | 01933 |

*Converted to 1NF (atomic rows):*

| Student_ID | Name | Phone |
| :--- | :--- | :--- |
| S01 | Fahim | 01711 |
| S01 | Fahim | 01822 |
| S02 | Noor | 01933 |

PK: `(Student_ID, Phone)`

#### 3. Second Normal Form (2NF)

**Rules:**
- The relation must be in 1NF.
- There must be **no partial dependency**. No non-prime attribute can depend on a proper subset of any candidate key.

**Example:**

Consider relation `ENROLL(StudentID, CourseID, StudentName, Grade)`:
- Candidate Key: `(StudentID, CourseID)`
- Dependencies:
  - `(StudentID, CourseID) -> Grade` (Full dependency)
  - `StudentID -> StudentName` (Partial dependency on proper subset `StudentID`)

*Converted to 2NF (decompose to remove partial dependency):*
1. `STUDENT(StudentID, StudentName)` with PK `StudentID`
2. `ENROLLMENT(StudentID, CourseID, Grade)` with PK `(StudentID, CourseID)`

*Short version for 2018 Q.4(c) (4 marks):* State the rules for 1NF (atomicity, no multi-valued attributes) with the phone number example. State the rules for 2NF (in 1NF, no partial dependencies) with the student course example.

---

## T08.7 · 2NF test from an FD set

### 2021 Q.5(c) · 04 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Given a relation R (A, B, C, D) and functional dependency at FD = { AB $\to$ CD, B $\to$ C }. Determine whether the given R is in 2NF? If not, convert it into 2NF.

*(Note: "functional dependency at FD" printed verbatim from original question paper)*

**Answer.**

#### 1. Determine Candidate Key and Attribute Types

Given relation $R(A, B, C, D)$ and functional dependencies:
$$
FD = \{AB \rightarrow CD, B \rightarrow C\}
$$

- Attribute $A$ never appears on the right-hand side of any dependency. Thus, every candidate key must contain $A$.
- Compute closure of $AB$:
$$
AB^+ = \{A, B, C, D\}
$$
- Test proper subsets:
  - $A^+ = \{A\}$
  - $B^+ = \{B, C\}$
  Neither subset is a superkey. Therefore, $AB$ is minimal.

$$
\text{Candidate Key} = \{AB\}
$$
$$
\text{Prime Attributes} = \{A, B\}
$$
$$
\text{Non-Prime Attributes} = \{C, D\}
$$

#### 2. Test for Second Normal Form (2NF)

A relation is in 2NF if it is in 1NF and no non-prime attribute depends on a proper subset of any candidate key.

Examine the dependencies:
1. $AB \rightarrow CD$: The determinant $AB$ is the complete candidate key. This is a **full functional dependency**.
2. $B \rightarrow C$: The determinant $B$ is a proper subset of candidate key $AB$, and $C$ is a non-prime attribute. This is a **partial functional dependency**.

Because a partial dependency exists ($B \rightarrow C$), **the relation $R$ is NOT in 2NF**.

#### 3. Conversion to 2NF

To achieve 2NF, we decompose $R$ by isolating the partial dependency into its own relation:

1. Create a relation for the partial dependency:
$$
R_1(B, C) \quad \text{with } FD_1 = \{B \rightarrow C\}
$$
$$
\text{PK of } R_1 = B
$$

2. Remove the determined attribute $C$ from the original relation:
$$
R_2(A, B, D) \quad \text{with } FD_2 = \{AB \rightarrow D\}
$$
$$
\text{PK of } R_2 = AB
$$

**Verification:**
- In $R_1(B, C)$, the candidate key is $B$. The non-prime attribute $C$ depends on the entire key. $R_1$ is in 2NF.
- In $R_2(A, B, D)$, the candidate key is $AB$. The non-prime attribute $D$ depends on the full key $AB$. $R_2$ is in 2NF.
- Lossless join: $R_1 \cap R_2 = \{B\}$, which is the primary key of $R_1$. Thus, the decomposition is lossless.

$$
\boxed{\text{Decomposed 2NF Relations: } R_1(B, C) \text{ and } R_2(A, B, D)}
$$

---

## T08.8 · Normalize an unnormalized table → 1NF → 2NF → 3NF

### 2017 Q.3(b) · 09 Marks

*Section A · Asked in: 2017*

**Question.** Consider the following data table com_employee. Is it already normalized? If not then normalize the table com_employee up to $3^{\text{rd}}$ normal form.

**com_employee**  
<table border="1" style="border-collapse: collapse;"><thead><tr><th>Pcode</th><th>Ptitle</th><th>EmpNo</th><th>EmName</th><th>EmCon</th><th>dNo</th><th>dName</th><th>HRate</th></tr></thead><tbody><tr><td>p1</td><td>Admission Test System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>1000</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1100</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E4</td><td>James</td><td>508, 509</td><td>D3</td><td>HR</td><td>800</td></tr><tr><td>p2</td><td>Salary System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>900</td></tr><tr><td>p2</td><td>Salary System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1000</td></tr></tbody></table>

**Answer.**

#### 1. Is the Table Already Normalized?

**No, the table is not normalized.**

It contains multi-valued entries in column `EmCon` (`501, 502` and `508, 509`). This directly violates the atomicity requirement of **First Normal Form (1NF)**. In addition, it mixes project, employee, contact, department, and assignment facts, causing partial and transitive dependencies.

#### 2. Functional Dependencies Identified from Data

- $\text{Pcode} \rightarrow \text{Ptitle}$
- $\text{EmpNo} \rightarrow \text{EmName}, \text{dNo}$
- $\text{dNo} \rightarrow \text{dName}$
- $(\text{Pcode}, \text{EmpNo}) \rightarrow \text{HRate}$ (an employee's hourly rate depends on the specific project)
- $\text{EmCon}$ is a multi-valued attribute of employee (`EmpNo`).

---

#### Step 1: Conversion to First Normal Form (1NF)

To achieve 1NF, we eliminate multi-valued fields by splitting them into separate atomic rows:

| Pcode | Ptitle | EmpNo | EmName | EmCon | dNo | dName | HRate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| p1 | Admission Test System | E1 | Jones | 501 | D1 | IT | 1000 |
| p1 | Admission Test System | E1 | Jones | 502 | D1 | IT | 1000 |
| p1 | Admission Test System | E3 | Smith | 505 | D2 | Database | 1100 |
| p1 | Admission Test System | E4 | James | 508 | D3 | HR | 800 |
| p1 | Admission Test System | E4 | James | 509 | D3 | HR | 800 |
| p2 | Salary System | E1 | Jones | 501 | D1 | IT | 900 |
| p2 | Salary System | E1 | Jones | 502 | D1 | IT | 900 |
| p2 | Salary System | E3 | Smith | 505 | D2 | Database | 1000 |

PK: `(Pcode, EmpNo, EmCon)`

---

#### Step 2: Conversion to Second Normal Form (2NF)

We eliminate partial dependencies where non-prime attributes depend on proper subsets of the composite key:
- `Pcode -> Ptitle` depends only on `Pcode`.
- `EmpNo -> EmName, dNo, dName` depends only on `EmpNo`.
- `(EmpNo, EmCon)` represents employee phone numbers.
- `(Pcode, EmpNo) -> HRate` depends on the full project-employee assignment.

We decompose into four 2NF relations:

**PROJECT**

| Pcode | Ptitle |
| :--- | :--- |
| p1 | Admission Test System |
| p2 | Salary System |

PK: `Pcode`

**EMPLOYEE_2NF**

| EmpNo | EmName | dNo | dName |
| :--- | :--- | :--- | :--- |
| E1 | Jones | D1 | IT |
| E3 | Smith | D2 | Database |
| E4 | James | D3 | HR |

PK: `EmpNo`

**EMP_CONTACT**

| EmpNo | EmCon |
| :--- | :--- |
| E1 | 501 |
| E1 | 502 |
| E3 | 505 |
| E4 | 508 |
| E4 | 509 |

PK: `(EmpNo, EmCon)`

**PROJECT_ASSIGNMENT**

| Pcode | EmpNo | HRate |
| :--- | :--- | :--- |
| p1 | E1 | 1000 |
| p1 | E3 | 1100 |
| p1 | E4 | 800 |
| p2 | E1 | 900 |
| p2 | E3 | 1000 |

PK: `(Pcode, EmpNo)`

---

#### Step 3: Conversion to Third Normal Form (3NF)

In `EMPLOYEE_2NF`, a transitive dependency exists:
$$
\text{EmpNo} \rightarrow \text{dNo} \quad \text{and} \quad \text{dNo} \rightarrow \text{dName}
$$
Here, `dNo` is a non-prime attribute determining another non-prime attribute `dName`.

We decompose `EMPLOYEE_2NF` into:
1. `DEPARTMENT(dNo, dName)` with PK `dNo`.
2. `EMPLOYEE(EmpNo, EmName, dNo)` with PK `EmpNo` and foreign key `dNo` referencing `DEPARTMENT`.

#### Final 3NF Schema and Relations

1. **PROJECT**  
   `PROJECT(Pcode, Ptitle)`  
   PK: `Pcode`

2. **DEPARTMENT**  

   | dNo | dName |
   | :--- | :--- |
   | D1 | IT |
   | D2 | Database |
   | D3 | HR |
   
   PK: `dNo`

3. **EMPLOYEE**  

   | EmpNo | EmName | dNo |
   | :--- | :--- | :--- |
   | E1 | Jones | D1 |
   | E3 | Smith | D2 |
   | E4 | James | D3 |
   
   PK: `EmpNo` | FK: `dNo` references `DEPARTMENT(dNo)`

4. **EMP_CONTACT**  
   `EMP_CONTACT(EmpNo, EmCon)`  
   PK: `(EmpNo, EmCon)` | FK: `EmpNo` references `EMPLOYEE(EmpNo)`

5. **PROJECT_ASSIGNMENT**  
   `PROJECT_ASSIGNMENT(Pcode, EmpNo, HRate)`  
   PK: `(Pcode, EmpNo)` | FKs: `Pcode` references `PROJECT(Pcode)`, `EmpNo` references `EMPLOYEE(EmpNo)`

---

### 2020 Q.8(b) · 08 Marks

*Section B · Asked in: 2020*

**Question.** Consider the given structure below:

<table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th style="padding: 3px 6px;">Proj. Num.</th><th style="padding: 3px 6px;">Proj. Name</th><th style="padding: 3px 6px;">Emp. No.</th><th style="padding: 3px 6px;">Emp. Name</th><th style="padding: 3px 6px;">Job Class</th><th style="padding: 3px 6px;">Chg/Hr</th><th style="padding: 3px 6px;">Hrs. Biller.</th><th style="padding: 3px 6px;">Total Charge</th></tr></thead><tbody><tr><td rowspan="2">13</td><td rowspan="2">Banking</td><td>103</td><td>John</td><td style="text-align: left;">Analyst</td><td>500</td><td>8</td><td>4000</td></tr><tr><td>105</td><td>Steve</td><td style="text-align: left;">Programmer</td><td>300</td><td>8</td><td>2400</td></tr><tr><td rowspan="2">26</td><td rowspan="2">Telecom</td><td>115</td><td>Jim</td><td style="text-align: left;">Business Analyst</td><td>100</td><td>10</td><td>1000</td></tr><tr><td>717</td><td>Joe</td><td style="text-align: left;">Engineer</td><td>300</td><td>7</td><td>2100</td></tr><tr><td rowspan="2">39</td><td rowspan="2">Finance</td><td>113</td><td>David</td><td style="text-align: left;">Team Leader</td><td>1000</td><td>4</td><td>4000</td></tr><tr><td>120</td><td>Jian</td><td style="text-align: left;">DBA</td><td>800</td><td>3</td><td>2400</td></tr></tbody></table>  
(i) Identify the anomalies in the given structure.  
(ii) Normalize it up to third Normal Form (3NF).

*(Note: In the original examination paper, "Hrs. Billed" is printed as "Hrs. Biller.", and the `Proj. Num.` and `Proj. Name` cells span both employee rows for each project)*

**Answer.**

#### (i) Anomalies in the Given Structure

1. **Redundancy and Derived Data:**
   - `Proj. Name` is repeated for every employee assigned to the same project.
   - `Total Charge` is a derived attribute ($\text{Total Charge} = \text{Chg/Hr} \times \text{Hrs. Biller.}$). Storing calculated values wastes space and creates data inconsistency risks.
2. **Update Anomaly:**
   - If the hourly charge (`Chg/Hr`) for a job class (e.g., "Programmer") changes, multiple rows across different projects must be updated. Missing a single row produces conflicting hourly rates.
3. **Insertion Anomaly:**
   - A new project cannot be added unless at least one employee is assigned to it, because `Emp. No.` is part of the primary key and cannot be `NULL`.
   - A new job class cannot be recorded without an assigned employee and project.
4. **Deletion Anomaly:**
   - If Project 39 (Finance) is completed and its rows are deleted, records for employees David (113) and Jian (120) are permanently lost if they work on no other project.

---

#### (ii) Normalization up to 3NF

*(Note: We use `Hrs_Billed` to denote the column printed as "Hrs. Biller.")*

**Identified Functional Dependencies:**
- $\text{Proj\_Num} \rightarrow \text{Proj\_Name}$
- $\text{Emp\_No} \rightarrow \text{Emp\_Name}, \text{Job\_Class}$
- $\text{Job\_Class} \rightarrow \text{Chg\_Hr}$
- $(\text{Proj\_Num}, \text{Emp\_No}) \rightarrow \text{Hrs\_Billed}$
- $\text{Total Charge}$ is dropped because it is derived.

#### Step 1: First Normal Form (1NF)
Fill in the merged project cells so that each row represents an atomic, complete record:

| Proj_Num | Proj_Name | Emp_No | Emp_Name | Job_Class | Chg_Hr | Hrs_Billed |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| 13 | Banking | 103 | John | Analyst | 500 | 8 |
| 13 | Banking | 105 | Steve | Programmer | 300 | 8 |
| 26 | Telecom | 115 | Jim | Business Analyst | 100 | 10 |
| 26 | Telecom | 717 | Joe | Engineer | 300 | 7 |
| 39 | Finance | 113 | David | Team Leader | 1000 | 4 |
| 39 | Finance | 120 | Jian | DBA | 800 | 3 |

PK: `(Proj_Num, Emp_No)`

#### Step 2: Second Normal Form (2NF)
Remove partial dependencies on the composite key `(Proj_Num, Emp_No)`:
- $\text{Proj\_Num} \rightarrow \text{Proj\_Name}$
- $\text{Emp\_No} \rightarrow \text{Emp\_Name}, \text{Job\_Class}, \text{Chg\_Hr}$

Decomposed into three relations:
1. `PROJECT(Proj_Num, Proj_Name)` with PK `Proj_Num`
2. `EMPLOYEE_2NF(Emp_No, Emp_Name, Job_Class, Chg_Hr)` with PK `Emp_No`
3. `ASSIGNMENT(Proj_Num, Emp_No, Hrs_Billed)` with PK `(Proj_Num, Emp_No)`

#### Step 3: Third Normal Form (3NF)
In `EMPLOYEE_2NF`, there is a transitive dependency:
$$
\text{Emp\_No} \rightarrow \text{Job\_Class} \quad \text{and} \quad \text{Job\_Class} \rightarrow \text{Chg\_Hr}
$$
We decompose `EMPLOYEE_2NF` into `EMPLOYEE` and `JOB`.

#### Final 3NF Relations and Data

1. **PROJECT**

   | Proj_Num | Proj_Name |
   | :---: | :--- |
   | 13 | Banking |
   | 26 | Telecom |
   | 39 | Finance |

   PK: `Proj_Num`

2. **JOB**

   | Job_Class | Chg_Hr |
   | :--- | :---: |
   | Analyst | 500 |
   | Programmer | 300 |
   | Business Analyst | 100 |
   | Engineer | 300 |
   | Team Leader | 1000 |
   | DBA | 800 |

   PK: `Job_Class`

3. **EMPLOYEE**

   | Emp_No | Emp_Name | Job_Class |
   | :---: | :--- | :--- |
   | 103 | John | Analyst |
   | 105 | Steve | Programmer |
   | 115 | Jim | Business Analyst |
   | 717 | Joe | Engineer |
   | 113 | David | Team Leader |
   | 120 | Jian | DBA |

   PK: `Emp_No` | FK: `Job_Class` references `JOB(Job_Class)`

4. **ASSIGNMENT**

   | Proj_Num | Emp_No | Hrs_Billed |
   | :---: | :---: | :---: |
   | 13 | 103 | 8 |
   | 13 | 105 | 8 |
   | 26 | 115 | 10 |
   | 26 | 717 | 7 |
   | 39 | 113 | 4 |
   | 39 | 120 | 3 |

   PK: `(Proj_Num, Emp_No)` | FKs: `Proj_Num` references `PROJECT(Proj_Num)`, `Emp_No` references `EMPLOYEE(Emp_No)`

---

### 2023 Q.2(a) · 06 Marks

*Section A · CLO4 · Asked in: 2023*

**Question.** Consider a university tracking students, their courses and exam scores. A sample table is given below. Step by step convert this to 3NF.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">S_ID</th><th style="padding: 4px 10px;">S-Name</th><th style="padding: 4px 10px;">Courses</th><th style="padding: 4px 10px;">Instructors</th><th style="padding: 4px 10px;">Grades</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">1</td><td style="padding: 4px 10px;">Alice</td><td style="padding: 4px 10px;">Math, Physics</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Brown</td><td style="padding: 4px 10px;">A, B+</td></tr><tr><td style="padding: 4px 10px;">2</td><td style="padding: 4px 10px;">Bob</td><td style="padding: 4px 10px;">Chemistry</td><td style="padding: 4px 10px;">Dr. White</td><td style="padding: 4px 10px;">A-</td></tr><tr><td style="padding: 4px 10px;">3</td><td style="padding: 4px 10px;">Charlie</td><td style="padding: 4px 10px;">Math, Biology, Chemistry</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Gray, Dr. White</td><td style="padding: 4px 10px;">B+, A-, A</td></tr></tbody></table>

**Answer.**

#### Step 1: Convert to First Normal Form (1NF)

The sample table violates 1NF because the attributes `Courses`, `Instructors`, and `Grades` contain multi-valued entries.

To achieve 1NF, we flatten each multi-valued row into individual atomic records:

| S_ID | S-Name | Course | Instructor | Grade |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Alice | Math | Dr. Smith | A |
| 1 | Alice | Physics | Dr. Brown | B+ |
| 2 | Bob | Chemistry | Dr. White | A- |
| 3 | Charlie | Math | Dr. Smith | B+ |
| 3 | Charlie | Biology | Dr. Gray | A- |
| 3 | Charlie | Chemistry | Dr. White | A |

**Primary Key for 1NF:** `(S_ID, Course)`

#### Functional Dependencies Identified:
1. `S_ID -> S-Name` (partial dependency on `S_ID`)
2. `Course -> Instructor` (partial dependency on `Course`)
3. `(S_ID, Course) -> Grade` (full dependency on the composite key)

---

#### Step 2: Convert to Second Normal Form (2NF)

In 1NF, `S-Name` and `Instructor` depend on parts of the composite primary key `(S_ID, Course)`.

To eliminate these partial dependencies, we decompose the table into three relations:

1. **STUDENT**

   | S_ID | S-Name |
   | :---: | :--- |
   | 1 | Alice |
   | 2 | Bob |
   | 3 | Charlie |

   PK: `S_ID`

2. **COURSE**

   | Course | Instructor |
   | :--- | :--- |
   | Math | Dr. Smith |
   | Physics | Dr. Brown |
   | Chemistry | Dr. White |
   | Biology | Dr. Gray |

   PK: `Course`

3. **ENROLLMENT**

   | S_ID | Course | Grade |
   | :---: | :--- | :---: |
   | 1 | Math | A |
   | 1 | Physics | B+ |
   | 2 | Chemistry | A- |
   | 3 | Math | B+ |
   | 3 | Biology | A- |
   | 3 | Chemistry | A |

   PK: `(S_ID, Course)`

All non-prime attributes in these three relations depend fully on their entire candidate keys. Thus, the schema is in 2NF.

---

#### Step 3: Check for Third Normal Form (3NF)

A relation in 2NF is in 3NF if no non-prime attribute transitively depends on a candidate key.

- In `STUDENT(S_ID, S-Name)`, `S_ID` is the candidate key and determines `S-Name`. No transitive dependency exists.
- In `COURSE(Course, Instructor)`, `Course` is the candidate key and determines `Instructor`. No transitive dependency exists.
- In `ENROLLMENT(S_ID, Course, Grade)`, `(S_ID, Course)` is the candidate key and determines `Grade`. No transitive dependency exists.

Since there are no transitive dependencies, the 2NF schema is already in **3NF**.

$$
\boxed{\text{Final 3NF Schema: } \text{STUDENT}(\underline{\text{S\_ID}}, \text{S-Name}), \; \text{COURSE}(\underline{\text{Course}}, \text{Instructor}), \; \text{ENROLLMENT}(\underline{\text{S\_ID}, \text{Course}}, \text{Grade})}
$$

---

### 2024 Q.3(a) · 04 Marks

*Section A · CO2 · Asked in: 2024*

**Question.** A library database stores information about Books, Authors, Publishers and Borrowers. Create a table that contains some data redundancy and partial dependencies. Also, show the procedure to normalize the table.

**Answer.**

#### 1. Unnormalized / 1NF Table with Redundancy and Partial Dependencies

Consider a single table `LIBRARY_LOAN` designed to store all lending records:

| Book_ID | Borrower_ID | Title | Author_ID | Author_Name | Publisher_Name | Borrower_Name | Borrow_Date |
| :---: | :---: | :--- | :---: | :--- | :--- | :--- | :---: |
| B101 | U01 | DBMS Concepts | A1 | Silberschatz | McGraw-Hill | Akib | 2024-01-10 |
| B101 | U02 | DBMS Concepts | A1 | Silberschatz | McGraw-Hill | Shuvo | 2024-02-15 |
| B202 | U01 | Operating Systems | A1 | Silberschatz | Wiley | Akib | 2024-03-01 |

**Primary Key:** `(Book_ID, Borrower_ID)`

**Functional Dependencies:**
- `Book_ID -> Title, Author_ID, Publisher_Name` (partial dependency on subset `Book_ID`)
- `Author_ID -> Author_Name` (transitive dependency)
- `Borrower_ID -> Borrower_Name` (partial dependency on subset `Borrower_ID`)
- `(Book_ID, Borrower_ID) -> Borrow_Date` (full dependency)

**Data Redundancy:**
- Book title, author details, and publisher name are duplicated whenever the same book is loaned to another borrower.
- Borrower name is repeated whenever a user borrows multiple books.

---

#### 2. Procedure to Normalize the Table

##### Step 1: Eliminate Partial Dependencies (Convert to 2NF)
Decompose `LIBRARY_LOAN` so non-prime attributes depend only on the full primary key:

1. `BOOK_INFO(Book_ID, Title, Author_ID, Author_Name, Publisher_Name)` with PK `Book_ID`
2. `BORROWER(Borrower_ID, Borrower_Name)` with PK `Borrower_ID`
3. `LOAN(Book_ID, Borrower_ID, Borrow_Date)` with PK `(Book_ID, Borrower_ID)`

This eliminates partial dependencies and achieves 2NF.

##### Step 2: Eliminate Transitive Dependencies (Convert to 3NF)
In `BOOK_INFO`, the dependency `Author_ID -> Author_Name` is transitive because `Author_ID` is a non-prime attribute determining `Author_Name`.

We decompose `BOOK_INFO` into:
1. `BOOK(Book_ID, Title, Author_ID, Publisher_Name)` with PK `Book_ID` and FK `Author_ID`
2. `AUTHOR(Author_ID, Author_Name)` with PK `Author_ID`

#### Final Normalized 3NF Schema:
1. **BOOK** (`Book_ID`, `Title`, `Author_ID`, `Publisher_Name`)  
   PK: `Book_ID` | FK: `Author_ID` references `AUTHOR(Author_ID)`
2. **AUTHOR** (`Author_ID`, `Author_Name`)  
   PK: `Author_ID`
3. **BORROWER** (`Borrower_ID`, `Borrower_Name`)  
   PK: `Borrower_ID`
4. **LOAN** (`Book_ID`, `Borrower_ID`, `Borrow_Date`)  
   PK: `(Book_ID, Borrower_ID)` | FKs: `Book_ID` references `BOOK`, `Borrower_ID` references `BORROWER`

---

## T08.9 · BCNF; 3NF vs BCNF; highest normal form

### CT-03 Q.01(d) · 02 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(d)** Determine the highest normal form satisfied by the given relation. Give a proper justification.

**Answer.**

1. **First Normal Form (1NF) Check:**  
   All attributes hold atomic, single values. Therefore, the relation satisfies **1NF**.

2. **Second Normal Form (2NF) Check:**  
   The candidate key is composite: $\{\text{StudentID}, \text{CourseID}\}$.  
   Prime attributes: $\{\text{StudentID}, \text{CourseID}\}$.  
   Non-prime attributes: $\{\text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}\}$.

   Examining the functional dependencies:
   - $\text{StudentID} \rightarrow \text{StudentName}$: The non-prime attribute $\text{StudentName}$ depends only on $\text{StudentID}$, which is a proper subset of the candidate key.
   - $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$: The non-prime attributes depend only on $\text{CourseID}$, which is a proper subset of the candidate key.

   Both dependencies are **partial functional dependencies**. Because non-prime attributes depend on proper subsets of the candidate key, the relation violates 2NF.

$$
\boxed{\text{Highest Normal Form Satisfied: First Normal Form (1NF)}}
$$

---

### CT-03 Q.04 · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Justify the statement: "Every BCNF relation is in 3NF, but every 3NF relation is not necessarily in BCNF."

**Answer.**

#### 1. Definitions of 3NF and BCNF

- **Boyce-Codd Normal Form (BCNF):**  
  A relation schema $R$ is in BCNF if for every non-trivial functional dependency $\alpha \rightarrow \beta$, $\alpha$ is a **superkey** of $R$.
- **Third Normal Form (3NF):**  
  A relation schema $R$ is in 3NF if for every non-trivial functional dependency $\alpha \rightarrow \beta$, at least one of the following conditions holds:
  1. $\alpha$ is a superkey of $R$, **OR**
  2. Each attribute $A \in (\beta - \alpha)$ is a **prime attribute** (member of some candidate key).

#### 2. Why Every BCNF Relation is in 3NF

If a relation is in BCNF, every non-trivial FD $\alpha \rightarrow \beta$ satisfies condition 1 ($\alpha$ is a superkey). Since condition 1 of 3NF is identical to the only condition of BCNF, every dependency that satisfies BCNF automatically satisfies 3NF. Thus, BCNF is a stricter subset of 3NF:
$$
\text{BCNF} \subset \text{3NF}
$$

#### 3. Why Every 3NF Relation is Not Necessarily in BCNF (Counterexample)

Consider relation $R(A, B, C, D)$ with functional dependencies:
$$
F = \{AB \rightarrow CD, \; D \rightarrow A\}
$$

1. **Find Candidate Keys:**
   - $AB^+ = \{A, B, C, D\} \implies AB$ is a candidate key.
   - $DB^+ = \{D, B, A, C\} \implies BD$ is a candidate key.
   - Prime attributes: $\{A, B, D\}$.
   - Non-prime attribute: $\{C\}$.

2. **Check 3NF:**
   - $AB \rightarrow CD$: $AB$ is a superkey (satisfies condition 1).
   - $D \rightarrow A$: $D$ is not a superkey. But attribute $A$ is a **prime attribute** because it is part of candidate key $AB$ (satisfies condition 2).
   - Therefore, the relation $R$ is in **3NF**.

3. **Check BCNF:**
   - In dependency $D \rightarrow A$, the determinant $D$ is not a superkey. BCNF does not allow the prime attribute relaxation (condition 2).
   - Therefore, the relation $R$ is **NOT in BCNF**.

Because relation $R$ is in 3NF but not in BCNF, the statement is justified.

---

## T08.10 · Pros/cons of normalization; denormalization

*No questions from past finals or class tests.*

*See also:* [[#T08.6 · Define normalization (and its importance) & 1NF / 2NF / 3NF]] (2017 Q.3(a))

---

## T08.11 · Lossless-join decomposition & dependency preservation

*No questions from past finals or class tests.*

---

[← Prev: T07 · Triggers and Stored Procedures](T07_Triggers_and_Stored_Procedures.md) | [Explanation layer](../Topicwise_answers_explaination/T08_Normalization_and_Functional_Dependencies.md) | [Next: T09 · Transactions, ACID, and Anomalies →](T09_Transactions_ACID_and_Anomalies.md)
