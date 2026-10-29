# ECE 2215: Database Systems — Database Normalization

<!-- Slide 1 -->
## Database Normalization
### Course Title: Data Base Systems
### Course No.: ECE 2215

**Rajshahi University of Engineering & Technology**

**Md. Rakibul Islam**  
Lecturer, Dept. of ETE, RUET  

*Heaven's Light is Our Guide*

---

<!-- Slide 2 -->
## Outline

1. Why Do We Need Normalization?
2. What is Normalization?
3. Insertion, deletion and update anomalies
4. Keys in DBMS
5. Functional Dependency
6. First Normal Form (1NF)
7. Second Normal Form (2NF)
8. Third Normal Form (3NF)
9. Boyce-Codd Normal Form(BCNF)
10. Denormalization
11. Decomposition

---

<!-- Slide 3 -->
## Why Do We Need Normalization?

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | AI | Dr. Abdullah | 018... |
| S02 | Zoha | DBMS | Dr. Hasan | 017... |

Notice that:
- Student information may be repeated
- Instructor information may be repeated
- Same course information may appear many times

**Problem:** Redundant data can cause inconsistencies.  
**Solution:** Database normalization.

---

<!-- Slide 4 -->
## What is Normalization?

Normalization is the process of organizing data in a database to:
- Reduce unnecessary data redundancy
- Eliminate undesirable data dependencies
- Prevent insertion, deletion and update anomalies
- Improve data consistency and integrity

---

<!-- Slide 5 -->
## Row-Level Duplication

Row-level duplication refers to entirely identical records across multiple rows. Row-level duplication occurs when an entire horizontal record (across all columns) is repeated.

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S02 | Zoha | DBMS | Dr. Hasan | 017... |

**Solution:** Primary Key.

---

<!-- Slide 6 -->
## Column-Level Duplication

Column-level duplication happens vertically within a single attribute field, or horizontally when two separate columns share redundant information. A single column repeats the same value across different rows.

**Problem:** There are three types of Anomalies.  
**Solution:** Normalization.

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | AI | Dr. Abdullah | 018... |
| S02 | Zoha | DBMS | Dr. Hasan | 017... |

---

<!-- Slide 7 -->
## Problems Without Normalization

1. **Update Anomaly**  
   The same information must be updated in multiple rows.

2. **Insertion Anomaly**  
   We cannot insert information unless some unrelated information is also available.

3. **Deletion Anomaly**  
   Deleting one piece of information accidentally removes another important piece of information.

---

<!-- Slide 8 -->
## Update Anomaly

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | AI | Dr. Abdullah | 018... |
| S02 | Zoha | DSA | Dr. Hasan | 017... |

Suppose Dr. Hasan changes to another instructor.  
We must update multiple rows.  
If one row is not updated:  
$\rightarrow$ Inconsistent data  

This is an update anomaly.

---

<!-- Slide 9 -->
## Insertion Anomaly

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | AI | Dr. Abdullah | 018... |
| S02 | Zoha | DSA | Dr. Hasan | 017... |

Suppose a new course is introduced:  
C04 - Machine Learning  
But no student has enrolled yet.  
If the table requires Student_ID:  
We cannot insert the course information without a student.  

This is an Insertion Anomaly

Normalization separates independent entities into different relations.

---

<!-- Slide 10 -->
## Deletion Anomaly

| Student_ID | Student_Name | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- | :--- |
| S01 | Riad | DBMS | Dr. Hasan | 017... |
| S01 | Riad | AI | Dr. Abdullah | 018... |
| S02 | Zoha | DSA | Dr. Hasan | 017... |

If S01 drops the AI course and we delete the row:  
$\rightarrow$ Information about AI course may also disappear.  

This is a:  
**Deletion Anomaly**

---

<!-- Slide 11 -->
## Keys in DBMS

A key is an attribute or a combination of attributes used to uniquely identify records (tuples) in a relational table.

**Main Types of Keys:**
- **Super Key:** Any attribute or combination of attributes that uniquely identifies a row.
- **Candidate Key:** A minimal Super Key with no unnecessary attributes.
- **Primary Key:** The Candidate Key selected to uniquely identify each row.
- **Alternate Key:** Candidate Keys that are not selected as the Primary Key.
- **Foreign Key:** An attribute that references the Primary Key of another table.
- **Composite Key:** A key consisting of two or more attributes.

