---
title: "T11 · Concurrency Control Protocols (Part 3 · Deadlock & Timestamp Ordering)"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T11
topic_id: T11
part: 3
exercise_count: 11
source_chapters:
  - "Chapter 18"
---

[← Prev: T11 Part 2](T11_Part2_2PL_and_Lock_Conversions.md) | [Index](00_Index.md) | [Next: T12 Part 1 →](T12_Part1_Failure_Types_and_RAID_Intro.md)

---

# T11 · Concurrency Control Protocols (Part 3 · Deadlock & Timestamp Ordering)

[← Prev: T11 Part 2](T11_Part2_2PL_and_Lock_Conversions.md) | [Exam-style T11](../Topicwise_answers_exam_style/T11_Concurrency_Control_Protocols.md) | [Next: T12 Part 1 →](T12_Part1_Failure_Types_and_RAID_Intro.md)

---

> [!info] Topic Overview & Scope
> This module provides complete, mathematically and technically rigorous solutions for the final segment of **Unit 6 (Concurrency Control Protocols)**. It addresses the practical and theoretical challenges of pessimistic locking—specifically **Strict 2PL**, **Deadlock Handling (Avoidance, Prevention, Detection, and Starvation)**—and transitions to optimistic and non-locking alternatives, centering on the **Timestamp-Ordering Protocol (TSO)**, its rollback invariants, cascading abort prevention via commit bits, expressive comparison with 2PL, and snapshot isolation mechanisms.

---

## Master Table of Assigned Exercises

| Exercise ID | Type | Silberschatz Section | Core Technical Concept | Exam Significance | Past Exam Direct Hits |
| :--- | :---: | :--- | :--- | :---: | :--- |
| **EX 18.17** | Regular | §18.1.1 (p. 840) | Benefits & disadvantages of Strict 2PL | High | Foundational theory |
| **EX 18.18** | Regular | §18.1.1 (p. 840) | Industrial dominance of Strict 2PL | High | Practical engine architecture |
| **EX 18.36** | Regular | §18.1.5 (p. 846) | Ordered locking with early unlock counterexample | Medium-High | Mathematical counterexample |
| **EX 18.20** | Regular | §18.2 (pp. 849–853) | Deadlock avoidance vs. detection cost trade-offs | Very High | ⚠️ **2018 Q.5(b) [3m]** |
| **EX 18.21** | Regular | §18.2.1 (pp. 850–851) | Starvation risks in deadlock avoidance | High | Viva & exam favorite |
| **PE 18.8** | Practice | §18.5 (pp. 861–863) | Equivalence of largest vs. most recent write timestamp | High | Invariant proof |
| **PE 18.12** | Practice | §18.5.1 (pp. 863–864) | Cascading aborts and livelock in TSO | Very High | Schedule trace & livelock |
| **EX 18.26** | Regular | §18.5.1 (p. 863) | Why rolled-back transactions receive a new timestamp | Critical | ⚠️ **2018 Q.6(b) [4m], 2024 Q.8(b) [3m]** |
| **EX 18.27** | Regular | §18.1, §18.5 | Incomparability proof: 2PL vs. Timestamp schedules | Very High | Class inclusion proof |
| **EX 18.28** | Regular | §18.5.1 (p. 863) | Commit bit for cascadelessness on reads vs. writes | High | Engine recovery design |
| **EX 18.30** | Regular | §18.9, §18.15 | Snapshot Isolation vs. Optimistic Concurrency Control | Medium-High | Modern MVCC engines |

---

## T11.3 · Strict and Rigorous Two-Phase Locking

### Exercise 18.17 · Benefits and Disadvantages of Strict Two-Phase Locking

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.17 (p. 902)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.3)
> - **Tested Concepts:** Strict 2PL protocol definition, strict schedules, cascading rollbacks, lock holding duration, concurrency trade-offs.

**Question (Silberschatz 7e Exercise 18.17).**
> What benefit does strict two-phase locking provide? What disadvantages result?

#### 1. Core Principles & Concept Overview
The basic Two-Phase Locking (2PL) protocol guarantees conflict serializability by constraining lock acquisitions and releases into two contiguous phases (growing and shrinking). However, basic 2PL does not restrict *when* locks are released during the shrinking phase. If a transaction $T_i$ releases an exclusive lock on data item $Q$ and subsequently aborts, another concurrent transaction $T_j$ that read the uncommitted modification made by $T_i$ must also be rolled back, causing **cascading rollbacks**.

To eliminate this vulnerability, database engines use **Strict Two-Phase Locking (Strict 2PL)**:
- **Protocol Rule:** In addition to adhering to standard two-phase locking rules, a transaction must hold **all its exclusive (X) locks until it terminates** (either commits or aborts). Shared (S) locks may be released during the shrinking phase.

```text
Basic 2PL:      [--- Growing Phase ---][Lock Point][--- Shrinking Phase (releasing X & S) ---> Commit]
Strict 2PL:     [--- Growing Phase ---][Lock Point][--- Shrinking Phase (releasing S only) ---> Commit (release all X locks)]
Rigorous 2PL:   [--- Growing Phase ------------------------------- Lock Point / Commit (release all X and S locks)]
```

#### 2. Detailed Step-by-Step Solution

##### Part A: Primary Benefits of Strict 2PL
1. **Ensures Strict Execution Schedules:**
   A schedule is defined as **strict** if for any two transactions $T_i$ and $T_j$, if a write operation of $T_i$ precedes a conflicting read or write operation of $T_j$, then the commit or abort operation of $T_i$ also precedes that conflicting read or write of $T_j$:
   $$
   w_i(Q) < o_j(Q) \implies c_i < o_j(Q) \quad \text{where } o_j \in \{r_j, w_j\}
   $$
   Because $T_i$ maintains exclusive ownership of $Q$ until commit time, no concurrent transaction $T_j$ can acquire an S-lock (to read) or an X-lock (to write) on $Q$ until $T_i$ has completely finished.
2. **Guarantees Cascadelessness (Freedom from Cascading Aborts):**
   Since no uncommitted data updates can be read by any other transaction, if transaction $T_i$ experiences a runtime error or deadlock rollback, it can be aborted in total isolation. No active concurrent transactions have observed its intermediate dirty writes; therefore, no cascading rollbacks occur.
3. **Drastically Simplifies Crash Recovery (Trivial Undo):**
   In a strict schedule, recovering an aborted transaction requires merely restoring the pre-transaction values (**before-images**) of the data items written by $T_i$. Because no other transaction could have overwritten $Q$ between $T_i$'s write and its abort, restoring the before-image does not accidentally overwrite the committed or uncommitted work of any other transaction.
4. **Preserves Conflict Serializability:**
   Strict 2PL inherits the mathematical serializability theorem of 2PL: all transactions can be serialized in the order of their lock points (which, for transactions holding all locks until completion, aligns directly with commit points).

##### Part B: Resulting Disadvantages
1. **Reduced Concurrency and Transaction Throughput:**
   Holding exclusive locks until transaction commit prolongs lock duration. A transaction that completes all updates to item $Q$ early in its execution cannot release the lock on $Q$ to allow waiting queries to proceed; the lock remains held through remaining disk I/O, network communication, and commit processing. This increases lock wait queues and reduces overall system throughput.
2. **Increased Transaction Latency and Blocking Overhead:**
   Concurrent transactions requiring access to frequently updated "hot spots" experience significant blocking delays, which elevates average transaction turnaround time.
3. **Does Not Prevent Deadlocks:**
   Strict 2PL does not eliminate the possibility of circular wait. Two transactions can easily acquire conflicting locks dynamically during their growing phases (e.g., $T_1$ holds an X-lock on $A$ and requests $B$; $T_2$ holds an X-lock on $B$ and requests $A$), resulting in a deadlock that requires detection and victim rollback.

| Feature / Property | Basic 2PL | Strict 2PL | Rigorous 2PL |
| :--- | :---: | :---: | :---: |
| **Conflict Serializability** | Guaranteed | Guaranteed | Guaranteed |
| **Cascadeless Schedules** | ❌ No (requires tracking) | ✅ Guaranteed | ✅ Guaranteed |
| **Strict Schedules** | ❌ No | ✅ Guaranteed | ✅ Guaranteed |
| **X-Locks Release Timing** | Shrinking phase | At `COMMIT` / `ABORT` | At `COMMIT` / `ABORT` |
| **S-Locks Release Timing** | Shrinking phase | Shrinking phase | At `COMMIT` / `ABORT` |
| **Deadlock Freedom** | ❌ No | ❌ No | ❌ No |
| **Concurrency Level** | High | Moderate | Low |

