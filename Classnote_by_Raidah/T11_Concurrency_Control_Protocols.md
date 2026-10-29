# T11: Concurrency Control Protocols — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 6 | `subtopicwise_list.md` T11 (37 marks · 5.8% · 6/7 · 🟠/🟡)  
**Source Pages:** Pages 28 (Right), 29, 30, 31, 32 (Left)

---

## 1. Deadlock & Coffman Conditions

<!-- Page 28 (Right) -->
<!-- Date: 22.09.2024 -->

A **deadlock** occurs when two or more transactions are in a simultaneous wait state, each waiting for a lock held by the other:
* $T_1$ acquires exclusive lock $X(A)$.
* $T_2$ acquires exclusive lock $X(B)$.
* $T_1$ requests shared lock $S(B)$ $\rightarrow$ waits for $T_2$.
* $T_2$ requests exclusive lock $X(A)$ $\rightarrow$ waits for $T_1$.
* Result: $T_1$ waits for $T_2$, and $T_2$ waits for $T_1$ $\implies$ **Deadlock!**

### 4 Necessary Coffman Conditions for Deadlock:
1. **Mutual Exclusion:** Resources cannot be shared; at least one resource must be held in non-shareable mode (only one transaction can hold the lock at a time).
2. **Hold and Wait:** A transaction currently holding at least one resource is waiting to acquire additional resources held by other transactions.
3. **No Preemption:** Resources cannot be forcibly taken away from a transaction; locks are released only voluntarily after the transaction finishes (a holding transaction cannot be interrupted or forced to release prematurely).
4. **Circular Wait:** A closed chain of transactions exists where $T_1$ waits for $T_2$, $T_2$ waits for $T_3$, and $T_n$ waits for $T_1$.

### Deadlock Prevention Methods:
* **Conservative 2PL (Pre-declaration):**
  * A transaction must lock all items it will access before it begins execution.
  * *Disadvantages:* Severe resource waste (locks held idle), and extremely difficult to predict all accessed data items in advance.

---

## 2. Timestamp-Based Deadlock Prevention Schemes

<!-- Page 29 -->

Transactions are assigned a monotonic timestamp $TS(T)$ when they enter the system:
* $TS(T_i) < TS(T_j) \implies T_i$ is older than $T_j$.

```text
Wait-Die (Non-preemptive):
  Older requests younger item -> Older WAITS
  Younger requests older item -> Younger DIES (rolls back)

Wound-Wait (Preemptive):
  Older requests younger item -> Older WOUNDS (preempts/rolls back younger)
  Younger requests older item -> Younger WAITS
```

### 1. Wait-Die Scheme (Non-preemptive):
Assume $T_1$ (timestamp 20, older) and $T_2$ (timestamp 30, younger). Data item $B$ is held by $T_2$:
* If $T_1$ requests $B$: $T_1$ is older $\implies$ **$T_1$ is allowed to wait** until $T_2$ finishes.
* If a younger transaction $T_3$ (timestamp 40) requests an item held by older $T_2$:
  * $T_3$ is younger $\implies$ **$T_3$ dies (rolls back)** to its initial state.
* *Summary: If an older transaction requests a resource, it is allowed to wait; if a younger transaction requests a resource from an older one, it dies and rolls back.*

### 2. Wound-Wait Scheme (Preemptive):
Assume $T_1$ (timestamp 20, older) and $T_2$ (timestamp 30, younger). Data item $B$ is held by $T_2$:
* If older $T_1$ requests $B$:
  * $T_1$ preempts / wounds $T_2 \implies$ **$T_2$ is rolled back** and releases the lock to $T_1$.
* If younger $T_3$ (timestamp 40) requests an item held by $T_2$:
  * $T_3$ is younger $\implies$ **$T_3$ is allowed to wait**.

---

## 3. Two-Phase Locking (2PL) Protocol

<!-- Page 30 (Left, Right) -->
<!-- Date: 20.09.2024 -->

* **Lock Types:**
  * **Shared Lock ($S$):** Allows read-only access (concurrent shared locks are compatible).
  * **Exclusive Lock ($X$):** Allows both read and write access (exclusive access, incompatible with all other locks).
* **Starvation:** A transaction waits indefinitely because other transactions repeatedly acquire shared locks (finite waiting required).

### Two-Phase Locking (2PL) Theorem:
* 2PL **always guarantees conflict serializability**.
* Equivalent serial schedule order is determined strictly by transaction **lock points** (the transaction that reaches its lock point first executes earlier in equivalent serial order).

![Fig_DBMS_p30_01: Hand-drawn Two-Phase Locking (2PL) protocol graph illustrating growing phase, lock point = 3, and shrinking phase for transactions T1 and T2](diagrams/DBMS_classnote_2310035_p30_fig01.jpg)
*Figure 30.1 — Two-Phase Locking protocol (2PL) graph (Page 30)*

### 2PL Phases:
1. **Growing Phase:**
   * A transaction may acquire locks, but cannot release any lock.
2. **Lock Point:**
   * The point where the transaction acquires its final lock (maximum number of locks held; here step 3 for $T_1$).
3. **Shrinking Phase:**
   * A transaction may release locks, but cannot acquire any new lock.

---

## 4. Timestamp Ordering (TSO) Protocol

<!-- Page 31 (Left, Right) & Page 32 (Left) -->
<!-- Date: 28.09.2024 -->

Every data item $Q$ maintains two system timestamps:
* **$WTS(Q)$:** Largest timestamp of any transaction that executed $\text{write}(Q)$ successfully.
* **$RTS(Q)$:** Largest timestamp of any transaction that executed $\text{read}(Q)$ successfully.

### 1. TSO Read Rule ($T_i$ issues $\text{read}(Q)$):
* **Case 1:** If $TS(T_i) < WTS(Q)$:
  * $T_i$ needs to read an old value of $Q$ that was already overwritten by a younger transaction.
  * $\implies$ **$T_i$ is rejected and rolled back** (restarts with a brand-new timestamp).
* **Case 2:** If $TS(T_i) \ge WTS(Q)$:
  * The read is valid and executed successfully.
  * Update $RTS(Q) := \max(RTS(Q), TS(T_i))$.

---

<!-- Page 31 (Right) -->

### 2. TSO Write Rule ($T_i$ issues $\text{write}(Q)$):
* **Case 1:** If $TS(T_i) < RTS(Q)$:
  * The value produced by $T_i$ was needed previously, but a younger transaction has already read a newer value.
  * $\implies$ **$T_i$ is rejected and rolled back**.
* **Case 2:** If $TS(T_i) < WTS(Q)$:
  * $T_i$ is attempting to write an obsolete value of $Q$.
  * $\implies$ **$T_i$ is rejected and rolled back** *(Standard TSO; Thomas' Write Rule ignores this obsolete write without aborting)*.
* **Case 3:** Otherwise:
  * The write operation is executed.
  * Update $WTS(Q) := TS(T_i)$.

### Serial Order Guarantee:
* TSO ensures conflict serializability with equivalent serial schedule matching transaction timestamps ($TS(T_i)$ order).

---

<!-- Page 32 (Left) -->

### TSO Worked Example:
* Given: $T_{25} = 10$, $RTS(B) = 10$.
* If $T_{26} = 20$ arrives and sets $RTS(B) = 20$ and $WTS(B) = 20$:
* Now if $T_{25}$ attempts to write $B$:
  * $TS(T_{25}) = 10 < RTS(B) = 20 \implies T_{25}$ is rolled back!
* Rule: Whichever transaction enters first must execute first according to timestamp ordering ($T_{25} \rightarrow T_{26}$).

