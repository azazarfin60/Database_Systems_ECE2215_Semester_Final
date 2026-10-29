# Previous Year Questions

Frozen source files: 7 semester-final papers (2017 to 2024) and 1 class-test collection.

These files serve as the verbatim, gold-standard reference archive for the course **ECE 2215: Database Systems** at Rajshahi University of Engineering & Technology (RUET).

---

## Contents

| File | What it holds |
| :--- | :--- |
| [`2017.md`](2017.md) | Pre-OBE semester-final paper (72 Marks). File system vs DBMS, E-R modeling, relational algebra, SQL DDL/DML, normalization up to 3NF, 2PL, log-based recovery, hashing, and database security triggers. |
| [`2018.md`](2018.md) | Pre-OBE semester-final paper (72 Marks). Aggregation, ternary E-R, relational algebra on insurance schema, 1NF/2NF, concurrency problems, deadlock, timestamp rollback, conflict serializability schedule, SQL queries, and RAID levels. |
| [`2019.md`](2019.md) | Pre-OBE semester-final paper (72 Marks). Data abstraction, railway ticketing E-R diagram, relational algebra on Covid patient database, 1NF/2NF, serializable schedule execution, SQL queries, and CGPA calculation formula. |
| [`2020.md`](2020.md) | Pre-OBE semester-final paper (72 Marks). 2-tier vs 3-tier architecture, vaccine database relational algebra, SQL injection, domain relational calculus ($\pi, \cup, \cap$), natural/outer joins table operations, transaction lifecycle, view serializability, and 3NF normalization table. |
| [`2021.md`](2021.md) | Transitional OBE paper (72 Marks, CLO mapped). DBA roles, referential integrity in MySQL, relational algebra with joins, candidate keys, canonical cover, functional dependencies closure, conflict serializability, wait-for-graph cycle diagram, and SQL injection. |
| [`2023.md`](2023.md) | Modern OBE paper (60 Marks, CLO mapped). RUET Central Library E-R diagram, table conversion to 3NF, SQL DDL/DML, candidate/super keys, RAID models, SQL VIEWs, Stored Procedures, Triggers, log-based recovery, and Timestamp Ordering schedules. |
| [`2024.md`](2024.md) | Modern OBE paper (60 Marks, CO mapped). RUET student database E-R, courier tracking file vs DBMS, SQL aggregation, security breach triggers, relational algebra multiple projects, inner vs outer joins, MySQL queries, ACID properties, RAID levels, and conflict serializability testing. |
| [`ClassTestQuestions.md`](ClassTestQuestions.md) | Class Test Collection (4 Tests, 20 Marks each): CT-01 (Data Abstraction, Schema Diagram, Application Structure, Relational Algebra), CT-02 (SQL Queries, Average CGPA, ER Modeling), CT-03 (Candidate Keys, Prime/Non-Prime Attributes, Normalization 1NF–BCNF), CT-04 (ACID Properties, Serial vs Concurrent, Conflict Serializability Schedule). |

---

## Paper Coverage & Curriculum Evolution

| Era | Years Covered | Course Code & Title | Section A | Section B | Full Marks |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Pre-OBE** | 2017 – 2020 | ECE 2215: Database Systems | Introduction, File vs DBMS, E-R Modeling, Relational Algebra, SQL Queries | Normalization (1NF–3NF), Transaction Processing, Concurrency Control (2PL, Timestamp), Recovery, Security | 72 |
| **Transitional OBE** | 2021 | ECE 2215: Data Base Systems | File Processing vs DBMS, Relational Algebra, E-commerce SQL, Keys & Attributes | ER Diagrams, Functional Dependencies, Canonical Cover, Serializability, Wait-For-Graph, Deadlock | 72 |
| **Modern OBE** | 2023 – 2024 | ECE 2215: Database Systems | Introduction, E-R Diagrams, Normalization (1NF–3NF), SQL DDL/DML, Joins (Natural & Outer) | Subqueries, Views, Triggers, Stored Procedures, Transactions (ACID), Concurrency Schedules, RAID Levels | 60 |

---

## Total Question Count

- **Semester Final Papers:** 148 sub-questions / lettered parts across 7 examination papers (56 main questions):
  - `2017.md`: 21 sub-questions
  - `2018.md`: 23 sub-questions
  - `2019.md`: 19 sub-questions
  - `2020.md`: 20 sub-questions
  - `2021.md`: 21 sub-questions
  - `2023.md`: 22 sub-questions
  - `2024.md`: 22 sub-questions
