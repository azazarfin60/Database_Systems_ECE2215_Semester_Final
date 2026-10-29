# T01: DB Concepts & Architecture — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 1 | `subtopicwise_list.md` T01 (44 marks · 6.9% · 7/7)  
**Source Pages:** Page 1 – Page 20 (Top)

---

<!-- Page 1 -->

## DBMS

### Definitions:
- **Data**: Raw, unprocessed facts without meaning.
  - **Ex:** 23, shishir, chuadanga
- **Information**: Processed data.
  - **Ex:** The age of shishir is 23
- **Database**: Collection of related data.
  - **Ex:** Library management system
- **Meta-data**: The database definition.
  - It is a complete description of a database or it defines the database. Information like the storage format or the type of the data that we are going to store in the database or the constraints on the data all these information is called as metadata.

---

---

<!-- Page 2 -->

## DBMS Definition:
Database management system is a system to manage the database and here managing could be either storing of data or retrieval of data from the database.
- Collection of programs that enables users to create and maintain the database.

### Functionalities:
1. **Define**: Specifying the data type, structures and constraints for the data to be stored.
   - **Constraints**: $\rightarrow$ limits on the data.
     $$\downarrow$$
     For example if I have age as the data to be stored then I can have a constraint, say age greater than 18 so only if age is greater than 18 then only the data can be stored in the database.
2. **Construct**: Process of storing data on some storage medium.

---

---

<!-- Page 3 -->

3. **Manipulate**: Querying the database to retrieve specific data, updating database and generating reports.
4. **Share**: Allows multiple users and programs to access the database concurrently or simultaneously.
5. **Protection of database**: From unauthorized access or from hardware or software failures and also maintenance of the database for a long period of time.

### Properties of Database:
1. A database represents some aspects of the real world (miniworld).
2. A database is a logically coherent collection of data with some inherent meaning.
3. A database is designed, built and populated with data for a specific purpose.

---

---

<!-- Page 4 -->

## DB System Environment

![p004_fig01: Database system environment architecture showing Users/Programmers, Application Programs/Queries, DBMS Software to process and access stored data, and Stored Database and Metadata](diagrams/p004_fig01.jpg)
*Figure 1 — Database System Environment (Page 4)*

```text
                  Users / Programmers
                           │
                           ▼
              Application Programs / Queries
                           │
                           ▼
           Software to process Queries / programs
                           │
                           ▼
             Software to Access Stored Data
                    │               │
                    ▼               ▼
           Stored Db Definition     Stored Database
               (MetaData)
```

---

---

<!-- Page 5 -->

## Characteristics of DBMS

### File System Approach (traditional)

![p005_fig01: Traditional file system approach showing isolated files for Account Dept and Exam Dept duplicating student attributes](diagrams/p005_fig01.jpg)
*Figure 1 — Traditional File System Approach with Departmental Data Duplication (Page 5)*

```text
       Account Dept                           Exam Dept
  ┌───────┬──────────┬──────────┐        ┌───────┬──────────┬────────┬────────┐
Roll_No  Name    Fees paid   fees      Roll_no  Name     Course   Grades
                               due
```

File system approach এ যদি আমরা ২ টা Dept চিন্তা করি যে একটি Account আর একটি Exam. এদের কিন্তু interest আলাদা তাই Data maintain করতে ২ Branch এ আলাদা file লাগবে। কিন্তু ২ জায়গায় Roll এবং Name আছে যা Redundancy create করে এবং space বেশি লাগে।

### DBMS Approach:
The entire data is stored in a single repository and multiple users can access the data based on their interests.

---

---

<!-- Page 6 -->

## Characteristics of DBMS Approach:
1. Self-describing Nature of a Database system.
2. Insulation between Programs and Data, and Data Abstraction.
3. Support of multiple views of the data.
4. Sharing of Data and multiuser Transaction processing.

### 1. Self-describing Nature of a Database system

- $\text{Database system} \rightarrow \text{Database} + \text{Meta-data (DB definition)}$
  $$\downarrow$$
  - **Stored in**: DBMS catalog.
  - **Used by**: DBMS software & Database user

- DBMS software must work equally well with any number of database applications.
- In traditional file processing, $\text{data definition} \rightarrow \text{part of application programs} \rightarrow \text{work with only one specific DB}$.

---

---

