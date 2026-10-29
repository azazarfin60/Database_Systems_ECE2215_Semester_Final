# ECE 2215: Database Systems — Master Lecture Slide Index

- **Course:** ECE 2215 — Data Base Systems
- **Credit:** 3.00
- **Institution:** Rajshahi University of Engineering & Technology (RUET)
- **Instructors:** Mst. Nafia Islam Shishir & Md. Rakibul Islam
- **Total Modules:** 8 Digitized Lecture Decks (371 slides total)
- **Quality Assurance Audit:** [`QA_Verification_Report.md`](../Bin/reports/LectureSlides/QA_Verification_Report.md) (**100% Certified PASS**)

---

## 1. Master Slide Decks Matrix

| Module | Document | Slides | Figures | Core Topics Covered | Syllabus Unit |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **01** | [`01_Intro_to_Database_and_DBMS.md`](01_Intro_to_Database_and_DBMS.md) | 33 | 9 | DBMS concepts, File systems vs. DBMS, 3-tier abstraction levels, Data independence, Storage manager, Query processor architecture | Unit 1: Concepts of Database Systems |
| **02** | [`02_Relational_Model.md`](02_Relational_Model.md) | 34 | 9 | Relation schemas, Tuples, Attributes, Keys (Super, Candidate, Primary, Foreign), Relational algebra ($\sigma, \Pi, \times, \bowtie, \rho, \cup, -, \cap, \gamma$) | Unit 3: Relational Model & Relational Algebra |
| **03** | [`03_Introduction_to_SQL.md`](03_Introduction_to_SQL.md) | 62 | 2 | DDL (`create`, `alter`), DML (`select-from-where`), Aggregates (`group by`, `having`), Nested subqueries (`in`, `some`, `all`, `exists`), Modifications (`insert`, `update`, `delete`, `case`) | Unit 4: Structured Query Language (SQL) |
| **04** | [`04_Joining_and_Views.md`](04_Joining_and_Views.md) | 35 | 11 | Natural join, Outer joins (Left $\mathbin{⟕}$, Right $\mathbin{⟖}$, Full $\mathbin{⟗}$), Join conditions (`on`, `using`), Views creation, Virtual relations, View updates, Integrity constraints | Unit 4: SQL & Relational Algebra (Joins & Views) |
| **05** | [`05_ER_Model.md`](05_ER_Model.md) | 80 | 40 | Entity sets, Attributes (composite, multivalued, derived), Keys, Mapping cardinalities, Weak entity sets, Extended ER (Specialization, Generalization, Aggregation), ER to Relational schema reduction | Unit 2: Entity-Relationship (ER) Concepts & Modeling |
| **06** | [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md) | 63 | 0 | Design pitfalls & anomalies, Keys, Functional Dependencies (FDs), Armstrong's Axioms, Attribute closure $X^+$ & candidate keys, 1NF, 2NF, 3NF, BCNF, Denormalization, Lossless decomposition, Dependency preservation | Unit 5: Relational Database Design & Normalization |
| **07** | [`07_Transactions.md`](07_Transactions.md) | 33 | 16 | Transaction concept, ACID properties, Transaction states, Concurrent schedules, Conflict serializability, Precedence graphs, Topological sorting, Concurrency anomalies (Dirty Read, Lost Update, Phantom Read) | Unit 6: Transaction Management |
| **08** | [`08_Concurrency_Control_Mechanisms.md`](08_Concurrency_Control_Mechanisms.md) | 31 | 15 | Schedule recoverability hierarchy (Recoverable, Cascadeless, Strict), Lock-based protocols (Shared/Exclusive, 2PL, Strict 2PL, Rigorous 2PL), Deadlock handling (wait-for graphs), Timestamp Ordering (TSO) protocol | Unit 6: Concurrency Control Protocols |
| **TOTAL** | **8 Modules** | **371** | **102** | **Complete Lecture Slide Coverage** | **All Core Units** |

---

## 2. RUET Syllabus & Learning Objectives Mapping