#### 3. RUET Exam Insights & Examiner Notes
- **Common Mistake:** Students often assert that Strict 2PL prevents deadlocks. Emphasize that Strict 2PL prevents **cascading rollbacks**, NOT deadlocks. Deadlocks are caused by the *acquisition order* of locks, whereas strictness governs the *release timing* of exclusive locks.
- **Mark Allocation Scheme (Exam Style):** In an RUET 4-mark question, allocate 2 marks for explaining the strictness/cascadelessness and recovery advantages, and 2 marks for detailing the concurrency bottleneck and persistence of deadlocks.

---

### Exercise 18.18 · Practical Popularity of Strict 2PL in Commercial DBMS

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.18 (p. 902)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.3)
> - **Tested Concepts:** Industrial concurrency control, ARIES/WAL recovery integration, lock management runtime overhead.

**Question (Silberschatz 7e Exercise 18.18).**
> Most implementations of database systems use strict two-phase locking. Suggest three reasons for the popularity of this protocol.

#### 1. Core Principles & Concept Overview
Virtually all classical relational database management systems that implement lock-based concurrency control—including IBM DB2, Microsoft SQL Server, and MySQL (InnoDB)—rely on Strict Two-Phase Locking (or its variant, Rigorous 2PL) rather than basic 2PL. The theoretical flexibility of basic 2PL is discarded in production environments in favor of the operational stability, predictability, and fault tolerance provided by Strict 2PL.

#### 2. Detailed Step-by-Step Solution

The three primary reasons for the ubiquitous adoption of Strict 2PL in commercial database engines are:

1. **Seamless Integration with Write-Ahead Logging (WAL) and Recovery Managers:**
   Commercial database engines rely on logging protocols (such as ARIES) to guarantee the Atomicity and Durability of transactions. In a non-strict schedule, if transaction $T_1$ writes $Q$, $T_2$ overwrites $Q$, and $T_1$ subsequently aborts, the recovery manager cannot simply restore the before-image of $Q$ without corrupting $T_2$'s write. Handling such non-strict aborts requires complex cascading compensation log records (CLRs) and mutual rollbacks. Strict 2PL ensures that no other transaction touches $Q$ until $T_1$ commits. Crash recovery and rollback are therefore **strictly local, deterministic, and trivial**: the before-image is simply written back.
2. **Elimination of Catastrophic Cascading Aborts:**
   In an enterprise production environment running hundreds of concurrent client connections, cascading aborts are unacceptable. If a long-running batch transaction aborts and cascades to hundreds of interactive client transactions, system availability collapses and client connections drop. Strict 2PL guarantees that transactions never read uncommitted data ($w_i(Q) < r_j(Q)$ requires $c_i < r_j(Q)$), ensuring **zero cascading rollbacks**. An abort is always localized to the single failing transaction.
3. **Simplified, Low-Overhead Lock Manager Implementation:**
   In basic 2PL, the DBMS runtime must dynamically track whether a transaction is currently in its growing phase or shrinking phase. In interactive applications where queries arrive sequentially from user applications, determining the exact "lock point" (the moment after which no further locks will ever be requested) is undecidable at runtime. If a transaction inadvertently releases a lock and later executes a query that needs a new lock, it violates 2PL. Strict 2PL eliminates this tracking complexity: **all locks are simply acquired as needed during execution, and all exclusive locks are released in a single batch operation at transaction commit or abort**.

```text
Production Lock Manager Architecture under Strict 2PL:
+-------------------------------------------------------------+
| Active Transaction Execution:                               |
|   Request Lock -> Granted or Queued -> Execute Data Access   |
|   (NO locks released during execution)                      |
+-------------------------------------------------------------+
                              |
                     [ COMMIT / ABORT ]
                              v
+-------------------------------------------------------------+
| End-of-Transaction (EOT) Clean-up:                          |
|   1. Flush Log Buffer to Disk (Write-Ahead Log)             |
|   2. Release ALL Held Exclusive Locks in Single Atomic Step  |
|   3. Awaken Waiting Transactions in Lock Queues             |
+-------------------------------------------------------------+
```

#### 3. RUET Exam Insights & Examiner Notes
- **Connection to Syllabus Unit 7 (Recovery):** RUET examiners reward answers that bridge Unit 6 (Concurrency) with Unit 7 (Recovery). Explicitly stating that Strict 2PL makes the ARIES recovery pass possible without cascading UNDO chains demonstrates a holistic understanding of database engine design.

---

### Exercise 18.36 · Ordered Locking with Unlocks Violating Serializability

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.36 (p. 904)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopics T11.3 & T11.4)
> - **Tested Concepts:** Non-2PL locking protocols, item ordering, precedence graph construction, conflict serializability counterexample.

**Question (Silberschatz 7e Exercise 18.36).**
> Consider the following locking protocol: All items are numbered, and once an item is unlocked, only higher-numbered items may be locked. Locks may be released at any time. Only X-locks are used. Show by an example that this protocol does not guarantee serializability.

#### 1. Core Principles & Concept Overview
Linear ordering of data items is a well-known technique to prevent **deadlocks** (by eliminating the circular wait condition). However, deadlock freedom is a *liveness* property, not a *safety* (serializability) property. 

The protocol proposed in this problem specifies:
1. Every data item has a unique integer identifier: $Q \in \{1, 2, \dots, n\}$.
2. Once a transaction unlocks an item $k$, it may only lock items $m$ such that $m > k$.
3. Locks may be released at any time, and only exclusive (X) locks are utilized.

Crucially, this protocol allows a transaction to release a lock on an item and subsequently acquire a lock on a higher-numbered item. Because the transaction acquires a lock *after* releasing a lock, it **violates the Two-Phase Locking condition**. Without the 2PL property, interleaved execution can create a cycle in the precedence graph, destroying serializability.

#### 2. Detailed Step-by-Step Solution

##### Step 1: System Definition & Item Numbering
Consider a database containing two data items, $A$ and $B$, assigned the following unique integer indices:
$$
\text{Item } A \implies 1, \quad \text{Item } B \implies 2
$$
Clearly, $\text{index}(A) < \text{index}(B)$.

##### Step 2: Transaction Definitions
Let two concurrent transactions, $T_1$ and $T_2$, both access and modify items $A$ and $B$:
- $T_1$: Updates item $A$, then updates item $B$.
- $T_2$: Updates item $A$, then updates item $B$.

##### Step 3: Construction of the Execution Schedule $S$
We interleave the locking, data access, and unlocking steps of $T_1$ and $T_2$ as follows:

| Time | Transaction | Operation Executed | Protocol Rule Verification |
| :--: | :--: | :-- | :-- |
| $t_1$ | $T_1$ | $\text{lock-X}(A)$ | Valid: $T_1$'s first lock (item 1). |
| $t_2$ | $T_1$ | $\text{write}(A)$ | Valid: $T_1$ holds exclusive lock on $A$. |
| $t_3$ | $T_1$ | $\text{unlock}(A)$ | Valid: Locks can be released at any time. Item unlocked: 1. |
| $t_4$ | $T_2$ | $\text{lock-X}(A)$ | Valid: Item 1 is now free; $T_2$'s first lock. |
| $t_5$ | $T_2$ | $\text{write}(A)$ | Valid: $T_2$ holds exclusive lock on $A$. |
| $t_6$ | $T_2$ | $\text{lock-X}(B)$ | Valid: $T_2$ has not unlocked anything yet; requests item 2. |
| $t_7$ | $T_2$ | $\text{write}(B)$ | Valid: $T_2$ holds exclusive lock on $B$. |
| $t_8$ | $T_2$ | $\text{unlock}(B)$ | Valid: Item unlocked: 2. |
| $t_9$ | $T_2$ | $\text{unlock}(A)$ | Valid: All locks released. |
| $t_{10}$ | $T_1$ | $\text{lock-X}(B)$ | **Protocol Check:** $T_1$ previously unlocked item 1 ($A$). It is now locking item 2 ($B$). Since $2 > 1$, **this lock request is strictly permitted!** |
| $t_{11}$ | $T_1$ | $\text{write}(B)$ | Valid: $T_1$ holds exclusive lock on $B$. |
| $t_{12}$ | $T_1$ | $\text{unlock}(B)$ | Valid: $T_1$ terminates. |

