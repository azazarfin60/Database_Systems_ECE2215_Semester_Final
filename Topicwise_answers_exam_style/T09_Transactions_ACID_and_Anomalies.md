---
title: "T09 · Transactions, ACID and Anomalies · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T08 · Normalization and Functional Dependencies](T08_Normalization_and_Functional_Dependencies.md) | [Explanation layer](../Topicwise_answers_explaination/T09_Transactions_ACID_and_Anomalies.md) | [Next: T10 · Serializability →](T10_Serializability.md)

---

# T09 · Transactions, ACID and Anomalies

> [!info] Topic card
> **Syllabus:** Unit 6 · **Weight:** 41 final marks (6.4%) · 7/7 papers + 14 CT marks
> **Sources:** Deck 07 (Slides 2–15, 28–33) · Textbook Ch. 17 (§17.1–17.5)
> **Blocks in this file:** 12 final + 3 CT questions (10 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T09.1 | ACID properties | 18 + 6 | 2017 Q.5(a), 2018 Q.4(b), 2021 Q.7(a), 2023 Q.4(b), 2024 Q.6(c), CT-04 Q.01 | [[#T09.1 · ACID properties\|Go]] |
| T09.2 | Consistency property alone, with example | 6 + 0 | 2019 Q.3(b), 2024 Q.2(c) | [[#T09.2 · Consistency property alone, with example\|Go]] |
| T09.3 | Transaction states / life-cycle diagram | 6 + 0 | 2020 Q.5(b), 2023 Q.4(c) | [[#T09.3 · Transaction states / life-cycle diagram\|Go]] |
| T09.4 | Concurrent execution advantages and schedules | 4 + 4 | 2018 Q.6(a), CT-04 Q.02 | [[#T09.4 · Concurrent execution advantages and schedules\|Go]] |
| T09.5 | Concurrency problems | 7 + 4 | 2018 Q.5(a), 2024 Q.8(a), CT-04 Q.03 | [[#T09.5 · Concurrency problems\|Go]] |

---

## T09.1 · ACID properties

### 2017 Q.5(a) · 04 Marks

*Section B · Asked in: 2017, 2021 (CLO1), 2024 (CO3) · L2 merge*

**Question (2017 Q.5(a)).** Briefly discuss the ACID properties of transaction.

**Question (2021 Q.7(a)).** Explain the ACID properties of transaction.

**Question (2024 Q.6(c)).** Briefly discuss the ACID properties of transaction.

**Answer.**

A **transaction** is a logical unit of program execution that accesses and updates data items. To preserve data integrity during crashes and concurrent access, the DBMS must ensure the four **ACID** properties:

1. **Atomicity ("All-or-None"):**
   - Either all operations of the transaction are properly reflected in the database, or none are.
   - If a failure happens before the transaction completes, partial modifications are rolled back.
   - **Enforced by:** The **Recovery System** (using undo log records).

2. **Consistency (Preservation of Invariants):**
   - Executing a transaction in isolation preserves database consistency.
   - The database moves from one valid state to another valid state, satisfying all integrity constraints.
   - In a fund transfer, the total balance sum must remain unchanged.
   - **Enforced by:** The **Application Programmer** (correct business logic) and DBMS **Integrity Constraints**.

3. **Isolation (Shielding Concurrent Access):**
   - Each transaction executes as if it were running alone without interference from other concurrent transactions.
   - Intermediate results remain hidden from other concurrent transactions until commit.
   - **Enforced by:** The **Concurrency-Control System** (using locking or timestamp protocols).

4. **Durability (Persistence):**
   - After a transaction completes successfully and commits, its updates persist in the database permanently.
   - The committed data survives subsequent system crashes or power outages.
   - **Enforced by:** The **Recovery System** (using redo logs and non-volatile stable storage).

*Short version for 2024 Q.6(c) (2 marks):*
- **Atomicity:** All operations complete or none do. The recovery system undoes partial writes.
- **Consistency:** Execution in isolation preserves database validity and invariants.
- **Isolation:** Intermediate updates remain hidden from concurrent transactions.
- **Durability:** Committed changes persist permanently on disk despite crashes.

---

### 2018 Q.4(b) · 04 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** Describe the ACID-properties of database system with appropriate diagram.

**Answer.**

To maintain database integrity against failures and concurrent updates, every transaction must satisfy four **ACID** properties:

- **Atomicity:** All operations of the transaction take effect or none do.
- **Consistency:** Execution in isolation preserves all explicit constraints and implicit invariants.
- **Isolation:** Intermediate uncommitted states remain invisible to other concurrent transactions.
- **Durability:** Committed updates survive crashes permanently on stable storage.

**Illustration with \$50 Fund Transfer ($T_1$):**  
Let account $A$ have \$1000 and account $B$ have \$2000. $T_1$ moves \$50 from $A$ to $B$.

$$
\begin{aligned}
1.&\quad \text{read}(A) \\
2.&\quad A := A - 50 \\
3.&\quad \text{write}(A) \quad [A \text{ becomes } \$950] \\
4.&\quad \text{read}(B) \\
5.&\quad B := B + 50 \\
6.&\quad \text{write}(B) \quad [B \text{ becomes } \$2050] \\
7.&\quad \text{commit}
\end{aligned}
$$

![ACID properties illustrated on a \$50 fund transfer transaction showing database state evolution and the four ACID guarantees](diagrams/T09_2018_Q4b_acid_transfer.jpg)
*Figure: ACID properties in fund transfer transaction (Generated)*

**Mapping to the Diagram:**
1. **Atomicity:** If a crash occurs after step 3, account $A$ is \$950 while account $B$ remains \$2000. The recovery system uses log records to roll back $A$ to \$1000.
2. **Consistency:** The invariant $A + B = \$3000$ holds in the initial state and in the final state. Money is neither created nor lost.
3. **Isolation:** Between steps 3 and 6, the sum is temporarily \$2950. Concurrency control blocks concurrent transaction $T_2$ from reading this intermediate state.
4. **Durability:** After step 7 commits, balances $A = \$950$ and $B = \$2050$ survive power loss.

---

### 2023 Q.4(b) · 04 Marks

*Section A · Asked in: 2023 (CLO3) · L1 (asked once)*

**Question.** Briefly explain the importance of ACID properties of transactions with suitable example.

**Answer.**

Databases must handle two critical challenges: system failures (crashes, power loss) and concurrent user execution. The ACID properties are essential because without them, database data becomes corrupt and untrustworthy.

**Example:** Transaction $T_1$ transfers \$50 from account $A$ (\$1000) to account $B$ (\$2000). The invariant is $A + B = \$3000$.

**Importance of Each Property:**

1. **Importance of Atomicity:**
   - *Failure case without atomicity:* The system crashes after deducting \$50 from $A$, before adding \$50 to $B$. The bank loses \$50 of customer money.
   - *Protection:* Atomicity forces the recovery manager to undo the deduction, restoring $A = \$1000$.

2. **Importance of Consistency:**
   - *Failure case without consistency:* A flawed program deducts \$50 from $A$ but adds \$100 to $B$.
   - *Protection:* Consistency ensures transaction logic preserves all domain rules. The total sum $A + B = \$3000$ remains balanced.

3. **Importance of Isolation:**
   - *Failure case without isolation:* An audit transaction $T_2$ reads balances right after $T_1$ writes $A = \$950$, before $T_1$ writes $B$. $T_2$ calculates total assets as $\$950 + \$2000 = \$2950$. It issues a false financial warning.
   - *Protection:* Isolation ensures $T_2$ sees either pre-transfer data (\$3000) or post-transfer data (\$3000).

4. **Importance of Durability:**
   - *Failure case without durability:* $T_1$ completes and confirms the transfer. Then a power outage occurs before updates reach disk. The transfer is lost upon reboot.
   - *Protection:* Durability guarantees that committed transactions are logged to stable storage and survive power loss.

---

### CT-04 Q.01 · 06 Marks

*Asked in: CT-04 (CO3) · L1 (asked once)*

**Question.** Define a transaction? Explain the four ACID properties of a transaction with suitable examples.

**Answer.**

**Definition:**  
A **transaction** is a logical unit of program execution that accesses and possibly updates various data items in a database. It consists of all operations executed between a `begin transaction` and an `end transaction` (`commit` or `abort`).

**The Four ACID Properties with Examples:**  
Consider transaction $T_1$ transferring \$50 from account $A$ (initially \$1000) to account $B$ (initially \$2000):

$$
T_1: \text{read}(A) \to A := A - 50 \to \text{write}(A) \to \text{read}(B) \to B := B + 50 \to \text{write}(B) \to \text{commit}
$$

1. **Atomicity ("All-or-None"):**
   - **Explanation:** Either all operations of the transaction take effect in the database or none do.
   - **Example:** If a crash happens after $\text{write}(A)$ has executed, $A$ is \$950 but $B$ is still \$2000. Atomicity requires the recovery system to undo the update on $A$ so that $A$ returns to \$1000.
   - **Enforcement:** Recovery system using log-based rollback.

2. **Consistency (Invariant Preservation):**
   - **Explanation:** A transaction running in isolation must preserve database consistency. It moves the database from one valid state to another valid state.
   - **Example:** The invariant is that total money $A + B = \$3000$. Before $T_1$, $A + B = \$1000 + \$2000 = \$3000$. After $T_1$, $A + B = \$950 + \$2050 = \$3000$. Consistency preserves the total money in the bank.
   - **Enforcement:** Application programmer logic and DBMS integrity constraints.

3. **Isolation (Shielding Concurrent Execution):**
   - **Explanation:** Even though multiple transactions execute concurrently, the system guarantees that each transaction is unaware of other concurrently running transactions. Intermediate results remain hidden.
   - **Example:** During $T_1$'s execution, after step 3, $A = \$950$ and $B = \$2000$. If transaction $T_2$ runs concurrently to print $A + B$, isolation prevents $T_2$ from reading the intermediate sum \$2950. $T_2$ sees either \$3000 before $T_1$ or \$3000 after $T_1$.
   - **Enforcement:** Concurrency-control manager (two-phase locking or timestamps).

4. **Durability (Permanence across Failures):**
   - **Explanation:** Once a transaction completes successfully and commits, its changes persist in the database, even if system crashes occur.
   - **Example:** Once $T_1$ executes `commit`, updates $A = \$950$ and $B = \$2050$ are recorded to stable storage. If power fails a second later, the values remain intact upon reboot.
   - **Enforcement:** Recovery system using write-ahead redo logging.

---

## T09.2 · Consistency property alone, with example

### 2019 Q.3(b) · 03 Marks

*Section A · Asked in: 2019, 2024 (CO1) · L2 merge (identical text)*

**Question (2019 Q.3(b), 2024 Q.2(c)).** Explain the consistency property of a database system with a proper example.

**Answer.**

**Definition:**  
The **consistency** property requires that executing a transaction in isolation preserves the consistency of the database. If the database starts in a valid state that satisfies all integrity rules, it must end in a valid state after the transaction completes.

**Categories of Consistency Constraints:**
1. **Explicit Constraints:** Rules enforced automatically by the DBMS, including primary keys, foreign keys, data types, and `CHECK` constraints (such as `balance >= 0`).
2. **Implicit Invariants:** Business rules that cannot easily be expressed in DDL, such as preserving total assets across account transfers.

**Example (Bank Transfer):**  
Let account $A$ have \$1000 and account $B$ have \$2000. The consistency invariant requires total funds to remain constant:

$$A + B = \$1000 + \$2000 = \$3000$$

Transaction $T_1$ transfers \$50 from $A$ to $B$:
1. $\text{read}(A)$
2. $A := A - 50$
3. $\text{write}(A) \quad [A = \$950]$
4. $\text{read}(B)$
5. $B := B + 50$
6. $\text{write}(B) \quad [B = \$2050]$

- **Temporary Inconsistency During Execution:** After step 3, $A = \$950$ and $B = \$2000$. The sum is $\$950 + \$2000 = \$2950$. The database enters a temporarily inconsistent state.
- **Restored Consistency at End:** After step 6 completes, $A = \$950$ and $B = \$2050$. The sum is $\$950 + \$2050 = \$3000$. Database consistency is restored.
- **Responsibility:** Ensuring transaction logic is correct is primarily the responsibility of the **application programmer**.

---

## T09.3 · Transaction states / life-cycle diagram

### 2020 Q.5(b) · 04 Marks

*Section B · Asked in: 2020 · L1 (asked once)*

**Question.** What is a transaction? Describe the life cycle of a transaction.

**Answer.**

**Definition:**  
A **transaction** is a logical unit of program execution that accesses and possibly updates various data items in a database.

**Life Cycle of a Transaction:**  
A transaction moves through five distinct states during its execution:

![Transaction state transition diagram showing states: active, partially committed, committed, failed, and aborted with transition arrows](../LectureSlides/diagrams/L07_p08_fig01.jpg)
*Figure: Transaction State Transition Diagram (Source: Deck 07, Slide 8)*

1. **Active:**  
   The initial state. The transaction enters this state upon creation and remains active while executing its read, write, and computational statements.
2. **Partially Committed:**  
   Entered after the final statement has been executed. The updates are still held in volatile main-memory buffers and have not yet been flushed permanently to disk.
3. **Failed:**  
   Entered when normal execution can no longer proceed due to hardware faults, internal logical errors, or concurrency conflicts.
4. **Aborted:**  
   Entered after the transaction has failed and the recovery system has undone all partial writes, restoring the database to its state prior to the transaction. After an abort, the system can:
   - **Restart** the transaction (if aborted by transient hardware failure or deadlock).
   - **Kill** the transaction (if aborted by bad input or internal programming errors).
5. **Committed:**  
   Entered after successful completion, once all updates are safely written to non-volatile log/storage. The transaction terminates successfully.

---

### 2023 Q.4(c) · 02 Marks

*Section A · Asked in: 2023 (CLO3) · L1 (asked once)*

**Question.** Draw state diagram of a transaction.

**Answer.**

![Transaction state transition diagram showing active, partially committed, committed, failed, and aborted states](../LectureSlides/diagrams/L07_p08_fig01.jpg)
*Figure: Transaction State Diagram (Source: Deck 07, Slide 8)*

**State Transitions:**
- **Active $\to$ Partially Committed:** When the transaction executes its final statement.
- **Partially Committed $\to$ Committed:** When updates are safely flushed to stable storage.
- **Active $\to$ Failed:** When a system error or logical fault occurs during execution.
- **Partially Committed $\to$ Failed:** When a failure occurs before updates are written to disk.
- **Failed $\to$ Aborted:** When rollback restores the database to its pre-transaction state.

---

## T09.4 · Concurrent execution advantages and schedules

### 2018 Q.6(a) · 04 Marks

*Section B · Asked in: 2018 · L1 (asked once)*

**Question.** Define transaction and schedule. What is the difference between serial schedule and serializable schedule?

**Answer.**

**Definitions:**
- **Transaction:** A logical unit of program execution that accesses and possibly updates various data items in a database.
- **Schedule:** A sequence of instructions that specifies the chronological order in which instructions of concurrent transactions are executed. A schedule must contain all operations of its constituent transactions and preserve the internal operation order within each transaction.

**Difference Between Serial Schedule and Serializable Schedule:**

| Feature | Serial Schedule | Serializable Schedule |
| :--- | :-- | :-- |
| **Instruction Interleaving** | No interleaving. Transactions run strictly one after another; each finishes before the next begins. | Instructions of multiple transactions are interleaved concurrently. |
| **System Concurrency** | Zero concurrency. Hardware sits idle during disk I/O waits. | High concurrency. CPU and disk operate in parallel across transactions. |
| **Throughput & Latency** | Low throughput. Short transactions suffer long queue delays. | High throughput. Short transactions complete with low average response time. |
| **Correctness** | Always correct and consistent by default. | Correct only if it produces the same final state as some serial execution. |
| **Verification** | No verification needed. | Requires testing (e.g., precedence graph cycle check for conflict serializability). |

---

### CT-04 Q.02 · 04 Marks

*Asked in: CT-04 (CO3) · L1 (asked once)*

**Question.** Differentiate between a serial schedule and a concurrent schedule. Mention two advantages of concurrent execution of transactions.

**Answer.**

**Difference Between Serial Schedule and Concurrent Schedule:**

| Feature | Serial Schedule | Concurrent Schedule |
| :--- | :-- | :-- |
| **Execution Pattern** | Non-interleaved. One transaction runs to completion before another begins. | Interleaved. Operations from different transactions overlap in time. |
| **Resource Use** | Low. CPU remains idle while a transaction waits for disk I/O. | High. CPU processes one transaction while disk serves another. |
| **Response Time** | High average response time; short transactions wait behind long ones. | Low average response time; short transactions finish quickly. |
| **Need for Concurrency Control** | None. Execution is safe without concurrency control protocols. | Essential. Needs protocols (locks/timestamps) to avoid anomalies. |

**Two Advantages of Concurrent Execution of Transactions:**
1. **Increased Processor and Disk Use (Better Throughput):**  
   A transaction consists of both CPU and disk I/O operations. The CPU and disk subsystems can operate in parallel. While one transaction performs disk reads or writes, the CPU can execute calculations for another transaction. This parallel operation keeps hardware busy and increases transaction throughput.
2. **Reduced Average Response Time (Lower Waiting Time):**  
   In a serial schedule, a short transaction must wait for preceding long-running transactions to finish. Concurrent execution allows transactions to share CPU cycles and disk accesses. Short transactions complete without unpredictable delays, reducing average response time.

---

## T09.5 · Concurrency problems

### 2018 Q.5(a) · 04 Marks

*Section B · Asked in: 2018, 2024 (CO3), CT-04 (CO3) · L2 merge*

**Question (2018 Q.5(a)).** If concurrency-control management is not implemented properly what problem may occur? Explain with example.

**Question (2024 Q.8(a)).** If concurrency-control management is not implemented properly what problem may occur? Explain with example.

**Question (CT-04 Q.03).** Explains any two problems caused by concurrent execution. *(Note: Printed verbatim in original script)*.

**Answer.**

If concurrency-control management is not implemented properly, uncoordinated interleaving violates transaction isolation. This causes five major anomalies:

1. **Lost Update Problem:**
   - **Concept:** An update done by one transaction is overwritten and lost because another concurrent transaction writes to the same item without incorporating the first update.
   - **Schedule ($A = 500$ initially):**

| Time | Transaction $T_1$ | Transaction $T_2$ | Database State / Note |
| :--- | :--- | :--- | :--- |
| $t_1$ | $\text{read}(A)$ | | $T_1$ reads $A = 500$ |
| $t_2$ | $A := A - 50$ | | $T_1$ computes local $A = 450$ |
| $t_3$ | $\text{write}(A)$ | | Database updated to $A = 450$ |
| $t_4$ | | $\text{write}(A)$ | $T_2$ performs blind write: $A = 25$ |
| $t_5$ | $\text{commit}$ | | $T_1$ commits |
| $t_6$ | | $\text{commit}$ | Final $A = 25$ ($T_1$'s $-\$50$ update is lost!) |

2. **Dirty Read Problem (Temporary Update Problem):**
   - **Concept:** Occurs when a transaction reads a data item updated by another transaction that has not yet committed and later fails and rolls back.
   - **Schedule ($A = 100$ initially):**

| Time | Transaction $T_1$ | Transaction $T_2$ | Database State / Note |
| :--- | :--- | :--- | :--- |
| $t_1$ | $\text{read}(A)$ | | $T_1$ reads $A = 100$ |
| $t_2$ | $A := A + 100$ | | $T_1$ computes local $A = 200$ |
| $t_3$ | $\text{write}(A)$ | | Database $A = 200$ (uncommitted) |
| $t_4$ | | $\text{read}(A)$ | $T_2$ reads dirty value $A = 200$ |
| $t_5$ | | $A := A - 50$ | $T_2$ computes $A = 150$ |
| $t_6$ | | $\text{write}(A)$ | Database $A = 150$ |
| $t_7$ | | $\text{commit}$ | $T_2$ commits with invalid data |
| $t_8$ | **Failure / Rollback** | | $T_1$ fails; log restores $A = 100$ |

$T_2$ based its computation on a temporary value that never officially existed, leaving the database inconsistent.

3. **Unrepeatable Read Problem:**
   - **Concept:** A transaction reads the same data item twice but obtains different values because another transaction modified and committed the item in between.
   - **Schedule ($A = 500$ initially):**

| Time | Transaction $T_1$ | Transaction $T_2$ | Database State / Note |
| :--- | :--- | :--- | :--- |
| $t_1$ | $\text{read}(A)$ | | $T_1$ reads $A = 500$ |
| $t_2$ | | $\text{read}(A)$ | $T_2$ reads $A = 500$ |
| $t_3$ | | $A := A + 100$ | $T_2$ computes local $A = 600$ |
| $t_4$ | | $\text{write}(A)$ | Database $A = 600$ |
| $t_5$ | | $\text{commit}$ | $T_2$ commits |
| $t_6$ | $\text{read}(A)$ | | $T_1$ reads $A = 600$ (reads different value!) |

4. **Phantom Read Problem:**
   - **Concept:** A transaction accesses a variable, but when it attempts to access that variable again, an error occurs because another transaction has deleted it.
   - **Schedule:**

| Time | Transaction $T_1$ | Transaction $T_2$ | Note |
| :--- | :--- | :--- | :--- |
| $t_1$ | $\text{read}(A)$ | $\text{read}(A)$ | Both transactions read data item $A$ |
| $t_2$ | $\text{delete}(A)$ | | $T_1$ deletes data item $A$ and commits |
| $t_3$ | | $\text{read}(A)$ | $T_2$ attempts to read $A$ again, but item does not exist |

5. **Incorrect Summary Problem:**
   - **Concept:** An aggregate transaction calculates a summary across items while another transaction updates them. The aggregate reads some items before the update and others after, yielding an inaccurate summary.
   - **Example:** $T_1$ transfers \$50 from $A$ to $B$. If $T_2$ reads $A$ after the deduction ($A = \$950$) but reads $B$ before the addition ($B = \$1000$), its computed sum is \$1950 instead of \$2000.

*Variant for 2024 Q.8(a) (3 marks):*  
List the five anomalies, then provide the full schedule tables for Lost Update and Dirty Read.

*Short version for CT-04 Q.03 (4 marks):*  
Select **Lost Update** and **Dirty Read** with their definitions and schedule tables above.

---

[← Prev: T08 · Normalization and Functional Dependencies](T08_Normalization_and_Functional_Dependencies.md) | [Explanation layer](../Topicwise_answers_explaination/T09_Transactions_ACID_and_Anomalies.md) | [Next: T10 · Serializability →](T10_Serializability.md)