<!-- Page 7 -->

### 2. Insulation between Programs and Data, and Data Abstraction

- In traditional file processing $\rightarrow$ structure of data file is embedded in the application programs.
- In database approach $\rightarrow$ structure of data files is stored in the DBMS catalog $\rightarrow$ separate from access programs (**program-data independence**).
- The characteristic that allows program-data independence is called **data abstraction**.
- DBMS provides users with conceptual representation of data. It hides the behind the scene details or the complicated details that are not of interest to the database user.
- **Data model** is a type of data abstraction that provides conceptual representation to the database users in a way that most users can understand and the data model hides the storage and implementation details from the users.

---

---

<!-- Page 8 -->

### Program-data independence:
The ability to modify the data structure or storage characteristics without affecting the application program that access that data.

In traditional file-processing systems, the data structures and the application programs were tightly coupled. If we changed the format of a file, we had to rewrite every single program that used that file. DBMS solves this problem by separating the two.

### 3. Support of multiple views of the Data
- A database has many users, each of whom may require a different view of database.
- A view which is a subset of database that is derived from a main database table. It contains virtual data or the data which is not physically stored or that is not explicitly stored derived from database.

---

---

<!-- Page 9 -->

### 4. Sharing of Data and Multiuser Transaction Processing
- A multiuser DBMS allows multiple users to access the database at the same time.
- DBMS must include **concurrency control**.
  $$\downarrow$$
  When multiple users are sharing the same database at the same time, it should prevent two users from editing the same data at the same time.
- **OLTP** (Online Transaction Processing) $\rightarrow$ major part of database application.
- DBMS must enforce several transaction properties:
  $$\downarrow$$
  *Transaction: program under execution*

#### Two different transaction properties:
1. **Isolation**:
   > যখন কোনো agent seat book করে তখন ঐ seat block হয়ে যায় এবং অন্য agent রা access করতে পারবে না।
2. **Atomicity**:
   > Transaction যদি complete না হয় বা অর্ধেক হয়ে থেমে যায় তাহলে ঐ seat কে release করতে হবে।

---

---

<!-- Page 10 -->

## Database Users

![p010_fig01: Classification of Database Users into Actors on the scene and Workers behind the scene with roles and descriptions](diagrams/p010_fig01.jpg)
*Figure 1 — Classification of Database Users: Actors on the Scene vs. Workers Behind the Scene (Page 10)*

| Actors on the scene | Workers Behind the scene |
| :--- | :-- |
| $\downarrow$<br>are the people whose jobs involve using large databases everyday | $\downarrow$<br>are the people whose work to maintain the database system environment<br>$\downarrow$<br>They deal with the design, development & operation of the database system environment |
| **Actors on scene (user):**<br>$\rightarrow$ Database Administrators<br>$\rightarrow$ Database Designers<br>$\rightarrow$ End Users<br>$\rightarrow$ System Analysts & Application Programmers (Software Engineers) | **Workers Behind the scene:**<br>$\rightarrow$ System designers & implementers<br>$\rightarrow$ Tool developers<br>$\rightarrow$ Operators & maintenance personnel |

---

---

<!-- Page 11 -->

## Details $\rightarrow$ Actors on the scene

### Database Administrators:
In any large organization, we might have many resources and we always need a main person or a chief person or a manager to manage these resources.

$\rightarrow$ In database environment,
- **Primary resource** $\rightarrow$ database
- **Secondary resource** $\rightarrow$ DBMS & related software.

$\rightarrow$ **Database Administrator (DBA) responsibility:**
1. Administering primary / secondary resources.
2. Authorizing access to the database.
3. Co-ordinating & monitoring use of database.
4. Acquiring Hardware & software resources as needed.

---

---

<!-- Page 12 -->

### Database Designers:
1. Identifying the data to be stored in the database.
2. Choosing appropriate structures to represent and store data.
3. Communicating with database users to understand their requirements and based on their requirements a database designer designs the database.
4. A designer interact with users and develop views for each of these group of users based on their requirements. So database designer develop views for each group of users then each view is linked with the views of other group of users and that final database design should fulfil the requirements of all the user groups.

> [!NOTE] View Definition
> A view is the subset of the database. It is derived from the main database and it only contains data that is required by a particular user.

---

---

<!-- Page 13 -->