##### Step 4: Verification of Protocol Compliance
- **$T_1$ Compliance:** $T_1$ locked item 1, unlocked item 1, and subsequently locked item 2. Because $2 > 1$, $T_1$ obeyed the protocol rule that only higher-numbered items may be locked after an unlock.
- **$T_2$ Compliance:** $T_2$ locked item 1, locked item 2, and then unlocked items 2 and 1. It never acquired a lock after an unlock.
- **Lock Modes:** Only X-locks were utilized. Both transactions strictly adhered to the protocol.

##### Step 5: Conflict Dependency and Serializability Analysis
We extract all pairs of conflicting operations between $T_1$ and $T_2$:
1. **Conflict on Item $A$:**
   At time $t_2$, $T_1$ executes $\text{write}(A)$. At time $t_5$, $T_2$ executes $\text{write}(A)$.
   Because $T_1$'s write precedes $T_2$'s write, in any conflict-equivalent serial schedule, $T_1$ must precede $T_2$:
   $$
   T_1 \xrightarrow{A} T_2
   $$
2. **Conflict on Item $B$:**
   At time $t_7$, $T_2$ executes $\text{write}(B)$. At time $t_{11}$, $T_1$ executes $\text{write}(B)$.
   Because $T_2$'s write precedes $T_1$'s write, in any conflict-equivalent serial schedule, $T_2$ must precede $T_1$:
   $$
   T_2 \xrightarrow{B} T_1
   $$

The resulting precedence graph $G = (V, E)$ is:
```text
       ---- (write A) --->
 [T1]                      [T2]
       <--- (write B) ----
```
The precedence graph contains a directed cycle: $T_1 \to T_2 \to T_1$.

##### Conclusion
Because the precedence graph contains a directed cycle, schedule $S$ is **not conflict serializable**. Consequently, this ordered locking protocol does not guarantee serializability.

#### 3. RUET Exam Insights & Examiner Notes
- **Why Did Ordered Locking Fail Here?** In the classical Tree Protocol (or DAG protocol), transactions can only lock a child node if they *currently hold a lock on its parent*. In this problem, $T_1$ dropped its lock on $A$ *before* locking $B$. That early release allowed $T_2$ to slip in between, write both $A$ and $B$, and create the backward conflict edge $T_2 \xrightarrow{B} T_1$.
- **Exam Strategy:** When asked to prove a protocol does not guarantee serializability, always construct a minimal 2-item ($A=1, B=2$), 2-transaction counterexample and draw the 2-node cycle graph clearly.

---

## T11.4 · Deadlock Handling (Prevention, Detection & Wait-For Graphs)

### Exercise 18.20 · Deadlock Avoidance vs. Deadlock Detection Cost Trade-offs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.20 (p. 902)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.4)
> - **Tested Concepts:** Deadlock avoidance, deadlock detection, wait-for graph, cycle detection, rollback cost, system overhead.
> - ⚠️ **Direct RUET Exam Hit:** Recycled verbatim in **2018 Q.5(b)** (4 marks).

**Question (Silberschatz 7e Exercise 18.20).**
> Under what conditions is it less expensive to avoid deadlock than to allow deadlocks to occur and then to detect them?

#### 1. Core Principles & Concept Overview
Database systems handle deadlocks via two opposing philosophical approaches:
1. **Deadlock Prevention / Avoidance:** The system restricts how transactions acquire locks or pre-empts transactions proactively (e.g., using conservative 2PL, total ordering of data items, or timestamp-based preemption like Wait-Die and Wound-Wait) so that a circular wait state is structurally impossible.
2. **Deadlock Detection and Recovery:** The system allows transactions to acquire locks freely. A background monitor periodically constructs a **wait-for graph** $G = (V, E)$ and runs cycle-detection algorithms (e.g., Tarjan's or Kosaraju's DFS). If a cycle is detected, the DBMS selects a victim transaction, aborts it, and reclaims its locks to break the deadlock.

Choosing between avoidance and detection is an optimization problem balancing monitoring overhead, false-positive aborts, lock contention, and the cost of transaction rollback.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Formal Cost Models
We can express the runtime cost of each strategy mathematically:
- **Cost of Detection Strategy:**
  $$
  \text{Cost}_{\text{detect}} = C_{\text{graph\_maint}} + C_{\text{cycle\_search}} + P_{\text{deadlock}} \times (C_{\text{victim\_select}} + C_{\text{rollback}} + C_{\text{restart}})
  $$
  Where $P_{\text{deadlock}}$ is the probability of a deadlock occurring, and $C_{\text{rollback}}$ is the lost work of the victim.
- **Cost of Avoidance / Prevention Strategy:**
  $$
  \text{Cost}_{\text{avoid}} = C_{\text{protocol\_overhead}} + P_{\text{false\_abort}} \times (C_{\text{rollback\_early}} + C_{\text{restart}}) + C_{\text{concurrency\_loss}}
  $$
  Where $P_{\text{false\_abort}}$ is the probability of killing a transaction that might never have actually entered a deadlock.

##### Step 2: Conditions Where Avoidance is Less Expensive Than Detection
Deadlock avoidance/prevention is cheaper than detection and recovery when the following operational conditions hold:

1. **High Lock Contention / High Conflict Probability ($P_{\text{deadlock}} \gg 0$):**
   When hundreds of concurrent transactions frequently contend for the same small set of "hot" data items, deadlocks occur frequently. Under detection, the wait-for graph will constantly contain cycles, triggering frequent, expensive rollbacks. Avoidance protocols (such as lock ordering or wound-wait) prevent these circular deadlocks systematically.
2. **Presence of Long-Running or Computationally Expensive Transactions:**
   If transactions perform heavy calculations, complex aggregations, or extensive disk modifications, aborting a transaction after it has run for minutes wastes vast CPU, memory, and I/O resources ($C_{\text{rollback}} \text{ is very large}$). Deadlock detection will often pick a long transaction as a victim or abort it near its completion. Avoidance schemes prevent such deep rollbacks (e.g., Wound-Wait gives priority to older transactions, ensuring they are never aborted by younger ones).
3. **High Overhead of Global Cycle Detection (Distributed Environments):**
   In distributed database systems (such as across clusters or cloud partitions), maintaining a global wait-for graph requires passing lock state messages across network nodes (using distributed edge-chasing algorithms). The communication latency and network overhead ($C_{\text{graph\_maint}}$) are severe. Local timestamp-based avoidance protocols (e.g., Wait-Die) require zero inter-node cycle detection messages.
4. **Transactions with Predictable / Statically Known Lock Requirements:**
   If transactions know their required data items before execution starts (as in pre-compiled stored procedures or batch jobs), the DBMS can enforce **strict item ordering** or acquire all locks atomically at the start (conservative 2PL). Here, avoidance incurs **zero runtime rollback cost and zero graph monitoring cost**, making it vastly superior to detection.

```text
Summary Cost Trade-off Matrix:
+-------------------------------+----------------------------------+----------------------------------+
| Workload / System Attribute   | Deadlock Avoidance is Cheaper    | Deadlock Detection is Cheaper    |
+-------------------------------+----------------------------------+----------------------------------+
| Lock Contention               | High (many overlapping writes)   | Low (mostly disjoint items)      |
| Transaction Duration          | Long-running, resource-intensive | Short OLTP, quick operations     |
| System Topology               | Distributed / multi-node clusters| Single-node, shared memory       |
| Lock Request Pattern          | Known a priori / orderable       | Unpredictable / ad-hoc dynamic   |
| Primary Penalty               | Concurrency throttle / false abort| Wasted work of rolled-back victim|
+-------------------------------+----------------------------------+----------------------------------+
```

##### Step 3: When Detection is Cheaper (Contrasting Case)
Conversely, in standard, short OLTP workloads with low contention, deadlocks are rare ($P_{\text{deadlock}} \approx 0$). Imposing avoidance restrictions unnecessarily reduces concurrency or aborts viable transactions (as in Wait-Die). In such systems, letting transactions run unhindered and checking for deadlocks only periodically (e.g., every 500 ms) is significantly less expensive.

#### 3. RUET Exam Insights & Examiner Notes
- **Past Exam Recycled Pattern:** This exact question appeared in **2018 Q.5(b)**: *"What do you know about deadlock in transaction management? Under what conditions it is less expensive to avoid deadlock than to allow deadlocks to occur and then to detect them?"*
- **Examiner's Grading Breakdown:**
  - 1 mark: Concise definition of deadlock in transaction management (circular wait on locks).
  - 3 marks: Clear statement of the conditions where avoidance wins (High contention, long/expensive transactions, high cycle-detection overhead/distributed nodes).

---

