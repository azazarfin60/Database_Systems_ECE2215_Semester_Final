# ECE 2215: Database Systems — Curated YouTube Learning Guide

A comprehensive, topic-by-topic directory of the highest-rated YouTube playlists, specialized lecture series, and standout single videos for **ECE 2215: Database Systems** at RUET (aligned with Silberschatz, Korth & Sudarshan, *Database System Concepts*, 7th Edition).

---

## 1. Curated Learning Paths

Depending on your study goal, choose the path that fits best:

| Path | Primary Goal | Recommended Channels / Instructors | Key Advantage |
| :--- | :--- | :--- | :--- |
| **Path A: Exam-Cram & Mark Maximizer** | Semester final exam clearance, step-by-step algorithms, short tricks | **Gate Smashers** (Varun Singla)<br>**Knowledge Gate** (Sanchit Jain) | Concise chalk-talks, exam-pattern matching, solved numerical problems. |
| **Path B: Deep Rigor & Problem Solving** | Tricky derivations, mathematical proofs, GATE CSE level depth | **Amit Khurana** (GATE CSE) | Deepest treatment of Relational Algebra, Functional Dependencies, and Normalization. |
| **Path C: Formal Textbook Alignment** | 1:1 match with Silberschatz 7e curriculum and definitions | **NPTEL** (Prof. Partha Pratim Das, IIT Kharagpur)<br>**Stanford University** (Prof. Jennifer Widom) | Rigorous academic standards, formal proofs, and textbook-exact terminology. |
| **Path D: Systems Engineering & Practical Internals** | How DBMS engines really work (storage engines, B+ trees, WAL, sharding) | **CMU 15-445/645** (Prof. Andy Pavlo)<br>**Hussein Nasser**<br>**ByteByteGo** | Industry-grade systems knowledge, execution engines, physical layout. |

---

## 2. The 5 Foundational Full-Course Playlists

