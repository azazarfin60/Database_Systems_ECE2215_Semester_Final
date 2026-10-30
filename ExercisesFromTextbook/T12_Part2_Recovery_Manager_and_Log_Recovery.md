---
title: "T12 · Recovery System and RAID (Part 2 · Recovery Manager & Log Tracing)"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T12
topic_id: "T12"
part: 2
exercise_count: 14
source_chapters:
  - "Chapter 17"
  - "Chapter 19"
---

[← Prev: T12 Part 1](T12_Part1_Failure_Types_and_RAID_Intro.md) | [Index](00_Index.md) | [Next: T12 Part 3 →](T12_Part3_Checkpoints_and_RAID_Levels.md)

---

# T12 · Recovery System and RAID (Part 2 · Recovery Manager & Log Tracing)

> [!info] Topic Card
> **Syllabus Unit:** Unit 7 (Recovery System & RAID)  
> **Topic Weight:** 43 printed final marks (6.8% syllabus share across 5/7 finals)  
> **Primary References:** Silberschatz 7e Chapter 17 (§17.1–§17.3), Chapter 19 (§19.1–§19.4, §19.7, §19.9)  
> **Direct RUET Final Hits in this Part:**  
> - ⚠️ **PE 17.1** $\rightarrow$ **Recycled in RUET 2018 Q.8(b)** [2 marks] (*Necessity of recovery manager in failure-free systems*)  
> **Core Concepts Covered:** Role of the Recovery Manager, Atomicity vs. Durability, Write-Ahead Logging (WAL) protocol, Undo/Redo scan directions, Checkpoint horizons, Normal vs. Archival logging, Savepoint partial rollbacks, Deferred vs. Immediate modification, Shadow Paging $\text{B}^+$-tree path copying, Compensation Log Records (CLRs), Physical vs. Logical rollbacks (ARIES NTAs), Multi-Version Concurrency Control (MVCC) buffer snapshots, and Buffer Management Policies (Steal/No-Force).

---

## Master Table of Solved Exercises

| Exercise ID | Type | Subtopic | Core Concept / Question Theme | RUET Exam Relevance |
| :--- | :---: | :---: | :--- | :--- |
| **PE 17.1** | Practice | T12.2 | Recovery manager need in failure-free hardware | ⚠️ **Direct Hit (2018 Q.8b)** |
| **PE 19.1** | Practice | T12.3 | Scan directions: Reverse Undo vs. Forward Redo | High (Underlies 2017 Q.6d, 2023 Q.7b) |
| **PE 19.2** | Practice | T12.3 | Checkpoint purpose, frequency & 3-way overheads | High (2019 Q.4b, 2024 Q.3b) |
| **PE 19.3** | Practice | T12.3 | Normal logging vs. Archival logging garbage collection | High (Disaster & media recovery) |
| **PE 19.4** | Practice | T12.3 | Savepoints architecture & partial transaction rollback | Moderate (Advanced transaction design) |
| **PE 19.5** | Practice | T12.3 | Deferred modification: log records, redo pass & memory | High (2017 Q.6d, 2023 Q.7b comparison) |
| **PE 19.6** | Practice | T12.3 | Shadow paging with $\text{B}^+$-tree: path copying vs. WAL | Moderate (Shadow paging trade-offs) |
| **PE 19.7** | Practice | T12.3 | The flaw of unlogged rollbacks & double-undo anomaly | Very High (Proves necessity of CLRs) |
| **PE 19.8** | Practice | T12.3 | File disk space retention across rollbacks & ARIES NTAs | High (Physical vs. logical recovery) |
| **PE 19.9** | Practice | T12.3 | Free-space reallocation anomalies & post-commit logs | High (Tuple vs. page granularity) |
| **PE 19.11** | Practice | T12.3 | Point-in-time recovery & logical vs. physical redo | High (Archival recovery & compensations) |
| **PE 19.13** | Practice | T12.3 | MVCC snapshot views via undo logs (Oracle CR buffers) | High (Modern DBMS engine internals) |
| **EX 19.16** | Regular | T12.3 | Inconsistency from violating the WAL protocol | Very High (Foundational theorem) |
| **EX 19.17** | Regular | T12.3 | Drawbacks of `no-steal` and `force` buffer policies | Very High (Haerder-Reuter taxonomy) |

---

## T12.2 · Role of the recovery manager

### Exercise 17.1 · Necessity of Recovery Manager in Failure-Free Systems

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 17.1 (Silberschatz 7e Chapter 17, page 831)
> - **Subtopic:** T12.2 · Role of the recovery manager
> - **RUET Relevance:** ⚠️ **Direct Hit in RUET 2018 Q.8(b)** [2 marks]
> - **Core Focus:** Transaction-induced aborts vs. hardware crashes; atomicity preservation

**Question (Silberschatz 7e Exercise 17.1).**  
Suppose that there is a database system that never fails. Is a recovery manager required for this system?

#### 1. Core Principles & Concept Overview

A common misconception among beginner database students is that the **recovery manager** exists solely to recover from hardware crashes, unexpected power outages, or physical disk head destruction.

However, the recovery manager is fundamentally responsible for guaranteeing the **Atomicity (A)** and **Durability (D)** properties of ACID:
1. **System / Hardware Crash Recovery:** Guarantees Durability for committed transactions and cleans up after volatile memory loss.
2. **Transaction-Level Rollback (Abort Processing):** Guarantees **Atomicity** for individual transactions that cannot complete their execution.

Even in a hypothetical environment with 100% hardware availability, zero power fluctuations, and bug-free operating systems, **individual transactions will still abort during normal operations**. Therefore, a recovery manager remains strictly mandatory.

#### 2. Detailed Step-by-Step Solution

**Direct Answer:** **Yes**, a recovery manager is still strictly required.

```text
+-----------------------------------------------------------------------------------+
|                           Hypothetical "Never-Failing" System                     |
|                                                                                   |
|  [Hardware & OS: 100% Reliable]                                                   |
|         |                                                                         |
|         v (No System Crashes / No Disk Failures)                                  |
|                                                                                   |
|  BUT Transactions Still Abort!                                                    |
|         |                                                                         |
|         +--> 1. Internal Logical Errors (Divide by zero, constraint violation)   |
|         +--> 2. Concurrency Control Aborts (Deadlock victim, serialization cycle) |
|         +--> 3. Explicit Application Aborts (User cancels form, API rollback)    |
|         |                                                                         |
|         v                                                                         |
|  [Recovery Manager MUST Intervene]                                                |
|         |                                                                         |
|         +--> Reads Undo Log Records / Executes Rollback Protocol                  |
|         +--> Restores Modified Data Items to Pre-Transaction State                |
|         +--> Releases Latches and Maintains Database Consistency (Atomicity)      |
+-----------------------------------------------------------------------------------+
```

##### Step 1: Why Transactions Abort Independently of Hardware Reliability

Even if the underlying server platform operates flawlessly, transactions can fail to complete due to three non-hardware causes:

1. **Transaction Internal Logical Errors:**
   - A business rule or programmatic condition may prevent completion.
   - *Examples:* Arithmetic overflow, division by zero, non-existent foreign key lookup, credit limit violation, or explicit `CHECK` constraint violations.
   - When an exception is thrown, the transaction must terminate prematurely.

2. **Concurrency Control Interventions:**
   - Under standard multi-user scheduling (such as Two-Phase Locking or Strict 2PL), transactions frequently encounter lock conflicts.
   - When two or more transactions form a cycle in the wait-for graph, a **deadlock** occurs. The concurrency control manager must select a **victim transaction** and abort it to break the circular dependency.
   - Under optimistic concurrency control or Timestamp Ordering (TSO), transactions that violate serializability ordering are systematically aborted and restarted.

3. **User-Initiated / External Application Aborts:**
   - A client application may issue an explicit `ROLLBACK` statement before completing execution (e.g., an e-commerce customer cancels an order on the checkout screen after items have already been reserved in the inventory table).

##### Step 2: The Role of the Recovery Manager During Transaction Abort

When an active transaction aborts:
- It may have already updated multiple data items in the database buffer pool and written those updates to disk (under standard **steal** buffer policies).
- To preserve the **Atomicity** property (the "all-or-nothing" rule), every update made by this aborted transaction must be completely erased.
- The **recovery manager** must:
  1. Scan the transaction's log records in reverse chronological order.
  2. Restore each modified data item to its pre-transaction value using the recorded *old values* ($V_{\text{old}}$).
  3. Clean up transaction state tables and write compensation or abort records.

Without a recovery manager, an aborted transaction would leave partial updates permanently etched into the database, violating consistency and leaving the database corrupted.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Examiner Scoring Key (RUET 2018 Q.8b)
> In RUET 2018 Q.8(b) (2 marks), this exact question was tested: *"Suppose that there is a database system that never failed, is a recovery manager required for this system? Justify your answer."*
> 
> **Marks Distribution:**
> - **1 Mark:** Stating unequivocally **"Yes, it is still required."**
> - **1 Mark:** Justifying with **transaction aborts** (logical errors, deadlocks, user cancellation) and the necessity of enforcing the **Atomicity** property by rolling back uncommitted partial updates.
> 
> **Common Student Error:** Many students answer "No" thinking recovery is only about replaying logs after power failure. Always emphasize that transaction rollback is an integral duty of the recovery manager!