### Unit 1: Concepts of Database Systems
- **Slide Reference:** [`01_Intro_to_Database_and_DBMS.md`](01_Intro_to_Database_and_DBMS.md)
- **Key Concepts:**
  - File systems vs. Database systems: Data redundancy, inconsistency, isolation, and integrity problems (Slides 6–7); DBMS Users & DBA functions (Slides 8–10).
  - Levels of Data Abstraction & Schemas: Physical, Logical, and View levels (Slides 13–14); Instances and Schemas (Slide 15). *(Physical/Logical Data Independence: `Textbook Ch. 01` §1.3.1).*
  - Database Languages: DDL (Slides 16–17), DML (Slide 18), and DQL (Slide 19).
  - DBMS Component Architecture: Storage Manager (Slide 23), Query Processor (Slides 24–25), and Transaction Management (Slide 26).
  - Database Architectures: Centralized/Shared-Memory (Slides 27–28) and Client-Server 2-tier and 3-tier Application Architectures (Slides 29–32).

### Unit 2: Entity-Relationship (ER) Concepts & Modeling
- **Slide Reference:** [`05_ER_Model.md`](05_ER_Model.md)
- **Key Concepts:**
  - Entities, Entity Sets, Relationship Sets, and Attribute Classifications: Simple, composite, single-valued, multi-valued, and derived (Slides 7–19).
  - Relationships & Mapping Cardinalities: One-to-one (1:1), One-to-many (1:N), Many-to-one (N:1), Many-to-many (N:M), total vs. partial participation, and ternary cardinality (Slides 20–29).
  - Keys & Weak Entity Sets: Primary keys (Slides 30–33), weak entity sets, identifying relationships, and discriminators / partial keys (Slides 34–37, 42).
  - Schema Reduction: Converting strong entity sets, weak entity sets, relationships, and composite/multivalued attributes into relational tables (Slides 40–48).
  - Extended ER (EER): Specialization (top-down), Generalization (bottom-up), Completeness constraints, Aggregation, and EER schema reduction (Slides 49–60).

### Unit 3: Relational Model & Relational Algebra
- **Slide Reference:** [`02_Relational_Model.md`](02_Relational_Model.md)
- **Key Concepts:**
  - Relational Structure: Attributes, tuples, domains, schemas, and instances (Slides 3–5).
  - Keys & Schema Diagrams: Superkey, Candidate key, Primary key, Foreign key, and University Schema Diagram (Slides 6–8).
  - Fundamental Relational Algebra Operations: Select ($\sigma$, Slides 11–12), Project ($\Pi$, Slides 13–14), Composition (Slide 15), Cartesian Product ($\times$, Slides 16–17), Join ($\bowtie$, Slides 18–19), Union ($\cup$, Slides 20–22), Set Intersection ($\cap$, Slide 23), Set Difference ($-$, Slide 24), Assignment ($\leftarrow$, Slide 25), and Rename ($\rho$, Slide 26).
  - Extended Relational Algebra & Design Pitfalls: Aggregate functions and grouping ($_{G}\gamma_{F}$, Slides 27–29), equivalent queries (Slides 30–31), and pitfalls in relational database design (Slides 32–33).

### Unit 4: Structured Query Language (SQL) & Advanced Operations
- **Slide References:** [`03_Introduction_to_SQL.md`](03_Introduction_to_SQL.md) & [`04_Joining_and_Views.md`](04_Joining_and_Views.md)
- **Key Concepts:**
  - Data Definition Language (DDL): `create table`, domain types, primary key, foreign key, `not null` constraints, `drop`/`alter table` (Deck 03, Slides 5–11).
  - Data Manipulation Language (DML): `select`, `from`, `where`, `rename`, string pattern matching (`like`), `order by`, set operations (`union`, `intersect`, `except`), and `null` values (Deck 03, Slides 12–29).
  - Aggregate Functions & Grouping: `avg`, `min`, `max`, `sum`, `count`, `group by`, and `having` (Deck 03, Slides 30–34).
  - Nested Subqueries: Set membership (`in`, `not in`), set comparison (`some`, `all`), empty relation tests (`exists`, `not exists`), duplicate tests (`unique`), `from` subqueries, `with` clause, and scalar subqueries (Deck 03, Slides 35–52).
  - Database Modifications: `delete`, `insert`, `update`, and `case` statements (Deck 03, Slides 53–61).
  - Join Variations: Inner join, Left Outer Join ($\mathbin{⟕}$), Right Outer Join ($\mathbin{⟖}$), Full Outer Join ($\mathbin{⟗}$), Cross Join, Natural Join, and join result examples (Deck 04, Slides 3–23).
  - Views: View definition (`create view`), views defined using other views, view expansion, materialized views, and update of views (Deck 04, Slides 24–34).

