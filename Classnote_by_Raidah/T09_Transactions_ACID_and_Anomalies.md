# T09: Transactions, ACID & Anomalies — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 6 | `subtopicwise_list.md` T09 (41 marks · 6.4% · 7/7 · 🔴)  
**Source Pages:** Page 25 (Right), Page 26 (Left), Page 28 (Left)

---

## 1. Concept of a Transaction

<!-- Page 25 (Right) -->
<!-- Date: 13.09.2024 -->

A **transaction** is a unit of program execution that accesses and possibly updates various data items.

### Classical Bank Transfer Example:
Transferring \$50 from account $A$ to account $B$:
1. `read(A)`
2. `A := A - 50`
3. `write(A)`
4. `read(B)`
5. `B := B + 50`
6. `write(B)`

---

## 2. ACID Properties

<!-- Page 26 (Left) -->
<!-- Date: 13.09.2024 -->

To ensure database integrity and correctness under concurrent access and system crashes, every transaction must satisfy the **ACID** properties:

* **A $\rightarrow$ Atomicity (All or Nothing):** Either all operations of the transaction are executed and reflected properly in the database, or none are. If a crash occurs after step 3, account $A$ must not lose \$50 without $B$ receiving it.
* **C $\rightarrow$ Consistency:** Execution of a transaction in isolation preserves database consistency. The sum $A + B$ before transfer must equal $A + B$ after transfer.
* **I $\rightarrow$ Isolation:** Each transaction executes unaware of other concurrently executing transactions. Intermediate states (e.g., between steps 3 and 6) are invisible to concurrent transactions.
* **D $\rightarrow$ Durability:** After a transaction successfully commits, all updates persist in the database and are never lost, even in the event of an immediate system crash or power outage.

---

## 3. Transaction State Lifecycle

<!-- Page 26 (Left) -->

![Fig_DBMS_p26_01: Hand-drawn transaction state transition diagram showing states active, partially committed (PC), committed, failed, and aborted](diagrams/DBMS_classnote_2310035_p26_fig01.jpg)
*Figure 26.1 — Transaction state transition lifecycle (Page 26)*

* **Active:** The initial state; the transaction remains in this state while it is executing read and write operations.
* **Partially Committed (PC):** The state after the final statement has been executed, but before commit updates are written to stable log storage.
* **Committed:** Entered after successful completion; updates are permanently saved and guaranteed durable.
* **Failed:** The state entered when normal execution can no longer proceed due to hardware error, internal logic error, or concurrency abort.
* **Aborted:** The state entered after the transaction has been rolled back and the database has been restored to its consistent pre-transaction state.

---

## 4. Concurrent Execution & Concurrency Anomalies

<!-- Page 26 (Left) & Page 28 (Left) -->

### Need for Concurrency Control:
Executing transactions concurrently in parallel improves system throughput and CPU/disk utilization. However, without proper concurrency control mechanisms, uncontrolled interleaving produces serious data anomalies:

1. **Lost Update Problem:**
   Two transactions read the same data item concurrently and update it based on the old value. The second write completely overwrites and obliterates the update made by the first transaction.
2. **Temporary Update / Dirty Read Problem:**
   Transaction $T_1$ updates a data item, and transaction $T_2$ reads that updated value before $T_1$ commits. If $T_1$ subsequently fails and aborts, $T_2$ has acted on invalid data that never legally existed.
3. **Incorrect Summary / Inconsistent Analysis Problem:**
   An aggregate transaction reads multiple values across accounts to compute a sum while another transaction is actively transferring funds between those accounts, producing an incorrect total.