---

## T12.3 · Log-based recovery

### Exercise 19.1 · Log Processing Direction: Reverse for Undo vs. Forward for Redo

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.1 (Silberschatz 7e Chapter 19, page 952)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Directly explains the algorithmic design tested in RUET 2017 Q.6(d) and 2023 Q.7(b)
> - **Core Focus:** Log-based recovery scan directions; causality preservation; idempotence

**Question (Silberschatz 7e Exercise 19.1).**  
Explain why log records for transactions on the undo-list must be processed in reverse order, whereas redo is performed in a forward direction.

#### 1. Core Principles & Concept Overview

Log-based recovery algorithms operate on an append-only sequential log stored on stable media. Each update log record records the state transition of a data item:

$$
\langle T_i, X, V_{\text{old}}, V_{\text{new}} \rangle
$$

During system restart recovery following a crash, the recovery manager classifies transactions into:
- **Redo List ($\mathcal{L}_{\text{redo}}$):** Transactions that have written a $\langle T_i \text{ commit}\rangle$ or $\langle T_i \text{ abort}\rangle$ record before the crash. Their committed updates must be guaranteed (Durability).
- **Undo List ($\mathcal{L}_{\text{undo}}$):** Transactions that were active (wrote $\langle T_i \text{ start}\rangle$) but have no terminal commit record. Their uncommitted updates must be completely erased (Atomicity).

The fundamental question is: *Why does the redo pass scan forward (oldest to newest), while the undo pass must scan backward (newest to oldest)?*

#### 2. Detailed Step-by-Step Solution

```text
Chronological Execution (Time --->)
Log Sequence:  [Rec 1: X <- 10] ---> [Rec 2: X <- 20] ---> [Rec 3: X <- 30]

REDO PASS (Forward Scan: Oldest -> Newest):
  Apply Rec 1: X = 10
  Apply Rec 2: X = 20
  Apply Rec 3: X = 30  ===> Final X = 30 (Matches true committed state!)
  (If backward: X would end up as 10, which is STALE!)

UNDO PASS (Reverse Scan: Newest -> Oldest):
  Transaction T_i performed: X=100 -> X=150 -> X=200
  Log contains:
    Rec A: <T_i, X, 100, 150>
    Rec B: <T_i, X, 150, 200>
  Reverse Undo:
    Undo Rec B: X <- 150
    Undo Rec A: X <- 100 ===> Final X = 100 (Original Pre-Transaction State!)
  (If forward: Undo Rec A sets X=100, then Undo Rec B sets X=150! WRONG!)
```

##### Part 1: Why Redo Must Proceed in the Forward Direction

1. **Reconstructing Chronological State Transitions:**
   - The purpose of the redo phase is to bring the database forward to the exact physical state it had reached just prior to the crash (*repeating history*).
   - Suppose two committed transactions $T_1$ and $T_2$ sequentially updated data item $X$:
     - $T_1$ sets $X = 20$.
     - Later, $T_2$ sets $X = 50$.
   - The sequential log contains:
     $$
     \langle T_1, X, 10, 20 \rangle \quad \dots \quad \langle T_2, X, 20, 50 \rangle
     $$
   - By scanning **forward** (from oldest to newest):
     - The recovery manager first applies $X \leftarrow 20$.
     - It then applies $X \leftarrow 50$.
     - The final state on disk is $X = 50$, which is the correct, chronologically final committed value.
2. **Failure of Reverse Redo:**
   - If redo were processed backward (newest to oldest):
     - It would first apply $X \leftarrow 50$.
     - Then it would apply $X \leftarrow 20$.
     - The final value would be $X = 20$, which erroneously overwrites a newer committed update with an older, superseded value!

##### Part 2: Why Undo Must Proceed in the Reverse Direction

1. **Restoring the Pre-Transaction Initial State:**
   - The purpose of the undo phase is to erase all partial updates performed by uncommitted transactions and restore the exact state that existed *before* the transaction started.
   - Suppose an uncommitted transaction $T_3$ modified data item $Y$ multiple times:
     - Initial value of $Y = 100$.
     - Step 1: $T_3$ updates $Y \leftarrow 150$. Log: $\langle T_3, Y, 100, 150 \rangle$.
     - Step 2: $T_3$ updates $Y \leftarrow 200$. Log: $\langle T_3, Y, 150, 200 \rangle$.
     - System crashes before $T_3$ commits.
   - By scanning **backward** (from newest to oldest):
     - The recovery manager first encounters $\langle T_3, Y, 150, 200 \rangle$ and restores $Y \leftarrow 150$.
     - It then continues backward and encounters $\langle T_3, Y, 100, 150 \rangle$ and restores $Y \leftarrow 100$.
     - The final value of $Y$ is $100$, which is the exact pre-transaction value!
2. **Failure of Forward Undo:**
   - If undo were executed forward:
     - The recovery manager would first process $\langle T_3, Y, 100, 150 \rangle$ and set $Y \leftarrow 100$.
     - Next, it would process $\langle T_3, Y, 150, 200 \rangle$ and set $Y \leftarrow 150$!
     - The final value of $Y$ would remain $150$—an uncommitted intermediate state created by $T_3$! Atomicity would be completely violated.

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Architectural Rule for Exam Tracing
> In RUET numerical recovery tracing questions (such as RUET 2017 Q.6d and 2023 Q.7b):
> - **Redo Pass:** Always scan the log from the checkpoint record **forward** to the end of the log.
> - **Undo Pass:** Always scan from the end of the log **backward** towards the beginning.
> - Demonstrating this opposite scanning direction with concrete variable values ($X_{\text{old}} \rightarrow X_{\text{new}}$) proves to the examiner that you understand the mathematical foundation of write-ahead logging.

---

### Exercise 19.2 · Checkpoint Mechanism: Frequency, Overhead, and Recovery Time Trade-offs

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.2 (Silberschatz 7e Chapter 19, page 952)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Directly informs checkpoint questions in RUET 2019 Q.4(b) and 2024 Q.3(b)
> - **Core Focus:** Checkpointing overhead trade-offs; normal performance vs. MTTR vs. media recovery

**Question (Silberschatz 7e Exercise 19.2).**  
Explain the purpose of the checkpoint mechanism. How often should checkpoints be performed? How does the frequency of checkpoints affect:
- System performance when no failure occurs?
- The time it takes to recover from a system crash?
- The time it takes to recover from a media (disk) failure?

#### 1. Core Principles & Concept Overview

In a naive log-based recovery system without checkpoints:
- The recovery manager must retain the **entire log from day one**.
- Upon a system crash, the recovery manager must scan and replay the entire log from the very beginning of the database history.
- This creates two fatal problems:
  1. The log file consumes unbounded stable storage.
  2. Crash recovery time grows linearly with the age of the database system, eventually taking hours or days to restart (intolerable Mean Time to Recover, MTTR).

The **checkpoint mechanism** solves this by periodically flushing dirty buffer pages to disk and writing a checkpoint record containing the list of currently active transactions. This establishes a bounded horizon past which log records for fully committed transactions are no longer required for crash recovery.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Purpose of the Checkpoint Mechanism
The checkpoint mechanism fulfills three critical objectives:
1. **Flushes Dirty Buffers:** Forces modified data blocks temporarily held in volatile RAM to non-volatile disk storage.
2. **Bounds Log Processing:** Establishes a known point in the log before which all updates by completed transactions are guaranteed to be physically on disk.
3. **Enables Log Pruning (Garbage Collection):** Allows the system to safely truncate and reclaim stable storage occupied by old log records that precede the checkpoint horizon.

##### Step 2: How Often Checkpoints Should Be Performed
Checkpoint frequency is determined by balancing two conflicting engineering objectives:
- **Optimization Objective:** Minimize total operational cost:
  $$
  C_{\text{total}} = C_{\text{normal}} + P(\text{crash}) \times C_{\text{recovery}}
  $$
- Checkpoints are typically triggered based on:
  1. **Log Volume Threshold:** E.g., whenever 100 MB of new log records have been generated.
  2. **Time Interval:** E.g., every 5 to 15 minutes during standard operation.
  3. **Buffer Pressure:** Whenever the proportion of dirty buffer pages exceeds a predefined threshold (e.g., 70% dirty pages).

##### Step 3: Analysis of Checkpoint Frequency on System Metrics

The impact of high checkpoint frequency (frequent checkpoints) versus low frequency (rare checkpoints) across the three scenarios is summarized below:

| Operational Metric | Frequent Checkpoints | Infrequent Checkpoints | Underlying Technical Reason |
| :--- | :--- | :--- | :--- |
| **1. System Performance (No Failure Occurs)** | **Degraded** (Lower throughput, higher latency) | **Optimal** (High throughput, low latency) | Checkpointing forces disk I/O to flush dirty buffer blocks and sync log buffers. Frequent flushing causes disk contention, cache churn, and CPU overhead during normal transactions. |
| **2. System Crash Recovery Time** | **Fast** (Short restart / Low MTTR) | **Slow** (Protracted restart / High MTTR) | With frequent checkpoints, the recovery manager only needs to scan from the most recent checkpoint forward. Infrequent checkpoints require scanning and replaying a much longer log backlog. |
| **3. Media (Disk) Failure Recovery Time** | **Negligible Impact** (Recovery time remains largely unchanged) | **Negligible Impact** (Recovery time remains largely unchanged) | Media recovery requires restoring a complete archival backup (dump) and replaying *all* archival logs since that dump. Regular checkpoints do not alter this log replay volume unless combined with physical disk dumps. |

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Distinction: Crash vs. Media Recovery
> In RUET exams (e.g., 2019 Q.4b and 2024 Q.3b), students frequently write that frequent checkpoints speed up recovery from *disk failure*.  
> **This is technically incorrect!**  
> Checkpoints only bound volatile memory loss during a *system crash*. If the non-volatile disk itself is physically destroyed, the data blocks flushed by the checkpoint are also destroyed. Recovery must start from the last offline tape/remote backup dump, so checkpoint frequency has virtually zero effect on media recovery time. Highlight this distinction for full marks!

---

### Exercise 19.3 · Normal vs. Archival Logging: Log Record Deletion Rules

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.3 (Silberschatz 7e Chapter 19, page 952)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Relevant to archival recovery, log maintenance, and backup administration
> - **Core Focus:** Conditions for log record truncation; crash logging vs. archival media logging

**Question (Silberschatz 7e Exercise 19.3).**  
Some database systems allow the administrator to choose between two forms of logging: *normal logging*, used to recover from system crashes, and *archival logging*, used to recover from media (disk) failure. When can a log record be deleted, in each of these cases, using the recovery algorithm of Section 19.4?

#### 1. Core Principles & Concept Overview

The lifecycle and retention requirements of log records depend entirely on the failure mode they are intended to protect against:
- **Normal Logging (Crash Recovery):** Assumes non-volatile disk storage remains intact (*fail-stop model*). Once a transaction's updates are guaranteed to be permanently stored on the non-volatile database disk, its log records are obsolete for crash recovery.
- **Archival Logging (Media / Disaster Recovery):** Assumes the entire physical disk can be destroyed by head crashes, fire, or catastrophic hardware failure. In this scenario, even if an update is on disk, that disk might be vaporized. Therefore, log records must be retained off-site to replay history against an older baseline database backup.

#### 2. Detailed Step-by-Step Solution

##### Case 1: Normal Logging (Crash Recovery)
Under the Section 19.4 recovery algorithm (checkpoint with active transaction list):

A log record $L$ can be safely deleted if and only if **all** of the following conditions are met:
1. **Committed State:** The transaction $T_i$ that generated $L$ has committed (or aborted and completed rollback).
2. **Dirty Page Flushed to Disk:** All database disk blocks updated by $T_i$ have been physically written out to non-volatile disk storage.
3. **Horizon Past Checkpoint:** A checkpoint has been successfully completed *after* $T_i$ committed and after all its dirty blocks were written.
4. **No Active Transaction Requires Preceding Records:** There is no active transaction currently running whose earliest uncommitted log record precedes $L$.

Mathematically, let $LSN_{\min}$ be the minimum of:
- The Log Sequence Number (LSN) of the oldest update log record of any transaction currently active at or since the checkpoint.
- The earliest LSN associated with any dirty page currently residing in the buffer pool.

Any log record with $LSN < LSN_{\min}$ can be permanently truncated and deleted from disk.

##### Case 2: Archival Logging (Media Recovery)
Under archival logging, disk blocks surviving in the local server are assumed to be susceptible to total destruction.

A log record $L$ can be deleted if and only if:
1. **Full Database Dump Completed:** A full physical backup (database dump) has been successfully executed **after** the update represented by $L$ took place.
2. **Dump Safely Archived:** The database dump has been safely written to independent, offline, or remote tertiary storage (such as magnetic tape, optical archive, or geographically remote cloud storage).
3. **Alternative: Log Off-Loaded:** If incremental backup is used, the log record itself has been safely copied and verified on the remote archival log repository.

Only when a newly verified baseline image encompasses all changes up to and beyond $L$ can $L$ be discarded from the primary server's archival log volume.

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Production Terminology Alignment
> - **Normal Logging:** Corresponds to PostgreSQL's `wal_level = minimal` or SQL Server's `Simple Recovery Model` (where log space is automatically truncated at each checkpoint).
> - **Archival Logging:** Corresponds to Oracle's `ARCHIVELOG` mode or SQL Server's `Full Recovery Model` (where WAL segments are archived continuously and never overwritten until backed up to tape/remote storage).

---

### Exercise 19.4 · Savepoint Architecture & Partial Rollback Mechanics

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.4 (Silberschatz 7e Chapter 19, page 952)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** Moderate · Advanced transaction control and partial rollback implementation
> - **Core Focus:** Nested transaction boundaries; savepoint logging; Compensation Log Records (CLRs)

**Question (Silberschatz 7e Exercise 19.4).**  
Describe how to modify the recovery algorithm of Section 19.4 to implement savepoints and to perform rollback to a savepoint. (Savepoints are described in Section 19.9.3.)

#### 1. Core Principles & Concept Overview

In enterprise application programming, long-running transactions frequently execute multiple discrete logical steps. If an error occurs in step 4, rolling back the entire transaction (steps 1 through 3) causes massive wasted computation.

A **savepoint** allows **partial transaction rollback**:
- The application sets an intermediate marker: `SAVEPOINT s1;`.
- If an exception occurs later, it issues: `ROLLBACK TO SAVEPOINT s1;`.
- Operations executed after `s1` are undone, but operations executed before `s1` remain intact, and the transaction remains in the **active** state.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Logging Modifications for Savepoints
To support savepoints, the recovery manager's logging protocol is augmented with two new log record types and an in-memory tracking structure:

1. **Savepoint Log Record:** When the statement `SAVEPOINT <name>` is executed by transaction $T_i$, write:
   $$
   \langle T_i \text{ savepoint } s \rangle
   $$
2. **Transaction Table Extension:** Maintain an in-memory dictionary for each active transaction $T_i$:
   $$
   \text{SavepointTable}[T_i] = \{ s \mapsto LSN(s) \}
   $$
   mapping each active savepoint name $s$ to the Log Sequence Number ($LSN$) of its corresponding log record.

##### Step 2: Algorithmic Procedure for `ROLLBACK TO SAVEPOINT s`
When the application issues `ROLLBACK TO SAVEPOINT s`:

```text
Algorithm: PartialRollback(T_i, s)
1. TargetLSN = SavepointTable[T_i].get(s);
2. CurrLSN = T_i.LastLSN;
3. While CurrLSN > TargetLSN do:
     Read log record L at CurrLSN;
     If L is an update record <T_i, X, V_old, V_new> then:
         Write Compensation Log Record (CLR): <T_i, X, V_old>;
         Restore data item X = V_old in buffer pool;
     Else if L is a nested savepoint defined after s then:
         Remove nested savepoint from SavepointTable[T_i];
     CurrLSN = L.PrevLSN; // Follow backward pointer chain for T_i
4. Write log record: <T_i rollback_to_savepoint s>;
5. T_i.LastLSN = LSN of the newly written rollback record;
6. Transaction T_i remains in ACTIVE state (continues execution).
```

##### Step 3: Interaction with System Crash Recovery
If the system crashes after a partial rollback to savepoint $s$:
- **Redo Phase:** Scans forward. It reapplies the original updates and then reapplies the CLRs generated during the partial rollback. History is repeated exactly as it happened.
- **Undo Phase:** If $T_i$ had not committed before the crash, $T_i$ is placed on the `undo-list`. The undo pass scans backward. Because CLRs contain `UndoNextLSN` pointers pointing back to records prior to the rollback, the recovery algorithm will **not** redundantly undo actions that were already undone during the partial rollback!

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Crucial Architectural Distinction
> An unexperienced student might assume rolling back to a savepoint terminates the transaction. Always point out that **`ROLLBACK TO SAVEPOINT` leaves the transaction in the `ACTIVE` state**, whereas a standard `ROLLBACK` transitions the transaction to the `ABORTED` terminal state!

---

### Exercise 19.5 · Deferred Database Modification: Log Formats, Redo Rules, and Local Cache Reads

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.5 (Silberschatz 7e Chapter 19, pages 952–953)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Directly contrasts with Immediate Modification tested in RUET 2017 Q.6(d) & 2023 Q.7(b)
> - **Core Focus:** Deferred modification log structure; elimination of Undo; private transaction workspace

**Question (Silberschatz 7e Exercise 19.5).**  
Suppose the deferred modification technique is used in a database.

a. Is the old value part of an update log record required any more? Why or why not?  
b. If old values are not stored in update log records, transaction undo is clearly not feasible. How would the redo phase of recovery have to be modified as a result?  
c. Deferred modification can be implemented by keeping updated data items in local memory of transactions and reading data items that have not been updated directly from the database buffer. Suggest how to efficiently implement a data item read, ensuring that a transaction sees its own updates.  
d. What problem would arise with the above technique if transactions perform a large number of updates?

