[← Previous: T13.4: Static vs. Dynamic Hashing](T13.04_Static_vs_Dynamic_Hashing.md) | [🏠 Index](00_Index.md) | [Next: 🏠 Index →](00_Index.md)

---

# 📐 99: Master Formula, Algorithm & SQL Syntax Sheet

> **Course:** ECE 2215: Database Systems | **Purpose:** Rapid Last-Minute Reference for All Operators, Formulas, Algorithms, and MySQL 8 Templates

---

## 1. E-R & EER Modeling (`T02`) — Reduction & Cardinality Formulas

### 1.1 Weak Entity Set Primary Key Formula
For a weak entity set $E$ that depends on strong identifying owner entity set $F$ via identifying relationship $R$:

$$
\text{PK}(E) = \text{PK}(F) \cup \text{Discriminator}(E)
$$

- **Where:** $\text{PK}(F)$ is the primary key of the strong owner entity set, and $\text{Discriminator}(E)$ (partial key, dashed underline in E-R diagrams) uniquely distinguishes weak entities within the same owner.
- **Boss Note:** [T02.4: Weak vs. Strong Entity Sets](T02.04_Weak_vs_Strong_Entity_Sets.md) · **Last Tested:** `2021 Q.8(c)`, `2020 Q.2(c)`

### 1.2 Foreign Key Placement by Mapping Cardinality
For a binary relationship set $R$ between entity sets $A$ and $B$:

| Cardinality Ratio | Chen Arrow Notation | Relational Schema Reduction Rule | Boss Note & Last Tested |
| :--- | :--- | :--- | :--- |
| **One-to-One ($1:1$)** | $A \longleftarrow R \longrightarrow B$ | Add $\text{PK}(A)$ as FK in $B$, or $\text{PK}(B)$ as FK in $A$ (prefer the side with total participation) | [T02.3](T02.03_Mapping_Cardinality_and_Participation.md), [T02.6](T02.06_Reduction_of_ER_to_Tables.md) (`2020 Q.1(c)`) |
| **One-to-Many ($1:N$)** | $A \longleftarrow R \text{ --- } B$ | Fold $R$ into the **"many" side** ($B$): add $\text{PK}(A)$ as a foreign key inside table $B$ | [T02.3](T02.03_Mapping_Cardinality_and_Participation.md), [T02.6](T02.06_Reduction_of_ER_to_Tables.md) (`2020 Q.1(c)`) |
| **Many-to-Many ($M:N$)** | $A \text{ --- } R \text{ --- } B$ | Create a **new junction table** $R$ with composite primary key: $$\text{PK}(R) = \text{PK}(A) \cup \text{PK}(B)$$ | [T02.3](T02.03_Mapping_Cardinality_and_Participation.md) (`2018 Q.3(c)`) |
| **Ternary ($A, B, C$)** | Diamond connecting $A, B, C$ | Create table $R$: if no arrow exists, $\text{PK}(R) = \text{PK}(A) \cup \text{PK}(B) \cup \text{PK}(C)$. If $C$ has an arrow ($\to C$), $\text{PK}(R) = \text{PK}(A) \cup \text{PK}(B)$ | [T02.6](T02.06_Reduction_of_ER_to_Tables.md) (`2018 Q.2(c)`) |

---

## 2. Relational Model & Relational Algebra (`T03`, `T04`, `T06`)

### 2.1 Referential Integrity Constraint
If relation $r_2(R_2)$ includes a foreign key $\alpha$ referencing the primary key $K$ of relation $r_1(R_1)$, then at every database instance:

$$
\Pi_{\alpha}(r_2) \subseteq \Pi_{K}(r_1)
$$

- **Where:** $\Pi_{\alpha}(r_2)$ is the set of non-null foreign key values appearing in referencing relation $r_2$, and $\Pi_{K}(r_1)$ is the set of primary key values in referenced relation $r_1$.
- **Boss Note:** [T03.3: Referential Integrity and Foreign Keys](T03.03_Referential_Integrity_and_Foreign_Keys.md) · **Last Tested:** `2021 Q.1(c)`