- **Class Tests:** 15 main questions (26 distinct question parts) across 4 class tests:
  - CT-01: 5 main questions (9 distinct items: Q1–Q3 standalone, Q4 with 4 relational algebra queries, Q5 with 2 expression descriptions)
  - CT-02: 2 main questions (6 parts: Q1 with parts a–d, Q2 with parts a–b)
  - CT-03: 4 main questions (7 parts: Q1 with parts a–d, Q2–Q4 standalone)
  - CT-04: 4 main questions (4 parts: Q1–Q4 standalone)
- **Grand Total:** 174 questions / parts fully digitized, audited, and verified verbatim with 100% precision.

---

## High-Frequency Core Topics (637 Printed Final Marks + 80 CT Marks)

| Topic ID & Name | Final Marks (Share) | Repeated Occurrences Across Finals & CTs |
| :--- | :---: | :--- |
| **`T05` SQL Queries (DDL, DML, Aggregates, Subqueries)** | 130 (`20.4%`) | Appeared in all 7 final papers (7/7) and CT-02 |
| **`T08` Normalization & Functional Dependencies (1NF–BCNF, $X^+$, $F_c$)** | 75 (`11.8%`) | Appeared in all 7 final papers (7/7) and CT-03 |
| **`T02` E-R & EER Modeling & Schema Reduction** | 67 (`10.5%`) | Appeared in all 7 final papers (7/7) and CT-02 |
| **`T10` Conflict & View Serializability (Precedence Graphs)** | 51 (`8.0%`) | Appeared in all 7 final papers (7/7) and CT-04 |
| **`T04` Relational Algebra ($\sigma, \Pi/\pi, \bowtie, \rho, -, \cup, \gamma$) & Calculus** | 48 (`7.5%`) | Appeared in 6 of 7 final papers (all except 2023) and CT-01 |
| **`T01` DB Concepts & Architecture (File vs. DBMS, DBA, Abstraction)** | 44 (`6.9%`) | Appeared in all 7 final papers (7/7) and CT-01 |
| **`T12` Database Recovery (Failures, WAL, Shadow Paging) & RAID** | 43 (`6.8%`) | Appeared in 5 of 7 final papers (2017, 2018, 2019, 2023, 2024) |
| **`T09` Transaction ACID Properties, States & Anomalies** | 41 (`6.4%`) | Appeared in all 7 final papers (7/7) and CT-04 |
| **`T11` Concurrency Control Protocols (2PL, Deadlock, TSO)** | 37 (`5.8%`) | Appeared in 6 of 7 final papers (all except 2019) |
| **`T03` Relational Model, Keys & Referential Integrity** | 28 (`4.4%`) | Appeared in 5 of 7 final papers (2018–2023) and CT-01 |
| **`T06` SQL Joins (Inner, Natural, Outer) & Views** | 28 (`4.4%`) | Appeared in 4 of 7 final papers (2019, 2020, 2023, 2024) |
| **`T07` Database Triggers & Stored Procedures** | 27 (`4.2%`) | Appeared in 5 of 7 final papers (2017, 2018, 2020, 2023, 2024) |
| **`T13` Security (SQL Injection), Indexing & Hashing** | 18 (`2.8%`) | Appeared in 4 of 7 final papers (2017, 2020, 2021, 2023) |

---

## Companion Analytics, Question Bank & Solved Answers

- **Statistical Analysis Report:** [`ECE2215_PYQ_Analysis_Report.md`](../ECE2215_PYQ_Analysis_Report.md) — era comparisons, recycled question chains, Silberschatz exercise mappings, and slide-vs.-textbook coverage.
- **Subtopic Weightage & Flow (`T01`–`T13`):** [`subtopicwise_list.md`](../subtopicwise_list.md) — 13 topics and 77 subtopics ranked by exam weight.
- **Subtopic-wise Verbatim Question Bank:** [`subtopicwise_questions.md`](../subtopicwise_questions.md) — all 148 final sub-questions and 26 CT parts sorted into `T01.1`–`T13.4`.
- **Solved Answer Banks:**
  - **Exam-Style Layer:** [`Topicwise_answers_exam_style/`](../Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) (`T01`–`T13`)
  - **Explanation Layer:** [`Topicwise_answers_explaination/`](../Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md) (`T01`–`T13`)