#### 1. Core Principles & Concept Overview

In database recovery theory, update strategies are split into two paradigms:
1. **Immediate Modification:** Updates made by active transactions are written to the database buffer pool and can be flushed to disk *before* commit (Steal policy). Requires both **Undo** (old values) and **Redo** (new values).
2. **Deferred Modification:** Updates made by active transactions are postponed from being written to the shared buffer pool or disk until the transaction successfully enters the **partially committed** state (No-Steal policy).

#### 2. Detailed Step-by-Step Solution

##### Part (a): Are Old Values Required in Update Log Records?
**Answer:** **No, old values are not required.**

**Technical Justification:**
- In deferred modification, no updates are allowed to modify the shared database buffer or physical disk blocks while the transaction is active.
- If a transaction aborts before reaching its commit point, none of its updates have ever touched the database on disk.
- Therefore, there is **nothing on disk to undo**.
- An update log record only needs to store the new value:
  $$
  \langle T_i, X, V_{\text{new}} \rangle
  $$
  Omitting $V_{\text{old}}$ saves substantial log space and reduces logging I/O overhead.

##### Part (b): Modification to the Redo Phase of Recovery
**Answer:**
Since undo is impossible without old values, the recovery algorithm must be structured so that **an undo phase is never needed**:

1. **Identification of Redo Candidates:**
   - Scan the log to identify all transactions that have both a $\langle T_i \text{ start}\rangle$ record and a $\langle T_i \text{ commit}\rangle$ record. These form the set $\mathcal{L}_{\text{redo}}$.
2. **Execution of Redo Only:**
   - Scan the log forward from the checkpoint and re-apply $\langle T_i, X, V_{\text{new}}\rangle$ **strictly for transactions in $\mathcal{L}_{\text{redo}}$**.
3. **Handling of Incomplete Transactions:**
   - Transactions with a $\langle T_i \text{ start}\rangle$ but **no** $\langle T_i \text{ commit}\rangle$ in the log are completely ignored!
   - Because of deferred modification, their updates were never flushed to disk prior to the crash. Hence, simply doing nothing leaves the database in a completely consistent state, naturally satisfying Atomicity.

##### Part (c): Efficient Implementation of Reads with Local Updates
**Answer:**
To maintain **Read-Your-Own-Writes** consistency within transaction $T_i$:

```text
Local Transaction Workspace: Private Hash Map
  Key: DataItemID  --->  Value: UpdatedValue

Read(X) Procedure:
  1. Probe Private Hash Map for Key X:
     +--> If Found: Return UpdatedValue (Private uncommitted write)
     +--> If Not Found: Read X from Shared Buffer Pool / Disk
```

- Each transaction maintains a private in-memory hash table:
  $$
  \text{LocalWrites}[T_i] = \{ X_j \mapsto V_{\text{new}} \}
  $$
- When transaction $T_i$ executes `read(X)`:
  1. It first probes its private hash map $\text{LocalWrites}[T_i]$.
  2. If an entry for $X$ is present, it returns the locally updated value immediately in $O(1)$ time.
  3. If $X$ is not in the local map, it issues a read request to the shared database buffer pool (fetching from disk if not cached).

##### Part (d): Problems Arising with Large Numbers of Updates
**Answer:**
If a transaction updates thousands or millions of records (e.g., a massive bulk payroll update):

1. **Volatile Memory Exhaustion:**
   - The transaction's private workspace will consume enormous amounts of RAM. If private buffers exceed physical memory, operating system page swapping occurs, causing severe performance degradation.
2. **High Commit Latency Spike:**
   - At commit time, the transaction must suddenly write thousands of log records and propagate all deferred modifications to the shared buffer pool in a single massive burst. This blocks other transactions, creating lock convoying and long tail latency.
3. **Loss of Concurrency:**
   - Long transactions holding large write sets in private memory cannot make their modifications visible, leading to extended lock holding times and increased risk of deadlock.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Immediate vs. Deferred Modification Comparison Table
> This comparison is a favorite theoretical question in RUET semester finals:
> 
> | Feature | Immediate Modification | Deferred Modification |
> | :--- | :--- | :--- |
> | **Disk Write Timing** | Can occur before commit (Steal) | Only occurs after commit (No-Steal) |
> | **Log Record Format** | $\langle T_i, X, V_{\text{old}}, V_{\text{new}} \rangle$ | $\langle T_i, X, V_{\text{new}} \rangle$ |
> | **Recovery Operations** | Both **Undo** and **Redo** | **Redo only** (No Undo) |
> | **Transaction Rollback** | Must restore $V_{\text{old}}$ using log | Simply discard private local workspace |

---

### Exercise 19.6 · Shadow Paging with $\text{B}^+$-Tree Page Tables: Path Copying and Logging Overheads

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.6 (Silberschatz 7e Chapter 19, page 953)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** Moderate · Deepens understanding of alternative recovery schemes
> - **Core Focus:** Copy-on-Write (path copying) in trees; shadow paging vs. WAL overheads

**Question (Silberschatz 7e Exercise 19.6).**  
The shadow-paging scheme requires the page table to be copied. Suppose the page table is represented as a $\text{B}^+$-tree.

a. Suggest how to share as many nodes as possible between the new copy and the shadow copy of the $\text{B}^+$-tree, assuming that updates are made only to leaf entries, with no insertions or deletions.  
b. Even with the above optimization, logging is much cheaper than a shadow copy scheme, for transactions that perform small updates. Explain why.

#### 1. Core Principles & Concept Overview

In basic shadow paging, the database maintains a **Page Table** mapping logical page numbers to physical disk block addresses.
- During transaction execution, updates are written to newly allocated disk blocks (*shadow pages*), and a *current page table* points to them while a *shadow page table* preserves the old pointers.
- At commit, the current page table pointer replaces the shadow page table pointer atomically.

However, copying an entire page table for every transaction is prohibitively expensive. Representing the page table as a $\text{B}^+$-tree allows **Copy-on-Write / Path Copying**, where unmodified branches of the tree are shared between the active and shadow versions.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Node Sharing via Path Copying in $\text{B}^+$-Trees

```text
           Root (Old) ------------------------+
          /          \                        |
       Node A       Node B (Shared)           |
      /      \                                |
   Leaf 1   Leaf 2 (Shared)                   |
     |                                        |
  [Page 1]                                    |
                                              |
(After updating Page 1 -> New Block 1'):      |
                                              v
           Root' (New) ------------------> [Points to Node A' and shared Node B]
          /
       Node A' --------------------------> [Points to Leaf 1' and shared Leaf 2]
      /
   Leaf 1'
     |
  [Block 1'] (New Data Block)
```

**Algorithmic Procedure for Path Copying:**
1. **Leaf Duplication:** When an update modifies a database page referenced by leaf node $L$ of the $\text{B}^+$-tree, allocate a new physical leaf node $L'$. $L'$ contains the updated disk block pointer, while retaining all unchanged pointers to other pages.
2. **Parent Duplication (Upward Propagation):** The parent internal node $P$ of $L$ must now point to $L'$. To avoid mutating the shadow tree, allocate a new internal node $P'$ whose child pointer points to $L'$, while all other sibling pointers point to the existing, unmodified children of $P$.
3. **Propagation to Root:** This copying process recurses upward strictly along the search path from $L$ to the root.
4. **Subtree Sharing:** Any subtree whose descendant leaves are **not** updated is never duplicated! Both the shadow $\text{B}^+$-tree and current $\text{B}^+$-tree point directly to the exact same shared physical nodes.

**Efficiency Calculation:**
- In a tree of height $h$, updating an entry requires copying only $h$ nodes (the path from leaf to root), rather than duplicating all $N$ nodes of the tree.

##### Part (b): Why Logging is Far Cheaper for Small Updates
Even with $\text{B}^+$-tree path copying, Write-Ahead Logging (WAL) is overwhelmingly more efficient for small updates for three physical reasons:

1. **Volume of Written Data (Amplification Factor):**
   - Suppose a transaction modifies a 4-byte customer account balance.
   - **In Shadow Paging with $\text{B}^+$ path copying:** The DBMS must write:
     - 1 newly allocated data page ($4\text{ KB}$ or $8\text{ KB}$).
     - $h$ new $\text{B}^+$-tree index nodes ($h \times 4\text{ KB}$ or $8\text{ KB}$).
     - For $h = 3$, writing a 4-byte update forces at least **$16\text{ KB}$ to $32\text{ KB}$ of physical disk I/O**!
   - **In Write-Ahead Logging (WAL):** The DBMS writes a single update log record:
     $$
     \langle T_i, \text{Account}, \text{balance}, 500, 550 \rangle
     $$
     which is only approximately **$40\text{ bytes}$**! The data page stays in memory buffer.
2. **Random vs. Sequential I/O:**
   - In shadow paging, the new data block and the $h$ tree nodes are allocated in disparate, non-contiguous physical disk blocks, requiring multiple random disk seeks.
   - In WAL, log records are appended sequentially to a continuous log buffer, which is flushed via high-throughput **sequential I/O**.
