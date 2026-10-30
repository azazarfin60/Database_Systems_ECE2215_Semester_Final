# ECE 2215: Database Systems — Master Textbook Exercises Index

- **Course:** ECE 2215 — Data Base Systems (RUET)
- **Credit:** 3.00
- **Institution:** Rajshahi University of Engineering & Technology (RUET)
- **Instructors:** Mst. Nafia Islam Shishir & Md. Rakibul Islam
- **Textbook:** Silberschatz, Korth & Sudarshan, *Database System Concepts* (7th Edition, McGraw-Hill, 2019)
- **Total Problem Files:** 26 topic-partitioned markdown documents (all $\le 15$ problems per file)
- **Total Exercises Solved:** **339 exercises** (137 Practice Exercises + 202 Regular Exercises)
- **Curriculum Scope:** Complete coverage across all 8 RUET Syllabus Units & 13 Core Topics (`T01`–`T13`)
- **Quality Assurance Audit:** **100% Certified PASS** (Isolated `$$` display math KaTeX fences, tagged code blocks, verified derivations, zero broken links/images)

### Companion Study Vaults
- **Topic-Wise Exam-Style Answers:** [`../Topicwise_answers_exam_style/`](../Topicwise_answers_exam_style/) — Concise, mark-calibrated exam sheet solutions for RUET finals.
- **Topic-Wise Explanations & Proofs:** [`../Topicwise_answers_explaination/`](../Topicwise_answers_explaination/) — In-depth pedagogical step-by-step proofs, common pitfalls, and examiner tips.
- **Master Lecture Slide Index:** [`../LectureSlides/00_Index.md`](../LectureSlides/00_Index.md) — 8 digitized lecture decks (371 slides total).
- **Previous Year Exam Bank:** [`../PreviousYearQuestion/`](../PreviousYearQuestion/) — 7 RUET semester final papers (2017–2024) + 4 Class Tests (CT-01–CT-04).
- **Curriculum Syllabus & Alignment:** [`../syllabus.md`](../syllabus.md) — Official 8-unit RUET syllabus and cross-resource alignment matrix.
- **PYQ Statistical Report & Question Bank:** [`../ECE2215_PYQ_Analysis_Report.md`](../ECE2215_PYQ_Analysis_Report.md) & [`../subtopicwise_questions.md`](../subtopicwise_questions.md).

---

## 1. Master Exercise Bank Matrix

