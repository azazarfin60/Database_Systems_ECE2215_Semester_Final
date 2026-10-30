---
title: "T11 (Part 1) · Locking Protocols & Compatibility · Exercise Solutions"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T11
topic_id: T11
part: 1
exercise_count: 11
source_chapters:
  - "Chapter 18"
---

[← Prev: T10](T10_Serializability.md) | [Index](00_Index.md) | [Next: T11 Part 2 →](T11_Part2_2PL_and_Lock_Conversions.md)

---

# T11 (Part 1) · Locking Protocols & Compatibility

> [!info] Topic Card · Concurrency Control Protocols (Part 1)
> **Syllabus Unit:** Unit 6 · Transactions & Concurrency Control  
> **Source Chapter:** Silberschatz, Korth & Sudarshan, *Database System Concepts* (7th Ed.), Chapter 18 (*Concurrency Control*)  
> **Primary Subtopic:** `T11.1` — Lock-based protocols, shared/exclusive locks, compatibility matrix, lock conversions, starvation handling, multiple-granularity locking, tree protocols, latch-free concurrency  
> **Assigned Exercises (11 Total):**  
> - **Practice Exercises (9):** PE 18.1, PE 18.6, PE 18.7, PE 18.9, PE 18.10, PE 18.11, PE 18.14, PE 18.15, PE 18.16  
> - **Regular Exercises (2):** EX 18.19, EX 18.22  
> **RUET Exam Alignment:** Directly solves recurring questions on 2PL lock points, conflict serializability proofs, tree/forest protocols, multiple-granularity intention locks, and lock-free data structures (tested in 2017 Q.7(a), 2018 Q.6(b), 2020 Q.7(b), 2021 Q.8(b), 2024 Q.8(b), and CT-04).

---

## Table of Exercises in This Note

| Exercise | Focus / Topic | Type | Subtopic | Key Mechanics & Core Concepts | RUET Final Exam Relevance |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **PE 18.1** | 2PL Serializability & Lock Points | Practice | T11.1 | Precedence graph acyclicity proof, lock-point topological order | High · Direct repeat of 2020 Q.7(b) |
| **PE 18.6** | OS Memory-Protection Locking | Practice | T11.1 | Page-level locking, `mprotect()`, `SIGSEGV` fault-driven lock upgrades | Medium · Conceptual architecture |
| **PE 18.7** | Increment Lock Mode ($I$) | Practice | T11.1 | Commutativity, $3 \times 3$ compatibility matrix, hot-spot counter throughput | High · Advanced locking design |
| **PE 18.9** | Multiple-Granularity Lock Overhead | Practice | T11.1 | Granularity hierarchy, intention locks (IS/IX), lock overhead trade-offs | High · Core concept in MGL |
| **PE 18.10** | Comprehensive Protocol Comparison | Practice | T11.1 | Evaluation of 7 protocols (2PL, MGL, Tree, TSO, OCC, MVTO, MV2PL) | High · RUET 10-mark essay favorite |
| **PE 18.11** | Speculative Dry-Run Pre-execution | Practice | T11.1 | Buffer cache pre-warming, I/O latency decoupling, lock holding reduction | Medium · Performance optimization |
| **PE 18.14** | $\text{B}^+$-Tree Safe-Node Early Unlocking | Practice | T11.1 | Latch crabbing, node split isolation, root contention mitigation | Medium · Index concurrency |
| **PE 18.15** | Snapshot Isolation Validation Schemes | Practice | T11.1 | First-committer-wins vs. First-updater-wins, write timestamps, lock isolation | High · Modern DBMS concurrency |
| **PE 18.16** | Latch-Free Lists & ABA Problem | Practice | T11.1 | Atomic CAS/DCAS, tagged pointers in 48-bit address space, lock-free stack | Medium · High-performance engine design |
| **EX 18.19** | Forest Protocol Non-Serializability | Exercise | T11.1 | Counterexample on disjoint trees, cross-tree interleaving cycle | High · Theoretical pitfall question |
| **EX 18.22** | Implicit vs. Explicit Locking | Exercise | T11.1 | Lock table footprint vs. ancestor inheritance, intention traversal | High · 3–4 mark direct definition |

---

## T11.1 · Lock-Based Protocols, Compatibility Matrix, and Concurrency Control

---

### Exercise 18.1 · Two-Phase Locking Ensures Conflict Serializability via Lock Points

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.1, Page 899.
> - **Type:** Practice Exercise (Theoretical Proof).
> - **Difficulty Rating:** ⭐⭐⭐⭐ (Medium-Hard).
> - **RUET Exam Mapping:** Directly identical to **RUET 2020 Q.7(b)** [04 Marks] and provides the theoretical foundation for **2021 Q.8(b)** and **2024 Q.8(b)**.

**Question (Silberschatz 7e Exercise 18.1).**  
Show that the two-phase locking protocol ensures conflict serializability and that transactions can be serialized according to their lock points.

---

#### 1. Core Principles & Concept Overview

- **Two-Phase Locking (2PL) Protocol:** A transaction $T_i$ must adhere to two distinct, monotonic phases during its execution:
  1. **Growing Phase:** $T_i$ may acquire new locks (shared or exclusive), but may not release any lock.
  2. **Shrinking Phase:** $T_i$ may release existing locks, but may not acquire any new locks.
- **Lock Point:** The exact instant in time when a transaction acquires its final lock (i.e., the end of its growing phase). Once the lock point is reached, the transaction can only hold or release locks.
- **Precedence Graph (Serialization Graph):** A directed graph $G = (V, E)$ where vertices $V$ represent committed transactions, and a directed edge $T_i \to T_j$ exists if there are conflicting operations $o_i \in T_i$ and $o_j \in T_j$ accessing the same data item $Q$ such that $o_i$ executes before $o_j$ in the schedule.
- **Conflict Serializability Theorem:** A schedule $S$ is conflict serializable if and only if its precedence graph $G(S)$ is acyclic (contains no directed cycles).

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Characterize the Temporal Ordering of Conflicting Operations
Let $S$ be any schedule produced by transactions following the Two-Phase Locking protocol. Suppose there is a directed edge $T_i \to T_j$ in the precedence graph $G(S)$.

By definition of an edge in $G(S)$:
1. $T_i$ executes an operation $o_i(Q)$ and $T_j$ executes an operation $o_j(Q)$ on a common data item $Q$.
2. At least one of these operations is a write (i.e., $(o_i = \text{write} \land o_j = \text{read})$, $(o_i = \text{read} \land o_j = \text{write})$, or $(o_i = \text{write} \land o_j = \text{write})$).
3. $o_i(Q)$ precedes $o_j(Q)$ in the schedule $S$.

##### Step 2: Map Operations to Lock Acquisitions and Releases
Under any lock-based concurrency control protocol:
- To execute $o_i(Q)$, transaction $T_i$ must hold an appropriate lock (Shared $S$ or Exclusive $X$) on item $Q$ at the time of execution.
- To execute $o_j(Q)$, transaction $T_j$ must hold a conflicting lock on item $Q$.
- Because the locks required by $o_i$ and $o_j$ are incompatible (by the lock compatibility matrix), $T_j$ cannot acquire its lock on $Q$ while $T_i$ still holds its lock on $Q$.
- Therefore, $T_i$ must release its lock on item $Q$ *before* $T_j$ can acquire its lock on item $Q$:
  $$
  t_{\text{unlock}}(T_i, Q) < t_{\text{lock}}(T_j, Q)
  $$

##### Step 3: Relate Lock Events to Lock Points
Let $L(T)$ denote the **lock point** of transaction $T$.
- By definition, $L(T_i)$ is the time at which $T_i$ obtains its last lock.
- Because $T_i$ obeys the 2PL rule, it cannot acquire any locks after it begins releasing locks. Therefore, all lock acquisitions of $T_i$ precede all lock releases of $T_i$.
- Specifically, the release of the lock on $Q$ by $T_i$ must occur at or after its lock point:
  $$
  L(T_i) \le t_{\text{unlock}}(T_i, Q)
  $$
- For transaction $T_j$, the acquisition of the lock on $Q$ must occur during its growing phase, which means it occurs at or before $T_j$'s lock point:
  $$
  t_{\text{lock}}(T_j, Q) \le L(T_j)
  $$

##### Step 4: Establish the Strict Inequality of Lock Points
Chaining the inequalities established in Steps 2 and 3:
$$
L(T_i) \le t_{\text{unlock}}(T_i, Q) < t_{\text{lock}}(T_j, Q) \le L(T_j)
$$

This yields the fundamental invariant:
$$
T_i \to T_j \in E \implies L(T_i) < L(T_j)
$$

##### Step 5: Prove Acyclicity of the Precedence Graph
We now prove that $G(S)$ contains no directed cycles by contradiction.

Assume, for the sake of contradiction, that $G(S)$ contains a directed cycle of length $k \ge 2$:
$$
T_1 \to T_2 \to T_3 \to \dots \to T_k \to T_1
$$

Applying our fundamental invariant to each edge along the cycle:
$$
L(T_1) < L(T_2) < L(T_3) < \dots < L(T_k) < L(T_1)
$$

By the transitivity of the strict inequality relation on real numbers:
$$
L(T_1) < L(T_1)
$$

This is a logical contradiction (no real number can be strictly less than itself).

Therefore, the assumption that a cycle exists is false. The precedence graph $G(S)$ must be strictly **acyclic**. By the Conflict Serializability Theorem, the schedule $S$ is **conflict serializable**.

##### Step 6: Serialization Order by Lock Points
Because $G(S)$ is a directed acyclic graph (DAG), it admits a topological sort. Since every directed edge $T_i \to T_j$ satisfies $L(T_i) < L(T_j)$, sorting the transactions in ascending numerical order of their lock points:
$$
L(T_{\pi(1)}) \le L(T_{\pi(2)}) \le \dots \le L(T_{\pi(n)})
$$
provides a valid topological sort of $G(S)$. Hence, the concurrent execution is equivalent to a serial schedule ordered by the transactions' lock points. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes

- **Marking Distribution (04 Marks):**
  - Stating 2PL growing/shrinking rules and defining the lock point: **1 Mark**.
  - Deriving the inequality $L(T_i) < L(T_j)$ across a conflict edge: **1.5 Marks**.
  - Cycle contradiction proof ($L(T_1) < L(T_1)$) and topological sort conclusion: **1.5 Marks**.
- **Common Exam Trap:** Students frequently forget to state *why* $t_{\text{unlock}}(T_i, Q) < t_{\text{lock}}(T_j, Q)$. Examiners penalize answers that do not explicitly mention the **lock compatibility matrix** (mutual exclusion of conflicting locks).
- **Exam-Sheet Time-Saver:** Draw a quick 1D timeline showing:
  `Growing Phase` $\to$ `[Lock Point L(Ti)]` $\to$ `Shrinking Phase (Unlock Q)` $\to$ `Tj acquires Q` $\to$ `[Lock Point L(Tj)]`.

---

### Exercise 18.6 · Page-Level Locking via Operating System Memory-Protection Mechanisms

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.6, Page 899.
> - **Type:** Practice Exercise (Systems Design / OS Integration).
> - **Difficulty Rating:** ⭐⭐⭐ (Medium).
> - **RUET Exam Mapping:** Directly relevant to advanced architecture questions in Unit 1 / Unit 6 concerning how the DBMS interacts with the OS virtual memory manager and persistent object stores.

**Question (Silberschatz 7e Exercise 18.6).**  
Locking is not done explicitly in persistent programming languages. Rather, objects (or the corresponding pages) must be locked when the objects are accessed. Most modern operating systems allow the user to set access protections (no access, read, write) on pages, and memory access that violate the access protections result in a protection violation (see the Unix `mprotect` command, for example). Describe how the access-protection mechanism can be used for page-level locking in a persistent programming language.

---

#### 1. Core Principles & Concept Overview

- **Persistent Programming Languages:** Languages where objects can outlive the execution of the process that created them, residing in persistent storage but accessed transparently in virtual memory via standard pointer dereferencing.
- **Hardware Page-Fault Trap:** Modern CPUs and MMUs (Memory Management Units) enforce page-level permissions:
  - `PROT_NONE`: Any read or write access triggers a hardware exception (`SIGSEGV` in Unix).
  - `PROT_READ`: Read accesses succeed without intervention; write accesses trigger an exception.
  - `PROT_READ | PROT_WRITE`: Both read and write operations proceed at raw hardware speed.
- **Transparent Locking:** Instead of emitting explicit software calls (`lock_shared()`, `lock_exclusive()`) before every variable dereference, the runtime intercepts MMU protection faults, acquires the appropriate lock from the lock manager, adjusts page permissions, and resumes execution.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Initial State Configuration
1. When a transaction begins, all virtual memory pages containing persistent objects are mapped into the process's address space.
2. The runtime invokes `mprotect(page_address, page_size, PROT_NONE)` on all persistent pages.
3. In this state, neither read nor write operations are permitted by the hardware MMU.

##### Step 2: Handling Read Accesses (Shared Lock Acquisition)
1. When the transaction executes an instruction that reads an object (e.g., `x = obj->value`), the CPU MMU detects an access violation because the page has `PROT_NONE`.
2. The OS delivers a segmentation fault signal (`SIGSEGV`) to the application process.
3. The database runtime's registered signal handler intercepts the trap and inspects the architecture-specific fault address register (`siginfo_t.si_addr`).
4. The signal handler requests a **Shared Lock (S-lock)** on the page containing that address from the DBMS lock manager.
5. If another transaction holds an incompatible (exclusive) lock on the page, the faulting thread is placed in a wait queue until the lock is granted.
6. Once the S-lock is granted:
   - The runtime calls `mprotect(page_address, page_size, PROT_READ)`.
   - The signal handler returns. The CPU re-executes the faulting load instruction.
7. Subsequent reads to any object on that page proceed at **zero CPU overhead** (no software lock checks).

##### Step 3: Handling Write Accesses (Exclusive Lock Upgrade)
1. When the transaction attempts to modify an object on a page currently protected with `PROT_READ` (e.g., `obj->value = 42`), the MMU triggers a write-protection fault (`SIGSEGV`).
2. The signal handler catches the fault and determines that the transaction already holds an S-lock on the page.
3. The runtime requests a **Lock Upgrade** from Shared (S) to **Exclusive (X)** mode from the lock manager:
   - If other transactions currently hold S-locks, the thread waits until they release them.
4. Once the X-lock is granted:
   - The runtime invokes `mprotect(page_address, page_size, PROT_READ | PROT_WRITE)`.
   - The signal handler returns, and the write instruction is re-executed successfully.
5. If the page was initially in `PROT_NONE` state (a blind write), the handler directly requests an X-lock and sets permissions to `PROT_READ | PROT_WRITE`.

##### Step 4: Transaction Commit or Abort (Lock Release & Reset)
1. Following the Two-Phase Locking protocol (typically Strict 2PL), all held page locks are retained until transaction completion.
2. At commit or abort:
   - Dirty pages are flushed to the write-ahead log (WAL) and disk.
   - The runtime calls `mprotect(page_address, page_size, PROT_NONE)` for all pages touched by the transaction.
   - All S and X locks are released in the lock manager.

```text
                    +------------------------+
                    |  Page State: PROT_NONE |
                    +------------------------+
                                |
                     Read Fault | (SIGSEGV)
                                v
               +----------------------------------+
               | Acquire Shared (S) Lock on Page  |
               | Call mprotect(..., PROT_READ)    |
               +----------------------------------+
                                |
                                v
                    +------------------------+
                    | Page State: PROT_READ  |
                    +------------------------+
                                |
                    Write Fault | (SIGSEGV)
                                v
            +---------------------------------------+
            | Upgrade to Exclusive (X) Lock on Page |
            | Call mprotect(..., PROT_READ|WRITE)   |
            +---------------------------------------+
                                |
                                v
                 +-----------------------------+
                 | Page State: PROT_READ|WRITE |
                 +-----------------------------+
                                |
                     Commit / Abort Event
                                v
              +------------------------------------+
              | Release Locks & Reset to PROT_NONE |
              +------------------------------------+
```

##### Step 5: Performance & Concurrency Trade-Offs
- **Advantages:** Eliminates the massive runtime overhead of interpreting or embedding software lock checks into compiled code; provides seamless object persistence.
- **Disadvantages:**
  - **Coarse Granularity:** Locking occurs at page granularity (typically $4\,\text{KB}$ to $64\,\text{KB}$), causing **false sharing** (two transactions modifying distinct objects on the same physical page will conflict).
  - **OS Context Switch Latency:** Handling a signal/page fault involves an expensive kernel-to-user context switch ($\approx 1\text{--}5\,\mu\text{s}$).

---

#### 3. RUET Exam Insights & Examiner Notes

- **Examiner Expectation:** A complete answer must mention: (1) Setting pages to `PROT_NONE`, (2) catching OS signals (`SIGSEGV`), (3) mapping read faults to S-locks and write faults to X-locks (lock upgrade), and (4) resetting permissions upon transaction completion.
- **Keyword Checklist:** `mprotect()`, `PROT_NONE`, `PROT_READ`, `PROT_WRITE`, signal handler / page fault, lock upgrade, false sharing.

---

### Exercise 18.7 · Atomic Increment Operations and Increment Lock Mode

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.7, Pages 899–900.
> - **Type:** Practice Exercise (Advanced Lock Protocol & Mathematical Proof).
> - **Difficulty Rating:** ⭐⭐⭐⭐ (Medium-Hard).
> - **RUET Exam Mapping:** Directly tests custom lock mode compatibility and commutativity principles, frequently examined in high-mark theoretical questions.

**Question (Silberschatz 7e Exercise 18.7).**  
Consider a database system that includes an atomic **increment** operation, in addition to the read and write operations. Let $V$ be the value of data item $X$. The operation
$$
\textbf{increment}(X) \text{ by } C
$$
sets the value of $X$ to $V + C$ in an atomic step. The value of $X$ is not available to the transaction unless the latter executes a $\text{read}(X)$.

Assume that increment operations lock the item in increment mode using the compatibility matrix in Figure 18.25.

a. Show that, if all transactions lock the data that they access in the corresponding mode, then two-phase locking ensures serializability.  
b. Show that the inclusion of **increment** mode locks allows for increased concurrency.

---

#### 1. Core Principles & Concept Overview

- **Figure 18.25 Compatibility Matrix:**
  The lock compatibility matrix between Shared ($S$), Exclusive ($X$), and Increment ($I$) modes is defined as:

| Mode Held \ Mode Requested | Shared ($S$) | Exclusive ($X$) | Increment ($I$) |
| :--- | :---: | :---: | :---: |
| **Shared ($S$)** | **True** | False | False |
| **Exclusive ($X$)** | False | False | False |
| **Increment ($I$)** | False | False | **True** |

- **Commutativity of Operations:** Two operations $o_1$ and $o_2$ commute if for all possible database states, executing $o_1$ followed by $o_2$ yields the exact same state and produces the exact same return values as executing $o_2$ followed by $o_1$.
- **Key Observation on Increment:**
  The operation $\textbf{increment}(X) \text{ by } C_1$ followed by $\textbf{increment}(X) \text{ by } C_2$ sets:
  $$
  V' = (V + C_1) + C_2 = V + (C_1 + C_2) = (V + C_2) + C_1
  $$
  Furthermore, neither operation returns a value to the issuing transaction. Thus, two increment operations commute unconditionally.

---

#### 2. Detailed Step-by-Step Solution

##### Part (a): Proof that 2PL with Increment Mode Ensures Serializability