### Exercise 18.21 · Starvation Possibility in Deadlock Avoidance Schemes

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.21 (p. 902)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.4)
> - **Tested Concepts:** Deadlock avoidance, starvation (livelock), Wait-Die vs. Wound-Wait, timeout schemes, anti-starvation mechanisms.

**Question (Silberschatz 7e Exercise 18.21).**
> If deadlock is avoided by deadlock-avoidance schemes, is starvation still possible? Explain your answer.

#### 1. Core Principles & Concept Overview
**Deadlock** and **Starvation** are fundamentally distinct concurrency failures:
- **Deadlock:** A state where two or more transactions are in a mutual circular wait, making forward progress impossible for any transaction in the set without external intervention.
- **Starvation (Livelock):** A state where a transaction is not deadlocked, but is repeatedly denied the resources it needs to complete, waiting indefinitely while other concurrent transactions continue to execute and commit.

Deadlock avoidance schemes guarantee that the system will never enter a state of circular wait. However, breaking circular wait does **not** automatically ensure fairness or guarantee that every transaction will complete within a finite time.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Core Answer Assertion
**YES, starvation is still completely possible under many deadlock-avoidance schemes**, unless explicit, dedicated anti-starvation mechanisms are integrated into the protocol.

##### Step 2: Proof by Analysis of Deadlock-Avoidance Mechanisms

1. **Timeout-Based Deadlock Avoidance:**
   - *Protocol:* A transaction that requests a lock is allowed to wait, but only for a fixed duration $T_{\text{timeout}}$. If the lock is not granted within that window, the DBMS assumes a deadlock may exist, aborts the transaction, and restarts it.
   - *Starvation Mechanism:* In a heavily loaded system with continuous lock contention, an unlucky transaction may repeatedly request a contentious lock, time out, abort, restart, and time out again. Meanwhile, other newly arriving transactions successfully acquire the lock during intervals when the unlucky transaction is backing off. The victim transaction experiences **indefinite starvation**.
2. **Wait-Die Scheme (Vulnerable to Starvation without Timestamp Preservation):**
   - *Protocol:* If transaction $T_i$ requests a data item held by $T_j$:
     - If $\text{TS}(T_i) < \text{TS}(T_j)$ ($T_i$ is older): $T_i$ is allowed to wait.
     - If $\text{TS}(T_i) > \text{TS}(T_j)$ ($T_i$ is younger): $T_i$ dies (aborts and restarts).
   - *Starvation Mechanism:* If the system assigns a **new timestamp** to $T_i$ upon restart, $T_i$ will remain permanently younger than active transactions. Every time it requests a lock held by an older transaction, it will be killed again, resulting in an infinite abort loop.
   - *Mitigation:* The Wait-Die scheme avoids starvation *only* if the aborted transaction **retains its original timestamp upon restart**. With each restart, older transactions commit and leave the system, causing $T_i$ to steadily become the oldest transaction, after which it will never be killed.
3. **Pre-declaration / Conservative 2PL (Locking All Items Upfront):**
   - *Protocol:* A transaction must declare and acquire all locks it will ever need in a single atomic operation before beginning execution. If any single lock cannot be granted, it acquires none and waits.
   - *Starvation Mechanism:* Suppose transaction $T$ needs items $\{A, B, C\}$. While $A$ is free, item $B$ is held by $T_1$. Once $T_1$ releases $B$, another transaction $T_2$ has already acquired $A$. Transaction $T$ can be starved indefinitely waiting for all requested items to be simultaneously free, even though no deadlock ever forms!
4. **Ordering of Data Items (Graph / Hierarchy):**
   - *Protocol:* Data items are ordered $1, \dots, n$, and transactions must lock items in monotonically increasing order.
   - *Starvation Mechanism:* Deadlocks are impossible because no circular wait can form. However, if the lock manager does not maintain a strict **First-In, First-Out (FIFO)** grant queue for each individual item, a transaction waiting for item $k$ can be bypassed repeatedly by newly arriving high-priority transactions, causing starvation.

##### Step 3: Architectural Remedies Against Starvation
To ensure a deadlock-avoidance scheme is also starvation-free, the DBMS must implement:
1. **Timestamp Preservation / Aging:** Transactions must keep their original birth timestamps across rollbacks, monotonically advancing their priority over time.
2. **FIFO Lock Queues:** A lock is granted strictly in arrival order; no newly arriving transaction can jump ahead of a waiting transaction, even in shared (S) mode.
3. **Randomized Exponential Backoff:** When a transaction aborts due to a timeout or wait-die condition, it waits a randomized, expanding time interval before retrying, preventing resonance lock-step starvation.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner's Catch:** This is a classic oral exam (viva) and theory question. Students frequently confuse deadlock with starvation and incorrectly assume that eliminating deadlocks solves all concurrency problems.
- **Key Phrase to Include:** State clearly that *"Deadlock avoidance guarantees the absence of circular wait, but does not guarantee fairness or liveness. Without aging or FIFO queues, starvation easily occurs."*

---

## T11.6 · Timestamp-Based Protocols & Advanced Concurrency Control

### Practice Exercise 18.8 · Largest vs. Most Recent Write Timestamp Equivalence

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Practice Exercise 18.8 (p. 900)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.6)
> - **Tested Concepts:** Timestamp-Ordering protocol, $W\text{-}TS(Q)$ semantic definition, monotonic timestamp invariants.

**Question (Silberschatz 7e Practice Exercise 18.8).**
> In timestamp ordering, $\text{W-timestamp}(Q)$ denotes the largest timestamp of any transaction that executed $\text{write}(Q)$ successfully. Suppose that, instead, we defined it to be the timestamp of the most recent transaction to execute $\text{write}(Q)$ successfully. Would this change in wording make any difference? Explain your answer.

#### 1. Core Principles & Concept Overview
In the standard Timestamp-Ordering (TSO) protocol, two timestamps are maintained for each data item $Q$:
- $\text{W-timestamp}(Q)$: The largest timestamp of any transaction that executed $\text{write}(Q)$ successfully.
- $\text{R-timestamp}(Q)$: The largest timestamp of any transaction that executed $\text{read}(Q)$ successfully.

The question asks whether replacing the mathematical term *"largest timestamp"* with the chronological term *"timestamp of the most recent transaction to execute write(Q) successfully"* alters the operational behavior or correctness of the protocol.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Core Assertion
**NO, this change in wording makes ABSOLUTELY NO DIFFERENCE.** Under the rules of the Timestamp-Ordering protocol, the two definitions are mathematically and operationally identical.

##### Step 2: Proof of Invariant Equivalence
Let us trace the rules governing a $\text{write}(Q)$ request issued by an arbitrary transaction $T_i$ with timestamp $\text{TS}(T_i)$ at physical wall-clock time $t$:

1. **Protocol Check 1 (Read Conflict):**
   If $\text{TS}(T_i) < \text{R-timestamp}(Q)$, the value produced by $T_i$ was needed previously by a younger transaction that has already read an older version. The write is rejected, and $T_i$ is rolled back.
2. **Protocol Check 2 (Write Conflict):**
   If $\text{TS}(T_i) < \text{W-timestamp}(Q)$, $T_i$ is attempting to write an obsolete value of $Q$ that has already been overwritten by a younger transaction with a larger timestamp. The write is rejected, and $T_i$ is rolled back.
3. **Execution Condition:**
   The write operation is allowed to execute successfully **if and only if**:
   $$
   \text{TS}(T_i) \ge \text{R-timestamp}(Q) \quad \text{and} \quad \text{TS}(T_i) \ge \text{W-timestamp}(Q)
   $$
4. **State Update:**
   When the write executes successfully, the system updates the write timestamp:
   $$
   \text{W-timestamp}(Q) \leftarrow \text{TS}(T_i)
   $$

##### Step 3: Analysis of the Chronological Sequence
Because any write request with $\text{TS}(T_i) < \text{W-timestamp}(Q)$ is **strictly rejected and aborted**, it is impossible for a transaction with a smaller timestamp to successfully write to $Q$ after a transaction with a larger timestamp has already written to $Q$.

Therefore, if we observe the sequence of transactions that successfully execute $\text{write}(Q)$ in chronological (real physical) time:
$$
T_{(1)}, T_{(2)}, T_{(3)}, \dots, T_{(k)}
$$
Their assigned logical timestamps must form a **monotonically non-decreasing sequence**:
$$
\text{TS}(T_{(1)}) \le \text{TS}(T_{(2)}) \le \text{TS}(T_{(3)}) \le \dots \le \text{TS}(T_{(k)})
$$

