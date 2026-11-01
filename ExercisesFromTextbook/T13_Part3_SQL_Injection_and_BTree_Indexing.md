---
title: "T13 (Part 3) · SQL Injection & B+-Tree Indexing · Exercise Solutions"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T13
topic_id: T13
part: 3
exercise_count: 15
source_chapters:
  - "Chapter 09"
  - "Chapter 14"
---

[← Prev: T13 Part 2](T13_Part2_Security_and_Authorization_B.md) | [Index](00_Index.md) | [Next: T13 Part 4 →](T13_Part4_Indexing_and_Hashing.md)

---

# T13 (Part 3) · SQL Injection & B+-Tree Indexing

> [!info] Topic Card
> **Syllabus Unit:** Unit 8 · Advanced Database Concepts & Security  
> **Topic Weight:** 18 final marks (2.8% total final weight) across 4/7 RUET papers  
> **Source Chapters:** Silberschatz 7e Chapter 09 (*Application Development*, §9.8) and Chapter 14 (*Indexing*, §14.1–§14.6, §14.9)  
> **Assigned Exercises:** 15 items: PE 9.8, PE 14.1, PE 14.2, PE 14.3, PE 14.4, PE 14.5, PE 14.6, PE 14.7, PE 14.8, PE 14.11, PE 14.13, PE 14.14, PE 14.15, EX 9.16, EX 14.16  
> **Subtopics Covered:**  
> - `T13.2` · SQL injection attack mechanisms, penetration testing, and parameterized defenses  
> - `T13.3` · Indexing paradigms: Dense vs. sparse indexing, clustering constraints, B+-tree node invariants, insertion/deletion traces, bulk loading, and bitmap indexing  
> **Past RUET Direct Hits:**  
> - ⚠️ **EX 9.16** recycled verbatim in **2020 Q.4(a) [5m]** and **2021 Q.8(b) [3m]** (SQL injection attack mechanisms and defense-in-depth).  
> - ⚠️ **EX 14.16 / PE 14.2** directly tested in **2023 Q.8(a) [2m]** (Dense vs. sparse indexing concepts and constraints).

---

## Table of Exercises