###### Step 1: Analyze Operation Conflicts
Two operations on the same data item $X$ conflict if and only if they do not commute:
1. **$\text{read}(X)$ and $\text{read}(X)$:** Commute (both obtain $S$-locks; $S$ is compatible with $S$).
2. **$\text{read}(X)$ and $\text{write}(X)$:** Do not commute ($S$ and $X$ are incompatible).
3. **$\text{write}(X)$ and $\text{write}(X)$:** Do not commute ($X$ and $X$ are incompatible).
4. **$\text{read}(X)$ and $\textbf{increment}(X)$:** Do not commute! If $\text{read}(X)$ executes first, it reads $V$; if $\textbf{increment}(X)$ executes first, the read returns $V + C$. The lock compatibility matrix correctly marks $S$ and $I$ as **incompatible** (False).
5. **$\text{write}(X)$ and $\textbf{increment}(X)$:** Do not commute! A write overwrites the value ($X := W$), discarding previous increments, whereas an increment computes $W + C$. The matrix correctly marks $X$ and $I$ as **incompatible** (False).
6. **$\textbf{increment}(X)$ and $\textbf{increment}(X)$:** **Commute!** Both operations add a constant to $X$, and neither transaction observes intermediate states. Thus, their execution order does not affect the final value of $X$ or any transaction's computations. The matrix marks $I$ and $I$ as **compatible** (True).

###### Step 2: Formulate the Serialization Graph with Non-Commuting Operations
Define the serialization graph $G = (V, E)$ where an edge $T_i \to T_j$ is introduced if and only if:
- $T_i$ and $T_j$ execute operations on the same data item $X$,
- The operations **do not commute**, and
- $T_i$ executes its non-commuting operation before $T_j$.

*(Note: If $T_i$ and $T_j$ only execute commutative increment operations on $X$, no edge is added between them for item $X$, because their execution order can be inverted without altering the final state or any observable result.)*

###### Step 3: Establish Lock Point Ordering
For every pair of non-commuting operations between $T_i$ and $T_j$ on item $X$:
1. The operations require incompatible lock modes (from the compatibility matrix).
2. Because the modes are incompatible, $T_j$ cannot acquire its lock on $X$ until $T_i$ has released its lock on $X$.
3. Thus, $T_i$ releases its lock on $X$ before $T_j$ acquires its lock on $X$:
   $$
   t_{\text{unlock}}(T_i, X) < t_{\text{lock}}(T_j, X)
   $$
4. Under the Two-Phase Locking protocol, all locks of $T_i$ are held until its lock point $L(T_i)$, and all locks of $T_j$ are acquired before or at its lock point $L(T_j)$:
   $$
   L(T_i) \le t_{\text{unlock}}(T_i, X) < t_{\text{lock}}(T_j, X) \le L(T_j) \implies L(T_i) < L(T_j)
   $$

###### Step 4: Deduce Acyclicity
Every directed edge in the precedence graph strictly increases the lock point ($L(T_i) < L(T_j)$). Therefore, any cycle would imply $L(T_1) < L(T_1)$, an impossibility.

Hence, the precedence graph is acyclic. Topological sorting by lock points yields an equivalent serial schedule. Transactions that share only increment operations on $X$ can be ordered arbitrarily in the serial schedule without affecting the final database state. Thus, serializability is guaranteed. $\blacksquare$

---

##### Part (b): Proof of Increased Concurrency

###### Step 1: Baseline Under Standard Read/Write Locking
In a standard system without an increment lock mode:
- An operation like `X := X + C` must be implemented via raw operations:
  $$
  \text{read}(X); \quad X := X + C; \quad \text{write}(X)
  $$
- To execute $\text{write}(X)$, the transaction must acquire an **Exclusive ($X$) lock** on $X$.
- Because $X$ mode is incompatible with $X$ mode, if $k$ transactions want to increment a common shared counter (e.g., ticket reservation count, account balance, seat allocation):
  $$
  \text{Concurrency} = 1
  $$
  All $k$ transactions are forced to execute strictly sequentially, forming a serialized queue.

###### Step 2: Concurrency Under Increment ($I$) Mode
- With the $I$ lock mode, each transaction requests an $I$-lock on $X$.
- Because $I$ mode is compatible with $I$ mode, **all $k$ transactions can hold increment locks on $X$ simultaneously**.
- Multiple increment operations can be executed concurrently in main memory (e.g., via hardware atomic instructions like `atomic_add` or CAS):
  $$
  \text{Concurrency} = k
  $$
- None of the incrementing transactions block each other. Concurrency on hot-spot data items increases from $1$ to $k$, drastically eliminating lock contention bottlenecks and enhancing system throughput. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes

- **Examiner Expectation:** In part (a), the examiner looks for a mathematical argument on **commutativity**. You must explicitly show that $(V + C_1) + C_2 = (V + C_2) + C_1$ and state that commutative operations do not induce dependency edges in the conflict graph.
- **Practical Real-World Example:** Cite an airline reservation system incrementing `booked_seats` or an e-commerce inventory decrementing stock. Under standard 2PL, this creates a severe throughput bottleneck; under increment locking, throughput scales linearly with CPU cores.

---

### Exercise 18.9 · Multiple-Granularity Locking Overhead and Concurrency Trade-Offs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.9, Page 900.
> - **Type:** Practice Exercise (Analytical Comparison & Examples).
> - **Difficulty Rating:** ⭐⭐⭐ (Medium).
> - **RUET Exam Mapping:** Directly tests understanding of hierarchical intention locking (IS, IX, SIX), which is tested in Unit 6 and CT-04.

**Question (Silberschatz 7e Exercise 18.9).**  
Use of multiple-granularity locking may require more or fewer locks than an equivalent system with a single lock granularity. Provide examples of both situations, and compare the relative amount of concurrency allowed.

---

#### 1. Core Principles & Concept Overview

- **Multiple-Granularity Locking (MGL):** Organizes data items as a tree hierarchy:
  $$
  \text{Database} \longrightarrow \text{Area} \longrightarrow \text{Relation} \longrightarrow \text{Page} \longrightarrow \text{Record / Tuple}
  $$
- **Intention Locks:** Before locking a node explicitly in Shared ($S$) or Exclusive ($X$) mode, a transaction must lock all its ancestor nodes in an appropriate **intention mode**:
  - **Intention-Shared (IS):** Indicates explicit locking will occur at a lower level in $S$ mode.
  - **Intention-Exclusive (IX):** Indicates explicit locking will occur at a lower level in $X$ mode.
  - **Shared and Intention-Exclusive (SIX):** The subtree is locked explicitly in $S$ mode, and explicit locking will occur at lower levels in $X$ mode.
- **Lock Compatibility Table for MGL:**

| Held \ Requested | IS | IX | S | SIX | X |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **IS** | True | True | True | True | False |
| **IX** | True | True | False | False | False |
| **S** | True | False | True | False | False |
| **SIX** | True | False | False | False | False |
| **X** | False | False | False | False | False |

---

#### 2. Detailed Step-by-Step Solution

##### Situation 1: MGL Requires Significantly FEWER Locks (Coarse Access Pattern)

###### Scenario:
Consider a transaction $T_1$ that scans an entire relation $R$ containing $1,000,000$ tuples to generate an end-of-month statistical audit report (pure read-only table scan).

###### Single Fine-Granularity System (Tuple-Level Locking Only):
- $T_1$ must request and obtain a Shared ($S$) lock on **every individual tuple**.
- **Total Locks Acquired:**
  $$
  \text{Locks}(T_1) = 1,000,000 \text{ locks}
  $$
- **Overhead:** Enormous memory consumption in the lock table, $10^6$ hash-table lookups, and massive lock manager CPU overhead.

###### Multiple-Granularity Locking (MGL) System:
- $T_1$ traverses the tree from the root:
  1. Acquires an **IS lock** on the Database.
  2. Acquires an **S lock** on the Relation $R$.
- **Total Locks Acquired:**
  $$
  \text{Locks}(T_1) = 2 \text{ locks}
  $$
- All $1,000,000$ tuples inside relation $R$ are **implicitly locked in S mode**.

###### Concurrency Comparison:
- **Under Fine Granularity:** Other concurrent transactions can still update tuples in relation $R$ that $T_1$ has not yet read or already finished reading (high concurrency, high overhead).
- **Under MGL:** Because $T_1$ holds an explicit $S$ lock on relation $R$, no concurrent transaction can acquire an $IX$ or $X$ lock on relation $R$. Therefore, **no updates to any tuple in relation $R$ are permitted** while $T_1$ runs.
- **Trade-off:** MGL drastically reduces lock overhead (from $10^6$ to 2), but reduces concurrent update capability on that specific relation.

---

##### Situation 2: MGL Requires Significantly MORE Locks (Fine Access Pattern)

###### Scenario:
Consider a transaction $T_2$ that updates a single customer's address record (one tuple $t$) in relation $R$.

###### Single Coarse-Granularity System (Relation-Level Locking Only):
- The only available lock unit is the entire relation.
- $T_2$ acquires a single **Exclusive ($X$) lock** on Relation $R$.
- **Total Locks Acquired:**
  $$
  \text{Locks}(T_2) = 1 \text{ lock}
  $$

###### Multiple-Granularity Locking (MGL) System:
- To lock tuple $t$ at the leaf level, $T_2$ must traverse the hierarchy from the root down to the leaf, acquiring intention locks on all ancestor nodes:
  1. Acquire **IX lock** on Database.
  2. Acquire **IX lock** on Area.
  3. Acquire **IX lock** on Relation $R$.
  4. Acquire **IX lock** on Page $P$ containing $t$.
  5. Acquire **X lock** on Tuple $t$.
- **Total Locks Acquired:**
  $$
  \text{Locks}(T_2) = 5 \text{ locks}
  $$
- Even compared to a single tuple-granularity system without intention locks, MGL requires 5 locks instead of 1.