| Part | Exercise Document | Topic ID & Name | Syllabus Unit | Source Chapters | Qs | Solved Exercise IDs | Direct RUET Exam Hits & Significance |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **01** | [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) | `T01` DB Concepts & Architecture | Unit 1 | Ch. 01, 02 | 15 | PE 1.1–1.5, EX 1.6–1.10, 1.12–1.15, 2.17 | DBMS vs File Systems, 3-Schema Architecture, DBA roles, Physical/Logical Data Independence |
| **02** | [`T02_Part1_ER_Modeling_Basics.md`](T02_Part1_ER_Modeling_Basics.md) | `T02` E-R & EER Modeling (Part 1) | Unit 2 | Ch. 06 | 13 | PE 6.1–6.4, 6.7, 6.9, 6.10, EX 6.5, 6.6, 6.13, 6.17–6.19 | **PE 6.2** (2018 Q.2c), **EX 6.17** (2020 Q.2c, 2021 Q.8c) — Entity vs Relationship sets, Weak entities |
| **03** | [`T02_Part2_ER_Scenarios_Reduction_EER.md`](T02_Part2_ER_Scenarios_Reduction_EER.md) | `T02` E-R & EER Modeling (Part 2) | Unit 2 | Ch. 06 | 13 | PE 6.8, 6.12, EX 6.15, 6.16, 6.20–6.28 | Specialization/Generalization, Disjoint/Overlap constraints, Full schema reduction algorithms |
| **04** | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) | `T03` Relational Model, Keys & Integrity | Unit 3 | Ch. 02, 03, 04, 06 | 14 | PE 2.1–2.4, 6.11, EX 2.10–2.13, 2.16, 3.19, 4.7, 4.9, 6.14 | **EX 6.14** (2018 Q.2a, 2021 Q.2b, 2023 Q.3b) — Superkey vs Candidate key, Foreign keys, Referential integrity |
| **05** | [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) | `T04` Relational Algebra & Calculus | Unit 3 | Ch. 02 | 8 | PE 2.5–2.9, EX 2.14, 2.15, 2.18 | **PE 2.6** (2017 Q.2a [8m]) — Relational Division ($\div$) derivation, TRC/DRC queries |
| **06** | [`T05_Part1_SQL_DDL_DML_Basics.md`](T05_Part1_SQL_DDL_DML_Basics.md) | `T05` SQL: DDL & DML Basics (Part 1) | Unit 4 | Ch. 03, 04, 05 | 13 | PE 3.1, 3.3, 3.7, 3.10, 5.4, EX 3.12, 3.13, 3.17, 3.18, 3.23, 3.26, 4.5, 5.16 | DDL constraints, `ON DELETE CASCADE`, Three-valued logic (`NULL`), Safe data modifications |
| **07** | [`T05_Part2_SQL_Clauses_and_Aggregations.md`](T05_Part2_SQL_Clauses_and_Aggregations.md) | `T05` SQL: Clauses & Aggregations (Part 2) | Unit 4 | Ch. 03, 04, 05 | 12 | PE 3.2, 3.5, 3.6, EX 3.11, 3.22, 3.30, 3.34, 4.22, 5.8–5.11 | `ORDER BY`, pattern matching (`LIKE`), `GROUP BY`, `HAVING`, CGPA computation formula |
| **08** | [`T05_Part3_SQL_Aggregations_and_Subqueries.md`](T05_Part3_SQL_Aggregations_and_Subqueries.md) | `T05` SQL: Extremes & Subqueries (Part 3) | Unit 4 | Ch. 03, 05 | 10 | PE 5.3, EX 3.20, 3.31–3.33, 3.35, 5.21–5.24 | Extremes without `LIMIT`/`TOP`, nested subqueries (`NOT EXISTS`, `ALL`), Recursive CTEs |
| **09** | [`T05_Part4_SQL_MultiTable_Business_Queries.md`](T05_Part4_SQL_MultiTable_Business_Queries.md) | `T05` SQL: Multi-Table Enterprise Queries (Part 4) | Unit 4 | Ch. 03, 04 | 15 | PE 3.4, 3.8, 3.9, EX 3.14–3.16, 3.21, 3.24, 3.25, 3.27–3.29, 4.16–4.18 | **PE 3.4 / EX 3.14** (2018 Q.3a, 2020 Q.7b, 2024 Q.5b) — Complex enterprise bank & employee schemas |
| **10** | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) | `T06` Joins and Views | Unit 4 | Ch. 04, 05 | 13 | PE 4.1–4.4, 5.6, EX 4.6, 4.10, 4.13–4.15, 4.19–4.21 | Outer Joins (Left $\mathbin{⟕}$, Right $\mathbin{⟖}$, Full $\mathbin{⟗}$), Updatable views & `WITH CHECK OPTION` |
| **11** | [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) | `T07` Triggers & Stored Procedures | Unit 4 | Ch. 04, 05, 09 | 14 | PE 4.8, 5.1, 5.2, 5.5, 5.7, EX 5.12–5.15, 5.17–5.20, 9.5 | ECA rules (`AFTER INSERT`, `BEFORE UPDATE`), cascading triggers, audit logging, JDBC statement leaks |
| **12** | [`T08_Part1_FDs_and_Armstrong_Axioms.md`](T08_Part1_FDs_and_Armstrong_Axioms.md) | `T08` Normalization: FDs & Axioms (Part 1) | Unit 5 | Ch. 07 | 15 | PE 7.2–7.6, 7.8, 7.9, EX 7.18, 7.23–7.28, 7.31 | **PE 7.6** (2021 Q.5b, CT-03 Q.1) — Formal Armstrong axiom derivations (Pseudotransitivity, Decomposition) |
| **13** | [`T08_Part2_Canonical_Cover_and_3NF.md`](T08_Part2_Canonical_Cover_and_3NF.md) | `T08` Normalization: Canonical Cover & 3NF (Part 2) | Unit 5 | Ch. 07 | 15 | PE 7.1, 7.7, EX 7.10, 7.12–7.16, 7.19, 7.20, 7.22, 7.29, 7.32, 7.33, 7.38 | **PE 7.7** (2021 Q.6b) — Canonical Cover ($F_c$) algorithm, 3NF synthesis algorithm |
| **14** | [`T08_Part3_BCNF_and_Advanced_Normalization.md`](T08_Part3_BCNF_and_Advanced_Normalization.md) | `T08` Normalization: BCNF & Advanced (Part 3) | Unit 5 | Ch. 07 | 14 | EX 7.11, 7.17, 7.21, 7.30, 7.34–7.37, 7.39–7.44 | BCNF decomposition trees, Lossless-join verification, Dependency preservation trade-offs |
| **15** | [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) | `T09` Transactions, ACID & Anomalies | Unit 6 | Ch. 01, 17, 18 | 9 | PE 17.2–17.4, EX 1.11, 17.12, 17.13, 18.13, 18.31, 18.32 | ACID properties, transaction states, Dirty Read, Lost Update, Phantom Read, Incorrect Summary |
| **16** | [`T10_Serializability.md`](T10_Serializability.md) | `T10` Serializability & Precedence Graphs | Unit 6 | Ch. 17 | 15 | PE 17.5–17.11, EX 17.14–17.21 | **EX 17.14** (2018 Q.6a), **EX 17.15** (2017 Q.5c, 2019 Q.4a), **PE 17.5** (2020 Q.6b), **PE 17.6** (2018/20/23/24) |
| **17** | [`T11_Part1_Locking_Protocols.md`](T11_Part1_Locking_Protocols.md) | `T11` Concurrency: Locking Modes (Part 1) | Unit 6 | Ch. 18 | 11 | PE 18.1, 18.6, 18.7, EX 18.9–18.11, 18.14–18.16, 18.19, 18.22 | Shared/Exclusive lock matrices, Lock conversion ($S \to X$), Starvation prevention algorithms |
| **18** | [`T11_Part2_2PL_and_Lock_Conversions.md`](T11_Part2_2PL_and_Lock_Conversions.md) | `T11` Concurrency: 2PL Mechanics (Part 2) | Unit 6 | Ch. 18 | 11 | PE 18.2–18.5, EX 18.23–18.25, 18.29, 18.33–18.35 | **PE 18.2** (2017 Q.7a) — 2PL lock point theorem, Strict 2PL vs Rigorous 2PL, Tree protocol |
| **19** | [`T11_Part3_Deadlock_and_Timestamp_Ordering.md`](T11_Part3_Deadlock_and_Timestamp_Ordering.md) | `T11` Concurrency: Deadlock & TSO (Part 3) | Unit 6 | Ch. 18 | 11 | PE 18.8, 18.12, 18.17, 18.18, EX 18.20, 18.21, 18.26–18.28, 18.30, 18.36 | **EX 18.20** (2018 Q.5b), **EX 18.26** (2018 Q.6b, 2024 Q.8b) — `wait-die` vs `wound-wait`, TSO restart timestamps |
| **20** | [`T12_Part1_Failure_Types_and_RAID_Intro.md`](T12_Part1_Failure_Types_and_RAID_Intro.md) | `T12` Recovery: Failure & Storage (Part 1) | Unit 7 | Ch. 12, 19 | 14 | PE 12.1–12.3, 19.10, 19.12, EX 12.6–12.10, 19.14, 19.15, 19.26, 19.27 | Volatile vs Nonvolatile vs Stable storage, Disk head crashes, RAID 1 mirroring atomicity |
| **21** | [`T12_Part2_Recovery_Manager_and_Log_Recovery.md`](T12_Part2_Recovery_Manager_and_Log_Recovery.md) | `T12` Recovery: Log Tracing & Manager (Part 2) | Unit 7 | Ch. 17, 19 | 14 | PE 17.1, 19.1–19.9, EX 19.11, 19.13, 19.16, 19.17 | **PE 17.1** (2018 Q.8b) — Write-Ahead Logging (WAL), Steal/No-Force, Redo and Undo pass algorithms |
| **22** | [`T12_Part3_Checkpoints_and_RAID_Levels.md`](T12_Part3_Checkpoints_and_RAID_Levels.md) | `T12` Recovery: Checkpoints, ARIES & RAID (Part 3) | Unit 7 | Ch. 12, 19 | 13 | PE 12.4, 12.5, EX 12.11–12.13, 19.18–19.25 | Fuzzy checkpoints, ARIES algorithm (Analysis, Redo, Undo), RAID 0/1/5/6 parity equations |
| **23** | [`T13_Part1_Security_and_Authorization_A.md`](T13_Part1_Security_and_Authorization_A.md) | `T13` Security: Privileges & Graphs (Part 1) | Unit 8 | Ch. 04, 09 | 15 | PE 9.1–9.4, 9.6, 9.7, 9.9–9.12, EX 4.11, 4.12, 4.23–4.25 | `GRANT` / `REVOKE` authorization graphs, Cascading revokes, RBAC roles, `REFERENCES` privilege |
| **24** | [`T13_Part2_Security_and_Authorization_B.md`](T13_Part2_Security_and_Authorization_B.md) | `T13` Security: Access & Governance (Part 2) | Unit 8 | Ch. 04, 09 | 14 | EX 4.26, 9.13–9.15, 9.17–9.26 | Virtual Private Database (VPD) row-level security, Non-monotonic authorization traps, Audit logging |
| **25** | [`T13_Part3_SQL_Injection_and_BTree_Indexing.md`](T13_Part3_SQL_Injection_and_BTree_Indexing.md) | `T13` Security & Indexing: SQLi & B+-Trees (Part 3) | Unit 8 | Ch. 09, 14 | 15 | PE 9.8, 14.1–14.8, EX 9.16, 14.11, 14.13–14.16 | **EX 9.16** (2020 Q.4a, 2021 Q.8b) — SQL Injection defenses (PreparedStatements), Dense vs Sparse indices, B+-tree node splits/merges |
| **26** | [`T13_Part4_Indexing_and_Hashing.md`](T13_Part4_Indexing_and_Hashing.md) | `T13` Indexing & Dynamic Hashing (Part 4) | Unit 8 | Ch. 14 | 13 | PE 14.9, 14.10, 14.12, EX 14.17–14.26 | Extendible dynamic hashing bucket doubling/splitting, Bitmap indices & existence bitmap masks |
| **TOTAL** | **26 Documents** | **All 13 Topics (`T01`–`T13`)** | **All 8 Units** | **Silberschatz 7e** | **339** | **137 PE + 202 EX** | **100% Complete Syllabus & PYQ Coverage** |