3. **Destruction of Physical Clustering (Fragmentation):**
   - Shadow paging scatters consecutive logical database pages across random physical disk sectors over time. This ruins sequential read scans for query execution. Logging preserves physical page clustering on disk permanently.

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Why Commercial DBMSs Abandoned Shadow Paging
> In early database systems (such as System R), shadow paging was explored. However, due to the severe write amplification and page table overhead analyzed above, modern enterprise engines (Oracle, PostgreSQL, SQL Server, MySQL InnoDB) unanimously adopt **Write-Ahead Logging (WAL)**. Citing this write-amplification factor ($40\text{ bytes}$ vs. $16\text{ KB}$) in RUET exams will demonstrate deep systems intuition.

---

### Exercise 19.7 · The Flaw of Unlogged Rollbacks: Anomalies from Double-Undo and Overwritten State

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.7 (Silberschatz 7e Chapter 19, page 953)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** Very High · Proves mathematically why Compensation Log Records (CLRs) are necessary
> - **Core Focus:** Repeated rollback anomalies; loss of committed data due to double-undo

**Question (Silberschatz 7e Exercise 19.7).**  
Suppose we (incorrectly) modify the recovery algorithm of Section 19.4 to not log actions taken during transaction rollback. When recovering from a system crash, transactions that were rolled back earlier would then be included in undo-list and rolled back again. Give an example to show how actions taken during the undo phase of recovery could result in an incorrect database state. (Hint: Consider a data item updated by an aborted transaction and then updated by a transaction that commits.)

#### 1. Core Principles & Concept Overview

In professional recovery architectures (such as ARIES and standard WAL), whenever an aborted transaction is rolled back, every restoration action it performs is explicitly recorded in the log as a **Compensation Log Record (CLR)** or an explicit $\langle T_i \text{ abort}\rangle$ record.

If a system *fails* to log rollback actions:
- A transaction $T_1$ that aborted and was rolled back during normal execution will have its original update records still present in the log without any record indicating that they were already undone!
- If a crash occurs later, the restart recovery algorithm will see $T_1$'s start record without a commit or abort record, place $T_1$ on the `undo-list`, and **roll it back a second time**!

This exercise asks us to construct a concrete, mathematically rigorous execution trace demonstrating how this "double-undo" catastrophic failure destroys committed data.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Scenario Construction
Let data item $A$ have an initial value:
$$
A = 10
$$

Now, consider the following sequence of events:

```text
Timeline:
1. T1 starts and updates A: 10 -> 20.
   Log written: <T1, A, 10, 20>
2. T1 aborts during normal operation!
   Recovery manager rolls back T1:
   Sets A = 10 (Restores old value).
   [FATAL BUG]: System does NOT write any log record for this rollback!
3. T2 starts.
4. T2 reads A = 10 and updates A = 50.
   Log written: <T2, A, 10, 50>
5. T2 successfully commits!
   Log written: <T2 commit> (Flushed to disk!)
6. *** SYSTEM CRASH OCCURS! ***
```

##### Step 2: The Log State on Stable Storage at Time of Crash
The physical log on stable disk contains:
1. $\langle T_1 \text{ start}\rangle$
2. $\langle T_1, A, 10, 20\rangle$
3. $\langle T_2 \text{ start}\rangle$
4. $\langle T_2, A, 10, 50\rangle$
5. $\langle T_2 \text{ commit}\rangle$

*(Notice: There is NO record of $T_1$'s rollback or abort!)*

##### Step 3: Crash Recovery Execution (Section 19.4 Algorithm)
Upon reboot, the recovery manager scans the log to form the transaction lists:
- $T_2$ has a $\langle T_2 \text{ commit}\rangle$ record $\implies T_2 \in \mathcal{L}_{\text{redo}}$.
- $T_1$ has a start record but **no** commit or abort record $\implies T_1 \in \mathcal{L}_{\text{undo}}$!

**Phase 1: Redo Pass (Forward Scan)**
- Replays $T_2$'s update:
  $$
  A \leftarrow 50
  $$

**Phase 2: Undo Pass (Backward Scan)**
- The recovery manager processes $\mathcal{L}_{\text{undo}}$, which contains $T_1$.
- It encounters record 2: $\langle T_1, A, 10, 20\rangle$.
- It executes the undo operation by restoring $A$ to its old value:
  $$
  A \leftarrow 10
  $$
- It marks $T_1$ as aborted.

##### Step 4: Analysis of Inconsistency
- What is the final value of $A$ in the database?
  $$
  A = 10
  $$
- **What should the value be?**  
  Transaction $T_2$ successfully committed! Under the **Durability** property of ACID, $T_2$'s update ($A = 50$) must be permanently preserved.
- **The Disaster:**  
  Because $T_1$'s rollback was not logged, $T_1$ was erroneously undone a second time *after* $T_2$ had committed, completely **overwriting and destroying $T_2$'s committed data**!
- Durability and Consistency are fatally compromised.

#### 3. RUET Exam Insights & Examiner Notes

> [!warning] Exam Trap & Takeaway
> This question provides the theoretical proof for why **Compensation Log Records (CLRs)** are indispensable in transaction processing. In RUET exams, if asked *"Why must abort actions be logged?"*, present this exact 5-step scenario ($A=10 \rightarrow 20 \rightarrow 10 \rightarrow 50 \rightarrow \text{crash} \rightarrow 10$). It gives examiners a watertight, concrete proof that cannot be disputed.

---

### Exercise 19.8 · Disk Space Allocation Persistence Across Rollbacks and ARIES NTAs

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.8 (Silberschatz 7e Chapter 19, page 953)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Explains physical vs. logical recovery and ARIES Nested Top Actions
> - **Core Focus:** Space management decoupling; Nested Top Actions (NTAs); avoiding file corruption

**Question (Silberschatz 7e Exercise 19.8).**  
Disk space allocated to a file as a result of a transaction should not be released even if the transaction is rolled back. Explain why, and explain how ARIES ensures that such actions are not rolled back.

#### 1. Core Principles & Concept Overview

In a database management system, a distinction exists between:
- **Logical Operations:** Inserting, updating, or deleting tuples in a relation (owned by a transaction).
- **Physical / Structural Operations:** Allocating a new disk page from the operating system to extend a tablespace, splitting an index page, or updating free-space bitmaps (system-level shared storage operations).

If a transaction $T_1$ allocates a new page $P$ to insert tuples, that page immediately becomes part of the file. Other concurrent transactions may quickly insert records or allocate adjacent space. If $T_1$ aborts, deallocating page $P$ as part of $T_1$'s logical rollback would corrupt the physical structure of the entire file system.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Why Allocated Disk Space Must NOT Be Released on Rollback

```text
+---------------------------------------------------------------------------------+
|                               File Space Extension Conflict                     |
|                                                                                 |
|  1. T1 inserts record -> Table is full -> T1 extends file, allocates Page 99.   |
|  2. T2 immediately inserts another record into Page 99 (or Page 100).           |
|  3. T2 COMMITS!                                                                 |
|  4. T1 ABORTS!                                                                  |
|                                                                                 |
|  DANGER IF DEALLOCATED:                                                         |
|  If T1's rollback releases Page 99 back to the OS:                              |
|  ===> T2's committed record is physically deleted or corrupted!                 |
|  ===> Free-space pointers and page directory links become dangling pointers!    |
+---------------------------------------------------------------------------------+
```

1. **Shared Multi-Transaction Dependencies:**
   - As soon as a page is allocated to a file, concurrent transactions ($T_2, T_3$) may insert their own tuples into that new page or update global space allocation tables.
   - Releasing the page would orphan or destroy committed tuples belonging to other transactions.
2. **File System and Extent Fragmentation:**
   - Repeatedly expanding and shrinking physical files on disk causes severe file-system level fragmentation and requires heavy operating system system-calls (`truncate()`, `fallocate()`).
   - Retaining the allocated page leaves it formatted in the database's free-space map, ready for instantaneous reuse by future transactions without OS overhead.

##### Step 2: How ARIES Ensures Allocation Actions Are Not Rolled Back
The ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) recovery method solves this using **Nested Top Actions (NTAs)**:

1. **Decoupling via Nested Top Actions (NTAs):**
   - The physical allocation of disk space is treated as an independent, atomic sub-operation outside the logical boundary of transaction $T_1$.
   - When $T_1$ triggers page allocation, an NTA is executed.
   - The NTA formats the page, updates the tablespace allocation bitmap, and writes an independent log record.
2. **Use of Compensation Log Records (CLRs) with `UndoNextLSN`:**
   - At the completion of the NTA, a dummy log record is written whose `UndoNextLSN` field points to the log record *prior* to the start of the NTA.
   - When transaction $T_1$ aborts and scans backward during rollback:
     - It encounters the NTA boundary.
     - Following the `UndoNextLSN` pointer, the recovery manager **completely bypasses and jumps over** the physical allocation log records!
   - Thus, $T_1$'s logical tuple insertions on that page are undone (the tuples are marked deleted), but the physical page allocation itself is **never undone**.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Physiological Logging Concept
