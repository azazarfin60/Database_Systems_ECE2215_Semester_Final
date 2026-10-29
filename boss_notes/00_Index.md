# 📚 ECE 2215: Database Systems — Boss Notes Master Index

> **Course:** ECE 2215: Database Systems (3.00 Credits) | **Department:** ECE, RUET
> **Instructors:** Mst. Nafia Islam Shishir & Md. Rakibul Islam
> **Exam Format:** Modern OBE — 60 Marks (80 Printed Marks), 3 Hours · Answer 6 of 8 Questions (3 from Section A + 3 from Section B)
> **Dataset Synthesized:** 7 Semester Finals (`2017`–`2021`, `2023`–`2024`; 637 printed marks, 148 sub-questions) + 4 Class Tests (`CT-01`–`CT-04`; 80 marks, 26 parts) = **174 Exam Question Parts (717 Marks)**

[📖 Course README](README.md) | [📐 Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md) | [Start Reading: T01.1 →](T01.01_Data_DB_and_DBMS_Basics.md)

---

## 🎯 Priority Legend

Thresholds are calibrated directly against the 7 RUET semester-final papers (`637` printed marks):

- 🔴 **CRITICAL / MUST (5–7 Finals, $\ge 70\%$ of papers):** Guaranteed to appear on your exam script. Master every derivation, query pattern, and Golden Question.
- 🟠 **HIGH (3–4 Finals, $40\text{–}60\%$ of papers):** Core recurring exam modules. Appears in roughly every alternate paper or carries heavy marks under Modern OBE.
- 🟡 **MEDIUM (2 Finals, $\sim 30\%$ of papers):** Tested regularly as 3–6 mark sub-questions. Know the definitions and worked examples cold.
- 🟢 **LOW / OCCASIONAL (0–1 Finals, $< 15\%$ of papers):** Tested once in a final or only in a Class Test.
- ⭐ **UNASKED SLIDE / BLUEPRINT CANDIDATE:** Never asked in a past final, but explicitly taught in the lecture slides, tested in a Class Test, or highlighted in the instructors' exam blueprint (`suggestions.md`). Prime source for "fresh" OBE questions.

---

## 🗂️ Complete Topic & Subtopic Index (86 Boss Notes)

### Syllabus Overview by Topic (`T01`–`T13`)

