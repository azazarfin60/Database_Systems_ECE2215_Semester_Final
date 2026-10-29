---
title: "T08 · Normalization and Functional Dependencies · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T07 · Triggers and Stored Procedures](T07_Triggers_and_Stored_Procedures.md) | [Exam-style layer](../Topicwise_answers_exam_style/T08_Normalization_and_Functional_Dependencies.md) | [Next: T09 · Transactions, ACID, and Anomalies →](T09_Transactions_ACID_and_Anomalies.md)

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

**What the examiner wants.**  
A structured answer listing data redundancy and the three classic modification anomalies (1.5 marks). Then, a concrete relational table example illustrating each problem clearly (2.5 marks).

**Key idea.**  
When you lump multiple real-world entities into a single relation, you store the same fact repeatedly. This repetition wastes disk space. Worse, when you modify, insert, or delete data, the database either loses valid facts or ends up with conflicting values. Normalization fixes this by giving each independent entity its own table.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: Why cannot a new course be added without a student in the example?  
  A: Because `Student_ID` is part of the primary key, and primary key attributes cannot be null.
- Q: How does normalization resolve the deletion anomaly?  
  A: By splitting the table into `STUDENT`, `COURSE`, and `ENROLLMENT` tables so course data exists independently of student enrollments.

> [!warning] Common mistakes
> - Listing only the names of anomalies without giving a concrete table example.
> - Confusing update anomaly with ordinary concurrency conflicts. Update anomaly is caused by redundant data copies in a single unnormalized table.
> - Forgetting to mention why an insertion fails: primary key columns reject `NULL` under Entity Integrity.

**Exam tip.**  
Draw a simple 3-row table with 5 columns. Use it to demonstrate all three anomalies one by one. This takes less than two minutes and guarantees full marks.

