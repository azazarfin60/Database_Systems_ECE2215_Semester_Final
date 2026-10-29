# T01: DB Concepts & Architecture — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 1 | `subtopicwise_list.md` T01 (44 marks · 6.9% · 7/7)  
**Source Pages:** Page 1, Page 4 (Right), Page 10 (Right), Page 11, Page 12 (Left, Right)

---

## 1. Introduction to Database & DBMS

<!-- Page 1 -->
<!-- Date: 29.06.2024 | Teacher: HAFSA MAM -->

📖 **Database System Concepts** $\longleftarrow$ Book name  
* Seventh Edition (Silberschatz, Korth & Sudarshan)

⊕ **DBMS $\rightarrow$ Database Management System**
* $\llcorner$ collection of interrelated data.
* $\llcorner$ a set of programs to access those data.

📖 It is needed to manage large bodies of information.

* **Importance?**
* **Applications?** Accounting, Banking, Airlines etc.
  * $\llcorner$ data highly available
  * $\llcorner$ are relatively large
  * $\llcorner$ accessed by multiple users

* **Data Model:**
  * Relational Model

* **Programming language:** MySQL

---

<!-- Page 10 (Right) -->
<!-- CLASS-01 | 01.07.2024 | NIS MAM -->

### Core Definitions

* **Database:** Organized collection of data stored and accessed electronically.
* **Two types:**
  * $\rightarrow$ **Structured:** In table format.
  * $\rightarrow$ **Unstructured:** Document or key-value based.

### Differences between Data & Information:

| Data | Information |
| :--- | :--- |
| Unorganised | Organised |
| Undefined | Defined |
| Smallest unit | Processed meaningful form |

* **Database Management System (DBMS):** Software system to access and manage the collection of interrelated data.
  * $\llcorner$ Characteristics
  * $\llcorner$ Application examples
  * $\llcorner$ Purposes of database systems

---

## 2. File Systems vs. DBMS (Drawbacks of File Systems)

<!-- Page 4 (Right) -->
<!-- CLASS-02 | 27.06.2024 -->

### How to make table?
* $\llcorner$ Dataset
* **Step 01:** Database create.
* **Step 02:** Table create (e.g., Students).
* **Step 03:** Insert record.

> [!WARNING]
> `DROP` permanently deletes the entire database along with all its tables and data!

### Drawbacks of Storing Data in a File System:
* **Data Redundancy & inconsistency:** Multiple copies of the same data across different files leading to conflicting values.
* **Difficulty in accessing data:** Need to write new application programs for each new query.
* **Data isolation:** Multiple files and disparate formats make ad-hoc querying difficult.
* **Integrity problem:** Hard to enforce cross-file consistency and constraints.
* **Atomicity of updates:** System failure mid-operation leaves data in an inconsistent state.
* **Concurrent access by multiple users:** Lack of coordinated access control leads to lost updates and race conditions.
* **Security problems:** Hard to provide granular access control to specific users.

---

## 3. Database Components & Roles of the DBA

<!-- Page 11 (Left) -->
<!-- CLASS-02 | 06.07.2024 -->

### Components of a Database System:
* **User data:** Actual records and facts stored in tables.
* **Metadata:** Data about data (data dictionary, schema definitions, constraints).

* $\rightarrow$ **Software:**
  * Actual DBMS software like MySQL, Oracle, PostgreSQL.
* $\rightarrow$ **Hardware:**
  * Physical devices like servers, storage disks, input-output devices (keyboard, monitor, printer).
* $\rightarrow$ **Procedure:**
  * Instructions and rules for using DBMS.
* $\rightarrow$ **Database Access Language:**
  * Used to interact with the database (create, read, update, delete data).

### Users of Relational Database Systems:
* **Naive users:** Interact via pre-built user interfaces / forms.
* **Application programmers:** Write code (Java, Python, C++) to interact with the database engine.

---

<!-- Page 11 (Right) -->

### Database Administrator (DBA):
* Schema definition
* Storage structure and access-method definition
* Schema and physical-organization modification
* Granting user authorization for data access
* Routine maintenance (backups, performance monitoring)

### Data Models Overview:
* Relational model
* Entity Relationship model
* Object-based data model
* Semi-structured data model (XML / JSON)
* *Older legacy models:*
  * Network model
  * Hierarchical model

---

## 4. Levels of Data Abstraction

<!-- Page 11 (Right) -->

Data abstraction (hiding internal storage and implementation details) $\rightarrow$ 3 levels of data abstraction:

```text
+------------------------------------+
|  View 1    |  View 2   |  View n   |  <- View Level
+------------------------------------+
|          Logical Level             |  <- Logical Level (What data are stored)
+------------------------------------+
|          Physical Level            |  <- Physical Level (How data are stored)
+------------------------------------+
```

1. $\Rightarrow$ **Physical level:** Describes *how* data are actually stored on secondary storage.
2. $\Rightarrow$ **Logical level:** Describes *what* data are stored and what relationships exist among them.
3. $\rightarrow$ **View level:** Describes only a part of the database relevant to a specific user group (hiding irrelevant/sensitive data).

### Instances vs. Schema:
* **Instance:** The collection of information stored in the database at a particular point in time (the actual data content at a specific moment).
* **Schema:** Logical design / structure of the database (skeleton / variable declaration, rarely changes).

---

## 5. DDL, DML & Database Languages

<!-- Page 11 (Right) & Page 12 (Left) -->

* **DDL (Data Definition Language):** Defines database schema and structural specifications (`CREATE`, `ALTER`, `DROP`).
* **DML (Data Manipulation Language):** Manipulates and queries stored data.
  * $\rightarrow$ **Procedural DML:** User specifies *what* data are required and *how* to get them.
  * $\rightarrow$ **Declarative (Nonprocedural / SQL):** User specifies *what* data are required without specifying how to retrieve them.
* **DQL (Data Query Language):** `SELECT` statements for retrieving information.
* **Database access from Application Programs:** Interfacing via C, C++, Java, Python using ODBC / JDBC.

---

## 6. Database Engine & Application Architectures

<!-- Page 12 (Left, Right) -->
<!-- CLASS-03 | 08.07.2024 | NIS MAM -->

### Database Design:
General structure of the database:
* $\rightarrow$ **Logical design:** Schema, tables, relationships, constraints.
* $\rightarrow$ **Physical design:** File organization, indexing, storage allocation.

### Database Engine Modules:
* $\rightarrow$ **Storage Manager:** Buffer manager, file manager, authorization and integrity manager, transaction manager.
* $\rightarrow$ **Query Processor:** DDL interpreter, DML compiler, query optimization and execution engine.
* $\rightarrow$ **Transaction Management:** Ensures atomicity, consistency, isolation, and durability (ACID) alongside concurrency control.

### Database Architecture:
* **Centralized database:** Database runs on a single central computer system.
* **Client-server database:** Front-end clients communicate with a central database server.
* **Parallel databases:** Multiple processors and disks run in parallel for high performance.
* **Distributed database:** Data physically stored across multiple geographically separated sites.

### Database Application Architectures:
* $\llcorner$ **Two-tier architecture:** Client directly communicates with the database server running the DBMS (`Client [App] <--> Database Server`).
* $\llcorner$ **Three-tier architecture:** Client interacts with an Application/Web server, which in turn accesses the database server (`Client [UI] <--> App/Web Server <--> Database Server`).

