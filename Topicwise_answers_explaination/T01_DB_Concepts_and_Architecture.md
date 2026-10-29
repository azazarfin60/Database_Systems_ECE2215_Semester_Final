---
title: "T01 · DB Concepts and Architecture · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T00 · Question Bank](../subtopicwise_questions.md) | [Exam-style layer](../Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) | [Next: T02 · E-R and EER Modeling →](T02_ER_and_EER_Modeling.md)

---

# T01 · DB Concepts and Architecture

> [!info] Topic card
> **Syllabus:** Unit 1 · **Weight:** 44 final marks (6.9%) in 7/7 papers + 7 CT marks
> **Sources:** Deck 01 · Textbook Ch. 1
> **Blocks in this file:** 13 final + 2 CT questions (9 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T01.1 | Data vs information, DB and DBMS | 0 + 0 | No questions | [[#T01.1 · Data vs information, DB and DBMS\|Go]] |
| T01.2 | File system vs DBMS | 21 + 0 | 2017 Q.1(a), 2018 Q.1(a), 2019 Q.1(a), 2021 Q.1(a), 2023 Q.1(b), 2024 Q.1(a) | [[#T01.2 · File system vs DBMS\|Go]] |
| T01.3 | Functions of the DBA and relation schema | 10 + 0 | 2017 Q.1(c), 2020 Q.1(a), 2021 Q.1(b) | [[#T01.3 · Functions of the DBA and relation schema\|Go]] |
| T01.4 | Data abstraction levels, schemas and instances | 8 + 5 | 2017 Q.2(b), 2019 Q.2(a), CT-01 Q.01 | [[#T01.4 · Data abstraction levels, schemas and instances\|Go]] |
| T01.5 | DDL vs DML | 2 + 0 | 2023 Q.1(c) | [[#T01.5 · DDL vs DML\|Go]] |
| T01.6 | DBMS engine components | 0 + 0 | No questions | [[#T01.6 · DBMS engine components\|Go]] |
| T01.7 | Two-tier vs three-tier architecture | 3 + 2 | 2020 Q.1(b), CT-01 Q.03 | [[#T01.7 · Two-tier vs three-tier architecture\|Go]] |

---

## T01.1 · Data vs information, DB and DBMS

*No questions from past finals or class tests.*

*See also:* [[#T01.2 · File system vs DBMS]] (2018 Q.1(a), 2019 Q.1(a))

---

## T01.2 · File system vs DBMS

### 2017 Q.1(a) · 04 Marks

*Section A · Asked in: 2017, 2021 (CLO1) · L2 merge*

**Question (2017 Q.1(a)).** Write down four significant differences between a file processing system and a DBMS.

**Question (2021 Q.1(a)).** Discuss four significant differences between a file-processing system and a DBMS.

**Answer.**

**What the examiner wants.**  
Four distinct architectural differences between an operating system file processing system and a DBMS. The mark split is 1 mark per difference. Examiners expect key technical concepts: redundancy, ad-hoc access, data independence, and concurrency or crash recovery.

**Key idea.**  
An operating system file stores a sequence of bytes. The OS does not understand the internal structure of the data inside the file. In contrast, a DBMS understands data structures, enforces relations and constraints, coordinates concurrent users, and guarantees recovery after system crashes.

**Step-by-step solution.**  

| Feature | File Processing System | DBMS (Database Management System) |
| :--- | :--- | :--- |
| **Data Redundancy & Inconsistency** | Data is duplicated across multiple separate files. Different copies easily get out of sync. | Centralizes data storage. Normalization avoids duplication and keeps copies consistent. |
| **Data Access & Retrieval** | Programmers must write a new custom program in C or Java for each new query. | Users write declarative queries (like SQL) to retrieve ad-hoc data quickly without new code. |
| **Data Isolation & Independence** | Data structures and application code are tightly coupled. Changing a file structure breaks programs. | Provides data abstraction. Changes to physical storage structures do not affect application programs. |
| **Concurrent Access & Recovery** | Hard to coordinate simultaneous access. Multiple updates cause lost data. Crash recovery is manual. | Built-in concurrency control prevents conflicting updates. Automated logging and recovery preserve ACID properties. |

*Variant for 2021 Q.1(a) (4 marks):* The same four differences directly answer the question.

**Check.**  
*Quick self-test:*
- Q: Why does a file system struggle with ad-hoc reporting?  
  A: Because each report requires a programmer to write and compile a new program from scratch.
- Q: How does a DBMS prevent data inconsistency when multiple copies exist?  
  A: It centralizes data and applies normalization so each fact is stored only once.

> [!warning] Common mistakes
> - Writing vague generalities like "file systems are old, DBMS is modern" instead of specific technical differences.
> - Omitting concurrent access anomalies and transaction crash recovery.
> - Writing a long essay instead of a structured comparison table.

**Exam tip.**  
Use a comparison table with clear feature titles. This layout allows the examiner to check off 1 mark per row in seconds.

**Sources.**  
- [Deck 01 · Slides 6–7](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.2](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

### 2018 Q.1(a) · 03 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** "A database is a tool for storing information efficiently"- Justify this statement.

**Answer.**

**What the examiner wants.**  
A clear technical justification showing how a database achieves efficiency. The expected mark split is 1 mark for each of the three dimensions of efficiency: storage space, retrieval speed, and operational concurrency.

**Key idea.**  
Efficiency means doing more while using fewer resources. Storing data in raw files wastes storage space through duplicate records and wastes time because lookups require scanning whole files. A database solves these issues with normalization, indexing, and multi-user transaction management.

**Step-by-step solution.**  
A database stores information efficiently by removing the major storage and access bottlenecks of traditional file systems:

1. **Storage Efficiency (Redundancy Control):** A database stores each fact in one place. It eliminates duplicate records across separate department files. This saves disk storage and prevents inconsistent copies.
2. **Retrieval Efficiency (Indexing and Query Optimization):** The DBMS uses tree or hash indexes. It also uses a cost-based query optimizer. This allows the system to find records in milliseconds without scanning whole files.
3. **Operational Efficiency (Concurrency and Data Independence):** Multiple users can query and update data at the same time without data corruption. Also, physical storage layouts can change without breaking existing application programs.

**Check.**  
*Quick self-test:*
- Q: What component of a DBMS ensures retrieval efficiency?  
  A: Index structures (like B+ trees) and the cost-based query optimizer.
- Q: How does redundancy control contribute to storage efficiency?  
  A: Storing facts once reduces disk space usage and removes the need for sync programs.

> [!warning] Common mistakes
> - Defining a database without explaining *why* it is efficient.
> - Focusing only on storage space while omitting query speed and concurrency.

**Exam tip.**  
Divide the answer into three clear headings: Storage Efficiency, Retrieval Efficiency, and Operational Efficiency.

**Sources.**  
- [Deck 01 · Slides 6–7, 24–25](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.2](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

### 2019 Q.1(a) · 03 Marks

*Section A · Asked in: 2019, 2023 (CLO1) · L2 merge*

**Question (2019 Q.1(a)).** Why DBMS is important? What are its advantages?

**Question (2023 Q.1(b)).** What are the advantages of DBMS over file processing system?

**Answer.**

**What the examiner wants.**  
A brief statement on why a DBMS is important (~1 mark) and a structured list of at least 4 to 5 key advantages over file systems (~2 marks).

**Key idea.**  
A DBMS provides a central, reliable layer between applications and physical storage. Its advantages directly fix the classic drawbacks of file processing systems: duplicate data, lack of ad-hoc access, and crash vulnerability.

**Step-by-step solution.**  
**Importance of DBMS:**  
A DBMS provides centralized, secure, and coordinated control over an organization's data. It replaces scattered operating system files and ensures that data remains reliable, shared, and recoverable during hardware or software crashes.

**Advantages of DBMS over File Processing Systems:**
1. **Control of Data Redundancy and Inconsistency:** Centralized data storage minimizes duplicate entries and prevents conflicting records.
2. **Data Independence:** Physical storage structures can change without requiring updates to application programs.
3. **Fast and Convenient Data Access:** Declarative query languages (like SQL) retrieve data without custom low-level programming.
4. **Transaction Management (ACID Properties):** Guarantees atomicity during crashes and protects data integrity during concurrent multi-user access.
5. **Data Security and Integrity Constraints:** Restricts unauthorized access through user privileges and enforces business rules automatically.

*Variant for 2023 Q.1(b) (3 marks):* Focus directly on the 5 advantages over file processing systems; omit the general importance statement.

**Check.**  
*Quick self-test:*
- Q: What does data independence mean in practice?  
  A: You can change disk storage layouts or indexes without rewriting application queries.
- Q: Why is atomicity a major advantage of DBMS?  
  A: It guarantees that fund transfers or updates complete fully or roll back completely during a crash.

> [!warning] Common mistakes
> - Listing fewer than 4 points for a 3-mark question.
> - Confusing software features with business benefits without naming technical mechanisms.

**Exam tip.**  
List 5 numbered advantages with bold titles. This guarantees full marks even if an examiner deducts for a brief point.

**Sources.**  
- [Deck 01 · Slides 4, 6–7](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.2](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

### 2024 Q.1(a) · 04 Marks

*Section A · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** A courier tracking company maintains large files for daily parcel updates. The data grows rapidly and requires fast retrieval. Choose between a file based system and a DBMS and justify the decision.

**Answer.**

**What the examiner wants.**  
An explicit recommendation (DBMS) and a justification directly using the scenario's facts: rapid data growth, fast retrieval, concurrent tracking updates, and data reliability. Mark split: 1 mark for the decision, 3 marks for linking scenario facts to technical justifications.

**Key idea.**  
A courier tracking service handles thousands of package updates and queries every hour. A file system would degrade rapidly because searching through growing flat files requires linear scans, and concurrent writes cause file corruption or severe locking delays. A DBMS provides indexing, concurrency control, and scalability.

**Step-by-step solution.**  
**Decision:** Choose a **DBMS (Database Management System)**.

**Justification:**
1. **Rapid Data Growth and Scalability:** As parcel records grow rapidly each day, a DBMS manages storage dynamically with tables and secondary storage. A file system suffers from large unwieldy files, data isolation, and slow sequential processing.
2. **Fast Retrieval via Indexing:** Customers and couriers need instant tracking updates. A DBMS builds B+ tree indexes on tracking numbers (`parcel_id`). This delivers lookup results in milliseconds instead of scanning large files line by line.
3. **Concurrent Multi-User Updates:** Delivery drivers, sorting hubs, and recipients update and read parcel records at the same time. A DBMS provides concurrency control to prevent lost updates and race conditions. A file system would require file locking, which blocks other users.
4. **Data Integrity and Constraints:** A DBMS automatically enforces rules. For example, status codes must be valid, and tracking IDs cannot be null or duplicated. File systems require custom application code to check every update.
5. **Crash Recovery and Backup:** Courier data cannot be lost during system crashes or power failures. A DBMS maintains write-ahead logs (WAL) and automatic transaction rollback to preserve tracking history.

**Check.**  
*Scenario link verification:*
- Fact: "Large files / grows rapidly" $\rightarrow$ Handled by DBMS dynamic page allocation and relational tables.
- Fact: "Requires fast retrieval" $\rightarrow$ Handled by B+ tree index lookups on parcel IDs.
- Operational reality: Couriers updating statuses on the road $\rightarrow$ Handled by row-level locking and ACID transactions.

> [!warning] Common mistakes
> - Writing a generic textbook essay about DBMS without mentioning the courier scenario.
> - Forgetting to state the decision explicitly in the opening line.

**Exam tip.**  
Start with a bold decision line. Then quote the scenario requirements directly in your justification bullet points.

**Sources.**  
- [Deck 01 · Slides 6–7, 23–26](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.2](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

## T01.3 · Functions of the DBA and relation schema

### 2020 Q.1(a) · 05 Marks

*Section A · Asked in: 2020, 2021 (CLO1), 2017 · L2 merge*

**Question (2020 Q.1(a)).** What are the five main functions of a database administrator? What is relation schema?

**Question (2021 Q.1(b)).** What are the five main functions of a database administrator?

**Question (2017 Q.1(c)).** What are the main functions of a database administrator? Point out the name only.

**Answer.**

**What the examiner wants.**  
The five official functions of a DBA (3 marks, following the exact terminology from Deck 01 Slide 10) and the definition of a relation schema with a formal example (2 marks).

**Key idea.**  
The Database Administrator (DBA) is the person with centralized control over the database system. The DBA handles both physical storage decisions and user authorization. A relation schema is the logical structural definition of a table (its blueprint).

**Step-by-step solution.**  
**Five Main Functions of a Database Administrator (DBA):**
1. **Schema definition:** The DBA creates the original database schema by executing DDL statements.
2. **Storage structure and access-method definition:** The DBA defines internal storage structures, indexing methods, and file organizations to optimize data access.
3. **Schema and physical-organization modification:** The DBA modifies database schemas and physical storage layouts to improve performance or adapt to changing business requirements.
4. **Granting of authorization for data access:** The DBA assigns access rights and user roles to regulate who can inspect or modify specific data items.
5. **Routine maintenance:** The DBA performs recurring operational tasks. These include periodically backing up the database, monitoring running jobs, and ensuring sufficient free disk space.

**Relation Schema:**  
A **relation schema** is the formal logical definition or blueprint of a relation (table). It specifies the name of the relation along with its set of attributes (columns) and their corresponding domains (data types).

- Format: $R(A_1, A_2, \dots, A_n)$
- Example: $\text{instructor}(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{salary})$, where $\underline{\text{ID}}$ serves as the primary key.

*Variant for 2021 Q.1(b) (3 marks):* State and explain the five DBA functions above; omit the relation schema.  
*Variant for 2017 Q.1(c) (2 marks):* List only the names: (1) Schema definition, (2) Storage structure and access-method definition, (3) Schema and physical-organization modification, (4) Granting of authorization for data access, (5) Routine maintenance.

**Check.**  
*Quick self-test:*
- Q: What is the difference between a relation schema and a relation instance?  
  A: The schema is the logical definition (table design), while an instance is the actual data populated at a given moment.
- Q: Which DBA function ensures that the system does not run out of storage during operations?  
  A: Routine maintenance (monitoring disk space and upgrading storage).

> [!warning] Common mistakes
> - Inventing informal duties (like "writes SQL queries" or "enters user records") instead of using the five official functions from Deck 01 Slide 10.
> - Forgetting to provide a concrete schema example for the relation schema part.

**Exam tip.**  
Examiners check off the exact 5 headings from Slide 10. Write the exact headings and underline them.

**Sources.**  
- [Deck 01 · Slide 10](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Deck 02 · Slide 6](../LectureSlides/02_Relational_Model.md)  
- [Textbook Ch. 1 §1.3.2, §1.8.2](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

## T01.4 · Data abstraction levels, schemas and instances

### 2017 Q.2(b) · 04 Marks

*Section A · Asked in: 2017, 2019, CT-01 (CO1, 5 Marks) · L2 merge*

**Question (2017 Q.2(b)).** What is the purpose of data abstraction? Describe the different level of data abstraction.

**Question (2019 Q.2(a)).** What is data abstraction? Describe the different level of data abstraction.

**Question (CT-01 · Q.01).** Define data abstraction. Describe different types of data abstractions.

**Answer.**

**What the examiner wants.**  
The definition and purpose of data abstraction (~1 mark), clear descriptions of all three abstraction levels (physical, logical, view) (~2 marks), and the architecture diagram (~1 mark).

**Key idea.**  
Database systems use complex data structures to store information efficiently. Most users and application programmers do not understand storage pointers or disk block layouts. Data abstraction hides low-level complexity to provide a clean and intuitive interface.

**Step-by-step solution.**  
**Purpose of Data Abstraction:**  
A database contains complex data structures, storage blocks, and indexing schemes. Most end users and programmers are not trained in low-level storage details. Data abstraction hides this physical complexity. It simplifies user interactions, enforces security, and enables physical data independence.

**Levels of Data Abstraction:**
1. **Physical level:** The lowest abstraction level. It describes *how* records are stored on secondary storage media (such as byte offsets, data blocks, B+ trees, and hashing schemes).
2. **Logical level:** The intermediate level. It describes *what* data is stored in the database and the relationships among those data. Programmers and administrators work at this level using schemas.
   Example record:
   ```text
   type instructor = record
       ID : string;
       name : string;
       dept_name : string;
       salary : integer;
   end;
   ```
3. **View level:** The highest abstraction level. It describes only the subset of the database relevant to a specific user group. It hides other data and complex structures for ease of use and security (for example, hiding instructor salaries from students).

![Three levels of data abstraction architecture showing view level, logical level, and physical level](../LectureSlides/diagrams/L01_p14_fig01.jpg)
*Figure: Three levels of data abstraction (Deck 01, Slide 14)*

*Variant for 2019 Q.2(a) (4 marks):* Define data abstraction, describe the three levels, and include the diagram.  
*Variant for CT-01 Q.01 (5 marks):* State the definition, explain the three levels, show the record example, and draw the diagram.

**Check.**  
*Quick level-matching test:*
- Record block allocation on disk blocks $\rightarrow$ Physical level.
- Entity definition with column names and data types $\rightarrow$ Logical level.
- Form displaying student grades without instructor salaries $\rightarrow$ View level.

> [!warning] Common mistakes
> - Mixing up the logical level and view level. Remember that the logical level describes the *entire* database, while each view describes a *subset*.
> - Leaving out the architecture diagram.

**Exam tip.**  
Draw the three-tiered box diagram with multiple view boxes on top, the logical box in the middle, and the physical box at the bottom.

**Sources.**  
- [Deck 01 · Slides 13–14](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.3](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

## T01.5 · DDL vs DML

### 2023 Q.1(c) · 02 Marks

*Section A · CLO1 · Asked in: 2023 · L1 (asked once)*

**Question.** Explain DDL and DML with example.

**Answer.**

**What the examiner wants.**  
A concise definition and a valid SQL example for DDL (1 mark), and a concise definition and a valid SQL example for DML (1 mark).

**Key idea.**  
DDL sets up the schema and tables. DML queries and manipulates the records stored within those tables.

**Step-by-step solution.**  
- **DDL (Data Definition Language):** A specialized set of commands used to define, alter, and delete the database schema and storage structures.
  Example:
  ```sql
  CREATE TABLE instructor (
      ID CHAR(5),
      name VARCHAR(20),
      dept_name VARCHAR(20),
      salary NUMERIC(8,2)
  );
  ```
- **DML (Data Manipulation Language):** A language used to query, insert, update, or delete data stored in the database.
  Example:
  ```sql
  SELECT name FROM instructor WHERE dept_name = 'Comp. Sci.';
  ```

**Check.**  
*Classification check:*
- `DROP TABLE student;` $\rightarrow$ DDL (modifies schema).
- `INSERT INTO instructor VALUES ('10101', 'Srinivasan', 'Comp. Sci.', 65000);` $\rightarrow$ DML (modifies data).

> [!warning] Common mistakes
> - Forgetting to include concrete SQL code examples.
> - Mistaking `SELECT` for DDL. `SELECT` is declarative DML (query language).

**Exam tip.**  
Keep the explanation to 1 sentence per term, followed immediately by a clean 4-line SQL statement.

**Sources.**  
- [Deck 01 · Slides 16–19](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.4](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

## T01.6 · DBMS engine components

*No questions from past finals or class tests.*

---

## T01.7 · Two-tier vs three-tier architecture

### 2020 Q.1(b) · 03 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Differentiate between the two-tier architecture and three-tier architecture of database. Which is better suited for web application? Why?

**Answer.**

**What the examiner wants.**  
Key differences between two-tier and three-tier database architectures (1.5 marks), and a definitive choice of three-tier for web applications with technical justification (1.5 marks).

**Key idea.**  
In two-tier systems, the client communicates directly with the database system. In three-tier systems, an application server sits between the client and the database. Web applications require three-tier architecture so client browsers remain lightweight and never access database ports directly.

**Step-by-step solution.**  
**Differences between Two-Tier and Three-Tier Architectures:**

| Feature | Two-Tier Architecture | Three-Tier Architecture |
| :--- | :--- | :--- |
| **Application Placement** | The application logic resides entirely on the client machine. | The client holds only the presentation layer. Application logic resides on an intermediate application server. |
| **Database Communication** | The client invokes database system calls directly over the network (using ODBC or JDBC). | The client communicates with the application server, which in turn contacts the database system. |
| **Client Overhead** | Thick (fat) client. Requires database drivers and business code installed on each client. | Thin client. Runs in a web browser or simple mobile interface. |

![Comparison of two-tier and three-tier database application architectures](../LectureSlides/diagrams/L01_p30_fig01.jpg)
*Figure: Two-tier and three-tier database architectures (Deck 01, Slide 30)*

**Web Application Choice & Reason:**  
**Three-tier architecture is better suited for web applications.**
- **Reason:** Web clients (browsers) should remain thin and lightweight without direct database drivers. Placing application logic on an intermediate server protects database credentials behind firewalls and allows connection pooling for thousands of concurrent users.

**Check.**  
*Quick self-test:*
- Q: Where does business logic execute in a three-tier setup?  
  A: On the intermediate application server.
- Q: Why is two-tier unsuitable for internet-scale web apps?  
  A: Exposing database ports directly to clients is insecure, and managing thousands of direct database connections overwhelms the database server.

> [!warning] Common mistakes
> - Suggesting two-tier for web applications.
> - Forgetting to explain *why* three-tier is suited for web applications (security and thin client).

**Exam tip.**  
State your verdict in bold font: **Three-tier architecture is better suited for web applications.** Then supply the two key reasons: thin clients and security/connection pooling.

**Sources.**  
- [Deck 01 · Slides 29–30](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.7](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

### CT-01 Q.03 · 02 Marks

*CT-01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Describe the structure of a database application.

**Answer.**

**What the examiner wants.**  
A concise description of the functional structure of a database application, covering user interaction, application logic, and database access.

**Key idea.**  
A database application acts as a mediator. It accepts user input through an interface, executes business rules using host programming languages, and interacts with the DBMS engine via queries.

**Step-by-step solution.**  
A database application connects user interfaces to the database engine through three functional layers:

1. **Presentation Layer (Client Front End):** The client interface (web browser, mobile app, or desktop form) through which users enter input and view results.
2. **Business Logic Layer (Application Server):** Programs written in host languages (like Python, Java, or C++) that implement business rules, validate input, and issue database queries.
3. **Data Access Layer (Database Server / DBMS Engine):** The database system that uses APIs (such as JDBC or ODBC) to execute SQL queries, manage transactions, and persist data.

**Check.**  
*Role verification:*
- Client / Front end: Collects inputs from the user.
- Application server / programs: Implements business rules that SQL alone cannot express.
- Database server / DBMS engine: Executes queries and manages storage blocks safely.

> [!warning] Common mistakes
> - Describing internal DBMS engine modules (storage manager, buffer manager) instead of the database *application* architecture.

**Exam tip.**  
List the three clear application tiers: Presentation Layer, Business Logic Layer, and Data Access Layer.

**Sources.**  
- [Deck 01 · Slides 20, 29–31](../LectureSlides/01_Intro_to_Database_and_DBMS.md)  
- [Textbook Ch. 1 §1.7](../Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md)

---

[← Prev: T00 · Question Bank](../subtopicwise_questions.md) | [Exam-style layer](../Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) | [Next: T02 · E-R and EER Modeling →](T02_ER_and_EER_Modeling.md)

