# ECE 2215: Data Base Systems

- **Course Code**: ECE 2215
- **Course Title**: Data Base Systems
- **Credits**: 3.00

---

## 1. Official Syllabus

```text
ECE 2215: Data Base Systems Credits: 3.00
Concepts of database systems: Files and Databases, Database Management
Systems, Transaction management, Structure of a DBMS, Applications
Entity-Relationship concepts: Entity types, Entity set, Attribute and key,
Relationships, Relation types, Entity relationship, ER modeling, ER diagrams,
Database design using ER diagrams, Enhanced Entity-Relationship (EER) model
Normalization: Normal forms, Normalized Relations and Database performance,
De-normalization
Relational model: Structure of relational databases, Relational algebra, Relational
algebra operations, Modification of the database, Introduction to views, Pitfalls in
relational database design.
SQL: Data Definition Language, Data Manipulation Language, Basics of SQL,
Query designing in SQL using aggregate functions and nested queries, Embedded
SQL, Triggers, Procedures, Indexes, Declarative Constrains and Database Triggers
Concurrency control: Lock based protocols, Timestamp based protocols,
Validation based protocols, Deadlock.
Recovery system: Failure classification, Storage structure, Recovery and
atomicity, Log-based recovery, Recovery with concurrent transactions, Advanced
recovery techniques, RAID model.
Advanced database management systems: No SQL Systems, distributed systems,
object-oriented System, Temporal, Database Security, Data Warehousing and Data
Mining, Database Administration and Tuning.
```

---

## 2. Structured Topic Breakdown

### Unit 1: Concepts of Database Systems
- **Files vs. Databases**: Limitations of file-processing systems, advantages of DBMS
- **Database Management Systems (DBMS)**: Characteristics, levels of data abstraction, data independence (physical and logical)
- **Structure of a DBMS**: Storage manager, query processor components, database architecture
- **Transaction Management**: Overview of transactions, ACID properties
- **Applications**: Database users, administrator (DBA) roles, real-world applications

### Unit 2: Entity-Relationship (ER) Concepts & Modeling
- **Entities & Attributes**: Entity types, entity sets, attributes (simple/composite, single/multi-valued, derived), keys (super key, candidate key, primary key)
- **Relationships**: Relationship sets, relationship degrees, mapping cardinalities (1:1, 1:N, N:M), participation constraints (total, partial)
- **ER Modeling & Diagrams**: Visual notation, weak entity sets, role indicators
- **Database Design using ER Diagrams**: Conversion of ER schemas into relational tables
- **Enhanced Entity-Relationship (EER) Model**: Specialization, generalization, attribute inheritance, aggregation, category/union types

### Unit 3: Relational Model & Relational Algebra
- **Structure of Relational Databases**: Relations, tuples, attributes, schemas, domains, integrity constraints (entity integrity, referential integrity / foreign keys)
- **Relational Algebra**: Fundamental operations (Select $\sigma$, Project $\Pi$, Union $\cup$, Set Difference $-$, Cartesian Product $\times$, Rename $\rho$)
- **Additional Relational Algebra Operations**: Set intersection, natural join $\bowtie$, theta join, outer joins (left, right, full), division $\div$
- **Database Modification**: Insert, delete, and update operations via relational algebra
- **Views**: Concept, creation, virtual relations, view updates
- **Design Pitfalls**: Redundancy, update anomalies, deletion anomalies, insertion anomalies

### Unit 4: Structured Query Language (SQL)
- **Basics of SQL**: Syntax, data types, schema definition
- **Data Definition Language (DDL)**: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
- **Data Manipulation Language (DML)**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **Advanced Query Formulation**:
  - Aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
  - Grouping and filtering: `GROUP BY`, `HAVING`
  - Nested and correlated subqueries, set operations (`UNION`, `INTERSECT`, `EXCEPT`)
- **Integrity & Constraints**: Declarative constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `PRIMARY KEY`, `FOREIGN KEY` with cascade options)
- **Views & Indexes**: View definition and materialization; Index creation (`CREATE INDEX`) and performance implications
- **Procedural SQL**: Stored procedures, functions, and database triggers
- **Embedded SQL**: Host language integration, cursors, dynamic SQL