---

## 2. RUET Syllabus & Learning Objectives Mapping

### Unit 1: Concepts of Database Systems
- **Exercise Document:** [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) (15 problems)
- **Companion Answers:** [Exam-style T01](../Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) · [Explanation T01](../Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md)
- **Key Concepts Solved:**
  - File-processing systems vs. Database systems: Data redundancy, inconsistency, access difficulty, data isolation, integrity problems, atomicity issues, concurrent-access anomalies, security restrictions (PE 1.1).
  - 3-Schema Architecture: Physical, Logical, and View levels; Physical and Logical Data Independence proofs (PE 1.2, PE 1.3).
  - Roles & Responsibilities: Database Administrator (DBA) functions, database users, query processor, and storage manager modules (EX 1.6–1.8).
  - Relational Schema Diagrams and NoSQL trade-offs (PE 1.4, EX 1.15, EX 2.17).
- **Direct RUET Exam Linkage:** Maps directly to 7/7 semester final Section A questions (`2017 Q.1a`, `2018 Q.1a`, `2019 Q.1a`, `2020 Q.1a`, `2021 Q.1a`, `2023 Q.1a`, `2024 Q.1a`) and `CT-01 Q.1`.

---

### Unit 2: Entity-Relationship (ER) & EER Modeling
- **Exercise Documents:**
  - [`T02_Part1_ER_Modeling_Basics.md`](T02_Part1_ER_Modeling_Basics.md) (13 problems)
  - [`T02_Part2_ER_Scenarios_Reduction_EER.md`](T02_Part2_ER_Scenarios_Reduction_EER.md) (13 problems)