---

<!-- Slide 12 -->
## Keys in DBMS

| Student_ID | Email | Name | Department |
| :--- | :--- | :--- | :--- |
| 101 | a@gmail.com | Akib | ECE |
| 102 | b@gmail.com | Shuvo | ECE |
| 103 | c@gmail.com | Sakib | ETE |

**Possible keys:**
- $\{\text{Student\_ID}\} \rightarrow \text{Candidate Key}$
- $\{\text{Email}\} \rightarrow \text{Candidate Key}$
- $\{\text{Student\_ID}, \text{Name}\} \rightarrow \text{Super Key}$
- $\{\text{Student\_ID}, \text{Email}\} \rightarrow \text{Super Key}$
- If Student_ID is selected $\rightarrow \text{Primary Key}$
- Email $\rightarrow \text{Alternate Key}$

---

<!-- Slide 13 -->
## Keys in DBMS

| Student_ID | Course_ID | Semester | Grade |
| :--- | :--- | :--- | :--- |
| 101 | CSE101 | Spring | A |
| 101 | CSE102 | Spring | B+ |
| 102 | CSE101 | Spring | A- |

$\text{Composite Key} = \{\text{Student\_ID}, \text{Course\_ID}\}$

---

<!-- Slide 14 -->
## Functional Dependency

A functional dependency (FD) describes a relationship between attributes.

**Notation:**  
$$X \rightarrow Y$$

**Read as:**  
$X$ determines $Y$.

| Student_ID | Student_Name | Department |
| :--- | :--- | :--- |
| S01 | Ferdous | CSE |
| S02 | Zaman | ETE |
| S03 | Nabila | ECE |

---

<!-- Slide 15 -->
## Types of Functional Dependency

### 1. Trivial Functional Dependency
If the attributes on the right side are already part of the left side:
$$\{\text{Student\_ID}, \text{Student\_Name}\} \rightarrow \text{Student\_Name}$$
This is a Trivial FD.

### 2. Non-Trivial Functional Dependency
If the right-side attribute is not part of the left side:
$$\text{Student\_ID} \rightarrow \text{Student\_Name}$$
This is a Non-Trivial FD.

### 3. Full Functional Dependency
An attribute depends on the entire composite key, not just part of it.

**Example:**
$$\{\text{Student\_ID}, \text{Course\_ID}\} \rightarrow \text{Grade}$$
The grade depends on both the student and the course.

---

<!-- Slide 16 -->
## Types of Functional Dependency

### 4. Partial Dependency
A non-key (non-prime) attribute depends on only part of a composite key.

**Example:**
$$\{\text{Student\_ID}, \text{Course\_ID}\} \rightarrow \text{Student\_Name}$$
But:
$$\text{Student\_ID} \rightarrow \text{Student\_Name}$$
Therefore, Student_Name depends only on part of the composite key.

A **Prime Attribute** is an attribute that is a member of at least one Candidate Key of a relation.

An attribute that does not belong to any Candidate Key is called a **Non-Prime Attribute**.

---

<!-- Slide 17 -->
## Types of Functional Dependency

### 5. Transitive Dependency
A Transitive Dependency occurs when a non-key (non-prime) attribute depends on another non-key (non-prime) attribute, which in turn depends on the primary key.

**Example:**  
$$\text{STUDENT}(\text{Student\_ID}, \text{Student\_Name}, \text{Dept\_ID}, \text{Department\_Name})$$

**Functional Dependencies:**
- $\text{Student\_ID} \rightarrow \text{Student\_Name}$
- $\text{Student\_ID} \rightarrow \text{Dept\_ID}$
- $\text{Dept\_ID} \rightarrow \text{Department\_Name}$

$\text{Candidate key} = \{\text{Student\_ID}\}$  
Dept_ID and Department_Name both are non-prime attribute.  
So a non-prime attribute depends on another non-prime attribute.

---

<!-- Slide 18 -->
## Properties of Functional Dependencies

Armstrong’s Axioms are a set of rules used to infer new Functional Dependencies (FDs) from existing FDs.

Suppose we have attributes $A, B, C$.

### 1. Reflexivity Rule
If $B \subseteq A$, then:
$$A \rightarrow B$$

**Example:**
$$\{\text{Student\_ID}, \text{Name}\} \rightarrow \text{Student\_ID}$$
Because Student_ID is already part of the left-hand side.

