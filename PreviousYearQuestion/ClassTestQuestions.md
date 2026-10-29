---
course_code: ECE 2215
course_title: Database Systems
document_type: Class Test Questions
tags:
  - class-tests
  - ece2215
  - dbms
  - relational-algebra
  - sql
  - normalization
  - transactions
---

# Department of Electrical & Computer Engineering
### Rajshahi University of Engineering & Technology (RUET)
**Course Code:** ECE 2215  
**Course Title:** Database Systems  
**Document:** Class Test (CT) Question Collection  

---

## Navigation & Overview

- [Class Test 01 (Data Abstraction, Schema & Relational Algebra)](#class-test-01-data-abstraction-schema--relational-algebra) — *Data Abstraction, Schema Diagram, Application Architecture, Relational Algebra Queries & Expressions*
- [Class Test 02 (SQL Queries & ER Modeling)](#class-test-02-sql-queries--er-modeling) — *SQL Data Retrieval, Aggregate Functions, Subqueries without LIMIT, ER Modeling (Entities, Relationships, Cardinality)*
- [Class Test 03 (Functional Dependencies, Normalization & BCNF)](#class-test-03-functional-dependencies-normalization--bcnf) — *Candidate Keys, Prime/Non-Prime Attributes, Normal Forms (1NF/2NF/3NF/BCNF), Anomalies*
- [Class Test 04 (Transactions, ACID & Conflict Serializability)](#class-test-04-transactions-acid--conflict-serializability) — *ACID Properties, Serial vs Concurrent Schedules, Concurrency Problems, Conflict Serializability Testing*

---

## Class Test 01 (Data Abstraction, Schema & Relational Algebra)

| Parameter | Details |
| :--- | :--- |
| **Institution** | Rajshahi University of Engineering & Technology |
| **Department** | Electrical & Computer Engineering |
| **Course No.** | ECE 2215 |
| **Course Title** | Data Base Systems |
| **Test Title** | CT - 1 |
| **Marks** | 20 |
| **Time** | 30 minutes |
| **Curriculum Standard** | With CO Mapping |

---

### Question 01

Define data abstraction. Describe different types of data abstractions.

**Marks:** 05 &emsp; | &emsp; **CO:** CO1

---

### Question 02

Draw a schema diagram for ECE, including 5 tables (Students, Courses, Instructors, Classroom, Results).

**Marks:** 05 &emsp; | &emsp; **CO:** CO1

---

### Question 03

Describe the structure of a database application.

**Marks:** 02 &emsp; | &emsp; **CO:** CO1

---

### Question 04

Relations:
- $\text{STUDENT}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name}, \text{CGPA})$
- $\text{COURSE}(\text{Course\_ID}, \text{Course\_Name}, \text{Student\_ID}, \text{Semester}, \text{Marks})$
- $\text{ALUMNI}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name})$

Write the relational algebra expressions for the following conditions using the relations above.

- **v.** Write the relational algebra expression to rename the relation $\text{STUDENT}$ as $\text{S}$ and display the $\text{Student\_ID}$ and $\text{Name}$ of all students.
- **vi.** Retrieve the $\text{Student\_ID}$, $\text{Name}$, and $\text{Course\_Name}$ of all students who belong to the CSE department and scored 80 or more marks in any course.
- **vii.** Write the relational algebra expression to retrieve the $\text{Student\_ID}$ and $\text{Name}$ of all students who are either in the $\text{STUDENT}$ relation or the $\text{ALUMNI}$ relation.
- **viii.** Write the relational algebra expression to determine the number of students in each department.

*(Note: Sub-parts are numbered v, vi, vii, viii on the original question script).*

**Marks:** 04 &emsp; | &emsp; **CO:** CO1

---

### Question 05

Describe the following relational algebra expression:

- **iii.**
  $$\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$$

- **iv.**
  $$\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$$

*(Note: Sub-parts are numbered iii, iv on the original question script).*

**Marks:** 04 &emsp; | &emsp; **CO:** CO1

---

## Class Test 02 (SQL Queries & ER Modeling)

| Parameter | Details |
| :--- | :--- |
| **Institution** | Rajshahi University of Engineering & Technology |
| **Department** | Electrical & Computer Engineering |
| **Course No.** | ECE 2215 |
| **Course Title** | Data Base Systems |
| **Test Title** | CT - 2 |
| **Marks** | 20 |
| **Time** | 20 minutes |
| **Curriculum Standard** | With CO Mapping |

---

### Question 01

Consider the table and write SQL queries for the following queries:

$$\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$$