### 2.2 Fundamental & Extended Relational Algebra Operators

| Operator | Notation & Equation | Meaning & Arity / Row Count | Boss Note & Last Tested |
| :--- | :--- | :--- | :--- |
| **Selection** | $$\sigma_{p}(r)$$ | Filters rows satisfying predicate $p$. Degree unchanged; $0 \le \lvert\sigma_p(r)\rvert \le \lvert r\rvert$ | [T04.1](T04.01_Basic_RA_Operators.md), [T04.2a](T04.02a_RA_Queries_Employee_and_Insurance.md) (`2024 Q.5(a)`) |
| **Projection** | $$\Pi_{A_1, A_2, \dots, A_k}(r)$$ | Keeps columns $A_1,\dots,A_k$ and **eliminates duplicate tuples** (set semantics) | [T04.1](T04.01_Basic_RA_Operators.md), [T04.2a](T04.02a_RA_Queries_Employee_and_Insurance.md) (`2024 Q.5(a)`) |
| **Cartesian Product** | $$r \times s$$ | Pairs every tuple of $r$ with every tuple of $s$. Degree $= \text{deg}(r)+\text{deg}(s)$; rows $= \lvert r\rvert \cdot \lvert s\rvert$ | [T04.1](T04.01_Basic_RA_Operators.md) (`CT-01 Q.05`) |
| **Set Union / Diff / Intersection** | $$r \cup s, \quad r - s, \quad r \cap s = r - (r - s)$$ | Requires **union compatibility** (same arity and matching attribute domains). Use $r - s$ for **"only / exclusively"** queries | [T04.2b](T04.02b_RA_Queries_Covid_and_Vaccine.md) (`2020 Q.2(a)`) |
| **Rename** | $$\rho_{x(A_1, \dots, A_n)}(E)$$ | Renames expression $E$ to $x$ with attributes $A_1,\dots,A_n$ (required for self-joins) | [T04.3](T04.03_Explaining_RA_Expressions.md) (`CT-01 Q.05(iv)`) |
| **Natural Join** | $$r \bowtie s = \Pi_{R \cup S}\!\left(\sigma_{r.A_1 = s.A_1 \land \dots \land r.A_k = s.A_k}(r \times s)\right)$$ | Equates all common attributes $R \cap S = \{A_1,\dots,A_k\}$ and removes duplicate common columns | [T04.1](T04.01_Basic_RA_Operators.md), [T06.1](T06.01_Types_of_Joins.md) (`2024 Q.5(a)`) |
| **Theta Join** | $$r \bowtie_{\theta} s = \sigma_{\theta}(r \times s)$$ | Cartesian product filtered by condition $\theta$; keeps all columns of $r$ and $s$ | [T04.1](T04.01_Basic_RA_Operators.md), [T06.1](T06.01_Types_of_Joins.md) (`2024 Q.3(c)`) |
| **Grouping & Aggregation** | $${}_{G_1, G_2, \dots, G_m}\gamma_{F_1(A_1), \dots, F_k(A_k)}(E)$$ | Groups tuples of $E$ by $G_1,\dots,G_m$ and applies aggregate functions $F_i \in \{\text{sum}, \text{count}, \text{avg}, \text{min}, \text{max}\}$ | [T04.4](T04.04_Extended_RA_Aggregation.md), [T04.2c](T04.02c_RA_Queries_Orders_Projects_CT.md) (`2024 Q.2(b)`) |
| **Outer Joins (RA)** | $$r \mathbin{⟕} s, \quad r \mathbin{⟖} s, \quad r \mathbin{⟗} s$$ | Preserves unmatched tuples from left ($r$), right ($s$), or both relations, padding missing attributes with `null` | [T06.3](T06.03_Outer_Join_Algebra.md) (`2024 Q.4(a)`) |