---

<!-- Slide 19 -->
## Properties of Functional Dependencies

### 2. Augmentation Rule
If:
$$A \rightarrow B$$
then:
$$AC \rightarrow BC$$

**Example:**  
If:
$$\text{Student\_ID} \rightarrow \text{Student\_Name}$$
Then:
$$\{\text{Student\_ID}, \text{Course\_ID}\} \rightarrow \{\text{Student\_Name}, \text{Course\_ID}\}$$

---

<!-- Slide 20 -->
## Properties of Functional Dependencies

### 3. Transitivity Rule
If:
$$A \rightarrow B$$
and
$$B \rightarrow C$$
then:
$$A \rightarrow C$$

**Example:**  
$$\text{Student\_ID} \rightarrow \text{Dept\_ID}$$
$$\text{Dept\_ID} \rightarrow \text{Department}$$
Therefore:
$$\text{Student\_ID} \rightarrow \text{Department}$$

---

<!-- Slide 21 -->
## Properties of Functional Dependencies

### 4. Union / Additivity
If:
$$A \rightarrow B$$
$$A \rightarrow C$$
Then:
$$A \rightarrow BC$$

**Example:**  
If:
$$\text{Student\_ID} \rightarrow \text{Name}$$
$$\text{Student\_ID} \rightarrow \text{Department}$$
Then:
$$\text{Student\_ID} \rightarrow \{\text{Name}, \text{Department}\}$$

---

<!-- Slide 22 -->
## Properties of Functional Dependencies

### 5. Decomposition / Projectivity
If:
$$A \rightarrow BC$$
Then:
$$A \rightarrow B$$
and
$$A \rightarrow C$$

**Example:**  
$$\text{Student\_ID} \rightarrow \{\text{Name}, \text{Department}\}$$
can be decomposed into:
$$\text{Student\_ID} \rightarrow \text{Name}$$
$$\text{Student\_ID} \rightarrow \text{Department}$$

---

<!-- Slide 23 -->
## Properties of Functional Dependencies

### 6. Pseudotransitivity
If:
$$A \rightarrow B$$
and
$$CB \rightarrow D$$
Then:
$$CA \rightarrow D$$

**Example:**  
$$\text{Student\_ID} \rightarrow \text{Dept\_ID}$$
and
$$\{\text{Dept\_ID}, \text{Semester}\} \rightarrow \text{Faculty}$$
Therefore:
$$\{\text{Student\_ID}, \text{Semester}\} \rightarrow \text{Faculty}$$

---

<!-- Slide 24 -->
## Properties of Functional Dependencies

| Property | Rule | Meaning |
| :--- | :--- | :--- |
| Reflexivity | $A \rightarrow B\text{, if } B \subseteq A$ | $A$ determines its subset |
| Augmentation | $A \rightarrow B \Rightarrow AC \rightarrow BC$ | Add the same attributes to both sides |
| Transitivity | $A \rightarrow B, B \rightarrow C \Rightarrow A \rightarrow C$ | Dependency can be transferred |
| Union | $A \rightarrow B, A \rightarrow C \Rightarrow A \rightarrow BC$ | Combine dependencies |
| Decomposition | $A \rightarrow BC \Rightarrow A \rightarrow B, A \rightarrow C$ | Split dependencies |
| Pseudotransitivity | $A \rightarrow B, CB \rightarrow D \Rightarrow CA \rightarrow D$ | Extended transitivity |

---

<!-- Slide 25 -->
## Finding Closure of Functional Dependencies

The closure of an attribute set, written as $F^+$ or $X^+$, is the set of all attributes that can be functionally determined by $X$ using a given set of Functional Dependencies (FDs).

If: $X^+ = \{A, B, C, D\}$  
it means that starting with attributes $X$, we can determine $A$, $B$, $C$, and $D$.

### Why do we find closure?
Attribute closure is useful for:
- Finding Candidate Keys
- Checking whether an FD is valid
- Testing whether an attribute set is a Super Key
- Database normalization
- Decomposing relations

---

<!-- Slide 26 -->
## Finding Closure of Functional Dependencies

**Given Relation**  
$$R(A, B, C, D, E) \qquad \text{FD} = \{A \rightarrow B, B \rightarrow C, C \rightarrow D, D \rightarrow E\}$$

