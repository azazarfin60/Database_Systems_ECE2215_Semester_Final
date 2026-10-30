---
title: "T12 (Part 3) · Checkpoints, ARIES & RAID Levels 0–6 · Exercises Bank"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T12
topic_id: T12
part: 3
exercise_count: 13
source_chapters:
  - "Chapter 12"
  - "Chapter 19"
---

[← Prev: T12 Part 2](T12_Part2_Recovery_Manager_and_Log_Recovery.md) | [Index](00_Index.md) | [Next: T13 Part 1 →](T13_Part1_Security_and_Authorization_A.md)

---

# T12 (Part 3) · Checkpoints, ARIES & RAID Levels 0–6

> [!info] Topic Card
> - **Course:** ECE 2215 · Database Systems (RUET)
> - **Syllabus Unit:** Unit 7 (Recovery System & RAID)
> - **Weight in RUET Finals:** 43 marks (6.8% aggregate share; tested in 5 of 7 recent finals)
> - **Source Textbook Chapters:** Silberschatz 7e Chapter 12 (*Physical Storage Systems*, §12.5) & Chapter 19 (*Recovery System*, §19.4–§19.8)
> - **Subtopics Covered:**
>   - **T12.3 (Part B):** Advanced log-based recovery, physiological logging, logical undo/redo, checkpoint log structures, ARIES three-pass mechanics, Dirty Page Table (DPT), and $\text{RecLSN}$.
>   - **T12.4:** RAID architectures (RAID 0, 1, 3, 4, 5, 6, 10/1+0), striping, parity distribution, failure domains, small write penalty, online rebuild interference, and background scrubbing.

---

## Table of Assigned Exercises