### 2.3 Relational Division ($r \div s$) for Universal Quantification ("For All")
Given $r(R)$ and $s(S)$ where $S \subset R$, let $T = R - S$. A tuple $t$ is in $r \div s$ if and only if $t$ appears in $r$ paired with **every** tuple in $s$:

$$
r \div s = \Pi_{R - S}(r) - \Pi_{R - S}\!\Big(\big(\Pi_{R - S}(r) \times s\big) - r\Big)
$$

- **Where:** $\Pi_{R-S}(r) \times s$ generates all possible pairings, subtracting $r$ leaves the *missing* required pairings, and subtracting those disqualified entities from $\Pi_{R-S}(r)$ leaves entities associated with **all** elements of $s$.
- **Boss Note:** [T04.5: Domain Relational Calculus and Relational Division](T04.05_Domain_Relational_Calculus_and_Division.md)

### 2.4 Silberschatz 6e Relational Algebra Database Modification (RUET Exam Convention)

$$
\begin{aligned}
\text{Deletion:} \quad & r \leftarrow r - E \\
\text{Insertion:} \quad & r \leftarrow r \cup E \\
\text{Update all rows:} \quad & r \leftarrow \Pi_{F_1, F_2, \dots, F_n}(r) \\
\text{Conditional update:} \quad & r \leftarrow \Pi_{F_1, \dots, F_n}\!\big(\sigma_{p}(r)\big) \cup \sigma_{\lnot p}(r)
\end{aligned}
$$

- **Boss Note:** [T04.2a: RA Queries — Employee, Insurance, and RA Updates](T04.02a_RA_Queries_Employee_and_Insurance.md) · **Last Tested:** `2018 Q.3(a)(iii)`, `2017 Q.2(a)(ii–iii)`

### 2.5 Domain Relational Calculus (DRC) Equivalents
For relation $r_1(A, B, C)$ and $r_2(A, B, C)$:

$$
\begin{aligned}
\Pi_{A}(r_1) &= \{\,\langle a \rangle \mid \exists b\,\exists c\,(\langle a, b, c \rangle \in r_1)\,\} \\
\sigma_{B = 17}(r_1) &= \{\,\langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \land b = 17\,\} \\
r_1 \cup r_2 &= \{\,\langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \lor \langle a, b, c \rangle \in r_2\,\} \\
r_1 \cap r_2 &= \{\,\langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \land \langle a, b, c \rangle \in r_2\,\} \\
r_1 - r_2 &= \{\,\langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \land \lnot(\langle a, b, c \rangle \in r_2)\,\}
\end{aligned}
$$

- **Boss Note:** [T04.5: Domain Relational Calculus and Relational Division](T04.05_Domain_Relational_Calculus_and_Division.md) · **Last Tested:** `2020 Q.4(b)`

---

## 3. SQL Formulas & MySQL 8 Templates (`T05`, `T06`, `T07`)

### 3.1 Weighted CGPA Formula & SQL Template
When student semester GPAs are in `GPA(roll, sem, gpa)` and semester credits are in `Credit(sem, credit)`:

$$
\text{CGPA} = \frac{\sum_{i} \left(\text{gpa}_i \times \text{credit}_i\right)}{\sum_{i} \text{credit}_i}
$$

```sql
SELECT g.roll,
       SUM(g.gpa * c.credit) / SUM(c.credit) AS cgpa
FROM GPA g
JOIN Credit c ON g.sem = c.sem
GROUP BY g.roll;
```

- **Boss Note:** [T05.5b: Weighted CGPA and Extremes Without LIMIT](T05.05b_CGPA_and_Extremes_Without_LIMIT.md) · **Last Tested:** `2019 Q.7(a)(iii)`, `2017 Q.4(a)(iii)`

### 3.2 Finding Extremes (Min / Max / 2nd-Highest) Without `LIMIT`