###### Concurrency Comparison:
- **Under Coarse Granularity (Relation-level X):** The entire relation $R$ is locked exclusively. No other transaction can read or write *any* tuple in $R$. Concurrency is crippled.
- **Under MGL:** $T_2$ holds only $IX$ locks on the Database, Area, Relation, and Page. Because $IX$ is compatible with $IX$ and $IS$, **thousands of other concurrent transactions can simultaneously read and update other tuples in the same relation and on the same page**.
- **Trade-off:** MGL incurs higher locking overhead (5 locks vs. 1), but achieves **vastly superior concurrency**.

---

##### Summary Comparison Matrix

| Metric | Situation 1: Bulk Relation Scan ($10^6$ tuples) | Situation 2: Point Single-Tuple Update |
| :--- | :--- | :--- |
| **Single-Granularity Locks** | $1,000,000$ (tuple-level) | $1$ (relation-level) |
| **MGL Locks** | $2$ (IS on DB, S on Relation) | $5$ (IX on path, X on tuple) |
| **Lock Count Ratio (MGL vs. Single)** | **$\approx 500,000\times$ FEWER locks** | **$5\times$ MORE locks** |
| **Concurrency Impact** | Lower update concurrency on relation $R$ | Maximized concurrency across all other tuples |
| **Optimal Use Case** | Analytical queries, reporting, table dumps | High-throughput OLTP transactions |

---

#### 3. RUET Exam Insights & Examiner Notes

- **Exam Presentation Tip:** Always structure your answer into two distinct, numbered subsections: (1) *Case where MGL requires fewer locks* and (2) *Case where MGL requires more locks*.
- **Examiner's Favorite Trap:** Forgetting to mention that ancestor nodes *must* be locked in intention modes. Make sure to list the full path: `Database (IX) -> Relation (IX) -> Page (IX) -> Tuple (X)`.

---

### Exercise 18.10 · Practical Evaluation & Comparative Analysis of 7 Concurrency Control Protocols

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.10, Page 900.
> - **Type:** Practice Exercise (Comprehensive Comparative Systems Analysis).
> - **Difficulty Rating:** ⭐⭐⭐⭐⭐ (Hard / Comprehensive).
> - **RUET Exam Mapping:** Standard 10-to-12 mark broad theoretical question in Section B of ECE 2215 semester finals.

**Question (Silberschatz 7e Exercise 18.10).**  
For each of the following protocols, describe aspects of practical applications that would lead you to suggest using the protocol, and aspects that would suggest not using the protocol:
- Two-phase locking
- Two-phase locking with multiple-granularity locking
- The tree protocol
- Timestamp ordering
- Validation
- Multiversion timestamp ordering
- Multiversion two-phase locking

---

#### 1. Core Principles & Concept Overview

Every concurrency control protocol navigates fundamental trade-offs:
1. **Serialization Guarantee:** Conflict serializability vs. View serializability.
2. **Deadlock Freedom:** Whether deadlocks are mathematically impossible or require detection/prevention.
3. **Cascading Rollback Prevention:** Recoverability and cascadelessness.
4. **Lock Overhead vs. Abort Overhead:** Pessimistic blocking vs. Optimistic restarting.
5. **Workload Alignment:** Read-heavy vs. Write-heavy; OLTP vs. OLAP.

---

#### 2. Detailed Step-by-Step Solution

##### Protocol 1: Standard Two-Phase Locking (2PL)
- **Aspects Suggesting Use:**
  - Standard OLTP applications with balanced read/write workloads and moderate contention.
  - Transactions require strict consistency, recoverability, and freedom from cascading rollbacks (when using **Strict 2PL**).
  - Data access patterns are dynamic and unpredictable at compile time.
- **Aspects Suggesting NOT Using:**
  - High-contention workloads on hot-spot data items: transactions block each other, causing convoy phenomena and severe throughput collapse.
  - Vulnerable to **deadlocks**, necessitating background deadlock detection threads (wait-for graph cycle hunting) or timeout aborts.
  - Long-running read queries block concurrent writers, starving updates.

##### Protocol 2: 2PL with Multiple-Granularity Locking (MGL)
- **Aspects Suggesting Use:**
  - Highly heterogeneous, mixed workloads where short point queries/updates (touching 1–5 records) run concurrently with large bulk scans (touching millions of records or entire tables).
  - Eliminates the need to hold millions of tuple locks during report generation or index rebuilds.
- **Aspects Suggesting NOT Using:**
  - Systems with purely uniform workloads (e.g., only single-record key-value lookups), where traversing the hierarchy and maintaining intention locks ($IS, IX$) adds pure CPU and memory overhead with zero concurrency benefit.
  - High implementation complexity in the lock manager engine.

##### Protocol 3: The Tree Protocol (Hierarchical Graph-Based Locking)
- **Aspects Suggesting Use:**
  - Specialized hierarchical data access, particularly **B+ tree index traversals** and directory tree navigation.
  - **Deadlock-Free:** Eliminates deadlock detection algorithms and wait-for graphs entirely.
  - Locks can be released earlier than in 2PL (no shrinking phase restriction), improving concurrency in the upper levels of the tree.
- **Aspects Suggesting NOT Using:**
  - Arbitrary, non-tree database schemas (general relational tables with many-to-many foreign keys cannot use it).
  - Transactions may be forced to lock unwanted ancestor nodes simply to reach a desired leaf node, causing unnecessary lock traffic.
  - Items cannot be relocked after being unlocked, severely limiting dynamic transactions that revisit data items.
  - Does not guarantee freedom from cascading aborts unless extended with strict holding rules.

##### Protocol 4: Timestamp Ordering (TSO)
- **Aspects Suggesting Use:**
  - Highly distributed database architectures where coordinating a centralized lock manager or distributed deadlock detection is prohibitively expensive.
  - Low-contention workloads where conflicts are rare.
  - **Deadlock-Free:** Because transactions never wait for locks, deadlocks are impossible.
- **Aspects Suggesting NOT Using:**
  - High-contention workloads: Conflicting operations cause frequent transaction aborts and rollbacks, wasting substantial CPU and I/O bandwidth.
  - Vulnerable to **starvation / livelock** of long-running transactions that repeatedly get aborted by newer incoming transactions.
  - Susceptible to cascading rollbacks unless writes are buffered until commit time.

##### Protocol 5: Validation-Based Protocol (Optimistic Concurrency Control - OCC)
- **Aspects Suggesting Use:**
  - Read-dominated environments (e.g., 95%+ read queries) where conflicts are exceptionally rare.
  - Memory-centric architectures where transactions execute entirely in private local memory workspaces without incurring locking overhead or latch contention.
  - Deadlock-free by design.
- **Aspects Suggesting NOT Using:**
  - Update-heavy or high-contention environments: Conflicting transactions run to completion before failing at the validation phase, completely wasting all CPU and memory work done during execution.
  - Long transactions face high abort probabilities because the likelihood of overlapping with a committed write transaction increases with transaction duration.

##### Protocol 6: Multiversion Timestamp Ordering (MVTO)
- **Aspects Suggesting Use:**
  - Environments with long-running analytical queries (OLAP) running alongside concurrent update transactions (OLTP).
  - **Read queries are never blocked and never cause aborts**: A read always finds an appropriate older version $Q_k$ where $\text{W-timestamp}(Q_k) \le TS(T_i)$.
- **Aspects Suggesting NOT Using:**
  - Substantial storage and garbage collection overhead: Older versions must be retained and periodically purged.
  - Write operations can still be aborted if an older transaction attempts to write an item that has already been read by a newer transaction ($TS(T_i) < \text{R-timestamp}(Q_k)$).

##### Protocol 7: Multiversion Two-Phase Locking (MV2PL)
- **Aspects Suggesting Use:**
  - The gold standard for modern commercial enterprise RDBMSs (PostgreSQL, Oracle, SQL Server, MySQL InnoDB).
  - Completely decouples readers from writers: **Readers never wait for writers, and writers never wait for readers.**
  - Read-only transactions run against a consistent historical snapshot (no locks acquired), while update transactions acquire standard 2PL locks on the latest version to ensure serializability.
- **Aspects Suggesting NOT Using:**
  - High storage footprint and CPU overhead required to maintain rollback segments / undo logs and execute background vacuum/purge threads.
  - Update-only workloads (100% writes) gain zero concurrency advantage over standard Strict 2PL while paying the version creation penalty.

---

##### Summary Comparison of Concurrency Control Protocols

| Protocol | Concurrency Mechanism | Deadlock Free? | Cascading Abort Free? | Primary Workload Advantage | Major Bottleneck / Disadvantage |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Two-Phase Locking (2PL)** | Pessimistic Lock Queues | No | Yes (Strict 2PL) | General OLTP, high consistency | Lock contention, deadlocks |
| **2PL with MGL** | Hierarchical Intention Locks | No | Yes (Strict) | Mixed bulk scans & point updates | Hierarchy navigation overhead |
| **Tree Protocol** | Directed Graph Locking | **Yes** | No | B+ tree indices, search paths | Unwanted ancestor locking |
| **Timestamp Ordering (TSO)** | Monotonic Timestamps | **Yes** | No (unless buffered) | Distributed systems, low conflict | High abort rate under contention |
| **Validation (OCC)** | Private Workspace Check | **Yes** | **Yes** | Read-heavy, rare conflicts | Wasted work on late aborts |
| **Multiversion TSO (MVTO)** | Multi-version Timestamps | **Yes** | **Yes** | Reads never abort or block | Storage overhead, write aborts |
| **Multiversion 2PL (MV2PL)** | MVCC Reads + 2PL Writes | No (for writes) | **Yes** | Readers never block writers | Version maintenance & vacuum |

---

#### 3. RUET Exam Insights & Examiner Notes

- **Structuring Strategy:** In RUET exams, avoid writing unformatted paragraphs. Use bulleted pairs for each protocol: **(a) When to Use (Pros)** and **(b) When NOT to Use (Cons)**.
- **High-Scoring Distinction:** Explicitly distinguish between **concurrency anomalies** (deadlocks, cascading rollbacks) and **resource overhead** (lock table memory, version garbage collection).