> Examiners look for the keyword **Physiological Logging** or **Nested Top Action (NTA)**. Emphasize that *logical undos* (erasing customer data) must never interfere with *physical structures* (disk space bitmaps), because physical structures are shared across all concurrent transactions.

---

### Exercise 19.9 · Concurrency Anomalies in Space Reallocation: Page vs. Tuple Locks and Post-Commit Actions

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.9 (Silberschatz 7e Chapter 19, pages 953–954)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Addresses high-concurrency storage engine design
> - **Core Focus:** Tuple vs. page locking; slot reuse collision; post-commit log actions

**Question (Silberschatz 7e Exercise 19.9).**  
Suppose a transaction deletes a record, and the free space generated thus is allocated to a record inserted by another transaction, even before the first transaction commits.

a. What problem can occur if the first transaction needs to be rolled back?  
b. Would this problem be an issue if page-level locking is used instead of tuple-level locking?  
c. Suggest how to solve this problem while supporting tuple-level locking, by logging post-commit actions in special log records, and executing them after commit. Make sure your scheme ensures that such actions are performed exactly once.

#### 1. Core Principles & Concept Overview

In high-performance database engines, **tuple-level locking** is preferred over **page-level locking** because it allows multiple transactions to concurrently insert, update, and delete different rows on the same physical disk page.

However, physical disk space management within a slotted page introduces subtle recovery dependencies when transactions abort.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Problem on Rollback
**Answer:**
1. **Physical Slot Collision / Overwrite:**
   - Transaction $T_1$ deletes record $R_1$ residing in Slot 3 of Page $P$.
   - The space occupied by Slot 3 is immediately returned to Page $P$'s free-space inventory.
   - Transaction $T_2$ now executes an `INSERT` and allocates the newly freed Slot 3 on Page $P$ for its new record $R_2$.
   - Now, $T_1$ aborts!
   - $T_1$'s rollback requires re-inserting $R_1$. If it attempts to restore $R_1$ into its original physical location (Slot 3 of Page $P$), it will **physically overwrite and corrupt $T_2$'s record $R_2$**!
2. **Record ID (RID) Invalidation:**
   - If $T_1$ instead places $R_1$ into a different slot on Page $P$ (or another page), $R_1$'s physical address (`PageID:SlotNumber`) changes.
   - Any secondary index pointing to $R_1$'s old address will now become a **dangling pointer** or point to $T_2$'s record, causing catastrophic index corruption!

##### Part (b): Would This Be an Issue Under Page-Level Locking?
**Answer:** **No, it would not be an issue.**

**Technical Reason:**
- Under page-level locking with Strict Two-Phase Locking (Strict 2PL), transaction $T_1$ must acquire an **exclusive lock (X-lock)** on the entire physical Page $P$ before deleting $R_1$.
- $T_1$ holds this page-level X-lock continuously until it reaches its final `COMMIT` or `ABORT` state.
- Therefore, transaction $T_2$ is blocked from acquiring a lock on Page $P$ and cannot read, modify, or insert any record on Page $P$ until $T_1$ completely finishes.
- The conflict cannot occur.

##### Part (c): Solution Supporting Tuple-Level Locking via Post-Commit Actions
**Answer:**
To achieve maximum concurrency with tuple-level locking without risking collision:

```text
Step 1: On Delete (T1):
  - Do NOT reclaim physical space!
  - Mark tuple R1 with a "TOMBSTONE" (Delete Bit = 1).
  - T1 holds exclusive lock ONLY on Tuple R1.

Step 2: On Insert (T2):
  - T2 cannot reuse R1's slot because it is still marked occupied (tombstone).
  - T2 allocates fresh space elsewhere on the page.

Step 3: At Commit (T1):
  - Write Post-Commit Log Record: <T1, POST_COMMIT_FREE, Page P, Slot 3>
  - Commit T1 and release tuple lock.

Step 4: Asynchronous Execution:
  - Reclaim physical slot 3 and defragment page.
  - PageLSN = LSN of Post-Commit Record (Guarantees Idempotence / Exactly Once).
```

1. **Logical Deletion (Tombstones):**
   - When $T_1$ deletes $R_1$, the system sets a *tombstone flag* (logical delete bit) on $R_1$'s slot header.
   - The physical space is **not** released to the page's free-space list.
   - $T_1$ holds an exclusive lock on tuple $R_1$, preventing any other transaction from accessing that specific tuple.
2. **Post-Commit Space Reclamation Logging:**
   - When $T_1$ commits, write a special log record:
     $$
     \langle T_1 \text{ post\_commit\_free } P, \text{Slot } 3 \rangle
     $$
   - The physical compaction and movement of Slot 3 into the free space list is deferred until *after* $T_1$ commits.
3. **Exactly-Once Guarantee via PageLSN:**
   - Every physical page $P$ maintains a header field `PageLSN` recording the LSN of the latest update applied to it.
   - When the post-commit cleaner frees Slot 3, it sets:
     $$
     \text{PageLSN} = LSN(\langle T_1 \text{ post\_commit\_free } P, \text{Slot } 3 \rangle)
     $$
   - If a crash occurs:
     - During redo, if $\text{PageLSN} \ge LSN(\text{record})$, the space reclamation is already on disk, so it is skipped.
     - If $\text{PageLSN} < LSN(\text{record})$, the reclamation is executed and `PageLSN` is updated.
   - This ensures the operation is strictly **idempotent** and executed exactly once.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Modern Engine Implementation
> This scheme is precisely how modern systems like PostgreSQL and InnoDB work. In PostgreSQL, `DELETE` merely sets `xmax` on the tuple header (tombstone). Physical space is never reclaimed by concurrent transactions until the `VACUUM` process executes post-commit space reclamation.

---

### Exercise 19.11 · Undoing Committed Transactions: Point-in-Time Recovery and SQL Logical Re-Execution

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.11 (Silberschatz 7e Chapter 19, page 954)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Fundamental to disaster recovery, point-in-time recovery (PITR), and compensation
> - **Core Focus:** Erroneously committed transactions; PITR algorithms; physical vs. logical redo

**Question (Silberschatz 7e Exercise 19.11).**  
Sometimes a transaction has to be undone after it has committed because it was erroneously executed—for example, because of erroneous input by a bank teller.

a. Give an example to show that using the normal transaction undo mechanism to undo such a transaction could lead to an inconsistent state.  
b. One way to handle this situation is to bring the whole database to a state prior to the commit of the erroneous transaction (called *point-in-time* recovery). Transactions that committed later have their effects rolled back with this scheme.  
Suggest a modification to the recovery algorithm of Section 19.4 to implement point-in-time recovery using database dumps.  
c. Later nonerroneous transactions can be reexecuted logically, if the updates are available in the form of SQL but cannot be reexecuted using their log records. Why?

#### 1. Core Principles & Concept Overview

Once a transaction commits, its effects become permanent (**Durability**). The database recovery manager cannot arbitrarily invoke normal low-level undo mechanisms on a committed transaction because subsequent independent transactions may have already read and based their business decisions on those committed values.

When human error occurs (e.g., a bank teller accidentally enters a \$1,000,000 deposit instead of \$100), two recovery paths exist:
1. **Compensating Transactions:** Executing a new, inverse transaction at the application layer.
2. **Point-In-Time Recovery (PITR):** Restoring the entire database to a snapshot prior to the error, sacrificing subsequent transactions.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Why Normal Undo Fails for Committed Transactions

**Concrete Counterexample:**
1. Initial account balances:
   $$
   \text{Account } A = \$100, \quad \text{Account } B = \$50
   $$
2. **Erroneous Transaction $T_1$:** A bank teller mistakenly deposits $\$1,000$ into Account $A$:
   - $T_1$ updates $A: 100 \rightarrow 1100$.
   - Log: $\langle T_1, A, 100, 1100 \rangle$.
   - $T_1$ commits!
3. **Legitimate Transaction $T_2$:** The customer immediately transfers $\$800$ from $A$ to $B$:
   - $T_2$ reads $A = \$1100$ (legal, since $T_1$ committed).
   - $T_2$ checks constraint: balance $\ge 800$ (satisfied!).
   - $T_2$ sets $A: 1100 \rightarrow 300$, and sets $B: 50 \rightarrow 850$.
   - Log: $\langle T_2, A, 1100, 300 \rangle$ and $\langle T_2, B, 50, 850 \rangle$.
   - $T_2$ commits!
4. **Catastrophic Failure of "Normal Undo":**
   - Suppose the recovery manager now executes "normal undo" on $T_1$:
   - It reads $\langle T_1, A, 100, 1100 \rangle$ and restores $A$ to its old value:
     $$
     A \leftarrow \$100
     $$
   - The database state is now:
     $$
     \text{Account } A = \$100, \quad \text{Account } B = \$850
     $$
   - **Total Money Created Out of Nowhere:**
     $$
     \text{Initial Sum} = \$150 \quad \implies \quad \text{Current Sum} = 100 + 850 = \$950
     $$
   - The customer transferred $\$800$ to $B$ while having their original $\$100$ balance completely restored! The database has entered a severely corrupted, financially invalid state.

