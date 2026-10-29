---
title: "T11 · Concurrency Control Protocols · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T10 · Serializability](T10_Serializability.md) | [Explanation layer](../Topicwise_answers_explaination/T11_Concurrency_Control_Protocols.md) | [Next: T12 · Recovery System and RAID →](T12_Recovery_System_and_RAID.md)

---

# T11 · Concurrency Control Protocols

> [!info] Topic card
> **Syllabus:** Unit 6 · **Weight:** 37 final marks (5.8%) in 6/7 papers
> **Sources:** Deck 08 · Textbook Ch. 18 §18.1–18.2, §18.5
> **Blocks in this file:** 9 final questions (8 blocks, 1 L2 merge)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T11.1 | Lock-based protocols: shared/exclusive locks, compatibility matrix, starvation | 0 + 0 | No questions | [[#T11.1 · Lock-based protocols: shared/exclusive locks, compatibility matrix, starvation\|Go]] |
| T11.2 | Two-phase locking: growing/shrinking phases, lock point, inserting lock/unlock instructions | 9 + 0 | 2017 Q.6(b), 2017 Q.7(a) | [[#T11.2 · Two-phase locking: growing/shrinking phases, lock point, inserting lock/unlock instructions\|Go]] |
| T11.3 | Strict / rigorous 2PL; drawbacks of 2PL | 0 + 0 | No questions | [[#T11.3 · Strict / rigorous 2PL; drawbacks of 2PL\|Go]] |
| T11.4 | Deadlock: conditions, prevention vs detection, wait-for graph, victim selection | 17 + 0 | 2017 Q.7(b), 2018 Q.5(b), 2020 Q.7(a), 2021 Q.8(a) | [[#T11.4 · Deadlock: conditions, prevention vs detection, wait-for graph, victim selection\|Go]] |
| T11.5 | Wait-die vs wound-wait | 0 + 0 | No questions | [[#T11.5 · Wait-die vs wound-wait\|Go]] |
| T11.6 | Timestamp ordering: R-TS/W-TS rules, trace a schedule; rolled-back transaction gets a NEW timestamp | 11 + 0 | 2018 Q.6(b), 2023 Q.8(c), 2024 Q.8(b) | [[#T11.6 · Timestamp ordering: R-TS/W-TS rules, trace a schedule; rolled-back transaction gets a NEW timestamp\|Go]] |

---

## T11.1 · Lock-based protocols: shared/exclusive locks, compatibility matrix, starvation

*No questions from past finals or class tests.*

*See also:* [[#2017 Q.7(a) · 05 Marks]] (starvation definition).

---

## T11.2 · Two-phase locking: growing/shrinking phases, lock point, inserting lock/unlock instructions

### 2017 Q.6(b) · 04 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** How concurrent execution of transactions are controlled using two phase based locking protocol? Briefly discuss with an example.

**Answer.**

**Two-Phase Locking (2PL) Protocol:**  
The Two-Phase Locking protocol controls concurrent transactions by requiring each transaction to acquire and release locks in two separate, sequential phases:

1. **Growing Phase:**
   - A transaction may obtain new locks (shared or exclusive).
   - It can also convert a shared lock to an exclusive lock (upgrade).
   - A transaction cannot release any lock in this phase.
2. **Shrinking Phase:**
   - A transaction may release held locks.
   - It can convert an exclusive lock to a shared lock (downgrade).
   - A transaction cannot obtain any new locks in this phase.

**Lock Point:**  
The point in time where a transaction acquires its final lock is called its **lock point**. Once a transaction releases its first lock, the shrinking phase begins. The 2PL protocol guarantees conflict serializability. Transactions execute in the order of their lock points.

![Two-Phase Locking protocol growing and shrinking phases against time](../LectureSlides/diagrams/L08_p13_fig01.jpg)  
*Figure: Two-Phase Locking Protocol (Source: Deck 08, Slide 13)*

**Example:**  
Consider transaction $T_1$ transferring money between accounts $A$ and $B$:

```text
lock-S(A);         -- Growing phase begins
read(A);
lock-X(B);         -- Lock point (last lock acquired)
read(B);
B := B - 50;
write(B);
unlock(A);         -- Shrinking phase begins (no more locks allowed)
unlock(B);         -- Final unlock
```

Here, all locks are obtained before any lock is released. Therefore, $T_1$ follows 2PL and guarantees conflict serializability with concurrent transactions.

---

### 2017 Q.7(a) · 05 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** What is starvation? Consider the following two transactions.

**T1:**  
  `read(A);`  
  `read(B);`  
  `if A = 0 then B:=B+15% of B;`  
  `write(B);`

**T2:**  
  `read(B);`  
  `read(A);`  
  `if B = 0 then A:=A+20% of A;`  
  `write(A);`

Add lock and unlock instructions to transaction T1 and T2, so that they observe the two phase locking protocol. Can the execution of these transactions result in a deadlock? Justify.

**Answer.**

**Starvation:**  
Starvation occurs when a transaction waits indefinitely for a lock on a data item. This happens when a continuous stream of other concurrent transactions keeps obtaining compatible locks on that item. The waiting transaction cannot make progress.

**Adding 2PL Instructions to T1 and T2:**  
Under Two-Phase Locking (2PL), all lock acquisitions must precede all unlock operations. $T_1$ reads $A$ (needs shared lock) and updates $B$ (needs exclusive lock). $T_2$ reads $B$ (needs shared lock) and updates $A$ (needs exclusive lock).

**Transaction T1:**
```text
lock-S(A);
read(A);
lock-X(B);
read(B);
if A = 0 then B := B + 15% of B;
write(B);
unlock(A);
unlock(B);
```

**Transaction T2:**
```text
lock-S(B);
read(B);
lock-X(A);
read(A);
if B = 0 then A := A + 20% of A;
write(A);
unlock(B);
unlock(A);
```

**Deadlock Analysis and Justification:**  
**Yes, the execution of these transactions can result in a deadlock.**

**Justification:**  
Consider the following interleaved execution sequence:

1. $T_1$ executes `lock-S(A)` and `read(A)`. $T_1$ holds a shared lock on $A$.
2. $T_2$ executes `lock-S(B)` and `read(B)`. $T_2$ holds a shared lock on $B$.
3. $T_1$ issues `lock-X(B)`. Because exclusive mode conflicts with shared mode (by the lock-compatibility matrix, S and X are incompatible), $T_1$ must wait for $T_2$ to release $B$.
4. $T_2$ issues `lock-X(A)`. Because exclusive mode conflicts with shared mode (by the lock-compatibility matrix, S and X are incompatible), $T_2$ must wait for $T_1$ to release $A$.

Now, $T_1$ waits for $T_2$, and $T_2$ waits for $T_1$. Under 2PL, neither transaction can unlock an item before acquiring all locks. A circular wait occurs:

$$\text{Cycle: } T_1 \to T_2 \to T_1$$

Neither transaction can make progress. Thus, a deadlock occurs.

![Wait-for graph showing deadlock cycle T1 to T2 to T1](diagrams/T11_2017_Q7a_deadlock_wait_for_graph.jpg)  
*Figure: Interleaved execution and wait-for graph cycle producing deadlock between T1 and T2 under 2PL*

---

## T11.3 · Strict / rigorous 2PL; drawbacks of 2PL

*No questions from past finals or class tests.*

---

## T11.4 · Deadlock: conditions, prevention vs detection, wait-for graph, victim selection

### 2017 Q.7(b) · 04 Marks

*Section B · Asked in: 2017 · L1 (asked once)*

**Question.** Define deadlock. Explain how deadlock is prevented?

**Answer.**

**Deadlock:**  
A deadlock is a condition in which two or more transactions are waiting indefinitely for locks held by each other. None of the transactions can continue without external intervention.

**Deadlock Prevention Methods:**  
Deadlock prevention protocols ensure that the system never enters a deadlock state. Four standard schemes are:

1. **Pre-declaration (Pre-claiming All Locks):**  
   Each transaction must lock all required data items at once before execution begins. If any item is unavailable, no locks are granted and the transaction waits.  
   *Drawbacks:* Difficult to predict needed items beforehand. Data item usage is low.

2. **Lock Ordering:**  
   Impose a global ordering on all data items ($d_1 < d_2 < \dots < d_n$). A transaction can only request a lock on item $d_j$ if it already holds locks on items that precede $d_j$. Circular waits cannot form.

3. **Timestamp-Based Schemes (Preemption and Rollback):**  
   Each transaction $T_i$ is assigned a unique timestamp $\text{TS}(T_i)$ when it begins. The system compares timestamps to decide whether to wait or roll back:

   | Scheme | When $T_i$ requests item held by $T_j$ | Type |
   | :--- | :--- | :--- |
   | **Wait-Die** | If $T_i$ is older ($\text{TS}(T_i) < \text{TS}(T_j)$), $T_i$ **waits**.<br>If $T_i$ is younger ($\text{TS}(T_i) > \text{TS}(T_j)$), $T_i$ **dies** (rolls back). | Non-preemptive |
   | **Wound-Wait** | If $T_i$ is older ($\text{TS}(T_i) < \text{TS}(T_j)$), $T_i$ **wounds** $T_j$ ($T_j$ rolls back).<br>If $T_i$ is younger, $T_i$ **waits**. | Preemptive |

4. **Timeout-Based Scheme:**  
   A transaction waits for a lock for only a set amount of time. If the lock is not granted within the interval, the transaction times out and rolls back.

![Wait-for graph with cycle indicating deadlock](../LectureSlides/diagrams/L08_p24_fig02.jpg)  
*Figure: Wait-for Graph with a cycle indicating deadlock (Source: Deck 08, Slide 24)*

---

### 2018 Q.5(b) · 04 Marks

*Section B · Asked in: 2018 · L1 (asked once)*

**Question.** What do you know about deadlock in transaction management? Under what conditions it is less expensive to avoid deadlock than to allow deadlocks to occur and then to detect them?

**Answer.**

**Deadlock in Transaction Management:**  
A deadlock is an execution state where a set of transactions $\{T_1, T_2, \dots, T_n\}$ cannot proceed because each transaction waits for a lock held by another transaction in the set. A circular wait forms in the wait-for graph. The DBMS must intervene, select a victim transaction, and roll it back to break the cycle.

**When Avoidance / Prevention is Less Expensive Than Detection:**  
Deadlock avoidance or prevention is less expensive than detection and recovery under the following conditions:

1. **High Lock Contention (High Conflict Probability):**  
   When many concurrent transactions compete for the same data items, deadlocks occur frequently. Deadlock detection would repeatedly discover cycles, causing frequent, costly rollbacks. Prevention stops deadlocks before they happen.
2. **Long-Running or Resource-Intensive Transactions:**  
   Rolling back a transaction that has performed extensive computation or heavy disk writes wastes substantial system work. Prevention avoids deep rollbacks.
3. **High Overhead of Cycle Detection:**  
   Continuously maintaining wait-for graphs and running cycle-detection searches under heavy workloads adds CPU overhead. Prevention avoids this monitoring burden.

**When Detection is Less Expensive:**  
When deadlocks are **rare** (short transactions, low concurrency, mostly disjoint data items), detection is cheaper. Prevention mechanisms reduce concurrency or cause false-positive aborts. Detection allows transactions to run freely and resolves only the rare deadlock that occurs.

---

### 2020 Q.7(a) · 04 Marks

*Section B · Asked in: 2020 · L1 (asked once)*

**Question.** What is deadlock? Describe the time-shared locking protocol with example.

**Answer.**

*Assumption: "Time-shared locking protocol" is an exam misprint for the Two-Phase Locking (2PL) protocol.*

**Deadlock:**  
A deadlock is a situation where two or more transactions are in a mutual wait condition, each waiting for a data lock held by the other. Neither transaction can make progress.

**Two-Phase Locking (2PL) Protocol:**  
The Two-Phase Locking protocol ensures conflict serializability by requiring that each transaction acquires and releases locks in two distinct phases:

1. **Growing Phase:** A transaction may acquire locks (shared or exclusive) and upgrade locks ($\text{S} \to \text{X}$). It cannot release any locks.
2. **Shrinking Phase:** A transaction may release held locks and downgrade locks ($\text{X} \to \text{S}$). It cannot acquire any new locks.

**Lock Point:**  
The point where a transaction acquires its final lock is its **lock point**. Serializability is guaranteed in the order of transaction lock points.

![Two-Phase Locking growing and shrinking phases](../LectureSlides/diagrams/L08_p13_fig01.jpg)  
*Figure: Two-Phase Locking Protocol (Source: Deck 08, Slide 13)*

**Example:**  
Consider transaction $T_1$ modifying accounts $A$ and $B$:

| Step | Action | Phase |
| :---: | :--- | :--- |
| 1 | $\text{lock-S}(A)$; $\text{read}(A)$ | Growing |
| 2 | $\text{lock-X}(B)$; $\text{read}(B)$; $\text{write}(B)$ | Growing (**Lock Point**) |
| 3 | $\text{unlock}(A)$ | Shrinking begins |
| 4 | $\text{unlock}(B)$ | Shrinking |

$T_1$ obtains all locks before releasing any lock. This satisfies 2PL and guarantees serializability.

---

### 2021 Q.8(a) · 05 Marks

*Section B · CLO1 · Asked in: 2021 · L1 (asked once)*

**Question.** What is deadlock? Consider the following wait-for-graph:

![Wait-for-graph for Q.8(a)](../PreviousYearQuestion/diagrams/2021_p02_fig01.jpg)  
*Figure 2021_Q8.a — Wait-for-graph for deadlock detection (Source: Page 2, Q.8(a))*

Determine whether the schedule contains any deadlock or not.

**Answer.**

**Deadlock:**  
A deadlock is a state where each transaction in a set is waiting for a resource or data lock held by another transaction in that set. None of the transactions can continue execution.

**Analysis of the Wait-For Graph:**  
The given wait-for graph has:
- **Vertices (Transactions):** $V = \{T_1, T_2, T_3, T_4, T_5\}$
- **Directed Edges:** $E = \{(T_1, T_4), (T_1, T_2), (T_1, T_3), (T_4, T_5), (T_5, T_2), (T_2, T_4)\}$

A directed edge $T_i \to T_j$ means transaction $T_i$ is waiting for transaction $T_j$ to release a required lock.

**Cycle Detection:**  
We trace the directed edges among transactions $T_2, T_4,$ and $T_5$:

$$T_4 \to T_5 \to T_2 \to T_4$$

1. $T_4$ is waiting for $T_5$.
2. $T_5$ is waiting for $T_2$.
3. $T_2$ is waiting for $T_4$.

This forms a closed directed cycle.

**Verdict:**  
**Yes, the schedule contains a deadlock.**

**Transactions in Deadlock:**  
Transactions $\mathbf{T_2, T_4, \text{ and } T_5}$ are deadlocked. (Note: $T_1$ is waiting on $T_2, T_3, T_4$, but is not part of the cycle. $T_3$ has no outgoing edges and is not blocked).

**Breaking the Deadlock:**  
The DBMS must select one transaction in the cycle ($T_2, T_4$, or $T_5$) as a **victim** based on minimum abort cost, roll it back, and release its locks. This breaks the cycle and allows the remaining transactions to complete.

---

## T11.5 · Wait-die vs wound-wait

*No questions from past finals or class tests.*

*See also:* [[#2017 Q.7(b) · 04 Marks]] (wait-die and wound-wait as deadlock prevention schemes).

---

## T11.6 · Timestamp ordering: R-TS/W-TS rules, trace a schedule; rolled-back transaction gets a NEW timestamp

### 2018 Q.6(b) · 04 Marks

*Section B · Asked in: 2018, 2024 (CO3) · L2 merge*

**Question (2018 Q.6(b), 2024 Q.8(b) · identical text).** When a transaction is rolled back under timestamp ordering and it is assigned a new timestamp? Why can it not simply keep its old timestamp?

**Answer.**

**When a Transaction is Rolled Back Under Timestamp Ordering:**  
Under the Timestamp Ordering (TSO) protocol, a transaction $T_i$ is rolled back whenever it attempts an operation that conflicts with a younger transaction:

1. **On Read:** $T_i$ issues $\text{read}(Q)$, but $\text{TS}(T_i) < \text{W-timestamp}(Q)$.  
   $T_i$ is attempting to read an older value of $Q$ that has already been overwritten by a younger transaction. The read is rejected and $T_i$ is rolled back.
2. **On Write:**
   - $T_i$ issues $\text{write}(Q)$, but $\text{TS}(T_i) < \text{R-timestamp}(Q)$.  
     The value of $Q$ that $T_i$ is producing was needed previously by a younger transaction, which already read an older value. The write is rejected and $T_i$ is rolled back.
   - $T_i$ issues $\text{write}(Q)$, but $\text{TS}(T_i) < \text{W-timestamp}(Q)$.  
     $T_i$ is attempting to overwrite $Q$ with an obsolete value after a younger transaction has already written it. The write is rejected and $T_i$ is rolled back.

**Assigning a New Timestamp:**  
When $T_i$ is rolled back, the system aborts it and restarts it. Upon restarting, the system assigns $T_i$ a **new, larger timestamp** using the current system clock or logical counter.

**Why It Cannot Keep Its Old Timestamp:**

1. **Avoids Immediate Re-abort:**  
   If $T_i$ kept its old timestamp, $\text{TS}(T_i)$ would remain smaller than the $\text{R-timestamp}$ or $\text{W-timestamp}$ values already written by the younger transactions. On restarting, when $T_i$ reaches the same step, the exact same timestamp check would fail again.
2. **Prevents Starvation (Livelock):**  
   Keeping the old timestamp traps the transaction in an endless abort and restart loop. It would never finish. A new timestamp breaks this cycle.
3. **Correct Serial Order:**  
   A new timestamp assigns the transaction a fresh position in the logical serialization order, placing it after the conflicting transactions and allowing its operations to execute successfully.

*Short version for 2024 Q.8(b) (3 marks):* Give the read and write rollback conditions concisely. Then explain in 2 points why the old timestamp causes repeated aborts and starvation.

---

### 2023 Q.8(c) · 04 Marks

*Section B · CLO3 · Asked in: 2023 · L1 (asked once)*

**Question.** Discuss the given schedule based on Timestamp ordering protocol.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 20px;">$T_1(100)$</th><th style="padding: 4px 20px;">$T_2(200)$</th><th style="padding: 4px 20px;">$T_3(300)$</th></tr></thead><tbody><tr><td style="padding: 4px 20px;">$R(A)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(B)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">$W(C)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(B)$</td></tr><tr><td style="padding: 4px 20px;">$R(C)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(B)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(A)$</td></tr></tbody></table>  
*(Note: In the original paper schedule, $W(C)$ of $T_1$ and $R(B)$ of $T_3$ occupy essentially the same vertical tier. Since $C$ and $B$ are disjoint data items, the concurrency protocol evaluation remains unaffected).*

**Answer.**

**Initial Setup:**  
- Transaction timestamps: $\text{TS}(T_1) = 100$, $\text{TS}(T_2) = 200$, $\text{TS}(T_3) = 300$.
- Initial data item timestamps:
  $$\text{R-TS}(A) = \text{W-TS}(A) = 0$$
  $$\text{R-TS}(B) = \text{W-TS}(B) = 0$$
  $$\text{R-TS}(C) = \text{W-TS}(C) = 0$$

**Step-by-Step Execution Trace:**

| Step | Txn | Op | Protocol Condition Check | Decision | Updated Timestamp State |
| :---: | :---: | :---: | :--- | :--- | :--- |
| **1** | $T_1$ | $R(A)$ | $\text{TS}(T_1) \ge \text{W-TS}(A) \implies 100 \ge 0$ (Valid) | **Execute** | $\text{R-TS}(A) = \max(0, 100) = 100$ |
| **2** | $T_2$ | $R(B)$ | $\text{TS}(T_2) \ge \text{W-TS}(B) \implies 200 \ge 0$ (Valid) | **Execute** | $\text{R-TS}(B) = \max(0, 200) = 200$ |
| **3** | $T_1$ | $W(C)$ | $\text{TS}(T_1) \ge \text{R-TS}(C)$ and $\text{W-TS}(C) \implies 100 \ge 0$ (Valid) | **Execute** | $\text{W-TS}(C) = 100$ |
| **4** | $T_3$ | $R(B)$ | $\text{TS}(T_3) \ge \text{W-TS}(B) \implies 300 \ge 0$ (Valid) | **Execute** | $\text{R-TS}(B) = \max(200, 300) = 300$ |
| **5** | $T_1$ | $R(C)$ | $\text{TS}(T_1) \ge \text{W-TS}(C) \implies 100 \ge 100$ (Valid) | **Execute** | $\text{R-TS}(C) = \max(0, 100) = 100$ |
| **6** | $T_2$ | $W(B)$ | $\text{TS}(T_2) < \text{R-TS}(B) \implies 200 < 300$ (**Violated!**) | **REJECTED** | **$T_2$ is rolled back** |
| **7** | $T_3$ | $W(A)$ | $\text{TS}(T_3) \ge \text{R-TS}(A)$ and $\text{W-TS}(A) \implies 300 \ge 100$ (Valid) | **Execute** | $\text{W-TS}(A) = 300$ |

**Evaluation and Discussion:**

1. **Steps 1 through 5:** Each read and write operation satisfies the timestamp ordering rules. Operations execute in valid order.
2. **Conflict at Step 6:** Transaction $T_2$ ($\text{TS}=200$) attempts to write item $B$. But at Step 4, transaction $T_3$ ($\text{TS}=300$) has already read $B$, setting $\text{R-TS}(B) = 300$. Because $\text{TS}(T_2) < \text{R-TS}(B)$ ($200 < 300$), $T_2$ is producing a value of $B$ that $T_3$ needed to read. The system assumed that value would never be produced.
3. **Rollback Action:** The write operation $W(B)$ by $T_2$ is **rejected**. The system **rolls back transaction $T_2$**.
4. **Step 7:** $T_3$ executes $W(A)$ successfully because $\text{TS}(T_3) = 300 \ge \text{R-TS}(A) = 100$.

**Conclusion:**  
**The schedule is not accepted without rollback.** Transaction $\mathbf{T_2}$ is aborted and rolled back at Step 6. When restarted, $T_2$ must be assigned a new timestamp greater than 300.

---

[← Prev: T10 · Serializability](T10_Serializability.md) | [Explanation layer](../Topicwise_answers_explaination/T11_Concurrency_Control_Protocols.md) | [Next: T12 · Recovery System and RAID →](T12_Recovery_System_and_RAID.md)