Find: $A^+$

- **Step 1:** Start with $A$  
  $A^+ = \{A\}$
- **Step 2:** Apply $A \rightarrow B$  
  $A^+ = \{A, B\}$
- **Step 3:** Apply $B \rightarrow C$  
  $A^+ = \{A, B, C\}$
- **Step 4:** Apply $C \rightarrow D$  
  $A^+ = \{A, B, C, D\}$
- **Step 5:** Apply $D \rightarrow E$  
  $A^+ = \{A, B, C, D, E\}$

Since $A^+$ contains all attributes of $R$, $A$ is a Super Key.  
If $A$ is also minimal, then $A$ is a Candidate Key.

$$B^+ = \{B, C, D, E\}$$
$$C^+ = \{C, D, E\}$$
$$D^+ = \{D, E\}$$
$$E^+ = \{E\}$$

$$\text{CK} = \{A\}$$
$$\text{Prime attribute} = \{A\}$$
$$\text{Non-prime attribute} = \{B, C, D, E\}$$

---

<!-- Slide 27 -->
## Finding Closure of Functional Dependencies

**Given Relation**  
$$R(A, B, C, D) \qquad \text{FD} = \{A \rightarrow B, B \rightarrow C, C \rightarrow D, D \rightarrow A\}$$

$$A^+ = \{A, B, C, D\}$$
$$B^+ = \{B, C, D, A\}$$
$$C^+ = \{C, D, A, B\}$$
$$D^+ = \{D, A, B, C\}$$

$$\text{CK} = \{A, B, C, D\}$$
$$\text{Prime attribute} = \{A, B, C, D\}$$
$$\text{Non-prime attribute} = \{\text{null}\}$$

---

<!-- Slide 28 -->
## Finding Closure of Functional Dependencies

**Given Relation**  
$$R(A, B, C, D, E) \qquad \text{FD} = \{A \rightarrow B, B \rightarrow C, CD \rightarrow E\}$$

$$AD^+ = \{A, D, B, C, E\}$$

$$\text{CK} = \{AD\}$$
$$\text{Prime attribute} = \{A, D\}$$
$$\text{Non-prime attribute} = \{B, C, E\}$$

---

<!-- Slide 29 -->
## Finding Closure of Functional Dependencies

**Given Relation**  
$$R(A, B, C, D, E) \qquad \text{FD} = \{A \rightarrow B, BC \rightarrow D, E \rightarrow C, D \rightarrow A\}$$

$$E^+ = \{E, C\}$$
$$AE^+ = \{A, B, E, C, D\}$$
$$DE^+ = \{D, A, B, E, C\}$$
$$BE^+ = \{B, E, C, D, A\}$$
$$CE^+ = \{C, E\}$$

$$\text{CK} = \{AE, DE, BE\}$$
$$\text{Prime attribute} = \{A, B, D, E\}$$
$$\text{Non-prime attribute} = \{C\}$$

---

<!-- Slide 30 -->
## First Normal Form (1NF)

A relation is in 1NF when:
- Each cell contains a single/atomic value
- No multi-valued attributes

| Student_ID | Name | Phone |
| :--- | :--- | :--- |
| S01 | Fahim | 0171, 0182 |
| S02 | Noor | 0193 |

| Student_ID | Name | Phone |
| :--- | :--- | :--- |
| S01 | Fahim | 0171 |
| S01 | Fahim | 0182 |
| S02 | Noor | 0193 |

---

<!-- Slide 31 -->
## Second Normal Form (2NF)

Consider:  
$$\text{ENROLLMENT}(\text{Student\_ID}, \text{Course\_ID}, \text{Student\_Name}, \text{Course\_Name}, \text{Grade})$$

**Primary Key:** $(\text{Student\_ID}, \text{Course\_ID})$

**Dependencies:**  
$$\text{Student\_ID} \rightarrow \text{Student\_Name}$$  
$$\text{Course\_ID} \rightarrow \text{Course\_Name}$$  
$$(\text{Student\_ID}, \text{Course\_ID}) \rightarrow \text{Grade}$$

A relation is in 2NF if:
1. It is already in 1NF
2. It has no partial functional dependency

| Student_ID | Course_ID | Student_Name | Course_Name | Grade |
| :--- | :--- | :--- | :--- | :--- |
| S01 | C01 | Santo | DBMS | A |
| S02 | C02 | Ratul | AI | B+ |