Consequently:
- The transaction that executed $\text{write}(Q)$ *most recently* in physical time is $T_{(k)}$.
- Its timestamp, $\text{TS}(T_{(k)})$, is automatically the *largest* timestamp among all transactions that have ever successfully written $Q$.

##### Step 4: Consideration of Thomas' Write Rule
Even if Thomas' Write Rule is incorporated (where a write with $\text{TS}(T_i) < \text{W-timestamp}(Q)$ is ignored rather than aborted):
- The obsolete write is discarded and **not executed**.
- The existing $\text{W-timestamp}(Q)$ is maintained without alteration.
Thus, the most recent transaction to *successfully execute* (update) the write remains the one with the largest timestamp.

##### Conclusion
The phrase *"the timestamp of the most recent transaction to execute write(Q) successfully"* describes the physical manifestation of the exact same value designated by *"the largest timestamp of any transaction that executed write(Q) successfully"*. The wording change has zero impact.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner's Objective:** This exercise tests whether students truly understand the rollback mechanism of TSO. The fact that writes with smaller timestamps are aborted guarantees that timestamps of successful writes can never decrease over physical time.

---

### Practice Exercise 18.12 · Cascading Aborts and Livelock (Starvation) in Timestamp Ordering

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Practice Exercise 18.12 (pp. 900–901)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.6)
> - **Tested Concepts:** Timestamp Ordering, cascading aborts, livelock, schedule tracing, dirty read vulnerability.

**Question (Silberschatz 7e Practice Exercise 18.12).**
> Consider the timestamp-ordering protocol, and two transactions, one that writes two data items $p$ and $q$, and another that reads the same two data items. Give a schedule whereby the timestamp test for a write operation fails and causes the first transaction to be restarted, in turn causing a cascading abort of the other transaction. Show how this could result in starvation of both transactions. (Such a situation, where two or more processes carry out actions, but are unable to complete their task because of interaction with the other processes, is called a **livelock**.)

#### 1. Core Principles & Concept Overview
Standard Timestamp Ordering guarantees conflict serializability and freedom from deadlock, but it **does not guarantee cascadelessness or recoverability**. If transaction $T_1$ writes an item $p$ and transaction $T_2$ reads that updated value before $T_1$ commits, a subsequent rollback of $T_1$ forces $T_2$ to be rolled back as well (**cascading abort**).

Furthermore, if the two transactions continuously restart with new timestamps and interleave their operations in the same relative sequence, they can repeatedly abort each other. Neither transaction is blocked (it is not a deadlock), but neither can ever commit. This is a **livelock** (mutual starvation).

#### 2. Detailed Step-by-Step Solution

##### Step 1: Initial Setup
- Transactions:
  - $T_1$: Writes data items $p$ and $q$.
  - $T_2$: Reads data items $p$ and $q$.
- Initial logical timestamps:
  $$
  \text{TS}(T_1) = 100, \quad \text{TS}(T_2) = 200 \quad (T_1 \text{ is older, } T_2 \text{ is younger})
  $$
- Initial data item timestamps:
  $$
  \text{R-TS}(p) = 0, \quad \text{W-TS}(p) = 0, \quad \text{R-TS}(q) = 0, \quad \text{W-TS}(q) = 0
  $$

##### Step 2: Step-by-Step Schedule Execution Causing Cascading Abort

| Step | Tx | Operation | Protocol Condition Evaluated | Protocol Action & State Update |
| :--: | :--: | :-- | :-- | :-- |
| 1 | $T_1$ | $\text{write}(p)$ | $\text{TS}(T_1) \ge \text{R-TS}(p) \; (100 \ge 0)$<br>$\text{TS}(T_1) \ge \text{W-TS}(p) \; (100 \ge 0)$ | **Granted.**<br>$\text{W-TS}(p) := 100$. |
| 2 | $T_2$ | $\text{read}(p)$ | $\text{TS}(T_2) \ge \text{W-TS}(p) \; (200 \ge 100)$ | **Granted.**<br>$\text{R-TS}(p) := \max(0, 200) = 200$.<br>*(Note: $T_2$ has now read uncommitted data written by $T_1$!)* |
| 3 | $T_2$ | $\text{read}(q)$ | $\text{TS}(T_2) \ge \text{W-TS}(q) \; (200 \ge 0)$ | **Granted.**<br>$\text{R-TS}(q) := \max(0, 200) = 200$. |
| 4 | $T_1$ | $\text{write}(q)$ | **Check:** $\text{TS}(T_1) < \text{R-TS}(q)$?<br>Here $\text{TS}(T_1) = 100$, but $\text{R-TS}(q) = 200$.<br>Condition $100 < 200$ is **TRUE**! | **VIOLATION! Write rejected.**<br>A younger transaction ($T_2$) has already read $q$ assuming $T_1$'s write would not happen.<br>**$T_1$ is ABORTED and ROLLED BACK.** |
| 5 | System | Cascading Abort | $T_2$ executed $\text{read}(p)$ in Step 2, observing the uncommitted write of $T_1$. | Since $T_1$ aborted, $T_2$'s read was dirty.<br>**$T_2$ MUST BE CASCADED AND ROLLED BACK.** |

##### Step 3: Emergence of Livelock and Starvation
Now observe what happens when both transactions restart:
1. Upon rollback, under standard TSO rules (to prevent immediate re-abort), both transactions are assigned **new timestamps**:
   $$
   \text{TS}(T_1') = 300, \quad \text{TS}(T_2') = 400
   $$
2. If the operating system or database thread scheduler dispatches them with the same relative timing:
   - At time $t_1$: $T_1'$ writes $p \implies \text{W-TS}(p) := 300$.
   - At time $t_2$: $T_2'$ reads $p \implies \text{R-TS}(p) := 400$.
   - At time $t_3$: $T_2'$ reads $q \implies \text{R-TS}(q) := 400$.
   - At time $t_4$: $T_1'$ tries to write $q$. Since $\text{TS}(T_1') = 300 < \text{R-TS}(q) = 400$, **$T_1'$ is aborted again!**
   - At time $t_5$: $T_2'$ is dragged down in another **cascading abort!**
3. Both transactions are assigned fresh timestamps ($\text{TS}(T_1'') = 500, \text{TS}(T_2'') = 600$), and the cycle repeats ad infinitum.

##### Conclusion
Both transactions are actively executing instructions and consuming system CPU cycles, but neither can ever commit. This represents a classic **livelock resulting in mutual starvation**.

```text
The Livelock / Cascading Abort Cycle:
  T1 writes p ---> T2 reads p ---> T2 reads q ---> T1 writes q fails (R-TS(q) > TS(T1))
       ^                                                    |
       |                                                    v
       |                                           T1 Aborts & Rolls Back
       |                                                    |
       |                                                    v
       |                                           T2 Cascaded Abort!
       |                                                    |
       +----- Restart Both with Fresh Timestamps <----------+
```

#### 3. RUET Exam Insights & Examiner Notes
- **Direct Connection to Lecture Slides:** In Lecture Deck 08 (Slide 28), the instructor explicitly notes: *"The timestamp-ordering protocol does not guarantee freedom from cascading rollbacks."* Drawing this 5-step trace table provides definitive proof.
- **Remedy Question:** Examiners often follow up with: *"How can this livelock be prevented?"* Answer: (1) Introduce a **commit bit** on data items to buffer reads (Exercise 18.28), or (2) Apply **randomized exponential backoff delays** before restarting aborted transactions.

---

### Exercise 18.26 · Why Rolled-Back Transactions Receive a New Timestamp

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.26 (p. 903)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.6)
> - **Tested Concepts:** Timestamp Ordering, transaction restart rules, starvation prevention, serialization ordering.
> - ⚠️ **Direct RUET Exam Hit:** Recycled verbatim in **2018 Q.6(b)** (4 marks) and **2024 Q.8(b)** (3 marks).

**Question (Silberschatz 7e Exercise 18.26).**
> When a transaction is rolled-back under timestamp ordering, it is assigned a new timestamp. Why can it not simply keep its old timestamp?

#### 1. Core Principles & Concept Overview
In timestamp-based concurrency control, a transaction's timestamp $\text{TS}(T_i)$ is not merely an identifier; it defines the transaction's **exact logical position in the equivalent serial order**. If $T_i$ has a smaller timestamp than $T_j$, the system is mathematically committed to executing an execution schedule equivalent to a serial schedule where $T_i$ runs before $T_j$.