- **Companion Answers:** [Exam-style T02](../Topicwise_answers_exam_style/T02_ER_and_EER_Modeling.md) · [Explanation T02](../Topicwise_answers_explaination/T02_ER_and_EER_Modeling.md)
- **Key Concepts Solved:**
  - Entity Sets vs Relationship Sets: Cardinality ratios (1:1, 1:N, N:1, M:N), participation constraints (total vs partial), attribute types (simple, composite, multivalued, derived) (PE 6.1–6.4).
  - Weak Entity Sets: Identifying relationship sets, discriminators / partial keys, and primary key composition rules (EX 6.5, 6.6, 6.13).
  - Extended ER (EER): Specialization (top-down), Generalization (bottom-up), completeness constraints (total/partial), disjointness constraints (disjoint/overlapping), and aggregation (PE 6.8, 6.12, EX 6.20–6.23).
  - Schema Reduction: Algorithmic translation of strong entities, weak entities, relationship sets, composite/multivalued attributes, and generalization hierarchies into relational tables (EX 6.15, 6.16, 6.24–6.28).
- **Direct RUET Exam Linkage:**
  - **PE 6.2** is recycled verbatim in **2018 Q.2(c)** (Course-Teacher-Student scenario).
  - **EX 6.17** is recycled in **2020 Q.2(c)** and **2021 Q.8(c)** (Hospital patient-doctor system).
  - Full scenario design drills mirror **2017 Q.1(b)** (RUET student database), **2019 Q.1(c)** (Train e-ticketing), **2023 Q.1(a)** (RUET central library), and `CT-02 Q.2`.

---

### Unit 3: Relational Model & Relational Algebra
- **Exercise Documents:**
  - [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) (14 problems)
  - [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) (8 problems)
- **Companion Answers:**
  - `T03`: [Exam-style T03](../Topicwise_answers_exam_style/T03_Relational_Model_Keys_and_Integrity.md) · [Explanation T03](../Topicwise_answers_explaination/T03_Relational_Model_Keys_and_Integrity.md)
  - `T04`: [Exam-style T04](../Topicwise_answers_exam_style/T04_Relational_Algebra_and_Calculus.md) · [Explanation T04](../Topicwise_answers_explaination/T04_Relational_Algebra_and_Calculus.md)
- **Key Concepts Solved:**
  - Relational Keys: Superkey, Candidate key, Primary key, Alternate key, and Foreign key definitions and minimal superkey proofs (PE 2.1–2.4, EX 2.10–2.12).
  - Integrity Constraints: Domain integrity, Entity integrity, Referential integrity, `ON DELETE CASCADE`, and arrow directions in schema diagrams (EX 2.13, 2.16, 3.19, 4.7, 4.9, 6.14).
  - Fundamental Relational Algebra: $\sigma, \Pi, \times, \bowtie_\theta, \cup, -, \cap, \rho, \leftarrow$ (PE 2.5, 2.6, EX 2.14, 2.15).
  - Universal Division ($\div$): Step-by-step mathematical derivation of $r \div s = \Pi_{R-S}(r) - \Pi_{R-S}((\Pi_{R-S}(r) \times s) - r)$ (PE 2.9).
  - Relational Calculus: Tuple Relational Calculus (TRC) and Domain Relational Calculus (DRC) query expressions, DRC safety conditions (EX 2.18).
- **Direct RUET Exam Linkage:**
  - **EX 6.14** matches **2018 Q.2(a)**, **2021 Q.2(b)**, and **2023 Q.3(b)**.
  - **PE 2.6** matches **2017 Q.2(a)** [8 Marks] and **EX 2.14(d)**.
  - DRC problems directly cover **2020 Q.4(b)**.

---

### Unit 4: Structured Query Language (SQL), Joins, Views, Triggers & Procedures
- **Exercise Documents:**
  - [`T05_Part1_SQL_DDL_DML_Basics.md`](T05_Part1_SQL_DDL_DML_Basics.md) (13 problems)
  - [`T05_Part2_SQL_Clauses_and_Aggregations.md`](T05_Part2_SQL_Clauses_and_Aggregations.md) (12 problems)
  - [`T05_Part3_SQL_Aggregations_and_Subqueries.md`](T05_Part3_SQL_Aggregations_and_Subqueries.md) (10 problems)
  - [`T05_Part4_SQL_MultiTable_Business_Queries.md`](T05_Part4_SQL_MultiTable_Business_Queries.md) (15 problems)
  - [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) (13 problems)
  - [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) (14 problems)
- **Companion Answers:**
  - `T05`: [Exam-style T05](../Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) · [Explanation T05](../Topicwise_answers_explaination/T05_SQL_DDL_DML_Aggregates_Subqueries.md)
  - `T06`: [Exam-style T06](../Topicwise_answers_exam_style/T06_Joins_and_Views.md) · [Explanation T06](../Topicwise_answers_explaination/T06_Joins_and_Views.md)
  - `T07`: [Exam-style T07](../Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) · [Explanation T07](../Topicwise_answers_explaination/T07_Triggers_and_Stored_Procedures.md)
