# ECE 2215: Database Systems — Teacher Guides & Exam Suggestions

**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Student Note-taker:** Raidah (Roll: 2310035)  
**Source Pages:** Page 23 (Left), Page 25 (Right), Page 34

---

## 1. Semester Final Exam Question Pattern & Blueprint

<!-- Page 34 -->

Teacher guidelines regarding final exam topic distribution and question sets:

### 1. Normalization & Functional Dependencies (Class Test & Final Pattern):
* **Format:** CT pattern problem set.
* **Core Requirements:**
  * Calculating attribute closures ($X^+$).
  * Identifying candidate keys and prime/non-prime attributes.
  * Checking which normal form a relation currently satisfies (1NF $\rightarrow$ 2NF $\rightarrow$ 3NF $\rightarrow$ BCNF).
  * Decomposing the relation into higher normal forms (3NF or BCNF) ensuring **lossless-join** and **dependency preservation**.
* **Key Questions:**
  * *Whether the relation is in a specific normal form?*
  * *And how to perform decomposition to bring it into that normal form?*

### 2. Transactions & Serializability:
* **Theory Questions:** ACID properties (with the \$50 transfer example), transaction lifecycle states.
* **Problem-Solving:**
  * Given a concurrent schedule, verify whether it is **Conflict Serializable** or **View Serializable**.
  * **Short-cut rule:**
    $$\text{Check view schedule for blind writes}$$
    * *Check for conflict operations and blind writes within the schedule.*
    * *If a schedule contains no blind writes, proving conflict serializability automatically proves it is view serializable!*

### 3. Concurrency Control Protocols:
* **Theory Type Focus:**
  * Timestamp Ordering (TSO) protocol rules (Read rules and Write rules).
  * Two-Phase Locking (2PL) growing/shrinking phases and lock points.
  * Deadlock conditions (4 Coffman conditions) and prevention schemes (Wait-Die vs. Wound-Wait).

### 4. Storage & RAID Architectures:
* RAID models (RAID 0, RAID 1, RAID 1+0, RAID 3, RAID 5, RAID 6).
* Architectural comparison: block striping vs. bit striping, dedicated parity vs. distributed parity ($P+Q$).

### 5. Queries & Relational Algebra (High Weightage):
* **Exam Weight:** **1 or more full question sets!**
* Complex SQL queries (nested subqueries with `EXISTS`, `NOT EXISTS`, `IN`, `SOME`, `ALL`, aggregation, grouping, ordering).
* Equivalent Relational Algebra expressions ($\sigma, \Pi, \bowtie, \times, -, \rho, \gamma$).

### 6. E-R Modeling:
* **Exam Weight:** **1 full question set!**
* Drawing complete E-R diagram from a scenario specification (identifying entities, simple/composite/multivalued/derived attributes, primary keys, weak entities, mapping cardinalities, and total/partial participation).

---

## 2. Class Test Scope & Guidelines

<!-- Page 23 (Left) -->

* **Class Test Syllabus:**
  * Up to **BCNF** (Boyce-Codd Normal Form).
  * Reference range: `Class note page 46 / Slides`.

---

## 3. Course Assignment & Term Project Instructions

<!-- Page 25 (Right) -->
<!-- Date: 13.09.2024 -->

### Assignment Specifications:
1. **Organization Selection:** Choose a real-world enterprise/organization (e.g., Hospital, University, Airline, E-commerce) $\rightarrow$ documented in Microsoft Word.
2. **Requirement Analysis:** Comprehensive theoretical requirements specification $\rightarrow$ documented in Word.
3. **E-R Diagram:** Hand-drawn conceptual E-R diagram with full attributes, cardinalities, and constraints (*hand-drawn*).
4. **Normalization:** Select at least one unnormalized operational table from the organization and demonstrate step-by-step normalization into 3NF / BCNF $\rightarrow$ documented in Word.

### Term Project:
* **Implementation:** Implement the relational database created in the assignment using MySQL.
* **Deliverables:** DDL schema scripts (`CREATE TABLE` with primary and foreign keys) + complete query suite demonstrating real-world operational retrieval.