### Unit 5: Relational Database Design & Normalization
- **Slide Reference:** [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md)
- **Key Concepts:**
  - Pitfalls in Relational Design: Row/column duplication, update anomalies, insertion anomalies, deletion anomalies (Slides 3–10).
  - Keys & Functional Dependencies (FD): Super, Candidate, Primary, Alternate, Composite, and Foreign keys (Slides 11–13); trivial, non-trivial, full, partial, and transitive FDs; Prime vs. Non-prime attributes (Slides 14–17).
  - Properties of FDs: Armstrong's Axioms (Reflexivity, Augmentation, Transitivity) and secondary rules (Union, Decomposition, Pseudotransitivity) (Slides 18–24).
  - Attribute Closure ($X^+$) & Candidate Keys: Step-by-step closure and candidate-key drills (Slides 25–29). *(Note: Canonical Cover $F_c$ is in `Textbook Ch. 07` §7.4.3, not in Deck 06).*
  - Normal Forms:
    - First Normal Form (1NF): Atomic domains (Slide 30).
    - Second Normal Form (2NF): Full functional dependency on candidate keys (Slides 31–36).
    - Third Normal Form (3NF): Elimination of transitive dependencies (Slides 37–40).
    - Boyce-Codd Normal Form (BCNF): Strict determinant conditions ($X$ must be a superkey), comparison table, and practice problem (Slides 41–46).
  - Denormalization & Decomposition Properties: Pros/cons of normalization and denormalization (Slides 47–51); lossless-join decomposition test ($R_1 \cap R_2 \rightarrow R_1$ or $R_1 \cap R_2 \rightarrow R_2$) and dependency preservation (Slides 52–62).