```sql
-- 1. Maximum / Minimum without LIMIT (handles ties correctly)
SELECT roll, gpa
FROM student
WHERE gpa = (SELECT MAX(gpa) FROM student);

-- 2. Second-Highest Value without LIMIT
SELECT MAX(gpa) AS second_highest_gpa
FROM student
WHERE gpa < (SELECT MAX(gpa) FROM student);
```

- **Boss Note:** [T05.5b: Weighted CGPA and Extremes Without LIMIT](T05.05b_CGPA_and_Extremes_Without_LIMIT.md) · **Last Tested:** `2024 Q.1(c)`, `2019 Q.7(a)(i, iv)`

### 3.3 Emulating `FULL OUTER JOIN` in MySQL 8
Because MySQL does not support the `FULL OUTER JOIN` keyword, always combine `LEFT JOIN` and `RIGHT JOIN` with `UNION` (which automatically removes duplicate matched rows):

```sql
SELECT c.`Course ID`, c.`Course Name`, t.Teacher
FROM Courses c
LEFT JOIN Teacher t ON c.`Course ID` = t.`Course ID`
UNION
SELECT t.`Course ID`, c.`Course Name`, t.Teacher
FROM Courses c
RIGHT JOIN Teacher t ON c.`Course ID` = t.`Course ID`;
```

- **Boss Note:** [T06.2: Computing Join Outcome Tables in MySQL](T06.02_Join_Outcome_Tables.md) · **Last Tested:** `2024 Q.4(a)`, `2020 Q.4(c)`

### 3.4 MySQL 8 Trigger & Stored Procedure Templates

```sql
-- Trigger Template (e.g., update stock or write audit log)
DELIMITER //
CREATE TRIGGER trg_after_order_insert
AFTER INSERT ON Orders
FOR EACH ROW
BEGIN
    UPDATE Products
    SET StockQuantity = StockQuantity - NEW.Quantity
    WHERE ProductID = NEW.ProductID;
END //
DELIMITER ;

-- Stored Procedure Template (with transaction handling)
DELIMITER //
CREATE PROCEDURE PlaceOrder(
    IN p_ProductID INT,
    IN p_CustomerID INT,
    IN p_Quantity INT
)
BEGIN
    DECLARE v_Stock INT;
    START TRANSACTION;
    SELECT StockQuantity INTO v_Stock
    FROM Products WHERE ProductID = p_ProductID FOR UPDATE;

    IF v_Stock >= p_Quantity THEN
        INSERT INTO Orders (ProductID, CustomerID, Quantity, OrderDate)
        VALUES (p_ProductID, p_CustomerID, p_Quantity, CURRENT_DATE);
        UPDATE Products SET StockQuantity = StockQuantity - p_Quantity
        WHERE ProductID = p_ProductID;
        COMMIT;
    ELSE
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock';
    END IF;
END //
DELIMITER ;
```

- **Boss Notes:** [T07.1](T07.01_Triggers_Definition_and_Syntax.md), [T07.2](T07.02_Triggers_for_Security.md), [T07.3](T07.03_Implementing_Triggers_and_Procedures.md) · **Last Tested:** `2024 Q.2(a)`, `2024 Q.6(b)`, `2023 Q.6(b)`

---

## 4. Functional Dependencies & Normalization (`T08`)

### 4.1 Armstrong's Axioms & Secondary Inference Rules
Let $\alpha, \beta, \gamma, \delta$ be subsets of attributes of relation schema $R$:

$$
\begin{aligned}
\text{1. Reflexivity (Primary):} \quad & \text{If } \beta \subseteq \alpha, \text{ then } \alpha \to \beta \\
\text{2. Augmentation (Primary):} \quad & \text{If } \alpha \to \beta, \text{ then } \gamma\alpha \to \gamma\beta \\
\text{3. Transitivity (Primary):} \quad & \text{If } \alpha \to \beta \text{ and } \beta \to \gamma, \text{ then } \alpha \to \gamma \\
\text{4. Union (Secondary):} \quad & \text{If } \alpha \to \beta \text{ and } \alpha \to \gamma, \text{ then } \alpha \to \beta\gamma \\
\text{5. Decomposition (Secondary):} \quad & \text{If } \alpha \to \beta\gamma, \text{ then } \alpha \to \beta \text{ and } \alpha \to \gamma \\
\text{6. Pseudotransitivity (Secondary):} \quad & \text{If } \alpha \to \beta \text{ and } \gamma\beta \to \delta, \text{ then } \alpha\gamma \to \delta
\end{aligned}
$$

- **Boss Note:** [T08.3: Armstrong's Axioms and Additional Inference Rules](T08.03_Armstrongs_Axioms.md)

### 4.2 Attribute Closure Algorithm ($X^+$ under $F$)
To compute the closure $X^+$ of attribute set $X$ under FD set $F$:

$$
\begin{aligned}
\text{Initialize:} \quad & \text{result} := X \\
\text{Repeat until unchanged:} \quad & \text{For each } (\alpha \to \beta) \in F: \\
& \quad \text{If } \alpha \subseteq \text{result}, \text{ then } \text{result} := \text{result} \cup \beta \\
\text{Output:} \quad & X^+ := \text{result}
\end{aligned}
$$

- **Superkey & Candidate Key Criterion:** $K$ is a **superkey** of $R$ iff $K^+ = R$. $K$ is a **candidate key** iff $K^+ = R$ and no proper subset $Y \subset K$ satisfies $Y^+ = R$.
- **L/R/M/N Shortcut for Candidate Keys:**
  - **L (Left-only) + N (Neither):** Must appear in **every** candidate key ( call this core $C$). If $C^+ = R$, then $C$ is the **unique** candidate key!
  - **R (Right-only):** Never appears in any candidate key.
  - **M (Middle: both sides):** Test combinations of $C$ with attributes from $M$ in increasing size order.
- **Boss Note:** [T08.4: Attribute Closure and Finding Candidate Keys](T08.04_Attribute_Closure_and_Candidate_Keys.md) · **Last Tested:** `2021 Q.5(b)`, `CT-03 Q.01(a)`

### 4.3 Extraneous Attribute & Canonical Cover ($F_c$) Test
Given FD set $F$ and $\alpha \to \beta \in F$:
1. **Testing $A \in \alpha$ (Left-hand side):** Attribute $A$ is extraneous in $\alpha$ iff $(\alpha - \{A\})^+$ computed under $F$ contains $\beta$.
2. **Testing $A \in \beta$ (Right-hand side):** Attribute $A$ is extraneous in $\beta$ iff $\alpha^+$ computed under the modified FD set $F' = (F - \{\alpha \to \beta\}) \cup \{\alpha \to (\beta - \{A\})\}$ still contains $A$.

- **Boss Note:** [T08.5: Canonical Cover of Functional Dependencies](T08.05_Canonical_Cover.md) · **Last Tested:** `2021 Q.6(a, b)`

### 4.4 Normal Form Hierarchy (1NF $\supset$ 2NF $\supset$ 3NF $\supset$ BCNF)

| Normal Form | Formal Condition (for every non-trivial FD $\alpha \to \beta$ where $\beta \not\subseteq \alpha$) | What It Eliminates | Boss Note & Last Tested |
| :--- | :--- | :--- | :--- |
| **1NF** | Every attribute domain is **atomic** (no multivalued cells, repeating groups, or composite lists) | Non-atomic / repeating groups | [T08.6](T08.06_Normal_Forms_1NF_2NF_3NF.md), [T08.8a](T08.08a_Normalization_Walkthrough_I.md) (`2024 Q.3(a)`) |
| **2NF** | In 1NF **and** no **non-prime** attribute $A$ is partially dependent on any candidate key $K$ (i.e., no proper subset $\alpha \subset K$ determines a non-prime $A$) | **Partial functional dependencies** | [T08.6](T08.06_Normal_Forms_1NF_2NF_3NF.md), [T08.7](T08.07_2NF_Test_from_FDs.md) (`2021 Q.5(c)`) |
| **3NF** | For every non-trivial $\alpha \to \beta$: **either** (a) $\alpha$ is a **superkey**, **or** (b) every attribute $A \in \beta - \alpha$ is a **prime attribute** (part of some candidate key) | **Transitive dependencies** of non-prime attributes | [T08.6](T08.06_Normal_Forms_1NF_2NF_3NF.md), [T08.8b](T08.08b_Normalization_Walkthrough_II.md) (`2023 Q.2(a)`) |
| **BCNF** | For every non-trivial $\alpha \to \beta$: $\alpha$ **must be a superkey** of $R$ (no prime-attribute exception!) | All FD-based redundancy (including prime-attribute dependencies) | [T08.9](T08.09_BCNF.md) (`CT-03 Q.01(d)`, `CT-03 Q.04`) |

### 4.5 Lossless-Join & Dependency Preservation Tests
For a binary decomposition of $R$ into $R_1$ and $R_2$ (where $R_1 \cup R_2 = R$):

$$
\text{Lossless-Join Condition:} \quad (R_1 \cap R_2) \to R_1 \in F^+ \quad \text{OR} \quad (R_1 \cap R_2) \to R_2 \in F^+
$$

Equivalently, compute the attribute closure $(R_1 \cap R_2)^+$ under $F$: the decomposition is **lossless** if and only if $R_1 \subseteq (R_1 \cap R_2)^+$ or $R_2 \subseteq (R_1 \cap R_2)^+$.

$$
\text{Dependency Preservation Condition:} \quad \left(\bigcup_{i=1}^{k} F_i\right)^+ = F^+
$$

- **Boss Note:** [T08.11: Lossless-Join Decomposition and Dependency Preservation](T08.11_Lossless_Join_and_Dependency_Preservation.md)

---

## 5. Transactions, Serializability & Concurrency Control (`T09`, `T10`, `T11`)

### 5.1 Instruction Conflict Rules & Precedence Graph $G = (V, E)$
Two instructions $I_i$ (of transaction $T_i$) and $I_j$ (of transaction $T_j$, $i \neq j$) on the **same data item $Q$** conflict iff at least one is a `write(Q)`:

$$
\begin{aligned}
I_i = \text{read}(Q), \; I_j = \text{read}(Q) &\implies \text{No conflict (commute)} \\
I_i = \text{read}(Q), \; I_j = \text{write}(Q) &\implies \text{Conflict (R-W)} \implies \text{Edge } T_i \to T_j \\
I_i = \text{write}(Q), \; I_j = \text{read}(Q) &\implies \text{Conflict (W-R)} \implies \text{Edge } T_i \to T_j \\
I_i = \text{write}(Q), \; I_j = \text{write}(Q) &\implies \text{Conflict (W-W)} \implies \text{Edge } T_i \to T_j
\end{aligned}
$$

- **Cycle Criterion:** Schedule $S$ is **conflict serializable** iff its precedence graph $G=(V,E)$ is **acyclic** (has no directed cycle). Equivalent serial schedules are given by all valid **topological sort** orders of $G$.
- **View Serializability & Blind Write Shortcut:** Every conflict-serializable schedule is view serializable. A schedule that is **not** conflict serializable can be view serializable **only if it contains a blind write** (a `write(Q)` without a preceding `read(Q)`).
- **Boss Notes:** [T10.1](T10.01_Conflicting_Instructions.md), [T10.3a](T10.03a_Precedence_Graph_Method.md), [T10.5](T10.05_View_Serializability.md) · **Last Tested:** `2024 Q.8(c)`, `2023 Q.8(b)`, `2020 Q.6(b)`

### 5.2 Lock Compatibility Matrix (`lock-S` vs. `lock-X`)

| Requested Mode $\backslash$ Held Mode | `S` (Shared) | `X` (Exclusive) |
| :--- | :---: | :---: |
| **`S` (Shared)** | `true` (Compatible) | `false` (Conflict: Wait) |
| **`X` (Exclusive)** | `false` (Conflict: Wait) | `false` (Conflict: Wait) |

- **Boss Note:** [T11.1: Shared and Exclusive Locks & Compatibility Matrix](T11.01_Shared_Exclusive_Locks.md) · **Last Tested:** `2017 Q.6(b)`, `2017 Q.7(a)`

### 5.3 Deadlock Prevention: `wait-die` vs. `wound-wait`
Suppose transaction $T_i$ requests a data item currently held in a conflicting lock mode by $T_j$:

| Scheme | Type | $TS(T_i) < TS(T_j)$ ($T_i$ is **Older**) | $TS(T_i) > TS(T_j)$ ($T_i$ is **Younger**) | Timestamp on Rollback |
| :--- | :--- | :--- | :--- | :--- |
| **`wait-die`** | Non-preemptive | Older $T_i$ **waits** for $T_j$ | Younger $T_i$ **dies** (rolls back) | **Retains ORIGINAL timestamp** (prevents starvation) |
| **`wound-wait`** | Preemptive | Older $T_i$ **wounds** (rolls back) younger $T_j$ | Younger $T_i$ **waits** for $T_j$ | **Retains ORIGINAL timestamp** (prevents starvation) |

- **Boss Note:** [T11.5: Wait-Die vs. Wound-Wait Deadlock Prevention](T11.05_Wait_Die_vs_Wound_Wait.md)

### 5.4 Timestamp-Ordering (TSO) Protocol Rules
Each transaction $T_i$ gets timestamp $TS(T_i)$. Each data item $Q$ maintains $\text{W-timestamp}(Q)$ and $\text{R-timestamp}(Q)$:

1. **$T_i$ issues $\text{read}(Q)$:**
   - If $TS(T_i) < \text{W-timestamp}(Q)$: **Reject** `read(Q)`, roll back $T_i$, and restart $T_i$ with a **NEW timestamp**.
   - If $TS(T_i) \ge \text{W-timestamp}(Q)$: **Execute** `read(Q)` and update:
     $$
     \text{R-timestamp}(Q) := \max\!\big(\text{R-timestamp}(Q),\, TS(T_i)\big)
     $$
2. **$T_i$ issues $\text{write}(Q)$:**
   - If $TS(T_i) < \text{R-timestamp}(Q)$ or $TS(T_i) < \text{W-timestamp}(Q)$: **Reject** `write(Q)`, roll back $T_i$, and restart $T_i$ with a **NEW timestamp**. *(Note: Under **Thomas' Write Rule**, if $TS(T_i) \ge \text{R-timestamp}(Q)$ and $TS(T_i) < \text{W-timestamp}(Q)$, the obsolete `write(Q)` is simply ignored without rolling back $T_i$.)*
   - Otherwise: **Execute** `write(Q)` and update:
     $$
     \text{W-timestamp}(Q) := TS(T_i)
     $$

- **Boss Note:** [T11.6: Timestamp-Ordering (TSO) Protocol](T11.06_Timestamp_Ordering.md) · **Last Tested:** `2024 Q.8(b)`, `2023 Q.8(c)`, `2018 Q.6(b)`

---

## 6. Recovery, RAID & Indexing/Hashing (`T12`, `T13`)

### 6.1 Log-Based Recovery: `undo` vs. `redo` Classification at Crash
Given a write-ahead log (WAL) starting from the most recent `<checkpoint L>` record:

$$
\begin{aligned}
\text{Redo-List (forward scan):} \quad & T_i \text{ has } \langle T_i, \text{commit}\rangle \text{ or } \langle T_i, \text{abort}\rangle \text{ in log} \implies \text{redo}(T_i) \text{ sets } X := V_{\text{new}} \\
\text{Undo-List (backward scan):} \quad & T_i \text{ has } \langle T_i, \text{start}\rangle \text{ but NO } \langle T_i, \text{commit}\rangle/\langle T_i, \text{abort}\rangle \implies \text{undo}(T_i) \text{ restores } X := V_{\text{old}}
\end{aligned}
$$

- **Boss Note:** [T12.3: Log-Based Recovery and Shadow Paging](T12.03_Log_Based_Recovery_and_Shadow_Paging.md) · **Last Tested:** `2023 Q.7(b)`, `2017 Q.6(d)`

### 6.2 RAID Levels Comparison ($N$ Total Disks)

| RAID Level | Architecture | Usable Capacity ($N$ Disks) | Disks Needed for $D$ Data Disks | Max Simultaneous Disk Failures Survived | Boss Note & Last Tested |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **RAID 0** | Block-level striping (no redundancy) | $N$ | $D$ | **0** (any single failure loses data) | [T12.4](T12.04_RAID_Levels.md) (`2024 Q.7(c)`) |
| **RAID 1** | Disk mirroring | $\frac{N}{2}$ | $2D$ | **1** (up to $\frac{N}{2}$ if in different mirror pairs) | [T12.4](T12.04_RAID_Levels.md) (`2024 Q.7(c)`) |
| **RAID 1+0** | Striped mirrors (mirror pairs, then stripe) | $\frac{N}{2}$ | $2D$ | **1** guaranteed (more if not same pair) | [T12.4](T12.04_RAID_Levels.md) (`2023 Q.4(a)`) |
| **RAID 3 / 4** | Bit-interleaved (3) / Block-interleaved (4) dedicated parity disk | $N - 1$ | $D + 1$ | **1** | [T12.4](T12.04_RAID_Levels.md) (`2023 Q.4(a)`) |
| **RAID 5** | Block-interleaved **distributed parity** ($P$) | $N - 1$ | $D + 1$ | **1** (eliminates single parity disk write bottleneck) | [T12.4](T12.04_RAID_Levels.md) (`2024 Q.7(c)`) |
| **RAID 6** | Block-interleaved **dual distributed parity** ($P + Q$, Reed-Solomon) | $N - 2$ | $D + 2$ | **2** simultaneous disk failures | [T12.4](T12.04_RAID_Levels.md) (`2024 Q.7(c)`) |

### 6.3 Static Hashing Bucket Allocation & Extendable Hashing Depth
For a static hash file storing $N_r$ records where each bucket block holds $f_r$ records, with overflow fudge factor $d \approx 0.20$:

$$
B = \left\lceil \frac{N_r}{f_r} \times (1 + d) \right\rceil \approx 1.2 \times \frac{N_r}{f_r} \text{ buckets}
$$

In **Extendable (Dynamic) Hashing** with global directory depth $i$ and bucket $j$ local depth $i_j$:

$$
\text{Directory Size} = 2^i \text{ pointers}, \qquad \text{Pointers to Bucket } j = 2^{\,i - i_j}
$$

- **Split without directory doubling:** If $i_j < i$ on overflow, increment $i_j := i_j + 1$, allocate one new bucket, and re-point half of the $2^{i-i_j}$ directory slots.
- **Split with directory doubling:** If $i_j = i$ on overflow, increment global depth $i := i + 1$ (doubling directory size from $2^i$ to $2^{i+1}$), then split bucket $j$.
- **Boss Note:** [T13.4: Static vs. Dynamic Hashing](T13.04_Static_vs_Dynamic_Hashing.md) · **Last Tested:** `2017 Q.7(c)`

---

[← Previous: T13.4: Static vs. Dynamic Hashing](T13.04_Static_vs_Dynamic_Hashing.md) | [🏠 Index](00_Index.md) | [Next: 🏠 Index →](00_Index.md)

