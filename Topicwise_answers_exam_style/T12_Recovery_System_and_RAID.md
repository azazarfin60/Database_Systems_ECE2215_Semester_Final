---
title: "T12 · Recovery System and RAID · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T11 · Concurrency Control Protocols](T11_Concurrency_Control_Protocols.md) | [Explanation layer](../Topicwise_answers_explaination/T12_Recovery_System_and_RAID.md) | [Next: T13 · Security, Indexing & Hashing →](T13_Security_Indexing_and_Hashing.md)

---

# T12 · Recovery System and RAID

> [!info] Topic card
> **Syllabus:** Unit 7 · **Weight:** 43 final marks (6.8%) in 5/7 papers
> **Sources:** Textbook Ch. 12 §12.5, Ch. 17 §17.1–17.3, Ch. 19 §19.1–19.4 · Deck 01 Slide 23, Deck 07 Slide 8
> **Blocks in this file:** 13 final questions (11 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T12.1 | Failure classification, precautions, recovery methods | 17 + 0 | 2017 Q.6(c), 2018 Q.5(c) (part 1), 2019 Q.4(b), 2023 Q.7(a), 2024 Q.3(b) | [[#T12.1 · Failure classification, precautions, recovery methods\|Go]] |
| T12.2 | Role of the recovery manager | 4 + 0 | 2018 Q.8(b) | [[#T12.2 · Role of the recovery manager\|Go]] |
| T12.3 | Log-based recovery and shadow paging | 7 + 0 | 2017 Q.6(d), 2023 Q.7(b) | [[#T12.3 · Log-based recovery and shadow paging\|Go]] |
| T12.4 | RAID levels, comparison, and recovery role | 15 + 0 | 2018 Q.5(c) (part 2), 2018 Q.8(c), 2023 Q.4(a), 2023 Q.7(c), 2024 Q.7(c) | [[#T12.4 · RAID levels, comparison, and recovery role\|Go]] |

---

## T12.1 · Failure classification, precautions, recovery methods

### 2017 Q.6(c) · 03 Marks

*Section B · Asked in: 2017, 2023 (CLO2) · L2 merge*

**Question (2017 Q.6(c)).** Classify and discuss the failures in DBMS.

**Question (2023 Q.7(a)).** Explain the different types of failures that can occur in a database system.

**Answer.**

A database management system experiences three main classes of failure based on the affected storage component:

1. **Transaction Failure:** An individual transaction aborts before completing.
   - *Logical Error:* Caused by internal transaction logic or bad data (such as division by zero, arithmetic overflow, or data not found).
   - *System Error:* The system enters an undesirable state (such as a deadlock or timeout) and terminates the transaction.
2. **System Crash:** A hardware failure, power outage, or operating system bug halts the database server.
   - The contents of **volatile storage** (main memory buffers) are lost.
   - The contents of **non-volatile storage** (disk drives) remain uncorrupted (*fail-stop assumption*).
3. **Disk Failure:** Physical damage destroys data blocks on non-volatile media.
   - Causes include head crashes, magnetic surface defects, or transfer errors.
   - Recovery requires redundancy such as RAID arrays or archival backups.

*Variant for 2023 Q.7(a) (CLO2, 3 marks):* The same three-part classification directly answers the question.

---

### 2018 Q.5(c) · Part 1 Failures (2 of 4 Marks)

*Section B · Asked in: 2018 · Part 1 of 2 (2 marks for failure types)*

**Question.** Discuss each type of failure that can happen in DBMS. How does RAID model help to recover a system?

*See also:* [[#2018 Q.5(c) · Part 2 RAID Recovery (2 of 4 Marks)]] for the second part.

**Answer.**

A DBMS is subject to three primary failure types:

1. **Transaction Failure:** A transaction cannot continue due to internal logical errors (invalid inputs, overflow) or system-induced conditions (deadlocks).
2. **System Crash:** Hardware faults or power cuts wipe volatile RAM. Disk storage remains intact under the fail-stop assumption.
3. **Disk Failure:** Head crashes or unreadable physical sectors destroy non-volatile disk blocks.

---

### 2019 Q.4(b) · 05 Marks

*Section A · Asked in: 2019, 2024 (CO1) · L2 merge*

**Question (2019 Q.4(b)).** How many ways a DBMS could be failed? What precautions should be taken considering the failure of DBMS and point out the recovery methods.

**Question (2024 Q.3(b)).** Discuss the ways of DBMS can be failed. Also, mention the precautions should be taken considering the failure of DBMS and point out the recovery methods.

**Answer.**

#### 1. Ways a DBMS Can Fail
A DBMS can fail in three primary ways:
- **Transaction Failure:** Caused by logical errors (overflow, invalid input) or system errors (deadlock aborts).
- **System Crash:** Loss of volatile main memory from power loss, CPU faults, or operating system crashes.
- **Disk Failure:** Loss of non-volatile disk storage caused by head crashes or bad sectors.
- *(Site / Disaster Failure):* Physical destruction of an entire data center caused by fire, flood, or earthquake.

#### 2. Precautions Against DBMS Failures
- **Write-Ahead Logging (WAL):** Force log records to stable storage before writing modified data pages to disk.
- **Uninterruptible Power Supply (UPS) & NVRAM:** Use battery-backed caches to prevent incomplete writes during sudden power loss.
- **Disk Redundancy (RAID):** Use mirroring (RAID 1) or parity (RAID 5/6) to survive single or double disk failures.
- **Archival Off-Site Backups:** Periodically copy full database dumps and log files to remote tape or cloud storage.

#### 3. Recovery Methods
- **Log-Based Recovery:**
  - *Undo:* Reverses uncommitted updates using old values from the log.
  - *Redo:* Re-applies committed updates using new values from the log.
- **Checkpoints:** Periodically flushes dirty buffer blocks and logs active transactions, bounding the restart log scan.
- **Shadow Paging:** Writes updates to a separate page copy and switches pointers atomically, avoiding undo/redo logs.
- **Archival Restore and Roll-Forward:** Restores the last offline backup and replays subsequent archived log records.

*Short version for 2024 Q.3(b) (CO1, 4 marks):* Provide the same three sections in concise bullet points to fit the 4-mark time limit.

---

## T12.2 · Role of the recovery manager

### 2018 Q.8(b) · 04 Marks

*Section B · Asked in: 2018 · L1 (asked once) · Textbook Exercise 17.1*

**Question.** Suppose that there is a database system that never failed, is a recovery manager required for this system? Justify your answer.

**Answer.**

**Yes, a recovery manager is still required.**

Even in a hypothetical system where the hardware and operating system never crash, a recovery manager is essential for the following reasons:

1. **Transactions Still Abort:** A failure-free hardware platform prevents system crashes and disk failures. But individual transactions still fail and must be rolled back.
2. **Causes of Transaction Abort:**
   - *Logical Errors:* A transaction may encounter bad user input, division by zero, arithmetic overflow, or missing data.
   - *Explicit User Aborts:* An application or user may voluntarily cancel an operation (such as issuing a `ROLLBACK` when funds are insufficient).
   - *Integrity Violations:* A transaction may violate primary key, foreign key, or check constraints, forcing an abort.
   - *Deadlock Resolution:* The concurrency controller may select a transaction as a deadlock victim and abort it to break the cycle.
3. **Preserving Atomicity:** The ACID property of **Atomicity** requires that all changes of an aborted transaction be undone. The database must return to its pre-transaction state.
4. **Execution of Rollback:** The recovery manager reads undo log records, restores old data values in the buffer and disk, and releases locks. Without a recovery manager, aborted transactions would leave partial, corrupted updates in the database.

---

## T12.3 · Log-based recovery and shadow paging

### 2017 Q.6(d) · 03 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** Discuss shortly the log-based recovery approach to ensure atomicity despite of failures of DBMS.

**Answer.**

Log-based recovery ensures atomicity by recording every database update in an append-only log on stable storage before modifying the actual database on disk.

1. **Log Records:** The system writes structured records:
   - $\langle T_i\text{ start}\rangle$, $\langle T_i\text{ commit}\rangle$, and $\langle T_i\text{ abort}\rangle$ track transaction state.
   - Update records $\langle T_i, X, V_1, V_2\rangle$ store the transaction ID, data item $X$, old value $V_1$ (for undo), and new value $V_2$ (for redo).
2. **Write-Ahead Logging (WAL) Rule:**
   - The update log record must reach stable storage before the corresponding data item is written to disk.
   - All log records of a transaction must reach stable storage before the transaction commits.
3. **Ensuring Atomicity on Failure:**
   - If a transaction aborts or the system crashes while it is active (no commit record in log), the recovery manager executes $\text{undo}(T_i)$. It uses the old values $V_1$ to reverse all partial modifications.
   - If the transaction committed before the crash, $\text{redo}(T_i)$ applies new values $V_2$ to guarantee durability.
   - *Alternative:* Shadow paging ensures atomicity without logs by maintaining current and shadow page tables, but it causes disk fragmentation.

---

### 2023 Q.7(b) · 04 Marks

*Section B · Asked in: 2023 (CLO2) · L1 (asked once)*

**Question.** What is log based recovery? Illustrate with an example of a system crash and recovery process.

**Answer.**

#### Definition
**Log-based recovery** is a crash recovery technique that records all database update actions on stable storage in a sequential log prior to updating the database on disk. By maintaining both old and new values, the recovery manager can undo incomplete transactions and redo committed transactions after a failure.

#### System Crash Example
Consider three transactions running on data items $A$, $B$, and $C$ with initial values $A = 1000$, $B = 2000$, and $C = 500$:
- $T_1$ transfers \$100 from $A$ to $B$ (commits).
- $T_2$ adds \$200 to $C$ (commits).
- $T_3$ subtracts \$50 from $B$ (active during crash).

**State of Log on Stable Storage at Crash:**
```text
1. <T1 start>
2. <T1, A, 1000, 900>
3. <T1, B, 2000, 2100>
4. <T1 commit>
5. <T2 start>
6. <T2, C, 500, 700>
7. <T3 start>
8. <T2 commit>
9. <T3, B, 2100, 2050>
---- CRASH OCCURS HERE ----
```

#### Recovery Process
1. **Analysis:** The recovery manager scans the log to classify transactions:
   - **Redo-list** = $\{T_1, T_2\}$ (both contain `<start>` and `<commit>` records).
   - **Undo-list** = $\{T_3\}$ (contains `<start>` but no `<commit>` or `<abort>` record).
2. **Redo Phase:** Scans the log forward to re-apply updates for committed transactions:
   - Redo $T_1$: set $A \leftarrow 900$, $B \leftarrow 2100$.
   - Redo $T_2$: set $C \leftarrow 700$.
3. **Undo Phase:** Scans the log backward to rollback uncommitted transactions:
   - Undo $T_3$: restores $B$ to its old value $2100$ using record 9.
   - Writes $\langle T_3\text{ abort}\rangle$ to the log.

**Final Database State:**
$A = 900$, $B = 2100$, $C = 700$. Both atomicity for $T_3$ and durability for $T_1$ and $T_2$ are satisfied.

---

## T12.4 · RAID levels, comparison, and recovery role

### 2018 Q.5(c) · Part 2 RAID Recovery (2 of 4 Marks)

*Section B · Asked in: 2018 · Part 2 of 2 (2 marks for RAID recovery)*

**Question.** Discuss each type of failure that can happen in DBMS. How does RAID model help to recover a system?

*See also:* [[#2018 Q.5(c) · Part 1 Failures (2 of 4 Marks)]] for the first part.

**Answer.**

The RAID (Redundant Array of Independent Disks) model protects the database system from disk and media failures in three ways:

1. **Immediate Failover via Mirroring (RAID 1):** If a primary disk fails, the system instantly directs read and write requests to the mirror drive. The database continues running with zero downtime and zero data loss.
2. **On-the-Fly Parity Reconstruction (RAID 5 / RAID 6):** When a disk fails, the RAID controller reconstructs lost data blocks on the fly using a bitwise XOR of the surviving data and parity blocks.
3. **Online Rebuild with Hot Spares:** The controller copies reconstructed data onto a standby spare disk in the background. The repair completes without taking the database offline.

---

### 2018 Q.8(c) · 03 Marks

*Section B · Asked in: 2018 · L1 (asked once)*

**Question.** Describe the different RAID levels.

**Answer.**

![RAID levels showing disk cylinder configurations for (a) RAID 0, (b) RAID 1, (c) RAID 5, and (d) RAID 6](../Textbook/Chapter_12_Physical_Storage/diagrams/fig_12_04_raid_levels.jpg)
*Figure 12.4: RAID levels (Textbook Ch. 12, Figure 12.4)*

RAID organizes multiple physical disks to provide performance and fault tolerance. The primary levels are:

- **RAID 0 (Block Striping, No Redundancy):** Blocks are striped across multiple disks. It offers high read and write throughput, but any single drive failure causes complete data loss.
- **RAID 1 (Mirrored Disks):** Every disk has an identical duplicate disk. It provides 100% data redundancy and fast recovery, but requires double the storage capacity.
- **RAID 5 (Block-Interleaved Distributed Parity):** Data and parity blocks are distributed across all $N + 1$ disks. It survives any single disk failure with low storage overhead ($1 / (N+1)$).
- **RAID 6 (P + Q Redundancy):** Uses two independent error-correcting blocks (P and Q) across all disks. It tolerates up to two simultaneous disk failures.

*Summary of Other Levels:*
- **RAID 2:** Bit-level striping with Hamming error-correcting codes (obsolete).
- **RAID 3:** Byte-level striping with a single dedicated parity disk (obsolete).
- **RAID 4:** Block-level striping with a single dedicated parity disk (suffers from parity disk write bottlenecks).
- **RAID 1+0 (RAID 10):** Combines mirroring and striping to deliver high fault tolerance and fast I/O.

---

### 2023 Q.4(a) · 04 Marks

*Section A · Asked in: 2023 (CLO1) · L1 (asked once)*

**Question.** Discuss the features of RAID models.

**Answer.**

A Redundant Array of Independent Disks (RAID) provides four major architectural features:

1. **Data Striping (Performance Enhancement):** Data is segmented into blocks or bytes and distributed across multiple physical drives. This enables parallel disk I/O, which boosts transfer rates for large accesses and balances access loads.
2. **Data Redundancy (Fault Tolerance):** Redundancy is achieved through mirroring (duplicate blocks in RAID 1) or parity codes (XOR parity in RAID 5; Reed-Solomon P+Q codes in RAID 6). If a disk fails, data is restored without data loss.
3. **Storage Virtualization:** An array of physical drives appears to the operating system and DBMS as a single, large logical volume.
4. **Online Rebuild and Hot Swapping:** Failed drives can be replaced while the system remains powered on. The controller automatically rebuilds data onto hot-spare disks in the background.
5. **Background Data Scrubbing:** The controller continuously reads idle sectors to detect and repair latent sector corruption (bit rot) before additional drive failures occur.

---

### 2023 Q.7(c) · 03 Marks

*Section B · Asked in: 2023 (CLO2) · L1 (asked once)*

**Question.** Briefly describe the RAID model and its significance in database recovery.

**Answer.**

#### Description of RAID Model
The RAID (Redundant Array of Independent Disks) model combines multiple physical disk drives into a single logical unit. It uses data striping for parallel speed and data redundancy (mirroring or parity) for reliability.

#### Significance in Database Recovery
1. **Physical Realization of Stable Storage:** Standard database recovery algorithms (such as Write-Ahead Logging) assume the existence of **stable storage** that survives system crashes and media failures. RAID 1, 5, and 6 provide this physical foundation.
2. **Prevents Costly Offline Restores:** A single physical drive failure does not force the database offline. The system avoids hours of downtime spent restoring tape archives and replaying redo logs.
3. **High Availability During Rebuild:** Transactions continue processing queries normally while the controller reconstructs failed data blocks in the background.
4. **Guarantees Transaction Log Durability:** Database transaction logs are typically placed on RAID 1 volumes, ensuring sequential write speed and protection against log loss.

---

### 2024 Q.7(c) · 03 Marks

*Section B · Asked in: 2024 (CO3) · L1 (asked once)*

**Question.** A multimedia archive contains very large image and video files. RAID is recommended for storage. Compare different RAID levels.

**Answer.**

#### Workload Characteristics
Multimedia archives store multi-gigabyte image and video files. The workload consists of high-throughput sequential reads (streaming, downloading), rare updates (write-once, read-many), and very high total capacity demands.

#### Comparison of RAID Levels

| RAID Level | Striping Unit | Redundancy Mechanism | Fault Tolerance | Usable Storage Capacity | Read Speed (Large Files) | Write Speed |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **RAID 0** | Block | None | 0 disks | 100% | Very Fast | Very Fast |
| **RAID 1** | Block / Drive | Mirroring (copy) | 1 disk per pair | 50% | Fast | Moderate |
| **RAID 5** | Block | Distributed Parity | 1 disk | $\frac{N-1}{N}$ (High) | Very Fast | Fast for sequential |
| **RAID 6** | Block | Distributed P + Q | 2 disks | $\frac{N-2}{N}$ (High) | Very Fast | Moderate |
| **RAID 1+0** | Block | Mirroring + Striping | 1 disk per pair | 50% | Very Fast | Very Fast |

#### Recommendation and Justification
- **Recommended Level:** **RAID 6** (or **RAID 5** for smaller arrays).
- **Justification:** Multimedia archives require high storage efficiency and sequential read throughput, making parity schemes far more economical than mirroring (which wastes 50% capacity). Because archives use massive multi-terabyte drives, rebuild times can take days; RAID 6 tolerates a second drive failure during rebuild, protecting against catastrophic data loss.

---

[← Prev: T11 · Concurrency Control Protocols](T11_Concurrency_Control_Protocols.md) | [Explanation layer](../Topicwise_answers_explaination/T12_Recovery_System_and_RAID.md) | [Next: T13 · Security, Indexing & Hashing →](T13_Security_Indexing_and_Hashing.md)