| Exercise ID | Short Title | Subtopic | Type | RUET Exam Relevance | Jump Link |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **PE 9.8** | Testing for SQL-Injection Vulnerabilities | T13.2 | Practice | High (Pen-testing methodologies) | [[#Exercise 9.8 · Testing for SQL-Injection Vulnerabilities\|Go]] |
| **EX 9.16** | SQL Injection Attack Mechanisms & Defenses | T13.2 | Standard | ⚠️ Direct Hit (2020 Q.4a, 2021 Q.8b) | [[#Exercise 9.16 · SQL Injection Attack Mechanisms & Defenses\|Go]] |
| **PE 14.1** | Over-Indexing Pitfalls & Storage/Write Penalty | T13.3 | Practice | High (DML maintenance costs) | [[#Exercise 14.1 · Over-Indexing Pitfalls & Storage/Write Penalty\|Go]] |
| **PE 14.2** | Physical Uniqueness of Clustering Indices | T13.3 | Practice | Core Concept (2023 Q.8a foundation) | [[#Exercise 14.2 · Physical Uniqueness of Clustering Indices\|Go]] |
| **PE 14.3** | B+-Tree Construction for $n = 4, 6, 8$ | T13.3 | Practice | High (Node split tracing) | [[#Exercise 14.3 · B+-Tree Construction for n = 4, 6, 8\|Go]] |
| **PE 14.4** | Dynamic Operations on B+-Trees | T13.3 | Practice | High (Coalescing & redistribution) | [[#Exercise 14.4 · Dynamic Operations on B+-Trees\|Go]] |
| **PE 14.5** | Tree Height Under B*-Tree Redistribution | T13.3 | Practice | Theoretical (Space utilization bounds) | [[#Exercise 14.5 · Tree Height Under B*-Tree Redistribution\|Go]] |
| **PE 14.6** | B+-Tree Range Query Iterator Design | T13.3 | Practice | Implementation (JDBC ResultSet pattern) | [[#Exercise 14.6 · B+-Tree Range Query Iterator Design\|Go]] |
| **PE 14.7** | Leaf Occupancy Under Sequential Insertion | T13.3 | Practice | High (50% worst-case utilization) | [[#Exercise 14.7 · Leaf Occupancy Under Sequential Insertion\|Go]] |
| **PE 14.8** | Bulk Loading Cost & Bottom-Up Construction | T13.3 | Practice | High (Random vs. sequential disk I/O) | [[#Exercise 14.8 · Bulk Loading Cost & Bottom-Up Construction\|Go]] |
| **PE 14.11** | Read Optimization in LSM-Trees | T13.3 | Practice | Advanced (Compaction policies) | [[#Exercise 14.11 · Read Optimization in LSM-Trees\|Go]] |
| **PE 14.13** | Bitmap Index Construction & Range Evaluation | T13.3 | Practice | High (Bitwise hardware acceleration) | [[#Exercise 14.13 · Bitmap Index Construction & Range Evaluation\|Go]] |
| **PE 14.14** | Spatial Point Lookup: B+-Tree vs. R-Tree | T13.3 | Practice | Analytical (Zero-overlap efficiency) | [[#Exercise 14.14 · Spatial Point Lookup: B+-Tree vs. R-Tree\|Go]] |
| **PE 14.15** | Nearest-Neighbor via Circular Region Queries | T13.3 | Practice | Algorithmic (Iterative radius expansion) | [[#Exercise 14.15 · Nearest-Neighbor via Circular Region Queries\|Go]] |
| **EX 14.16** | Dense vs. Sparse Index Selection Criteria | T13.3 | Standard | ⚠️ Direct Hit (2023 Q.8a) | [[#Exercise 14.16 · Dense vs. Sparse Index Selection Criteria\|Go]] |

---

## T13.2 · SQL injection

### Exercise 9.8 · Testing for SQL-Injection Vulnerabilities

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09, Section 9.8 (*Application Security*), Page 456
> - **Exercise Type:** Practice Exercise 9.8 (Sub-parts a, b)
> - **Subtopic:** `T13.2` · SQL injection: how it works and prevention
> - **RUET Relevance:** High. Explains dynamic testing methodologies, fuzzer mechanics, and non-text attack vectors (hidden form fields, cookies, HTTP headers).

**Question (Silberschatz 7e Exercise 9.8).**  
Testing for SQL-injection vulnerability:  
**a.** Suggest an approach for testing an application to find if it is vulnerable to SQL injection attacks on text input.  
**b.** Can SQL injection occur with forms of HTML input other than text boxes? If so, how would you test for vulnerability?

---

#### 1. Core Principles & Concept Overview

SQL injection (SQLi) occurs when untrusted user input is concatenated directly into a dynamic SQL query string, allowing user input to break out of data literals and be executed as SQL commands by the database engine parser. 

Testing for SQLi relies on **Dynamic Application Security Testing (DAST)** (black-box fuzzing) and **Static Application Security Testing (SAST)** (source-code analysis):
1. **Syntax Injection & Error Induction:** Injecting metacharacters (e.g., `'`, `"`, `;`, `--`, `/* */`) that violate SQL grammar if concatenated unescaped, causing the database to throw internal SQL syntax error messages.
2. **Tautological Testing (Boolean-Based Blind):** Submitting boolean conditions that force query predicates to evaluate to `TRUE` (e.g., `' OR '1'='1`) versus `FALSE` (e.g., `' AND '1'='2`) and observing differences in application responses.
3. **Time-Based Blind Probing:** Injecting database sleep functions (e.g., `pg_sleep(5)`, `WAITFOR DELAY '0:0:5'`) to confirm code execution via response latency without relying on reflected error text.
4. **Input Vector Independence:** HTTP is stateless and text-based. Web clients send key-value pairs via HTTP `GET` query strings, `POST` request bodies, cookies, and headers. Any parameter processed by backend SQL queries—regardless of whether rendered as a dropdown, radio button, or hidden field in a browser—is completely controllable by an attacker.

---

#### 2. Detailed Step-by-Step Solution

##### (a) Approach for Testing Vulnerabilities on Text Input

A systematic testing methodology for text input fields involves four progressive phases:

1. **Character Fuzzing & Error Signature Detection:**
   - Input special SQL delimiter characters into the text input box:

```text
'
"
' OR '1'='1
' OR '1'='2
'; --
```
   - *Observation:* Check if the web response returns an HTTP 500 Internal Server Error, or displays an unhandled database error string such as `You have an error in your SQL syntax`, `Unclosed quotation mark before the character string`, or `ORA-00933: SQL command not properly ended`.
   - *Implication:* The presence of a database error proves the input escaped its data boundary and directly altered the SQL parser tree.

2. **Boolean-Based Inference (Blind SQLi):**
   - When database errors are suppressed by custom error handling, test whether user inputs alter the logical outcome:
     - **Test 1 (True Predicate):** Submit `admin' AND '1'='1` or `' OR 1=1 --`.
     - **Test 2 (False Predicate):** Submit `admin' AND '1'='2`.
   - *Observation:* If Test 1 logs in or returns search results, whereas Test 2 reports "User not found" or an empty page, the query logic is being manipulated dynamically.

3. **Time-Based Latency Testing:**
   - When no visual or content differences are returned, test for code execution using delay primitives:

```sql
'; WAITFOR DELAY '0:0:5'--      (Microsoft SQL Server)
' OR pg_sleep(5)--              (PostgreSQL)
' OR sleep(5)--                 (MySQL)
```
   - *Observation:* If the server response time increases by exactly 5 seconds, the SQL statement was parsed, dynamically injected, and executed.

4. **Automated Fuzzing & Static Analysis:**
   - Employ automated security testing tools (e.g., OWASP ZAP, SQLmap, Burp Suite Active Scanner) to inject boundary payloads across all parameters.
   - Complement with static code analysis tools (e.g., SonarQube, Semgrep) to flag dynamic query constructions such as `statement.executeQuery("SELECT ... " + userInput)`.

##### (b) SQL Injection via Non-Text HTML Inputs and Testing Procedures

**Yes**, SQL injection can occur through any HTML form input, including:
- Dropdown select boxes (`<select name="dept">`)
- Radio buttons (`<input type="radio" name="role">`)
- Checkboxes (`<input type="checkbox" name="active">`)
- Hidden input fields (`<input type="hidden" name="user_id" value="101">`)
- HTTP Request Headers (`Cookie`, `User-Agent`, `Referer`, `X-Forwarded-For`)

**Underlying Mechanism:**  
HTML form controls only restrict input within a cooperative web browser. An attacker does not interact with the backend database exclusively through the browser GUI; an attacker can intercept, modify, and transmit arbitrary HTTP requests directly using command-line tools (`curl`, Python `requests`) or local interception proxies (Burp Suite, OWASP ZAP, Fiddler).

```text
[Attacker Client] 
       │ 
       │ Intercepts HTTP POST /login
       │ Modifies hidden/dropdown field: role=' OR '1'='1
       ▼
[Web Application Server] 
       │ 
       │ Dynamic String Concatenation:
       │ "SELECT * FROM users WHERE role = '" + req.getParameter("role") + "'"
       ▼
[Database Engine Parser] ──► Executes injected syntax!
```

**Testing Procedure for Non-Text Inputs:**
1. **Interception Setup:** Route browser traffic through an HTTP proxy (e.g., OWASP ZAP).
2. **Form Submission & Request Trapping:** Fill out the form normally in the browser and click submit. Capture the outgoing raw HTTP request in the proxy before it reaches the server.
3. **Payload Substitution:** Modify the parameter values corresponding to `<select>`, `<input type="hidden">`, or cookie values by inserting SQL injection strings (e.g., replacing `<option value="CS">` with `CS' OR '1'='1--`).
4. **Forward and Analyze:** Forward the modified HTTP request to the server and evaluate the response for database syntax errors, altered query results, or time delays.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Strategy & Scoring Tips
> - **Core Vulnerability Premise:** Always emphasize that client-side validation (HTML `pattern`, JavaScript `onsubmit`, dropdown selections) provides **zero security**. Security controls must exist on the server side because HTTP clients can be completely simulated.
> - **Testing Pillars:** In RUET semester finals, answer both parts by distinguishing between **Error-based testing**, **Boolean blind testing**, and **Time-based blind testing**. Mentioning proxy-based parameter tampering (e.g., modifying hidden fields via Burp Suite) demonstrates deep practical understanding.

---

### Exercise 9.16 · SQL Injection Attack Mechanisms & Defenses

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09, Section 9.8 (*Application Security*), Page 457
> - **Exercise Type:** Standard Exercise 9.16
> - **Subtopic:** `T13.2` · SQL injection: how it works and prevention
> - **Past RUET Direct Hits:** ⚠️ **Recycled in 2020 Q.4(a) [5m]** and **2021 Q.8(b) [3m]**
> - **Cross-Reference:** `Topicwise_answers_exam_style/T13_Security_Indexing_and_Hashing.md`

**Question (Silberschatz 7e Exercise 9.16).**  
What is an SQL injection attack? Explain how it works and what precautions must be taken to prevent SQL injection attacks.

---

#### 1. Core Principles & Concept Overview

An **SQL injection (SQLi) attack** occurs when untrusted external input containing SQL control syntax is concatenated directly into a dynamic SQL query string. Because the database engine treats the resulting string as a unified command stream, the lexical scanner and parser interpret attacker-supplied text as SQL keywords, operators, and clauses rather than literal data constants.

```text
Untrusted Input ──► String Concatenation ──► Parser Breakdown ──► Malicious Execution
  (' OR 1=1 --)      ("... WHERE name = '"+)   (Data becomes code)   (Auth Bypass / Data Dump)
```

**Defense in Depth:** The only mathematically complete defense against SQL injection is the strict separation of code and data via **Prepared Statements (Parameterized Queries)**. Secondary defensive measures include input whitelisting, stored procedures, principle of least privilege, and database error cloaking.

---

#### 2. Detailed Step-by-Step Solution

##### 1. Definition
An **SQL Injection Attack** is an exploit technique wherein an attacker crafts input containing database syntax metacharacters to alter the structure of dynamic SQL statements executed by the application backend, enabling unauthorized data retrieval, authentication bypass, data tampering, or administrative system compromise.

##### 2. How It Works (Detailed Mechanics & Exploit Scenarios)

Consider a backend authentication servlet executing dynamic query concatenation:

```python
# Vulnerable string concatenation
sql_query = "SELECT * FROM users WHERE username = '" + user_input + "' AND password = '" + pass_input + "'"
cursor.execute(sql_query)
```

###### Scenario A: Authentication Bypass (Tautology Attack)
- **Attacker Input:**  
  `username`: `admin' --`  
  `password`: *(arbitrary text, e.g., `pass123`)*
- **Constructed SQL:**
  ```sql
  SELECT * FROM users WHERE username = 'admin' --' AND password = 'pass123'
  ```
- **Execution Breakdown:**  
  1. The single quote `'` after `admin` closes the string literal for `username`.
  2. The SQL comment symbol `--` instructs the parser to discard the entire remainder of the line.
  3. The query simplifies to `SELECT * FROM users WHERE username = 'admin'`. The password verification check is bypassed, granting access to the administrator account.

###### Scenario B: Data Exfiltration via Always-True Predicates
- **Attacker Input in Search Field:**  
  `user_input`: `' OR '1'='1`
- **Constructed SQL:**
  ```sql
  SELECT * FROM instructor WHERE name = '' OR '1'='1';
  ```
- **Execution Breakdown:**  
  Because `'1'='1'` evaluates unconditionally to `TRUE`, the `WHERE` clause matches every row in the relation, dumping the entire table contents to the client interface.

###### Scenario C: Destructive Attack (Stacked / Piggybacked Queries)
- **Attacker Input:**  
  `user_input`: `'; DROP TABLE takes; --`
- **Constructed SQL:**
  ```sql
  SELECT * FROM student WHERE ID = ''; DROP TABLE takes; --';
  ```
- **Execution Breakdown:**  
  The semicolon `;` terminates the initial `SELECT` statement. The database parser immediately evaluates the second statement (`DROP TABLE takes`), deleting the entire table from storage.

##### 3. Precautions and Countermeasures to Prevent SQL Injection

```text
                  ┌──────────────────────────────────────────────┐
                  │          SQL INJECTION PREVENTION            │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼──────────────────────────────┐
         ▼                               ▼                              ▼
┌──────────────────┐           ┌───────────────────┐          ┌───────────────────┐
│ Primary Defense  │           │ Defensive Coding  │          │ System Hardening  │
│  - Prepared      │           │  - Input Whitelist│          │  - Least Privilege│
│    Statements    │           │  - Stored Procs   │          │  - Error Masking  │
│  - Parameterized │           │  - ORM Frameworks │          │  - DB Firewalls   │
└──────────────────┘           └───────────────────┘          └───────────────────┘
```

1. **Prepared Statements with Parameterized Queries (Primary Defense):**
   - The query structure is pre-compiled by the database engine into an execution tree before runtime data parameters are bound. User input is transmitted across a separate protocol channel as pure data, never evaluated by the SQL parser.
   - **Java / JDBC Example:**

```java
String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setString(1, user_input);
pstmt.setString(2, pass_input);
ResultSet rs = pstmt.executeQuery();
```
   - **Python DB-API Example:**

```python
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user_input, pass_input))
```

2. **Input Validation and Whitelisting:**
   - Enforce strict typing, data lengths, and regex patterns (e.g., verifying an `ID` matches `^[0-9]{5}$`).
   - For query components that cannot accept bind parameters (such as table names, column names, or sort directions `ASC`/`DESC`), compare user input against a hardcoded in-memory whitelist:

```python
allowed_columns = {"name", "salary", "dept_name"}
sort_col = user_col if user_col in allowed_columns else "name"
```

3. **Use of Stored Procedures:**
   - Parameterized stored procedures encapsulate database operations behind predefined schemas. (Note: dynamic SQL concatenation inside stored procedures must be strictly avoided).

4. **Principle of Least Privilege (PoLP):**
   - The database user account under which the application connects should possess only minimal required permissions (e.g., `SELECT`, `INSERT` on application tables).
   - Revoke administrative privileges (`DROP TABLE`, `ALTER TABLE`, `GRANT`, `SHUTDOWN`) from web database accounts.

5. **Error Message Masking:**
   - Never expose raw database diagnostic messages, table identifiers, or stack traces in HTTP responses. Output generic messages (e.g., *"An error occurred. Please try again later."*).

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Direct Exam Hit Analysis
> - **2020 Q.4(a) [5m]:** Asked verbatim: *"What is an SQL injection attack? Explain how it works and what precautions must be taken to prevent SQL injection attack."*
> - **2021 Q.8(b) [3m]:** Asked: *"What is SQL injection attack? Describe the precautions that should be taken to prevent this attack."*
> 
> **Rubric Distribution for Full Marks (5 Marks):**
> - **Definition:** 1 Mark (Clear statement of input concatenation leading to parser interpretation).
> - **How it Works (Code Example):** 2 Marks (Must include vulnerable query string and `' OR '1'='1` or `' --` exploit walkthrough).
> - **Precautions:** 2 Marks (Must highlight **Prepared Statements** with code syntax, plus Least Privilege and Input Validation).

---

## T13.3 · Indexing: dense vs sparse, B+-tree

### Exercise 14.1 · Over-Indexing Pitfalls & Storage/Write Penalty

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.1 (*Basic Concepts*), Page 680
> - **Exercise Type:** Practice Exercise 14.1
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** High. Foundational conceptual question explaining why index creation is a write-heavy trade-off in production databases.

**Question (Silberschatz 7e Exercise 14.1).**  
Indices speed query processing, but it is usually a bad idea to create indices on every attribute, and every combination of attributes, that are potential search keys. Explain why.

---

#### 1. Core Principles & Concept Overview

An index is an auxiliary physical access path designed to minimize disk block accesses for search keys during retrieval queries (`SELECT`). However, indices are not free abstractions:
- Every index consumes persistent disk storage and volatile buffer cache space.
- Any modification to the base table (`INSERT`, `UPDATE`, `DELETE`) requires synchronized updates across all indices defined on the altered attributes.
- The space of possible composite search keys experiences a combinatorial explosion: for a table with $k$ attributes, the number of non-empty subsets is $2^k - 1$, and ordered permutations total $\sum_{m=1}^{k} \frac{k!}{(k-m)!}$.

---

#### 2. Detailed Step-by-Step Solution

Creating indices on every attribute and combination of attributes is counter-productive due to five major technical factors:

1. **Storage Space Overhead:**
   - Each index requires its own set of disk blocks to store search keys, record pointers, and internal tree/bucket structures.
   - For secondary indices or multi-attribute composite keys, the aggregate storage required by the indices frequently exceeds the storage footprint of the original database relation itself by several multiples.

2. **DML Modification Penalty (Write Amplification):**
   - **Insertions:** An `INSERT` of a single tuple into a relation with $m$ indices requires $m$ separate index insertions. Each index insertion may cause B+-tree node splits, leaf reallocations, and random disk writes.
   - **Deletions:** A `DELETE` requires locating and deleting entries from all $m$ indices, potentially causing underflow merges and pointer redistribution.
   - **Updates:** An `UPDATE` modifying attribute values requires removing the old key and inserting the new key in each associated index. Write latency escalates linearly or super-linearly with $m$.

3. **Buffer Pool Contention and Cache Thrashing:**
   - Database buffer pools have finite main-memory capacity. As the number of active index structures grows, internal index blocks compete with base data pages for memory slots.
   - Cache hit ratios decline, resulting in frequent disk eviction, page faults, and increased disk I/O bottlenecks.

4. **Query Optimizer Latency and Sub-optimal Plan Selection:**
   - The relational query optimizer must evaluate search space combinations of access paths across all available indices.
   - Having dozens of overlapping indices increases query compilation time and can lead cost-based optimizers into sub-optimal plan selections due to imprecise statistical estimates.

5. **Combinatorial Infeasibility:**
   - For a relation with $k = 10$ attributes, indexing all combinations requires:
     
     $$
     \sum_{m=1}^{10} \binom{10}{m} = 2^{10} - 1 = 1,023 \text{ unordered sets}
     $$
     
   - If attribute ordering in composite indices is accounted for, permutations exceed $3.6 \times 10^6$, which is completely impossible to construct, maintain, or store.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Examiner Checklist
> - When asked about indexing trade-offs, divide your answer into **Storage Overhead**, **Maintenance (DML) Overhead**, **Buffer Contention**, and **Optimizer Overhead**.
> - Always mention: *"Read performance gains come at the expense of write latency and disk space."*

---

### Exercise 14.2 · Physical Uniqueness of Clustering Indices

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.2 (*Ordered Indices*), Page 680
> - **Exercise Type:** Practice Exercise 14.2
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Direct theoretical foundation for distinguishing clustering vs. secondary indices (tested in 2023 Q.8a).

**Question (Silberschatz 7e Exercise 14.2).**  
Is it possible in general to have two clustering indices on the same relation for different search keys? Explain your answer.

---

#### 1. Core Principles & Concept Overview

- **Clustering Index (Primary Index):** An index whose search key dictates the physical sequential storage ordering of records on persistent disk blocks.
- **Nonclustering Index (Secondary Index):** An index whose search key specifies an ordering different from the physical sequential storage order of the records.

```text
Clustering Index:   Key Order ──► [Disk Block 1] ──► [Disk Block 2] (Contiguous Sequential Order)
Secondary Index:    Key Order ──► Pointers scatter randomly across [Block 1, Block 5, Block 2...]
```

---

#### 2. Detailed Step-by-Step Solution

**No**, in general, it is **not possible** to have two clustering indices on the same relation for different search keys.

##### Mathematical & Physical Explanation:
1. **Physical Ordering Singularity:**
   - A single file of records stored on persistent storage media (e.g., magnetic disk or SSD) has exactly **one** physical sequence of records.
   - If a clustering index is constructed on search key $K_1$ (e.g., `ID`), records in data blocks must be arranged contiguously such that:
     
     $$
     \text{Record}_1(K_1) \le \text{Record}_2(K_1) \le \dots \le \text{Record}_N(K_1)
     $$
     
2. **Order Conflict with Key $K_2$:**
   - If a second clustering index were created on search key $K_2$ (e.g., `dept_name`), the records would simultaneously have to satisfy:
     
     $$
     \text{Record}_{p(1)}(K_2) \le \text{Record}_{p(2)}(K_2) \le \dots \le \text{Record}_{p(N)}(K_2)
     $$
     
   - Unless key $K_2$ has a strictly monotonic, 1-to-1 correlation with $K_1$ (meaning sorting by $K_1$ identically sorts by $K_2$), the two ordering constraints are mathematically incompatible on a single physical dataset.
3. **Role of Secondary Indices:**
   - Any other index built on $K_2$ must be a **nonclustering (secondary) index**. In a secondary index, index records are ordered by $K_2$, but the pointers refer to records distributed arbitrarily throughout the physically clustered blocks of $K_1$.

##### Edge Case Exception (Multiple Physical Replicas):
The only way a database system can support two clustering indices on different search keys for the same logical relation is by storing **two redundant physical copies** of the entire relation (e.g., via clustered materialized views or partitioned projections in columnar stores like Vertica/ClickHouse). However, for a single stored physical relation, only **one** clustering index can exist.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Distinctions
> - Do not confuse a *clustering index* with an index on a *primary key*. While clustering indices are often built on the primary key, a clustering index can be built on any attribute (e.g., `dept_name`).
> - However, the invariant remains: **exactly one clustering index per physical file**.

---

### Exercise 14.3 · B+-Tree Construction for $n = 4, 6, 8$

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.3 (*B+-Tree Index Files*), Page 680
> - **Exercise Type:** Practice Exercise 14.3 (Sub-parts a, b, c)
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Extremely high. Demonstrates the mechanics of B+-tree node invariants, leaf split points, and key promotion rules.

**Question (Silberschatz 7e Exercise 14.3).**  
Construct a B+-tree for the following set of key values:  

$$
(2, 3, 5, 7, 11, 17, 19, 23, 29, 31)
$$

Assume that the tree is initially empty and values are added in ascending order. Construct B+-trees for the cases where the number of pointers that will fit in one node is as follows:  
**a.** Four ($n = 4$)  
**b.** Six ($n = 6$)  
**c.** Eight ($n = 8$)

---

#### 1. Core Principles & Concept Overview

In Silberschatz 7e (§14.3), a B+-tree node has a maximum pointer fanout of $n$:
- **Leaf Node Structure:**
  - Maximum pointers: $n$ (stores up to $n - 1$ search-key values, and the $n$-th pointer points to the next sibling leaf).
  - Minimum keys: $\lceil (n - 1) / 2 \rceil$.
  - **Leaf Split Rule:** When an insertion causes a leaf node to exceed capacity (holding $n$ values), it is split into two nodes:
    - The first $\lceil n / 2 \rceil$ values remain in the left leaf.
    - The remaining values go to the new right leaf.
    - The smallest key in the new right leaf is **copied up** to the parent node.
- **Nonleaf (Internal) Node Structure:**
  - Maximum pointers: $n$ (stores up to $n - 1$ search-key values).
  - Minimum pointers: $\lceil n / 2 \rceil$ (minimum $\lceil n / 2 \rceil - 1$ keys). Root node is an exception: it can have as few as 2 pointers.
  - **Nonleaf Split Rule:** When an internal node with $n - 1$ keys receives a new key (totalling $n$ keys and $n + 1$ pointers):
    - Pointers $P_1 \dots P_{\lceil (n + 1) / 2 \rceil}$ and intervening keys stay in the left node.
    - Key at index $\lceil (n + 1) / 2 \rceil$ is **pushed up** to the parent (not retained in the child).
    - Remaining pointers and keys go to the new right internal node.

---

#### 2. Detailed Step-by-Step Solution

Insertion sequence: $2, 3, 5, 7, 11, 17, 19, 23, 29, 31$ in ascending order.

##### (a) Case 1: Four Pointers ($n = 4$)
- Max keys per leaf = $n - 1 = 3$. Min keys per leaf = $\lceil 3/2 \rceil = 2$.
- Max child pointers per nonleaf = $4$ (max $3$ keys). Min pointers = $\lceil 4/2 \rceil = 2$.
- Split point for leaf with 4 keys: $\lceil 4/2 \rceil = 2$ stay left, 2 go right.

**Step-by-step trace:**
1. Insert $2, 3, 5$: Leaf node $[2, 3, 5]$.
2. Insert $7$: Overfull $[2, 3, 5, 7]$. Split:
   - Left leaf: $[2, 3]$
   - Right leaf: $[5, 7]$
   - Copy up $5$ to Root.  
   - *Root:* $[5]$, pointing to $[2, 3]$ and $[5, 7]$.
3. Insert $11$: Right leaf becomes $[5, 7, 11]$ (valid, $\le 3$).
4. Insert $17$: Right leaf overfull $[5, 7, 11, 17]$. Split:
   - Left leaf: $[5, 7]$
   - Right leaf: $[11, 17]$
   - Copy up $11$ to Root.
   - *Root:* $[5, 11]$, pointing to $[2, 3]$, $[5, 7]$, $[11, 17]$.
5. Insert $19$: Right leaf becomes $[11, 17, 19]$ (valid, $\le 3$).
6. Insert $23$: Right leaf overfull $[11, 17, 19, 23]$. Split:
   - Left leaf: $[11, 17]$
   - Right leaf: $[19, 23]$
   - Copy up $19$ to Root.
   - *Root:* $[5, 11, 19]$, pointing to $[2, 3]$, $[5, 7]$, $[11, 17]$, $[19, 23]$. (Root has 3 keys, 4 pointers — full).
7. Insert $29$: Right leaf becomes $[19, 23, 29]$ (valid).
8. Insert $31$: Right leaf overfull $[19, 23, 29, 31]$. Split:
   - Left leaf: $[19, 23]$
   - Right leaf: $[29, 31]$
   - Copy up $29$ to Root.
   - *Root Overflow:* Root receives $29$, becoming $[5, 11, 19, 29]$ with 5 pointers ($P_1 \dots P_5$).
   - Split nonleaf root: $\lceil (4+1)/2 \rceil = 3$ pointers stay left ($P_1, P_2, P_3$ with keys $5, 11$).
   - Middle key $19$ is **pushed up** to create a new Root.
   - Pointers $P_4, P_5$ with key $29$ go to right internal node.

**Final Tree Structure for $n = 4$:**

```text
                         ┌──────┐
                         │  19  │  (Root)
                         └──┬─┬─┘
            ┌───────────────┘ └──────────────┐
            ▼                                ▼
       ┌─────────┐                      ┌─────────┐
       │  5 │ 11 │                      │   29    │  (Internal Nodes)
       └─┬───┬──┬┘                      └──┬────┬─┘
    ┌────┘   │  └─────┐              ┌─────┘    │
    ▼        ▼        ▼              ▼          ▼
 ┌─────┐  ┌─────┐  ┌──────┐       ┌──────┐   ┌──────┐
 │ 2│3 │─►│ 5│7 │─►│11│17 │──────►│19│23 │──►│29│31 │ (Leaves)
 └─────┘  └─────┘  └──────┘       └──────┘   └──────┘
```

---

##### (b) Case 2: Six Pointers ($n = 6$)
- Max keys per leaf = $n - 1 = 5$. Min keys per leaf = $\lceil 5/2 \rceil = 3$.
- Max pointers per nonleaf = $6$ (max $5$ keys). Min pointers = $\lceil 6/2 \rceil = 3$.
- Split point for leaf with 6 keys: $\lceil 6/2 \rceil = 3$ stay left, 3 go right.

**Step-by-step trace:**
1. Insert $2, 3, 5, 7, 11$: Leaf node $[2, 3, 5, 7, 11]$ (full, 5 keys).
2. Insert $17$: Overfull $[2, 3, 5, 7, 11, 17]$. Split:
   - Left leaf: $[2, 3, 5]$
   - Right leaf: $[7, 11, 17]$
   - Copy up $7$ to Root.
   - *Root:* $[7]$, pointing to $[2, 3, 5]$ and $[7, 11, 17]$.
3. Insert $19, 23$: Right leaf becomes $[7, 11, 17, 19, 23]$ (full, 5 keys).
4. Insert $29$: Right leaf overfull $[7, 11, 17, 19, 23, 29]$. Split:
   - Left leaf: $[7, 11, 17]$
   - Right leaf: $[19, 23, 29]$
   - Copy up $19$ to Root.
   - *Root:* $[7, 19]$, pointing to $[2, 3, 5]$, $[7, 11, 17]$, and $[19, 23, 29]$.
5. Insert $31$: Right leaf becomes $[19, 23, 29, 31]$ (4 keys $\le 5$, valid).

**Final Tree Structure for $n = 6$:**

```text
                  ┌─────────┐
                  │  7 │ 19 │  (Root)
                  └──┬───┬──┘
         ┌───────────┘   │   └───────────┐
         ▼               ▼               ▼
    ┌─────────┐    ┌───────────┐    ┌─────────────┐
    │ 2│ 3│ 5 │───►│ 7│ 11│ 17 │───►│19│23│29│ 31 │ (Leaves)
    └─────────┘    └───────────┘    └─────────────┘
```

---

##### (c) Case 3: Eight Pointers ($n = 8$)
- Max keys per leaf = $n - 1 = 7$. Min keys per leaf = $\lceil 7/2 \rceil = 4$.
- Max pointers per nonleaf = $8$ (max $7$ keys). Min pointers = $\lceil 8/2 \rceil = 4$.
- Split point for leaf with 8 keys: $\lceil 8/2 \rceil = 4$ stay left, 4 go right.

**Step-by-step trace:**
1. Insert $2, 3, 5, 7, 11, 17, 19$: Leaf node $[2, 3, 5, 7, 11, 17, 19]$ (full, 7 keys).
2. Insert $23$: Overfull $[2, 3, 5, 7, 11, 17, 19, 23]$. Split:
   - Left leaf: $[2, 3, 5, 7]$ (4 keys)
   - Right leaf: $[11, 17, 19, 23]$ (4 keys)
   - Copy up $11$ to Root.
   - *Root:* $[11]$, pointing to $[2, 3, 5, 7]$ and $[11, 17, 19, 23]$.
3. Insert $29, 31$: Right leaf becomes $[11, 17, 19, 23, 29, 31]$ (6 keys $\le 7$, valid).

**Final Tree Structure for $n = 8$:**

```text
                       ┌──────┐
                       │  11  │  (Root)
                       └──┬─┬─┘
            ┌─────────────┘ └─────────────┐
            ▼                             ▼
   ┌───────────────┐           ┌───────────────────┐
   │ 2 │ 3 │ 5 │ 7 │──────────►│ 11│ 17│ 19│ 23│ 29│31 │ (Leaves)
   └───────────────┘           └───────────────────┘
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Scoring Precision
> - Always show the intermediate split points explicitly. Examiners award marks for:
>   1. Identifying whether a key is **copied up** (leaf split: key remains in the right leaf) or **pushed up** (internal node split: key leaves the node and moves exclusively into the parent).
>   2. Drawing horizontal sibling pointers connecting all leaf nodes from left to right.

---

### Exercise 14.4 · Dynamic Operations on B+-Trees

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.3 (*B+-Tree Index Files*), Page 680
> - **Exercise Type:** Practice Exercise 14.4 (Operations a, b, c, d, e)
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Very High. Demonstrates B+-tree deletion algorithms, sibling merging (coalescing), and parent router updates.

**Question (Silberschatz 7e Exercise 14.4).**  
For each B+-tree of Exercise 14.3, show the form of the tree after each of the following series of operations:  
**a.** Insert 9.  
**b.** Insert 10.  
**c.** Insert 8.  
**d.** Delete 23.  
**e.** Delete 19.

---

#### 1. Core Principles & Concept Overview

- **Insertion:** Locates leaf, places entry in sorted order. If node exceeds capacity, split and promote median/smallest key.
- **Deletion:** Locates entry and deletes from leaf:
  - If leaf has $\ge \lceil (n - 1) / 2 \rceil$ keys, stop.
  - If leaf has too few keys (underflow), attempt to **coalesce (merge)** with adjacent sibling if their combined entries fit within $n - 1$ keys.
  - If combined entries exceed $n - 1$, perform **redistribution** by borrowing an entry from a sibling and updating the parent's separating key.
  - Sibling merging causes a key to be deleted from the parent, which can cascade upwards to reduce tree height.

---

#### 2. Detailed Step-by-Step Solution

##### 1. Tracking Tree $n = 4$ Across Operations

Starting with the final $n = 4$ tree from Exercise 14.3:

**a. Insert 9:**
- $9$ falls into leaf $[5, 7]$.
- $[5, 7]$ becomes $[5, 7, 9]$. (3 keys $\le 3$, fits without split).

**b. Insert 10:**
- $10$ falls into leaf $[5, 7, 9]$, making it overfull: $[5, 7, 9, 10]$.
- Split at $\lceil 4/2 \rceil = 2$:
  - Left leaf: $[5, 7]$
  - Right leaf: $[9, 10]$
  - Copy up $9$ to parent $[5, 11]$.
- Parent $[5, 11]$ receives $9$ and becomes $[5, 9, 11]$ (3 keys, 4 pointers $\le 4$, fits).
- *Internal Node 1:* $[5, 9, 11]$, pointing to $[2, 3]$, $[5, 7]$, $[9, 10]$, $[11, 17]$.

**c. Insert 8:**
- $8$ falls into leaf $[5, 7]$.
- Leaf becomes $[5, 7, 8]$ (3 keys $\le 3$, fits).

**d. Delete 23:**
- $23$ is deleted from leaf $[19, 23]$. Leaf becomes $[19]$ (1 key $\implies$ underflow, since $\lceil 3/2 \rceil = 2$).
- Check adjacent sibling $[29, 31]$: combined count $= 1 + 2 = 3 \le 3$. **Coalesce!**
- Merged leaf: $[19, 29, 31]$.
- Discard right leaf $[29, 31]$. Delete key $29$ from parent $[29]$.
- Parent now has 0 keys and 1 pointer (underflow, internal node requires $\ge 2$ pointers).
- Check sibling internal node $[5, 9, 11]$ (has 4 pointers). **Redistribute!**
  - Rightmost child of $[5, 9, 11]$ (pointer to $[11, 17]$) is transferred to the underfull right internal node.
  - Separating key $19$ in the root comes down to the right node; key $11$ moves up to become the new root key.
- *Root:* $[11]$
- *Left Internal:* $[5, 9]$, pointing to $[2, 3]$, $[5, 7, 8]$, $[9, 10]$.
- *Right Internal:* $[19]$, pointing to $[11, 17]$ and $[19, 29, 31]$.

```text
                         ┌──────┐
                         │  11  │  (Root)
                         └──┬─┬─┘
            ┌───────────────┘ └──────────────┐
            ▼                                ▼
        ┌───────┐                         ┌──────┐
        │ 5 │ 9 │                         │  19  │  (Internal Nodes)
        └──┬─┬─┬┘                         └──┬──┬┘
    ┌──────┘ │ └─────┐                  ┌────┘  │
    ▼        ▼       ▼                  ▼       ▼
 ┌─────┐  ┌───────┐ ┌────┐           ┌─────┐ ┌────────┐
 │ 2│3 │─►│ 5│7│8 │►│9│10│──────────►│11│17│►│19│29│31│ (Leaves)
 └─────┘  └───────┘ └────┘           └─────┘ └────────┘
```

**e. Delete 19:**
- $19$ is deleted from leaf $[19, 29, 31]$. Leaf becomes $[29, 31]$ (2 keys $\ge 2$, valid).
- *(Note on Router Key):* Under Silberschatz 7e (§14.3.3.2, p. 646), a key value deleted from a leaf that remains in an internal router node (`19`) does not strictly require modification unless underflow occurs. However, if routers are updated to match the smallest key in the right child, `19` in the internal node is updated to `29`.
- Final Leaves: $[2, 3]$, $[5, 7, 8]$, $[9, 10]$, $[11, 17]$, $[29, 31]$.

---

##### 2. Tracking Tree $n = 6$ Across Operations

Starting with $n = 6$ tree: Root $[7, 19]$; Leaves: $[2, 3, 5]$, $[7, 11, 17]$, $[19, 23, 29, 31]$.

**a. Insert 9:**
- $9$ goes into leaf $[7, 11, 17] \implies [7, 9, 11, 17]$ (4 keys $\le 5$, fits).

**b. Insert 10:**
- $10$ goes into leaf $[7, 9, 11, 17] \implies [7, 9, 10, 11, 17]$ (5 keys $\le 5$, full).

**c. Insert 8:**
- $8$ goes into leaf $[7, 9, 10, 11, 17] \implies$ Overfull: $[7, 8, 9, 10, 11, 17]$.
- Split at $\lceil 6/2 \rceil = 3$:
  - Left leaf: $[7, 8, 9]$
  - Right leaf: $[10, 11, 17]$
  - Copy up $10$ to Root.
- Root $[7, 19]$ becomes $[7, 10, 19]$ (3 keys, 4 pointers $\le 6$, fits).

**d. Delete 23:**
- $23$ is deleted from $[19, 23, 29, 31] \implies [19, 29, 31]$. (3 keys $\ge \lceil 5/2 \rceil = 3$, valid, no underflow).

**e. Delete 19:**
- $19$ is deleted from $[19, 29, 31] \implies [29, 31]$ (2 keys $\implies$ underflow, min is 3).
- Check sibling $[10, 11, 17]$: total keys $= 3 + 2 = 5 \le 5$. **Coalesce!**
- Merged leaf: $[10, 11, 17, 29, 31]$.
- Discard right leaf. Remove key $19$ from Root.
- *Root:* $[7, 10]$, pointing to $[2, 3, 5]$, $[7, 8, 9]$, and $[10, 11, 17, 29, 31]$.

```text
                  ┌─────────┐
                  │  7 │ 10 │  (Root)
                  └──┬───┬──┘
         ┌───────────┘   │   └───────────┐
         ▼               ▼               ▼
    ┌─────────┐    ┌─────────┐    ┌─────────────────┐
    │ 2│ 3│ 5 │───►│ 7│ 8│ 9 │───►│10│11│17│29│ 31  │ (Leaves)
    └─────────┘    └─────────┘    └─────────────────┘
```

---

##### 3. Tracking Tree $n = 8$ Across Operations

Starting with $n = 8$ tree: Root $[11]$; Leaves: $[2, 3, 5, 7]$, $[11, 17, 19, 23, 29, 31]$.

**a. Insert 9:** Leaf $[2, 3, 5, 7]$ becomes $[2, 3, 5, 7, 9]$ (5 keys $\le 7$).  
**b. Insert 10:** Leaf becomes $[2, 3, 5, 7, 9, 10]$ (6 keys $\le 7$).  
**c. Insert 8:** Leaf becomes $[2, 3, 5, 7, 8, 9, 10]$ (7 keys $\le 7$, full).  
**d. Delete 23:** Deleted from $[11, 17, 19, 23, 29, 31] \implies [11, 17, 19, 29, 31]$ (5 keys $\ge \lceil 7/2 \rceil = 4$, valid).  
**e. Delete 19:** Deleted from $[11, 17, 19, 29, 31] \implies [11, 17, 29, 31]$ (4 keys $\ge 4$, valid).  

**Final Tree Structure for $n = 8$:**
- *Root:* $[11]$
- *Leaf 1:* $[2, 3, 5, 7, 8, 9, 10]$
- *Leaf 2:* $[11, 17, 29, 31]$

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Crucial Rule on Deletion
> - Underflow threshold is strictly $\lceil (n - 1) / 2 \rceil$ for leaves.
> - When coalescing two leaf nodes, remember to **remove the separating key from the parent**. If the parent underflows, apply coalescing/redistribution recursively up to the root.

---

### Exercise 14.5 · Tree Height Under B*-Tree Redistribution

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.4.1 (*B+-Tree File Organization*), Page 680 (referencing Page 651)
> - **Exercise Type:** Practice Exercise 14.5
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Advanced analytical question on B*-tree space utilization ($\ge 66\%$) and resulting height bounds.

**Question (Silberschatz 7e Exercise 14.5).**  
Consider the modified redistribution scheme for B+-trees described on page 651. What is the expected height of the tree as a function of $n$?

---

#### 1. Core Principles & Concept Overview

On page 651–652, Silberschatz outlines the **B*-tree** variation:
- Instead of immediately splitting an overfull node, the system attempts to redistribute entries with an adjacent sibling node so that both are approximately two-thirds full.
- A split occurs only when **both** a node and its sibling are completely full. At that point, the two full nodes ($2n$ entries) are split into **three** nodes, each containing at least $\lfloor 2n / 3 \rfloor$ pointers.
- Minimum node occupancy increases from $50\%$ ($\lceil n / 2 \rceil$) to $66.7\%$ ($\lceil 2n / 3 \rceil$).

---

#### 2. Detailed Step-by-Step Solution

##### 1. Fanout Bounds in B*-Tree
Let $n$ be the maximum pointer capacity of a node, and let $K$ be the total number of search-key entries indexed:
- In a standard B+-tree, minimum fanout per internal node is:
  
  $$
  f_{\text{std}} = \left\lceil \frac{n}{2} \right\rceil
  $$
  
- In the modified redistribution scheme ($B^*$-tree), every non-root node is guaranteed to hold at least:
  
  $$
  f_{\text{B*}} = \left\lfloor \frac{2n}{3} \right\rfloor \approx \frac{2n}{3} \text{ pointers}
  $$

##### 2. Mathematical Height Derivation
Let $h$ denote the height of the tree (number of levels from root to leaf, where the root is at level 1):
1. **Level 1 (Root):** Contains at least 2 child pointers (in the worst case).
2. **Level 2:** Contains at least $2 \times \lfloor 2n/3 \rfloor$ pointers.
3. **Level 3:** Contains at least $2 \times (\lfloor 2n/3 \rfloor)^2$ pointers.
4. **Level $h$ (Leaves):** The total number of leaf nodes $L$ is bounded from below by:
   
   $$
   L \ge 2 \cdot \left( \left\lfloor \frac{2n}{3} \right\rfloor \right)^{h-2}
   $$

If the relation contains $K$ search keys, and each leaf node holds at least $\lfloor 2(n - 1) / 3 \rfloor$ keys, then:

$$
K \ge 2 \cdot \left( \left\lfloor \frac{2n}{3} \right\rfloor \right)^{h-2} \cdot \left\lfloor \frac{2(n - 1)}{3} \right\rfloor
$$

Solving for the maximum (worst-case) height $h$:

$$
\left( \left\lfloor \frac{2n}{3} \right\rfloor \right)^{h-2} \le \frac{K}{2 \lfloor 2(n-1)/3 \rfloor}
$$

Taking the logarithm with base $\lfloor 2n/3 \rfloor$:

$$
h - 2 \le \log_{\lfloor 2n/3 \rfloor} \left( \frac{K}{2 \lfloor 2(n-1)/3 \rfloor} \right)
$$

$$
h \le \left\lceil \log_{\lfloor 2n/3 \rfloor} \left( \frac{K}{2 \lfloor 2(n-1)/3 \rfloor} \right) \right\rceil + 2
$$

##### 3. Expected Height Expression
Under average operating conditions, random insertions produce an expected node fanout of:

$$
f_{\text{avg}} \approx \frac{n + \lfloor 2n/3 \rfloor}{2} \approx \frac{5n}{6}
$$

Therefore, the **expected height** of the tree as a function of $n$ is:

$$
h_{\text{expected}} \approx \left\lceil \log_{\frac{5n}{6}} (K) \right\rceil \in O\left( \log_{\frac{2n}{3}} K \right)
$$

**Comparative Insight:** Because the logarithm base increases from $n/2$ to $2n/3$, the height of a $B^*$-tree is strictly less than or equal to that of a standard B+-tree for the same dataset, reducing random disk I/O accesses during traversals.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Theory vs. Implementation
> Mention that while $B^*$-trees decrease tree height and save disk storage (66% minimum utilization vs. 50%), the update algorithm is more complex because an insertion or deletion must inspect two adjacent sibling nodes rather than one, increasing concurrency locking contention.

---

### Exercise 14.6 · B+-Tree Range Query Iterator Design

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.3.2 (*Querying a B+-Tree*), Page 680
> - **Exercise Type:** Practice Exercise 14.6
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Medium-High. bridges database engine query execution pipelines (Volcano iterator model) with physical B+-tree leaf chaining.

**Question (Silberschatz 7e Exercise 14.6).**  
Give pseudocode for a B+-tree function `findRangeIterator()`, which is like the function `findRange()`, except that it returns an iterator object, as described in Section 14.3.2. Also give pseudocode for the iterator class, including the variables in the iterator object, and the `next()` method.

---

#### 1. Core Principles & Concept Overview

- Standard `findRange(lb, ub)` loads all matching record pointers into a large in-memory collection and returns it. This causes high memory consumption and latency when the range spans millions of records.
- **Iterator Pattern (Volcano Model / Cursor):** Returns a stateful cursor immediately after locating the first matching leaf. Successive records are fetched on demand via `next()`.
- The iterator maintains state: a pointer to the current leaf block, the current slot index within that block, and the upper bound search key $ub$.

---

#### 2. Detailed Step-by-Step Solution

```text
[findRangeIterator(lb, ub)]
          │
          │ Traverses Root ──► Internal ──► Leaf
          ▼
Instantiates Iterator(startLeaf, startIndex, ub)
          │
          ▼
Client calls iter.next() ──► Yields record pointer
                             Advances slot; if at end of leaf, 
                             follows P_n to next sibling leaf!
```

##### 1. Factory Function: `findRangeIterator(lb, ub)`

```java
// Function that locates the starting leaf and returns an Iterator instance
function findRangeIterator(SearchKey lb, SearchKey ub) -> BTreeRangeIterator {
    Node C = root;
    
    // Traverse down to the leaf level
    while (C is not a leaf node) {
        int i = 1;
        while (i <= C.numKeys && lb > C.keys[i]) {
            i = i + 1;
        }
        C = C.pointers[i]; // Follow child pointer
    }
    
    // At leaf node C: find the first key >= lb
    int i = 1;
    while (i <= C.numKeys && C.keys[i] < lb) {
        i = i + 1;
    }
    
    // Return initialized iterator object
    return new BTreeRangeIterator(C, i, ub);
}
```

##### 2. Class Definition: `BTreeRangeIterator`

```java
class BTreeRangeIterator {
    // Instance variables preserving cursor state
    private LeafNode currentNode;   // Pointer to current leaf block
    private int currentIndex;       // Current key index within currentNode
    private SearchKey upperBound;   // Maximum key value to retrieve

    // Constructor
    public BTreeRangeIterator(LeafNode startNode, int startIndex, SearchKey ub) {
        this.currentNode = startNode;
        this.currentIndex = startIndex;
        this.upperBound = ub;
        
        // Handle case where startIndex exceeds startNode capacity
        normalizeCursor();
    }

    // Helper to advance across leaf boundaries if current node is exhausted
    private void normalizeCursor() {
        while (this.currentNode != null && this.currentIndex > this.currentNode.numKeys) {
            this.currentNode = this.currentNode.nextSiblingPointer; // Follow P_n
            this.currentIndex = 1; // Reset index to first slot in next leaf
        }
    }

    // Returns true if there are more records in [lb, ub]
    public boolean hasNext() {
        if (this.currentNode == null) {
            return false;
        }
        // Check if current key exceeds upper bound
        if (this.currentNode.keys[this.currentIndex] > this.upperBound) {
            return false;
        }
        return true;
    }

    // Returns next RecordPointer and advances cursor
    public RecordPointer next() {
        if (!hasNext()) {
            return null; // or throw NoSuchElementException
        }

        // 1. Retrieve the record pointer
        RecordPointer result = this.currentNode.pointers[this.currentIndex];

        // 2. Advance cursor
        this.currentIndex = this.currentIndex + 1;

        // 3. Move to next sibling leaf if this leaf is exhausted
        normalizeCursor();

        return result;
    }
}
```

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Key Details
> Ensure your pseudocode explicitly handles the **leaf boundary transition**: when `currentIndex > currentNode.numKeys`, the iterator must follow pointer $P_n$ (`currentNode.nextSiblingPointer`) to the adjacent block on disk and reset `currentIndex = 1`.

---

### Exercise 14.7 · Leaf Occupancy Under Sequential Insertion

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.4.4 (*Bulk Loading of B+-Trees*), Page 680
> - **Exercise Type:** Practice Exercise 14.7
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** High. Explains why sequentially inserting sorted data into a B+-tree results in pathological 50% storage waste without bulk loading.

**Question (Silberschatz 7e Exercise 14.7).**  
What would the occupancy of each leaf node of a B+-tree be if index entries were inserted in sorted order? Explain why.

---

#### 1. Core Principles & Concept Overview

When records are inserted into a B+-tree in strictly ascending order:
1. Every new search-key value is strictly greater than all existing keys in the tree.
2. Therefore, every insertion target is guaranteed to be the **rightmost leaf node**.
3. No new key is ever inserted into any previously closed leaf node to the left.

---

#### 2. Detailed Step-by-Step Solution

##### Leaf Occupancy Analysis:
- Let $n$ be the maximum pointer capacity of a leaf node (holding up to $n - 1$ search-key values).
- When the rightmost leaf node fills up and receives its $n$-th value, it is split:
  - According to the B+-tree split algorithm (§14.3.3.1), the first $\lceil n / 2 \rceil$ values remain in the existing left leaf node.
  - The remaining $n - \lceil n / 2 \rceil = \lfloor n / 2 \rfloor$ values are moved into a newly allocated right leaf node.
  - The smallest key of the new leaf is copied to the parent.
- **The Freezing Effect:**  
  Because all subsequent incoming search keys are strictly greater than all keys processed so far, all future insertions will target the new rightmost leaf node (or subsequent leaves created further to the right).  
  **No additional keys will ever be added to the left node.**

##### Conclusion:
- **All non-rightmost leaf nodes:** Will remain frozen at **exactly** $\lceil n / 2 \rceil$ search-key entries.
- **Occupancy Percentage:**  
  
  $$
  \text{Occupancy} \approx \frac{\lceil n/2 \rceil}{n - 1} \approx 50\%
  $$
  
- **Rightmost leaf node:** Contains between $\lfloor n / 2 \rfloor$ and $n - 1$ keys, depending on how recently the last split occurred.

**Practical Implication:** Inserting presorted data one record at a time produces the worst-case space utilization allowed by B+-tree invariants (50% internal fragmentation). This is the direct justification for **Bulk Loading** algorithms (§14.4.4).

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Note
> Clearly state that *all interior leaves are frozen at minimum capacity ($\lceil n/2 \rceil$)*, while only the single rightmost leaf fluctuates.

---

### Exercise 14.8 · Bulk Loading Cost & Bottom-Up Construction

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.4.4 (*Bulk Loading of B+-Trees*), Page 680
> - **Exercise Type:** Practice Exercise 14.8 (Sub-parts a, b, c)
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Very High. Quantitative comparison between naive one-by-one insertion vs. external sort bulk loading.

**Question (Silberschatz 7e Exercise 14.8).**  
Suppose you have a relation $r$ with $n_r$ tuples on which a secondary B+-tree is to be constructed.  
**a.** Give a formula for the cost of building the B+-tree index by inserting one record at a time. Assume each block will hold an average of $f$ entries and that all levels of the tree above the leaf are in memory.  
**b.** Assuming a random disk access takes 10 milliseconds, what is the cost of index construction on a relation with 10 million records?  
**c.** Write pseudocode for bottom-up construction of a B+-tree, which was outlined in Section 14.4.4. You can assume that a function to efficiently sort a large file is available.

---

#### 1. Core Principles & Concept Overview

- **One-by-one Insertion Cost:** For an unindexed relation, inserting entries one by one in arbitrary order causes random disk reads and random disk writes for every leaf block accessed.
- **Bulk Loading (Bottom-Up Construction):** 
  1. Extract `(search_key, record_pointer)` pairs into a flat file.
  2. Sort the file on `search_key` using external merge sort (sequential I/O).
  3. Pack the sorted entries sequentially into leaf blocks up to maximum fill capacity.
  4. Build nonleaf internal levels bottom-up level by level.

---

#### 2. Detailed Step-by-Step Solution

##### (a) Cost Formula for One-at-a-Time Construction

Assumptions:
- Number of tuples: $n_r$.
- All internal levels above the leaves reside in main memory buffer pool (0 disk I/O for internal nodes).
- Average leaf node capacity: $f$ entries. Total leaf blocks $\approx \lceil n_r / f \rceil$.
- When $n_r$ is large, consecutive insertions target random leaf blocks that do not reside in memory cache.

For each of the $n_r$ records:
1. **Random Read:** Read the target leaf block from disk into memory $\implies 1 \text{ read}$.
2. **Random Write:** After modifying the leaf in memory, write the dirty block back to disk $\implies 1 \text{ write}$.
3. **Split Allocations:** Approximately $n_r / f$ splits occur, each writing an additional newly allocated leaf block to disk.

$$
\text{Total Disk I/O Operations} \approx 2 \cdot n_r + \frac{n_r}{f} \approx 2 n_r \text{ random disk I/Os}
$$

If $t_{\text{seek}}$ represents the average random disk access time:

$$
\text{Cost}_{\text{one-at-a-time}} = 2 n_r \cdot t_{\text{seek}}
$$

---

##### (b) Numerical Cost for 10 Million Records

Given:
- $n_r = 10,000,000 = 10^7$ records.
- $t_{\text{seek}} = 10 \text{ ms} = 0.010 \text{ seconds}$.

$$
\text{Total I/O Time} \approx 2 \cdot 10^7 \cdot 0.010 \text{ s} = 200,000 \text{ seconds}
$$

Converting into hours:

$$
\text{Time in Hours} = \frac{200,000}{3,600} \approx 55.56 \text{ hours} \approx 2.31 \text{ days!}
$$

*(Including leaf split writes with $f \approx 100$ adds an extra $10^5 \times 0.01\text{ s} = 1,000\text{ s}$, yielding $\approx 55.83\text{ hours}$).*

---

##### (c) Pseudocode for Bottom-Up B+-Tree Construction

```java
// Bottom-up construction algorithm (Bulk Loading)
function bulkLoadBTree(File unsortedRecords, int n, float fillFactor) -> Node {
    // Step 1: Extract (search_key, record_pointer) and sort externally
    File sortedEntries = externalMergeSort(unsortedRecords, keyAttribute);

    // Calculate maximum entries per leaf according to desired fillFactor (e.g., 0.9)
    int maxLeafKeys = floor((n - 1) * fillFactor);
    
    List<LeafNode> currentLevelNodes = new List<LeafNode>();
    LeafNode prevLeaf = null;

    // Step 2: Pack sorted entries sequentially into leaf blocks
    while (sortedEntries.hasNext()) {
        LeafNode leaf = new LeafNode(n);
        while (leaf.numKeys < maxLeafKeys && sortedEntries.hasNext()) {
            Entry e = sortedEntries.readNext();
            leaf.addEntry(e.key, e.pointer);
        }
        
        // Link sibling pointers (P_n)
        if (prevLeaf != null) {
            prevLeaf.nextSiblingPointer = leaf;
        }
        prevLeaf = leaf;
        currentLevelNodes.add(leaf);
        writeBlockToDiskSequentially(leaf);
    }

    // Step 3: Build nonleaf levels bottom-up
    List<Node> childLevel = currentLevelNodes;
    
    while (childLevel.size() > 1) {
        List<InternalNode> nextLevel = new List<InternalNode>();
        int maxInternalKeys = floor((n - 1) * fillFactor);
        
        int i = 0;
        while (i < childLevel.size()) {
            InternalNode parent = new InternalNode(n);
            
            // First pointer points to first child without a preceding key
            parent.pointers[1] = childLevel.get(i);
            i = i + 1;
            
            // Remaining pointers are paired with separating router keys
            while (parent.numKeys < maxInternalKeys && i < childLevel.size()) {
                Node child = childLevel.get(i);
                SearchKey routerKey = child.getSmallestKey();
                
                parent.addKeyAndPointer(routerKey, child);
                i = i + 1;
            }
            nextLevel.add(parent);
            writeBlockToDiskSequentially(parent);
        }
        childLevel = nextLevel; // Move up one level
    }

    // The single remaining node is the root
    Node root = childLevel.get(0);
    return root;
}
```

**Efficiency Gain:** Bulk loading replaces $200,000$ seconds of random I/O with sequential streaming I/O and external sorting, building the entire index in under **10 minutes**!

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Calculations
> Memorize the calculation: $10^7 \text{ records} \times 2 \times 10\text{ ms} = 200,000\text{ s} \approx 55.6\text{ hours}$. Showing the contrast between random disk head movement vs. sequential stream write is the core answer requirement.

---

### Exercise 14.11 · Read Optimization in LSM-Trees

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.7 (*Write-Optimized Indices*), Page 681
> - **Exercise Type:** Practice Exercise 14.11
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Medium. Modern database indexing concept (RocksDB, Cassandra, Bigtable) testing LSM read/write trade-offs.

**Question (Silberschatz 7e Exercise 14.11).**  
In write-optimized trees such as the LSM tree or the stepped-merge index, entries in one level are merged into the next level only when the level is full. Suggest how this policy can be changed to improve read performance during periods when there are many reads but no updates.

---

#### 1. Core Principles & Concept Overview

- **Log-Structured Merge Tree (LSM-Tree):** Appends incoming writes to an in-memory buffer (`memtable`). When full, the `memtable` is flushed to disk as an immutable sorted run (Level $L_0$).
- When Level $L_i$ fills up, it is merged into Level $L_{i+1}$ via background **compaction**.
- **Read Amplification Bottleneck:** Because data is divided across multiple levels, a read query must check the memtable, $L_0$ files, and subsequent levels until the key is found or all levels are examined.

```text
Incoming Write ──► [Memtable (RAM)] ──► Flushed to L0 ──► L1 ──► L2 ──► L3 (Disk)
Point Read     ──► Searches Memtable ──► Checks L0 ───► Checks L1 ──► (Multiple Disk Seeks)
```

---

#### 2. Detailed Step-by-Step Solution

##### Policy Modifications for Read-Heavy / Idle Workloads:

1. **Eager / Proactive Background Compaction:**
   - Under standard policy, compaction occurs lazily—only when a level is $100\%$ full.
   - When the system detects a read-heavy workload with zero or minimal write traffic, it can trigger **proactive early compaction**:
     - Consolidate multiple runs from $L_0$ and $L_1$ into $L_2$ even if levels are only partially filled.
     - Eliminate duplicate historical versions of updated records and purge deleted records (`tombstones`).
   - *Benefit:* Minimizes the number of active SSTable files across levels, reducing read probes from $O(\text{Levels})$ down to 1.

2. **Major Compaction into a Single Unified Level:**
   - During extended read-only periods, execute a **major compaction**, merging all existing disk levels into a single, fully sorted B+-tree or single SSTable level.
   - *Benefit:* Point lookups and range scans access exactly one sorted component without multi-way merging.

3. **Dynamic Bloom Filter Reconstruction:**
   - Use the quiet write period to recompute and optimize **Bloom filters** for the remaining levels, allocating more bits per key to lower false-positive rates to near zero.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Conceptual Summary
> State clearly: *"Lazy compaction optimizes for write throughput; eager/proactive compaction optimizes for read latency."*

---

### Exercise 14.13 · Bitmap Index Construction & Range Evaluation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.9 (*Bitmap Indices*), Page 681 (referencing Figure 14.1)
> - **Exercise Type:** Practice Exercise 14.13 (Sub-parts a, b)
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Very High. Demonstrates bitwise logic, hardware-level boolean execution, and range query processing.

**Question (Silberschatz 7e Exercise 14.13).**  
Consider the *instructor* relation shown in Figure 14.1.  
**a.** Construct a bitmap index on the attribute *salary*, dividing salary values into four ranges: below 50,000, 50,000 to below 60,000, 60,000 to below 70,000, and 70,000 and above.  
**b.** Consider a query that requests all instructors in the Finance department with salary of 80,000 or more. Outline the steps in answering the query, and show the final and intermediate bitmaps constructed to answer the query.

---

#### 1. Core Principles & Concept Overview

- A **bitmap** is an array of bits where the $i$-th bit corresponds to the $i$-th record in the relation.
- The $i$-th bit is set to `1` if record $i$ satisfies the predicate, and `0` otherwise.
- Complex multi-attribute queries are answered by performing bitwise Boolean operations (`AND`, `OR`, `NOT`) in CPU registers over the bitmaps, without touching the underlying relation until matching record positions are identified.

---

#### 2. Detailed Step-by-Step Solution

##### 1. Reference Data: Instructor Relation (Figure 14.1)
The 12 records of the *instructor* relation in sorted order of `ID` (record numbers $0$ to $11$) are:

| Rec ID ($i$) | ID | Name | Dept Name | Salary (\$) |
| :---: | :---: | :--- | :--- | :---: |
| **0** | 10101 | Srinivasan | Comp. Sci. | 65,000 |
| **1** | 12121 | Wu | Finance | 90,000 |
| **2** | 15151 | Mozart | Music | 40,000 |
| **3** | 22222 | Einstein | Physics | 95,000 |
| **4** | 32343 | El Said | History | 60,000 |
| **5** | 33456 | Gold | Physics | 87,000 |
| **6** | 45565 | Katz | Comp. Sci. | 75,000 |
| **7** | 58583 | Califieri | History | 62,000 |
| **8** | 76543 | Singh | Finance | 80,000 |
| **9** | 76766 | Crick | Biology | 72,000 |
| **10** | 83821 | Brandt | Comp. Sci. | 92,000 |
| **11** | 98345 | Kim | Elec. Eng. | 80,000 |

---

##### (a) Construction of Range Bitmap Index on `salary`

We divide salaries into four range categories:
1. $R_1$: $\text{Salary} < 50,000$
2. $R_2$: $50,000 \le \text{Salary} < 60,000$
3. $R_3$: $60,000 \le \text{Salary} < 70,000$
4. $R_4$: $\text{Salary} \ge 70,000$

Evaluating each record $i \in \{0 \dots 11\}$:
- **Record 0 (65k):** Falls in $R_3$
- **Record 1 (90k):** Falls in $R_4$
- **Record 2 (40k):** Falls in $R_1$
- **Record 3 (95k):** Falls in $R_4$
- **Record 4 (60k):** Falls in $R_3$
- **Record 5 (87k):** Falls in $R_4$
- **Record 6 (75k):** Falls in $R_4$
- **Record 7 (62k):** Falls in $R_3$
- **Record 8 (80k):** Falls in $R_4$
- **Record 9 (72k):** Falls in $R_4$
- **Record 10 (92k):** Falls in $R_4$
- **Record 11 (80k):** Falls in $R_4$

**Resulting 12-Bit Bitmaps (bit 0 on the left, bit 11 on the right):**

| Range Identifier | Salary Condition | Bit Sequence (Rec 0 $\dots$ Rec 11) |
| :--- | :--- | :---: |
| **Bitmap $B_{R1}$** | $\text{Salary} < 50\text{k}$ | `0 0 1 0 0 0 0 0 0 0 0 0` |
| **Bitmap $B_{R2}$** | $50\text{k} \le \text{Salary} < 60\text{k}$ | `0 0 0 0 0 0 0 0 0 0 0 0` |
| **Bitmap $B_{R3}$** | $60\text{k} \le \text{Salary} < 70\text{k}$ | `1 0 0 0 1 0 0 1 0 0 0 0` |
| **Bitmap $B_{R4}$** | $\text{Salary} \ge 70\text{k}$ | `0 1 0 1 0 1 1 0 1 1 1 1` |

---

##### (b) Query Evaluation: Finance Instructors with $\text{Salary} \ge 80,000$

**Query:**
```sql
SELECT * FROM instructor WHERE dept_name = 'Finance' AND salary >= 80000;
```

###### Step 1: Department Bitmap
The bitmap for predicate `dept_name = 'Finance'` is constructed by setting bit $i = 1$ if record $i$ belongs to Finance:
- Record 1 (Wu) and Record 8 (Singh) belong to Finance.
- **$B_{\text{Finance}}$** = `0 1 0 0 0 0 0 0 1 0 0 0`

###### Step 2: Salary Predicate Bitmap ($\text{Salary} \ge 80,000$)
- From the instructor table, instructors with salary $\ge 80,000$ are:
  - Rec 1 (90k), Rec 3 (95k), Rec 5 (87k), Rec 8 (80k), Rec 10 (92k), Rec 11 (80k).
- **$B_{\text{Salary} \ge 80\text{k}}$** = `0 1 0 1 0 1 0 0 1 0 1 1`  
  *(Note: Rec 6 [75k] and Rec 9 [72k] have bit `0` because they are $< 80\text{k}$)*.

###### Step 3: Bitwise Intersection (AND)
Compute the bitwise `AND` between the two intermediate bitmaps:

```text
  B_Finance:             0 1 0 0 0 0 0 0 1 0 0 0
AND
  B_Salary>=80k:         0 1 0 1 0 1 0 0 1 0 1 1
─────────────────────────────────────────────────
  Final Result Bitmap:   0 1 0 0 0 0 0 0 1 0 0 0
```

###### Step 4: Record Retrieval
- Scan the result bitmap: bit positions with value `1` are **index 1** and **index 8**.
- Fetch Record 1: `(12121, Wu, Finance, 90000)`
- Fetch Record 8: `(76543, Singh, Finance, 80000)`
- Only 2 records are retrieved from disk, with zero wasted block scans!

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Presentation Standard
> Always display the intermediate bitmaps and write out the vertical bitwise `AND` calculation clearly. Examiners verify both the bit strings and the final identified records (`Wu` and `Singh`).

---

### Exercise 14.14 · Spatial Point Lookup: B+-Tree vs. R-Tree

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.8 (*Spatial Data*), Page 681–682
> - **Exercise Type:** Practice Exercise 14.14
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** High. Compares one-dimensional ordered structures (B+-trees) with multi-dimensional spatial indices (R-trees) under point query workloads.

**Question (Silberschatz 7e Exercise 14.14).**  
Suppose you have a relation containing the $x, y$ coordinates and names of restaurants. Suppose also that the only queries that will be asked are of the following form: The query specifies a point and asks if there is a restaurant exactly at that point. Which type of index would be preferable, R-tree or B-tree? Why?

---

#### 1. Core Principles & Concept Overview

- **B+-Tree:** Imposes a strict total linear order on one-dimensional search keys or lexicographically ordered composite keys $(x, y)$.
- **R-Tree:** A multi-dimensional bounding-box hierarchy designed for spatial objects (points, rectangles, polygons) to support bounding-box and region intersection queries.

---

#### 2. Detailed Step-by-Step Solution

A **B+-tree (or B-tree) index on the composite search key $(x, y)$** is distinctly preferable to an R-tree for this specific workload.

##### Reasons:

1. **Exact-Match Total Ordering vs. Bounding Box Overlaps:**
   - In a composite B+-tree with search key $(x, y)$, entries are ordered lexicographically:
     
     $$
     (x_1, y_1) < (x_2, y_2) \iff (x_1 < x_2) \lor (x_1 = x_2 \land y_1 < y_2)
     $$
     
   - Looking up an exact point $(x_q, y_q)$ traverses a **single, unique root-to-leaf path** of length $O(\log_B N)$. Zero backtracking is required.
   - In contrast, internal nodes of an R-tree store Minimum Bounding Boxes (MBRs) that **frequently overlap** in spatial dimensions. A point $(x_q, y_q)$ may fall inside multiple overlapping bounding boxes, forcing the search algorithm to explore **multiple downward branches**, leading to worst-case $O(N)$ lookup behavior.

2. **Higher Fanout and Lower Tree Height:**
   - A B+-tree node stores simple coordinate scalar pairs $(x, y)$ and 8-byte child pointers.
   - An R-tree node must store 4 coordinate values per child to define the bounding box $[x_{\text{min}}, y_{\text{min}}, x_{\text{max}}, y_{\text{max}}]$ in addition to child pointers.
   - Consequently, the fanout $n$ of an R-tree node is significantly smaller than that of a B+-tree node of the same block size. A smaller fanout results in a taller tree and more disk I/O operations per query.

3. **Maintenance Simplicity:**
   - B+-tree splits and rebalancing are deterministic and simple.
   - R-tree insertions require complex, computationally expensive MBR expansion heuristics (e.g., quadratic split, R*-tree topological sort) to minimize bounding box area and overlap.

**Conclusion:** R-trees are designed for spatial range queries (e.g., *"Find all restaurants within a 5 km rectangle"*) or nearest-neighbor searches where coordinates cannot be sorted independently. For strictly exact point lookups (`x = ? AND y = ?`), the composite B+-tree is superior in speed, storage, and predictability.

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Pitfall
> Do not assume spatial data *must* always use an R-tree! The choice of index structure depends entirely on the **query workload**. For exact equality point queries, B+-tree is strictly superior.

---

### Exercise 14.15 · Nearest-Neighbor via Circular Region Queries

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.8 (*Spatial Data*), Page 682
> - **Exercise Type:** Practice Exercise 14.15
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **RUET Relevance:** Medium-High. Algorithmic problem-solving adapting region query primitives to nearest-neighbor search.

**Question (Silberschatz 7e Exercise 14.15).**  
Suppose you have a spatial database that supports region queries with circular regions, but not nearest-neighbor queries. Describe an algorithm to find the nearest neighbor by making use of multiple region queries.

---

#### 1. Core Principles & Concept Overview

- Given: Oracle function `regionQuery(Q, r)` that returns the set of all database points lying within distance $r$ from query point $Q$:
  
  $$
  \text{Disk}(Q, r) = \{ P \mid \text{dist}(Q, P) \le r \}
  $$
  
- Objective: Find the single point $P^* \ne Q$ that minimizes $\text{dist}(Q, P^*)$.
- Challenge: If initial radius $r$ is too small, the query returns 0 points. If $r$ is too large, the query returns millions of irrelevant points.
- Solution: **Iterative Radius Doubling (Exponential Expansion) with Bound Tightening**.

---

#### 2. Detailed Step-by-Step Solution

```text
    [Query Point Q]
         │
         ├─── Probe 1: Radius r (Empty)
         │
         ├─────── Probe 2: Radius 2r (Empty)
         │
         ├─────────────── Probe 3: Radius 4r (Returns candidates {P1, P2})
         │                Calculate d_min = dist(Q, P1)
         │
         ▼
    Candidate d_min <= 4r guaranteed to be true Nearest Neighbor!
```

##### Algorithmic Steps:

1. **Initial Radius Estimation:**
   - Estimate an initial radius $r_0$ based on data density. If the database indexes $N$ points across a total geographic area $A$, the average area per point is $A / N$.
   - Set initial radius $r_0 = \sqrt{\frac{A}{\pi N}}$ (or a small system-defined constant $\epsilon$).

2. **Exponential Expansion (Finding an Enclosing Radius):**
   - Execute $S = \text{regionQuery}(Q, r)$.
   - While $S$ is empty (or contains only $Q$ itself):
     - Double the search radius: $r \leftarrow 2 \cdot r$.
     - Re-execute $S = \text{regionQuery}(Q, r)$.
   - Because space is bounded and $N \ge 1$, this loop terminates in $O(\log(r_{\text{max}} / r_0))$ iterations.

3. **Candidate Identification and Bound Tightening:**
   - Let $S = \{P_1, P_2, \dots, P_k\}$ be the non-empty set of points returned from the first successful query with radius $r$.
   - Calculate Euclidean distance from $Q$ to each candidate:
     
     $$
     d_i = \text{dist}(Q, P_i) = \sqrt{(Q.x - P_i.x)^2 + (Q.y - P_i.y)^2}
     $$
     
   - Identify the point with minimum distance:
     
     $$
     P_{\text{min}} = \arg\min_{P_i \in S} d_i, \quad \text{with } d_{\text{min}} = \text{dist}(Q, P_{\text{min}})
     $$

4. **Correctness & Termination Guarantee:**
   - Is it possible that a point closer than $P_{\text{min}}$ exists?
   - Any point closer than $P_{\text{min}}$ must have a distance $d < d_{\text{min}} \le r$.
   - However, our query `regionQuery(Q, r)` has **already returned all points** within radius $r$.
   - Therefore, the disk $\text{Disk}(Q, d_{\text{min}})$ is completely contained inside $\text{Disk}(Q, r)$, meaning all candidate points within distance $d_{\text{min}}$ are already members of $S$.
   - Hence, $P_{\text{min}}$ is **provably the true nearest neighbor**, and no further queries are needed!

---

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Correctness Invariant
> Emphasize step 4: because $d_{\text{min}} \le r$, and `regionQuery(Q, r)` retrieved *all* points within radius $r$, the closest point in that set is guaranteed to be the global nearest neighbor without requiring a second verification query.

---

### Exercise 14.16 · Dense vs. Sparse Index Selection Criteria

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 14, Section 14.2.1 (*Dense and Sparse Indices*), Page 682
> - **Exercise Type:** Standard Exercise 14.16
> - **Subtopic:** `T13.3` · Indexing: dense vs sparse, B+-tree
> - **Past RUET Direct Hits:** ⚠️ **Tested directly in 2023 Q.8(a) [2m]**
> - **Cross-Reference:** `Topicwise_answers_exam_style/T13_Security_Indexing_and_Hashing.md`

**Question (Silberschatz 7e Exercise 14.16).**  
When is it preferable to use a dense index rather than a sparse index? Explain your answer.

---

#### 1. Core Principles & Concept Overview

- **Dense Index:** Contains an index record for **every** search-key value in the data file.
- **Sparse Index:** Contains an index record for only **some** search-key values (typically one entry per disk block). Requires the underlying data file to be physically sorted on the search key.

```text
Dense Index:    [Key 1] ──► Record 1    Sparse Index:   [Key 1] ──► Block 1 (Rec 1, 2, 3)
                [Key 2] ──► Record 2                    [Key 4] ──► Block 2 (Rec 4, 5, 6)
                [Key 3] ──► Record 3
```

---

#### 2. Detailed Step-by-Step Solution

It is preferable to use a **dense index** over a sparse index in the following four operational scenarios:

1. **Nonclustering (Secondary) Indices:**
   - If the data file is not physically sorted on the search key, a sparse index **cannot be used at all**.
   - Because records with consecutive key values are scattered randomly across different disk blocks, an index entry must exist for every individual search key to locate its record. Thus, secondary indices are always dense.

2. **Index-Only Queries (Covering Indices):**
   - When a query requests only the indexed search key or an existence check (`WHERE key = ?` or `SELECT key`), a dense index can answer the query entirely in memory/index without fetching the data block from disk.
   - In a sparse index, the system cannot verify whether an intermediate key exists without reading the actual data block from disk, incurring an extra physical disk I/O.

3. **Faster Random Point Lookups:**
   - In a dense index, locating the search key in the index yields a direct pointer to the record (or its duplicate list), requiring only 1 subsequent data block read.
   - In a sparse index, the index pointer leads to the beginning of a data block. The system must then perform a CPU sequential scan or binary search through the records within the block. When records are variable-length or blocks are large, dense indices provide faster lookup.

4. **Small Relations / In-Memory Resident Indices:**
   - When memory is sufficient to store the entire index, the storage savings of a sparse index become irrelevant. The direct addressing speed of a dense index is preferred.

##### Summary Comparison Table (Exam-Ready):

| Evaluation Feature | Dense Index | Sparse Index |
| :--- | :--- | :--- |
| **Number of Entries** | One entry per search-key value in file | One entry per block of data file |
| **Data File Ordering** | Works on sorted or unsorted files | Data file **must be physically sorted** |
| **Lookup Speed** | Faster (direct pointer to record) | Slower (requires subsequent block scan) |
| **Index-Only Evaluation** | Supported (can answer without data block) | Not supported (must read data block) |
| **Storage Overhead** | Large (many index blocks) | Small (often fits entirely in RAM) |
| **Write/DML Overhead** | High (frequent index record inserts) | Low (records inserted inside block without index change) |

---

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Direct Exam Hit Analysis
> - **2023 Q.8(a) [2m]:** *"Write short note on dense and sparse index."*
> - In RUET semester finals, provide:
>   1. The two definitions (dense = every key; sparse = some keys / one per block).
>   2. The mandatory ordering constraint: **sparse indices require ordered data files**.
>   3. The comparative trade-off: **dense is faster for lookups / secondary indices, sparse saves disk space**.


---

[← Prev: T13 Part 2](T13_Part2_Security_and_Authorization_B.md) | [Index](00_Index.md) | [Next: T13 Part 4 →](T13_Part4_Indexing_and_Hashing.md)