- **Key Concepts Solved:**
  - DDL & Integrity: `CREATE TABLE`, `CHECK`, `FOREIGN KEY ... ON DELETE CASCADE`, `ALTER TABLE`, domain constraints (Part 1).
  - DML Clauses: `ORDER BY`, string matching with `LIKE`, aggregate functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`), `GROUP BY`, and `HAVING` (Part 2).
  - Advanced Subqueries: Correlated subqueries, set membership (`IN`, `NOT IN`), set comparisons (`SOME`, `ALL`), existence tests (`EXISTS`, `NOT EXISTS`), unique tests (`UNIQUE`), and Recursive CTEs (`WITH RECURSIVE`) (Part 3).
  - Enterprise Queries: Bank schema (`customer`, `account`, `loan`, `depositor`, `borrower`) and Employee schema (`employee`, `works`, `company`, `manages`) complex queries (Part 4).
  - Joins & Views: Natural Join pitfalls, Outer Joins (Left $\mathbin{⟕}$, Right $\mathbin{⟖}$, Full $\mathbin{⟗}$), updatable views, and `WITH CHECK OPTION` (T06).
  - Triggers & Stored Procedures: Event-Condition-Action (ECA) model, `BEFORE` / `AFTER` triggers, cascading trigger control, SQL/PSM stored procedures and functions, JDBC connection and cursor management (T07).
- **Direct RUET Exam Linkage:**
  - SQL is the single highest-yield area in RUET exams: **130 final marks (20.4% total weight)** across all 7 finals.
  - **PE 3.4 / EX 3.14** (Employee-Company schema) is recycled in **2018 Q.3(a)**, **2020 Q.7(b)**, and **2024 Q.5(b)**.
  - Outer join queries mirror **2019 Q.3(b)**, **2020 Q.3(c)**, and **2024 Q.6(c)**.
  - Trigger implementations mirror **2017 Q.3(b)**, **2018 Q.4(a)**, **2020 Q.3(b)**, **2023 Q.4(c)**, and **2024 Q.6(a)**.

---

### Unit 5: Relational Database Design & Normalization
- **Exercise Documents:**
  - [`T08_Part1_FDs_and_Armstrong_Axioms.md`](T08_Part1_FDs_and_Armstrong_Axioms.md) (15 problems)
  - [`T08_Part2_Canonical_Cover_and_3NF.md`](T08_Part2_Canonical_Cover_and_3NF.md) (15 problems)
  - [`T08_Part3_BCNF_and_Advanced_Normalization.md`](T08_Part3_BCNF_and_Advanced_Normalization.md) (14 problems)
- **Companion Answers:** [Exam-style T08](../Topicwise_answers_exam_style/T08_Normalization_and_Functional_Dependencies.md) · [Explanation T08](../Topicwise_answers_explaination/T08_Normalization_and_Functional_Dependencies.md)
- **Key Concepts Solved:**
  - Functional Dependencies & Armstrong's Axioms: Formal mathematical proofs for Reflexivity, Augmentation, Transitivity, Union, Decomposition, and Pseudotransitivity (Part 1).
  - Attribute Closure ($X^+$) & Candidate Keys: Systematic closure algorithm, candidate key discovery drills, and prime vs non-prime attributes (Part 1 & 2).
  - Canonical Cover ($F_c$): Extraneous attribute elimination algorithm on LHS and RHS (Part 2).
  - 3NF Synthesis Algorithm: Preserving dependencies, lossless-join guarantee, and candidate key schema additions (Part 2).
  - BCNF Decomposition: Step-by-step BCNF tree decompositions, testing dependency preservation, and why BCNF may fail to preserve dependencies (Part 3).
  - Advanced Topics: 4NF multivalued dependencies (MVDs), denormalization performance trade-offs, and temporal database integrity (Part 3).
- **Direct RUET Exam Linkage:**
  - Normalization carries **75 final marks (11.8% curriculum share)** across all 7 finals and `CT-03`.
  - **PE 7.6** (Armstrong proof for Pseudotransitivity and Decomposition) is asked in **2021 Q.5(b)** and `CT-03 Q.1`.
  - **PE 7.7** (Canonical Cover derivation) is asked in **2021 Q.6(b)**.
  - Candidate key derivations and 3NF/BCNF decompositions mirror **2017 Q.4(a/b)**, **2018 Q.4(c)**, **2019 Q.5(b)**, **2020 Q.5(a/b)**, **2023 Q.6(a/b)**, and **2024 Q.7(a/b)**.

---

### Unit 6: Transaction Management & Concurrency Control
- **Exercise Documents:**
  - [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) (9 problems)
  - [`T10_Serializability.md`](T10_Serializability.md) (15 problems)
  - [`T11_Part1_Locking_Protocols.md`](T11_Part1_Locking_Protocols.md) (11 problems)
  - [`T11_Part2_2PL_and_Lock_Conversions.md`](T11_Part2_2PL_and_Lock_Conversions.md) (11 problems)
  - [`T11_Part3_Deadlock_and_Timestamp_Ordering.md`](T11_Part3_Deadlock_and_Timestamp_Ordering.md) (11 problems)
- **Companion Answers:**
  - `T09`: [Exam-style T09](../Topicwise_answers_exam_style/T09_Transactions_ACID_and_Anomalies.md) · [Explanation T09](../Topicwise_answers_explaination/T09_Transactions_ACID_and_Anomalies.md)
  - `T10`: [Exam-style T10](../Topicwise_answers_exam_style/T10_Serializability.md) · [Explanation T10](../Topicwise_answers_explaination/T10_Serializability.md)
  - `T11`: [Exam-style T11](../Topicwise_answers_exam_style/T11_Concurrency_Control_Protocols.md) · [Explanation T11](../Topicwise_answers_explaination/T11_Concurrency_Control_Protocols.md)
- **Key Concepts Solved:**
  - Transaction States & ACID Properties: Atomicity, Consistency, Isolation, Durability with banking scenarios; Transaction state transition diagrams (T09).
  - Concurrency Anomalies: Lost Update, Dirty Read, Unrepeatable Read, Phantom Phenomenon, and Incorrect Summary Problem mechanics (T09).
  - Serializability: Conflicting instructions, conflict serializability, precedence graphs, topological sorting, view serializability (3 conditions & blind writes), and recoverable vs cascadeless schedules (T10).
  - Locking Protocols: Shared/Exclusive locks, lock compatibility matrix, lock conversions (upgrade/downgrade), and starvation prevention (T11 Part 1).
  - Two-Phase Locking (2PL): Growing phase, shrinking phase, 2PL lock point theorem, Strict 2PL, Rigorous 2PL, and Tree protocol (T11 Part 2).
  - Deadlocks & Timestamp Ordering: Deadlock prevention (`wait-die`, `wound-wait`), wait-for graphs, victim selection, and Timestamp Ordering Protocol (TSO) read/write rules and Thomas' Write Rule (T11 Part 3).
- **Direct RUET Exam Linkage:**
  - Topics `T09`, `T10`, and `T11` together account for **129 final marks (20.2% curriculum weight)**.
  - **EX 17.14** (Serial vs Serializable) is asked in **2018 Q.6(a)**.
  - **EX 17.15** (Conditional increment schedules) is asked in **2017 Q.5(c)** and **2019 Q.4(a)**.
  - **PE 17.5** (View serializability) is asked in **2020 Q.6(b)**.
  - **PE 17.6** (Precedence graph testing) is asked in **2018 Q.6(c)**, **2020 Q.6(a)**, **2023 Q.8(b)**, and **2024 Q.8(c)**.
  - **PE 18.2** (2PL lock points) is asked in **2017 Q.7(a)**.
  - **EX 18.20** (Deadlock prevention `wait-die`/`wound-wait`) is asked in **2018 Q.5(b)**.
  - **EX 18.26** (TSO protocol & rollback timestamp rules) is asked in **2018 Q.6(b)** and **2024 Q.8(b)**.

---

### Unit 7: Recovery System & Storage / RAID
- **Exercise Documents:**
  - [`T12_Part1_Failure_Types_and_RAID_Intro.md`](T12_Part1_Failure_Types_and_RAID_Intro.md) (14 problems)
  - [`T12_Part2_Recovery_Manager_and_Log_Recovery.md`](T12_Part2_Recovery_Manager_and_Log_Recovery.md) (14 problems)
  - [`T12_Part3_Checkpoints_and_RAID_Levels.md`](T12_Part3_Checkpoints_and_RAID_Levels.md) (13 problems)
- **Companion Answers:** [Exam-style T12](../Topicwise_answers_exam_style/T12_Recovery_System_and_RAID.md) · [Explanation T12](../Topicwise_answers_explaination/T12_Recovery_System_and_RAID.md)
- **Key Concepts Solved:**
  - Failure Classifications: Transaction failure (logical error, internal abort), System crash (fail-stop assumption), Disk failure (head crash), Volatile vs Nonvolatile vs Stable storage (Part 1).
  - Log-Based Recovery & WAL: Write-Ahead Logging (WAL) rules, Deferred database modification, Immediate database modification, Redo-only vs Undo/Redo recovery, and Steal/No-Force buffer management (Part 2).
  - Recovery Algorithms: Concrete redo-pass and undo-pass log tracing, Compensation Log Records (CLRs), and the ARIES recovery algorithm (Analysis, Redo, Undo) (Part 2 & 3).
  - Checkpoints: Checkpoint records, fuzzy checkpoints, and active transaction list determination (Part 3).
  - RAID Systems: Complete mathematical formulas and trade-offs for RAID 0 (striping), RAID 1 (mirroring), RAID 10 (1+0), RAID 3 (bit parity), RAID 4 (block parity), RAID 5 (distributed parity), and RAID 6 (dual parity Reed-Solomon/P+Q) (Part 1 & 3).
- **Direct RUET Exam Linkage:**
  - Recovery & RAID carries **43 final marks (6.8% curriculum weight)** in 5/7 finals (`2017`, `2018`, `2019`, `2023`, `2024`).
  - **PE 17.1** (Deferred vs Immediate modification log tracing) is asked in **2018 Q.8(b)**.
  - RAID architectures and parity formulas mirror **2017 Q.7(b)**, **2019 Q.7(b)**, **2023 Q.7(b)**, and **2024 Q.7(c)**.

---

### Unit 8: Advanced DBMS: Security, Authorization, Indexing & Dynamic Hashing
- **Exercise Documents:**
  - [`T13_Part1_Security_and_Authorization_A.md`](T13_Part1_Security_and_Authorization_A.md) (15 problems)
  - [`T13_Part2_Security_and_Authorization_B.md`](T13_Part2_Security_and_Authorization_B.md) (14 problems)
  - [`T13_Part3_SQL_Injection_and_BTree_Indexing.md`](T13_Part3_SQL_Injection_and_BTree_Indexing.md) (15 problems)
  - [`T13_Part4_Indexing_and_Hashing.md`](T13_Part4_Indexing_and_Hashing.md) (13 problems)
- **Companion Answers:** [Exam-style T13](../Topicwise_answers_exam_style/T13_Security_Indexing_and_Hashing.md) · [Explanation T13](../Topicwise_answers_explaination/T13_Security_Indexing_and_Hashing.md)
- **Key Concepts Solved:**
  - Authorization & Access Control: `GRANT` and `REVOKE` statements, authorization graphs, cascading revocation rules, Role-Based Access Control (RBAC), and `REFERENCES` privilege restrictions (Part 1).
  - Advanced Governance: Row-level security via Virtual Private Database (VPD), non-monotonic authorization traps in outer joins, and trigger-based audit logging (Part 2).
  - Application Security & SQL Injection: Tautology attacks (`' OR '1'='1`), statement injection (`'; DROP TABLE`), and defenses using parameterized queries (`PreparedStatement`) (Part 3).
  - Indexing: Dense indices vs Sparse indices, primary (clustering) vs secondary (non-clustering) indices, multi-level indices (Part 3).
  - B+-Trees: Node structure (order $n$), search complexity, insertion with node splitting, deletion with borrowing and merging (Part 3).
  - Dynamic Hashing & Bitmap Indices: Extendible dynamic hashing with global and local depth directory expansion, bitmap indices and existence bitmap masks (Part 4).