When an operation of $T_i$ violates this ordering, the DBMS rolls $T_i$ back. Understanding why $T_i$ must receive a **new, larger timestamp** upon restart requires analyzing what happens to data item timestamps when conflicting transactions execute.

#### 2. Detailed Step-by-Step Solution

##### Part 1: Conditions Causing Rollback Under Timestamp Ordering
Under the standard TSO protocol, a transaction $T_i$ is rolled back whenever it attempts an operation that arrives "too late":
1. **On Read Request $\text{read}(Q)$:**
   $$
   \text{TS}(T_i) < \text{W-timestamp}(Q)
   $$
   *Reason:* A younger transaction with a larger timestamp has already overwritten $Q$. $T_i$ needed to read the older value, which is no longer available. The read is rejected, and $T_i$ rolls back.
2. **On Write Request $\text{write}(Q)$:**
   $$
   \text{TS}(T_i) < \text{R-timestamp}(Q)
   $$
   *Reason:* A younger transaction has already read the current value of $Q$ under the assumption that $T_i$'s write had already occurred earlier. Allowing $T_i$ to write now would invalidate the data already consumed by the younger transaction. The write is rejected, and $T_i$ rolls back.
3. **On Write Request $\text{write}(Q)$ (Without Thomas' Write Rule):**
   $$
   \text{TS}(T_i) < \text{W-timestamp}(Q)
   $$
   *Reason:* $T_i$ is attempting to write an obsolete value over an update already committed by a younger transaction.

##### Part 2: Why the Transaction Cannot Keep Its Old Timestamp
If the system permitted $T_i$ to retain its original, old timestamp $\text{TS}(T_i)$ upon restart, the following catastrophic failures occur:

1. **Guaranteed Immediate Re-Abort (Persistent Protocol Failure):**
   The data item timestamps $\text{R-timestamp}(Q)$ and $\text{W-timestamp}(Q)$ are recorded directly in the database and **never decrease**. They reflect the timestamps of younger transactions that successfully executed.
   If $T_i$ restarts with its old timestamp, then when it re-executes and reaches the exact same operation, its timestamp will still be smaller than the item's timestamps:
   $$
   \text{TS}(T_i) < \text{R-timestamp}(Q) \quad \text{or} \quad \text{TS}(T_i) < \text{W-timestamp}(Q)
   $$
   The exact same protocol test will fail again immediately. $T_i$ will be aborted at the exact same point on every single restart!
2. **Permanent Starvation (Livelock):**
   Because the data items' timestamps only remain constant or advance to even higher values as other transactions execute, an old timestamp becomes increasingly obsolete. Keeping the old timestamp traps the transaction in an **infinite abort-restart loop**, guaranteeing starvation.
3. **Restoring a Feasible Serialization Position:**
   The old timestamp represents a logical time slot in the serialization history that has already been invalidated by concurrent operations. To execute successfully, the restarted transaction must be repositioned in logical time **after** the conflicting transactions. Assigning a **new, larger timestamp** (from the current system clock or monotonic counter) places $T_i$ at the end of the serialization schedule, where its operations can successfully execute without conflicting with past operations.

##### Part 3: Critical Examination Comparison (TSO vs. Deadlock Prevention)
RUET examiners frequently test whether students confuse Timestamp Ordering with Deadlock Prevention:

| Protocol Mechanism | Protocol Type | Rolled-Back Transaction Timestamp | Technical Justification |
| :--- | :---: | :---: | :--- |
| **Wait-Die / Wound-Wait** | Lock-Based (Deadlock Prevention) | **KEEPS OLD Timestamp** | In locking, timestamps act as a **priority queue**. Keeping the old timestamp ensures the transaction steadily ages into the "oldest" transaction, guaranteeing it will never be aborted again and preventing starvation. |
| **Timestamp Ordering (TSO)** | Non-Locking (Serialization) | **RECEIVES NEW Timestamp** | In TSO, timestamps define the **serial order**. An old timestamp is obsolete and will repeatedly fail against advanced data item timestamps. A new timestamp moves the transaction to the present, enabling it to succeed. |

#### 3. RUET Exam Insights & Examiner Notes
- **Direct Hits in RUET Finals:**
  - **2018 Q.6(b) [4 marks]:** *"When a transaction is rolled back under timestamp ordering and it is assigned a new timestamp? Why can it not simply keep its old timestamp?"*
  - **2024 Q.8(b) [3 marks]:** Same question verbatim.
- **Examiner's Checklist for Full Marks:**
  1. Clearly state the exact conditions for read rollback ($\text{TS} < \text{W-TS}$) and write rollback ($\text{TS} < \text{R-TS}$).
  2. State that item timestamps never decrease.
  3. Explain that keeping the old timestamp guarantees an immediate re-abort and permanent livelock.
  4. Explicitly highlight the contrast with the Wait-Die deadlock prevention protocol.

---

### Exercise 18.27 · Expressive Incomparability: 2PL Schedules vs. Timestamp Ordering Schedules

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.27 (p. 903)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopics T11.2 & T11.6)
> - **Tested Concepts:** Schedule class inclusion, Two-Phase Locking vs. Timestamp Ordering, expressive incomparability.

**Question (Silberschatz 7e Exercise 18.27).**
> Show that there are schedules that are possible under the two-phase locking protocol but not possible under the timestamp protocol, and vice versa.

#### 1. Core Principles & Concept Overview
Both the Two-Phase Locking (2PL) protocol and the Timestamp-Ordering (TSO) protocol guarantee conflict serializability. However, they enforce serializability through fundamentally different mechanisms:
- **2PL:** Serialization order is determined dynamically at runtime by the relative order of the transactions' **lock points** (the moment the final lock is acquired).
- **TSO:** Serialization order is determined strictly a priori by the predetermined **timestamps** assigned at transaction startup.

Because their constraints are orthogonal, neither protocol is a subset of the other:
$$
\text{Class}(2\text{PL}) \setminus \text{Class}(\text{TSO}) \neq \emptyset \quad \text{and} \quad \text{Class}(\text{TSO}) \setminus \text{Class}(2\text{PL}) \neq \emptyset
$$

#### 2. Detailed Step-by-Step Solution

##### Part A: Schedule Possible Under 2PL, but NOT Possible Under TSO

###### Step 1: Schedule Construction
Consider two transactions $T_1$ and $T_2$ accessing a shared data item $A$.
Let their start timestamps in TSO be:
$$
\text{TS}(T_1) = 100, \quad \text{TS}(T_2) = 200 \quad (T_1 \text{ started before } T_2)
$$

Consider the following schedule $S_1$:
$$
S_1 = r_2(A), \; w_2(A), \; c_2, \; r_1(A), \; w_1(A), \; c_1
$$
In words: $T_2$ executes its read and write on $A$ and commits; subsequently, $T_1$ executes its read and write on $A$ and commits.

###### Step 2: Evaluation Under 2PL
1. $T_2$ acquires $\text{lock-X}(A)$, reads $A$, writes $A$, reaches its lock point, and releases $\text{lock-X}(A)$ upon commit.
2. $T_1$ then acquires $\text{lock-X}(A)$, reads $A$, writes $A$, reaches its lock point, and releases $\text{lock-X}(A)$ upon commit.
3. Both transactions strictly observe two-phase locking (growing phase followed by shrinking phase).
4. The lock point of $T_2$ precedes the lock point of $T_1$. The schedule is conflict-equivalent to the serial schedule $\langle T_2, T_1 \rangle$.
5. **Result:** Schedule $S_1$ is **valid and completely permitted under 2PL**.

###### Step 3: Evaluation Under TSO
1. Initial state: $\text{R-TS}(A) = 0, \text{W-TS}(A) = 0$.
2. When $T_2$ writes $A$, because $\text{TS}(T_2) = 200 \ge 0$, the write succeeds, setting:
   $$
   \text{W-TS}(A) \leftarrow 200
   $$
3. Next, $T_1$ attempts to execute $r_1(A)$.
4. The TSO protocol checks: Is $\text{TS}(T_1) < \text{W-TS}(A)$?
   $$
   \text{TS}(T_1) = 100 < \text{W-TS}(A) = 200 \implies \textbf{TRUE!}
   $$
5. $T_1$'s read request is rejected, and **$T_1$ is aborted and rolled back**.
6. **Result:** Schedule $S_1$ is **impossible under TSO**.

---

##### Part B: Schedule Possible Under TSO, but NOT Possible Under 2PL

###### Step 1: Schedule Construction
Consider two transactions $T_1$ and $T_2$ accessing two data items $A$ and $B$.
Let their timestamps be:
$$
\text{TS}(T_1) = 100, \quad \text{TS}(T_2) = 200
$$