- **(a)** Display all students from the ECE department. `[Marks: 02 | CO: CO2]`
- **(b)** Display students from the ECE department whose CGPA is greater than 3.50, arranged by CGPA in descending order. `[Marks: 02 | CO: CO2]`
- **(c)** Find students whose CGPA is greater than the overall average CGPA. `[Marks: 03 | CO: CO2]`
- **(d)** Display the students having the second-highest CGPA without using LIMIT. `[Marks: 03 | CO: CO2]`

**Marks:** 10 &emsp; | &emsp; **CO:** CO2

---

### Question 02

A university maintains information about Students, Courses, and Teachers. A student can enroll in several courses and each course can have many students. Each course is taught by one teacher, though a teacher may teach several courses.

- **(a)** Identify the entities, attributes, primary keys, relationships, and cardinalities. `[Marks: 04 | CO: CO3]`
- **(b)** Draw the complete ER diagram. `[Marks: 06 | CO: CO3]`

**Marks:** 10 &emsp; | &emsp; **CO:** CO3

---

## Class Test 03 (Functional Dependencies, Normalization & BCNF)

| Parameter | Details |
| :--- | :--- |
| **Institution** | Rajshahi University of Engineering & Technology |
| **Department** | Electrical & Computer Engineering |
| **Course No.** | ECE 2215 |
| **Course Title** | Data Base Systems |
| **Test Title** | Class Test - 3 |
| **Marks** | 20 |
| **Time** | 30 Minutes |
| **Curriculum Standard** | With CO Mapping |

---

### Question 01

Consider the relation:

$$\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$$

Assume the following functional dependencies:

$$\begin{aligned}
\text{StudentID} &\rightarrow \text{StudentName} \\
\text{CourseID} &\rightarrow \text{CourseName}, \text{InstructorID} \\
\text{InstructorID} &\rightarrow \text{InstructorName} \\
(\text{StudentID}, \text{CourseID}) &\rightarrow \text{Grade}
\end{aligned}$$

- **a)** Identify all the possible candidate key of the relation. `[Marks: 04]`
- **b)** Identify the prime and non-prime attributes. `[Marks: 02]`
- **c)** Identify the partial and transitive dependencies. `[Marks: 02]`
- **d)** Determine the highest normal form satisfied by the given relation. Give a proper justification. `[Marks: 02]`

**Marks:** 10 &emsp; | &emsp; **CO:** CO3

---

### Question 02

Mention the problems caused by an unnormalized relation.

**Marks:** 03 &emsp; | &emsp; **CO:** CO3

---

### Question 03

Define normalization and state its main objective.

**Marks:** 03 &emsp; | &emsp; **CO:** CO3

---

### Question 04

Justify the statement: "Every BCNF relation is in 3NF, but every 3NF relation is not necessarily in BCNF."

**Marks:** 04 &emsp; | &emsp; **CO:** CO3

---

## Class Test 04 (Transactions, ACID & Conflict Serializability)

| Parameter | Details |
| :--- | :--- |
| **Institution** | Rajshahi University of Engineering & Technology |
| **Department** | Electrical & Computer Engineering |
| **Course No.** | ECE 2215 |
| **Course Title** | Data Base Systems |
| **Test Title** | Class Test - 4 |
| **Marks** | 20 |
| **Time** | 30 Minutes |
| **Curriculum Standard** | With CO Mapping |

---

### Question 01

Define a transaction? Explain the four ACID properties of a transaction with suitable examples.

**Marks:** 06 &emsp; | &emsp; **CO:** CO3

---

### Question 02

Differentiate between a serial schedule and a concurrent schedule. Mention two advantages of concurrent execution of transactions.

**Marks:** 04 &emsp; | &emsp; **CO:** CO3

---

### Question 03

Explains any two problems caused by concurrent execution.

*(Note: Printed as "Explains any two problems caused by concurrent execution." in the original question script).*

**Marks:** 04 &emsp; | &emsp; **CO:** CO3

---

### Question 04

Determine whether the schedule is conflict serializable or not. If it is serializable, give the equivalent serial order.

| $T_1$ | $T_2$ | $T_3$ |
| :---: | :---: | :---: |
| $\text{Write}(A)$ | | |
| | $\text{Read}(A)$ | |
| | | $\text{Write}(B)$ |
| $\text{Write}(B)$ | | |
| | | $\text{Write}(B)$ |
| | $\text{Write}(A)$ | |
| | | $\text{Read}(B)$ |
| | $\text{Read}(B)$ | |

**Marks:** 06 &emsp; | &emsp; **CO:** CO3