**Sources.**  
- [Deck 06 · Slides 3–10](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

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

**What the examiner wants.**  
Direct answers to all three parts: (i) evaluation of storage wastage due to repeated student attributes and multi-valued course lists (2 marks); (ii) analysis of update anomalies and inconsistencies (2 marks); (iii) analysis of deletion challenges including string manipulation and loss of records for single-course students (2 marks).

**Key idea.**  
The table mixes three different concepts in one place: student demographics, individual course grades, and registered course lists. Even worse, `Reg Sub Code` stores multiple course codes inside a single cell. This design wastes storage and creates severe data manipulation headaches.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: What makes `Reg Sub Code` non-atomic?  
  A: It packs multiple codes (`ECE-2103` and `ECE-2107`) separated by line breaks into a single table cell.
- Q: Which row in the table suffers the most from deleting `ECE-2107`?  
  A: The row for `1710004` (Mr. D), because `ECE-2107` is his only course.

> [!warning] Common mistakes
> - Answering part (i) by only saying "it is bad" without highlighting the non-atomic column and repeated text.
> - Overlooking student 1710004 in part (iii). You must distinguish between students taking multiple courses and students taking only that single course.

**Exam tip.**  
Number your answers exactly as `(i)`, `(ii)`, and `(iii)`. Cite specific roll numbers (e.g., `1710001`, `1710004`) from the given table in your arguments.

**Sources.**  
- [Deck 06 · Slides 3–10, 30](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.1.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2021 Q.6(c) · 04 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Consider the following table:

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;"><u>st_id</u></th><th style="padding: 4px 10px;">Name</th><th style="padding: 4px 10px;">Course</th><th style="padding: 4px 10px;">Session</th><th style="padding: 4px 10px;">Fee</th><th style="padding: 4px 10px;">Dept</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">Devi</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">Sona</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">Varun</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">Satish</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">105</td><td style="padding: 4px 10px;">Amisha</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr></tbody></table>  
Is there any data redundancy in the above table? What kinds of problems/ anomalities it will produce for this table in future?

*(Note: "problems/ anomalities" printed verbatim from original question paper)*

**Answer.**

**What the examiner wants.**  
Clear verification of data redundancy with attribute identification (1.5 marks), followed by an explanation of update, insertion, and deletion anomalies tailored to this exact table (2.5 marks).

**Key idea.**  
Notice that all five students have identical course details: "DBMS", "2022", "90k", and "CS". The course fee and department depend on `Course`, not on the individual student `st_id`. Putting course facts into the student table creates textbook modification anomalies.

**Step-by-step solution.**

#### 1. Presence of Data Redundancy

**Yes, significant data redundancy exists.**

The attributes `Course` ("DBMS"), `Session` ("2022"), `Fee` ("90k"), and `Dept` ("CS") are duplicated across all 5 rows. In this schema, `Fee` and `Dept` depend on `Course`, not on the primary key `st_id`. Storing course-level attributes in every student record creates column-level duplication.

#### 2. Future Problems and Anomalies

1. **Storage Overhead:** Storing identical strings ("DBMS", "2022", "90k", "CS") for hundreds of students in the same course wastes physical storage.
2. **Update Anomaly:** If the fee for the DBMS course increases from 90k to 95k, every student record enrolled in DBMS must be updated. If one row is missed, students enrolled in the exact same course see conflicting fees.
3. **Insertion Anomaly:** If the department introduces a new course (e.g., "AI", Session "2022", Fee "85k") before any student enrolls, this course cannot be entered into the database. The primary key `st_id` cannot be `NULL` due to the Entity Integrity constraint.
4. **Deletion Anomaly:** If all students (101 to 105) complete the term or cancel their enrollment, deleting their records removes all 5 rows. This accidentally deletes all records of the DBMS course, its fee, and its department.

**Check.**  
*Quick self-test:*
- Q: What functional dependency causes redundancy in this table?  
  A: $\text{Course} \rightarrow \text{Fee}, \text{Dept}, \text{Session}$.
- Q: How can this table be normalized to 2NF/3NF?  
  A: Decompose into $\text{STUDENT}(\underline{\text{st\_id}}, \text{Name}, \text{Course})$ and $\text{COURSE}(\underline{\text{Course}}, \text{Session}, \text{Fee}, \text{Dept})$.

> [!warning] Common mistakes
> - Stating that there is no redundancy because every row has a unique `st_id`. Redundancy exists across non-key attributes!
> - Describing anomalies in general terms without linking them to "DBMS", "90k", or "CS".

**Exam tip.**  
Start with a direct "Yes" to answer the first question immediately. Then present the anomalies with bullet points using the values printed in the question table.

**Sources.**  
- [Deck 06 · Slides 5–10](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.1.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2023 Q.2(b) · 04 Marks

*Section A · CLO4 · Asked in: 2023*

**Question.** What are the anomalies that normalization aims to eliminate? Provide examples of insertion, deletion and update anomalies.

**Answer.**

**What the examiner wants.**  
Naming the three anomalies (1 mark), followed by clear definitions and concrete examples for each using an employee/department or student/course table (3 marks).

**Key idea.**  
When independent facts share a table, they cannot be modified independently. An insertion requires dummy data, a deletion erases unintended facts, and an update requires touchpoints across many records.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: Which DBMS rule prevents inserting a department with a null `Emp_ID`?  
  A: The Entity Integrity constraint.
- Q: What is the solution to these anomalies?  
  A: Decompose `EMP_DEPT` into `EMPLOYEE(Emp_ID, Emp_Name, Dept_ID)` and `DEPARTMENT(Dept_ID, Dept_Name, Location)`.

> [!warning] Common mistakes
> - Writing abstract definitions without providing the required examples.
> - Creating three separate unrelated examples when a single small table can illustrate all three anomalies cleanly.

**Exam tip.**  
Stick to the standard `EMP_DEPT` or `STUDENT_COURSE` table. It keeps your answer compact and lets you show all three anomalies on the same data.

**Sources.**  
- [Deck 06 · Slides 7–10](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.1.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.2 · FDs: trivial, full/partial, transitive; prime vs non-prime attributes

### CT-03 Q.01(b-c) · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(b)** Identify the prime and non-prime attributes. `[02 Marks]`  
**(c)** Identify the partial and transitive dependencies. `[02 Marks]`

**Answer.**

**What the examiner wants.**  
Accurate classification of attributes as prime or non-prime based on the candidate key (2 marks), and identification of all partial and transitive functional dependencies with explicit determinants and dependents (2 marks).

**Key idea.**  
A prime attribute belongs to at least one candidate key. Any attribute not in a candidate key is non-prime. A partial dependency occurs when a non-prime attribute depends on only part of a composite key. A transitive dependency occurs when a non-prime attribute depends on another non-prime attribute.

**Step-by-step solution.**

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

**Check.**  
*Attribute partition check:*
- Total attributes in schema = 7.
- Prime attributes count = 2 ($\text{StudentID}, \text{CourseID}$).
- Non-prime attributes count = 5 ($\text{StudentName}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade}$).
- $2 + 5 = 7$. Every attribute is accounted for.

> [!warning] Common mistakes
> - Treating `InstructorID` as a prime attribute because it appears on the LHS of `InstructorID -> InstructorName`. Prime status comes strictly from membership in a candidate key, not from being a determinant!
> - Listing $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$ as a partial dependency. It is a full dependency because it requires both attributes of the key.

**Exam tip.**  
Write down the candidate key before answering part (b). Even if part (a) is graded separately, stating the candidate key explicitly protects your marks.

**Sources.**  
- [Deck 06 · Slides 16–17](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.4, §7.5.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

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

**What the examiner wants.**  
Demonstrating the closure computation of functional dependencies (2 marks), followed by finding all candidate keys with proof of minimality (2 marks).

**Key idea.**  
Computing the full set $F^+$ on a 5-attribute schema yields hundreds of dependencies. In an exam, state that $F^+$ is too large to write in its entirety, compute the attribute closures of single attributes and relevant combinations, and derive key non-trivial dependencies using Armstrong's axioms. Then identify all minimal attribute sets whose closure is $\{A, B, C, D, E\}$.

**Step-by-step solution.**

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

**Check.**  
*Verification of Candidate Keys:*
- Single attribute keys: $A$ and $E$ have closures equal to $R$. They are single attributes, so minimality is trivial.
- Pair keys: $BC^+ = R$, and proper subsets $B^+ = \{B, D\} \neq R$, $C^+ = \{C\} \neq R$. Thus $BC$ is minimal.
- Pair keys: $CD^+ = R$, and proper subsets $C^+ = \{C\} \neq R$, $D^+ = \{D\} \neq R$. Thus $CD$ is minimal.
- Are there other keys? Attributes not determined by anything except keys: $C$ appears on no LHS and is only determined by $A$ and $E$. So any key without $A$ or $E$ must contain $C$. With $C$, we need $B$ or $D$ to derive the rest. Thus exactly four keys exist.

> [!warning] Common mistakes
> - Spending 20 minutes trying to list all FDs in $F^+$. State clearly that $F^+$ is too large, then show the attribute closures and derived non-trivial FDs.
> - Missing $BC$ or $CD$ as candidate keys because they consist of two attributes.
> - Including non-minimal superkeys like $AB$ or $AC$ as candidate keys.

**Exam tip.**  
Compute single-attribute closures first. Once you see that $A^+ = R$ and $E^+ = R$, you already have two candidate keys. Then test pairs containing $C$.

**Sources.**  
- [Deck 06 · Slides 25–29](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.4.1–7.4.2](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### CT-03 Q.01(a) · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(a)** Identify all the possible candidate key of the relation.

**Answer.**

**What the examiner wants.**  
Systematic derivation of candidate keys: identifying core non-RHS attributes (1.5 marks), showing the step-by-step expansion of the attribute closure (1.5 marks), and proving minimality (1 mark).

**Key idea.**  
Look at which attributes never appear on the right side of any arrow. Those attributes can never be derived from anything else, so they must be part of every candidate key.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: Can `InstructorID` be added to form a candidate key?  
  A: No. Adding `InstructorID` produces a superkey, but not a candidate key, because it is not minimal.
- Q: Could another candidate key exist without `StudentID`?  
  A: No, because no functional dependency has `StudentID` on the right side. It cannot be derived.

> [!warning] Common mistakes
> - Stating the key by intuition without showing the step-by-step growth of $X^+$.
> - Forgetting to test the proper subsets $\{\text{StudentID}\}$ and $\{\text{CourseID}\}$ to prove minimality.

**Exam tip.**  
Start your solution by listing attributes that never appear on the RHS. This proves to the examiner that no other combination of attributes can be a candidate key.

**Sources.**  
- [Deck 06 · Slides 25–27](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.4.2](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.5 · Canonical cover Fc (and how it differs from normalization)

### 2021 Q.6(a) · 03 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Differentiate between normalization and canonical cover in DBMS.

**Answer.**

**What the examiner wants.**  
A comparison table highlighting key differences in definition, goal, inputs, outputs, and operational level (3 marks).

**Key idea.**  
Normalization restructures tables (schemas). Canonical cover simplifies functional dependencies (constraints). You often compute a canonical cover first so that normalization algorithms (like 3NF synthesis) run efficiently.

**Step-by-step solution.**

| Parameter | Normalization | Canonical Cover ($F_c$) |
| :--- | :--- | :--- |
| **Definition** | The process of decomposing relation schemas to eliminate redundancy and update/delete/insert anomalies. | A minimal, non-redundant set of functional dependencies equivalent to the original FD set ($F_c \equiv F$). |
| **Primary Goal** | Design high-integrity tables that eliminate anomalies and avoid data duplication. | Simplify the set of integrity constraints so DBMS updates can be validated with minimal overhead. |
| **Input** | A relation schema $R$ and its functional dependencies $F$. | A set of functional dependencies $F$. |
| **Output** | A collection of decomposed relations $\{R_1, R_2, \dots, R_k\}$ in a desired normal form (e.g., 3NF, BCNF). | A simplified functional dependency set $F_c$ with no extraneous attributes and unique left-hand sides. |
| **Level of Operation** | Operates on the schema design level (splitting tables and foreign keys). | Operates purely on the mathematical dependency level (simplifying FDs). |

**Check.**  
*Quick self-test:*
- Q: Does finding a canonical cover change the table structure?  
  A: No. It only simplifies the rules that describe relationships between attributes.
- Q: When is canonical cover used during database design?  
  A: It is used in algorithms like the 3NF synthesis algorithm to construct minimal 3NF relations.

> [!warning] Common mistakes
> - Writing that canonical cover is an alternative to normalization. They are complementary steps in database design.
> - Presenting unstructured paragraphs instead of a clear comparison table.

**Exam tip.**  
Use 4 to 5 structured comparison rows. A comparison table is easier to read and earns maximum marks for 3-mark questions.

**Sources.**  
- [Deck 06 · Slide 4](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.4.3](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

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

**What the examiner wants.**  
Formal mathematical definition of functional dependency (2 marks), followed by a complete step-by-step canonical cover derivation: union rule check, extraneous attribute testing on LHS and RHS, and the final canonical set (3 marks).

**Key idea.**  
A canonical cover has no redundant attributes and no redundant dependencies, with each LHS combined. To test if an attribute is extraneous on the RHS, remove it and see if you can still derive it using the remaining dependencies. To test an attribute on the LHS, remove it and see if the reduced LHS can derive the RHS under the original dependencies.

**Step-by-step solution.**

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

**Check.**  
*Equivalence verification:*
- Every FD in $F_c$ is directly present in $F$, so $F \implies F_c$.
- Every FD in $F$ is directly present in $F_c$, so $F_c \implies F$.
- Thus, $F_c \equiv F$, all LHS are unique, and no attribute is extraneous.

> [!warning] Common mistakes
> - Writing a vague definition of FD without mentioning the tuple comparison ($t_1[\alpha] = t_2[\alpha] \implies t_1[\beta] = t_2[\beta]$).
> - Forgetting the formal difference between testing an attribute on the LHS vs testing on the RHS.
> - Splitting $A \rightarrow BC$ into $A \rightarrow B$ and $A \rightarrow C$ and claiming the split is the final canonical cover. In Silberschatz 7e canonical cover, dependencies with identical LHS must be merged using the union rule.

**Exam tip.**  
Show the closure calculation for each extraneous attribute test explicitly. Even if the answer is "no attribute is extraneous", showing the test proves you know the algorithm.

**Sources.**  
- [Deck 06 · Slide 14](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.2, §7.4.3](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.6 · Define normalization (and its importance) & 1NF / 2NF / 3NF

### 2017 Q.3(a) · 03 Marks

*Section A · Asked in: 2017, CT-03 · L2 merge*

**Question (2017 Q.3(a)).** What do you mean by normalization? Why normalization is important for database?

**Question (CT-03 Q.03).** Define normalization and state its main objective.

**Answer.**

**What the examiner wants.**  
A concise definition of normalization (1.5 marks) and four clear points on why it is important for relational database design (1.5 marks).

**Key idea.**  
Normalization is systematic database cleanup. It takes messy, bloated tables and divides them into well-behaved tables where every non-key column depends strictly on the primary key.

**Step-by-step solution.**

#### 1. What is Normalization?

**Normalization** is a formal, systematic technique for designing relational database schemas. It decomposes relations with anomalies into smaller, well-structured relations to reduce data redundancy and ensure data integrity.

#### 2. Importance of Normalization (Main Objectives)

Normalization is essential for relational databases because it:

1. **Eliminates Unnecessary Data Redundancy:** Prevents storing the same facts repeatedly across multiple records, which conserves physical storage.
2. **Prevents Database Anomalies:** Completely removes insertion, deletion, and update anomalies that corrupt data during modifications.
3. **Ensures Data Consistency and Integrity:** Guarantees that an update applied to one record keeps all related facts accurate and consistent.
4. **Preserves Data Dependencies:** Ensures all real-world business constraints and functional dependencies can be enforced efficiently without complex cross-table joins.

*Short version for CT-03 Q.03 (3 marks):* Define normalization as the systematic decomposition of relations to minimize redundancy and eliminate anomalies. State the main objective: to produce well-structured tables free of insertion, update, and deletion anomalies while maintaining data consistency.

**Check.**  
*Quick self-test:*
- Q: What does normalization decompose?  
  A: It decomposes a relation schema $R$ into a set of smaller schemas $\{R_1, R_2, \dots, R_k\}$.
- Q: What two properties must a good decomposition guarantee?  
  A: Lossless-join decomposition and dependency preservation.

> [!warning] Common mistakes
> - Giving an overly casual definition like "making databases normal" without mentioning decomposition and anomaly elimination.
> - Forgetting to list data consistency and anomaly prevention as core objectives.

**Exam tip.**  
Provide the formal definition in 2 to 3 lines, followed by a numbered list of four distinct benefits.

**Sources.**  
- [Deck 06 · Slide 4](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2017 Q.8(c) · 03 Marks

*Section B · Asked in: 2017*

**Question.** What is 1NF, 2NF and 3NF?

**Answer.**

**What the examiner wants.**  
Accurate, concise definitions for 1NF, 2NF, and 3NF, highlighting the primary defect each normal form eliminates (1 mark per normal form).

**Key idea.**  
- 1NF removes multi-valued/composite attributes (enforces atomicity).
- 2NF removes partial dependencies (non-key attributes depending on part of a composite key).
- 3NF removes transitive dependencies (non-key attributes depending on other non-key attributes).

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: If a table has a single-attribute primary key and is in 1NF, is it automatically in 2NF?  
  A: Yes! Partial dependencies can only exist when the primary key is composite.
- Q: Can a relation have transitive dependencies and still be in 2NF?  
  A: Yes. 2NF only forbids partial dependencies; 3NF is required to eliminate transitive dependencies.

> [!warning] Common mistakes
> - Forgetting to state "It is already in 1NF" when defining 2NF, or "It is already in 2NF" when defining 3NF. Normal forms are strictly cumulative.
> - Confusing partial dependency (part of key determines non-prime) with transitive dependency (non-prime determines non-prime).

**Exam tip.**  
For a 3-mark question, spend exactly one concise paragraph on each normal form. Highlight the key terms: **atomic values**, **no partial dependencies**, and **no transitive dependencies**.

**Sources.**  
- [Deck 06 · Slides 30, 31, 37](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.4, §7.5.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2019 Q.3(a) · 04 Marks

*Section A · Asked in: 2018, 2019 · L2 merge*

**Question (2019 Q.3(a)).** What is normalization? Discuss 1NF and 2NF.

**Question (2018 Q.4(c)).** Explain the rules of 1NF and 2NF with a proper example.

**Answer.**

**What the examiner wants.**  
Definition of normalization (1 mark), detailed discussion of 1NF rules with a clear example (1.5 marks), and 2NF rules with a clear example (1.5 marks).

**Key idea.**  
1NF requires that every cell holds one single value (no lists). 2NF requires 1NF plus that every non-key attribute depends on the whole key, not just half of it.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: What makes a phone list violate 1NF?  
  A: Storing multiple phone numbers in one row makes the cell non-atomic.
- Q: Why is `StudentName` partially dependent in `ENROLL`?  
  A: Because knowing `StudentID` is already enough to determine `StudentName`; `CourseID` is completely unnecessary.

> [!warning] Common mistakes
> - Discussing rules without providing before-and-after tables for the examples.
> - Choosing a 2NF example with a single-attribute primary key. Partial dependencies only exist when candidate keys are composite!

**Exam tip.**  
Keep the examples minimal: use a 2-row table for 1NF and a 4-attribute relation for 2NF.

**Sources.**  
- [Deck 06 · Slides 30–34](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.4](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.7 · 2NF test from an FD set

### 2021 Q.5(c) · 04 Marks

*Section B · CLO1 · Asked in: 2021*

**Question.** Given a relation R (A, B, C, D) and functional dependency at FD = { AB $\to$ CD, B $\to$ C }. Determine whether the given R is in 2NF? If not, convert it into 2NF.

*(Note: "functional dependency at FD" printed verbatim from original question paper)*

**Answer.**

**What the examiner wants.**  
Candidate key derivation and attribute classification (1 mark), identification of the partial dependency violating 2NF (1.5 marks), and correct decomposition into 2NF relations with candidate keys identified (1.5 marks).

**Key idea.**  
Candidate key is $AB$. The dependency $B \rightarrow C$ has $B$ on its left, which is only part of the key $AB$. Because $C$ is a non-prime attribute depending on half the key, it is a partial dependency. Decompose to isolate $B \rightarrow C$ into its own relation.

**Step-by-step solution.**

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

**Check.**  
*Decomposition property check:*
- Attribute union: $R_1 \cup R_2 = \{B, C\} \cup \{A, B, D\} = \{A, B, C, D\} = R$.
- Common attributes: $R_1 \cap R_2 = \{B\}$.
- Since $B$ is the candidate key of $R_1$, the intersection is a superkey of $R_1$. The decomposition is guaranteed to be lossless!

> [!warning] Common mistakes
> - Leaving attribute $C$ inside $R_2$, producing $(A, B, C, D)$ and $(B, C)$, which fails to eliminate the partial dependency from the main relation.
> - Forgetting to state the candidate key of each newly formed relation.

**Exam tip.**  
Always show the intersection $R_1 \cap R_2$ and state that it forms a key for $R_1$. This proves your decomposition is lossless.

**Sources.**  
- [Deck 06 · Slides 35–36](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.4, §7.5.1](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.8 · Normalize an unnormalized table → 1NF → 2NF → 3NF

### 2017 Q.3(b) · 09 Marks

*Section A · Asked in: 2017*

**Question.** Consider the following data table com_employee. Is it already normalized? If not then normalize the table com_employee up to $3^{\text{rd}}$ normal form.

**com_employee**  
<table border="1" style="border-collapse: collapse;"><thead><tr><th>Pcode</th><th>Ptitle</th><th>EmpNo</th><th>EmName</th><th>EmCon</th><th>dNo</th><th>dName</th><th>HRate</th></tr></thead><tbody><tr><td>p1</td><td>Admission Test System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>1000</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1100</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E4</td><td>James</td><td>508, 509</td><td>D3</td><td>HR</td><td>800</td></tr><tr><td>p2</td><td>Salary System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>900</td></tr><tr><td>p2</td><td>Salary System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1000</td></tr></tbody></table>

**Answer.**

**What the examiner wants.**  
Direct answer on normalization status with justification (1 mark), followed by a clear, progressive three-step transformation: 1NF with atomic rows and primary key (2.5 marks), 2NF eliminating partial dependencies (2.5 marks), and 3NF eliminating transitive dependencies with sample tables and keys (3 marks).

**Key idea.**  
Notice that `EmCon` has comma-separated contact numbers (violates 1NF). Next, project titles depend only on `Pcode`, and employee names depend only on `EmpNo` (violates 2NF). Finally, department name depends on `dNo`, which depends on `EmpNo` (violates 3NF).

**Step-by-step solution.**

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

**Check.**  
*Trace check:*
- Can we reconstruct the hourly rate of Jones on Admission Test System?  
  Join `PROJECT_ASSIGNMENT` (`p1`, `E1`, `1000`) with `PROJECT` (`p1`, `Admission Test System`) and `EMPLOYEE` (`E1`, `Jones`, `D1`). The rate is 1000.
- Can we find Jones's department name?  
  Follow `E1 -> D1 -> IT`. It matches the original table perfectly.

> [!warning] Common mistakes
> - Missing `EMP_CONTACT` as its own separate table. If you leave `EmCon` inside `EMPLOYEE`, you re-introduce multi-valued non-atomic data.
> - Putting `HRate` in the `EMPLOYEE` table. Notice from the table that Jones has `HRate = 1000` on project `p1`, but `HRate = 900` on project `p2`. `HRate` depends on both `Pcode` and `EmpNo`!

**Exam tip.**  
State the functional dependencies at the top before writing any tables. This justifies every table split to the examiner.

**Sources.**  
- [Deck 06 · Slides 30–40](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3, §7.5](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2020 Q.8(b) · 08 Marks

*Section B · Asked in: 2020*

**Question.** Consider the given structure below:

<table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th style="padding: 3px 6px;">Proj. Num.</th><th style="padding: 3px 6px;">Proj. Name</th><th style="padding: 3px 6px;">Emp. No.</th><th style="padding: 3px 6px;">Emp. Name</th><th style="padding: 3px 6px;">Job Class</th><th style="padding: 3px 6px;">Chg/Hr</th><th style="padding: 3px 6px;">Hrs. Biller.</th><th style="padding: 3px 6px;">Total Charge</th></tr></thead><tbody><tr><td rowspan="2">13</td><td rowspan="2">Banking</td><td>103</td><td>John</td><td style="text-align: left;">Analyst</td><td>500</td><td>8</td><td>4000</td></tr><tr><td>105</td><td>Steve</td><td style="text-align: left;">Programmer</td><td>300</td><td>8</td><td>2400</td></tr><tr><td rowspan="2">26</td><td rowspan="2">Telecom</td><td>115</td><td>Jim</td><td style="text-align: left;">Business Analyst</td><td>100</td><td>10</td><td>1000</td></tr><tr><td>717</td><td>Joe</td><td style="text-align: left;">Engineer</td><td>300</td><td>7</td><td>2100</td></tr><tr><td rowspan="2">39</td><td rowspan="2">Finance</td><td>113</td><td>David</td><td style="text-align: left;">Team Leader</td><td>1000</td><td>4</td><td>4000</td></tr><tr><td>120</td><td>Jian</td><td style="text-align: left;">DBA</td><td>800</td><td>3</td><td>2400</td></tr></tbody></table>  
(i) Identify the anomalies in the given structure.  
(ii) Normalize it up to third Normal Form (3NF).

*(Note: In the original examination paper, "Hrs. Billed" is printed as "Hrs. Biller.", and the `Proj. Num.` and `Proj. Name` cells span both employee rows for each project)*

**Answer.**

**What the examiner wants.**  
Part (i): Identification of data redundancy and concrete examples of update, insertion, and deletion anomalies (3 marks). Part (ii): Complete normalization progression to 1NF, 2NF, and 3NF with sample rows and primary keys (5 marks).

**Key idea.**  
The table has merged project cells (violating 1NF) and derived calculations (`Total Charge = Chg/Hr * Hrs. Biller.`). It mixes project data, employee data, job classification rates, and project assignments. Unmerge the cells, drop the derived attribute, isolate partial dependencies into separate tables (2NF), and remove the transitive job charge rate dependency (3NF).

**Step-by-step solution.**

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

**Check.**  
*Lossless join check:*
- `PROJECT` joins with `ASSIGNMENT` on `Proj_Num` (key of `PROJECT`).
- `EMPLOYEE` joins with `ASSIGNMENT` on `Emp_No` (key of `EMPLOYEE`).
- `JOB` joins with `EMPLOYEE` on `Job_Class` (key of `JOB`).
- Every join is on a primary key, so no spurious tuples can be generated.

> [!warning] Common mistakes
> - Keeping `Total Charge` as a separate column across the decomposed tables. Derived attributes should be dropped during normalization.
> - Forgetting to decompose `Job_Class -> Chg_Hr` in 3NF. `Chg_Hr` depends on the job role, not directly on the individual employee.

**Exam tip.**  
Explicitly state that `Total Charge` is dropped because it is a calculated attribute. This shows the examiner that you understand schema optimization.

**Sources.**  
- [Deck 06 · Slides 30–40](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3, §7.5](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2023 Q.2(a) · 06 Marks

*Section A · CLO4 · Asked in: 2023*

**Question.** Consider a university tracking students, their courses and exam scores. A sample table is given below. Step by step convert this to 3NF.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">S_ID</th><th style="padding: 4px 10px;">S-Name</th><th style="padding: 4px 10px;">Courses</th><th style="padding: 4px 10px;">Instructors</th><th style="padding: 4px 10px;">Grades</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">1</td><td style="padding: 4px 10px;">Alice</td><td style="padding: 4px 10px;">Math, Physics</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Brown</td><td style="padding: 4px 10px;">A, B+</td></tr><tr><td style="padding: 4px 10px;">2</td><td style="padding: 4px 10px;">Bob</td><td style="padding: 4px 10px;">Chemistry</td><td style="padding: 4px 10px;">Dr. White</td><td style="padding: 4px 10px;">A-</td></tr><tr><td style="padding: 4px 10px;">3</td><td style="padding: 4px 10px;">Charlie</td><td style="padding: 4px 10px;">Math, Biology, Chemistry</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Gray, Dr. White</td><td style="padding: 4px 10px;">B+, A-, A</td></tr></tbody></table>

**Answer.**

**What the examiner wants.**  
Step-by-step conversion starting from unnormalized table to 1NF (atomic rows, 2 marks), then to 2NF eliminating partial dependencies (2 marks), and checking/verifying 3NF (2 marks).

**Key idea.**  
Flatten the comma-separated lists to get 1NF. Notice that student names depend on student ID, and instructor depends on course. These are partial dependencies on the composite key `(S_ID, Course)`. Splitting into `STUDENT`, `COURSE`, and `ENROLLMENT` achieves 2NF. Since there are no further transitive dependencies, the tables are also in 3NF.

**Step-by-step solution.**

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

**Check.**  
*Reconstruction check:*
- Query: What did Alice score in Math, and who taught it?  
  Join `STUDENT` on `S_ID = 1`, `ENROLLMENT` on `Course = 'Math'`, and `COURSE` on `Course = 'Math'`. Result: Alice, Math, Dr. Smith, Grade A. Perfectly matches row 1 of the initial table.

> [!warning] Common mistakes
> - Splitting the data incorrectly by pairing the wrong instructor with the wrong course. Follow the exact order in the comma-separated strings!
> - Overcomplicating Step 3: if a relation in 2NF has no transitive dependencies, clearly state that it already satisfies 3NF.

**Exam tip.**  
Underline the primary keys in your final relations to make them stand out clearly.

**Sources.**  
- [Deck 06 · Slides 30–40](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3, §7.5](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### 2024 Q.3(a) · 04 Marks

*Section A · CO2 · Asked in: 2024*

**Question.** A library database stores information about Books, Authors, Publishers and Borrowers. Create a table that contains some data redundancy and partial dependencies. Also, show the procedure to normalize the table.

**Answer.**

**What the examiner wants.**  
Designing an unnormalized library table that clearly exhibits data redundancy and partial dependencies (2 marks), followed by a clear step-by-step normalization procedure decomposing into 2NF and 3NF relations (2 marks).

**Key idea.**  
Create a table with a composite primary key like `(Book_ID, Borrower_ID)`. Store book details (title, publisher) and borrower details (borrower name) alongside the loan date. Because book details depend only on `Book_ID` and borrower name depends only on `Borrower_ID`, the table has clear partial dependencies and redundancy.

**Step-by-step solution.**

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

**Check.**  
*Self-test on entities:*
- Does the final schema represent Books, Authors, Publishers, and Borrowers cleanly?  
  Yes. Books, Authors, and Borrowers each have dedicated relations, and `Publisher_Name` is recorded with each Book.
- Are all partial dependencies removed?  
  Yes. `LOAN` contains only the composite key `(Book_ID, Borrower_ID)` and its fully dependent attribute `Borrow_Date`.

> [!warning] Common mistakes
> - Creating an example table with a single-attribute primary key. Partial dependencies require a composite primary key!
> - Forgetting to define the primary keys of the final normalized tables.

**Exam tip.**  
Keep your invented table small: 3 rows and 8 columns are enough to showcase both partial and transitive dependencies clearly.

**Sources.**  
- [Deck 06 · Slides 31–40](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3, §7.5](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.9 · BCNF; 3NF vs BCNF; highest normal form

### CT-03 Q.01(d) · 02 Marks

*CO3 · Asked in: CT-03*

**Question.** Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(d)** Determine the highest normal form satisfied by the given relation. Give a proper justification.

**Answer.**

**What the examiner wants.**  
Identifying the highest normal form satisfied (1NF, 1 mark) and giving a rigorous justification explaining why it satisfies 1NF but fails 2NF (1 mark).

**Key idea.**  
All attribute values are atomic, so the relation is in 1NF. But the composite key is `(StudentID, CourseID)`, and non-prime attributes like `StudentName` and `CourseName` depend on parts of that key. Since partial dependencies exist, it fails 2NF. The highest normal form reached is therefore 1NF.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: Could this relation be in 2NF if `Grade` was the only non-prime attribute?  
  A: Yes! If `Grade` were the only non-prime attribute, it would depend on the full composite key, so no partial dependencies would exist.
- Q: What is needed to bring this relation to 2NF?  
  A: Decompose into relations where non-prime attributes depend on full keys.

> [!warning] Common mistakes
> - Guessing 2NF or 3NF without checking if non-prime attributes depend on subsets of the candidate key.
> - Forgetting to state that it satisfies 1NF before explaining why it fails 2NF.

**Exam tip.**  
A 2-mark question requires only 3 to 4 sentences: confirm 1NF atomicity, point out one partial dependency, and conclude that the relation violates 2NF.

**Sources.**  
- [Deck 06 · Slides 30–31](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.4](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

### CT-03 Q.04 · 04 Marks

*CO3 · Asked in: CT-03*

**Question.** Justify the statement: "Every BCNF relation is in 3NF, but every 3NF relation is not necessarily in BCNF."

**Answer.**

**What the examiner wants.**  
Formal definitions of 3NF and BCNF showing why BCNF condition is a strict subset of 3NF conditions (2 marks), followed by a concrete counterexample relation that satisfies 3NF but violates BCNF (2 marks).

**Key idea.**  
BCNF requires every determinant to be a superkey. 3NF allows an escape clause: if the determinant is not a superkey, the dependency is still valid as long as the right-hand side consists of prime attributes. Therefore, BCNF is strictly stronger than 3NF.

**Step-by-step solution.**

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

**Check.**  
*Quick self-test:*
- Q: What is the benefit of 3NF over BCNF?  
  A: A 3NF decomposition can always achieve both lossless join and dependency preservation. BCNF decomposition cannot always preserve functional dependencies.
- Q: What makes $A$ a prime attribute in $D \rightarrow A$?  
  A: Attribute $A$ belongs to candidate key $AB$.

> [!warning] Common mistakes
> - Explaining the statement in prose without giving the mathematical definition of both normal forms.
> - Inventing an incorrect counterexample that fails 3NF as well. Use the standard example $R(A, B, C, D)$ with $AB \rightarrow CD$ and $D \rightarrow A$ from the lecture slides.

**Exam tip.**  
Use the exact counterexample from Slide 40 and Slide 43 of Deck 06 ($R(A, B, C, D)$ with $AB \rightarrow CD, D \rightarrow A$). Examiners at RUET recognize it immediately.

**Sources.**  
- [Deck 06 · Slides 40–43](../LectureSlides/06_DBMS_Normalization.md)
- [Textbook Ch. 7 §7.3.1, §7.3.3](../Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md)

---

## T08.10 · Pros/cons of normalization; denormalization

*No questions from past finals or class tests.*

*See also:* [[#T08.6 · Define normalization (and its importance) & 1NF / 2NF / 3NF]] (2017 Q.3(a))

---

## T08.11 · Lossless-join decomposition & dependency preservation

*No questions from past finals or class tests.*

---

[← Prev: T07 · Triggers and Stored Procedures](T07_Triggers_and_Stored_Procedures.md) | [Exam-style layer](../Topicwise_answers_exam_style/T08_Normalization_and_Functional_Dependencies.md) | [Next: T09 · Transactions, ACID, and Anomalies →](T09_Transactions_ACID_and_Anomalies.md)