**Problem:**  
Student_Name depends only on Student_ID.  
Course_Name depends only on Course_ID.  
Therefore, partial dependencies exist.  
The relation is NOT in 2NF.

---

<!-- Slide 32 -->
## Second Normal Form (2NF)

| Student_ID | Student_Name |
| :--- | :--- |
| S01 | Santo |
| S02 | Ratul |

| Course_ID | Course_Name |
| :--- | :--- |
| C01 | DBMS |
| C02 | AI |

| Student_ID | Course_ID | Grade |
| :--- | :--- | :--- |
| S01 | C01 | A |
| S02 | C02 | B+ |

---

<!-- Slide 33 -->
## Second Normal Form (2NF)

| Customer_ID | Store_ID | Location |
| :--- | :--- | :--- |
| 1 | 1 | R |
| 1 | 3 | S |
| 2 | 1 | R |
| 3 | 2 | I |
| 4 | 3 | S |

**Primary Key:** $(\text{Customer\_ID}, \text{Store\_ID})$

**Dependencies:**  
$$\text{Store\_ID} \rightarrow \text{Location}$$

Here partial dependencies exist.  
The relation is NOT in 2NF.

---

<!-- Slide 34 -->
## Second Normal Form (2NF)

| Store_ID | Location |
| :--- | :--- |
| 1 | R |
| 2 | I |
| 3 | S |

| Customer_ID | Store_ID |
| :--- | :--- |
| 1 | 1 |
| 1 | 3 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |

---

<!-- Slide 35 -->
## Second Normal Form (2NF)

**Given Relation**  
$$R(A, B, C, D, E, F) \qquad \text{FD} = \{A \rightarrow B, C \rightarrow F, EC \rightarrow D, E \rightarrow A\}$$

$$CE^+ = \{C, E, F, A, B, D\}$$

$$\text{CK} = \{CE\}$$
$$\text{Prime attribute} = \{C, E\}$$
$$\text{Non-prime attribute} = \{A, B, D, F\}$$

---

<!-- Slide 36 -->
## Second Normal Form (2NF)

**Given Relation**  
$$R(A, B, C, D, E, F) \qquad \text{FD} = \{A \rightarrow B, C \rightarrow F, EC \rightarrow D, E \rightarrow A\}$$

- $A \rightarrow B \Rightarrow A \text{ and } B\text{ both are Non-prime attribute so no partial dependency.}$
- $C \rightarrow F \Rightarrow C\text{ is a part of Composite key and } F\text{ is a non-prime attribute. So here partial dependency exist.}$
- $EC \rightarrow D \Rightarrow \text{Here Fully dependency exit.}$
- $E \rightarrow A \Rightarrow E\text{ is a part of Composite key and } A\text{ is a non-prime attribute. So here partial dependency exist.}$

The relation is NOT in 2NF.

---

<!-- Slide 37 -->
## Third Normal Form (3NF)

A relation is in 3NF if:
- It is already in 2NF
- It has no transitive dependency

| Student_ID | Student_Name | Department_ID | Department_Name |
| :--- | :--- | :--- | :--- |
| S01 | Santo | D01 | ECE |
| S02 | Ratul | D02 | ETE |

| Student_ID | Student_Name | Department_ID |
| :--- | :--- | :--- |
| S01 | Santo | D01 |
| S02 | Ratul | D02 |

| Department_ID | Department_Name |
| :--- | :--- |
| D01 | ECE |
| D02 | ETE |

---

<!-- Slide 38 -->
## Third Normal Form (3NF)

| Roll | Division | District | Thana |
| :--- | :--- | :--- | :--- |
| 1 | Rajshahi | Bogura | Nandigram |
| 2 | Dhaka | Faridpur | Kotwali |
| 3 | Chattogram | Cox's Bazar | Ramu |

$$\text{FD} = \{\text{Roll} \rightarrow \text{Division}, \text{Division} \rightarrow \text{District}, \text{District} \rightarrow \text{Thana}\}$$

$$\text{CK} = \{\text{Roll}\}$$
$$\text{Prime attribute} = \{\text{Roll}\}$$
$$\text{Non-prime attribute} = \{\text{Division}, \text{District}, \text{Thana}\}$$

Here Division determines District and District determines Thana. In both case transitive dependencies exits as a non prime attributes determines another non-prime attributes.