| Exercise ID | Type | Silberschatz 7e | Subtopic | Focus / Problem Description | RUET Exam Relevance |
| :--- | :--- | :--- | :---: | :--- | :--- |
| [[#Exercise 19.18 · Non-Strict 2PL Rollback & Inconsistent Log Recovery\|EX 19.18]] | Regular | Ch. 19 Ex. 19.18 | T12.3 | Non-strict 2PL early lock release & recovery failure | High (2PL & Atomicity coupling) |
| [[#Exercise 19.19 · Physiological Redo Logging in Slotted-Page Storage\|EX 19.19]] | Regular | Ch. 19 Ex. 19.19 | T12.3 | Physiological logging vs slotted page defragmentation | Conceptual (Storage & Log efficiency) |
| [[#Exercise 19.20 · Logical Undo vs. Logical Redo Logging Asymmetry\|EX 19.20]] | Regular | Ch. 19 Ex. 19.20 | T12.3 | Why logical undo is common while logical redo is avoided | Core ARIES Theory |
| [[#Exercise 19.21 · Crash Recovery Trace Before Abort Record in Log-Based Recovery\|EX 19.21]] | Regular | Ch. 19 Ex. 19.21 | T12.3 | Fig. 19.5 crash before abort log record & recovery trace | Direct Exam Favorite (Log Tracing) |
| [[#Exercise 19.22 · Long-Running Transactions: Section 19.4 vs. ARIES & Log Truncation\|EX 19.22]] | Regular | Ch. 19 Ex. 19.22 | T12.3 | Long transactions: recovery overhead & log truncation | Systems Architecture |
| [[#Exercise 19.23 · Crash During Logical Undo Recovery & Secondary Crash Tracing\|EX 19.23]] | Regular | Ch. 19 Ex. 19.23 | T12.3 | Fig. 19.7 crash during rollback of logical operation | Advanced Recovery Mechanics |
| [[#Exercise 19.24 · Log-Based Recovery vs. Shadow Paging for Newly Allocated Disk Pages\|EX 19.24]] | Regular | Ch. 19 Ex. 19.24 | T12.3 | Log recovery vs shadow copy for newly allocated pages | 2017 Q.6(d), 2023 Q.7(b) |
| [[#Exercise 19.25 · ARIES Checkpoints: Dirty Page Table & RecLSN Redo Optimization\|EX 19.25]] | Regular | Ch. 19 Ex. 19.25 | T12.3 | Dirty Page Table filtering & $\text{RecLSN}$ skipping rules | Advanced Modern DBMS Design |
| [[#Practice Exercise 12.4 · Parity-Block Allocation Flaw in a 4-Disk RAID Array\|PE 12.4]] | Practice | Ch. 12 PE 12.4 | T12.4 | Parity block arrangement flaw on 4 disks ($B_1 \dots B_4$ with $P_1$) | Mathematical / Structural Fault |
| [[#Practice Exercise 12.5 · Architectural Trade-offs of Disk Array Size in RAID 5\|PE 12.5]] | Practice | Ch. 12 PE 12.5 | T12.4 | Trade-offs of fewer vs more disks in a RAID 5 array | 2018 Q.8(c), 2023 Q.7(c) |
| [[#Exercise 12.11 · Online Hot-Spare Rebuild & Access Interference Across RAID Levels\|EX 12.11]] | Regular | Ch. 12 Ex. 12.11 | T12.4 | Online rebuild interference comparison across RAID levels | Enterprise Reliability |
| [[#Exercise 12.12 · Disk Scrubbing Mechanics & Latent Sector Defect Prevention\|EX 12.12]] | Regular | Ch. 12 Ex. 12.12 | T12.4 | Disk scrubbing purpose, mechanisms, and latent errors | 2019 Q.4(b), 2024 Q.3(b) |
| [[#Exercise 12.13 · Optimal Storage Architecture for Write-Intensive Fault-Tolerant Workloads\|EX 12.13]] | Regular | Ch. 12 Ex. 12.13 | T12.4 | RAID selection & caching for write-intensive workloads | 2018 Q.5(c), 2023 Q.4(a) |

---

## T12.3 · Log-based recovery & checkpoints

---

### Exercise 19.18 · Non-Strict 2PL Rollback & Inconsistent Log Recovery

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.18 (Page 956)
> - **Subtopic:** T12.3 (Log-Based Recovery & Concurrency Interactions)
> - **Prerequisites:** Two-Phase Locking (2PL), Strict 2PL, Physical Undo Logging, Cascading Rollback.
> - **RUET Relevance:** Crucial theoretical question explaining why transaction recovery models strictly require the concurrency control subsystem to enforce Strict 2PL or Rigorous 2PL.

**Question (Silberschatz 7e Exercise 19.18).**
Suppose two-phase locking is used, but exclusive locks are released early, that is, locking is not done in a strict two-phase manner. Give an example to show why transaction rollback can result in a wrong final state, when using the log-based recovery algorithm.

#### 1. Core Principles & Concept Overview

In transaction management, concurrency control and crash recovery are inextricably linked:
- **Two-Phase Locking (Standard 2PL):** Guarantees serializability. Locks may be released as soon as the transaction enters its shrinking phase, even while the transaction is still computing and before it commits.
- **Strict Two-Phase Locking (Strict 2PL):** Requires that **all exclusive (X) locks** held by a transaction must be retained until the transaction formally completes (either commits or aborts).
- **Physical Log-Based Recovery:** Standard log-based recovery algorithms (such as Silberschatz §19.4) write update log records of the form $\langle T_i, X, V_{old}, V_{new} \rangle$. When a transaction $T_i$ aborts, the recovery manager rolls back $T_i$ by performing a **physical undo**: it scans the log backward and blindly restores the old value $V_{old}$ to the data item $X$.

If exclusive locks are released early (non-strict 2PL), another transaction $T_j$ can acquire an exclusive lock on $X$, read or overwrite $X$, and even commit. If $T_i$ subsequently aborts, physically restoring $X \leftarrow V_{old}$ wipes out $T_j$'s committed updates without $T_j$'s knowledge, violating both **Atomicity** and **Durability**.

```text
Time Line: Non-Strict 2PL Hazard Leading to Overwritten Committed State
-----------------------------------------------------------------------------------------
T1: Acquire X(A) -> Write(A, 200) -> Release X(A) [EARLY RELEASE] ------------------> Abort!
                                          \
T2:                                        Acquire X(A) -> Write(A, 300) -> Commit!
-----------------------------------------------------------------------------------------
Log: <T1 start>    <T1, A, 100, 200>      <T2 start>   <T2, A, 200, 300>  <T2 commit>  Undo T1:
                                                                                       A <- 100 (CRASH/LOSS!)
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Initial State & Transaction Logic
Let the database contain a data item $A$ with an initial value:
$$
A = 100
$$
Consider two transactions, $T_1$ and $T_2$:
- $T_1$ updates $A$ by adding $100$ (setting $A = 200$).
- $T_2$ updates $A$ by adding $100$ (setting $A = 300$).

##### Step 2: Execution Schedule Under Non-Strict 2PL
1. **$t_1$:** $T_1$ starts. Log record $\langle T_1\text{ start}\rangle$ is written.
2. **$t_2$:** $T_1$ acquires an exclusive lock on $A$: $\text{lock-X}(A)$.
3. **$t_3$:** $T_1$ writes $A = 200$. Log record $\langle T_1, A, 100, 200\rangle$ is written to the log buffer.
4. **$t_4$ (Early Lock Release):** $T_1$ enters its shrinking phase and releases its exclusive lock on $A$: $\text{unlock}(A)$. Note that $T_1$ has **not yet committed**.
5. **$t_5$:** $T_2$ starts. Log record $\langle T_2\text{ start}\rangle$ is written.
6. **$t_6$:** $T_2$ requests and successfully acquires $\text{lock-X}(A)$ because $T_1$ already released it.
7. **$t_7$:** $T_2$ reads $A$ (value $200$) and writes $A = 300$. Log record $\langle T_2, A, 200, 300\rangle$ is written.
8. **$t_8$:** $T_2$ releases $\text{lock-X}(A)$ and commits. Log record $\langle T_2\text{ commit}\rangle$ is flushed to stable storage.
9. **$t_9$ (Rollback of $T_1$):** $T_1$ encounters a division by zero error, a system constraint violation, or is selected as a deadlock victim. $T_1$ must abort.

##### Step 3: Execution of the Log-Based Recovery Algorithm
The recovery manager initiates transaction rollback for $T_1$:
1. The log is scanned backward to find all update records belonging to $T_1$.
2. It encounters the record $\langle T_1, A, 100, 200\rangle$.
3. The standard physical undo rule is executed:
   $$
   \text{Data item } A \leftarrow V_{old} = 100
   $$
4. A compensation / redo-only log record is written: $\langle T_1, A, 100\rangle$.
5. The record $\langle T_1\text{ start}\rangle$ is found. The abort record $\langle T_1\text{ abort}\rangle$ is written to the log.

##### Step 4: Analysis of the Inconsistent Final State
- **Expected Correct State:** Transaction $T_2$ successfully committed at $t_8$. Under the Durability ($D$) property of ACID, all updates made by a committed transaction must persist permanently in the database.
- **Actual Database State:** The physical undo performed during $T_1$'s rollback reset $A$ to $100$.
- **Discrepancy:** The update executed by $T_2$ ($A = 300$) has been completely obliterated. The final state reflects neither the serial execution $T_1 \to T_2$ nor $T_2$ executing alone (which would yield $A = 100 + 100 = 200$). The database is in an invalid and corrupted state.

##### Step 5: Formal Architectural Conclusion
Physical undo logging assumes that the value of $X$ at the time of rollback is identical to the after-image $V_{new}$ written by the aborting transaction. This assumption holds **if and only if no other transaction has modified $X$ in the interim**, which is guaranteed strictly when exclusive locks are held until transaction termination (Strict 2PL).

#### 3. RUET Exam Insights & Examiner Notes
- **Recycled Theme:** In RUET exams (e.g., 2017 Q.7a on Strict 2PL and 2018 Q.8b on Recovery Manager), questions frequently test the rationale behind concurrency control protocols. Examiners look for the specific phrase **"dirty read resulting in lost updates during physical rollback"**.
- **Common Student Misconception:** Students often assume that cascading rollback would automatically abort $T_2$. However, in this scenario, $T_2$ **already committed** at time $t_8$ before $T_1$ aborted at $t_9$. A committed transaction **cannot be rolled back** without violating the fundamental Durability contract.
- **Alternative Solution:** To permit early lock release for performance, the system must abandon physical undo logging and employ **logical undo logging** (operational logging), as explored in Exercise 19.20.

---

### Exercise 19.19 · Physiological Redo Logging in Slotted-Page Storage

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.19 (Page 956)
> - **Subtopic:** T12.3 (Physiological Logging & Slotted Page Organization)
> - **Prerequisites:** Slotted-page architecture (Ch. 13), Physical vs. Logical vs. Physiological logging.
> - **RUET Relevance:** Advanced systems question explaining why enterprise storage engines (Oracle, PostgreSQL, InnoDB) use physiological logging rather than pure byte-level physical logging.

**Question (Silberschatz 7e Exercise 19.19).**
Physiological redo logging can reduce logging overheads significantly, especially with a slotted page record organization. Explain why.

#### 1. Core Principles & Concept Overview

To understand logging efficiency, we classify recovery logging into three paradigms:
1. **Physical Logging:** Logs the exact binary byte differences (e.g., page address, byte offset, length, before-image bytes, after-image bytes).
2. **Logical Logging:** Logs the high-level relational operation (e.g., `INSERT INTO student VALUES ('101', 'Alice')`).
3. **Physiological Logging:** *"Physical to a page, logical within a page"*. It specifies the physical disk page identifier, but within that page, describes the operation logically (e.g., "Insert tuple into slot index $k$" or "Delete record at slot index $j$").

##### Slotted-Page Architecture
In a slotted-page architecture (standard in relational DBMSs for variable-length records):
- The **page header** contains an array of slot entries located at the beginning of the page, growing downward.
- Each slot entry stores a pair: $(\text{offset}, \text{length})$ pointing to the actual record payload.
- The **tuple records** are allocated from the bottom of the page, growing upward into the contiguous free space in the middle.

```text
+-----------------------------------------------------------------------+
| Page Header: [PageLSN | Free Space Pointer | Slot 1 | Slot 2 | Slot 3]|
|                                                                       |
|                          Contiguous Free Space                        |
|                                                                       |
| [Record 3 Data]         [Record 1 Data]               [Record 2 Data] |
+-----------------------------------------------------------------------+
0                                                                     4KB / 8KB
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Internal Mechanics of Slotted-Page Maintenance
When records are updated, deleted, or inserted:
1. **Record Deletion:** Deleting a record leaves a hole in the physical byte layout.
2. **Page Compaction (Defragmentation):** To ensure that incoming records find contiguous free space, the storage engine shifts existing records within the page to close gaps.
3. **Slot Array Adjustment:** The slot pointers in the header must be rewritten to point to the new physical byte offsets of the moved records.

##### Step 2: The Catastrophic Overhead of Pure Physical Logging
Suppose an application deletes a small 30-byte record from a 4 KB or 8 KB page, triggering page compaction:
- The compaction process shifts 15 other records downward in memory to consolidate free space.
- A **physical redo logger** inspects raw bytes. Because 3,000 bytes of data were shifted across the page, the physical log must record either:
  1. Full page after-images (4096 or 8192 bytes written to the log buffer for a 30-byte deletion!), or
  2. A massive series of byte-range move/diff records spanning several kilobytes.
- **Result:** Severe write amplification, saturation of the WAL log buffer, and constant disk I/O bottlenecks.

##### Step 3: How Physiological Redo Logging Solves the Problem
Under physiological logging:
- The log record specifies:
  $$
  \langle \text{PageID} = P, \text{Op} = \text{DELETE}, \text{Slot} = 2 \rangle
  $$
- **Log Size:** The log record requires merely 16 to 24 bytes (Transaction ID, Page ID, Operation code, Slot number, and LSN).
- **Redo Execution:** During recovery, the recovery engine reads the physiological log record, locates Page $P$, and invokes the internal slotted-page management subroutine to delete Slot 2 and compact the page in memory.
- **Idempotency Preservation:** Because the operation is targeted to a single physical page, the page's header contains a `PageLSN`. If $\text{PageLSN} \ge \text{LogRecord.LSN}$, the entire physiological action is skipped, ensuring strict mathematical idempotence:
  $$
  \text{Redo}(\text{Redo}(P)) = \text{Redo}(P)
  $$

##### Step 4: Quantitative Comparison
Let us summarize the structural performance difference:

| Logging Scheme | Data Logged for Record Shift / Defrag | Log Volume | Redo Complexity | Idempotence |
| :--- | :--- | :--- | :--- | :--- |
| **Physical (Full Page)** | Entire 4 KB / 8 KB page buffer | Extreme ($4096$ B) | Trivial (byte copy) | Guaranteed |
| **Physical (Byte Diff)** | All shifted byte intervals across page | High ($1000\text{--}4000$ B) | Low (offset memcpy) | Guaranteed |
| **Physiological** | Page ID + Slot Index + Op Descriptor | Minimal ($20\text{--}40$ B) | Moderate (page-internal routine) | Guaranteed via `PageLSN` |
| **Logical** | High-level SQL string / relational op | Very Low ($30\text{--}60$ B) | High (requires index searches) | Hard to guarantee |

#### 3. RUET Exam Insights & Examiner Notes
- **Key Takeaway:** Physiological redo logging achieves the minimal log volume of logical logging while preserving the page-level isolation and strict idempotency of physical logging.
- **Examiner Scoring Tip:** When answering questions regarding write-ahead logging (WAL) efficiency, highlight that **physiological logging decouples internal page storage reorganizations from WAL generation**.

---

### Exercise 19.20 · Logical Undo vs. Logical Redo Logging Asymmetry

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.20 (Page 956)
> - **Subtopic:** T12.3 (Logical Logging Asymmetry & ARIES Design)
> - **Prerequisites:** Physiological Redo, Logical Undo, ARIES Philosophy ("Repeating History").
> - **RUET Relevance:** Fundamental design concept of the ARIES recovery algorithm (C. Mohan et al., IBM Research), testing the core distinction between the Redo pass and Undo pass.

**Question (Silberschatz 7e Exercise 19.20).**
Explain why logical undo logging is used widely, whereas logical redo logging (other than physiological redo logging) is rarely used.

#### 1. Core Principles & Concept Overview

In modern recovery systems (such as ARIES), there is a fundamental asymmetry between how **Redo** and **Undo** are implemented:
- **Redo Paradigm:** Uses **physical** or **physiological** logging.
- **Undo Paradigm:** Uses **logical** undo logging (operation-level inverses).

```text
               +-------------------------------------------------------------+
               |                  The Fundamental Asymmetry                  |
               +-------------------------------------------------------------+
               | Redo: Physical / Physiological ONLY                         |
               |       -> Must replay exact history blindly                  |
               |       -> Must be strictly idempotent                        |
               |       -> Must not rely on high-level system structures      |
               +-------------------------------------------------------------+
               | Undo: Logical Inverses Permitted & Widely Used              |
               |       -> Required when locks are released early (latches)   |
               |       -> Operates on structurally consistent pages          |
               |       -> Avoids destroying concurrent updates               |
               +-------------------------------------------------------------+
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Why Logical Undo Logging is Indispensable
1. **Early Latch and Lock Release on Internal Structures:**
   - In high-performance database systems, operations on physical indices (e.g., B+-trees) and allocation bitmaps acquire short-term **latches** rather than long-term transaction locks.
   - For example, if transaction $T_1$ inserts a key into a B+-tree, it causes a node split. Once the split finishes, $T_1$ immediately releases the page latches on the B+-tree nodes so other transactions ($T_2, T_3$) can insert keys into those same nodes.
2. **Hazard of Physical Undo:**
   - If $T_1$ subsequently aborts, the system **cannot physically restore** the B+-tree pages to their pre-split byte states! Doing so would destroy all the insertions made by $T_2$ and $T_3$ in the meantime.
3. **The Logical Undo Solution:**
   - Instead, the recovery system executes an **inverse logical operation**:
     $$
     \text{Inverse}(\text{Insert}(K)) \implies \text{Delete}(K)
     $$
   - The deletion of key $K$ traverses the B+-tree logically and deletes $K$ cleanly, preserving all surrounding concurrent modifications.

##### Step 2: Why Pure Logical Redo Logging is Rarely Used
Logical redo logging means recording high-level operations (e.g., `INSERT INTO table`) and re-executing them during restart recovery. This is almost never done for three decisive reasons:

1. **Failure of Idempotency:**
   - Crash recovery may crash repeatedly. The redo phase must be strictly **idempotent**: replaying a log record multiple times must yield the exact same physical result:
     $$
     f(f(S)) = f(S)
     $$
   - A logical operation like "Append record $R$" or "Increment counter by 5" is **not idempotent**. If executed twice, it creates duplicate records or double increments.
   - Physical and physiological redo records can be easily stamped with an LSN (`PageLSN`). If $\text{PageLSN} \ge \text{RecordLSN}$, the update is bypassed. Pure logical operations lack a single physical page anchor to track such state.
2. **State Dependencies & Broken Invariants During Recovery:**
   - A logical redo operation requires that the entire underlying system state (secondary indices, free space catalogs, hash tables) is already completely intact and structurally consistent.
   - However, during crash recovery, some disk pages may reflect updates up to the crash point, while others may contain stale data from hours ago. Re-executing a high-level query on a half-updated database will fail, throw constraint errors, or insert into wrong physical locations.
3. **Violation of the "Repeating History" Principle:**
   - Modern recovery relies on **repeating history**: the redo pass brings the entire database (including uncommitted transactions, aborted transactions, and internal structures) up to the exact state it was in at the instant of the crash.
   - Only after history has been repeated physically can the system safely execute logical undo operations. Logical redo would make repeating history impossible.

#### 3. RUET Exam Insights & Examiner Notes
- **Key Formulation:** Examiners reward answers that clearly articulate:
  > *"Logical undo is necessary to support concurrency and early release of lower-level locks/latches without cascading rollbacks; physical/physiological redo is necessary to guarantee idempotency and permit repeating history during crash restart."*
- **Syllabus Connection:** Relates directly to Unit 6 (Concurrency Control) and Unit 7 (Recovery System), illustrating how short-term latching in index management forces the recovery architecture to adopt logical undo.

---

### Exercise 19.21 · Crash Recovery Trace Before Abort Record in Log-Based Recovery

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.21 (Page 956)
> - **Subtopic:** T12.3 (Log Tracing, Redo Pass, Undo Pass, Compensation Records)
> - **Prerequisites:** Checkpoints with active transaction lists (§19.4), Compensation Log Records (CLRs).
> - **RUET Relevance:** High-frequency exam pattern. RUET semester finals regularly require students to trace log execution step-by-step from a given log fragment.

**Question (Silberschatz 7e Exercise 19.21).**
Consider the log in Figure 19.5. Suppose there is a crash just before the log record $\langle T_0\text{ abort}\rangle$ is written out. Explain what would happen during recovery.

#### 1. Core Principles & Concept Overview

##### Reference Log from Figure 19.5 (Silberschatz 7e, Page 924)
The textbook log fragment presents the following chronological records on stable storage:

```text
[Log Sequence in Figure 19.5 up to the Crash Point]
  LSN 01: <T0 start>
  LSN 02: <T0, B, 2000, 2050>
  LSN 03: <T1 start>
  LSN 04: <checkpoint {T0, T1}>
  LSN 05: <T1, C, 700, 600>
  LSN 06: <T1 commit>
  LSN 07: <T2 start>
  LSN 08: <T2, A, 500, 400>
  LSN 09: <T0, B, 2000>          <-- Compensation/Redo-only log record during T0 rollback
  ================================ CRASH OCCURS HERE! ================================
  (Missing: <T0 abort> was NEVER written out to the stable log!)
```

##### Two-Phase Recovery Protocol (§19.4)
1. **Redo Phase (Forward Scan from Checkpoint):**
   - Initialize `undo-list` $= L$ from $\langle\text{checkpoint } L\rangle$.
   - For every normal update record $\langle T_i, X, V_1, V_2 \rangle$ or redo-only record $\langle T_i, X, V_2 \rangle$, write $X \leftarrow V_2$ (repeat history).
   - If $\langle T_i\text{ start}\rangle$ is found, add $T_i$ to `undo-list`.
   - If $\langle T_i\text{ commit}\rangle$ or $\langle T_i\text{ abort}\rangle$ is found, remove $T_i$ from `undo-list`.
2. **Undo Phase (Backward Scan from End of Log):**
   - For every update record of a transaction in `undo-list`, restore the old value and write a redo-only log record.
   - When $\langle T_i\text{ start}\rangle$ is reached, write $\langle T_i\text{ abort}\rangle$ and remove $T_i$ from `undo-list`.
   - Stop when `undo-list` becomes empty.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Redo Phase Execution (Scan Forward from LSN 04)
- **Initialization:** At LSN 04, the checkpoint record is $\langle\text{checkpoint } \{T_0, T_1\}\rangle$.
  $$
  \text{undo-list} \leftarrow \{T_0, T_1\}
  $$
- **Scan LSN 05:** $\langle T_1, C, 700, 600\rangle$.
  - Replay update: Set data item $C \leftarrow 600$.
- **Scan LSN 06:** $\langle T_1\text{ commit}\rangle$.
  - Transaction $T_1$ has committed.
  - Remove $T_1$ from `undo-list`:
    $$
    \text{undo-list} \leftarrow \{T_0\}
    $$
- **Scan LSN 07:** $\langle T_2\text{ start}\rangle$.
  - Add $T_2$ to `undo-list`:
    $$
    \text{undo-list} \leftarrow \{T_0, T_2\}
    $$
- **Scan LSN 08:** $\langle T_2, A, 500, 400\rangle$.
  - Replay update: Set data item $A \leftarrow 400$.
- **Scan LSN 09:** $\langle T_0, B, 2000\rangle$.
  - This is a redo-only (compensation) record. Replay update: Set data item $B \leftarrow 2000$.
- **End of Log Reached:**
  - In the original Figure 19.5, an abort record $\langle T_0\text{ abort}\rangle$ was present which removed $T_0$.
  - **CRITICAL CONDITION:** In this exercise, the crash occurred *before* $\langle T_0\text{ abort}\rangle$ was written.
  - Therefore, $T_0$ is **never removed** from `undo-list`.
  - Final status at end of Redo Phase:
    $$
    \mathbf{\text{undo-list} = \{T_0, T_2\}}
    $$

##### Step 2: Undo Phase Execution (Scan Backward from LSN 09)
The recovery manager now scans backward from the end of the log to undo transactions in $\text{undo-list} = \{T_0, T_2\}$:

1. **Examine LSN 09:** $\langle T_0, B, 2000\rangle$.
   - This is a **redo-only record** (compensation record) without an undo value.
   - The recovery algorithm takes **no undo action** on redo-only records (in ARIES, it follows the `UndoNextLSN` pointer; in Section 19.4, it simply skips taking an undo step here).
2. **Examine LSN 08:** $\langle T_2, A, 500, 400\rangle$.
   - $T_2 \in \text{undo-list}$.
   - Undo update: Restore data item $A \leftarrow 500$.
   - Write new redo-only log record:
     $$
     \langle T_2, A, 500\rangle
     $$
3. **Examine LSN 07:** $\langle T_2\text{ start}\rangle$.
   - Start record for $T_2$ is found.
   - Write log record:
     $$
     \langle T_2\text{ abort}\rangle
     $$
   - Remove $T_2$ from `undo-list`:
     $$
     \text{undo-list} \leftarrow \{T_0\}
     $$
4. **Examine LSN 05:** $\langle T_1, C, 700, 600\rangle$.
   - $T_1 \notin \text{undo-list}$. Skip.
5. **Examine LSN 03:** $\langle T_1\text{ start}\rangle$.
   - Skip.
6. **Examine LSN 02:** $\langle T_0, B, 2000, 2050\rangle$.
   - $T_0 \in \text{undo-list}$.
   - Undo update: Restore data item $B \leftarrow 2000$.
   - Write new redo-only log record:
     $$
     \langle T_0, B, 2000\rangle
     $$
   - *(Note: $B$ was already $2000$ due to LSN 09. Re-writing $B = 2000$ is completely harmless and strictly idempotent).*
7. **Examine LSN 01:** $\langle T_0\text{ start}\rangle$.
   - Start record for $T_0$ is found.
   - Write log record:
     $$
     \langle T_0\text{ abort}\rangle
     $$
   - Remove $T_0$ from `undo-list`:
     $$
     \text{undo-list} \leftarrow \emptyset
     $$

##### Step 3: Termination & Summary of Added Log Records
The `undo-list` is now empty. Recovery terminates cleanly, and normal transaction processing resumes.

The new log records appended to stable storage during recovery are:
1. $\langle T_2, A, 500\rangle$
2. $\langle T_2\text{ abort}\rangle$
3. $\langle T_0, B, 2000\rangle$
4. $\langle T_0\text{ abort}\rangle$

Final consistent database state:
$$
A = 500, \quad B = 2000, \quad C = 600
$$

#### 3. RUET Exam Insights & Examiner Notes
- **Contrast with Standard Fig. 19.5:** In the standard textbook diagram, $T_0$ is already considered aborted before the crash, so only $T_2$ appears in the `undo-list`. In this problem, because $\langle T_0\text{ abort}\rangle$ was lost in volatile memory during the crash, the recovery manager must treat $T_0$ as an active uncommitted transaction and undo it.
- **Idempotence Demonstration:** This exercise provides concrete proof of the mathematical idempotence of recovery: re-restoring $B = 2000$ causes no error and preserves consistency.

---

### Exercise 19.22 · Long-Running Transactions: Section 19.4 vs. ARIES & Log Truncation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.22 (Page 956)
> - **Subtopic:** T12.3 (Long-Running Transactions, Checkpoint Overhead, Log Truncation)
> - **Prerequisites:** Checkpoint algorithm (§19.4), ARIES Dirty Page Table, Log Truncation.
> - **RUET Relevance:** Critical systems-level question on operational database maintenance and why checkpointing without dirty page tracking cripples production databases.

**Question (Silberschatz 7e Exercise 19.22).**
Suppose there is a transaction that has been running for a very long time but has performed very few updates.
a. What effect would the transaction have on recovery time with the recovery algorithm of Section 19.4, and with the ARIES recovery algorithm?
b. What effect would the transaction have on deletion of old log records?

#### 1. Core Principles & Concept Overview

- **Section 19.4 Checkpoint Mechanism:** Writes a checkpoint record containing a list of all currently active transactions $L = \{T_1, \dots, T_k\}$. During crash restart, the redo phase scans forward starting from the **most recent checkpoint**. The undo phase scans backward through the log.
- **ARIES Checkpoint Mechanism:** Employs **non-blocking fuzzy checkpoints**. The checkpoint stores:
  1. **Transaction Table (TT):** All active transactions and their `LastLSN`.
  2. **Dirty Page Table (DPT):** All dirty buffer pages and their `RecLSN` (the earliest LSN that dirtied the page on disk).
  - The redo phase starts from:
    $$
    \text{RedoLSN} = \min_{P \in \text{DPT}} P.\text{RecLSN}
    $$
- **Log Truncation:** The process of reclaiming disk space by physically deleting stable log files that are no longer needed for any possible crash recovery scenario.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Effect on Recovery Time

###### 1. Recovery Algorithm of Section 19.4:
- **Redo Phase:** The redo scan begins at the most recent checkpoint. The fact that transaction $T_{long}$ has been running for days or weeks does **not** push the redo starting point backward, provided regular checkpoints have been taken. The redo phase time is determined solely by the number of log records written since the last checkpoint.
- **Undo Phase:**
  - If $T_{long}$ commits before the crash, it does not affect the undo phase.
  - If $T_{long}$ was active at the time of the crash, it is placed in the `undo-list`.
  - Because Section 19.4 performs a **sequential backward scan** across the entire physical log, the recovery manager must scan backward all the way to $T_{long}$'s start record ($\langle T_{long}\text{ start}\rangle$)!
  - **Performance Impact:** Even though $T_{long}$ performed very few updates, the undo scan must sequentially read gigabytes or terabytes of old log records just to find those few updates and the start record. This causes a **massive increase in recovery time**.

###### 2. ARIES Recovery Algorithm:
- **Redo Phase:**
  - The redo scan starts at $\min(\text{RecLSN})$ from the DPT.
  - Because $T_{long}$ performed very few updates, if the buffer pages containing those few updates were flushed to disk during normal operation, their `RecLSN` values were removed from the DPT.
  - Consequently, $T_{long}$ **does not pull the redo start point backward**. Redo time remains minimal.
- **Undo Phase:**
  - ARIES does **not** scan the physical log sequentially backward during undo.
  - Each log record contains a `PrevLSN` field, forming a backward linked list for each transaction.
  - The undo phase maintains a priority queue of active transactions and directly follows the `PrevLSN` pointer chain for $T_{long}$.
  - **Performance Impact:** Because $T_{long}$ performed very few updates, ARIES follows only a handful of pointers, jumping across vast gaps in the log without reading intermediate records.
  - **Conclusion for ARIES:** $T_{long}$ has **virtually zero effect on recovery time**.

##### Part (b): Effect on Deletion of Old Log Records (Log Truncation)

In any Write-Ahead Logging (WAL) system, a log record at sequence number $K$ cannot be truncated (deleted) if it is needed for either:
1. **Redo:** There is a dirty page in memory whose on-disk version does not yet contain the update at $K$.
2. **Undo:** The record belongs to an active transaction that might abort in the future.

$$
\text{Truncation Limit LSN} = \min \left( \min_{P \in \text{DPT}} P.\text{RecLSN}, \; \min_{T_i \in \text{Active}} T_i.\text{StartLSN} \right)
$$

- **The Disaster for Both Algorithms:**
  - Because $T_{long}$ has been active for a very long time, its $\langle T_{long}\text{ start}\rangle$ record has a very small LSN ($T_{long}.\text{StartLSN}$).
  - Even if all pages updated by $T_{long}$ have been flushed to disk, the recovery manager **cannot delete any log record written after $T_{long}.\text{StartLSN}$**, because if $T_{long}$ aborts, the system needs its log records to execute undo.
- **Operational Consequence:**
  - Stable log disk space **cannot be reclaimed**.
  - The log volume will grow monotonically until the disk drive fills up completely, at which point the entire DBMS will stall and reject all incoming transactions.
- **Production Remedy:** Database engines enforce a maximum transaction duration timeout. If a transaction stays open too long, the system forcibly aborts it to allow log truncation.

#### 3. RUET Exam Insights & Examiner Notes
- **Summary Matrix for Exam Answers:**

| Metric | Section 19.4 Algorithm | ARIES Algorithm |
| :--- | :--- | :--- |
| **Redo Start Point** | Last Checkpoint | $\min_{P \in \text{DPT}} P.\text{RecLSN}$ |
| **Undo Traversal** | Sequential backward scan of whole log | Pointer chasing via `PrevLSN` chains |
| **Impact of $T_{long}$ on Recovery Time** | **Severe** (undo scan must read back to start) | **Negligible** (jumps directly via pointers) |
| **Impact of $T_{long}$ on Log Truncation** | **Severe** (blocks log deletion completely) | **Severe** (blocks log deletion completely) |

- **Exam Alert:** Many students incorrectly state that ARIES solves the log truncation problem for long transactions. Make sure to emphasize that **log truncation is blocked in ALL WAL systems** as long as a transaction remains uncommitted.

---

### Exercise 19.23 · Crash During Logical Undo Recovery & Secondary Crash Tracing

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.23 (Page 956)
> - **Subtopic:** T12.3 (Crash During Recovery, Logical Undo, Operation Abort Records)
> - **Prerequisites:** Logical Undo Logging, Figure 19.7, Operation-Begin / Operation-End / Operation-Abort records.
> - **RUET Relevance:** Advanced theoretical question on crash recovery survivability, testing what happens when a system crashes *while already recovering from a previous crash*.

**Question (Silberschatz 7e Exercise 19.23).**
Consider the log in Figure 19.7. Suppose there is a crash during recovery, just before the operation abort log record is written for operation $O_1$. Explain what will happen when the system recovers again.

#### 1. Core Principles & Concept Overview

##### Logical Undo Logging Framework (§19.6.2)
When operations release locks early, their undo cannot be physical. The log records for a logical operation $O_j$ executed by transaction $T_i$ consist of:
1. $\langle T_i, O_j\text{, operation-begin}\rangle$
2. Normal physical update records representing internal actions of $O_j$ (used for undo if crash happens *during* normal operation).
3. $\langle T_i, O_j\text{, operation-end}, U\rangle$, where $U$ describes the logical undo operation needed if $T_i$ aborts *after* $O_j$ finishes.

##### How Undo of Completed Operations Works:
1. When rolling back, encountering $\langle T_i, O_j\text{, operation-end}, U\rangle$ causes the system to execute the logical undo operation $U$.
2. The physical updates performed by $U$ are logged to stable storage.
3. Once $U$ completes, an operation-abort record is written:
   $$
   \langle T_i, O_j\text{, operation-abort}\rangle
   $$
4. The backward scan then **skips all internal log records** of $O_j$ until it reaches $\langle T_i, O_j\text{, operation-begin}\rangle$, preventing double undo.

#### 2. Detailed Step-by-Step Solution

##### Step 1: The Exact State of the Log at the Second Crash
Referring to Figure 19.7 (Silberschatz 7e, Page 939):
- Transaction $T_0$ executed $O_1$ on $C$ ($C: 700 \to 600$, inverse $+100$) and released lower-level locks.
- Transaction $T_1$ executed $O_2$ on $C$ ($C: 600 \to 400$) and committed.
- $T_0$ decided to abort. During its rollback, the system executed the logical undo of $O_1$, which added $100$ to $C$ ($C: 400 \to 500$).
- This was logged as a physical update record:
  $$
  \langle T_0, C, 400, 500\rangle
  $$
- **SECOND CRASH OCCURS:** The system crashes **immediately before** writing:
  $$
  \langle T_0, O_1\text{, operation-abort}\rangle
  $$

```text
Log on Stable Storage at Time of Second Crash:
  ...
  <T1, O2, operation-end, (C, +200)>
  <T0, C, 400, 500>                     <-- Physical update generated by logical undo of O1
  ================================ SECOND CRASH! ================================
  (MISSING: <T0, O1, operation-abort> was NEVER written!)
```

##### Step 2: What Happens When the System Recovers Again?

###### Phase 1: Redo Phase (Repeating History)
1. The recovery manager scans forward from the last checkpoint.
2. It replays all logged updates in exact historical sequence.
3. It encounters the record $\langle T_0, C, 400, 500\rangle$ and applies it:
   $$
   C \leftarrow 500
   $$
4. Because neither $\langle T_0\text{ commit}\rangle$ nor $\langle T_0\text{ abort}\rangle$ exists in the log, $T_0$ is placed in `undo-list`.
5. Redo phase completes. $C$ is currently $500$.

###### Phase 2: Undo Phase (Backward Scan)
The recovery manager scans backward to undo $T_0$:

1. **Encountering the Incomplete Undo Record:**
   - The first record encountered for $T_0$ during the backward scan is the physical update record:
     $$
     \langle T_0, C, 400, 500\rangle
     $$
   - Because there is **no corresponding operation-abort log record** preceding it, the recovery manager treats this as an ordinary physical update executed by $T_0$!
   - It performs a standard physical undo: restores the old value $400$ to $C$:
     $$
     C \leftarrow 400
     $$
   - It logs a redo-only compensation record: $\langle T_0, C, 400\rangle$.
   - **Crucial Architectural Effect:** Undoing this partial undo brings data item $C$ back to $400$, which is the exact state left by $T_1$'s committed operation $O_2$!

2. **Re-encountering the Logical Operation End Record:**
   - Continuing the backward scan, the system encounters:
     $$
     \langle T_0, O_1\text{, operation-end, (C, +100)}\rangle
     $$
   - Since no $\langle T_0, O_1\text{, operation-abort}\rangle$ was found earlier in the backward scan, the recovery manager concludes that operation $O_1$ has **not yet been undone**.
   - It re-executes the logical undo operation: adds $100$ to $C$:
     $$
     C \leftarrow 400 + 100 = 500
     $$
   - It logs a new physical update record: $\langle T_0, C, 400, 500\rangle$.
   - It now successfully writes:
     $$
     \langle T_0, O_1\text{, operation-abort}\rangle
     $$

3. **Skipping Internal Records & Completing Rollback:**
   - With the operation-abort record now logged, the system skips all physical log records of $O_1$ until it encounters $\langle T_0, O_1\text{, operation-begin}\rangle$.
   - It proceeds backward, undoing any earlier updates of $T_0$ (such as $B = 2050 \to 2000$).
   - Finally, it finds $\langle T_0\text{ start}\rangle$, writes $\langle T_0\text{ abort}\rangle$, and terminates.

#### 3. RUET Exam Insights & Examiner Notes
- **The Core Elegance of the Protocol:** Emphasize that the recovery system does not need any ad-hoc patch to handle a crash during logical undo. By logging the logical undo actions physically, **a crash during an undo simply causes the partial undo to be physically undone**, safely restoring the database to a valid state from which the logical undo can be retried cleanly.

---

### Exercise 19.24 · Log-Based Recovery vs. Shadow Paging for Newly Allocated Disk Pages

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.24 (Page 956)
> - **Subtopic:** T12.3 (Log-Based Recovery vs. Shadow Paging)
> - **Prerequisites:** Shadow Paging scheme, Log-based buffer management (Steal/No-Force).
> - **RUET Relevance:** Directly maps to RUET semester final questions comparing Shadow Paging with Log-Based Recovery (e.g., 2017 Q.6d, 2023 Q.7b).

**Question (Silberschatz 7e Exercise 19.24).**
Compare log-based recovery with the shadow-copy scheme in terms of their overheads for the case when data are being added to newly allocated disk pages (in other words, there is no old value to be restored in case the transaction aborts).

#### 1. Core Principles & Concept Overview

- **Log-Based Recovery (WAL):** Maintains an append-only log on stable storage. Changes are made to pages in memory, and dirty pages are written back to their assigned physical disk blocks in-place.
- **Shadow-Copy (Shadow Paging) Scheme:** Maintains two page tables during transaction execution:
  - `current_page_table`: Points to the most up-to-date disk pages.
  - `shadow_page_table`: Points to the original database pages on disk.
  - When pages are updated or newly allocated, they are written to newly allocated physical disk blocks. At commit time, the shadow pointer is atomically updated to point to the current page table. If the transaction aborts, the new blocks are freed.

```text
Shadow Paging with Newly Allocated Pages:
+--------------------+
| Current Page Table | ----> [New Block 101] (Newly Written Data)
+--------------------+ ----> [New Block 102] (Newly Written Data)
| Shadow Page Table  | ----> [NULL / Old State]
+--------------------+
Commit: Write Page Table to disk & swing db_pointer.
Abort:  Discard Current Page Table & deallocate Blocks 101, 102.
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Comparative Breakdown of Overheads

We evaluate overhead across four system dimensions:

###### 1. Logging Overhead:
- **Shadow-Copy Scheme:**
  - Incurred logging cost: **Zero**.
  - Because newly allocated pages do not have old values, and commit is achieved by swinging the root database pointer, no undo log records and no redo data log records need to be written to disk.
- **Log-Based Recovery:**
  - Must write **redo log records** containing the newly inserted data to the log buffer and force them to stable storage at commit time (WAL rule).
  - Undo logging is minimal (only a page deallocation record is needed, since there is no before-image).
  - *Advantage: Shadow Paging.*

###### 2. Page Table & Directory Overhead:
- **Shadow-Copy Scheme:**
  - Allocating new pages requires updating the page directory.
  - At commit time, all modified portions of the page directory (which can span many disk pages in large databases) must be forced to disk before the root pointer can be swapped.
- **Log-Based Recovery:**
  - Page allocation is recorded via small allocation bitmap updates in buffer memory and logged as short log records. No entire page directory needs to be forced.
  - *Advantage: Log-Based Recovery.*

###### 3. Disk Locality & Fragmentation Overhead:
- **Shadow-Copy Scheme:**
  - Completely destroys sequential clustering. Even when pages are newly allocated, subsequent updates to those pages will force them to be relocated to new shadow blocks, scattering related pages across disparate physical disk cylinders.
- **Log-Based Recovery:**
  - Pages are written **in-place**. Newly allocated pages can be assigned contiguous physical cylinder extents, preserving contiguous sequential read performance for subsequent queries.
  - *Advantage: Log-Based Recovery.*

###### 4. Abort Overhead:
- **Shadow-Copy Scheme:**
  - Extremely fast. The system simply discards the `current_page_table` from volatile memory and returns the newly allocated disk blocks to the free list bitmap.
- **Log-Based Recovery:**
  - The recovery manager scans backward and logs compensation/abort records, deallocating the pages in the free space map.
  - *Advantage: Shadow Paging.*

##### Step 2: Summary Matrix

| Evaluation Dimension | Log-Based Recovery (WAL) | Shadow-Copy Scheme |
| :--- | :--- | :--- |
| **Data Logging Cost** | High (must write all inserted data to log) | **None** (zero data logging) |
| **Commit Overhead** | Flush log buffer to disk (sequential write) | Flush modified page tables + pointer swap |
| **Disk Block Locality** | **Preserved** (in-place physical clustering) | Destroyed (high physical fragmentation) |
| **Concurrent Transactions**| **High** (page-level / row-level locks) | Very Low (single-writer page table bottleneck)|
| **Rollback / Abort Cost** | Moderate (undo scan & deallocation logging)| **Instantaneous** (discard memory page table) |

#### 3. RUET Exam Insights & Examiner Notes
- **Direct Exam Mapping:** In RUET 2017 Q.6(d) and 2023 Q.7(b), the exam asks: *"Explain shadow paging recovery technique with its advantages and disadvantages."*
- **Examiner Tip:** While shadow paging has lower data-logging overhead for bulk appends, conclude by emphasizing why enterprise systems (Oracle, SQL Server, PostgreSQL) still choose log-based recovery: **shadow paging does not support fine-grained concurrent transactions**, because having multiple concurrent transactions modify a shared page table requires massive locking that degrades throughput.

---

### Exercise 19.25 · ARIES Checkpoints: Dirty Page Table & RecLSN Redo Optimization

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 (Recovery System) · Exercise 19.25 (Page 956)
> - **Subtopic:** T12.3 (ARIES Recovery, Dirty Page Table, RecLSN, Redo Optimization)
> - **Prerequisites:** ARIES 3-pass protocol, Dirty Page Table (DPT), PageLSN, RecLSN.
> - **RUET Relevance:** Advanced theoretical question on state-of-the-art crash recovery algorithms.

**Question (Silberschatz 7e Exercise 19.25).**
In the ARIES recovery algorithm:
a. If at the beginning of the analysis pass, a page is not in the checkpoint dirty page table, will we need to apply any redo records to it? Why?
b. What is RecLSN, and how is it used to minimize unnecessary redos?

#### 1. Core Principles & Concept Overview

The **ARIES (Algorithm for Recovery and Isolation Exploiting Semantics)** recovery algorithm operates in three distinct passes:
1. **Analysis Pass:** Scans forward from the checkpoint to reconstruct the state of the system at the crash point, rebuilding the **Transaction Table (TT)** and the **Dirty Page Table (DPT)**.
2. **Redo Pass:** Scans forward from the earliest unwritten change ($\min(\text{RecLSN})$) and "repeats history".
3. **Undo Pass:** Scans backward, undoing the actions of all active (loser) transactions using `PrevLSN` pointer chains.

##### Key ARIES Data Structures
- **Dirty Page Table (DPT):** Maintained in cache memory. Contains an entry for every dirty page currently residing in the buffer pool.
- **$\text{PageLSN}$:** Stamped in each physical page header on disk; records the LSN of the most recent log record that updated the page.
- **$\text{RecLSN}$ (Recovery LSN):** Associated with each page entry in the DPT; records the LSN of the log record that **first dirtied** the page since it was last flushed to disk.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Will Redo Records Need to be Applied to a Page Absent from the Checkpoint DPT?

- **Direct Answer:** **Yes, it is entirely possible** that redo records will need to be applied to that page.
- **Technical Justification:**
  1. If a page $P$ is not in the Dirty Page Table at the time the checkpoint is recorded, it means that at that specific instant, page $P$ was **clean** in the buffer pool (or was not loaded in memory at all). In other words, all updates made to $P$ prior to the checkpoint had already been flushed to non-volatile disk storage.
  2. However, **after the checkpoint record was written**, a transaction may have executed a new update on page $P$ before the system crashed!
  3. During the **Analysis Pass**, the recovery manager scans the log forward from the checkpoint. When it encounters the log record for that post-checkpoint update on page $P$, it detects that $P$ is not in the DPT and **dynamically adds page $P$ to the DPT**, setting its $\text{RecLSN}$ to that log record's LSN.
  4. Consequently, during the subsequent **Redo Pass**, the recovery manager will read that log record and apply the redo update to page $P$.
- *(Note: If the page was never updated after the checkpoint, it will never be added to the DPT during the analysis pass, and indeed no redo will ever be applied to it).*

##### Part (b): What is RecLSN, and How Does it Minimize Unnecessary Redos?

###### 1. Definition of RecLSN:
$\text{RecLSN}$ (Recovery Log Sequence Number) is the LSN of the **earliest log record that modified a page since the page was last flushed to disk**.
When a clean page $P$ in the buffer pool is updated by log record $L$:
$$
\text{If } P \notin \text{DPT} \implies \text{Insert } (P, \; \text{RecLSN} = L) \text{ into DPT}
$$
Once page $P$ is flushed to disk, its entry is evicted from the DPT. If $P$ is dirtied again later, its new $\text{RecLSN}$ will be set to the LSN of the new update.

###### 2. How RecLSN Minimizes Unnecessary Redos:
The ARIES recovery algorithm uses $\text{RecLSN}$ to filter out redundant disk I/O and redo computation at two distinct levels:

1. **Global Redo Starting Bound:**
   - The Redo Pass does not scan from the beginning of the log, nor blindly from the checkpoint.
   - It begins scanning forward from:
     $$
     \text{RedoLSN} = \min_{P \in \text{DPT}} P.\text{RecLSN}
     $$
   - Any log records prior to $\text{RedoLSN}$ are guaranteed to have already been written to disk across **all** database pages. Thousands of old log records are completely skipped globally.
2. **Page-Level I/O Avoidance (The Redo Test):**
   - When scanning forward during the redo pass, for every update record $L$ targeting page $P$:
     - **Test 1:** Is page $P$ present in the DPT? If $P \notin \text{DPT}$, the page is completely clean on disk. **Skip redo without touching disk!**
     - **Test 2:** If $P \in \text{DPT}$, is $L < P.\text{RecLSN}$? If yes, this update was flushed to disk prior to the first dirtying event currently tracked. **Skip redo without touching disk!**
   - Only if $P \in \text{DPT}$ and $L \ge P.\text{RecLSN}$ does the recovery engine perform an expensive disk read to fetch page $P$ into memory and check:
     $$
     \text{If } \text{PageLSN} < L \implies \text{Apply Redo}
     $$
     $$
     \text{If } \text{PageLSN} \ge L \implies \text{Skip Redo}
     $$
   - **Performance Impact:** Eliminating the disk read for all pages passing Tests 1 and 2 reduces restart recovery I/O by orders of magnitude.

#### 3. RUET Exam Insights & Examiner Notes
- **Differentiating PageLSN and RecLSN:**
  - $\text{PageLSN}$ is stored on the **disk page itself** (measures the latest update on disk).
  - $\text{RecLSN}$ is stored in the **in-memory DPT** (measures the oldest unwritten update in buffer).
- **Examiner Scoring Focus:** Make sure to highlight that $\text{RecLSN}$ allows ARIES to skip disk reads entirely during the redo pass. Many students only mention skipping the redo logic, forgetting that avoiding the disk read of page $P$ is the primary performance win.

---

## T12.4 · RAID levels

---

### Practice Exercise 12.4 · Parity-Block Allocation Flaw in a 4-Disk RAID Array

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 (Physical Storage Systems) · Practice Exercise 12.4 (Page 583)
> - **Subtopic:** T12.4 (RAID Architecture, Parity Striping, Failure Independence)
> - **Prerequisites:** Parity calculations, RAID 4, RAID 5 block distribution.
> - **RUET Relevance:** Tests fundamental architectural principles of RAID disk arrays: failure domain isolation and parity solvability.

**Question (Silberschatz 7e Practice Exercise 12.4).**
Consider the following data and parity-block arrangement on four disks:

| Disk 1 | Disk 2 | Disk 3 | Disk 4 |
| :---: | :---: | :---: | :---: |
| $B_1$ | $B_2$ | $B_3$ | $B_4$ |
| $P_1$ | $B_5$ | $B_6$ | $B_7$ |
| $B_8$ | $P_2$ | $B_9$ | $B_{10}$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |

The $B_i\text{s}$ represent data blocks; the $P_i\text{s}$ represent parity blocks. Parity block $P_i$ is the parity block for data blocks $B_{4i-3}$ to $B_{4i}$. What, if any, problem might this arrangement present?

#### 1. Core Principles & Concept Overview

##### Fundamental Rule of Redundant Arrays:
The foundational premise of any RAID architecture (levels 1 through 6) is **failure domain isolation**:
> *A parity block and any of the data blocks it protects must NEVER reside on the same physical disk.*

If a parity group consists of data blocks $\{D_1, D_2, \dots, D_k\}$ and parity $P$, the parity equation is:
$$
P = D_1 \oplus D_2 \oplus \dots \oplus D_k
$$
If disk failure occurs, we have 1 lost disk. For the system to reconstruct a lost data block $D_x$, the remaining $(k-1)$ data blocks AND the parity block $P$ must be readable from the surviving disks:
$$
D_x = P \oplus \bigoplus_{j \ne x} D_j
$$
If both $D_x$ and $P$ are located on the failed disk, we are left with 1 equation and 2 unknowns, rendering data reconstruction mathematically impossible.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Analyze Parity Group 1 ($i = 1$)
The question defines:
$$
\text{Parity block } P_i \text{ protects data blocks } B_{4i-3} \text{ to } B_{4i}
$$
For $i = 1$:
- Data blocks covered: $B_{4(1)-3} = B_1$ up to $B_{4(1)} = B_4$, i.e., $\{B_1, B_2, B_3, B_4\}$.
- Parity equation:
  $$
  P_1 = B_1 \oplus B_2 \oplus B_3 \oplus B_4
  $$
- Now look at the physical disk assignments from the table:
  - $B_1$ is located on **Disk 1** (Row 1).
  - $B_2$ is located on **Disk 2** (Row 1).
  - $B_3$ is located on **Disk 3** (Row 1).
  - $B_4$ is located on **Disk 4** (Row 1).
  - $P_1$ is located on **Disk 1** (Row 2)!

##### Step 2: The Catastrophic Failure Mode
- **Scenario:** Suppose **Disk 1** suffers a head crash or hardware failure.
- **Data Lost:** Disk 1 contains both data block **$B_1$** and parity block **$P_1$**. Both are lost simultaneously.
- **Attempted Recovery:**
  - Surviving disks: Disk 2 (has $B_2$), Disk 3 (has $B_3$), Disk 4 (has $B_4$).
  - Reconstruction formula:
    $$
    B_1 = P_1 \oplus B_2 \oplus B_3 \oplus B_4
    $$
  - Because $P_1$ was on Disk 1, $P_1$ is unavailable.
  - The equation has two unknown variables ($B_1$ and $P_1$):
    $$
    B_1 \oplus P_1 = B_2 \oplus B_3 \oplus B_4
    $$
  - There is no mathematical or algorithmic way to solve for $B_1$. **Data block $B_1$ is permanently destroyed by a single disk failure!**

##### Step 3: Analyze Parity Group 2 ($i = 2$)
For $i = 2$:
- Data blocks covered: $B_{4(2)-3} = B_5$ up to $B_8$, i.e., $\{B_5, B_6, B_7, B_8\}$.
- Physical locations:
  - $B_5$ is on **Disk 2** (Row 2).
  - $B_6$ is on **Disk 3** (Row 2).
  - $B_7$ is on **Disk 4** (Row 2).
  - $B_8$ is on **Disk 1** (Row 3).
  - $P_2$ is on **Disk 2** (Row 3)!
- **Identical Failure:** Both data block $B_5$ and its parity block $P_2$ reside on **Disk 2**. A failure of Disk 2 causes permanent, unrecoverable data loss for block $B_5$.

##### Step 4: Root Cause & Correct Architectural Design
- **Root Cause:** A parity stripe of size $K$ data blocks requires at least $K + 1$ disks so that each block resides on a separate physical spindle. The proposed scheme attempted to store 4 data blocks + 1 parity block = 5 blocks across only 4 disks.
- **Correct RAID 5 Configuration on 4 Disks:**
  - With $N = 4$ disks, each parity group must contain $N - 1 = 3$ data blocks and 1 parity block:
    $$
    P_i = B_{3i-2} \oplus B_{3i-1} \oplus B_{3i}
    $$
  - Correct layout:

| Disk 1 | Disk 2 | Disk 3 | Disk 4 |
| :---: | :---: | :---: | :---: |
| $B_1$ | $B_2$ | $B_3$ | $P_1$ |
| $B_4$ | $B_5$ | $P_2$ | $B_6$ |
| $B_7$ | $P_3$ | $B_8$ | $B_9$ |
| $P_4$ | $B_{10}$ | $B_{11}$ | $B_{12}$ |

#### 3. RUET Exam Insights & Examiner Notes
- **Common Exam Trap:** Students seeing the word "RAID" often assume that any configuration labeled with parity blocks automatically tolerates a single disk failure. In exam questions that provide an explicit disk-block table, **always verify that no column contains both a data block and its corresponding parity block**.
- **Grading Rule:** Clearly state: *"The arrangement fails the single-disk fault tolerance requirement because $B_1$ and $P_1$ are co-located on Disk 1, and $B_5$ and $P_2$ are co-located on Disk 2."*

---

### Practice Exercise 12.5 · Architectural Trade-offs of Disk Array Size in RAID 5

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 (Physical Storage Systems) · Practice Exercise 12.5 (Page 583)
> - **Subtopic:** T12.4 (RAID 5 Array Sizing, Reliability, Rebuild Degradation)
> - **Prerequisites:** RAID 5 mechanics, Mean Time to Data Loss (MTTDL), Small write penalty.
> - **RUET Relevance:** Directly tested in RUET 2018 Q.8(c) and 2023 Q.7(c) (comparing RAID levels and analyzing RAID 5 recovery performance).

**Question (Silberschatz 7e Practice Exercise 12.5).**
A database administrator can choose how many disks are organized into a single RAID 5 array. What are the trade-offs between having fewer disks versus more disks, in terms of cost, reliability, performance during failure, and performance during rebuild?

#### 1. Core Principles & Concept Overview

Let $N$ denote the total number of disks in a single RAID 5 array.
- In RAID 5, data and parity are block-interleaved across all $N$ disks.
- One disk's worth of total array capacity is dedicated to distributed parity.
- Storage efficiency:
  $$
  \text{Usable Storage Ratio} = \frac{N - 1}{N} = 1 - \frac{1}{N}
  $$
- Parity storage overhead:
  $$
  \text{Overhead Ratio} = \frac{1}{N}
  $$

Choosing $N$ involves fundamental engineering trade-offs between cost, statistical reliability, and degraded performance.

#### 2. Detailed Step-by-Step Solution

We analyze the four trade-off dimensions requested:

##### 1. Cost & Storage Efficiency
- **More Disks (Large $N$, e.g., $N = 12$ to $16$):**
  - Parity overhead is only $\frac{1}{16} \approx 6.25\%$.
  - Usable capacity is $93.75\%$.
  - **Advantage:** Highly cost-effective; maximizes usable gigabytes per dollar spent on hardware.
- **Fewer Disks (Small $N$, e.g., $N = 3$ to $5$):**
  - For $N = 3$, parity consumes $\frac{1}{3} \approx 33.3\%$ of total capacity.
  - For $N = 4$, parity consumes $25\%$.
  - **Disadvantage:** Higher cost per usable gigabyte.

##### 2. Reliability (Mean Time to Data Loss - MTTDL)
RAID 5 can tolerate the failure of **exactly one disk**. If a second disk fails before the first failed disk is completely rebuilt, catastrophic array failure and total data loss occur.
- The failure rate of an individual disk is $\lambda = \frac{1}{\text{MTTF}_{disk}}$.
- In an array of $N$ disks, the array failure rate is roughly proportional to $N$.
- Once a disk fails, there are $(N - 1)$ surviving disks. The probability that one of these $(N - 1)$ surviving disks fails during the rebuild window $T_{rebuild}$ is:
  $$
  P(\text{second failure}) \approx (N - 1) \cdot \lambda \cdot T_{rebuild}
  $$
- **More Disks (Large $N$):** **Much Lower Reliability.**
  - Higher probability of an initial disk failure.
  - With $(N - 1)$ disks operating under extreme stress during rebuild, the statistical risk of a second disk crashing (or encountering a latent unrecoverable read error) is significantly higher.
- **Fewer Disks (Small $N$):** **Much Higher Reliability.**
  - Lower probability of multiple concurrent disk failures.

##### 3. Performance During Failure (Degraded Mode)
When a disk fails, the array continues operating in degraded mode.
- If a user query requests a block from one of the $(N - 1)$ healthy disks, it is served normally.
- If a user query requests a block that resided on the **failed disk**, the RAID controller must reconstruct it on-the-fly by reading the corresponding blocks from **all $(N - 1)$ surviving disks** and computing their XOR sum:
  $$
  D_{lost} = P \oplus D_1 \oplus D_2 \oplus \dots \oplus D_{N-2}
  $$
- **More Disks (Large $N$):** **Severe Performance Degradation.**
  - Every read to the missing disk generates $(N - 1)$ physical disk read operations across all surviving drives! For $N = 16$, a single lost read triggers 15 disk reads, causing severe channel congestion, queue buildup, and massive latency spikes.
- **Fewer Disks (Small $N$):** **Mild Performance Degradation.**
  - For $N = 4$, reading a lost block requires reading only 3 surviving blocks. Degraded mode latency is significantly lower.

##### 4. Performance During Rebuild
When the failed disk is replaced by a hot spare, the entire capacity of the failed disk must be reconstructed.
- Rebuild requires reading **every single block on all $(N - 1)$ surviving disks** from start to finish, calculating XOR parity, and writing the result sequentially to the new disk.
- **More Disks (Large $N$):** **Much Slower Rebuild & Severe System Throttling.**
  - The aggregate I/O load across $(N - 1)$ disks competing with production database queries is massive.
  - The rebuild process takes days, during which the array remains dangerously vulnerable to a second failure.
- **Fewer Disks (Small $N$):** **Fast Rebuild & Minimal Impact.**
  - Fewer disks are tied up in the rebuild scan; data throughput is higher, and the array returns to the fully protected state much faster.

##### Summary Comparison Matrix

| Evaluation Dimension | Small Array Size ($N = 3 \text{ to } 5$) | Large Array Size ($N \ge 10$) |
| :--- | :--- | :--- |
| **Storage Capacity Overhead** | High ($20\% \text{ to } 33\%$) | **Low** ($6\% \text{ to } 10\%$) |
| **Hardware Cost per Usable GB** | Higher | **Lower** |
| **Statistical Reliability (MTTDL)**| **High** (lower chance of 2nd failure) | Low (high chance of 2nd failure) |
| **Degraded Read Multiplier** | Small ($(N-1) = 2 \text{ to } 4$ reads) | Large ($(N-1) \ge 9$ reads) |
| **Rebuild Duration & Contention** | **Short** / Low user impact | Long / Severe user impact |

#### 3. RUET Exam Insights & Examiner Notes
- **Enterprise Best Practice:** In real-world enterprise database storage (e.g., SAN storage pools), DBAs typically limit RAID 5 array sizes to **$N \le 7$ or $8$ disks**. For larger pools, administrators switch to **RAID 6** (dual parity, tolerating two concurrent failures) or **RAID 10** (striped mirrors).
- **Exam Answer Structure:** Structure your answer exactly around the four headers: *Cost*, *Reliability*, *Degraded Performance*, and *Rebuild Performance*. Examiners award full marks when quantitative formulas ($\frac{N-1}{N}$ and $(N-1)$ read multiplier) are included.

---

### Exercise 12.11 · Online Hot-Spare Rebuild & Access Interference Across RAID Levels

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 (Physical Storage Systems) · Exercise 12.11 (Page 584)
> - **Subtopic:** T12.4 (Hot-Spare Rebuilding & Workload Interference)
> - **Prerequisites:** RAID 0, RAID 1 (Mirroring), RAID 3, RAID 5, RAID 6 mechanics.
> - **RUET Relevance:** Tests real-world database availability and high-performance storage design under continuous $24/7$ operational constraints.

**Question (Silberschatz 7e Exercise 12.11).**
RAID systems typically allow you to replace failed disks without stopping access to the system. Thus, the data in the failed disk must be rebuilt and written to the replacement disk while the system is in operation. Which of the RAID levels yields the least amount of interference between the rebuild and ongoing disk accesses? Explain your answer.

#### 1. Core Principles & Concept Overview

- **Hot-Swapping and Online Rebuilding:** Enterprise storage arrays do not take databases offline when a disk fails. An operator hot-swaps the physical drive (or a software hot-spare is activated), and the RAID controller rebuilds the missing data in the background while processing production transactions.
- **Source of Interference:** Background rebuild processes and ongoing user queries compete for:
  1. Disk head positioning (seek time and rotational latency).
  2. Disk channel / bus bandwidth.
  3. RAID controller CPU and cache bandwidth.
- **Interference Metric:** The level of interference is directly proportional to **how many surviving disks must be accessed** to reconstruct each block, and whether unaffected disk pairs can operate independently.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Evaluate Parity-Based RAID Levels (RAID 3, 4, 5, 6)
- **Mechanics of Rebuild in RAID 3, 4, and 5:**
  - Parity-based schemes do not duplicate data.
  - To reconstruct each missing block on the replacement disk, the rebuild engine must read the corresponding blocks from **all $(N - 1)$ surviving disks** in the array and XOR them together.
  - **Resulting Interference:**
    - **100% of the surviving disks** in the array are under continuous read load from the rebuild process.
    - If a user query attempts to access *any* block on *any* disk in the array, the disk arm must seek away from the sequential rebuild scan to service the user query, and then seek back.
    - This causes extreme head thrashing, destroying I/O throughput across the entire database.
- **Mechanics of Rebuild in RAID 6:**
  - Similar to RAID 5, but involves dual parity calculations (Reed-Solomon or XOR/diagonal parity), requiring heavy read traffic across all surviving drives.

##### Step 2: Evaluate Mirroring (RAID Level 1 and RAID Level 10 / 1+0)
- **Mechanics of Rebuild in RAID 1:**
  - In RAID 1 (mirroring), every disk has an identical mirror counterpart.
  - When a disk fails, its data is completely intact on **a single surviving disk** (its mirror pair).
  - To rebuild the replacement disk, the system only needs to perform a sequential read from **that single mirror disk** and write the data directly to the replacement disk!
  - **Resulting Interference:**
    1. **Zero Interference for Other Disks:** In an array of 8 disks configured as 4 mirrored pairs (RAID 10), the other 3 mirrored pairs (6 disks) experience **zero rebuild traffic**. Queries accessing data on those disks run at 100% full speed with no contention!
    2. **Minimal Interference on the Pair:** For the single surviving mirror drive, user read queries can be interleaved with the sequential background copy, or background rebuild can be throttled during peak hours.

##### Step 3: Comparative Analysis

| RAID Level | Number of Disks Read During Rebuild | Scope of Interference Across Array | Workload Interference Level |
| :--- | :---: | :--- | :--- |
| **RAID 0** | N/A (Cannot rebuild) | Total Data Loss | N/A |
| **RAID 1 / 10** | **Exactly 1 disk** | **Isolated strictly to the failed disk's mirror** | **Least Interference** |
| **RAID 3 / 4** | All surviving disks ($N - 1$) | Global array degradation | High |
| **RAID 5** | All surviving disks ($N - 1$) | Global array degradation | Severe |
| **RAID 6** | All surviving disks ($N - 1$ or $N - 2$) | Global array degradation + CPU parity load | Severe |

##### Step 4: Final Conclusion
**RAID Level 1 (Mirroring)** yields the **least amount of interference** between the rebuild and ongoing disk accesses. Only one healthy drive is read to copy data to the replacement drive, leaving all other drives in the storage subsystem entirely unencumbered.

#### 3. RUET Exam Insights & Examiner Notes
- **Direct Link to RUET 2018 Q.8(c):** In 2018 Q.8(c), students were asked to discuss how RAID recovers a system and compare levels. Emphasizing the **rebuild interference isolation of RAID 1** is a strong differentiator that earns top marks.
- **Key Technical Nuance:** Mention that while RAID 1 incurs a 50% capacity penalty, this rebuild advantage (coupled with no write penalty) is the primary reason high-transaction banking databases prefer RAID 10 over RAID 5/6.

---

### Exercise 12.12 · Disk Scrubbing Mechanics & Latent Sector Defect Prevention

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 (Physical Storage Systems) · Exercise 12.12 (Page 584)
> - **Subtopic:** T12.4 (Disk Scrubbing, Latent Sector Errors, Media Reliability)
> - **Prerequisites:** Bad sector remapping, Parity verification, Unrecoverable Read Errors (URE).
> - **RUET Relevance:** Crucial reliability topic directly aligned with syllabus precautions against failure (2019 Q.4b, 2024 Q.3b).

**Question (Silberschatz 7e Exercise 12.12).**
What is scrubbing, in the context of RAID systems, and why is scrubbing important?

#### 1. Core Principles & Concept Overview

- **Latent Sector Errors (LSE) / Silent Data Corruption:** Modern hard disk drives (HDDs) and solid-state drives (SSDs) store billions of magnetic domains or floating-gate charges. Over time, physical defects, magnetic decay, thermal cycling, or firmware bugs can render individual sectors unreadable.
- **The "Latent" Threat:** If a sector is located in a cold table or archive block that is rarely accessed by normal queries, the corruption remains completely unnoticed (latent) by the operating system and DBMS.
- **Disk Scrubbing (Data Scrubbing):** A proactive background maintenance task where the RAID controller or storage daemon systematically reads every physical block across all disks in the array, verifies sector checksums and parity consistency, and reconstructs damaged sectors before subsequent disk crashes occur.

```text
The Latent Sector Trap During RAID 5 Rebuild:
========================================================================================
1. Disk 1 Crashes! (Array enters Degraded Mode; Rebuild starts)
2. Controller reads Surviving Disks:
   Disk 2: Block 5000 [OK]
   Disk 3: Block 5000 [LATENT SECTOR ERROR! UNREADABLE!] <--- CATASTROPHIC DATA LOSS!
   Disk 4: Block 5000 [OK]
Result: Cannot XOR blocks to rebuild Disk 1 Block 5000! Both Disk 1 and Disk 3 are lost!
========================================================================================
With Scrubbing: Latent error on Disk 3 is detected while Disk 1 is HEALTHY -> Auto-repaired!
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Detailed Mechanics of Disk Scrubbing
Disk scrubbing runs as a low-priority background process during idle hours:
1. **Sequential Sector Verification:** The controller reads disk sectors sequentially across all drives in a parity group:
   $$
   \{D_1, D_2, \dots, D_{N-1}, P\}
   $$
2. **Error-Correcting Code (ECC) Check:** When reading each sector, the disk drive's internal hardware verifies the low-level sector ECC.
3. **Parity Re-computation:** The RAID controller computes:
   $$
   \text{Check} = D_1 \oplus D_2 \oplus \dots \oplus D_{N-1} \oplus P
   $$
   - In a consistent array, $\text{Check} = 0$.
4. **Correction and Remapping:**
   - If an individual disk reports an unreadable sector (Unrecoverable Read Error - URE), the controller uses the surviving data and parity blocks from the other disks to reconstruct the lost sector:
     $$
     D_{bad} = P \oplus \bigoplus_{j \ne bad} D_j
     $$
   - The controller then instructs the affected disk drive to **remap the bad sector** to a pre-allocated healthy spare sector on an alternate track, and writes the reconstructed data into the remapped location.
   - If parity is inconsistent without a reported sector error, the controller logs an integrity alert.

##### Step 2: Why Scrubbing is Essential for RAID Survivability
Scrubbing is critical because of a deadly compounding failure scenario known as **Double Failure During Rebuild**:

1. **The Rebuild Vulnerability Window:**
   - Suppose Disk 1 suffers a complete mechanical failure.
   - The DBA replaces Disk 1, and the RAID controller begins rebuilding its contents.
   - To rebuild the missing disk, the controller **must successfully read 100% of all sectors on all $(N - 1)$ surviving disks**.
2. **The Encounter with a Latent Bad Sector:**
   - If even a **single sector** on one of the surviving disks has decayed into an unreadable state, the controller cannot compute the XOR parity for that stripe.
   - Because Disk 1 is dead, and the surviving disk has an unreadable sector, the array now has **two concurrent block losses in the same stripe**.
   - In RAID 5, this causes the rebuild to abort with an **Unrecoverable Read Error (URE)**, resulting in permanent, unrecoverable data loss or total volume offline failure!
3. **How Scrubbing Prevents Data Loss:**
   - By periodically reading every sector when **all disks are still fully operational**, latent sector errors are caught early while full redundancy is available.
   - The corrupted block is repaired immediately, ensuring that when an actual full disk failure occurs in the future, the surviving disks are guaranteed to be 100% readable during the rebuild.

#### 3. RUET Exam Insights & Examiner Notes
- **Direct Exam Relevance:** Maps directly to precautions against DBMS failures (Unit 7, RUET 2019 Q.4b, 2024 Q.3b).
- **Examiner Scoring Focus:** Always include the phrase:
  > *"Scrubbing prevents latent sector errors from turning a single disk failure into an unrecoverable double-failure event during RAID rebuild."*

---

### Exercise 12.13 · Optimal Storage Architecture for Write-Intensive Fault-Tolerant Workloads

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 (Physical Storage Systems) · Exercise 12.13 (Page 584)
> - **Subtopic:** T12.4 (RAID Selection, Write-Intensive Workloads, Small Write Penalty)
> - **Prerequisites:** RAID 0, RAID 1, RAID 5 small write penalty, Non-Volatile RAM (NVRAM).
> - **RUET Relevance:** Standard architectural decision problem tested in RUET 2018 Q.5(c) and 2023 Q.4(a).

**Question (Silberschatz 7e Exercise 12.13).**
Suppose you have data that should not be lost on disk failure, and the application is write-intensive. How would you store the data?

#### 1. Core Principles & Concept Overview

The application presents two strict design constraints:
1. **High Fault Tolerance:** Zero data loss upon single (or even multiple) disk failures.
2. **Write-Intensive Workload:** High rate of random and sequential write transactions.

##### The Small Write Penalty in Parity RAID:
In parity-based RAID systems (RAID 4, RAID 5, RAID 6), updating a single random data block requires the infamous **Read-Modify-Write cycle**:
- To write a new data block $D_{new}$:
  1. Read old data block from disk: $D_{old}$.
  2. Read old parity block from disk: $P_{old}$.
  3. Compute new parity: $P_{new} = P_{old} \oplus (D_{old} \oplus D_{new})$.
  4. Write new data block: $D_{new}$.
  5. Write new parity block: $P_{new}$.
- **Cost:** **2 disk reads + 2 disk writes = 4 physical disk I/O operations** for a single logical write!
- In RAID 6, updating a block requires **3 disk reads + 3 disk writes = 6 physical I/Os**.
- Under write-heavy workloads, parity-based RAID arrays suffer severe I/O bottlenecks.

```text
Write Penalty Comparison for Updating 1 Block:
-------------------------------------------------------------------------
RAID 5 (Parity):   [Read D_old] + [Read P_old] + [Write D_new] + [Write P_new]  = 4 I/Os!
RAID 1 (Mirror):   [Write Primary D_new] + [Write Mirror D_new] in parallel    = 2 I/Os!
-------------------------------------------------------------------------
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Evaluation of Candidate RAID Configurations

###### 1. RAID Level 0 (Striping):
- Write performance is high, but provides **zero redundancy**. A single disk failure loses all data. **Rejected.**

###### 2. RAID Level 5 / 6 (Distributed Parity):
- High fault tolerance, but the 4-I/O small write penalty creates severe disk head contention, high write latency, and low transactional throughput. **Rejected for write-intensive workloads.**

###### 3. RAID Level 1 (Mirroring) / RAID Level 10 (RAID 1+0):
- **Fault Tolerance:** Every block is written to two independent physical disks. Survived by any single disk failure, and can survive multiple failures as long as no two failed disks form a mirrored pair.
- **Write Performance:**
  - Writing a block requires **exactly 2 writes** (one to the primary disk, one to the mirror disk).
  - Crucially: **Zero read operations are required!**
  - Both writes can be issued completely in parallel by the disk controller.
- **Striping Benefits (RAID 10):** By combining striping (RAID 0) across multiple mirrored pairs (RAID 1), independent write requests to different stripes are executed concurrently across separate spindle pairs.

##### Step 2: Incorporating Non-Volatile Write Caching (NVRAM / Battery-Backed Buffer)
To maximize throughput for write-intensive applications, the physical storage architecture must be augmented with **Non-Volatile RAM (NVRAM)** or **battery-backed enterprise SSD write buffers**:
1. When a transaction issues a write, the data is written directly to duplicate, battery-backed NVRAM write buffers on the storage controller.
2. The DBMS receives an immediate commit acknowledgement (in tens of microseconds).
3. The controller sorts and merges pending writes in NVRAM, flushing them to the physical RAID 1/10 disk drives asynchronously in large, sequential, contiguous blocks.

##### Step 3: Comparative Architectural Scorecard

| Architecture | Write I/O Amplification | Read-Modify-Write Penalty? | Write Throughput | Tolerance to Single Failure? | Storage Capacity Efficiency |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **RAID 0** | 1 write | No | Very High | **No (0% safe)** | 100% |
| **RAID 5** | 4 I/Os (2R + 2W) | **Yes** | Poor | Yes (1 disk) | $\frac{N-1}{N}$ (e.g., 80%) |
| **RAID 6** | 6 I/Os (3R + 3W) | **Yes** | Very Poor | Yes (2 disks) | $\frac{N-2}{N}$ (e.g., 67%) |
| **RAID 10 (1+0)** | **2 writes (in parallel)** | **No** | **High** | **Yes (1 to N/2 disks)** | **50%** |
| **RAID 10 + NVRAM**| **Batched writes** | **No** | **Maximum** | **Yes + Power Loss Safe** | **50%** |

##### Step 4: Final Recommendation
To store write-intensive data that must never be lost on disk failure:
1. Store the data on a **RAID 1+0 (RAID 10)** disk array (striped mirrored pairs).
2. Equip the RAID controller with **redundant, battery-backed Non-Volatile RAM (NVRAM) or enterprise SSD write buffers** to absorb burst writes and eliminate rotational disk latency.
3. Explicitly accept the **50% storage capacity trade-off** as the necessary cost for achieving zero read-modify-write penalty, high random-write IOPS, and robust fault tolerance.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner Expectation:** In RUET exams (e.g., 2018 Q.5c on how RAID models help recovery and 2023 Q.4a on physical storage design), examiners specifically seek:
  1. Mention of the **RAID 5 small write penalty** ($2\text{ reads} + 2\text{ writes} = 4\text{ I/Os}$).
  2. Selection of **RAID 1 or RAID 10** for write-heavy applications.
  3. Mention of **NVRAM / battery-backed write caches** to buffer dirty write blocks safely across power interruptions.

---

## Pedagogical Summary & RUET Final Prep Check

To achieve full marks on T12 recovery and RAID questions in ECE 2215:

1. **Strict 2PL & Log Recovery Coupling:**
   Always remember that physical undo logging requires Strict 2PL. If locks are released early, logical undo logging (operational inverse logging) must be used.
2. **Idempotence of Redo:**
   Redo repeats history blindly from checkpoint or $\min(\text{RecLSN})$. It replays both committed and aborted transaction updates. Idempotency is mathematically guaranteed by the page-level condition:
   $$
   \text{If } \text{PageLSN} \ge \text{RecordLSN} \implies \text{Skip Redo}
   $$
3. **RAID Design Invariants:**
   - Never place a data block and its parity block on the same physical disk.
   - For $N$ disks in RAID 5, each stripe consists of $(N - 1)$ data blocks and $1$ parity block.
   - RAID 1 / RAID 10 is the universally preferred architecture for write-intensive enterprise database engines due to the complete absence of the 4-I/O small write penalty and isolated online rebuild interference.


---

[← Prev: T12 Part 2](T12_Part2_Recovery_Manager_and_Log_Recovery.md) | [Index](00_Index.md) | [Next: T13 Part 1 →](T13_Part1_Security_and_Authorization_A.md)