##### Part (b): Point-in-Time Recovery (PITR) Algorithm Using Dumps
To roll back the entire database to a timestamp $t_{\text{target}}$ immediately preceding $T_1$'s commit:

```text
Algorithm: PointInTimeRecovery(DumpFile, ArchivalLog, t_target)
1. Restore:
     Load the most recent full database dump taken at time t_dump (where t_dump < t_target).
2. Redo Pass (Roll-Forward):
     Scan the Archival Log starting from the LSN corresponding to t_dump forward.
     For each log record L encountered:
         If L.Timestamp < t_target then:
             If L is an update record <T_k, X, V_old, V_new> then:
                 Apply update: X = V_new;
         Else:
             Stop log scan!
3. Undo Pass (Rollback Incomplete Transactions):
     Identify all transactions active at t_target that had not committed before t_target.
     Scan backward and undo their operations.
4. Bring Database Online:
     The database is now consistent at exact time t_target (Erroneous T1 never existed).
```

##### Part (c): Why Later Transactions Must Be Re-Executed via SQL (Not Log Records)
**Answer:**
Physical/physiological log records store state-based values:
$$
\langle T_2, A, 1100, 300 \rangle
$$
- These state values were computed by $T_2$ **based on the erroneous state** ($A = 1100$).
- If we replayed $T_2$'s physical log record, it would blindly set $A = \$300$! That would instantly re-inject the effects of the erroneous transaction back into the database.
- In contrast, if $T_2$ is re-executed logically using its original SQL:
  ```sql
  UPDATE Account SET balance = balance - 800 WHERE account_id = 'A';
  ```
  The SQL logic will evaluate against the true restored balance ($A = \$100$), detect that funds are insufficient ($100 - 800 < 0$), and abort cleanly, preserving database integrity!

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Real-World Enterprise Relevance
> Point-In-Time Recovery (PITR) is a standard disaster-recovery feature in PostgreSQL and Oracle. Emphasize to the examiner that **physical log records cannot be replayed across an altered history**, because physical records carry state deltas predicated on values that no longer exist.

---

### Exercise 19.13 · MVCC Snapshot Views via Undo Logs: Oracle Buffer Handling Scheme

> [!info] Exercise Metadata
> - **Exercise:** Practice Exercise 19.13 (Silberschatz 7e Chapter 19, pages 954–955)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** High · Bridge between Recovery Systems (T12) and Concurrency / Isolation (T10/T11)
> - **Core Focus:** Multi-Version Concurrency Control (MVCC); Oracle Consistent Read (CR) blocks; Undo segments

**Question (Silberschatz 7e Exercise 19.13).**  
The Oracle database system uses undo log records to provide a snapshot view of the database under snapshot isolation. The snapshot view seen by transaction $T_i$ reflects updates of all transactions that had committed when $T_i$ started and the updates of $T_i$; updates of all other transactions are not visible to $T_i$.

Describe a scheme for buffer handling whereby transactions are given a snapshot view of pages in the buffer. Include details of how to use the log to generate the snapshot view. You can assume that operations as well as their undo actions affect only one page.

#### 1. Core Principles & Concept Overview

In traditional locking (Strict 2PL), **readers block writers and writers block readers**.  
Modern database engines avoid this bottleneck using **Multi-Version Concurrency Control (MVCC)** under **Snapshot Isolation (SI)**:
- PostgreSQL implements MVCC by appending new tuple versions directly into data tables (*in-place multi-versioning*).
- Oracle, MySQL InnoDB, and Undo-based engines implement MVCC by keeping only the latest version in the data page and using **undo log records** (stored in *undo tablespaces / rollback segments*) to reconstruct older versions on-the-fly for readers.

#### 2. Detailed Step-by-Step Solution

```text
+-----------------------------------------------------------------------------------+
|                        Oracle Consistent Read (CR) Buffer Flow                    |
|                                                                                   |
|  Transaction Ti starts at SCN = 100.                                              |
|  Ti reads Page P.                                                                 |
|                                                                                   |
|  [Buffer Pool: Page P]                                                            |
|  +-------------------------------------+                                          |
|  | Page Header: PageSCN = 140          |  ===> 140 > 100 (Page is TOO NEW for Ti!)|
|  | Latest Data: Balance = $5,000       |                                          |
|  | Undo Pointer -> [Undo Record #42]   |                                          |
|  +-------------------------------------+                                          |
|                     |                                                             |
|                     v (Allocate Private Memory Buffer)                            |
|  [Private CR Buffer (Page P')] <------+                                           |
|  | Copy of Page P                     |                                           |
|  +------------------------------------+                                           |
|                     |                                                             |
|                     v Apply Undo Record #42                                       |
|  Rolls back Balance to $4,200.                                                    |
|  Header becomes PageSCN = 95.                                                     |
|                     |                                                             |
|                     v Check: PageSCN (95) <= Ti.SCN (100)?                        |
|  ===> YES! Consistent Snapshot Achieved. Ti reads $4,200 from CR Buffer!          |
+-----------------------------------------------------------------------------------+
```

##### Step 1: Timestamping and SCN Allocation
1. **System Change Number (SCN):** The database maintains a monotonically increasing logical clock (SCN).
2. **Transaction Snapshot Horizon:** When transaction $T_i$ begins, it is assigned a start timestamp:
   $$
   SCN(T_i)
   $$
   $T_i$'s snapshot must reflect all commits where $SCN_{\text{commit}} \le SCN(T_i)$, and must hide all updates where $SCN > SCN(T_i)$ or updates from active, uncommitted transactions.

##### Step 2: Buffer Pool Inspection Protocol
When transaction $T_i$ requests a page $P$:
1. $T_i$ locates Page $P$ in the shared buffer cache.
2. It examines the page header:
   - **`PageSCN`:** The SCN of the most recent transaction that modified Page $P$.
   - **`ActiveTransactionFlag`:** Indicates whether an active transaction is currently holding an uncommitted lock on the page.
3. **Snapshot Visibility Test:**
   - If $\text{PageSCN} \le SCN(T_i)$ and the modifying transaction has committed:
     - The page is **directly visible** to $T_i$.
     - $T_i$ reads Page $P$ directly from the shared buffer pool without copying.

##### Step 3: Reconstruction of Consistent Read (CR) Buffers
If $\text{PageSCN} > SCN(T_i)$ or the page contains uncommitted modifications:
1. **Allocate Ephemeral CR Buffer:**
   - The buffer manager allocates a private, ephemeral memory block called a **Consistent Read (CR) page copy**: $P'$.
   - It performs a fast memory copy of Page $P$ into $P'$.
2. **Backward Rollback via Undo Records:**
   - The header of $P'$ contains an `UndoPtr` pointing to the latest undo record in the undo tablespace.
   - The recovery engine fetches the undo record:
     $$
     \langle T_k, P, \text{old\_data}, \text{PrevUndoPtr} \rangle
     $$
   - It applies this undo record to the private buffer $P'$, effectively rolling back $T_k$'s update.
   - It updates the header of $P'$ to reflect the prior SCN.