### Unit 5: Relational Database Design & Normalization
- **Purpose of Normalization**: Eliminating anomalies, preserving dependencies, lossless join decomposition
- **Functional Dependencies (FD)**: Definition, Armstrong's axioms, closure of attribute sets, canonical cover
- **Normal Forms**:
  - First Normal Form (1NF)
  - Second Normal Form (2NF)
  - Third Normal Form (3NF)
  - Boyce-Codd Normal Form (BCNF)
  - Higher normal forms overview (4NF, 5NF)
- **Database Performance & De-normalization**: Normalized relations vs. query performance, strategic trade-offs, controlled denormalization

### Unit 6: Transaction Management & Concurrency Control
- **Transactions**: Concept, transaction states, ACID properties (Atomicity, Consistency, Isolation, Durability)
- **Schedules & Serializability**: Conflict serializability, view serializability, precedence graphs
- **Concurrency Control Protocols**:
  - **Lock-based Protocols**: Shared and exclusive locks, Two-Phase Locking (2PL), Strict 2PL, Rigorous 2PL, multiple granularity locking
  - **Timestamp-based Protocols**: Thomas write rule, timestamp ordering
  - **Validation-based Protocols**: Optimistic concurrency control (Read, Validation, Write phases)
- **Deadlock Handling**: Deadlock prevention, detection (wait-for graph), recovery (victim selection, rollback, starvation)

### Unit 7: Database Recovery Systems
- **Failure Classification**: Transaction failures, system crashes, disk failures
- **Storage Structure**: Volatile, nonvolatile, and stable storage
- **Atomicity & Recovery**:
  - Log-based recovery (Write-Ahead Logging / WAL, immediate modification, deferred modification)
  - Checkpointing (fuzzy checkpointing, frequency)
  - Recovery algorithms (ARIES-style redo/undo passes)
- **Concurrent Transaction Recovery**: Log records, rollback handling under concurrency
- **Advanced Recovery & Storage**: Shadow paging, remote backup systems
- **RAID Architecture**: Redundant Arrays of Independent Disks (RAID 0, 1, 5, 6, 10), data striping, parity, reliability

### Unit 8: Advanced Database Management Systems
- **NoSQL Systems**: Key-value stores, document stores, column-family, graph databases, CAP theorem, eventual consistency
- **Distributed Database Systems**: Architecture, fragmentation, replication, distributed transactions, 2-phase commit (2PC)
- **Object-Oriented & Object-Relational Systems**: Complex types, inheritance, object identity, ODL/OQL
- **Temporal Databases**: Valid time, transaction time, bitemporal data
- **Database Security**: Authentication, discretionary access control (DAC / `GRANT`, `REVOKE`), role-based access control (RBAC), encryption, SQL injection prevention
- **Data Warehousing & Data Mining**: OLAP vs. OLTP, star/snowflake schemas, ETL pipelines, knowledge discovery
- **Database Administration & Tuning**: Physical database design, indexing strategies, query plan evaluation, buffer management tuning

---

## 3. Course Material & Textbook Mapping

### Primary Reference Textbook & Vault Resources
- **Title**: *Database System Concepts*, 7th Edition (2019)  
- **Authors**: Abraham Silberschatz, Henry F. Korth, S. Sudarshan  
- **Chapter Notes**: [`Textbook/`](Textbook/README.md)
- **Lecture Slides**: [`LectureSlides/`](LectureSlides/00_Index.md) (8 decks, 371 slides)
- **Student Class Notes**: [`Classnote_by_Raidah/`](Classnote_by_Raidah/README.md) (Roll 2310035) & [`Handnote_by_Fahim_2310002/`](Handnote_by_Fahim_2310002/README.md) (Roll 2310002)
- **Past Questions & Analytics**: [`PreviousYearQuestion/`](PreviousYearQuestion/README.md), [`ECE2215_PYQ_Analysis_Report.md`](ECE2215_PYQ_Analysis_Report.md), [`subtopicwise_list.md`](subtopicwise_list.md), and [`subtopicwise_questions.md`](subtopicwise_questions.md)
- **Solved Topic-wise Answer Banks**: [`Topicwise_answers_exam_style/`](Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) & [`Topicwise_answers_explaination/`](Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md)

### Alignment Matrix