| Topic ID | Topic Name | Syllabus Unit | Final Marks | Share | Finals | Priority | Exam Section |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **T01** | DB Concepts & Architecture | Unit 1 | 44 | 6.9% | 7/7 | 🔴 | Section A only (usually Q.1) |
| **T02** | E-R & EER Modeling | Unit 2 | 67 | 10.5% | 7/7 | 🔴 | Mostly Section A |
| **T03** | Relational Model, Keys & Integrity | Unit 3 | 28 | 4.4% | 5/7 | 🟡 | Mostly Section A |
| **T04** | Relational Algebra & Calculus | Unit 3 | 48 | 7.5% | 6/7 | 🟠 | Mostly Section A (Q.2) |
| **T05** | SQL (DDL, DML, Aggregates, Subqueries) | Unit 4 | **130** | **20.4%** | 7/7 | 🔴 | **Both Sections** (#1 Topic) |
| **T06** | Joins & Views | Unit 4 | 28 | 4.4% | 4/7 | 🟠 | Both (11.2% in 2023–24) |
| **T07** | Triggers & Stored Procedures | Unit 4 | 27 | 4.2% | 5/7 | 🟠 | Mostly Section B |
| **T08** | Normalization & Functional Dependencies | Unit 5 | **75** | **11.8%** | 7/7 | 🔴 | **Both Sections** (#2 Topic) |
| **T09** | Transactions, ACID & Anomalies | Unit 6 | 41 | 6.4% | 7/7 | 🔴 | Both Sections |
| **T10** | Serializability & Precedence Graphs | Unit 6 | 51 | 8.0% | 7/7 | 🔴 | Mostly Section B |
| **T11** | Concurrency Control Protocols | Unit 6 | 37 | 5.8% | 6/7 | 🟠 | Section B only |
| **T12** | Recovery System & RAID | Unit 7 | 43 | 6.8% | 5/7 | 🟠 | Mostly Section B (13.1% in 2023–24) |
| **T13** | Security, Indexing & Hashing | Unit 8 | 18 | 2.8% | 4/7 | 🟢 | Mostly Section B |

---

### Unit 1 · T01: Database Concepts & Architecture (44 Marks · 6.9% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01 | [T01.1: Data, DB, and DBMS Basics](T01.01_Data_DB_and_DBMS_Basics.md) | `T01.1` | 🟢 ⭐ | 0/7 | — | Data vs. information, structured vs. unstructured data, DBMS applications |
| 02 | [T01.2: File System vs. DBMS](T01.02_File_System_vs_DBMS.md) | `T01.2` | 🔴 | 5/7 | 21 | 8 disadvantages of file processing, courier scenario (2024 Q1a) |
| 03 | [T01.3: DBA Functions and Relation Schema](T01.03_DBA_Functions_and_Relation_Schema.md) | `T01.3` | 🟠 | 3/7 | 10 | 5 core functions of a DBA, formal relation schema vs. table |
| 04 | [T01.4: Data Abstraction, Schemas, and Instances](T01.04_Data_Abstraction_Schemas_Instances.md) | `T01.4` | 🟡 | 2/7 + CT-01 | 8 (+5) | Physical/logical/view levels, physical data independence |
| 05 | [T01.5: DDL vs. DML](T01.05_DDL_vs_DML.md) | `T01.5` | 🟢 | 1/7 | 2 | Procedural vs. declarative DML, data dictionary metadata |
| 06 | [T01.6: DBMS Engine Components](T01.06_DBMS_Engine_Components.md) | `T01.6` | 🟢 ⭐ | 0/7 | — | Storage Manager (4 modules), Query Processor (3 modules) |
| 07 | [T01.7: Two-Tier vs. Three-Tier Architecture](T01.07_Two_Tier_vs_Three_Tier_Architecture.md) | `T01.7` | 🟢 | 1/7 + CT-01 | 3 (+5) | Client/server ODBC/JDBC vs. application server three-tier |

---

### Unit 2 · T02: E-R and EER Modeling (67 Marks · 10.5% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 08 | [T02.1: Entities, Relationships, and Degree](T02.01_Entities_Relationships_and_Degree.md) | `T02.1` | 🟢 | 1/7 | 4 | Entity sets, relationship sets, descriptive attributes, unary/binary/ternary degree |
| 09 | [T02.2: Attribute Types](T02.02_Attribute_Types.md) | `T02.2` | 🟡 | 2/7 | 8 | Simple vs. composite, single-valued vs. multivalued, derived attributes |
| 10 | [T02.3: Mapping Cardinality and Participation Constraints](T02.03_Mapping_Cardinality_and_Participation.md) | `T02.3` | 🟡 | 2/7 | 8 | 1:1, 1:N, N:1, M:N arrow rules, total (double line) vs. partial participation |
| 11 | [T02.4: Weak vs. Strong Entity Sets](T02.04_Weak_vs_Strong_Entity_Sets.md) | `T02.4` | 🟠 | 4/7 | 11 | Discriminator (dashed underline), identifying relationship, composite PK |
| 12 | [T02.5a: E-R Design Method — Student & Teacher-Course DBs](T02.05a_ER_Design_Method_Student_and_Teacher_Course.md) | `T02.5` | 🔴 | 5/7 + CT-02 | 24 (+10) | 5-step design recipe, RUET Student DB (2017 Q1b = 2024 Q1b), 2018 Q1c |
| 13 | [T02.5b: E-R Design — Ticketing, Library, and University](T02.05b_ER_Design_Ticketing_Library_University.md) | `T02.5` | 🔴 | 5/7 + CT-02 | (in 24) | Train E-Ticketing (2019 Q1c), RUET Library (2023 Q1a), CT-02 Q2 |
| 14 | [T02.6: Reduction of E-R Diagrams to Relational Tables](T02.06_Reduction_of_ER_to_Tables.md) | `T02.6` | 🟢 | 1/7 | 5 | Strong/weak entities, M:N junction tables, ternary PK reduction (2018 Q2c) |
| 15 | [T02.7: EER Specialization and Generalization](T02.07_EER_Specialization_Generalization.md) | `T02.7` | 🟢 | 1/7 | 2 | Top-down vs. bottom-up ISA hierarchies, disjoint/overlapping constraints |
| 16 | [T02.8: EER Aggregation](T02.08_EER_Aggregation.md) | `T02.8` | 🟡 | 2/7 | 5 | Abstracting a relationship set into a higher-level entity set (`proj_guide` + `eval_for`) |

---

### Unit 3 · T03: Relational Model, Keys & Integrity (28 Marks · 4.4% · 5/7 Finals · 🟡)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 17 | [T03.1: Relation, Tuple, Attribute, and Domain](T03.01_Relation_Tuple_Domain.md) | `T03.1` | 🟢 | 1/7 | 2 | Formal relational terminology, domain vs. data type (2018 Q3b) |
| 18 | [T03.2: Relational Keys](T03.02_Keys.md) | `T03.2` | 🔴 | 5/7 | 21 | Superkey, candidate key, primary key, alternate key, composite key, foreign key |
| 19 | [T03.3: Referential Integrity and Foreign Key Syntax](T03.03_Referential_Integrity_and_Foreign_Keys.md) | `T03.3` | 🟢 | 1/7 | 5 | Referential integrity $\Pi_\alpha(r_2) \subseteq \Pi_K(r_1)$, MySQL `FOREIGN KEY` DDL (2021 Q1c) |
| 20 | [T03.4: Schema Diagrams](T03.04_Schema_Diagrams.md) | `T03.4` | 🟢 ⭐ | 0/7 + CT-01 | 0 (+5) | Drawing relational schema boxes with underlined PKs and FK arrows (CT-01 Q2) |

---

### Unit 3 · T04: Relational Algebra & Calculus (48 Marks · 7.5% · 6/7 Finals · 🟠)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 21 | [T04.1: Basic Relational Algebra Operators](T04.01_Basic_RA_Operators.md) | `T04.1` | 🟢 ⭐ | 0/7 | — | $\sigma, \Pi, \cup, -, \times, \rho$ plus $\cap, \bowtie, \leftarrow$ and arity/domain compatibility |
| 22 | [T04.2a: RA Queries — Employee, Insurance, and RA Updates](T04.02a_RA_Queries_Employee_and_Insurance.md) | `T04.2` | 🔴 | 6/7 + CT-01 | 41 (+4) | RA query recipe, 6e-style updates $r \leftarrow \Pi_{\dots}(r)$, 2017 Q2a, 2018 Q3a |
| 23 | [T04.2b: RA Queries — Covid and Vaccine Schemas](T04.02b_RA_Queries_Covid_and_Vaccine.md) | `T04.2` | 🔴 | 6/7 + CT-01 | (in 41) | Covid schema (2019 Q2b = 2024 Q5a), "1st dose only" set difference (2020 Q2a) |
| 24 | [T04.2c: RA Queries — Orders, Projects, and CT Drills](T04.02c_RA_Queries_Orders_Projects_CT.md) | `T04.2` | 🔴 | 6/7 + CT-01 | (in 41) | Customer/Orders (2021 Q2a), Project count $>4$ (2024 Q2b), CT-01 Q4 |
| 25 | [T04.3: Explaining RA Expressions in Words](T04.03_Explaining_RA_Expressions.md) | `T04.3` | 🟢 | 1/7 + CT-01 | 4 (+2) | Inside-out AST translation, self-join maximum pattern (2021 Q2c, CT-01 Q5) |
| 26 | [T04.4: Extended Relational Algebra and Aggregation](T04.04_Extended_RA_Aggregation.md) | `T04.4` | 🟠 | 4/7 + CT-01 | (in T04.2) | Grouping operator ${}_{G}\gamma_{F}$, finding max group via temp relations |
| 27 | [T04.5: Domain Relational Calculus and Relational Division](T04.05_Domain_Relational_Calculus_and_Division.md) | `T04.5` | 🟢 | 1/7 | 3 | DRC $\{\langle x_1,\dots,x_n \rangle \mid P\}$ (2020 Q4b) and relational division $r \div s$ |

---

### Unit 4 · T05: SQL — DDL, DML, Aggregates & Subqueries (130 Marks · 20.4% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 28 | [T05.1: What Is SQL?](T05.01_What_Is_SQL.md) | `T05.1` | 🟢 | 1/7 | 2 | SQL overview, sublanguages (DDL, DML, DCL, TCL), three-valued logic (2019 Q5a) |
| 29 | [T05.2a: SQL DDL & DML Syntax and Student Table Drills](T05.02a_DDL_DML_Syntax_and_Student_Tables.md) | `T05.2` | 🔴 | 6/7 | 33 | `CREATE`, `INSERT`, `ALTER TABLE ADD`, `UPDATE`, `DELETE` (2017 Q4a, 2018 Q7a = 2024 Q4b) |
| 30 | [T05.2b: SQL DDL & DML Practice Sets](T05.02b_DDL_DML_Practice_Sets.md) | `T05.2` | 🔴 | 6/7 | (in 33) | Covid DDL (2019 Q5c), E-commerce DDL (2021 Q3a), Employee DDL/DML (2023 Q3a) |
| 31 | [T05.3: Basic SQL Query Clauses](T05.03_Basic_Query_Clauses.md) | `T05.3` | 🟢 | 2/7 + CT-02 | (in T05.5/8) | `DISTINCT`, `ORDER BY`, `AS`, `LIKE` pattern matching `%` and `_` (CT-02 Q1b) |
| 32 | [T05.4: SQL Aggregate Functions](T05.04_Aggregate_Functions.md) | `T05.4` | 🟡 | 2/7 | 7 | `AVG`, `MIN`, `MAX`, `SUM`, `COUNT(*)` vs. `COUNT(col)` and `NULL` ignoring (2019 Q8a, 2024 Q7a) |
| 33 | [T05.5a: GROUP BY and HAVING Clauses](T05.05a_GROUP_BY_and_HAVING.md) | `T05.5` | 🟠 | 3/7 + CT-02 | 24 (+3) | `WHERE` vs. `HAVING` execution pipeline, grouping rules (2018 Q7b, CT-02 Q1d) |
| 34 | [T05.5b: Weighted CGPA and Extremes Without LIMIT](T05.05b_CGPA_and_Extremes_Without_LIMIT.md) | `T05.5` | 🟠 | 3/7 + CT-02 | (in 24) | $\text{CGPA} = \frac{\sum(\text{gpa}\cdot\text{credit})}{\sum\text{credit}}$, min/max/2nd-highest without `LIMIT` (2019 Q7a, 2024 Q1c) |
| 35 | [T05.6: SQL Subqueries](T05.06_Subqueries.md) | `T05.6` | 🟡 | 2/7 + CT-02 | 8 (+3) | `IN`/`NOT IN`, `SOME`/`ALL`, `EXISTS`/`NOT EXISTS`, correlated subqueries, `WITH` (2019 Q8b, 2024 Q6a) |
| 36 | [T05.7a: Multi-Table Query Sets — Covid and Company](T05.07a_Query_Sets_Covid_and_Company.md) | `T05.7` | 🔴 | 5/7 | **44** | #1 Subtopic by marks: Covid DB (2019 Q5b) and Company DB (2020 Q3b) |
| 37 | [T05.7b: Multi-Table Query Sets — Insurance and E-Commerce](T05.07b_Query_Sets_Insurance_and_Ecommerce.md) | `T05.7` | 🔴 | 5/7 | (in 44) | Insurance DB (2020 Q7b = 2024 Q5b, Ex. 3.4/3.14) and E-Commerce DB (2021 Q4a) |
| 38 | [T05.8: SQL Short Notes — ON DELETE CASCADE, GROUP BY, ORDER BY, AS](T05.08_Short_Notes_ON_DELETE_CASCADE_GROUP_BY_ORDER_BY.md) | `T05.8` | 🟠 | 3/7 | 10 | High-frequency 2.5-mark short-note questions (2019 Q8c, 2023 Q6c, 2024 Q7b) |
| 39 | [T05.9: TRUNCATE vs. DELETE](T05.09_TRUNCATE_vs_DELETE.md) | `T05.9` | 🟢 | 1/7 | 2 | DDL vs. DML, rollback, triggers, `AUTO_INCREMENT` reset (2023 Q6a) |

---

### Unit 4 · T06: Joins & Views (28 Marks · 4.4% · 4/7 Finals · 🟠 · 11.2% in Modern OBE)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 40 | [T06.1: Types of SQL Joins](T06.01_Types_of_Joins.md) | `T06.1` | 🟠 | 3/7 | 11 | Inner, natural, theta, left/right/full outer, cross join comparisons (2019 Q3c, 2023 Q5c, 2024 Q3c) |
| 41 | [T06.2: Computing Join Outcome Tables in MySQL](T06.02_Join_Outcome_Tables.md) | `T06.2` | 🟡 | 2/7 | 11 | Step-by-step outcome tables for `Courses` $\bowtie$ `Teacher` + MySQL `LEFT UNION RIGHT` (2020 Q4c, 2024 Q4a) |
| 42 | [T06.3: Outer-Join Relational Algebra](T06.03_Outer_Join_Algebra.md) | `T06.3` | 🟢 ⭐ | 0/7 | — | $\mathbin{⟕}, \mathbin{⟖}, \mathbin{⟗}$ definitions, non-commutativity/non-associativity |
| 43 | [T06.4: SQL Views — Benefits and CREATE VIEW](T06.04_Views.md) | `T06.4` | 🟢 | 1/7 | 6 | Security, abstraction, multi-table `CREATE VIEW` evaluation (2023 Q5a, Q5b) |
| 44 | [T06.5: View Expansion, Updatable Views, and Materialized Views](T06.05_View_Expansion_Updatable_Materialized.md) | `T06.5` | 🟢 ⭐ | 0/7 | — | View expansion rewriting, 4 updatable view rules, materialized view maintenance |

---

### Unit 4 · T07: Triggers & Stored Procedures (27 Marks · 4.2% · 5/7 Finals · 🟠 · 8.1% in Modern OBE)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 45 | [T07.1: SQL Triggers — Definition, Purpose, and Syntax](T07.01_Triggers_Definition_and_Syntax.md) | `T07.1` | 🟡 | 2/7 | 9 | ECA model, `BEFORE`/`AFTER`, `FOR EACH ROW`, `NEW`/`OLD`, `DELIMITER //` (2018 Q8a = 2020 Q8a) |
| 46 | [T07.2: Triggers for Database Security](T07.02_Triggers_for_Security.md) | `T07.2` | 🟡 | 2/7 | 8 | Proactive `BEFORE` prevention (`SIGNAL`) vs. forensic `AFTER` audit logging (2017 Q8b = 2024 Q2a) |
| 47 | [T07.3: Implementing Triggers and Stored Procedures](T07.03_Implementing_Triggers_and_Procedures.md) | `T07.3` | 🟡 | 2/7 | 10 | Order-placement stored procedure + stock-update & audit triggers (2023 Q6b, 2024 Q6b) |

---

### Unit 5 · T08: Normalization & Functional Dependencies (75 Marks · 11.8% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 48 | [T08.1: Why Normalize? Redundancy and Update Anomalies](T08.01_Why_Normalize_Anomalies.md) | `T08.1` | 🟠 | 4/7 + CT-03 | 18 (+3) | Insertion, deletion, and update anomalies with concrete table traces |
| 49 | [T08.2: Functional Dependencies and Attribute Classification](T08.02_Functional_Dependency_Types.md) | `T08.2` | 🟢 ⭐ | 0/7 + CT-03 | 0 (+4) | Trivial/non-trivial, full vs. partial, transitive FDs; prime vs. non-prime attributes (CT-03 Q1b–c) |
| 50 | [T08.3: Armstrong's Axioms and Additional Inference Rules](T08.03_Armstrongs_Axioms.md) | `T08.3` | 🟢 ⭐ | 0/7 | — | Reflexivity, Augmentation, Transitivity + proofs of Union, Decomposition, Pseudotransitivity |
| 51 | [T08.4: Attribute Closure and Finding Candidate Keys](T08.04_Attribute_Closure_and_Candidate_Keys.md) | `T08.4` | 🟢 | 1/7 + CT-03 | 4 (+4) | $X^+$ closure algorithm, L/R/M/N attribute shortcut, 2021 Q5b (Ex. 7.6), CT-03 Q1a |
| 52 | [T08.5: Canonical Cover of Functional Dependencies](T08.05_Canonical_Cover.md) | `T08.5` | 🟢 | 1/7 | 8 | Extraneous attribute test, computing $F_c$, canonical cover vs. normalization (2021 Q6a, Q6b) |
| 53 | [T08.6: Normal Forms — 1NF, 2NF, and 3NF](T08.06_Normal_Forms_1NF_2NF_3NF.md) | `T08.6` | 🟠 | 3/7 + CT-03 | 14 (+3) | Formal definitions, violation tests, and decomposition rules for 1NF, 2NF, 3NF |
| 54 | [T08.7: Testing 2NF from a Functional Dependency Set](T08.07_2NF_Test_from_FDs.md) | `T08.7` | 🟢 | 1/7 | 4 | Testing $R(A,B,C,D)$ with $AB \to CD, B \to C$ and lossless 2NF decomposition (2021 Q5c) |
| 55 | [T08.8a: Table Normalization Walkthroughs I (2017 & 2024)](T08.08a_Normalization_Walkthrough_I.md) | `T08.8` | 🟠 | 4/7 | 27 | Step-by-step UNF $\to$ 1NF $\to$ 2NF $\to$ 3NF method, `com_employee` (2017 Q3b), library (2024 Q3a) |
| 56 | [T08.8b: Table Normalization Walkthroughs II (2020 & 2023)](T08.08b_Normalization_Walkthrough_II.md) | `T08.8` | 🟠 | 4/7 | (in 27) | Project billing table with `Hrs. Biller.` (2020 Q8b) and Course/Instructor grades (2023 Q2a) |
| 57 | [T08.9: Boyce-Codd Normal Form (BCNF) and 3NF vs. BCNF](T08.09_BCNF.md) | `T08.9` | 🟢 ⭐ | 0/7 + CT-03 | 0 (+6) | BCNF definition, prime-attribute escape clause in 3NF, highest NF test (CT-03 Q1d, Q4) |
| 58 | [T08.10: Pros and Cons of Normalization & Denormalization](T08.10_Denormalization.md) | `T08.10` | 🟢 ⭐ | 0/7 | — | Join overhead vs. write anomalies, controlled redundancy in OLAP, materialized views |
| 59 | [T08.11: Lossless-Join Decomposition and Dependency Preservation](T08.11_Lossless_Join_and_Dependency_Preservation.md) | `T08.11` | 🟢 ⭐ | 0/7 | — | Spurious tuples, binary lossless test $R_1 \cap R_2 \to R_1 \text{ or } R_2$, dependency preservation (**Teacher Blueprint #1!**) |

---

### Unit 6 · T09: Transactions, ACID & Concurrency Anomalies (41 Marks · 6.4% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 60 | [T09.1: ACID Properties of Transactions](T09.01_ACID_Properties.md) | `T09.1` | 🔴 | 5/7 + CT-04 | 18 (+6) | Atomicity, Consistency, Isolation, Durability with the \$50 bank transfer trace & diagram |
| 61 | [T09.2: The Consistency Property in Depth](T09.02_Consistency.md) | `T09.2` | 🟡 | 2/7 | 6 | Sum preservation $A+B$, temporary violation during active execution (2019 Q3b = 2024 Q2c) |
| 62 | [T09.3: Transaction States and Life-Cycle Diagram](T09.03_Transaction_States.md) | `T09.3` | 🟡 | 2/7 | 6 | Active, Partially Committed, Committed, Failed, Aborted + Restart vs. Kill (2020 Q5b, 2023 Q4c) |
| 63 | [T09.4: Concurrent Execution and Schedules](T09.04_Concurrent_Execution_and_Schedules.md) | `T09.4` | 🟢 | 1/7 + CT-04 | 4 (+4) | Throughput/response-time benefits, serial vs. concurrent vs. serializable schedules (2018 Q6a, CT-04 Q2) |
| 64 | [T09.5: Concurrency Anomalies](T09.05_Concurrency_Problems.md) | `T09.5` | 🟡 | 2/7 + CT-04 | 7 (+4) | Dirty read, lost update, unrepeatable read, phantom read, incorrect summary (2018 Q5a = 2024 Q8a) |

---

### Unit 6 · T10: Serializability (51 Marks · 8.0% · 7/7 Finals · 🔴)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 65 | [T10.1: Conflicting Instructions and Conflict Serializability](T10.01_Conflicting_Instructions.md) | `T10.1` | 🟢 | 1/7 | 2 | R-W, W-R, W-W conflict rules on same data item, conflict equivalence (2017 Q5b) |
| 66 | [T10.2: Conflict Equivalence by Swapping Instructions](T10.02_Conflict_Equivalence_by_Swapping.md) | `T10.2` | 🟢 | 1/7 | 4 | Step-by-step non-conflicting adjacent instruction swaps to reach serial order (2020 Q5c) |
| 67 | [T10.3a: Precedence-Graph Method and Cycle Detection](T10.03a_Precedence_Graph_Method.md) | `T10.3` | 🔴 | 5/7 + CT-04 | 26 (+6) | Precedence graph $G=(V,E)$ algorithm, topological sort, 2018 Q6c = 2024 Q8c, CT-04 Q4 |
| 68 | [T10.3b: Precedence-Graph Drills I (2020 Q6a & 2021 Q7b)](T10.03b_Precedence_Graph_Drills_I.md) | `T10.3` | 🔴 | 5/7 + CT-04 | (in 26) | Subscript schedule notation $r_1(X); w_2(X)$ (2020 Q6a i–ii) and tabular schedule (2021 Q7b) |
| 69 | [T10.3c: Precedence-Graph Drills II (2021 Q7c & 2023 Q8b)](T10.03c_Precedence_Graph_Drills_II.md) | `T10.3` | 🔴 | 5/7 + CT-04 | (in 26) | 2-transaction cycle (2021 Q7c) and 4-transaction DAG with all 3 serial orders (2023 Q8b) |
| 70 | [T10.4: Building Serializable and Non-Serializable Schedules](T10.04_Building_Serializable_Schedules.md) | `T10.4` | 🟡 | 2/7 | 13 | Conditional `if A = 0 then B := B + 1` schedules (2017 Q5c, 2019 Q4a = Ex. 17.15) |
| 71 | [T10.5: View Serializability and Blind Writes](T10.05_View_Serializability.md) | `T10.5` | 🟢 | 1/7 | 6 | Initial read, read-from, final write conditions; blind write shortcut (2020 Q6b) |
| 72 | [T10.6: Recoverable, Cascadeless, and Strict Schedules](T10.06_Recoverable_Cascadeless_Strict_Schedules.md) | `T10.6` | 🟢 ⭐ | 0/7 | — | Recoverability hierarchy: Strict $\subset$ Cascadeless $\subset$ Recoverable |

---

### Unit 6 · T11: Concurrency Control Protocols (37 Marks · 5.8% · 6/7 Finals · 🟠)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 73 | [T11.1: Shared and Exclusive Locks & Compatibility Matrix](T11.01_Shared_Exclusive_Locks.md) | `T11.1` | 🟢 ⭐ | 1/7 | (in T11.2) | `lock-S` vs. `lock-X` compatibility matrix, starvation cause & FIFO cure (2017 Q7a) |
| 74 | [T11.2: Two-Phase Locking (2PL) Protocol](T11.02_Two_Phase_Locking.md) | `T11.2` | 🟢 | 1/7 | 9 | Growing/shrinking phases, lock point serializability, lock conversion (2017 Q6b, Q7a) |
| 75 | [T11.3: Strict 2PL, Rigorous 2PL, and Drawbacks of 2PL](T11.03_Strict_and_Rigorous_2PL.md) | `T11.3` | 🟢 ⭐ | 0/7 | — | Preventing cascading rollbacks under Strict/Rigorous 2PL |
| 76 | [T11.4: Deadlock Handling — Prevention, Detection & Wait-For Graph](T11.04_Deadlock.md) | `T11.4` | 🟠 | 4/7 | 17 | 4 Coffman conditions, wait-for graph cycle detection, victim selection (2017 Q7b, 2018 Q5b, 2020 Q7a, 2021 Q8a) |
| 77 | [T11.5: Wait-Die vs. Wound-Wait Deadlock Prevention](T11.05_Wait_Die_vs_Wound_Wait.md) | `T11.5` | 🟢 ⭐ | 0/7 | — | Non-preemptive `wait-die` vs. preemptive `wound-wait`; **retains ORIGINAL timestamp** (**Teacher Blueprint!**) |
| 78 | [T11.6: Timestamp-Ordering (TSO) Protocol](T11.06_Timestamp_Ordering.md) | `T11.6` | 🟠 | 3/7 | 11 | $\text{R-timestamp}(Q)$ & $\text{W-timestamp}(Q)$ rules, schedule trace (2023 Q8c), **NEW timestamp on rollback** (2018 Q6b = 2024 Q8b) |

---

### Unit 7 · T12: Recovery System & RAID (43 Marks · 6.8% · 5/7 Finals · 🟠 · 13.1% in Modern OBE)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 79 | [T12.1: Failure Classification and Recovery Precautions](T12.01_Failure_Classification.md) | `T12.1` | 🔴 | 5/7 | 17 | Transaction failure (logical/system), system crash, disk failure (2017 Q6c, 2018 Q5c, 2019 Q4b = 2024 Q3b, 2023 Q7a) |
| 80 | [T12.2: Role of the Recovery Manager](T12.02_Recovery_Manager_Role.md) | `T12.2` | 🟢 | 1/7 | 4 | Why a never-failing DB still needs a recovery manager for concurrency aborts (2018 Q8b = Ex. 17.1) |
| 81 | [T12.3: Log-Based Recovery and Shadow Paging](T12.03_Log_Based_Recovery_and_Shadow_Paging.md) | `T12.3` | 🟡 | 2/7 | 7 | WAL rule, `<Ti, X, V1, V2>`, `undo`/`redo` crash trace, checkpoints, shadow paging (2017 Q6d, 2023 Q7b) |
| 82 | [T12.4: RAID Levels and Storage Reliability](T12.04_RAID_Levels.md) | `T12.4` | 🟠 | 3/7 | 15 | RAID 0, 1, 1+0, 3, 5, 6 architecture, capacity, parity overhead, multimedia archive choice (2018 Q5c/8c, 2023 Q4a/7c, 2024 Q7c) |

---

### Unit 8 · T13: Security, Indexing & Hashing (18 Marks · 2.8% · 4/7 Finals · 🟢)

| # | Boss Note File | Subtopic | Priority | Exam Freq | Marks | Key Exam Focus |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 83 | [T13.1: Database Security Threats and Authorization](T13.01_Security_and_Authorization.md) | `T13.1` | 🟢 | 1/7 | 4 | CIA triad, 4 database security threats, SQL `GRANT` and `REVOKE` (2017 Q8a) |
| 84 | [T13.2: SQL Injection — Mechanism and Prevention](T13.02_SQL_Injection.md) | `T13.2` | 🟡 | 2/7 | 9 | `' OR '1'='1` tautology attack, `PreparedStatement` parameterized queries (2020 Q4a = Ex. 9.16, 2021 Q8b) |
| 85 | [T13.3: Ordered Indexing — Dense vs. Sparse Index and B+-Trees](T13.03_Dense_vs_Sparse_Index.md) | `T13.3` | 🟢 | 1/7 | 2 | Dense vs. sparse index trade-offs, clustering requirement, B+-tree overview (2023 Q8a) |
| 86 | [T13.4: Static vs. Dynamic Hashing](T13.04_Static_vs_Dynamic_Hashing.md) | `T13.4` | 🟢 | 1/7 | 3 | Hash bucket overflow chaining vs. extendable hashing directory doubling (2017 Q7c) |

---

## 📊 Exam Triage Strategy (Study Paths by Time Remaining)

Because the exam requires you to answer **3 questions from Section A (30 marks)** and **3 questions from Section B (30 marks)** on separate answer scripts, your study plan must balance both sections.

### 🗓️ Path 1: If You Have 7+ Days (Full Mastery — Target: 55–60 / 60 Marks)

Follow this 7-day sequence so foundational concepts feed naturally into query writing, schema design, and transaction protocols:

- **Day 1 (Foundations & E-R Modeling — Section A Q.1):** Read `T01.01`–`T01.07` and `T02.01`–`T02.08` (16 files). Practice drawing the 5 full E-R diagrams in `T02.05a` and `T02.05b` by hand.
- **Day 2 (Relational Keys & Relational Algebra — Section A Q.2):** Read `T03.01`–`T03.04` and `T04.01`–`T04.05` (11 files). Drill the set-difference ("only") and ${}_{G}\gamma_{F}$ aggregation patterns in `T04.02a`–`T04.02c`.
- **Day 3 (SQL Mastery — Both Sections):** Read `T05.01`–`T05.09` (12 files). Write out the multi-table queries in `T05.07a` and `T05.07b` and the weighted CGPA / no-`LIMIT` extreme queries in `T05.05b`.
- **Day 4 (Joins, Views, Triggers & Procedures — Modern OBE Favorites):** Read `T06.01`–`T06.05` and `T07.01`–`T07.03` (8 files). Practice computing the 4 join outcome tables (`T06.02`) and writing a `DELIMITER //` trigger and stored procedure (`T07.03`).
- **Day 5 (Normalization & Functional Dependencies — Both Sections):** Read `T08.01`–`T08.11` (12 files). Master both the table walkthroughs (`T08.08a`–`T08.08b`) and the FD-set closure/CK/BCNF/lossless pipeline (`T08.04`, `T08.09`, `T08.11`).
- **Day 6 (Transactions, Serializability & Concurrency Control — Section B):** Read `T09.01`–`T09.05`, `T10.01`–`T10.06`, and `T11.01`–`T11.06` (17 files). Trace every precedence graph in `T10.03a`–`T10.03c` and the TSO schedule in `T11.06`.
- **Day 7 (Recovery, RAID, Security & Final Review — Section B):** Read `T12.01`–`T12.04` and `T13.01`–`T13.04` (8 files), then review the [Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md).

---

### 🗓️ Path 2: If You Have 3 Days (High-Yield Core — Target: 48–54 / 60 Marks)

Focus strictly on the 🔴 and 🟠 files (42 files total) that account for **86% of all exam marks**:

- **Day 1 (Section A Lock-In — 30 Marks):**
  - **Q.1 Slot (DB Intro + E-R):** [T01.2 File vs. DBMS](T01.02_File_System_vs_DBMS.md), [T01.3 DBA Functions](T01.03_DBA_Functions_and_Relation_Schema.md), [T01.4 Data Abstraction](T01.04_Data_Abstraction_Schemas_Instances.md), [T02.4 Weak Entities](T02.04_Weak_vs_Strong_Entity_Sets.md), [T02.5a](T02.05a_ER_Design_Method_Student_and_Teacher_Course.md) & [T02.5b E-R Design](T02.05b_ER_Design_Ticketing_Library_University.md).
  - **Q.2 Slot (Keys + RA):** [T03.2 Keys](T03.02_Keys.md), [T04.2a](T04.02a_RA_Queries_Employee_and_Insurance.md)–[T04.2c RA Queries](T04.02c_RA_Queries_Orders_Projects_CT.md).
- **Day 2 (Cross-Section Heavyweights — SQL, Joins/Views, Normalization):**
  - **SQL & Joins:** [T05.2a DDL/DML](T05.02a_DDL_DML_Syntax_and_Student_Tables.md), [T05.5a](T05.05a_GROUP_BY_and_HAVING.md)–[T05.5b CGPA & Extremes](T05.05b_CGPA_and_Extremes_Without_LIMIT.md), [T05.6 Subqueries](T05.06_Subqueries.md), [T05.7a](T05.07a_Query_Sets_Covid_and_Company.md)–[T05.7b Multi-Table SQL](T05.07b_Query_Sets_Insurance_and_Ecommerce.md), [T05.8 Short Notes](T05.08_Short_Notes_ON_DELETE_CASCADE_GROUP_BY_ORDER_BY.md), [T06.1 Join Types](T06.01_Types_of_Joins.md), [T06.2 Join Outcome Tables](T06.02_Join_Outcome_Tables.md), [T06.4 Views](T06.04_Views.md).
  - **Normalization:** [T08.1 Anomalies](T08.01_Why_Normalize_Anomalies.md), [T08.4 Closure & CKs](T08.04_Attribute_Closure_and_Candidate_Keys.md), [T08.6 1NF–3NF](T08.06_Normal_Forms_1NF_2NF_3NF.md), [T08.8a](T08.08a_Normalization_Walkthrough_I.md)–[T08.8b Walkthroughs](T08.08b_Normalization_Walkthrough_II.md), [T08.9 BCNF](T08.09_BCNF.md), [T08.11 Lossless & Dep. Preservation](T08.11_Lossless_Join_and_Dependency_Preservation.md).
- **Day 3 (Section B Lock-In — Transactions, Serializability, Concurrency, Recovery/RAID, Triggers):**
  - **Transactions & Serializability:** [T09.1 ACID](T09.01_ACID_Properties.md), [T09.3 States](T09.03_Transaction_States.md), [T09.5 Anomalies](T09.05_Concurrency_Problems.md), [T10.3a](T10.03a_Precedence_Graph_Method.md)–[T10.3c Precedence Graphs](T10.03c_Precedence_Graph_Drills_II.md), [T10.5 View Serializability](T10.05_View_Serializability.md).
  - **CC, Recovery & Triggers:** [T11.4 Deadlock](T11.04_Deadlock.md), [T11.5 Wait-Die/Wound-Wait](T11.05_Wait_Die_vs_Wound_Wait.md), [T11.6 TSO](T11.06_Timestamp_Ordering.md), [T12.1 Failures](T12.01_Failure_Classification.md), [T12.3 Log Recovery](T12.03_Log_Based_Recovery_and_Shadow_Paging.md), [T12.4 RAID](T12.04_RAID_Levels.md), [T07.1](T07.01_Triggers_Definition_and_Syntax.md)–[T07.3 Triggers & Procedures](T07.03_Implementing_Triggers_and_Procedures.md).

---

### 🗓️ Path 3: If You Have 1 Night (Emergency Survival — Target: 38–45 / 60 Marks)

Do not try to read all 86 files in one night. Study these **15 highest-yield files** (~4.5 hours total), read the [Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md), and get at least 4 hours of sleep so you do not make silly mistakes on SQL joins or precedence-graph arrows:

1. **Section A Q.1 (10m):** [T01.2 File System vs. DBMS](T01.02_File_System_vs_DBMS.md) + [T02.5a E-R Design Method](T02.05a_ER_Design_Method_Student_and_Teacher_Course.md) + [T02.4 Weak vs. Strong Entities](T02.04_Weak_vs_Strong_Entity_Sets.md).
2. **Section A Q.2 (10m):** [T03.2 Relational Keys](T03.02_Keys.md) + [T04.2a RA Query Recipe](T04.02a_RA_Queries_Employee_and_Insurance.md).
3. **Section A Q.3/Q.4 (10m):** [T08.1 Anomalies](T08.01_Why_Normalize_Anomalies.md) + [T08.8a Normalization Walkthrough Recipe](T08.08a_Normalization_Walkthrough_I.md) + [T06.2 Join Outcome Tables](T06.02_Join_Outcome_Tables.md).
4. **Section B SQL Question (10m):** [T05.2a DDL/DML Syntax](T05.02a_DDL_DML_Syntax_and_Student_Tables.md) + [T05.5b CGPA & No-LIMIT Extremes](T05.05b_CGPA_and_Extremes_Without_LIMIT.md) + [T05.8 SQL Short Notes](T05.08_Short_Notes_ON_DELETE_CASCADE_GROUP_BY_ORDER_BY.md).
5. **Section B Transactions/CC Question (10m):** [T09.1 ACID Properties](T09.01_ACID_Properties.md) + [T10.3a Precedence-Graph Method](T10.03a_Precedence_Graph_Method.md) + [T11.6 Timestamp Ordering](T11.06_Timestamp_Ordering.md).
6. **Section B Recovery/RAID or Triggers Question (10m):** [T12.1 Failure Classification](T12.01_Failure_Classification.md) + [T12.4 RAID Levels](T12.04_RAID_Levels.md) + [T07.1–T07.3 Triggers](T07.01_Triggers_Definition_and_Syntax.md).

---

## 🔮 Data-Driven Exam Predictions

Synthesizing the 2023–2024 Modern-OBE shift (`ECE2215_PYQ_Analysis_Report.md` §A3), the 4 Class Tests (`CT-01`–`CT-04`), and the instructors' explicit exam blueprint recorded in Raidah's notebook (`Classnote_by_Raidah/suggestions.md` p. 34):

1. **Rising Modern-OBE Topics (Guaranteed in 2023 & 2024):**
   - **Joins & Views (`T06`):** Surged from `2.6%` in Pre-OBE to **`11.2%`** in Modern OBE. Expect either a 4-way join outcome table (`Natural`, `Left`, `Right`, `Full Outer Join` in MySQL using `UNION`: [T06.2](T06.02_Join_Outcome_Tables.md)) or a multi-table `CREATE VIEW` query ([T06.4](T06.04_Views.md)).
   - **Recovery & RAID (`T12`):** Surged from `5.8%` to **`13.1%`**. Raidah's class notes explicitly highlight **RAID 0, 1, 1+0, 3, 5, 6** comparisons (striping vs. mirroring vs. dedicated/distributed parity: [T12.4](T12.04_RAID_Levels.md)), alongside failure classification ([T12.1](T12.01_Failure_Classification.md)) and WAL crash recovery ([T12.3](T12.03_Log_Based_Recovery_and_Shadow_Paging.md)).
   - **Triggers & Stored Procedures (`T07`):** Surged from `3.7%` to **`8.1%`**, shifting from pure theory to writing a MySQL `CREATE TRIGGER` or `CREATE PROCEDURE` for an order/inventory/audit scenario ([T07.3](T07.03_Implementing_Triggers_and_Procedures.md)).

2. **Top Unasked Blueprint Candidates (`⭐` — Taught & Highlighted by Instructors, Never in a Final Yet):**
   - **FD-Set Normalization Pipeline (`T08.4` + `T08.9` + `T08.11`):** Tested in `CT-03 Q.1` and listed as Item #1 in `suggestions.md`: given $R(A,B,C,D,E)$ and an FD set $F$, compute attribute closures $X^+$, find all candidate keys, classify prime vs. non-prime attributes, identify the highest normal form (1NF/2NF/3NF/BCNF), and decompose into 3NF/BCNF while testing **lossless-join** ($R_1 \cap R_2 \to R_1 \text{ or } R_2$) and **dependency preservation**.
   - **Wait-Die vs. Wound-Wait Deadlock Prevention (`T11.5`):** Explicitly named in `suggestions.md` Item #3 alongside the 4 Coffman conditions. Know the non-preemptive vs. preemptive timestamp rules and why rolled-back transactions keep their **original** timestamp here ([T11.5](T11.05_Wait_Die_vs_Wound_Wait.md)) while getting a **new** timestamp under TSO ([T11.6](T11.06_Timestamp_Ordering.md)).
   - **View Serializability & Blind-Write Shortcut (`T10.5`):** Highlighted in `suggestions.md` Item #2: if a schedule is not conflict serializable, check whether it has any **blind writes** (a `write(Q)` without a preceding `read(Q)`). No blind writes $\implies$ not view serializable!

---

## ✅ Guaranteed Marks Checklist (Top 12 High-Certainty Exam Blocks)

Verify that you can solve each of these 12 items from memory before walking into the exam hall:

- [ ] **1. Multi-Table SQL & DDL/DML (`T05.2`, `T05.7` — 10–15 marks):** Write `CREATE TABLE` with PK/FK, `ALTER TABLE ... ADD`, multi-table joins, and `NOT EXISTS` / `NOT IN` anti-joins ([T05.02a](T05.02a_DDL_DML_Syntax_and_Student_Tables.md), [T05.07a](T05.07a_Query_Sets_Covid_and_Company.md), [T05.07b](T05.07b_Query_Sets_Insurance_and_Ecommerce.md)).
- [ ] **2. SQL Aggregation, Weighted CGPA & No-`LIMIT` Extremes (`T05.5`, `T05.8` — 4–8 marks):** Write $\text{CGPA} = \frac{\sum(\text{gpa}\cdot\text{credit})}{\sum\text{credit}}$, find max/min/2nd-highest using subqueries without `LIMIT`, and write short notes on `ON DELETE CASCADE`, `GROUP BY`, `ORDER BY`, `AS` ([T05.05b](T05.05b_CGPA_and_Extremes_Without_LIMIT.md), [T05.08](T05.08_Short_Notes_ON_DELETE_CASCADE_GROUP_BY_ORDER_BY.md)).
- [ ] **3. Relational Algebra Queries (`T04.2` — 4–8 marks):** Translate English queries into $\sigma, \Pi, \bowtie, -, {}_{G}\gamma_{F}$, and 6e-style updates $r \leftarrow \Pi_{\dots}(r)$ ([T04.02a](T04.02a_RA_Queries_Employee_and_Insurance.md)–[T04.02c](T04.02c_RA_Queries_Orders_Projects_CT.md)).
- [ ] **4. Full E-R Diagram & Weak Entities (`T02.4`, `T02.5` — 4–6 marks):** Draw a clean Chen E-R diagram with underlined PKs, dashed-underline discriminators, double-diamond identifying relationships, and double-line total participation ([T02.04](T02.04_Weak_vs_Strong_Entity_Sets.md), [T02.05a](T02.05a_ER_Design_Method_Student_and_Teacher_Course.md)).
- [ ] **5. Table Normalization & FD-Set BCNF/Lossless (`T08.1`, `T08.8`, `T08.9`, `T08.11` — 6–10 marks):** Normalize an unnormalized table to 3NF showing populated tables at each step, and test $X^+$, candidate keys, BCNF, and lossless join ([T08.08a](T08.08a_Normalization_Walkthrough_I.md), [T08.09](T08.09_BCNF.md), [T08.11](T08.11_Lossless_Join_and_Dependency_Preservation.md)).
- [ ] **6. Precedence Graph & View Serializability (`T10.3`, `T10.5` — 4–6 marks):** List all R-W, W-R, W-W conflicts, draw $G=(V,E)$, test for cycles, list all topological sort serial orders, and check for blind writes ([T10.03a](T10.03a_Precedence_Graph_Method.md)–[T10.03c](T10.03c_Precedence_Graph_Drills_II.md), [T10.05](T10.05_View_Serializability.md)).
- [ ] **7. File System vs. DBMS & DBA Roles (`T01.2`, `T01.3` — 3–5 marks):** Explain the 8 file-system disadvantages and 5 DBA functions ([T01.02](T01.02_File_System_vs_DBMS.md), [T01.03](T01.03_DBA_Functions_and_Relation_Schema.md)).
- [ ] **8. Relational Keys (`T03.2` — 3–4 marks):** Distinguish superkey, candidate key, primary key, alternate key, composite key, and foreign key with a concrete relation table ([T03.02](T03.02_Keys.md)).
- [ ] **9. ACID Properties & Concurrency Anomalies (`T09.1`, `T09.5` — 4–6 marks):** Trace the \$50 transfer from $A$ to $B$ across all 4 ACID properties and illustrate dirty read, lost update, and unrepeatable read ([T09.01](T09.01_ACID_Properties.md), [T09.05](T09.05_Concurrency_Problems.md)).
- [ ] **10. Deadlock & Timestamp Ordering (`T11.4`, `T11.5`, `T11.6` — 4–6 marks):** State the 4 Coffman conditions, trace wait-for graph cycles, compare `wait-die` vs. `wound-wait`, and trace TSO read/write rules + the new-timestamp-on-rollback rule ([T11.04](T11.04_Deadlock.md)–[T11.06](T11.06_Timestamp_Ordering.md)).
- [ ] **11. Failure Classification, Log Recovery & RAID (`T12.1`, `T12.3`, `T12.4` — 6–10 marks):** Classify the 3 failure types, trace WAL `undo`/`redo` with checkpoints, and compare RAID 0, 1, 1+0, 3, 5, 6 ([T12.01](T12.01_Failure_Classification.md), [T12.03](T12.03_Log_Based_Recovery_and_Shadow_Paging.md), [T12.04](T12.04_RAID_Levels.md)).
- [ ] **12. Joins, Views & Triggers (`T06.1`, `T06.2`, `T07.1`–`T07.3` — 6–10 marks):** Compute Natural/Left/Right/Full Outer Join outcome tables and write a MySQL `BEFORE`/`AFTER` trigger or stored procedure ([T06.02](T06.02_Join_Outcome_Tables.md), [T07.03](T07.03_Implementing_Triggers_and_Procedures.md)).

---

[📖 Course README](README.md) | [📐 Master Formula & Syntax Sheet](99_Master_Formula_and_Syntax_Sheet.md) | [Start Reading: T01.1 →](T01.01_Data_DB_and_DBMS_Basics.md)