The relation is NOT in 3NF.

---

<!-- Slide 39 -->
## Third Normal Form (3NF)

**Given Relation**  
$$R(A, B, C, D) \qquad \text{FD} = \{AB \rightarrow C, C \rightarrow D\}$$

$$AB^+ = \{A, B, C, D\}$$

$$\text{CK} = \{AB\}$$
$$\text{Prime attribute} = \{A, B\}$$
$$\text{Non-prime attribute} = \{C, D\}$$

- $AB \rightarrow C \Rightarrow \text{Fully dependency.}$
- $C \rightarrow D \Rightarrow C \ \& \ D\text{ both are non-prime attribute. So here transitive dependency exist.}$

The relation is NOT in 3NF.

---

<!-- Slide 40 -->
## Third Normal Form (3NF)

**Given Relation**  
$$R(A, B, C, D) \qquad \text{FD} = \{AB \rightarrow CD, D \rightarrow A\}$$

$$AB^+ = \{A, B, C, D\}$$
$$DB^+ = \{D, B, A, C\}$$

$$\text{CK} = \{AB, BD\}$$
$$\text{Prime attribute} = \{A, B, D\}$$
$$\text{Non-prime attribute} = \{C\}$$

- $AB \rightarrow CD \Rightarrow \text{Fully dependency.}$
- $D \rightarrow A \Rightarrow A \ \& \ D\text{ both are prime attribute. So here NO transitive dependency exist.}$

The relation is in 3NF.

---

<!-- Slide 41 -->
## Boyce-Codd Normal Form (BCNF)

BCNF is a stronger version of 3NF.

A relation is in BCNF if:  
For every non-trivial functional dependency $X \rightarrow Y$, $X$ must be a super key or candidate key.

In other words, Every determinant must be a candidate key/super key.

| 3NF | BCNF |
| :--- | :--- |
| Less strict | More strict |
| Allows some dependencies where determinant isn't a super key | Every determinant must be a super key |
| Usually easier to achieve | May require further decomposition |
| Dependency preservation is often easier | Dependency preservation may sometimes be lost |

---

<!-- Slide 42 -->
## Boyce-Codd Normal Form (BCNF)

$$R(\text{Student}, \text{Course}, \text{Instructor})$$

Functional Dependencies: $\{\text{Student}, \text{Course}\} \rightarrow \text{Instructor}, \text{Instructor} \rightarrow \text{Course}$

Candidate key: $\{\text{StudentCourse}, \text{StudentInstructor}\}$

| Functional Dependency | Is LHS a Super Key? | BCNF |
| :--- | :--- | :---: |
| $\{\text{Student}, \text{Course}\} \rightarrow \text{Instructor}$ | Yes | ✓ |
| $\text{Instructor} \rightarrow \text{Course}$ | No | ✗ |

The relation is NOT in BCNF.

---

<!-- Slide 43 -->
## Boyce-Codd Normal Form (BCNF)

**Given Relation**  
$$R(A, B, C, D) \qquad \text{FD} = \{AB \rightarrow CD, D \rightarrow A\}$$

$$AB^+ = \{A, B, C, D\}$$
$$DB^+ = \{D, B, A, C\}$$

$$\text{CK} = \{AB, BD\}$$
$$\text{Prime attribute} = \{A, B, D\}$$
$$\text{Non-prime attribute} = \{C\}$$

- $AB \rightarrow CD \Rightarrow \text{LHS is candidate key.}$
- $D \rightarrow A \Rightarrow \text{LHS is not a candidate key or super key.}$

The relation is NOT in BCNF.

---

<!-- Slide 44 -->
## Boyce-Codd Normal Form (BCNF)

**Given Relation**  
$$R(A, B, C, D, E) \qquad \text{FD} = \{A \rightarrow B, B \rightarrow C, AC \rightarrow D, D \rightarrow E\}$$

$$A^+ = \{A, B, C, D, E\}$$

$$\text{CK} = \{A\}$$

| FD | Is LHS a Super Key? | BCNF |
| :--- | :--- | :---: |
| $A \rightarrow B$ | Yes | ✓ |
| $B \rightarrow C$ | No | ✗ |
| $AC \rightarrow D$ | Yes, because $AC$ contains $A$ | ✓ |
| $D \rightarrow E$ | No | ✗ |