Consider the following interleaved schedule $S_2$:
$$
S_2 = r_1(A), \; w_2(A), \; r_1(B), \; w_2(B)
$$

###### Step 2: Evaluation Under TSO
Let initial timestamps for $A$ and $B$ be 0:
1. $r_1(A)$: $\text{TS}(T_1) = 100 \ge \text{W-TS}(A) = 0 \implies$ Granted. $\text{R-TS}(A) := 100$.
2. $w_2(A)$: $\text{TS}(T_2) = 200 \ge \text{R-TS}(A) = 100$ and $\ge \text{W-TS}(A) = 0 \implies$ Granted. $\text{W-TS}(A) := 200$.
3. $r_1(B)$: $\text{TS}(T_1) = 100 \ge \text{W-TS}(B) = 0 \implies$ Granted. $\text{R-TS}(B) := 100$.
4. $w_2(B)$: $\text{TS}(T_2) = 200 \ge \text{R-TS}(B) = 100$ and $\ge \text{W-TS}(B) = 0 \implies$ Granted. $\text{W-TS}(B) := 200$.
5. Every operation passes the timestamp test without rollback. The precedence graph has edges:
   $$
   T_1 \xrightarrow{A} T_2 \quad \text{and} \quad T_1 \xrightarrow{B} T_2
   $$
   The graph is acyclic, equivalent to serial order $\langle T_1, T_2 \rangle$.
6. **Result:** Schedule $S_2$ is **valid and completely permitted under TSO**.

###### Step 3: Evaluation Under 2PL
Now attempt to execute the exact interleaved operation sequence of $S_2$ using locks:
1. For $T_1$ to execute $r_1(A)$, it must hold at least an S-lock on $A$.
2. For $T_2$ to subsequently execute $w_2(A)$ while $T_1$ is still active, $T_1$ **must release its lock on $A$** (since X-locks and S-locks are mutually incompatible).
3. The moment $T_1$ releases its lock on $A$, **$T_1$ enters its shrinking phase**.
4. By the fundamental definition of Two-Phase Locking:
   $$
   \text{A transaction in the shrinking phase CANNOT acquire any new locks!}
   $$
5. At step 3, $T_1$ must execute $r_1(B)$. To read $B$, $T_1$ must acquire a lock on $B$.
   - If $T_1$ did not lock $B$ upfront, it is blocked from acquiring a lock on $B$ now, violating 2PL.
   - If $T_1$ had locked $B$ upfront before releasing $A$, then $T_1$ would hold a lock on $B$ at step 4. In that case, $T_2$ could not acquire an X-lock on $B$ to execute $w_2(B)$ until $T_1$ finishes!
6. Therefore, the exact sequence of interleaved operations in $S_2$ **cannot be produced by any 2PL execution**.
7. **Result:** Schedule $S_2$ is **impossible under 2PL**.

```text
Venn Diagram Representation of Concurrency Control Schedules:
+-------------------------------------------------------------+
| Conflict Serializable Schedules (CSR)                       |
|                                                             |
|   +-----------------------+     +-----------------------+   |
|   | 2PL Schedules         |     | TSO Schedules         |   |
|   |                       |     |                       |   |
|   |      Schedule S1      |     |      Schedule S2      |   |
|   |   (r2 w2 c2 r1 w1 c1) |     |   (r1 w2 r1 w2)       |   |
|   |                       |     |                       |   |
|   +-----------+-----------+     +-----------+-----------+   |
|               |                             |               |
|               +-------------+---------------+               |
|                             |                               |
|                             v                               |
|                     [ Intersection ]                        |
|                  Strict Serial Execution                    |
+-------------------------------------------------------------+
```

#### 3. RUET Exam Insights & Examiner Notes
- **Mathematical Rigor:** In RUET exams, avoid vague prose when comparing protocol coverage. Always provide the two concrete schedules ($S_1$ and $S_2$), evaluate each against the lock point and timestamp rules step by step, and state the formal set relation:
  $$
  \text{Class}(2\text{PL}) \not\subseteq \text{Class}(\text{TSO}) \quad \text{and} \quad \text{Class}(\text{TSO}) \not\subseteq \text{Class}(2\text{PL})
  $$

---

### Exercise 18.28 · Cascading Abort Prevention via Commit Bit on Reads

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.28 (p. 903)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.6)
> - **Tested Concepts:** Timestamp Ordering enhancements, commit bit, dirty read prevention, cascading rollbacks, write invariants.

**Question (Silberschatz 7e Exercise 18.28).**
> Under a modified version of the timestamp protocol, we require that a commit bit be tested to see whether a read request must wait. Explain how the commit bit can prevent cascading abort. Why is this test not necessary for write requests?

#### 1. Core Principles & Concept Overview
The primary practical drawback of the standard Timestamp-Ordering protocol is that it permits transactions to read uncommitted updates, leading to dirty reads and cascading rollbacks. 

To overcome this, the modified protocol introduces a **Commit Bit**, denoted $c(Q)$, associated with each data item $Q$:
- $c(Q) = \text{true}$: The transaction that performed the last write on $Q$ has successfully committed.
- $c(Q) = \text{false}$: The transaction that performed the last write on $Q$ is still active (uncommitted).

#### 2. Detailed Step-by-Step Solution

##### Part 1: How the Commit Bit Prevents Cascading Aborts for Reads
Under standard TSO, if transaction $T_j$ issues $\text{read}(Q)$ and $\text{TS}(T_j) \ge \text{W-timestamp}(Q)$, the read is granted immediately, even if the transaction that wrote $Q$ (say $T_i$) has not committed. If $T_i$ aborts later, $T_j$ must be aborted as well.

In the modified protocol:
1. When transaction $T_j$ issues $\text{read}(Q)$:
   - The protocol first performs the standard serializability check: Is $\text{TS}(T_j) < \text{W-timestamp}(Q)$? If yes, $T_j$ is aborted.
   - If $\text{TS}(T_j) \ge \text{W-timestamp}(Q)$, the protocol evaluates the commit bit $c(Q)$:
     - **Case A ($c(Q) = \text{true}$):** The last write to $Q$ has committed. $T_j$ reads the committed value immediately, and $\text{R-timestamp}(Q) \leftarrow \max(\text{R-timestamp}(Q), \text{TS}(T_j))$.
     - **Case B ($c(Q) = \text{false}$):** The writing transaction $T_i$ is still uncommitted. $T_j$ is **suspended and placed in a wait queue** for data item $Q$.
2. **Resolution of the Waiting Read:**
   - If $T_i$ **commits**: $c(Q)$ is set to $\text{true}$. All transactions waiting to read $Q$ (including $T_j$) are awakened and allowed to read the committed value.
   - If $T_i$ **aborts**: $T_i$'s uncommitted write is removed, $Q$ is restored to its previous committed before-image, and $c(Q)$ is set to $\text{true}$. Transaction $T_j$ is awakened and reads the valid, pre-existing committed value.
3. **Outcome:**
   Because a transaction is **never permitted to read uncommitted data**, an abort of $T_i$ can never propagate to $T_j$. The schedule is guaranteed to be **cascadeless (and recoverable)**.

```text
Read Operation Flow with Commit Bit:
  T_j issues read(Q)
         |
  TS(T_j) < W-TS(Q)? ---- YES ----> [ Abort T_j ]
         | NO
         v
    c(Q) == true? ------ YES ----> [ Read Allowed Immediately ]
         | NO
         v
  [ Suspend T_j in Wait Queue ]
         |
  +------+------+
  |             |
(Writer Commits) (Writer Aborts)
  |             |
  v             v
Set c(Q)=true   Restore Before-image
Awaken T_j      Awaken T_j (Reads Old Committed Value)
```

##### Part 2: Why the Commit Bit Test is NOT Necessary for Write Requests
When a transaction $T_k$ issues a $\text{write}(Q)$ request:
1. **Writes Do Not Ingest Dirty Data:**
   A write operation produces a new value; it does not read or depend upon the current data contents of $Q$. Thus, executing a write never causes $T_k$ to "consume" a dirty value that would require $T_k$'s abort if the previous writer aborts.
2. **Standard Protocol Rules Already Protect Overwrites:**
   - If $\text{TS}(T_k) < \text{R-timestamp}(Q)$ or $\text{TS}(T_k) < \text{W-timestamp}(Q)$, the write is already rejected by standard TSO rules.
   - If $\text{TS}(T_k) \ge \text{W-timestamp}(Q)$ and $\ge \text{R-timestamp}(Q)$, $T_k$ is logically positioned *after* the previous writer.