---

### Exercise 18.11 · Speculative Pre-Execution (Dry-Run) to Decouple Disk I/O from Lock Holding

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.11, Page 900.
> - **Type:** Practice Exercise (Performance Optimization Analysis).
> - **Difficulty Rating:** ⭐⭐⭐⭐ (Medium-Hard).
> - **RUET Exam Mapping:** High-level architectural reasoning question explaining why modern in-memory and disk-resident engines use prefetching and dry-run execution.

**Question (Silberschatz 7e Exercise 18.11).**  
Explain why the following technique for transaction execution may provide better performance than just using strict two-phase locking: First execute the transaction without acquiring any locks and without performing any writes to the database as in the validation-based techniques, but unlike the validation techniques do not perform either validation or writes on the database. Instead, rerun the transaction using strict two-phase locking. *(Hint: Consider waits for disk I/O.)*

---

#### 1. Core Principles & Concept Overview

- **The Disk I/O Latency Bottleneck under Strict 2PL:**
  In a traditional disk-resident database, access times follow a steep hierarchy:
  - Main Memory (DRAM) access: $\approx 50\text{--}100\,\text{ns}$.
  - Solid-State Drive (NVMe SSD) I/O: $\approx 20\text{--}100\,\mu\text{s}$.
  - Magnetic Hard Disk (HDD) I/O: $\approx 5\text{--}10\,\text{ms}$ ($10^5\times$ slower than DRAM).
- **The Lock Holding Convoys Problem:**
  Under Strict 2PL, if transaction $T$ acquires a lock on data item $A$ in memory, and then attempts to read data item $B$ which is not in the buffer pool, $T$ must suspend execution and wait for disk I/O.
  While $T$ is asleep waiting for disk I/O:
  - It continues to **hold the lock on $A$**.
  - Any other transaction needing $A$ is forced to wait, creating massive lock queues and system-wide throughput collapse.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Deconstruct the Proposed Two-Phase Technique
The proposed execution model operates in two successive passes:
1. **Pass 1 (Speculative Dry-Run / Buffer Pre-Warming):**
   - The transaction executes its business logic in a private local workspace.
   - It acquires **zero locks** from the lock manager.
   - It performs **no physical writes** to the database or log.
   - Whenever it touches a data item that is not present in the buffer pool, the database buffer manager issues asynchronous disk read requests and loads the required disk pages into main memory.
2. **Pass 2 (Execution under Strict 2PL):**
   - The transaction restarts and executes normally following Strict 2PL.
   - It acquires locks, performs updates, writes to the log, and commits.

##### Step 2: Analyze the Latency and Lock Holding Durations
Let transaction $T$ access $k$ distinct disk pages that are not cached in the buffer pool. Let $T_{\text{I/O}} \approx 10\,\text{ms}$ be the average disk I/O latency, and let $T_{\text{CPU}} \approx 10\,\mu\text{s}$ be the CPU processing time.

###### Under Standard Strict 2PL:
- $T$ acquires a lock on page 1, then waits $10\,\text{ms}$ for page 2 to load from disk.
- Total lock holding duration for page 1 is:
  $$
  D_{\text{standard}} \approx k \times T_{\text{I/O}} \approx k \times 10\,\text{ms}
  $$
- Other concurrent transactions requiring page 1 are blocked for tens of milliseconds.

###### Under the Speculative Dry-Run Technique:
- **During Pass 1:** $T$ incurs all $k \times T_{\text{I/O}}$ disk wait penalties. However, because $T$ holds **zero locks**, **it blocks absolutely no other transactions**.
- **During Pass 2:** All $k$ pages are already resident in the high-speed buffer pool (cache hits).
- $T$ executes entirely at memory speed:
  $$
  D_{\text{dry-run}} \approx k \times T_{\text{CPU}} \approx k \times 10\,\mu\text{s}
  $$
- Locks are acquired and held only for microseconds instead of milliseconds!

```text
Standard Strict 2PL:
[Lock Acquired] === WAITING FOR DISK I/O (10 ms) === [Lock Released at Commit]
  ^---- Lock held for 10+ ms; blocks all conflicting transactions ----^

Proposed Speculative Technique:
Pass 1: === FETCH DISK PAGES INTO BUFFER POOL (10 ms) === (NO LOCKS HELD!)
Pass 2: [Lock] = FAST MEMORY EXEC (10 µs) = [Commit & Unlock]
          ^-- Lock held for 10 µs only! (1000x shorter holding time) --^
```

##### Step 3: Quantify Concurrency and Contention Benefits
- **Exponential Contention Reduction:** By the queuing theory of lock contention (e.g., the Gray-Reuter model), probability of lock conflict is proportional to the square of lock holding time:
  $$
  \text{Conflict Probability} \propto (D_{\text{lock}})^2
  $$
  Reducing lock holding duration from $10\,\text{ms}$ to $10\,\mu\text{s}$ ($1,000\times$ reduction) slashes conflict probability by a factor of nearly $1,000,000\times$!
- **Zero Abort Overhead compared to Optimistic OCC:**
  Unlike validation-based OCC, which validates at commit time and aborts if a conflict occurred (wasting all computed work), this technique never performs optimistic commit. It simply re-runs under Strict 2PL, ensuring strict serializability without cascade risks.

##### Step 4: Trade-Off Analysis
- **Disadvantage:** Duplicate CPU execution (running the application logic twice).
- **Justification:** In modern database engines, CPU cycles are abundant and cheap, whereas disk I/O and lock contention are the dominant system bottlenecks. Pre-warming the cache completely justifies the minor CPU cost.

---

#### 3. RUET Exam Insights & Examiner Notes

- **Examiner's Core Grading Criterion:** The hint says *"Consider waits for disk I/O."* Your answer must explicitly contrast lock holding duration during disk page faults versus in-memory execution.
- **Key Metric to State:** Lock holding duration drops from milliseconds ($10^{-3}\,\text{s}$) to microseconds ($10^{-6}\,\text{s}$), eliminating lock contention convoys.

---

### Exercise 18.14 · Early Lock Release in $\text{B}^+$-Tree Concurrency (Safe Nodes & Latch Crabbing)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.14, Page 901.
> - **Type:** Practice Exercise (Index Concurrency & Tree Protocols).
> - **Difficulty Rating:** ⭐⭐⭐⭐ (Medium-Hard).
> - **RUET Exam Mapping:** Directly tests tree-locking protocols and latch crabbing in $\text{B}^+$-tree index structures (Unit 6 & Unit 8).

**Question (Silberschatz 7e Exercise 18.14).**  
Suppose that we use the tree protocol of Section 18.1.5 to manage concurrent access to a $\text{B}^+$-tree. Since a split may occur on an insert that affects the root, it appears that an insert operation cannot release any locks until it has completed the entire operation. Under what circumstances is it possible to release a lock earlier?

---

#### 1. Core Principles & Concept Overview

- **$\text{B}^+$-Tree Structural Invariant:**
  - In a $\text{B}^+$-tree of order $M$, every internal node contains at most $M-1$ search keys and $M$ child pointers.
  - An insertion occurs at a leaf node. If the leaf already contains $M-1$ keys, it **splits**, pushing a median key and a new child pointer up into its parent.
  - If the parent is also full ($M-1$ keys), the split cascades upward, potentially propagating all the way to the root.
- **The Root Contention Problem:**
  If an insert transaction must retain an exclusive lock on the root until the entire insert completes, **all concurrent operations (searches, inserts, deletes) across the entire database are completely blocked at the root**, devastating throughput.
- **Latch Crabbing / Lock Coupling:** A top-down traversal protocol where an operation acquires a lock on a child node before releasing the lock on its parent.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Define the Concept of a "Safe Node"
A node in a $\text{B}^+$-tree is defined as **safe** with respect to an insertion if an insertion into its subtree cannot cause this node to split:
- **Definition (Safe for Insert):** A node $N$ is **safe for insertion** if it currently contains strictly fewer than the maximum permitted number of entries:
  $$
  \text{Entries}(N) \le M - 2 \quad (\text{i.e., has space for at least one more key without splitting})
  $$

##### Step 2: The Split Isolation Property
If an insertion operation descends down a branch of the $\text{B}^+$-tree and encounters a node $N$ that is **safe**:
1. Even if all descendants below $N$ (children, grandchildren, leaf) are completely full and split all the way up, the split cascade will insert at most one new key into $N$.
2. Because $N$ has room to accommodate that new key, **$N$ will absorb the split and will NOT split itself**.
3. Therefore, no structural modification can ever propagate above node $N$ into $N$'s parent or any ancestor.