The relation is NOT in BCNF.

---

<!-- Slide 45 -->
## Comparison of Normal Forms

| Normal Form | Main Condition |
| :--- | :--- |
| 1NF | Atomic values |
| 2NF | 1NF + No partial dependency |
| 3NF | 2NF + No transitive dependency |
| BCNF | Every determinant is a super key or candidate key |

---

<!-- Slide 46 -->
## Practice Problem

Consider:  
$$\text{ENROLLMENT}(\text{Student\_ID}, \text{Student\_Name}, \text{Course\_ID}, \text{Course\_Name}, \text{Instructor\_ID}, \text{Instructor\_Name}, \text{Grade})$$

Assume:
- $(\text{Student\_ID}, \text{Course\_ID})$ is the primary key
- $\text{Student\_ID} \rightarrow \text{Student\_Name}$
- $\text{Course\_ID} \rightarrow \text{Course\_Name}, \text{Instructor\_ID}$
- $\text{Instructor\_ID} \rightarrow \text{Instructor\_Name}$

### Questions
1. Is the relation in 1NF?
2. Identify the partial dependencies.
3. Is it in 2NF?
4. Identify the transitive dependency.
5. Is it in 3NF if not decompose the relation into 3NF tables.
6. Identify the primary and foreign keys.

---

<!-- Slide 47 -->
## Advantages of Normalization

Normalization provides:
- Reduced data redundancy
- Improved data consistency
- Fewer update anomalies
- Fewer insertion anomalies
- Fewer deletion anomalies
- Improved data integrity
- Easier database maintenance
- Better logical database design

---

<!-- Slide 48 -->
## Disadvantages of Normalization

Normalization is not always perfect.  
There are some disadvantages also:
- More tables are created
- Queries may require more JOIN operations
- Complex queries can become slower
- Database design can become more complicated
- Excessive normalization may affect performance

**Therefore:**  
Good database design requires a balance between normalization and performance.

---

<!-- Slide 49 -->
## Denormalization

Denormalization is the process of intentionally adding redundant data or combining normalized tables to improve database read performance.

It is generally performed after normalization when query performance becomes more important than minimizing redundancy.

---

<!-- Slide 50 -->
## When to Use Denormalization?

Denormalization is useful when:
- The database is read-intensive
- Complex queries require many JOINs
- Faster response time is required
- Data is mainly used for reporting or analytics
- Performance optimization is more important than minimizing redundancy

---

<!-- Slide 51 -->
## Normalization vs Denormalization

| Normalization | Denormalization |
| :--- | :--- |
| Reduces redundancy | Introduces controlled redundancy |
| Improves data consistency | Improves read performance |
| Requires more tables | May combine tables |
| May require more JOINs | Reduces JOIN operations |
| Useful for OLTP systems | Often useful for OLAP/reporting systems |

---

<!-- Slide 52 -->
## Decomposition

The term decomposition refers to the process in which we break down a table in a database into various elements or parts. Thus, decomposition replaces a given relation with a collection of various smaller relations. Thus, in a database, we can make any table break down into multiple tables when we want to collect a particular set of data.

### Types of Decomposition
- Lossless Decomposition
- Lossy Decomposition

---

<!-- Slide 53 -->
## Lossless Decomposition

The process in which where we can regain the original relation $R$ with the help of joins from the multiple relations formed after decomposition. This process is termed as lossless decomposition.

It is used to remove the redundant data from the database while retaining the useful information. The lossless decomposition tries to ensure following things:
- While regaining the original relation, no information should be lost.
- If we perform join operation on the sub-divided relations, we must get the original relation.

---

<!-- Slide 54 -->
## Lossy Decomposition

A decomposition is lossy if joining the decomposed relations produces:
- Missing information, or
- Extra/spurious tuples

### Important Properties of Decomposition
1. Decomposition Must be Lossless
2. Dependency Preservation

---

<!-- Slide 55 -->
## Condition for Lossless-Join Decomposition

Suppose relation:  
$R$ is decomposed into: $R_1$ and $R_2$

The decomposition is lossless if:  
$$(R_1 \cap R_2) \rightarrow R_1 \quad \text{or} \quad (R_1 \cap R_2) \rightarrow R_2$$

### Meaning
The common attributes between the two relations must functionally determine all attributes of at least one relation.

---