### Unit 6: Transaction Management & Concurrency Control
- **Slide References:** [`07_Transactions.md`](07_Transactions.md) & [`08_Concurrency_Control_Mechanisms.md`](08_Concurrency_Control_Mechanisms.md)
- **Key Concepts:**
  - Transaction Concept & ACID Properties: Atomicity, Consistency, Isolation, Durability with fund transfer example (Deck 07, Slides 3–7).
  - Transaction State Transitions: Active, Partially Committed, Committed, Failed, Aborted (Deck 07, Slides 8–9).
  - Concurrent Schedules: Serial schedules vs. concurrent executions (Deck 07, Slides 10–15).
  - Serializability: Conflicting instructions, conflict serializability, instruction swapping rules, view serializability, precedence graphs, cycle detection, and topological sorting (Deck 07, Slides 16–27).
  - Concurrency Anomalies: Dirty read, unrepeatable read, lost update, phantom read, incorrect summary problem (Deck 07, Slides 28–33).
  - Schedule Classification: Recoverable schedules, cascadeless schedules, strict schedules (Deck 08, Slides 3–8).
  - Lock-Based Protocols: Shared/Exclusive locks, lock compatibility matrix, starvation, Two-Phase Locking (2PL), 2PL drawbacks, Strict 2PL, Rigorous 2PL (Deck 08, Slides 9–19).
  - Deadlock Handling: Deadlock conditions, prevention (`wait-die`, `wound-wait`), detection using wait-for graphs, victim selection and rollback (Deck 08, Slides 20–25).
  - Timestamp-Based Protocols: System timestamps and Timestamp Ordering (TSO) protocol rules for reads and writes (Deck 08, Slides 26–30). *(Note: Thomas' write rule and the TSO rollback new-timestamp rule are in `Textbook Ch. 18` §18.5).*

---

## 3. Cross-Referencing: Previous Year Examination Questions

Students can map digitized lecture content directly to official semester final exam questions in [`/home/azaz/AntigravityxStudy/SemesterFinal_2_2/ECE_2215/PreviousYearQuestion/`](../PreviousYearQuestion/):

| Exam Year & Question | Question Description | Directly Mapped Slide Module |
| :--- | :--- | :--- |
| **2024 Q.1 (a)** | Courier tracking company: File system vs. DBMS decision and justification | [`01_Intro_to_Database_and_DBMS.md`](01_Intro_to_Database_and_DBMS.md#slide-6) |
| **2024 Q.1 (b)** | E-R diagram for RUET student database (basic info, advisor, registration, result) | [`05_ER_Model.md`](05_ER_Model.md#slide-39) |
| **2024 Q.1 (c)** | SQL aggregate query: Average grade for each course (`group by`) | [`03_Introduction_to_SQL.md`](03_Introduction_to_SQL.md#slide-32) |
| **2024 Q.2 (b)** | Relational algebra: Employees working on multiple projects | [`02_Relational_Model.md`](02_Relational_Model.md#slide-27) |
| **2024 Q.2 (c)** | Database consistency property with proper example | [`07_Transactions.md`](07_Transactions.md#slide-6) |
| **2024 Q.3 (a)** | Library database normalization: Redundancy, partial dependencies, and normalization procedure | [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md#slide-31) |
| **2024 Q.3 (b)** | DBMS failure modes, precautions, and recovery methods | [`01_Intro_to_Database_and_DBMS.md`](01_Intro_to_Database_and_DBMS.md#slide-23) & [`07_Transactions.md`](07_Transactions.md#slide-8) |
| **2024 Q.3 (c)** | Differentiate between Inner Join and Outer Join | [`04_Joining_and_Views.md`](04_Joining_and_Views.md#slide-4) |
| **2024 Q.4 (a)** | Relational tables join outcome: Natural, Left Outer, Right Outer, and Full Outer Joins | [`04_Joining_and_Views.md`](04_Joining_and_Views.md#slide-6) |
| **2024 Q.4 (b)** | SQL DDL & DML: Create student table, insert entry, alter schema, filter by dept | [`03_Introduction_to_SQL.md`](03_Introduction_to_SQL.md#slide-7) |
| **2024 Q.5 (a)** | Relational algebra queries: Patient medical symptom and Covid test queries | [`02_Relational_Model.md`](02_Relational_Model.md#slide-11) |
| **2023 Q.1 (a)** | E-R diagram for RUET Central Library Management System (Books, Members, Staff, Borrowing, Reservations) | [`05_ER_Model.md`](05_ER_Model.md#slide-39) |
| **2023 Q.1 (b)** | Advantages of DBMS over file processing system | [`01_Intro_to_Database_and_DBMS.md`](01_Intro_to_Database_and_DBMS.md#slide-6) |
| **2023 Q.2 (a)** | Step-by-step conversion of university student/course/instructor table to 3NF | [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md#slide-31) |
| **2023 Q.2 (b)** | Anomalies eliminated by normalization (insertion, deletion, and update anomalies) | [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md#slide-3) |
| **2023 Q.3 (a)** | SQL queries on Employee table (`CREATE`, `INSERT`, correlated subquery for > dept avg salary) | [`03_Introduction_to_SQL.md`](03_Introduction_to_SQL.md#slide-43) |
| **2023 Q.3 (b)** | Distinctions among Primary key, Candidate key, Super key, and Composite key | [`02_Relational_Model.md`](02_Relational_Model.md#slide-6) & [`06_DBMS_Normalization.md`](06_DBMS_Normalization.md#slide-11) |
| **2023 Q.4 (b)** | Importance of ACID properties of transactions with suitable example | [`07_Transactions.md`](07_Transactions.md#slide-3) |
| **2023 Q.8 (b)** | Conflict serializability test using precedence graph and all possible serialized schedules | [`07_Transactions.md`](07_Transactions.md#slide-25) |
| **2023 Q.8 (c)** | Schedule evaluation based on Timestamp Ordering (TSO) protocol | [`08_Concurrency_Control_Mechanisms.md`](08_Concurrency_Control_Mechanisms.md#slide-26) |
