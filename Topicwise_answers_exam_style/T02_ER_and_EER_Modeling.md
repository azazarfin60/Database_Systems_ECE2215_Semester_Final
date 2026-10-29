---
title: "T02 · E-R and EER Modeling · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T01 · DB Concepts and Architecture](T01_DB_Concepts_and_Architecture.md) | [Explanation layer](../Topicwise_answers_explaination/T02_ER_and_EER_Modeling.md) | [Next: T03 · Relational Model, Keys & Integrity →](T03_Relational_Model_Keys_and_Integrity.md)

---

# T02 · E-R and EER Modeling

> [!info] Topic card
> **Syllabus:** Unit 2 · **Weight:** 67 final marks (10.5%) in 7/7 papers + 10 CT marks
> **Sources:** Deck 05 · Textbook Ch. 6
> **Blocks in this file:** 18 final + 1 CT questions (15 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T02.1 | Entity sets, relationship sets, types of relationships | 4 + 0 | 2021 Q.5(a) | [[#T02.1 · Entity sets, relationship sets, types of relationships\|Go]] |
| T02.2 | Attribute types | 8 + 0 | 2020 Q.5(a), 2021 Q.3(b) | [[#T02.2 · Attribute types\|Go]] |
| T02.3 | Mapping cardinality and participation constraints | 8 + 0 | 2018 Q.3(c), 2020 Q.1(c) | [[#T02.3 · Mapping cardinality and participation constraints\|Go]] |
| T02.4 | Weak vs strong entity sets | 11 + 0 | 2018 Q.1(b), 2019 Q.1(b), 2020 Q.2(c), 2021 Q.8(c) | [[#T02.4 · Weak vs strong entity sets\|Go]] |
| T02.5 | Design a full E-R diagram for a scenario | 24 + 10 | 2017 Q.1(b), 2018 Q.1(c), 2019 Q.1(c), 2023 Q.1(a), 2024 Q.1(b), CT-02 Q.02 | [[#T02.5 · Design a full E-R diagram for a scenario\|Go]] |
| T02.6 | Reduction of E-R to relational tables | 5 + 0 | 2018 Q.2(c) | [[#T02.6 · Reduction of E-R to relational tables\|Go]] |
| T02.7 | EER: specialization / generalization | 2 + 0 | 2017 Q.6(a) | [[#T02.7 · EER: specialization / generalization\|Go]] |
| T02.8 | EER: aggregation | 5 + 0 | 2018 Q.2(b), 2020 Q.3(a) | [[#T02.8 · EER: aggregation\|Go]] |

---

## T02.1 · Entity sets, relationship sets, types of relationships

### 2021 Q.5(a) · 04 Marks

*Section B · CLO1 · Asked in: 2021 · L1 (asked once)*

**Question.** What is ER diagram? Illustrate different types of relationship that can be represented in ER diagram.

**Answer.**

An **Entity-Relationship (E-R) diagram** is a graphical tool used in database design. It represents the conceptual schema of an enterprise by depicting entities, their attributes, and the relationships among them.

The **degree** of a relationship set is the number of participating entity sets. Different types of relationships based on degree include:

1. **Unary (Recursive) Relationship (Degree 1):**
   - The same entity set participates more than once in different roles.
   - *Example:* A `course` entity related to another `course` entity via a `prereq` relationship (roles: `course_id` and `prereq_id`).

2. **Binary Relationship (Degree 2):**
   - Involves two distinct entity sets. This is the most common relationship type.
   - *Example:* `instructor` and `student` linked by the `advisor` relationship.

3. **Ternary Relationship (Degree 3):**
   - Involves three distinct entity sets simultaneously.
   - *Example:* `proj_guide` linking `instructor`, `student`, and `project`.

| Relationship Type | Degree | Description | Example |
| :--- | :---: | :--- | :--- |
| **Unary (Recursive)** | 1 | Association among entities of the same entity set | Course $\xrightarrow{\text{prereq}}$ Course |
| **Binary** | 2 | Association between two distinct entity sets | Instructor $\xrightarrow{\text{advisor}}$ Student |
| **Ternary** | 3 | Association among three distinct entity sets | Instructor, Student, Project $\xrightarrow{\text{proj\_guide}}$ |
| **$n$-ary** | $n$ | Association among $n$ entity sets | Rare; usually decomposed into binary |

---

## T02.2 · Attribute types

### 2020 Q.5(a) · 04 Marks

*Section B · Asked in: 2020 · L1 (asked once)*

**Question.** Differentiate between-  
(i) Simple and composite attribute  
(ii) Single-valued and multi-valued attribute

**Answer.**

**(i) Simple vs Composite Attribute:**

| Feature | Simple (Atomic) Attribute | Composite Attribute |
| :--- | :--- | :--- |
| **Definition** | Cannot be divided into smaller subparts. | Can be divided into smaller subparts that form independent attributes. |
| **Structure** | Holds a single atomic value from its domain. | Forms a hierarchy of component attributes. |
| **E-R Notation** | Single ellipse connected to the entity rectangle. | An ellipse connected to component ellipses. |
| **Storage / Schema** | Maps to a single column in a relational table. | Flattened into separate columns for each subpart. |
| **Example** | `salary`, `student_id`, `credits` | `name` (`first_name`, `last_name`), `address` (`street`, `city`, `zip_code`) |

**(ii) Single-Valued vs Multi-Valued Attribute:**

| Feature | Single-Valued Attribute | Multi-Valued Attribute |
| :--- | :--- | :--- |
| **Definition** | Holds at most one value for a specific entity instance. | Can hold a set of values for a single entity instance. |
| **Values per Entity** | Exactly one value per record. | Zero, one, or multiple values per record. |
| **E-R Notation** | Single ellipse. | Double ellipse (concentric ellipses). |
| **Table Conversion** | Stored directly in the main entity table. | Converted into a separate table with the entity primary key. |
| **Example** | `date_of_birth`, `roll_no`, `nid` | `phone_numbers`, `degrees`, `email_addresses` |

---

### 2021 Q.3(b) · 04 Marks

*Section A · CLO4 · Asked in: 2021 · L1 (asked once)*

**Question.** Define entity and attribute. Explain the following attributes-  
(i) Multi-valued  
(ii) Derived  
(iii) Composite

**Answer.**

- **Entity:** A "thing" or "object" in the real world that exists and is distinguishable from other objects (e.g., a specific instructor `ID = 22222`, or a student).
- **Attribute:** A descriptive property possessed by all members of an entity set (e.g., `name`, `salary`).

**Explanation of Attribute Types:**

1. **Multi-valued Attribute:**
   - Holds a set of multiple values for a single entity instance.
   - Depicted by a **double ellipse** in Chen notation.
   - *Example:* An instructor may have multiple phone numbers (`phone_numbers` = `{0171..., 0181...}`).

2. **Derived Attribute:**
   - The value is not stored directly. It is computed from stored attributes or system values.
   - Depicted by a **dashed ellipse** in Chen notation.
   - *Example:* `age` derived from current date minus `date_of_birth`.

3. **Composite Attribute:**
   - Can be divided into smaller component attributes with independent meanings.
   - Depicted by an ellipse with attached branches leading to sub-ellipses.
   - *Example:* `name` divided into `first_name`, `middle_initial`, and `last_name`.

![Representing complex attributes in ER diagram: composite name and address, multivalued phone_number, and derived age](../LectureSlides/diagrams/L05_p19_fig01.jpg)
*Figure: Complex Attributes in ER Diagram Notation (Deck 05, Slide 19)*

---

## T02.3 · Mapping cardinality and participation constraints

### 2018 Q.3(c) · 04 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** What is mapping cardinality? How a many to many relationship can be converted into table. Explain with example.

**Answer.**

**Mapping Cardinality:**  
Mapping cardinality (or cardinality ratio) expresses the number of entities to which another entity can be associated via a relationship set. For binary relationships, it must be 1:1, 1:N, N:1, or M:N.

**Conversion of a Many-to-Many (M:N) Relationship into a Table:**
1. Create a dedicated relation schema for the relationship set.
2. Include the primary key of each participating entity set as foreign keys in this new table.
3. Include any descriptive attributes associated with the relationship set.
4. The composite primary key of the new table is formed by the union of the primary keys of both participating entity sets.

![Many to many relationship between Student and Course with descriptive attribute grade and reduction to tables](diagrams/T02_2018_Q3c_many_to_many_er.jpg)
*Figure: Many-to-Many Relationship Model and Reduction to Relational Table*

**Example:**
- Entity `STUDENT` with attributes `student_id` (PK), `name`.
- Entity `COURSE` with attributes `course_id` (PK), `title`.
- Relationship `Takes` (M:N) with descriptive attribute `grade`.

**Relational Schemas:**

**student**(**student_id**, name)  
`PK: student_id`

**course**(**course_id**, title)  
`PK: course_id`

**takes**(**student_id**, **course_id**, grade)  
`PK: (student_id, course_id)`  
`FK: student_id references student(student_id), course_id references course(course_id)`

---

### 2020 Q.1(c) · 04 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** What is mapping cardinalities? Define different types of cardinalities.

**Answer.**

**Mapping Cardinality:**  
Mapping cardinality specifies how many entities from one entity set can be associated with entities from another entity set through a binary relationship set.

**Types of Mapping Cardinalities:**

1. **One-to-One (1:1):**
   - An entity in $A$ is associated with at most one entity in $B$, and an entity in $B$ is associated with at most one entity in $A$.
   - *Example:* A department has at most one head (`dept_head`).

2. **One-to-Many (1:N):**
   - An entity in $A$ is associated with any number (0 or more) of entities in $B$. An entity in $B$ is associated with at most one entity in $A$.
   - *Example:* An instructor advises many students, but each student has at most one advisor.

3. **Many-to-One (N:1):**
   - An entity in $A$ is associated with at most one entity in $B$. An entity in $B$ is associated with any number of entities in $A$.
   - *Example:* Many students belong to one department.

4. **Many-to-Many (M:N):**
   - An entity in $A$ is associated with any number of entities in $B$, and an entity in $B$ is associated with any number of entities in $A$.
   - *Example:* A student can register for multiple courses, and a course can contain multiple students.

*See also:* [[#2018 Q.1(c) · 05 Marks]] (tests participation constraints) and [[#CT-02 Q.02 · 10 Marks]] (identifies entities, keys, relationships, and cardinalities).

---

## T02.4 · Weak vs strong entity sets

### 2018 Q.1(b) · 04 Marks

*Section A · Asked in: 2018, 2020, 2021 (CLO1) · L2 merge*

**Question (2018 Q.1(b)).** Define entity set. Explain the following with suitable example: (i) strong entity set and (ii) weak entity set.

**Question (2020 Q.2(c)).** Explain the difference between a weak and a strong entity set with appropriate example.

**Question (2021 Q.8(c)).** Explain weak and strong entity set with appropriate example.

**Answer.**

**Entity Set:**  
An entity set is a collection of entities of the same type that share the same properties or attributes (e.g., the set of all students in a university).

| Feature | Strong Entity Set | Weak Entity Set |
| :--- | :--- | :--- |
| **Primary Key** | Has sufficient attributes to form its own primary key. | Lacks a primary key of its own. Uses a partial key (discriminator). |
| **Existence Dependency** | Independent. Does not depend on another entity set. | Existence-dependent on an identifying (strong) entity set. |
| **E-R Notation** | Single rectangle. | Double rectangle. |
| **Relationship Set** | Connected via regular relationship (single diamond). | Connected via identifying relationship (double diamond). |
| **Discriminator Key** | None (uses full primary key underlined with solid line). | Has a discriminator underlined with a dashed line. |
| **Composite PK** | Its own primary key. | Formed by (Owner Primary Key + Discriminator). |
| **Example** | `course` with primary key `course_id`. | `section` with discriminator `sec_id`, `semester`, `year`. |

![Weak entity set section connected to identifying strong entity set course via sec_course](../LectureSlides/diagrams/L05_p37_fig01.jpg)
*Figure: Expressing Weak Entity Sets in ER Diagram (Deck 05, Slide 37)*

- **Strong Entity Set Example:** `course` has attributes `course_id` (PK), `title`, `credits`. It exists independently.
- **Weak Entity Set Example:** `section` has attributes `sec_id`, `semester`, `year`. A section number like `Sec 1` is meaningless without knowing the course. Its full primary key is `(course_id, sec_id, semester, year)`.

*Short version for 2020 Q.2(c) and 2021 Q.8(c) (2 marks):*  
State the comparison table rows (Primary Key, Dependency, Notation, Example) and omit the separate entity set definition.

---

### 2019 Q.1(b) · 03 Marks

*Section A · Asked in: 2019 · L1 (asked once)*

**Question.** What are entity and entity set? How is a weak entity set handled in DBMS? Explain.

**Answer.**

- **Entity:** An object that exists in the real world and is distinguishable from other objects.
- **Entity Set:** A collection of entities of the same type sharing the same attributes.

**Handling a Weak Entity Set in DBMS:**
1. **Primary Key Formation:** The DBMS cannot identify weak entity tuples by local attributes alone. It combines the primary key of the identifying strong entity with the weak entity's discriminator (partial key).
   $$\text{PK}(\text{Weak}) = \text{PK}(\text{Identifying Entity}) \cup \text{Discriminator}$$
2. **Table Schema Reduction:** A dedicated table is created for the weak entity. It includes the identifying entity's primary key as a foreign key along with all weak entity attributes. The identifying relationship does not need a separate table.
3. **Foreign Key Integrity with Cascade:** The identifying foreign key is declared with `ON DELETE CASCADE`. If the owner entity tuple is deleted, all dependent weak entity tuples are automatically removed.

---

## T02.5 · Design a full E-R diagram for a scenario

### 2017 Q.1(b) · 06 Marks

*Section A · Asked in: 2017, 2024 (CO3) · L2 merge*

**Question (2017 Q.1(b)).** Draw an E-R diagram for RUET student database which can be used to store student's basic information, course advisor's information, subject registration, result information.

**Question (2024 Q.1(b)).** Draw an E-R diagram for RUET student database which can be used to store student’s basic information, course advisor’s information, subject registration, result information.

**Answer.**

**Design Specifications:**
1. **STUDENT:** Basic information entity with primary key `roll_no`. Attributes: `name`, `dept_name`, `series`.
2. **ADVISOR:** Faculty advisor entity with primary key `advisor_id`. Attributes: `name`, `designation`, `department`.
3. **COURSE (SUBJECT):** Academic course entity with primary key `course_code`. Attributes: `course_title`, `credits`.
4. **RESULT:** Semester examination outcome entity with primary key `result_id`. Attributes: `semester`, `gpa`, `cgpa`.

**Relationships:**
- `Advises` (1:N): An advisor guides multiple students. Each student has one advisor (total participation of student).
- `Registers` (M:N): Students register for multiple courses, and courses have many students. Descriptive attributes: `session`, `semester`.
- `Obtains` (1:N): Each student obtains multiple semester results (total participation of result).

![Conceptual ER diagram for RUET Student Database with Advisor, Student, Course, and Result](diagrams/T02_2017_Q1b_ruet_student_er.jpg)
*Figure: RUET Student Database Conceptual E-R Diagram*

*Short version for 2024 Q.1(b) (2 marks):*  
Draw the 4 entity rectangles (`STUDENT`, `ADVISOR`, `COURSE`, `RESULT`) and 3 relationship diamonds (`Advises`, `Registers`, `Obtains`) with primary keys underlined (`roll_no`, `advisor_id`, `course_code`, `result_id`) and cardinality labels (1:N, M:N, 1:N). Omit secondary descriptive attributes to complete within 2 marks.

---

### 2018 Q.1(c) · 05 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** What is E-R model? Draw an E-R diagram that includes teacher, student and course entities with following constraints: (i) Each teacher must take at least one course; (ii) A student can register one or more courses; (iii) A course may have teacher or not.

**Answer.**

**E-R Model:**  
The Entity-Relationship (E-R) model is a high-level conceptual data model. It views the real-world enterprise as a collection of basic objects called entities and relationships among these objects.

**Constraints Mapping in E-R Diagram:**
- *(i) Each teacher must take at least one course:*  
  **Total participation** of `TEACHER` in relationship `Teaches`, represented by a **double line** from `TEACHER` to `Teaches` (cardinality $1..\text{*}$).
- *(ii) A student can register one or more courses:*  
  **Total participation** of `STUDENT` in relationship `Registers`, represented by a **double line** from `STUDENT` to `Registers` (cardinality $1..\text{*}$, M:N relationship).
- *(iii) A course may have teacher or not:*  
  **Partial participation** of `COURSE` in relationship `Teaches`, represented by a **single line** from `COURSE` to `Teaches` (cardinality $0..1$ or $0..\text{*}$).

![Teacher Student Course ER diagram with participation constraints](diagrams/T02_2018_Q1c_teacher_student_course_er.jpg)
*Figure: E-R Diagram with Total and Partial Participation Constraints*

---

### 2019 Q.1(c) · 06 Marks

*Section A · Asked in: 2019 · L1 (asked once)*

**Question.** Suppose you are recruited as a database specialist by the Rajshahi High-Tech authority to help them design a database for train e-ticketing system efficiently. Now think the regular features and draw an E-R diagram accordingly.

**Answer.**

**System Requirements & Entities:**
1. **PASSENGER:** Stores account details. Attributes: `user_id` (PK), `name`, `nid`, `phone`.
2. **TICKET:** Represents booked travel tickets. Attributes: `ticket_no` (PK), `journey_date`, `seat_no`, `fare`, `class`.
3. **TRAIN:** Represents trains. Attributes: `train_no` (PK), `train_name`, `total_seats`.
4. **STATION:** Represents railway stops. Attributes: `station_code` (PK), `station_name`, `city`.

**Relationships:**
- `Books` (1:N): A passenger books one or more tickets. Each ticket is booked by one passenger (descriptive attribute: `booking_date`).
- `For_Train` (N:1): Many tickets belong to a specific train. Each ticket is assigned to exactly one train.
- `Stops_At` (M:N): Trains stop at multiple stations, and stations service multiple trains. Descriptive attributes: `arrival_time`, `dep_time`.

![Train E Ticketing ER diagram for Rajshahi High Tech Authority](diagrams/T02_2019_Q1c_train_eticketing_er.jpg)
*Figure: Train E-Ticketing System E-R Diagram*

---

### 2023 Q.1(a) · 05 Marks

*Section A · CLO4 · Asked in: 2023 · L1 (asked once)*

**Question.** Draw an ER diagram for RUET Central Library Management System. You have to consider the entities mentioned below:  
(i) Books (ii) Members (iii) Staff (iv) Borrowing (v) Reservations

**Answer.**

*Design Note: Borrowing and Reservations are explicitly specified as entity sets in the prompt; each is modeled with its own unique identifier and transaction attributes.*

**Entity Sets & Attributes:**
1. **BOOKS:** `book_id` (PK), `isbn`, `title`, `author`, `edition`.
2. **MEMBERS:** `member_id` (PK), `name`, `type`, `department`.
3. **STAFF:** `staff_id` (PK), `name`, `designation`.
4. **BORROWING:** `borrow_id` (PK), `borrow_date`, `due_date`, `return_date`.
5. **RESERVATIONS:** `res_id` (PK), `res_date`, `status`.

**Relationships:**
- `Issues` (1:N): A staff member processes multiple borrowings.
- `Borrows` (1:N): A member initiates multiple borrowings.
- `Includes` (N:1): A borrowing record links to the specific book borrowed.
- `Reserves` (1:N): A member makes multiple book reservations.
- `For_Book` (N:1): A reservation is placed for a specific book.

![RUET Central Library Management System ER diagram with Borrowing and Reservations as Entities](diagrams/T02_2023_Q1a_ruet_library_er.jpg)
*Figure: RUET Central Library Management System E-R Diagram*

---

### CT-02 Q.02 · 10 Marks

*CO3 · Asked in: CT-02 · L1 (asked once)*

**Question.** A university maintains information about Students, Courses, and Teachers. A student can enroll in several courses and each course can have many students. Each course is taught by one teacher, though a teacher may teach several courses.  
**(a)** Identify the entities, attributes, primary keys, relationships, and cardinalities. `[04 Marks]`  
**(b)** Draw the complete ER diagram. `[06 Marks]`

**Answer.**

**(a) Identification of Components:**

| Component | Type | Details | Primary Key |
| :--- | :--- | :--- | :--- |
| **STUDENT** | Entity Set | Attributes: `student_id`, `name`, `email`, `dept_name` | `student_id` |
| **COURSE** | Entity Set | Attributes: `course_id`, `title`, `credits` | `course_id` |
| **TEACHER** | Entity Set | Attributes: `teacher_id`, `name`, `dept_name`, `phone` | `teacher_id` |
| **Enrolls** | Relationship Set | Connects `STUDENT` and `COURSE` | `(student_id, course_id)` |
| **Teaches** | Relationship Set | Connects `TEACHER` and `COURSE` | `course_id` |

**Cardinalities:**
- **Student to Course (`Enrolls`):** Many-to-Many (**M:N**). A student enrolls in several courses; each course has many students.
- **Teacher to Course (`Teaches`):** One-to-Many (**1:N**). A teacher teaches several courses; each course is taught by exactly one teacher.

**(b) Complete E-R Diagram:**

![University Enterprise ER diagram for CT-02 Q.02](diagrams/T02_CT02_Q02_university_er.jpg)
*Figure: University Enterprise Complete E-R Diagram*

---

## T02.6 · Reduction of E-R to relational tables

### 2018 Q.2(c) · 05 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** Consider a database used to record the marks that students get in different examinations of different course offerings. (i) Construct an E-R diagram that models examinations as entities, and uses a ternary relationship for the above database; (ii) Draw a relational data model for the above corresponding E-R diagram.

**Answer.**

**(i) E-R Diagram with Ternary Relationship:**
- Participating Entity Sets: `STUDENT`, `COURSE_OFFERING`, `EXAM`.
- Ternary Relationship: `Scores` connecting all three entity sets.
- Relationship Attribute: `marks` (descriptive attribute placed on `Scores`).

![Ternary relationship diagram for student marks in examinations of course offerings](diagrams/T02_2018_Q2c_ternary_exam_er.jpg)
*Figure: Ternary Relationship Model for Student Exam Marks*

**(ii) Relational Data Model (Relational Schemas):**

**student**(**student_id**, name, dept_name)  
`PK: student_id`

**course_offering**(**offering_id**, semester, year)  
`PK: offering_id`

**exam**(**exam_id**, exam_type, max_marks)  
`PK: exam_id`

**scores**(**student_id**, **offering_id**, **exam_id**, marks)  
`PK: (student_id, offering_id, exam_id)`  
`FK: student_id references student(student_id), offering_id references course_offering(offering_id), exam_id references exam(exam_id)`

*See also:* [[#2018 Q.3(c) · 04 Marks]] (conversion of M:N relationships into relational tables).

---

## T02.7 · EER: specialization / generalization

### 2017 Q.6(a) · 02 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** Write short note on specialization and generalization in DBMS.

**Answer.**

- **Specialization (Top-down):**  
  A top-down design process. A higher-level entity set is divided into lower-level entity sets that have distinctive attributes or participate in specific relationships.
  - *Example:* `person` specialized into `employee` and `student`.

- **Generalization (Bottom-up):**  
  A bottom-up design process. Multiple lower-level entity sets sharing common properties are synthesized into a single higher-level entity set.
  - *Example:* Combining `instructor` and `secretary` into `employee`.

- **Key Properties:**
  1. **Attribute Inheritance:** Lower-level entity sets automatically inherit all attributes and relationship participations of the higher-level entity.
  2. **Representation:** Depicted in E-R diagrams by a triangle labeled **ISA** ("is a").

![Specialization hierarchy with higher-level entity person specialized into employee and student](../LectureSlides/diagrams/L05_p51_fig01.jpg)
*Figure: Specialization Hierarchy Example (Deck 05, Slide 51)*

---

## T02.8 · EER: aggregation

### 2018 Q.2(b) · 03 Marks

*Section A · Asked in: 2018, 2020 · L2 merge*

**Question (2018 Q.2(b)).** Define the concept of aggregation. Give two examples of where this concept is useful.

**Question (2020 Q.3(a)).** What is aggregation in ER-model design?

**Answer.**

**Definition:**  
Aggregation is an abstraction in E-R modeling through which a relationship set is treated as a higher-level abstract entity set. This allows the relationship itself to participate in further relationships with other entity sets without duplicating attributes.

![Aggregation representation in ER diagram showing relationship treated as higher-level entity](../LectureSlides/diagrams/L05_p59_fig01.jpg)
*Figure: Aggregation Representation in E-R Diagram (Deck 05, Slide 59)*

**Two Examples Where Aggregation is Useful:**

1. **Student Project Evaluation:**  
   The ternary relationship `proj_guide` associates `student`, `instructor`, and `project`. To record an `evaluation` for that specific guidance assignment, treating `proj_guide` as an aggregate entity avoids creating an overlapping ternary relationship. `evaluation` links directly to the aggregate `proj_guide` through the relationship `eval_for`.

2. **Employee Project Monitoring:**  
   Employees work on projects via the relationship `Works_On`. A manager needs to monitor that specific work assignment. By aggregating `Works_On` into an entity, the `manager` can participate in a relationship `Monitors` directly with the aggregate entity `(Employee, Project)`.

*Short version for 2020 Q.3(a) (2 marks):*  
Give the definition of aggregation and describe Example 1 (`proj_guide` with `eval_for`) in 2 lines.

---

[← Prev: T01 · DB Concepts and Architecture](T01_DB_Concepts_and_Architecture.md) | [Explanation layer](../Topicwise_answers_explaination/T02_ER_and_EER_Modeling.md) | [Next: T03 · Relational Model, Keys & Integrity →](T03_Relational_Model_Keys_and_Integrity.md)