- **Direct RUET Exam Linkage:**
  - **EX 9.16** (SQL Injection mechanisms and PreparedStatements) is asked in **2020 Q.4(a)** and **2021 Q.8(b)**.
  - Authorization privileges mirror **2017 Q.8(a)** and **2023 Q.8(c)**.
  - Indexing trade-offs and B+-tree derivations mirror **2017 Q.8(b)** and **2020 Q.8(a/b)**.

---

## 3. Fast Sequential Study Order & Navigation Flow

Follow this sequential reading roadmap to systematically conquer the entire Silberschatz 7e exercise bank from foundational concepts to advanced database engine internals:

| Step | Topic & Part | File Document Link | Previous Document | Next Document |
| :---: | :--- | :--- | :--- | :--- |
| **01** | `T01` DB Concepts & Architecture | [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) | *(Start of Bank)* | [`T02_Part1_ER_Modeling_Basics.md`](T02_Part1_ER_Modeling_Basics.md) |
| **02** | `T02` E-R Modeling (Part 1) | [`T02_Part1_ER_Modeling_Basics.md`](T02_Part1_ER_Modeling_Basics.md) | [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) | [`T02_Part2_ER_Scenarios_Reduction_EER.md`](T02_Part2_ER_Scenarios_Reduction_EER.md) |
| **03** | `T02` E-R Modeling (Part 2) | [`T02_Part2_ER_Scenarios_Reduction_EER.md`](T02_Part2_ER_Scenarios_Reduction_EER.md) | [`T02_Part1_ER_Modeling_Basics.md`](T02_Part1_ER_Modeling_Basics.md) | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) |
| **04** | `T03` Relational Model & Keys | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) | [`T02_Part2_ER_Scenarios_Reduction_EER.md`](T02_Part2_ER_Scenarios_Reduction_EER.md) | [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) |
| **05** | `T04` Relational Algebra & Calculus | [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) | [`T05_Part1_SQL_DDL_DML_Basics.md`](T05_Part1_SQL_DDL_DML_Basics.md) |
| **06** | `T05` SQL Basics (Part 1) | [`T05_Part1_SQL_DDL_DML_Basics.md`](T05_Part1_SQL_DDL_DML_Basics.md) | [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) | [`T05_Part2_SQL_Clauses_and_Aggregations.md`](T05_Part2_SQL_Clauses_and_Aggregations.md) |
| **07** | `T05` SQL Clauses (Part 2) | [`T05_Part2_SQL_Clauses_and_Aggregations.md`](T05_Part2_SQL_Clauses_and_Aggregations.md) | [`T05_Part1_SQL_DDL_DML_Basics.md`](T05_Part1_SQL_DDL_DML_Basics.md) | [`T05_Part3_SQL_Aggregations_and_Subqueries.md`](T05_Part3_SQL_Aggregations_and_Subqueries.md) |
| **08** | `T05` SQL Subqueries (Part 3) | [`T05_Part3_SQL_Aggregations_and_Subqueries.md`](T05_Part3_SQL_Aggregations_and_Subqueries.md) | [`T05_Part2_SQL_Clauses_and_Aggregations.md`](T05_Part2_SQL_Clauses_and_Aggregations.md) | [`T05_Part4_SQL_MultiTable_Business_Queries.md`](T05_Part4_SQL_MultiTable_Business_Queries.md) |
| **09** | `T05` SQL Enterprise (Part 4) | [`T05_Part4_SQL_MultiTable_Business_Queries.md`](T05_Part4_SQL_MultiTable_Business_Queries.md) | [`T05_Part3_SQL_Aggregations_and_Subqueries.md`](T05_Part3_SQL_Aggregations_and_Subqueries.md) | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) |
| **10** | `T06` Joins and Views | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) | [`T05_Part4_SQL_MultiTable_Business_Queries.md`](T05_Part4_SQL_MultiTable_Business_Queries.md) | [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) |
| **11** | `T07` Triggers & Procedures | [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) | [`T08_Part1_FDs_and_Armstrong_Axioms.md`](T08_Part1_FDs_and_Armstrong_Axioms.md) |
| **12** | `T08` Normalization (Part 1) | [`T08_Part1_FDs_and_Armstrong_Axioms.md`](T08_Part1_FDs_and_Armstrong_Axioms.md) | [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) | [`T08_Part2_Canonical_Cover_and_3NF.md`](T08_Part2_Canonical_Cover_and_3NF.md) |
| **13** | `T08` Normalization (Part 2) | [`T08_Part2_Canonical_Cover_and_3NF.md`](T08_Part2_Canonical_Cover_and_3NF.md) | [`T08_Part1_FDs_and_Armstrong_Axioms.md`](T08_Part1_FDs_and_Armstrong_Axioms.md) | [`T08_Part3_BCNF_and_Advanced_Normalization.md`](T08_Part3_BCNF_and_Advanced_Normalization.md) |
| **14** | `T08` Normalization (Part 3) | [`T08_Part3_BCNF_and_Advanced_Normalization.md`](T08_Part3_BCNF_and_Advanced_Normalization.md) | [`T08_Part2_Canonical_Cover_and_3NF.md`](T08_Part2_Canonical_Cover_and_3NF.md) | [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) |
| **15** | `T09` Transactions & ACID | [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) | [`T08_Part3_BCNF_and_Advanced_Normalization.md`](T08_Part3_BCNF_and_Advanced_Normalization.md) | [`T10_Serializability.md`](T10_Serializability.md) |
| **16** | `T10` Serializability | [`T10_Serializability.md`](T10_Serializability.md) | [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) | [`T11_Part1_Locking_Protocols.md`](T11_Part1_Locking_Protocols.md) |
| **17** | `T11` Locking Protocols (Part 1) | [`T11_Part1_Locking_Protocols.md`](T11_Part1_Locking_Protocols.md) | [`T10_Serializability.md`](T10_Serializability.md) | [`T11_Part2_2PL_and_Lock_Conversions.md`](T11_Part2_2PL_and_Lock_Conversions.md) |
| **18** | `T11` 2PL Mechanics (Part 2) | [`T11_Part2_2PL_and_Lock_Conversions.md`](T11_Part2_2PL_and_Lock_Conversions.md) | [`T11_Part1_Locking_Protocols.md`](T11_Part1_Locking_Protocols.md) | [`T11_Part3_Deadlock_and_Timestamp_Ordering.md`](T11_Part3_Deadlock_and_Timestamp_Ordering.md) |
| **19** | `T11` Deadlock & TSO (Part 3) | [`T11_Part3_Deadlock_and_Timestamp_Ordering.md`](T11_Part3_Deadlock_and_Timestamp_Ordering.md) | [`T11_Part2_2PL_and_Lock_Conversions.md`](T11_Part2_2PL_and_Lock_Conversions.md) | [`T12_Part1_Failure_Types_and_RAID_Intro.md`](T12_Part1_Failure_Types_and_RAID_Intro.md) |
| **20** | `T12` Recovery & Storage (Part 1) | [`T12_Part1_Failure_Types_and_RAID_Intro.md`](T12_Part1_Failure_Types_and_RAID_Intro.md) | [`T11_Part3_Deadlock_and_Timestamp_Ordering.md`](T11_Part3_Deadlock_and_Timestamp_Ordering.md) | [`T12_Part2_Recovery_Manager_and_Log_Recovery.md`](T12_Part2_Recovery_Manager_and_Log_Recovery.md) |
| **21** | `T12` Log Recovery (Part 2) | [`T12_Part2_Recovery_Manager_and_Log_Recovery.md`](T12_Part2_Recovery_Manager_and_Log_Recovery.md) | [`T12_Part1_Failure_Types_and_RAID_Intro.md`](T12_Part1_Failure_Types_and_RAID_Intro.md) | [`T12_Part3_Checkpoints_and_RAID_Levels.md`](T12_Part3_Checkpoints_and_RAID_Levels.md) |
| **22** | `T12` Checkpoints & RAID (Part 3) | [`T12_Part3_Checkpoints_and_RAID_Levels.md`](T12_Part3_Checkpoints_and_RAID_Levels.md) | [`T12_Part2_Recovery_Manager_and_Log_Recovery.md`](T12_Part2_Recovery_Manager_and_Log_Recovery.md) | [`T13_Part1_Security_and_Authorization_A.md`](T13_Part1_Security_and_Authorization_A.md) |
| **23** | `T13` Security Privileges (Part 1) | [`T13_Part1_Security_and_Authorization_A.md`](T13_Part1_Security_and_Authorization_A.md) | [`T12_Part3_Checkpoints_and_RAID_Levels.md`](T12_Part3_Checkpoints_and_RAID_Levels.md) | [`T13_Part2_Security_and_Authorization_B.md`](T13_Part2_Security_and_Authorization_B.md) |
| **24** | `T13` Access Control (Part 2) | [`T13_Part2_Security_and_Authorization_B.md`](T13_Part2_Security_and_Authorization_B.md) | [`T13_Part1_Security_and_Authorization_A.md`](T13_Part1_Security_and_Authorization_A.md) | [`T13_Part3_SQL_Injection_and_BTree_Indexing.md`](T13_Part3_SQL_Injection_and_BTree_Indexing.md) |
| **25** | `T13` SQLi & B+-Trees (Part 3) | [`T13_Part3_SQL_Injection_and_BTree_Indexing.md`](T13_Part3_SQL_Injection_and_BTree_Indexing.md) | [`T13_Part2_Security_and_Authorization_B.md`](T13_Part2_Security_and_Authorization_B.md) | [`T13_Part4_Indexing_and_Hashing.md`](T13_Part4_Indexing_and_Hashing.md) |
| **26** | `T13` Dynamic Hashing (Part 4) | [`T13_Part4_Indexing_and_Hashing.md`](T13_Part4_Indexing_and_Hashing.md) | [`T13_Part3_SQL_Injection_and_BTree_Indexing.md`](T13_Part3_SQL_Injection_and_BTree_Indexing.md) | *(End of Bank)* |

---