### 1. [Gate Smashers — DBMS Complete Playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y)
- **Instructor:** Varun Singla
- **Why it's essential:** The undisputed #1 choice for South Asian engineering exams. Fast-paced, high retention, and focuses heavily on exam traps.
- **Companion Playlist:** [Gate Smashers — Dedicated SQL Playlist](https://www.youtube.com/playlist?list=PLxCzCOWd7aiHqU4HKL7-SITyuSIcD93id) (covers DDL, DML, Subqueries, Joins, and Views).

### 2. [Amit Khurana — Databases (DBMS) for GATE](https://www.youtube.com/playlist?list=PLC36xJgs4dxGcz7nZaxGxxmbJrcgDXhFk)
- **Instructor:** Amit Khurana
- **Why it's essential:** Over 200 lectures covering every corner of database theory. If a concept seems confusing or mathematically ambiguous elsewhere, his derivations make it crystal clear.

### 3. [NPTEL — Database Management System](https://youtube.com/playlist?list=PLZSMY6R71lx4aLOGYRYXWk2xCT_zJS_aZ)
- **Instructor:** Prof. Partha Pratim Das (IIT Kharagpur)
- **Why it's essential:** Taught directly following the Silberschatz textbook structure. Perfect when you need to cite formal academic definitions or follow lecture slide progressions.

### 4. [Stanford University — Introduction to Databases](https://www.youtube.com/playlist?list=PLroEs25KGvwzmvIxYHRhoGTz9w8LeXek0)
- **Instructor:** Prof. Jennifer Widom (Stanford University)
- **Why it's essential:** Legendary computer science course covering relational design theory, functional dependencies, multi-valued dependencies, and declarative query optimization.

### 5. [CMU 15-445/645 — Intro to Database Systems](https://www.youtube.com/@CMUDatabaseGroup/playlists)
- **Instructor:** Prof. Andy Pavlo (Carnegie Mellon University)
- **Why it's essential:** World standard for understanding database internals: buffer pool managers, hash tables, dynamic B+ trees, query execution iterators, concurrency control, and ARIES recovery.

---

## 3. Syllabus Topic-by-Topic Breakdown (Playlists & Standout Single Videos)

### Unit 1: Concepts of Database Systems (Topic `T01`)
*Covers: File processing limitations, 3-tier architecture, data abstraction levels, data independence, DBA roles.*

- **Core Lectures:**
  - **Gate Smashers (Lec 1–8):**
    - `Lec-1:` File System vs. DBMS.
    - `Lec-2:` 3 Schema Architecture & Levels of Data Abstraction (Internal, Conceptual, External).
    - `Lec-3:` Physical vs. Logical Data Independence.
    - `Lec-7 & 8:` 2-Tier vs. 3-Tier Client-Server Architecture.
- **Standout Video on Architecture & Real-World Systems:**
  - **ByteByteGo — YouTube Architecture Breakdown:** Search `ByteByteGo "Design YouTube"` (Directly explains the Silberschatz Exercise 1.4 question: why raw video blobs belong on Object Storage/CDNs while metadata lives in Relational/Document DBMS).

---

### Unit 2: Entity-Relationship & EER Modeling (Topic `T02`)
*Covers: Entity sets, relationship cardinalities (1:1, 1:N, M:N), participation constraints, weak entities, ER reduction to tables, specialization/generalization, aggregation.*

- **Core Playlist:** [Jenny's Lectures DBMS Series](https://www.youtube.com/playlist?list=PLdo5W4Nhv31b33kF46f9aFjoJPOkdlsRc) & Gate Smashers (Lec 12–25).
- **High-Yield Standout Videos (Repeated Exam Questions):**
  - **ER Diagram to Relational Tables (Crucial — 24 Exam Marks):**  
    Search: `Gate Smashers "Converting ER Diagram to Relational Tables"`  
    *Covers how to reduce 1:1, 1:N, M:N relationships, weak entities, and multivalued attributes without data loss or redundant tables.*
  - **Weak Entity Sets & Identifying Relationships:**  
    Search: `Gate Smashers "Lec-17: Weak Entity Set in DBMS"`.
  - **Specialization, Generalization & Aggregation (EER):**  
    Search: `Gate Smashers "Lec-24: Specialization and Generalization in DBMS"`.

---

### Unit 3: Relational Model, Keys & Relational Algebra (Topics `T03` & `T04`)
*Covers: Keys (Candidate, Primary, Super, Foreign), Integrity constraints, Relational Algebra fundamental & additional operators, Division ($\div$), Aggregation ($\gamma$), Tuple & Domain Relational Calculus.*

- **Core Playlist:** [Amit Khurana — Relational Algebra](https://www.youtube.com/playlist?list=PLC36xJgs4dxGcz7nZaxGxxmbJrcgDXhFk)
- **Standout Single Videos:**
  - **Understanding All Database Keys:**  
    Search: `Gate Smashers "Lec-9: What is CANDIDATE KEY and PRIMARY key | DBMS"`  
    *(Also check Decomplexify: "Database Keys Explained")*.
  - **Relational Algebra Operators:**  
    Search: `Gate Smashers "Relational Algebra in DBMS | Operations with Solved Examples"`.
  - **The Relational Division Operator ($\div$):**  
    Search: `Amit Khurana "Division Operator in Relational Algebra"`  
    *Explains how $\div$ answers "find all students who took EVERY course offered by the department".*
  - **Tuple Relational Calculus (TRC) vs Domain Relational Calculus (DRC):**  
    Search: `Amit Khurana "Tuple Relational Calculus TRC in DBMS"`.

---

### Unit 4: Structured Query Language (SQL), Joins & Views (Topics `T05` & `T06`)
*Covers: DDL/DML, GROUP BY, HAVING, Correlated subqueries, Inner/Outer Joins, Updatable Views, Materialized Views.*

- **Comprehensive Practical Course:**
  - **Harvard CS50's Intro to Databases with SQL (Carter Zenke):**  
    Available on [freeCodeCamp YouTube](https://www.youtube.com/watch?v=vPW0fG_Y45c) (Full 6-hour university masterclass from basic `SELECT` to multi-table joins, subqueries, and indexing).
- **Exam-Specific Standout Videos:**
  - **Correlated Subqueries vs. Simple Nested Subqueries:**  
    Search: `Gate Smashers "Correlated Subquery in SQL"`.
  - **All Types of Joins Visualized:**  
    Search: `Gate Smashers "Joins in DBMS | Inner, Left Outer, Right Outer, Full Outer"`.
  - **Views & Updatable Views:**  
    Search: `Gate Smashers "Views in SQL | Updatable and Read-Only Views"`.

---

### Unit 5: Triggers & Stored Procedures (Topic `T07`)
*Covers: Event-Condition-Action (ECA) model, BEFORE/AFTER triggers, Statement vs. Row-level, `:NEW` and `:OLD` qualifiers, Stored Procedures with IN/OUT parameters.*

- **Top Series:** [kudvenkat — SQL Server Video Tutorials](https://www.youtube.com/user/kudvenkat/playlists)
- **Standout Single Videos:**
  - **Stored Procedures with Parameters:**  
    Search: `kudvenkat "Part 18 - Stored Procedures in SQL Server"`.
  - **Database Triggers (DML, After, Instead Of):**  
    Search: `kudvenkat "Part 43 - Triggers in SQL Server"` & `Part 44 - After Update Trigger`.
  - **Conceptual Overview & Real-Life Use Cases:**  
    Search: `Gate Smashers "SQL Triggers with Real-Life Examples"`.

---

### Unit 6: Relational Database Design & Normalization (Topic `T08`)
*The highest-weight exam section (75 marks across RUET past papers). Covers: FDs, Armstrong's Axioms, Attribute Closure, Candidate Keys, 1NF, 2NF, 3NF, BCNF, Canonical Cover ($F_c$), Lossless Join Decomposition, Dependency Preservation.*

- **Top Concept Series:**
  - **Decomplexify — Learn Database Normalization (1NF, 2NF, 3NF, 4NF, 5NF):**  
    Search: `Decomplexify "Learn Database Normalization"` (The cleanest, most intuitive visual walk-through of insertion, deletion, and update anomalies).
- **High-Yield Algorithmic Standout Videos:**
  1. **Finding Candidate Keys Shortcut (Attribute Closure $X^+$):**  
     Search: `Gate Smashers "How to find Candidate Key in DBMS | Shortcut trick"`.
  2. **Canonical Cover / Minimal Cover ($F_c$):**  
     Search: `Gate Smashers "Lec-34: Minimal Cover in DBMS With Example | Canonical cover"`.
  3. **Lossless Join Decomposition Property ($R_1 \cap R_2 \to R_1$ or $R_2$):**  
     Search: `Gate Smashers "Lec-46: Lossless Join Decomposition with Example"`.
  4. **Dependency Preservation Decomposition:**  
     Search: `Gate Smashers "Lec-45: Dependency Preserving Decomposition"`.
  5. **3NF vs. BCNF Decomposition Algorithms:**  
     Search: `Knowledge Gate "BCNF Decomposition in DBMS with Examples"`.

---

### Unit 7: Transactions & Concurrency Control (Topics `T09`, `T10`, `T11`)
*Covers: ACID properties, Transaction states, Concurrency anomalies, Conflict serializability, View serializability, Precedence Graph, 2PL, Strict/Rigorous 2PL, Timestamp Ordering (TSO), Thomas' Write Rule, Deadlock handling.*

- **Standout Conceptual Videos:**
  - **ACID Explained with Practical DB Examples:**  
    Search: `Hussein Nasser "Relational Database ACID Transactions Explained by Example"`.
  - **Concurrency Anomalies (Dirty Read, Non-Repeatable Read, Phantom Read):**  
    Search: `Gate Smashers "Lec-92: Concurrency Problems in DBMS"`.
- **Exam Testing Standout Videos:**
  - **Conflict Serializability & Precedence Graph Cycle Test:**  
    Search: `Gate Smashers "Lec-98: Conflict Serializability | Precedence Graph | Transaction"`.
  - **View Serializability & Blind Writes:**  
    Search: `Gate Smashers "Lec-100: View Serializability in DBMS"`.
  - **Two-Phase Locking (2PL, Strict 2PL, Rigorous 2PL):**  
    Search: `Gate Smashers "Lec-104: Two Phase Locking Protocol (2PL)"`.
  - **Deadlock Handling (Wait-Die vs. Wound-Wait):**  
    Search: `Gate Smashers "Deadlock Prevention in DBMS | Wait-Die & Wound-Wait"`.
  - **Timestamp Ordering (TSO) & Thomas' Write Rule:**  
    Search: `Gate Smashers "Lec-109: Timestamp Ordering Protocol"` & `Amit Khurana "Thomas Write Rule in DBMS"`.

---

### Unit 8: Database Recovery System & RAID Architecture (Topic `T12`)
*Covers: Failure classifications, Write-Ahead Logging (WAL), Deferred vs. Immediate modification, Checkpoints (Active transaction lists, Undo/Redo), Shadow Paging, RAID levels 0, 1, 5, 6, 10.*

- **Standout Recovery Videos:**
  - **Log-Based Recovery (Immediate vs. Deferred Modification):**  
    Search: `Gate Smashers "Lec-112: Log Based Recovery in DBMS"`.
  - **Checkpoints Recovery (Undo & Redo Lists Step-by-Step):**  
    Search: `Gate Smashers "Lec-113: Recovery with Concurrent Transactions (Checkpoints)"`.
  - **Advanced Recovery: ARIES Algorithm:**  
    Search: `CMU 15-445 "Lecture 20: Database Crash Recovery (ARIES)"` (By Prof. Andy Pavlo).
- **Standout RAID Storage Videos:**
  - **RAID 0, 1, 5, and 10 Animated:**  
    Search: `PowerCert Animated Videos "What is RAID 0, 1, 5, & 10?"` (The best 7-minute animation explaining data striping, mirroring, and distributed parity).
  - **RAID 5 vs. RAID 6 (Dual Parity Fault Tolerance):**  
    Search: `PowerCert Animated Videos "RAID 5 vs RAID 6"`.

---

### Unit 9: Indexing, Storage & Security (Topic `T13`)
*Covers: Dense vs. Sparse indexing, B-Trees and B+ Trees (insertion/splitting/deletion), Hashing (Static & Dynamic), SQL Injection prevention.*

- **Standout B-Tree & B+ Tree Videos:**
  - **B-Trees and B+ Trees in Databases (Why & How):**  
    Search: `Abdul Bari "10.2 B Trees and B+ Trees. How they are useful in Databases"` (Masterclass in understanding disk block sizing, search fanout, and leaf-node linking).
  - **B+ Tree Insertion & Splitting Algorithm:**  
    Search: `Abdul Bari "B+ Tree insertion and deletion"` or `Gate Smashers "B+ Tree in DBMS with Example"`.
- **Database Indexing Internals:**
  - **Indexing Explained:**  
    Search: `Hussein Nasser "Database Indexing Explained (with PostgreSQL)"`.
  - **Dense vs. Sparse Indexing:**  
    Search: `Gate Smashers "Indexing in DBMS | Primary, Secondary, Clustering, Dense & Sparse"`.
- **Database Security & SQL Injection:**
  - **Live Demonstration of SQL Injection:**  
    Search: `Computerphile "Running an SQL Injection Attack"` (Dr. Mike Pound demonstrates how `' OR 1=1 --` bypasses authentication and how parameterized queries/prepared statements block it).

---

## 4. Rapid Revision / Night-Before-Exam Options

If you have less than 24 hours before your semester final or class test:

1. **[Knowledge Gate — DBMS in One Shot (Sanchit Jain)](https://youtu.be/YRnjGeQbsHQ):**  
   A structured 6–8 hour marathon covering every standard university topic in sequential order.
2. **Gate Smashers DBMS Revision Marathon:**  
   Focuses on solving numerical questions (finding candidate keys, checking 3NF/BCNF, precedence graphs for conflict serializability, and 2PL schedules).
3. **Decomplexify (Speed Review):**  
   Watch their 3 short videos on *Normalization*, *ER Diagrams*, and *Database Keys* to cement intuitive mental models.