##### Step 3: The Early Lock Release Condition
During the downward traversal of the $\text{B}^+$-tree for an insert operation:
1. The transaction locks the root in Exclusive ($X$) mode.
2. It locks the appropriate child node $C$ in $X$ mode before releasing the lock on the parent (crabbing).
3. **Early Release Trigger:** The moment the transaction locks a child node $C$ and examines its header:
   - **If $C$ is SAFE ($\text{Keys}(C) < M - 1$):**
     The transaction can **immediately release all locks held on all ancestors of $C$** (including the root and all intermediate nodes between the root and $C$'s parent)!
   - **If $C$ is FULL ($\text{Keys}(C) = M - 1$):**
     $C$ is unsafe. The transaction must retain locks on $C$'s ancestors, because a split from below might cascade through $C$ into its parent.

```text
Traversal Example (Order M = 4, Max Keys = 3):

           [ Root: 1 Key ]  <-- SAFE! (1 < 3)
              /          \
     [ Node A: 3 Keys ]   ...
        /             \
[ Leaf 1: 3 Keys ]  [ Leaf 2: 2 Keys ]

1. Insert targets Leaf 1:
   - Lock Root (X). Root has 1 key (SAFE).
   - Lock Node A (X). Node A has 3 keys (UNSAFE / FULL).
     -> Cannot release Root lock yet!
   - Lock Leaf 1 (X). Leaf 1 has 3 keys (UNSAFE / FULL).
     -> Must retain locks on Root, Node A, and Leaf 1 (split propagates to root).

2. Insert targets Leaf 2:
   - Lock Root (X). Root has 1 key (SAFE).
   - Lock Node A (X). Node A has 3 keys (UNSAFE).
   - Lock Leaf 2 (X). Leaf 2 has 2 keys (SAFE! 2 < 3).
     -> RELEASE ALL ANCESTOR LOCKS IMMEDIATELY (Unlock Root and Node A)!
     -> Only Leaf 2 remains locked during the insert.
```

##### Step 4: Practical Concurrency Impact
- In real-world $\text{B}^+$-trees, the fanout $M$ is typically between $50$ and $200$.
- Nodes are full only a tiny fraction of the time ($\approx 1/M$ probability).
- Consequently, an insert operation almost always encounters a safe node within the first 1 or 2 levels below the root.
- The exclusive lock on the root is released after just a few memory/pointer operations, reducing root lock hold times by over $99\%$ and enabling massive concurrent throughput.

---

#### 3. RUET Exam Insights & Examiner Notes

- **Examiner's Keyword Requirement:** You must use the formal term **Safe Node** and define it mathematically ($\text{Keys} < M - 1$).
- **Complementary Rule for Delete:** In oral exams or viva, teachers often ask: *"What is a safe node for deletion?"*  
  *(Answer: A node that contains strictly more than the minimum allowed entries $\lceil M/2 \rceil - 1$, so it cannot cause underflow/coalescing).*

---

### Exercise 18.15 · Validation Mechanisms in Snapshot Isolation (FCW vs. FUW)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.15, Page 901.
> - **Type:** Practice Exercise (Detailed Systems Algorithm Design).
> - **Difficulty Rating:** ⭐⭐⭐⭐⭐ (Hard).
> - **RUET Exam Mapping:** Core modern transaction processing topic; tests Snapshot Isolation validation algorithms and write-write conflict resolution.

**Question (Silberschatz 7e Exercise 18.15).**  
The snapshot isolation protocol uses a validation step which, before performing a write of a data item by transaction $T$, checks if a transaction concurrent with $T$ has already written the data item.

a. A straightforward implementation uses a start timestamp and a commit timestamp for each transaction, in addition to an *update set*, that is, the set of data items updated by the transaction. Explain how to perform validation for the first-committer-wins scheme by using the transaction timestamps along with the update sets. You may assume that validation and other commit processing steps are executed serially, that is, for one transaction at a time.  
b. Explain how the validation step can be implemented as part of commit processing for the first-committer-wins scheme, using a modification of the above scheme, where instead of using update sets, each data item has a write timestamp associated with it. Again, you may assume that validation and other commit processing steps are executed serially.  
c. The first-updater-wins scheme can be implemented using timestamps as described above, except that validation is done immediately after acquiring an exclusive lock, instead of being done at commit time.  
   i. Explain how to assign write timestamps to data items to implement the first-updater-wins scheme.  
   ii. Show that as a result of locking, if the validation is repeated at commit time the result would not change.  
   iii. Explain why there is no need to perform validation and other commit processing steps serially in this case.

---

#### 1. Core Principles & Concept Overview

- **Snapshot Isolation (SI):**
  - When transaction $T$ begins, it is assigned $\text{Start-TS}(T)$.
  - $T$ reads data from the committed snapshot of the database at time $\text{Start-TS}(T)$.
  - Writes are buffered in $T$'s private workspace until commit.
- **Write-Write Conflict Resolution:**
  - **First-Committer-Wins (FCW):** Transactions update privately; at commit time, the first concurrent transaction to commit succeeds; any subsequent concurrent transaction trying to commit updates to the same item is aborted.
  - **First-Updater-Wins (FUW):** A transaction acquires an exclusive lock when it first attempts to update a data item. If another concurrent transaction already updated it, it aborts immediately.

---

#### 2. Detailed Step-by-Step Solution

##### Part (a): First-Committer-Wins (FCW) using Update Sets

###### Step 1: Timestamp & State Representation
- Each transaction $T$ is assigned a start timestamp $\text{Start-TS}(T)$ when it begins.
- When $T$ attempts to commit, it enters a critical section (serial commit processing).
- Let $W(T)$ denote the **update set** (write set) of data items modified by $T$.

###### Step 2: Validation Algorithm
To validate transaction $T$:
1. Identify all transactions $T_k$ that committed *after* $T$ started, but *before* $T$ attempts to commit:
   $$
   \text{Start-TS}(T) < \text{Commit-TS}(T_k) < \text{Current-Time}
   $$
2. For every such committed concurrent transaction $T_k$, compute the set intersection of their update sets:
   $$
   \text{Conflict Check} = W(T) \cap W(T_k)
   $$
3. **Decision Rule:**
   - If $W(T) \cap W(T_k) \ne \emptyset$ for any such $T_k$:  
     **Validation FAILS.** Transaction $T$ is aborted (first-committer-wins rule violated).
   - If $W(T) \cap W(T_k) = \emptyset$ for all such $T_k$:  
     **Validation SUCCEEDS.** $T$ is assigned $\text{Commit-TS}(T) = \text{Current-Time}$, its updates $W(T)$ are written to the database, and $T$ commits.

---

##### Part (b): First-Committer-Wins (FCW) using Per-Item Write Timestamps

###### Step 1: Data Structure Modification
- Eliminate the historical list of transaction update sets.
- Associate with each data item $Q$ a scalar attribute: $\text{W-TS}(Q)$, representing the commit timestamp of the transaction that last wrote $Q$.

###### Step 2: Validation Algorithm at Commit Time
Under serial commit processing:
1. When transaction $T$ enters commit processing, evaluate its update set $W(T)$.
2. For each data item $Q \in W(T)$, check whether $Q$ was updated after $T$ took its snapshot:
   $$
   \text{W-TS}(Q) > \text{Start-TS}(T)
   $$
3. **Decision Rule:**
   - If $\exists Q \in W(T)$ such that $\text{W-TS}(Q) > \text{Start-TS}(T)$:  
     Another transaction has committed an update to $Q$ during $T$'s lifetime. **Validation FAILS**, and $T$ is aborted.
   - If $\forall Q \in W(T)$, $\text{W-TS}(Q) < \text{Start-TS}(T)$:  
     **Validation SUCCEEDS.**
     1. Assign $T$ a new timestamp $\text{Commit-TS}(T) = \text{Current-Time}$.
     2. For each $Q \in W(T)$, set $\text{W-TS}(Q) := \text{Commit-TS}(T)$ and write the new value.
     3. Commit transaction $T$.

---

##### Part (c): First-Updater-Wins (FUW) via Exclusive Locking

###### Sub-part (i): Write Timestamp Assignment
1. When transaction $T$ executes its first write to data item $Q$, it must immediately request and acquire an **Exclusive Lock ($X$) on $Q$**.
2. Immediately upon acquiring the lock, $T$ validates item $Q$:
   - Checks if $\text{W-TS}(Q) > \text{Start-TS}(T)$.
   - If true, another transaction committed an update to $Q$ after $T$ started. $T$ immediately aborts and releases its lock.
   - If false, validation passes. $T$ buffers its update locally.
3. **Timestamp Assignment:** The timestamp $\text{W-TS}(Q)$ is updated to $\text{Commit-TS}(T)$ **at the time $T$ commits**, immediately before releasing the exclusive lock on $Q$.

###### Sub-part (ii): Invariance of Validation at Commit Time
- Suppose transaction $T$ validated $Q$ upon acquiring the lock, satisfying:
  $$
  \text{W-TS}(Q) < \text{Start-TS}(T)
  $$
- From the instant $T$ acquires the exclusive lock on $Q$ until the instant $T$ commits, **$T$ continuously holds the exclusive lock on $Q$**.
- Because the lock is exclusive, **no other transaction can acquire a lock or write to $Q$** during this interval.
- Consequently, the physical value of $\text{W-TS}(Q)$ cannot be modified by any other transaction while $T$ holds the lock.
- Therefore, if the validation condition $\text{W-TS}(Q) < \text{Start-TS}(T)$ were to be re-evaluated at commit time, it is mathematically guaranteed to yield the exact same True result. Re-validation is completely redundant.

###### Sub-part (iii): Eliminating the Serial Commit Bottleneck
- In schemes (a) and (b), commit validation was global and lockless. If two transactions committed concurrently, they could simultaneously validate overlapping sets without observing each other's pending writes, leading to lost updates. Hence, commit processing had to be centralized and strictly serial.
- In scheme (c), **mutual exclusion is enforced at the granular data-item level via exclusive locks**:
  - If two concurrent transactions attempt to write the *same* item $Q$, the second transaction is blocked at lock acquisition time, perfectly serializing their conflict checks on $Q$.
  - If two transactions update completely *disjoint* data items, their validations and writes are completely independent and can execute concurrently across multiple CPU cores without any risk of interference.
- Therefore, there is no need for a global serial commit critical section, removing the central bottleneck and enabling massive scalability. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes

- **Examiner Comparison Checklist:**
  - **FCW:** Aborts at commit time; detects conflicts late.
  - **FUW:** Aborts at write time (lock acquisition); detects conflicts early, avoiding wasted work.
  - **Locking Benefit:** Exclusive locks transform global serialization into independent fine-grained locks.

---

### Exercise 18.16 · Latch-Free Data Structures, the ABA Problem, and Atomic CAS/DCAS

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Practice Exercise 18.16, Pages 901–902.
> - **Type:** Practice Exercise (Low-Level Lock-Free Concurrency & CPU Architecture).
> - **Difficulty Rating:** ⭐⭐⭐⭐⭐ (Hard).
> - **RUET Exam Mapping:** Directly tests advanced multi-core in-memory database engine topics (Silberschatz Section 18.8 / Unit 8).

**Question (Silberschatz 7e Exercise 18.16).**  
Consider functions $\text{insert\_latchfree}()$ and $\text{delete\_latchfree}()$, shown in Figure 18.23.

a. Explain how the ABA problem can occur if a deleted node is reinserted.  
b. Suppose that adjacent to *head* we store a counter *cnt*. Also suppose that $\text{DCAS}((head, cnt), (oldhead, oldcnt), (newhead, newcnt))$ atomically performs a compare-and-swap on the 128 bit value $(head, cnt)$. Modify the $\text{insert\_latchfree}()$ and $\text{delete\_latchfree}()$ to use the DCAS operation to avoid the ABA problem.  
c. Since most processors use only 48 bits of a 64 bit address to actually address memory, explain how the other 16 bits can be used to implement a counter, in case the DCAS operation is not supported.

---

#### 1. Core Principles & Concept Overview

- **Latch-Free (Lock-Free) Stack (Treiber Stack):**
  Uses the hardware atomic primitive $\text{CAS}(\&var, oldval, newval)$:
  - If $*var == oldval$, sets $*var = newval$ and returns True.
  - Otherwise, leaves $*var$ unchanged and returns False.
- **Figure 18.23 Baseline Code:**
```c
void insert_latchfree(Node* n) {
    do {
        oldhead = head;
        n->next = oldhead;
    } while (!CAS(&head, oldhead, n));
}

Node* delete_latchfree() {
    do {
        oldhead = head;
        if (oldhead == NULL) return NULL;
        newhead = oldhead->next;
    } while (!CAS(&head, oldhead, newhead));
    return oldhead;
}
```

---

#### 2. Detailed Step-by-Step Solution

##### Part (a): Step-by-Step Manifestation of the ABA Problem

###### Initial State:
The concurrent stack consists of three nodes:
$$
\text{head} \longrightarrow A \longrightarrow B \longrightarrow C \longrightarrow \text{NULL}
$$

###### Step 1: Thread 1 Initiates Deletion and is Preempted
1. Thread $T_1$ calls `delete_latchfree()`.
2. $T_1$ reads `oldhead = head` (which points to node $A$).
3. $T_1$ reads `newhead = oldhead->next` (which points to node $B$).
4. **Preemption:** Right before executing `CAS(&head, oldhead, newhead)`, Thread $T_1$ is descheduled by the operating system.

###### Step 2: Thread 2 Deletes Nodes A and B
1. Thread $T_2$ runs and calls `delete_latchfree()`. It successfully pops node $A$.
   $$
   \text{Stack: } \text{head} \longrightarrow B \longrightarrow C \longrightarrow \text{NULL}
   $$
2. Thread $T_2$ calls `delete_latchfree()` again. It successfully pops node $B$. Node $B$ is deallocated/freed.
   $$
   \text{Stack: } \text{head} \longrightarrow C \longrightarrow \text{NULL}
   $$

###### Step 3: Node A is Reinserted
1. Node $A$ (or newly allocated memory at the identical address $A$) is re-pushed onto the stack by Thread $T_2$ via `insert_latchfree(A)`.
2. Node $A$'s next pointer is set to point to $C$:
   $$
   \text{Stack: } \text{head} \longrightarrow A \longrightarrow C \longrightarrow \text{NULL}
   $$

###### Step 4: Thread 1 Resumes and Corrupts the Data Structure
1. Thread $T_1$ wakes up and finally executes its pending instruction:
   $$
   \text{CAS}(\&head, \text{oldhead}, \text{newhead}) \quad \text{where } \text{oldhead} = A, \text{ newhead} = B
   $$
2. The CPU compares $*head$ with $oldhead$. Because the head pointer currently points to $A$, **the comparison evaluates to TRUE!**
3. The CAS succeeds and assigns:
   $$
   \text{head} := B
   $$
4. **Catastrophic Failure:**
   - Node $B$ was already deleted and freed (its memory may be corrupted or unmapped).
   - Node $C$ is completely severed from the stack and leaked.
   - The stack is now corrupted, pointing to invalid memory ($B$). This is the **ABA Problem** (value was $A$, changed to $B$, and restored to $A$, fooling CAS).

---

##### Part (b): Solution using Double Compare-And-Swap (DCAS)

To prevent the ABA problem, we pair the `head` pointer with a monotonically increasing 64-bit integer counter `cnt`. A 128-bit atomic `DCAS` primitive verifies both simultaneously.

###### Modified `insert_latchfree`:
```c
void insert_latchfree(Node* n) {
    Node* oldhead;
    uint64_t oldcnt;
    do {
        oldhead = head;
        oldcnt = cnt;
        n->next = oldhead;
    } while (!DCAS((&head, &cnt), 
                   (oldhead, oldcnt), 
                   (n, oldcnt + 1)));
}
```

###### Modified `delete_latchfree`:
```c
Node* delete_latchfree() {
    Node* oldhead;
    Node* newhead;
    uint64_t oldcnt;
    do {
        oldhead = head;
        oldcnt = cnt;
        if (oldhead == NULL) 
            return NULL;
        newhead = oldhead->next;
    } while (!DCAS((&head, &cnt), 
                   (oldhead, oldcnt), 
                   (newhead, oldcnt + 1)));
    return oldhead;
}
```

###### Why DCAS Solves the Problem:
In the ABA scenario, even though the pointer value changed from $A \to B \to A$, the counter incremented on every operation:
$$
\text{State: } (A, 100) \longrightarrow (B, 101) \longrightarrow (C, 102) \longrightarrow (A, 103)
$$
When Thread $T_1$ attempts `DCAS` with its expected value $(A, 100)$, the comparison fails because $103 \ne 100$. The operation safely aborts and retries.

---

##### Part (c): 16-Bit Tagged Pointers in 48-Bit Virtual Address Space

###### Hardware Architectural Background:
In modern 64-bit architectures (such as x86-64 and ARMv8-A), virtual address translation uses only the lower **48 bits** (supporting $256\,\text{TB}$ of address space). The upper **16 bits** (bits 48 to 63) are unused for addressing.

###### Tagged Pointer Implementation:
We can pack a 16-bit version counter directly into the unused upper 16 bits of a single 64-bit pointer, allowing the algorithm to run using standard, universally available **64-bit single-word CAS** (`CMPXCHG` on x86-64):

1. **Packing:**
   $$
   \text{tagged\_head} = \left(\text{counter} \ll 48\right) \;\mathbin{\vert}\; \left(\text{raw\_pointer} \;\mathbin{\&}\; \text{0x0000FFFFFFFFFFFF}\right)
   $$
2. **Unpacking Pointer (Dereferencing):**
   $$
   \text{raw\_pointer} = \text{tagged\_head} \;\mathbin{\&}\; \text{0x0000FFFFFFFFFFFF}
   $$
3. **Unpacking Counter:**
   $$
   \text{counter} = \text{tagged\_head} \gg 48
   $$
4. **Atomic Update:**
   When performing CAS, compute:
   $$
   \text{new\_tagged} = \left((\text{old\_counter} + 1) \ll 48\right) \;\mathbin{\vert}\; \text{new\_pointer}
   $$
   Execute single 64-bit `CAS(&tagged_head, old_tagged, new_tagged)`.

Because the 16-bit counter increments on every update, any cycle ($A \to B \to A$) will result in a mismatched tag in the upper 16 bits, causing standard 64-bit CAS to detect the modification and fail safely without requiring hardware 128-bit DCAS support. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes

- **Diagram Advice:** Draw the 3-step sequence showing Thread 1 holding $(A, B)$, Thread 2 popping $A$ and $B$ and reinserting $A$, and Thread 1 committing dangling pointer $B$.
- **Bitwise Precision:** Stating that x86-64 uses only 48 bits for virtual addressing demonstrates elite technical competence and guarantees full marks on system implementation questions.

---

### Exercise 18.19 · Non-Serializability of the Forest Protocol

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Exercise 18.19, Pages 902–903.
> - **Type:** Regular Exercise (Counterexample & Protocol Flaw Proof).
> - **Difficulty Rating:** ⭐⭐⭐⭐ (Medium-Hard).
> - **RUET Exam Mapping:** Standard theoretical question testing why the tree protocol requires a single root and why relaxing it to a forest destroys serializability.

**Question (Silberschatz 7e Exercise 18.19).**  
Consider a variant of the tree protocol called the *forest* protocol. The database is organized as a forest of rooted trees. Each transaction $T_i$ must follow the following rules:
- The first lock in each tree may be on any data item.
- The second, and all subsequent, locks in a tree may be requested only if the parent of the requested node is currently locked.
- Data items may be unlocked at any time.
- A data item may not be relocked by $T_i$ after it has been unlocked by $T_i$.

Show that the forest protocol does *not* ensure serializability.

---

#### 1. Core Principles & Concept Overview

- **Standard Tree Protocol Invariant:**
  The standard tree protocol operates on a **single rooted tree**. It guarantees conflict serializability because transactions can be serialized according to the order in which they lock the unique root (or common ancestor) of the tree.
- **The Forest Protocol Flaw:**
  A forest consists of multiple disjoint trees with **no shared root or common ancestor**.
  If a transaction can lock items in Tree 1, unlock them, and then begin locking items in Tree 2, it can interleave with another transaction to form an alternating cyclic dependency between the two trees.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Construct a Minimal Database Forest
Let the database consist of a forest with two completely disjoint trees:
- **Tree 1:** Consists of a single root node $A$.
- **Tree 2:** Consists of a single root node $B$.

*(Note: To show the generality of the proof, even if Tree 1 had child nodes $A \to A_1$ and Tree 2 had child nodes $B \to B_1$, the failure occurs at the root level).*

##### Step 2: Define Two Concurrent Transactions
- Transaction $T_1$ updates both $A$ and $B$:
  $$
  T_1: \quad \text{write}(A); \quad \text{write}(B)
  $$
- Transaction $T_2$ updates both $A$ and $B$:
  $$
  T_2: \quad \text{write}(A); \quad \text{write}(B)
  $$

##### Step 3: Construct the Interleaved Execution Schedule $S$
Consider the following chronological schedule of lock and data operations:

| Step | Transaction | Operation Executed | Rule Compliance Check under Forest Protocol |
| :---: | :---: | :--- | :--- |
| **1** | $T_1$ | $\text{lock-X}(A)$ | **Rule 1:** First lock in Tree 1; can be on any item ($A$). |
| **2** | $T_1$ | $\text{write}(A)$ | Executes write on $A$. |
| **3** | $T_1$ | $\text{unlock}(A)$ | **Rule 3:** Data items may be unlocked at any time. |
| **4** | $T_2$ | $\text{lock-X}(A)$ | **Rule 1:** First lock in Tree 1 for $T_2$; granted since $A$ is free. |
| **5** | $T_2$ | $\text{write}(A)$ | Executes write on $A$. |
| **6** | $T_2$ | $\text{lock-X}(B)$ | **Rule 1:** First lock in Tree 2 for $T_2$; can be on any item ($B$). |
| **7** | $T_2$ | $\text{write}(B)$ | Executes write on $B$. |
| **8** | $T_2$ | $\text{unlock}(A)$ | **Rule 3:** Unlocks $A$. |
| **9** | $T_2$ | $\text{unlock}(B)$ | **Rule 3:** Unlocks $B$. |
| **10** | $T_1$ | $\text{lock-X}(B)$ | **Rule 1:** First lock in Tree 2 for $T_1$; valid! |
| **11** | $T_1$ | $\text{write}(B)$ | Executes write on $B$. |
| **12** | $T_1$ | $\text{unlock}(B)$ | **Rule 3:** Unlocks $B$. |

##### Step 4: Verify Complete Compliance with Forest Protocol Rules
Let us verify every rule of the Forest Protocol for both transactions:
1. **Rule 1 (First lock in each tree):**
   - For $T_1$: First lock in Tree 1 was on $A$ (Step 1). First lock in Tree 2 was on $B$ (Step 10). Both valid.
   - For $T_2$: First lock in Tree 1 was on $A$ (Step 4). First lock in Tree 2 was on $B$ (Step 6). Both valid.
2. **Rule 2 (Subsequent locks require locked parent):**
   - No subsequent locks were requested within either tree. Valid.
3. **Rule 3 (Unlock at any time):**
   - Both transactions unlocked items at valid times. Valid.
4. **Rule 4 (No relocking of unlocked items):**
   - $T_1$ locked $A$, unlocked $A$, and never relocked $A$.
   - $T_1$ locked $B$, unlocked $B$, and never relocked $B$.
   - $T_2$ locked $A$ and $B$, unlocked both, and never relocked either. Valid.

**Both transactions adhere 100% strictly to the rules of the Forest Protocol.**

##### Step 5: Construct the Precedence Graph
Now examine the conflicting operations in schedule $S$:
1. **Conflict on Item $A$:**
   $T_1$ wrote $A$ (Step 2) before $T_2$ wrote $A$ (Step 5).
   $$
   \implies \text{Directed edge: } T_1 \longrightarrow T_2
   $$
2. **Conflict on Item $B$:**
   $T_2$ wrote $B$ (Step 7) before $T_1$ wrote $B$ (Step 11).
   $$
   \implies \text{Directed edge: } T_2 \longrightarrow T_1
   $$

The precedence graph $G(S)$ contains the directed cycle:
$$
T_1 \rightleftharpoons T_2
$$

Because the precedence graph contains a cycle, **the schedule $S$ is NOT conflict serializable**.

##### Step 6: Theoretical Root Cause Analysis
Why does the tree protocol guarantee serializability on a single tree, but fail on a forest?
- In a single tree, every pair of conflicting transactions must cross a common ancestor (at least the root). The transaction that locks the common ancestor first is guaranteed to precede the other across all nodes in the tree.
- In a forest, there is **no common ancestor** linking Tree 1 and Tree 2. Transaction $T_1$ can enter its shrinking phase in Tree 1 (releasing $A$) and subsequently enter a growing phase in Tree 2 (locking $B$), effectively violating the two-phase property across the global database. $\blacksquare$

---

#### 3. RUET Exam Insights & Examiner Notes

- **Exam Strategy:** Never write an abstract prose argument for this question. Construct the exact 2-transaction, 2-tree table shown above.
- **Marking Key:** Examiners look specifically for:
  1. The step-by-step trace showing where $T_1$ unlocks $A$ before locking $B$.
  2. The explicit identification of edges $T_1 \to T_2$ (on $A$) and $T_2 \to T_1$ (on $B$).
  3. The final conclusion that $G(S)$ contains a cycle.

---

### Exercise 18.22 · Implicit vs. Explicit Locking in Multiple-Granularity Protocols

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 18 (*Concurrency Control*), Exercise 18.22, Page 902.
> - **Type:** Regular Exercise (Conceptual & Algorithmic Comparison).
> - **Difficulty Rating:** ⭐⭐ (Easy-Medium).
> - **RUET Exam Mapping:** Standard 3-to-4 mark definition/distinction question in Unit 6 semester finals.

**Question (Silberschatz 7e Exercise 18.22).**  
In multiple-granularity locking, what is the difference between implicit and explicit locking?

---

#### 1. Core Principles & Concept Overview

In a multiple-granularity locking (MGL) hierarchy:
$$
\text{Database} \longrightarrow \text{Area} \longrightarrow \text{Relation} \longrightarrow \text{Page} \longrightarrow \text{Record / Tuple}
$$
A transaction can lock a node at any level of the tree. The protocol distinguishes sharply between locks explicitly registered with the lock manager and locks logically inherited down the tree hierarchy.

---

#### 2. Detailed Step-by-Step Solution

##### Step 1: Definition of Explicit Locking
- **Definition:** An **explicit lock** is a lock that a transaction directly and intentionally requests on a specific node $Q$ by issuing a formal lock request (`lock-S`, `lock-X`, `lock-IS`, `lock-IX`, or `lock-SIX`) to the DBMS lock manager.
- **Physical Representation:** An explicit lock results in an actual, tangible **lock table entry** allocated in memory, mapping the resource identifier of node $Q$ to the transaction ID, granted mode, and waiting queue.
- **Example:** Transaction $T$ issues `lock-X(R)` on Relation $R$. An entry is added to the lock manager hash table: `[Resource: Relation R, Lock Mode: X, Holder: T]`.

##### Step 2: Definition of Implicit Locking
- **Definition:** An **implicit lock** is a lock that is **logically inherited** by a node $Q$ as a direct consequence of an explicit lock held by the transaction on one of $Q$'s **ancestor nodes** in the hierarchy.
- **Physical Representation:** **Zero memory is allocated in the lock table** for node $Q$. The lock manager does not create an entry for $Q$. Instead, node $Q$'s locked status is deduced dynamically by checking the locks held on its ancestors.
- **Inheritance Semantics:**
  - If transaction $T$ holds an explicit **Shared ($S$) lock** on Relation $R$, all pages and all tuples inside $R$ are **implicitly locked in Shared ($S$) mode** by $T$. $T$ can read any tuple in $R$ without requesting individual locks.
  - If transaction $T$ holds an explicit **Exclusive ($X$) lock** on Relation $R$, all pages and all tuples inside $R$ are **implicitly locked in Exclusive ($X$) mode** by $T$. $T$ can read and modify any tuple in $R$ without requesting individual locks.

##### Step 3: Conflict Detection Mechanism between Explicit and Implicit Locks
When another transaction $T_j$ wishes to explicitly lock a fine-grained node (e.g., tuple $t$):
1. **Checking for Incompatible Implicit Locks:**
   $T_j$ cannot simply check if an entry exists for $t$ in the lock table. It must traverse the tree path upward from $t$ to the root, inspecting the lock table for any **ancestor** holding an incompatible explicit lock ($S$ or $X$).
2. **Checking for Incompatible Explicit Locks at Lower Levels:**
   Conversely, when a transaction $T_k$ attempts to explicitly lock a coarse node (e.g., Relation $R$) in $X$ mode, it does not need to scan millions of individual tuples to see if any are explicitly locked. It simply checks if any transaction holds an **Intention Lock ($IS$ or $IX$)** directly on Relation $R$. If none do, no descendant tuple can be explicitly locked!

---

##### Summary Comparison: Explicit vs. Implicit Locking

| Dimension | Explicit Locking | Implicit Locking |
| :--- | :--- | :--- |
| **Origin / Mechanism** | Directly requested by transaction via lock call | Inherited automatically from ancestor nodes |
| **Lock Table Entry** | Yes (physical memory allocated in lock hash table) | **No** (purely logical; zero lock table footprint) |
| **Granularity Target** | Specifically targeted node (e.g., Relation $R$ or Tuple $t$) | All descendant nodes in the subtree below the locked ancestor |
| **Detection Method** | Direct hash lookup on the resource identifier | Traversal of ancestor path up to the tree root |
| **System Overhead** | High if applied to millions of fine items | **Zero memory overhead**; instant bulk locking |
| **Intended Workload** | Fine-grained OLTP point updates | Large table scans, bulk updates, report queries |

---

#### 3. RUET Exam Insights & Examiner Notes

- **Marking Distribution (04 Marks):**
  - Definition of Explicit Locking with lock table entry mention: **1.5 Marks**.
  - Definition of Implicit Locking with ancestor inheritance mention: **1.5 Marks**.
  - Conflict detection mechanism (why Intention locks exist): **1 Mark**.
- **Common Trap:** Do not confuse *implicit locking* with *automatic locking done by the SQL compiler*. In DBMS literature and Silberschatz Chapter 18, implicit locking strictly refers to the logical inheritance of locks down an MGL hierarchy!


---

[← Prev: T10](T10_Serializability.md) | [Index](00_Index.md) | [Next: T11 Part 2 →](T11_Part2_2PL_and_Lock_Conversions.md)