| Syllabus Unit & Topic | Topic IDs | Lecture Slide Deck | Class Notes (Raidah · Fahim) | Textbook Notes (Silberschatz 7th Ed.) | Solved PYQ Answers (Exam-Style · Explanation) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Unit 1: Concepts of Database Systems** | `T01` | [01_Intro_to_Database_and_DBMS.md](LectureSlides/01_Intro_to_Database_and_DBMS.md) | [Raidah T01](Classnote_by_Raidah/T01_DB_Concepts_and_Architecture.md)<br>[Fahim T01](Handnote_by_Fahim_2310002/T01_DB_Concepts_and_Architecture.md) | [Chapter 01 - Introduction.md](Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md) | [Exam T01](Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) · [Expl T01](Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md) |
| **Unit 2: Entity-Relationship (ER & EER)** | `T02` | [05_ER_Model.md](LectureSlides/05_ER_Model.md) | [Raidah T02](Classnote_by_Raidah/T02_ER_and_EER_Modeling.md)<br>[Fahim T02](Handnote_by_Fahim_2310002/T02_ER_and_EER_Modeling.md) | [Chapter 06 - Database Design Using the E-R Model.md](Textbook/Chapter_06_ER_Model/Chapter%2006%20-%20Database%20Design%20Using%20the%20E-R%20Model.md) | [Exam T02](Topicwise_answers_exam_style/T02_ER_and_EER_Modeling.md) · [Expl T02](Topicwise_answers_explaination/T02_ER_and_EER_Modeling.md) |
| **Unit 3: Relational Model & Algebra** | `T03`, `T04` | [02_Relational_Model.md](LectureSlides/02_Relational_Model.md) | [Raidah T03](Classnote_by_Raidah/T03_Relational_Model_Keys_and_Integrity.md), [T04](Classnote_by_Raidah/T04_Relational_Algebra_and_Calculus.md)<br>[Fahim T03](Handnote_by_Fahim_2310002/T03_Relational_Model_Keys_and_Integrity.md) | [Chapter 02 - Introduction to the Relational Model.md](Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)<br>[Chapter 16 - Query Optimization.md](Textbook/Chapter_16_Query_Optimization/Chapter%2016%20-%20Query%20Optimization.md) *(§16.1 $\gamma$)* | [Exam T03](Topicwise_answers_exam_style/T03_Relational_Model_Keys_and_Integrity.md), [T04](Topicwise_answers_exam_style/T04_Relational_Algebra_and_Calculus.md) · [Expl T03](Topicwise_answers_explaination/T03_Relational_Model_Keys_and_Integrity.md), [T04](Topicwise_answers_explaination/T04_Relational_Algebra_and_Calculus.md) |
| **Unit 4: SQL (Basics, Queries, Joins, Views, Triggers, Procedures)** | `T05`, `T06`, `T07` | [03_Introduction_to_SQL.md](LectureSlides/03_Introduction_to_SQL.md)<br>[04_Joining_and_Views.md](LectureSlides/04_Joining_and_Views.md) | [Raidah T05](Classnote_by_Raidah/T05_SQL_DDL_DML_Aggregates_Subqueries.md), [T06](Classnote_by_Raidah/T06_Joins_and_Views.md)<br>[Fahim T05](Handnote_by_Fahim_2310002/T05_SQL_DDL_DML_Aggregates_Subqueries.md), [T06](Handnote_by_Fahim_2310002/T06_Joins_and_Views.md), [T07](Handnote_by_Fahim_2310002/T07_Triggers_and_Stored_Procedures.md) | [Chapter 03 - Introduction to SQL.md](Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md)<br>[Chapter 04 - Intermediate SQL.md](Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md)<br>[Chapter 05 - Advanced SQL.md](Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md) | [Exam T05](Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md), [T06](Topicwise_answers_exam_style/T06_Joins_and_Views.md), [T07](Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) · [Expl T05](Topicwise_answers_explaination/T05_SQL_DDL_DML_Aggregates_Subqueries.md), [T06](Topicwise_answers_explaination/T06_Joins_and_Views.md), [T07](Topicwise_answers_explaination/T07_Triggers_and_Stored_Procedures.md) |
| **Unit 5: Relational Design & Normalization** | `T08` | [06_DBMS_Normalization.md](LectureSlides/06_DBMS_Normalization.md) | [Raidah T08](Classnote_by_Raidah/T08_Normalization_and_FDs.md) | [Chapter 07 - Relational Database Design.md](Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md) | [Exam T08](Topicwise_answers_exam_style/T08_Normalization_and_Functional_Dependencies.md) · [Expl T08](Topicwise_answers_explaination/T08_Normalization_and_Functional_Dependencies.md) |
| **Unit 6: Transactions & Concurrency Control** | `T09`, `T10`, `T11` | [07_Transactions.md](LectureSlides/07_Transactions.md)<br>[08_Concurrency_Control_Mechanisms.md](LectureSlides/08_Concurrency_Control_Mechanisms.md) | [Raidah T09](Classnote_by_Raidah/T09_Transactions_ACID_and_Anomalies.md), [T10](Classnote_by_Raidah/T10_Serializability.md), [T11](Classnote_by_Raidah/T11_Concurrency_Control_Protocols.md) | [Chapter 17 - Transactions.md](Textbook/Chapter_17_Transactions/Chapter%2017%20-%20Transactions.md)<br>[Chapter 18 - Concurrency Control.md](Textbook/Chapter_18_Concurrency_Control/Chapter%2018%20-%20Concurrency%20Control.md) | [Exam T09](Topicwise_answers_exam_style/T09_Transactions_ACID_and_Anomalies.md), [T10](Topicwise_answers_exam_style/T10_Serializability.md), [T11](Topicwise_answers_exam_style/T11_Concurrency_Control_Protocols.md) · [Expl T09](Topicwise_answers_explaination/T09_Transactions_ACID_and_Anomalies.md), [T10](Topicwise_answers_explaination/T10_Serializability.md), [T11](Topicwise_answers_explaination/T11_Concurrency_Control_Protocols.md) |
| **Unit 7: Recovery System & Storage** | `T12` | *(Refer to Textbook & Class Notes)* | [Raidah T12](Classnote_by_Raidah/T12_Recovery_and_RAID.md) *(RAID)* | [Chapter 19 - Recovery System.md](Textbook/Chapter_19_Recovery_System/Chapter%2019%20-%20Recovery%20System.md)<br>[Chapter 12 - Physical Storage Systems.md](Textbook/Chapter_12_Physical_Storage/Chapter%2012%20-%20Physical%20Storage%20Systems.md) *(§12.5 RAID)* | [Exam T12](Topicwise_answers_exam_style/T12_Recovery_System_and_RAID.md) · [Expl T12](Topicwise_answers_explaination/T12_Recovery_System_and_RAID.md) |
| **Unit 8: Advanced Database Systems** | `T13` | *(Refer to Textbook)* | *(Refer to Textbook)* | [Chapter 09 - Application Development.md](Textbook/Chapter_09_App_Development/Chapter%2009%20-%20Application%20Development.md) *(§9.8 Security)*<br>[Chapter 14 - Indexing.md](Textbook/Chapter_14_Indexing/Chapter%2014%20-%20Indexing.md)<br>[Chapter 10 - Big Data.md](Textbook/Chapter_10_Big_Data/Chapter%2010%20-%20Big%20Data.md)<br>[Chapter 11 - Data Analytics.md](Textbook/Chapter_11_Data_Analytics/Chapter%2011%20-%20Data%20Analytics.md)<br>[Chapter 20 - Database-System Architectures.md](Textbook/Chapter_20_Architectures/Chapter%2020%20-%20Database-System%20Architectures.md)<br>[Chapter 21 - Parallel and Distributed Storage.md](Textbook/Chapter_21_Distributed_Storage/Chapter%2021%20-%20Parallel%20and%20Distributed%20Storage.md)<br>[Chapter 22 - Parallel and Distributed Query Processing.md](Textbook/Chapter_22_Distributed_Query/Chapter%2022%20-%20Parallel%20and%20Distributed%20Query%20Processing.md)<br>[Chapter 23 - Parallel and Distributed Transaction Processing.md](Textbook/Chapter_23_Distributed_Transactions/Chapter%2023%20-%20Parallel%20and%20Distributed%20Transaction%20Processing.md) | [Exam T13](Topicwise_answers_exam_style/T13_Security_Indexing_and_Hashing.md) · [Expl T13](Topicwise_answers_explaination/T13_Security_Indexing_and_Hashing.md) |