<!-- Slide 56 -->
## Lossless-Join Example

Consider:  
$$R(A, B, C) \qquad \text{Functional dependency: } A \rightarrow B$$

Decompose $R$ into: $R_1(A, B)$ and $R_2(A, C)$

Common attribute: $R_1 \cap R_2 = \{A\}$

Since:
$$A \rightarrow AB$$
Therefore:
$$A \rightarrow R_1$$

Hence:  
**The decomposition is Lossless.**

---

<!-- Slide 57 -->
## Dependency Preservation

A decomposition is dependency preserving if all functional dependencies can be checked without joining the decomposed relations.

Suppose:  
$$R(A, B, C) \qquad \text{Functional dependencies: } A \rightarrow B, \ B \rightarrow C$$

Decompose into: $R_1(A, B)$ and $R_2(B, C)$

Both dependencies can still be enforced directly:
- In $R_1$: $A \rightarrow B$
- In $R_2$: $B \rightarrow C$

Therefore:  
**The decomposition is Dependency Preserving.**

---

<!-- Slide 58 -->
## Dependency Preservation

Consider:  
$$R(A, B, C) \qquad \text{Functional dependencies: } A \rightarrow B, \ B \rightarrow C$$

Suppose we decompose into:  
$R_1(A, B)$ and $R_2(A, C)$

The dependency:  
$B \rightarrow C$ cannot be checked directly in either relation.

Therefore:  
**The decomposition is NOT dependency preserving.**

---

<!-- Slide 59 -->
## Decomposition in Different Normal Forms

### 1NF
Decomposition may be required to remove:
- Repeating groups
- Multi-valued attributes

### 2NF
Decomposition removes:
- Partial dependencies

### 3NF
Decomposition removes:
- Transitive dependencies

### BCNF
Decomposition removes:
- Functional dependencies where the determinant is not a super key or candidate key.

> **3NF always ensure dependency preserving decomposition but not in BCNF**

---

<!-- Slide 60 -->
## General Steps of Decomposition

- **Step 1:** Identify the relation: $R(A_1, A_2, \dots, A_n)$
- **Step 2:** Identify all functional dependencies.
- **Step 3:** Identify candidate keys.
- **Step 4:** Determine whether the relation violates a normal form.
- **Step 5:** Identify the problematic dependency.
- **Step 6:** Create separate relations.
- **Step 7:** Check:
  - Lossless join
  - Dependency preservation

---

<!-- Slide 61 -->
## Practice Problem

Check whether this decomposition given is a lossy or lossless join decomposition.

$\text{Relational Schema} = R(X, Y, Z)$

Decompositions,  
$R_1(X, Y)$  
$R_2(X, Z)$

**Relation $R(X, Y, Z)$:**

| X | Y | Z |
| :--- | :--- | :--- |
| X1 | Y1 | Z1 |
| X2 | Y1 | Z1 |
| X1 | Y2 | Z2 |
| X1 | Y3 | Z3 |

**Decomposition $R_1(X, Y)$:**

| X | Y |
| :--- | :--- |
| X1 | Y1 |
| X2 | Y1 |
| X1 | Y2 |
| X1 | Y3 |

**Decomposition $R_2(X, Z)$:**

| X | Z |
| :--- | :--- |
| X1 | Z1 |
| X2 | Z1 |
| X1 | Z2 |
| X1 | Z3 |

---

<!-- Slide 62 -->
## Practice Problem

Solution: Now, this decomposition will be lossless if $R = R_1 \bowtie R_2$

Thus, $R_1 \bowtie R_2$ will be equal to

**$R_1 \bowtie R_2$:**

| X | Y | Z |
| :--- | :--- | :--- |
| X1 | Y1 | Z1 |
| X1 | Y1 | Z2 |
| X2 | Y1 | Z1 |
| X1 | Y2 | Z2 |
| X1 | Y2 | Z1 |
| X1 | Y3 | Z3 |
| X1 | Y3 | Z1 |

**Original Relation $R$:**

| X | Y | Z |
| :--- | :--- | :--- |
| X1 | Y1 | Z1 |
| X2 | Y1 | Z1 |
| X1 | Y2 | Z2 |
| X1 | Y3 | Z3 |

As $R_1 \bowtie R_2$ is not equal to $R$, so it is Lossy Decomposition

---

<!-- Slide 63 -->
## Thank you