3. **Iteration Until Snapshot Horizon is Reached:**
   - $T_i$ compares the new $\text{PageSCN}(P')$ against $SCN(T_i)$.
   - If $\text{PageSCN}(P') > SCN(T_i)$, it follows `PrevUndoPtr` and applies the next older undo record.
   - This loop repeats until a version of the page is materialized where:
     $$
     \text{PageSCN}(P') \le SCN(T_i)
     $$
4. **Execution:** $T_i$ executes its query against $P'$. The shared buffer pool and physical disk remain completely unmodified.

##### Step 4: The "Snapshot Too Old" Anomaly (ORA-01555)
Because undo segments are organized as circular ring buffers, old undo records are overwritten once the space is needed by newer transactions. If a very long-running query takes hours to complete, its required undo records may have been overwritten, resulting in the famous error:
$$
\text{ORA-01555: snapshot too old: rollback segment too small}
$$

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] The Golden Rule of Modern Concurrency
> In RUET exams, explaining that **"Readers never block writers, and writers never block readers"** through undo-generated CR buffers demonstrates top-tier understanding of database engine internals.

---

### Exercise 19.16 · Write-Ahead Logging (WAL) Protocol Violation and Unrecoverable States

> [!info] Exercise Metadata
> - **Exercise:** Regular Exercise 19.16 (Silberschatz 7e Chapter 19, page 955)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** Very High · Foundational question on Write-Ahead Logging (WAL)
> - **Core Focus:** Proof of WAL necessity; atomicity corruption upon crash

**Question (Silberschatz 7e Exercise 19.16).**  
Explain how the database may become inconsistent if some log records pertaining to a block are not output to stable storage before the block is output to disk.

#### 1. Core Principles & Concept Overview

The **Write-Ahead Logging (WAL) Protocol** enforces two mandatory rules governing the interaction between volatile buffer memory and stable non-volatile storage:

> [!important] The Two Fundamental WAL Invariants
> 1. **WAL Rule 1 (The Steal Rule / Pre-Write Flush):** Before any dirty data block in volatile cache is written to non-volatile disk storage, all log records pertaining to that block up to that update **must** be flushed to stable storage.
> 2. **WAL Rule 2 (The Commit Rule / Force-Log):** Before a transaction enters the committed state, all of its log records (including the commit record) **must** be flushed to stable storage.

Exercise 19.16 directly asks: *What catastrophic failure occurs if WAL Rule 1 is violated?*

#### 2. Detailed Step-by-Step Solution

```text
+-----------------------------------------------------------------------------------+
|                        VIOLATION OF WAL RULE 1 (Disaster Trace)                   |
|                                                                                   |
|  1. In Volatile RAM:                                                              |
|     - Transaction T1 modifies X: 100 -> 999.                                      |
|     - Log Record written to Log Buffer: <T1, X, 100, 999>                         |
|                                                                                   |
|  2. Buffer Manager Steals Block:                                                  |
|     - Buffer pool runs out of memory.                                             |
|     - [VIOLATION]: Flushes Block containing X=999 to DISK!                        |
|     - Log Buffer <T1, X, 100, 999> remains in volatile RAM (NOT flushed)!         |
|                                                                                   |
|  3. POWER FAILS / CRASH OCCURS!                                                   |
|     - Volatile RAM (Log Buffer) is WIPED OUT!                                     |
|                                                                                   |
|  4. Restart Recovery:                                                             |
|     - On Disk: X = 999 (Dirty uncommitted write).                                 |
|     - On Stable Log: NO RECORD of T1 modifying X exists!                          |
|     - Recovery Manager CANNOT UNDO T1!                                            |
|     ===> X = 999 is permanently baked into the database! (Atomicity Destroyed!)  |
+-----------------------------------------------------------------------------------+
```

##### Step 1: Detailed Step-by-Step Failure Scenario

1. **Initial Consistent State:**
   - Data item $X$ resides on disk block $B$ with value $X = 100$.
2. **Transaction Update in Volatile Memory:**
   - Active transaction $T_1$ updates $X$ to $999$.
   - The buffer manager updates the page in RAM.
   - The log record $\langle T_1, X, 100, 999 \rangle$ is appended to the **volatile log buffer** in RAM.
3. **The WAL Violation (Premature Block Write):**
   - The database buffer manager experiences memory pressure. It chooses block $B$ as a victim for replacement (Steal policy).
   - **Violation:** Block $B$ (containing $X = 999$) is written out to disk.
   - However, the operating system / DBMS **fails to flush the log buffer to stable disk first**. The log record $\langle T_1, X, 100, 999 \rangle$ remains exclusively in volatile memory.
4. **System Crash:**
   - A power outage occurs immediately.
   - Volatile memory is instantly erased. The log buffer containing $\langle T_1, X, 100, 999 \rangle$ is lost forever.
   - Non-volatile disk retains block $B$ containing the uncommitted value $X = 999$.

##### Step 2: Consequence During Restart Recovery
Upon system reboot:
1. The recovery manager scans the stable log to identify transactions needing undo.
2. **The log on stable storage contains zero information about $T_1$'s update on $X$!**
3. The recovery manager has no way of knowing that $X$ was ever changed from $100$ to $999$, nor does it have the old value ($100$) needed to restore it.
4. Consequently, no undo operation is performed on block $B$.
5. The uncommitted update $X = 999$ remains permanently stored in the database!

##### Step 3: Fundamental Property Violated
- The **Atomicity** property of ACID is shattered: a transaction that never committed has had its partial updates permanently incorporated into the database.
- The **Consistency** property is shattered: invariants depending on $X$'s true value are violated.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] The Formal Definition of WAL
> When answering this question in RUET exams, state the formal WAL theorem:
> $$
> \text{LSN}_{\text{log\_flushed}} \ge \text{PageLSN}(B) \quad \text{prior to } \text{DiskWrite}(B)
> $$
> If $\text{PageLSN}(B) > \text{LSN}_{\text{log\_flushed}}$, writing block $B$ to disk creates a fatal unrecoverable hazard.

---

### Exercise 19.17 · Buffer Management Architectures: Trade-offs of No-Steal and Force Policies

> [!info] Exercise Metadata
> - **Exercise:** Regular Exercise 19.17 (Silberschatz 7e Chapter 19, page 955)
> - **Subtopic:** T12.3 · Log-based recovery
> - **RUET Relevance:** Very High · Haerder-Reuter recovery classification matrix
> - **Core Focus:** Buffer management policies; Steal vs. No-Steal; Force vs. No-Force

**Question (Silberschatz 7e Exercise 19.17).**  
Outline the drawbacks of the no-steal and force buffer management policies.

#### 1. Core Principles & Concept Overview

In their seminal 1983 paper, Theo Haerder and Andreas Reuter established the universal taxonomy for database recovery and buffer management based on two independent orthogonal dimensions:

```text
                      BUFFER MANAGEMENT MATRIX
                               Steal?
                     YES                   NO
             +---------------------+---------------------+
       YES   | Steal / Force       | No-Steal / Force    |
Force?       | (Requires Undo)     | (No Undo / No Redo) |
             +---------------------+---------------------+
       NO    | Steal / No-Force    | No-Steal / No-Force |
             | (Modern Standard)   | (Requires Redo)     |
             +---------------------+---------------------+
```

1. **Steal vs. No-Steal:**
   - **Steal:** The buffer manager can evict (write to disk) a dirty page updated by an *uncommitted* transaction to free up buffer space for another transaction. $\implies$ **Requires UNDO logging**.
   - **No-Steal:** The buffer manager is strictly forbidden from writing a dirty page to disk until the transaction has committed. $\implies$ **Eliminates UNDO logging**.
2. **Force vs. No-Force:**
   - **Force:** At commit time, the buffer manager *must* synchronously write all dirty pages updated by the transaction to disk before commit completes. $\implies$ **Eliminates REDO logging**.
   - **No-Force:** At commit time, updated pages can remain dirty in memory buffers; only sequential log records are forced to disk. $\implies$ **Requires REDO logging**.

Exercise 19.17 requires analyzing the severe operational drawbacks of adopting `no-steal` and `force`.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Drawbacks of the `No-Steal` Policy

Under `no-steal`, every page modified by an active transaction must remain pinned in volatile memory until that transaction completely finishes:

1. **Severe Memory Starvation and Transaction Size Limits:**
   - If a batch transaction updates 500,000 rows across 50,000 distinct database pages, all 50,000 pages must be simultaneously held in volatile RAM.
   - If the total buffer pool contains only 32,000 frames, the transaction **cannot execute**! The system either aborts the transaction or deadlocks due to memory exhaustion.
   - `No-steal` makes large bulk updates, data warehouse loads, and long-running batch jobs virtually impossible.
2. **Drastic Reduction in Cache Hit Rates:**
   - Inactive dirty pages belonging to long-running transactions remain pinned in RAM, stealing buffer frames that could otherwise cache hot, frequently accessed read pages.
   - This severely degrades overall query throughput for all concurrent users.
3. **Complex Buffer Replacement Interference:**
   - Standard cache eviction algorithms (such as LRU, 2Q, or Clock) are paralyzed because they are legally prohibited from evicting dirty pages, forcing suboptimal eviction of useful clean pages.

##### Step 2: Drawbacks of the `Force` Policy

Under `force`, a transaction cannot commit until every database page it modified is physically written to disk:

1. **Massive Commit Latency (Random I/O Bottleneck):**
   - A single transaction updating 20 rows scattered across 20 distinct database pages requires **20 independent random disk writes** to different physical sectors at commit time.
   - Because disk writes are slow (especially on rotating media and high-latency arrays), the transaction must block and wait, leading to horrific commit latency.
2. **Destruction of I/O Batching / Absorption:**
   - In high-throughput transaction processing, a single "hot" page (such as a branch account balance or counter) is updated hundreds of times per second by different transactions.
   - Under `no-force`, that page remains in memory and absorbs all 1,000 updates, eventually being flushed to disk once.
   - Under `force`, that single page must be written to disk **1,000 separate times** (once for each committing transaction), completely saturating disk write bandwidth!
3. **Write Amplification:**
   - Modifying a single 4-byte attribute on an 8 KB page requires writing the entire 8,192-byte page to disk.
   - In contrast, a `no-force` policy appends a 40-byte log record sequentially, deferring page writes to background asynchronous checkpoint flushers.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] The Universal Standard: Steal / No-Force
> Conclude answers in RUET exams by highlighting that **all modern commercial DBMSs (PostgreSQL, Oracle, SQL Server, MySQL InnoDB) use the `Steal / No-Force` architecture**.
> - `Steal` maximizes buffer memory utilization.
> - `No-Force` maximizes transaction commit speed through sequential log writes.
> - The trade-off is that `Steal / No-Force` requires both **Undo** and **Redo** recovery mechanisms during restart, which is managed via WAL and ARIES.


---

[← Prev: T12 Part 1](T12_Part1_Failure_Types_and_RAID_Intro.md) | [Index](00_Index.md) | [Next: T12 Part 3 →](T12_Part3_Checkpoints_and_RAID_Levels.md)