### End Users:
$\rightarrow$ End users are the people whose jobs require access to the database for querying, updating, generating reports.

$\rightarrow$ **Several categories of end users:**
1. **Casual end users**: Accesses database occasionally
   - Typically middle or high-level managers or occasional browsers.
2. **Naive or parametric end users**:
   - Constantly querying and updating database using canned transactions.
3. **Sophisticated end users**:
   - Engineers, scientists, business analysts or any other users who are familiar with the DBMS.
4. **Stand-alone users**:
   - Maintains personal databases by using ready made program packages.

---

---

<!-- Page 14 -->

## Database Users & Canned Transactions

### System Analysts & Application Programmers (Software Engineers)

- $\rightarrow$ **System Analysts** determine the requirements of end users especially the naive users or the parametric end users and then develop specifications for canned transaction.
- $\rightarrow$ **Application Programmers** $\rightarrow$ test, debug, document and maintain these canned transaction.

> [!NOTE] Canned Transaction
> $\hookrightarrow$ Sometimes called a predefined or packaged transaction. It is standard, highly optimized and frequently executed query or update that has been written, tested and stored in advance.

---

---

<!-- Page 15 -->

## Workers Behind the Scene

- $\rightarrow$ **System designers and implementers:**  
  Design and implement DBMS modules & interfaces as a package.

- $\rightarrow$ **Tool Developers:**  
  Persons who design and implement tools  
  $$\downarrow$$  
  software packages.

- $\rightarrow$ **Operators and maintenance personnel:**  
  Responsible for actual running and maintenance of hardware & software.

---

---

<!-- Page 16 -->

## Advantages of DBMS Approach

- $\rightarrow$ Controlling Redundancy
- $\rightarrow$ Restricting Unauthorized Access
- $\rightarrow$ Providing Persistent storage for program objects
- $\rightarrow$ Providing storage structures for efficient query processing.
- $\rightarrow$ Providing Backup & recovery
- $\rightarrow$ Providing multiple user interfaces.
- $\rightarrow$ Representing complex relationships among Data
- $\rightarrow$ Enforcing Integrity constraints.

---

---

<!-- Page 17 -->

## Data Models

- $\rightarrow$ Data model is used to describe the structure of the database $\rightarrow$ helps to achieve data abstraction.
- $\rightarrow$ Includes a set of basic operations for specifying retrievals or updates on the database.
- $\rightarrow$ Also includes concepts to specify the behaviour of a database application.

### Categories of Data Model

#### High-level or conceptual Data Model:
- Provides concepts that are close to the way many users see/perceive data.
- Use concepts such as entities, attributes and relationships.
  - **Entities** $\rightarrow$ Represent real world object or concept.
  - **Attributes** $\rightarrow$ further describe an entity.
  - **Relationships** $\rightarrow$ association among 2 or more entities.

---

---

<!-- Page 18 -->

## Data Models & Schema Concepts

#### Low-level or physical Data Model:
- Describes how data is stored in the computer.
- Access path $\rightarrow$ structure for efficient search of database records.

#### Representational (or implementation) Data Model:
- Represent data using record structures — that's why it is called record-based data models.

### Terminologies

- $\rightarrow$ **Database Schema:** Description of a database. It is just a plan or a layout or a blueprint of the database.
- $\rightarrow$ **Schema Diagram:** Displayed schema.

![Fig_p018_01: Schema diagram displaying the Student relation schema with attributes Name, Roll, Branch, and Address](diagrams/p018_fig01.jpg)
*Figure 18.1 — Schema diagram for Student relation (Page 18)*

- $\rightarrow$ **Schema Construct:** Each object within the schema. Ex. Student, Course etc.

---

---

<!-- Page 19 -->

- $\rightarrow$ **Database state (or instance or snapshot):** The data in the database at a particular moment.

## Database Design

### Overview of the Design Process

- Designing a database application is complex.
- Interaction of the application with the database.
- The needs of the users play a central role in the design process.
- Design phases are also crucial.
- Conceptual, logical and database design.
- Ensures integrity, efficiency and security.

### Design Phases

- The initial phase is to characterize the data need and DB users.
- The next phase pertains to data model.

---

---

<!-- Page 20 -->

- Followed by a fully developed conceptual schema.
- The final phase is the process of implementation.

### Design Issues

- Redundancy
- Incompleteness
