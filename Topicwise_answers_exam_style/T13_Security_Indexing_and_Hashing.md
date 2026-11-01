---
title: "T13 · Security, Indexing and Hashing · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T12 · Recovery System and RAID](T12_Recovery_System_and_RAID.md) | [Explanation layer](../Topicwise_answers_explaination/T13_Security_Indexing_and_Hashing.md)

---

# T13 · Security, Indexing and Hashing

> [!info] Topic card
> **Syllabus:** Unit 8 · **Weight:** 18 final marks (2.8%) in 4/7 papers · 0 CT marks
> **Sources:** Textbook Ch. 4 §4.7, Ch. 5 §5.1, Ch. 9 §9.8, Ch. 14, Ch. 24 §24.5 · Deck 01 Slides 20–32
> **Blocks in this file:** 5 final questions (4 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T13.1 | Database security threats and authorization | 4 + 0 | 2017 Q.8(a) | [[#T13.1 · Database security threats and authorization\|Go]] |
| T13.2 | SQL injection: how it works and prevention | 9 + 0 | 2021 Q.8(b), 2020 Q.4(a) | [[#T13.2 · SQL injection: how it works and prevention\|Go]] |
| T13.3 | Indexing: dense vs sparse index | 2 + 0 | 2023 Q.8(a) | [[#T13.3 · Indexing: dense vs sparse index\|Go]] |
| T13.4 | Hashing: static vs dynamic | 3 + 0 | 2017 Q.7(c) | [[#T13.4 · Hashing: static vs dynamic\|Go]] |

---

## T13.1 · Database security threats and authorization

### 2017 Q.8(a) · 04 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** Describe four of the main threats to database security.

**Answer.**

Four main threats to database security and their countermeasures are:

1. **SQL Injection:**
   - **Threat:** Attackers enter malicious SQL syntax into user input fields. The application concatenates this input into queries. The parser then executes unintended commands.
   - **Countermeasure:** Use prepared statements with parameterized queries. Validate all user inputs against strict type and format rules.

2. **Privilege Abuse and Unauthorized Access:**
   - **Threat:** Legitimate users or compromised accounts obtain excessive privileges. They access or modify sensitive data beyond their authorized duties.
   - **Countermeasure:** Enforce the principle of least privilege. Use Role-Based Access Control (`GRANT`/`REVOKE`) and restricted SQL views.

3. **Data Eavesdropping and Leakage:**
   - **Threat:** Attackers intercept unencrypted data in transit over the network. They can also steal plaintext database files and backup disks.
   - **Countermeasure:** Encrypt network traffic using TLS/SSL. Encrypt database storage and backup files using Transparent Data Encryption (TDE).

4. **Denial of Service (DoS):**
   - **Threat:** Attackers flood the database server with excessive requests or complex queries. This exhausts CPU, memory, and connection pools, making the database unavailable.
   - **Countermeasure:** Use connection pooling, enforce query execution timeouts, and apply rate limiting with database firewalls.

---

## T13.2 · SQL injection: how it works and prevention

### 2021 Q.8(b) · 05 Marks

*Section B · CLO4 · Asked in: 2021 (CLO4), 2020 (Sec A, 4m) · L2 merge*

**Question (2021 Q.8(b)).** What is SQL injection attack? Describe the precautions that should be taken to prevent this attack.

**Question (2020 Q.4(a)).** What is an SQL injection attack? Explain how it works and what precautions must be taken to prevent SQL injection attack.

**Answer.**

**1. What is an SQL Injection Attack?**  
An **SQL injection attack** occurs when an attacker inputs malicious SQL commands into an application input field. The application concatenates this untrusted input directly into a dynamic SQL query string. The database parser interprets the malicious input as SQL instructions rather than data. This allows the attacker to bypass authentication, read unauthorized data, or modify and delete tables.

**2. How It Works**  
Consider an application that builds a query using string concatenation:

```python
# Vulnerable query construction
query = "SELECT * FROM instructor WHERE name = '" + user_input + "'"
```

- **Scenario 1: Authentication Bypass / Data Dumping**
  - **Attacker input:** `' OR '1'='1`
  - **Resulting SQL:**

```sql
SELECT * FROM instructor WHERE name = '' OR '1'='1';
```
  - **Mechanism:** The quote closes the name literal. The `'1'='1'` condition is always true. The database returns all records in the `instructor` table.

- **Scenario 2: Destructive Attack (Piggybacked Query)**
  - **Attacker input:** `'; DROP TABLE student; -- `
  - **Resulting SQL:**

```sql
SELECT * FROM instructor WHERE name = ''; DROP TABLE student; -- ';
```
  - **Mechanism:** The semicolon terminates the first query. The database engine executes the injected `DROP TABLE student` statement. The trailing `--` treats the remaining query syntax as a comment.

**3. Precautions to Prevent SQL Injection**  

1. **Use Prepared Statements (Parameterized Queries):**
   This is the primary defense. The application precompiles the SQL query structure with placeholders. User input is bound separately as data parameters. The parser never executes parameter content as SQL commands.
   ```python
   # Secure parameterized query
   cursor.execute("SELECT * FROM instructor WHERE name = %s", (user_input,))
   ```
   In Java/JDBC, use `PreparedStatement` with `?` markers and `setString()`.

2. **Input Validation and Whitelisting:**
   Validate data types, lengths, and patterns before passing them to queries. For dynamic query parts like table or column names that cannot use parameters, check input against an explicit whitelist of allowed identifiers.

3. **Enforce Least Privilege:**
   Configure database user accounts with minimal necessary privileges. A public web application account should only have `SELECT` or `INSERT` access. It must never have administrative permissions like `DROP TABLE` or `GRANT`.

4. **Use Parameterized Stored Procedures:**
   Wrap database operations inside stored procedures with typed parameters. Do not concatenate dynamic SQL inside the stored procedure body.

5. **Suppress Database Error Messages:**
   Hide internal database error details, table names, and stack traces from end users. Display generic error pages instead.

*Short version for 2020 Q.4(a) (4 marks):* Provide the definition, the `' OR '1'='1` exploit example, and the three core precautions: prepared statements, input validation, and least privilege.

---

## T13.3 · Indexing: dense vs sparse index

### 2023 Q.8(a) · 02 Marks

*Section B · CLO1 · Asked in: 2023 · L1 (asked once)*

**Question.** Write short note on dense and sparse index.

**Answer.**

**1. Definitions**  
- **Dense Index:** An index that contains an index record for **every** search-key value in the data file. To find a record, the system looks up the search key directly in the index and follows its pointer.
- **Sparse Index:** An index that contains index records for only **some** search-key values (typically one entry per disk block). The data file **must be sorted** on the search key. To find a record, the system finds the largest index key less than or equal to the target value, then scans the data block sequentially.

![Dense index on instructor file with search key ID](../Textbook/Chapter_14_Indexing/diagrams/fig_14_02.jpg)
*Figure 13.1: Dense index on instructor file with search key ID (Source: Textbook Ch. 14, Fig. 14.2).*

![Sparse index on instructor file with search key ID](../Textbook/Chapter_14_Indexing/diagrams/fig_14_03.jpg)
*Figure 13.2: Sparse index on instructor file with search key ID (Source: Textbook Ch. 14, Fig. 14.3).*

**2. Comparison**  

| Feature | Dense Index | Sparse Index |
| :--- | :--- | :--- |
| **Index Entries** | One entry for every search-key value in the file. | One entry for only some search-key values (usually one per disk block). |
| **Lookup Speed** | Faster. Locates the exact record or its list of duplicates directly. | Slower. Requires an index lookup followed by a sequential block scan. |
| **Space Overhead** | Large. The index file consumes significant disk or memory space. | Small. The index file is much smaller and often fits in main memory. |
| **File Ordering** | Can be built on sorted (clustering) or unsorted (non-clustering) files. | Requires the data file to be ordered on the search key (clustering only). |
| **Maintenance Cost** | High. Insertions and deletions often require adding or removing index entries. | Low. Records can often be inserted or deleted inside a block without updating the index. |

**Practical Trade-off:** A sparse index with one entry per disk block offers a good compromise between lookup speed and index size.

---

## T13.4 · Hashing: static vs dynamic

### 2017 Q.7(c) · 03 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** What is hashing? Differentiate between static and dynamic hashing.

**Answer.**

**1. What is Hashing?**  
**Hashing** is a search and data organization technique. It uses a mathematical function $h(K)$, called a **hash function**. The function maps a search key $K$ to the address of the **bucket** storing the record. A bucket is a storage unit, typically a disk block. Hashing provides direct $O(1)$ average search time for equality queries without traversing tree pointers.

**2. Differentiate between Static and Dynamic Hashing**  

| Feature | Static Hashing | Dynamic Hashing |
| :--- | :--- | :--- |
| **Number of Buckets** | Fixed at database creation time. | Adjusts dynamically as the database grows or shrinks. |
| **Overflow Handling** | Uses overflow bucket chains when a bucket fills up. | Buckets split or coalesce. Overflow chains are avoided or minimized. |
| **Lookup Performance** | Degrades over time. Long overflow chains require slow sequential scans. | Remains fast ($O(1)$ disk accesses) even after substantial growth. |
| **Reorganization** | Requires periodic offline rebuilding of the whole file with a new hash function. | Reorganizes incrementally, one bucket at a time, without stopping database access. |
| **Space Usage** | Poor. Allocating few buckets causes overflow; allocating many wastes space. | High. Storage capacity scales smoothly with the actual number of records. |
| **Common Examples** | Modulo hashing with overflow chaining. | Extendable hashing and linear hashing. |

![General extendable hash structure with bucket address table and bucket depths](../Textbook/Chapter_24_Advanced_Indexing/diagrams/fig_24_08.jpg)
*Figure 13.3: General extendable hash structure with bucket address table (Source: Textbook Ch. 24, Fig. 24.8).*

---

[← Prev: T12 · Recovery System and RAID](T12_Recovery_System_and_RAID.md) | [Explanation layer](../Topicwise_answers_explaination/T13_Security_Indexing_and_Hashing.md)