3. **Commit Bit Shields Other Transactions:**
   When $T_k$ executes its write, it sets $c(Q) \leftarrow \text{false}$ and updates $\text{W-timestamp}(Q) \leftarrow \text{TS}(T_k)$. Any subsequent transaction attempting to *read* this new value will be forced to wait because $c(Q) = \text{false}$.
4. **Independent Rollback Handling:**
   If $T_k$ subsequently aborts, the recovery manager simply restores the prior before-image of $Q$. Because no third transaction was allowed to read $T_k$'s write (due to the read commit-bit test), **$T_k$'s abort affects no other transactions**.
5. **Conclusion:**
   Forcing write operations to wait on $c(Q)$ would introduce unnecessary transaction delays without providing any additional recovery benefit.

#### 3. RUET Exam Insights & Examiner Notes
- **Key Conceptual Takeaway:** The commit bit essentially grafts the cascadelessness property of Strict 2PL onto the non-locking Timestamp-Ordering framework.
- **Examiner's Favorite Follow-up:** *"Does adding wait queues for reads introduce deadlocks into TSO?"* Answer: **YES!** Because transactions can now wait for other transactions to commit, circular wait can occur (e.g., $T_1$ waits for $T_2$'s commit bit on $A$, while $T_2$ waits for $T_1$'s commit bit on $B$). The protocol must be paired with a wait-for graph or timeout monitor!

---

### Exercise 18.30 · Snapshot Isolation (First-Committer-Wins) vs. Optimistic Concurrency Control

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 18 (Concurrency Control), Regular Exercise 18.30 (p. 903)
> - **Syllabus Unit:** Unit 6 · Concurrency Control Protocols (Subtopic T11.6 & Advanced CC)
> - **Tested Concepts:** Snapshot Isolation (SI), First-Committer-Wins rule, Optimistic Concurrency Control (OCC), validation phase, write skew.

**Question (Silberschatz 7e Exercise 18.30).**
> Outline the key similarities and differences between the timestamp-based implementation of the first-committer-wins version of snapshot isolation, described in Exercise 18.15, and the optimistic-concurrency control-without-read-validation scheme, described in Section 18.9.3.

#### 1. Core Principles & Concept Overview
Modern high-performance relational and in-memory database engines (such as PostgreSQL, Oracle, and Microsoft SQL Server Hekaton) frequently avoid heavy shared locking by utilizing multi-version snapshots or optimistic validation:
- **Snapshot Isolation (SI) with First-Committer-Wins:** A transaction reads data from a consistent snapshot as of its start time ($\text{Start-TS}$). Writes are buffered privately. At commit time, the transaction validates that no other concurrent transaction that committed after its $\text{Start-TS}$ has written to any data item in its update set (**write-write conflict check**). If a conflict exists, it aborts ("first committer wins").
- **Optimistic Concurrency Control (OCC) Without Read Validation:** Classical OCC divides execution into Read, Validation, and Write phases. In main-memory designs where reads are executed against a multi-version consistent state, explicit read-set validation against concurrent writes can be omitted if the system only targets Snapshot Isolation or checks write-set collisions directly.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Comparative Architectural Analysis

```text
Execution Lifecycle Comparison:

Snapshot Isolation (First-Committer-Wins):
  [Start: Get Start-TS] ---> [Read from Snapshot] ---> [Buffer Writes in Local Memory]
                                                                |
                                                                v
                                              [Validation: Overlapping Write Check]
                                                    /                     \
                                            (Conflict Found)        (No Conflict)
                                                  /                         \
                                           [ Abort Tx ]              [ Assign Commit-TS ]
                                                                     [ Write to Database ]

OCC Without Read Validation:
  [Phase 1: Read Phase] --------> [Read Consistent Memory State]
                                  [Buffer Updates in Private Write Set]
                                                |
                                                v
  [Phase 2: Validation Phase] --> [Acquire Short-Term Latches on Write Set]
                                  [Verify No Concurrent Writes Committed to Same Items]
                                                |
                                                v
  [Phase 3: Write Phase] -------> [Copy Buffered Writes to Database State]
                                  [Release Latches & Commit]
```

##### Step 2: Key Similarities
1. **Lock-Free Read Operations:**
   In both protocols, read requests never acquire shared (S) locks and never block concurrent write operations. Reads are satisfied from a point-in-time snapshot.
2. **Private Local Write Buffering:**
   Updates are never applied directly to the global database during transaction execution. Both schemes buffer modified tuples in private transaction-local workspace until commit processing begins.
3. **Commit-Time Concurrency Validation:**
   Both protocols adopt an optimistic philosophy: conflicts are not detected eagerly when operations occur, but are deferred to transaction validation at commit time.
4. **Resolution of Write-Write Collisions (First-Committer-Wins):**
   Both schemes enforce the exact same rule for write-write conflicts: if transactions $T_1$ and $T_2$ execute concurrently and both attempt to modify the same item $Q$, the transaction that reaches the commit phase first succeeds; the slower transaction is detected as conflicting and is aborted.
5. **Freedom from Cascading Aborts:**
   Because neither protocol ever exposes uncommitted private writes to other active transactions, cascading rollbacks are structurally impossible.

##### Step 3: Key Differences

| Dimension | Snapshot Isolation (First-Committer-Wins) | OCC Without Read Validation (§18.9.3) |
| :--- | :--- | :--- |
| **Primary System Target** | Disk-based or general-purpose RDBMS (PostgreSQL, Oracle) with MVCC undo logs. | High-throughput, multi-core **main-memory databases** (e.g., Silo, Hekaton). |
| **Serializability Guarantee** | **Does NOT guarantee serializability.** Vulnerable to the **Write Skew anomaly** (where transactions read overlapping data and update disjoint data). | When read validation is omitted, it provides Snapshot Isolation. If serializability is required, it must be paired with SSI locks or epoch validation. |
| **Validation Mechanism** | Uses **monotonic timestamp intervals** ($\text{Start-TS}(T)$ to $\text{Commit-TS}(T)$) or inspects item write timestamps ($\text{W-timestamp}(Q) > \text{Start-TS}(T)$). | Uses **short-term memory latches** to lock write-set records atomically, verifying version counters without timestamp range joins. |
| **Storage Architecture** | Requires multi-version storage records (tuple header commit-tags, rollback undo segments). | Updates memory pointers directly during the microsecond write phase; does not require deep undo segment traversal. |
| **Abort Penalty** | Relatively high (disk buffer coordination and undo logging). | Extremely low (discarding private in-memory cache buffers). |

##### Step 4: The Write Skew Anomaly in Snapshot Isolation
To illustrate why first-committer-wins SI does not ensure full serializability (whereas full OCC with read validation does), consider the classic **medical doctor on-call constraint**:
- *Integrity Constraint:* At least one doctor must remain on call ($A + B \ge 1$). Currently, both $A$ and $B$ are on call ($A=1, B=1$).
- $T_1$ reads $A$ and $B$; seeing both active, $T_1$ takes leave by updating $A \leftarrow 0$.
- $T_2$ reads $A$ and $B$ concurrently; seeing both active, $T_2$ takes leave by updating $B \leftarrow 0$.
- *Under First-Committer-Wins SI:*
  - $T_1$'s update set is $\{A\}$. No other transaction updated $A$. $T_1$ commits.
  - $T_2$'s update set is $\{B\}$. No other transaction updated $B$. $T_2$ commits.
  - *Result:* $A=0, B=0$ (zero doctors on call). The integrity constraint is violated! The schedule is non-serializable.
- *Under Classical OCC (with Read Validation):*
  - $T_2$'s validation step checks whether the data items it *read* ($\{A, B\}$) were modified by $T_1$. Since $A$ was modified by $T_1$, $T_2$'s read validation **fails**, and $T_2$ is aborted, preserving database consistency.

#### 3. RUET Exam Insights & Examiner Notes
- **Modern Curriculum Value:** This question connects traditional locking theory to modern enterprise engine internals. Emphasize that while Snapshot Isolation eliminates dirty reads, non-repeatable reads, and lost updates, its lack of read validation allows **write skew**, which is why PostgreSQL implemented Serializable Snapshot Isolation (SSI).


---

[← Prev: T11 Part 2](T11_Part2_2PL_and_Lock_Conversions.md) | [Index](00_Index.md) | [Next: T12 Part 1 →](T12_Part1_Failure_Types_and_RAID_Intro.md)
