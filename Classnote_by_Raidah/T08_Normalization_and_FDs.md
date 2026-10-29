# T08: Normalization & Functional Dependencies — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructor:** Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 5 | `subtopicwise_list.md` T08 (75 marks · 11.8% · 7/7 · 🔴)  
**Source Pages:** Pages 19–25

---

## 1. Why Normalize? (Redundancy & Anomalies)

<!-- Page 19 (Right) -->
<!-- Date: 16.08.2024 | Teacher: RAKIBUL SIR -->

### Sample Unnormalized Relation:
| Student_ID | Student_Name | Course | Instructor | Mobile |
| :--- | :--- | :--- | :--- | :--- |
| 01 | A | DBMS | I1 | 013... |
| 02 | B | AI | I2 | 0137... |
| 01 | A | AI | I2 | 0137... |

* **Why is Normalization needed?**
  * To eliminate database design anomalies and reduce redundant data.
* **Update Anomaly:** Instructor $I_2$'s mobile number changes. If updated in one row but not another, inconsistent information results.
* **Insert Anomaly:** Cannot insert a new instructor without assigning them to an enrolled student.
* **Delete Anomaly:** Deleting a student's enrollment in a course inadvertently deletes the entire record of the instructor teaching that course.

* **Row-Level Duplication:** Resolved via **Primary Key** selection.
* **Column-Level Duplication:** Resolved via **Normalization** through functional dependencies.

### Review of Key Definitions:
* **Candidate Key:** Minimal superkey $\rightarrow$ a superkey such that no proper subset is a candidate key.
* **Primary Key:** Chosen candidate key.
* **Alternate Key:** Remaining unchosen candidate keys.
* **Superkey:** Primary key + other attributes (any combination of attributes that uniquely identifies tuples).
* **Foreign Key:** References the primary key of another relation.
* **Composite Key:** Combination of multiple attributes that collectively identify records uniquely when no single attribute suffices.

---

## 2. Functional Dependencies & Armstrong's Axioms

<!-- Page 20 (Left, Right) -->

A functional dependency (FD) describes a relationship between attribute sets:
$$X \rightarrow Y \quad (X \text{ determines } Y)$$

### Classification of Functional Dependencies:

1. **Trivial Functional Dependency:**
   * $Y \subseteq X$ (The right-hand side is a subset of the left-hand side).
   * Example: $\{\text{Name}, \text{Roll}\} \rightarrow \{\text{Name}\}$
2. **Non-trivial Functional Dependency:**
   * $Y \nsubseteq X$ (No attribute on the right-hand side appears on the left-hand side, i.e., $X \cap Y = \emptyset$).
   * Example: $\{\text{Student\_ID}\} \rightarrow \{\text{Name}\}$
3. **Full Functional Dependency:**
   * $Y$ is dependent on the entire composite key $X$, and not on any proper subset of $X$.
   * Example: $\{\text{St\_ID}, \text{Course\_ID}\} \rightarrow \{\text{Grade}\}$
4. **Partial Functional Dependency:**
   * $Y$ depends on a part (proper subset) of a composite candidate key.
   * Example: $\{\text{ID}, \text{Course\_ID}\} \rightarrow \text{Name}$ (since $\text{ID} \rightarrow \text{Name}$).
5. **Transitive Dependency:**
   * Functional dependency between non-key attributes:
   $$\text{Roll} \longrightarrow \text{Division} \longrightarrow \text{District} \longrightarrow \text{Thana}$$
   $$\text{Candidate Key} \longrightarrow \text{Non-key} \longrightarrow \text{Non-key}$$

### Prime vs. Non-Prime Attributes:
* **Prime Attribute:** Belongs to at least one candidate key.
* **Non-prime Attribute:** Does not belong to any candidate key.

---

<!-- Page 20 (Right) -->

### Armstrong's Axioms (Sound and Complete Rules):

1. **Reflexivity Rule:**
   $$\text{If } B \subseteq A, \text{ then } A \rightarrow B$$
   * Example: $\{\text{St\_ID}, \text{Name}\} \rightarrow \{\text{Name}\}$
2. **Augmentation Rule:**
   $$\text{If } A \rightarrow B, \text{ then } AC \rightarrow BC$$
   * Example: $\{\text{ID}\} \rightarrow \{\text{Name}\} \implies \{\text{ID}, \text{C\_ID}\} \rightarrow \{\text{Name}, \text{C\_ID}\}$
3. **Transitivity Rule:**
   $$\text{If } A \rightarrow B \text{ and } B \rightarrow C, \text{ then } A \rightarrow C$$
4. **Union / Additivity Rule:**
   $$\text{If } A \rightarrow B \text{ and } A \rightarrow C, \text{ then } A \rightarrow BC$$
5. **Decomposition Rule:**
   $$\text{If } A \rightarrow BC, \text{ then } A \rightarrow B \text{ and } A \rightarrow C$$
6. **Pseudotransitivity Rule:**
   $$\text{If } A \rightarrow B \text{ and } CB \rightarrow D, \text{ then } CA \rightarrow D$$

---

## 3. Attribute Closures ($X^+$) & Finding Candidate Keys

<!-- Page 21 (Left, Right) -->

### Example 1: Linear FD Chain
Given relation:
$$R(A, B, C, D, E), \quad FD = \{A \rightarrow B, \quad B \rightarrow C, \quad C \rightarrow D, \quad D \rightarrow E\}$$

* $A^+ = \{A, B, C, D, E\} \longrightarrow \text{Contains all attributes} \implies A \text{ is Candidate Key}$
* $B^+ = \{B, C, D, E\}$
* $C^+ = \{C, D, E\}$
* $D^+ = \{D, E\}$
* $E^+ = \{E\}$

* **Candidate Key:** $A$
* Any superset like $AB, AC, \dots$ is a **Superkey**.

---

<!-- Page 21 (Right) -->

### Example 2: Cyclic Dependencies
Given relation:
$$R(A, B, C, D), \quad FD = \{A \rightarrow B, \quad B \rightarrow C, \quad C \rightarrow D, \quad D \rightarrow A\}$$

* $A^+ = \{A, B, C, D\} \longrightarrow \text{Candidate Key}$
* $B^+ = \{B, C, D, A\} \longrightarrow \text{Candidate Key}$
* $C^+ = \{C, D, A, B\} \longrightarrow \text{Candidate Key}$
* $D^+ = \{D, A, B, C\} \longrightarrow \text{Candidate Key}$

* **Candidate Keys:** $\{A, B, C, D\}$
* **Prime Attributes:** $\{A, B, C, D\}$
* **Non-prime Attributes:** $\emptyset$ (empty set)

---

### Example 3: Missing Right-Hand Side Attributes
Given relation:
$$R(A, B, C, D, E), \quad FD = \{A \rightarrow B, \quad B \rightarrow C, \quad CD \rightarrow E\}$$

> [!TIP]
> Attributes that never appear on the right-hand side of any functional dependency MUST be part of every candidate key!  
> Here, $D$ is never on the right side $\implies D$ must be part of every candidate key.

* $A^+ = \{A, B, C\}$
* $B^+ = \{B, C\}$
* $C^+ = \{C\}$
* $D^+ = \{D\}$
* Composite key testing:
  $$(AD)^+ = \{A, B, C, D, E\} \longrightarrow \text{Candidate Key}$$
* **Candidate Key:** $AD$
* **Prime attributes:** $\{A, D\}$
* **Non-prime attributes:** $\{B, C, E\}$

---

## 4. Normal Forms (1NF, 2NF, 3NF, BCNF)

<!-- Page 22 (Left, Right) & Page 23 (Left) -->
<!-- Date: 23.08.2024 / 25.08.2024 -->

```text
+-------------------------------------------------------+
|  1NF: Atomic attribute values only                    |
+-------------------------------------------------------+
|  2NF: 1NF + No partial dependency                     |
+-------------------------------------------------------+
|  3NF: 2NF + No transitive dependency                  |
|       (For X -> Y: X is superkey OR Y is prime)       |
+-------------------------------------------------------+
|  BCNF: Stronger 3NF                                   |
|       (For every X -> Y: X must be a superkey)        |
+-------------------------------------------------------+
```

### Comprehensive Candidate Key Analysis:
Given relation:
$$FD = \{A \rightarrow B, \quad BC \rightarrow D, \quad E \rightarrow C, \quad D \rightarrow A\}$$

* $A^+ = \{A, B\}$
* $BC^+ = \{B, C, D, A\}$
* $E^+ = \{E, C\}$
* $(BE)^+ = \{B, E, C, D, A\} = \{A, B, C, D, E\} \longrightarrow \text{Candidate Key}$
* $(AE)^+ = \{A, E, B, C, D\} \longrightarrow \text{Candidate Key}$
* $(DE)^+ = \{D, E, A, B, C\} \longrightarrow \text{Candidate Key}$

* **Candidate Keys:** $\{BE, AE, DE\}$
* **Prime attributes:** $\{A, B, D, E\}$
* **Non-prime attribute:** $\{C\}$

---

<!-- Page 22 (Right) -->

### 3NF Condition Check:
Given:
$$R(A, B, C, D, E, F), \quad FD = \{A \rightarrow B, \quad C \rightarrow F, \quad CE \rightarrow D, \quad E \rightarrow A\}$$
$$(CE)^+ = \{C, E, F, D, A, B\} \implies CK = CE$$
* Prime: $\{C, E\}$
* Non-prime: $\{A, B, D, F\}$

Example sub-relation:
$$AB \rightarrow \text{Candidate Key}$$
* Prime: $\{A, B\}$, Non-prime: $\{C, D\}$
* $AB \rightarrow C$: $AB$ is superkey ✓
* $C \rightarrow D$: $C$ is non-prime, $D$ is non-prime $\implies$ **Transitive dependency!**
* It is not in Third Normal Form (3NF). Decompose into:
  $$R_1(A, B, C), \quad R_2(C, D)$$

---

<!-- Page 23 (Left) -->

### BCNF (Boyce-Codd Normal Form):

Given relation:
$$FD = \{AB \rightarrow CD, \quad D \rightarrow A\}$$
* $AB^+ = \{A, B, C, D\}$
* $BD^+ = \{B, D, A, C\}$
* $BC^+ = \{B, C\}$
* Prime attributes: $\{A, B, D\}$
* Non-prime attribute: $\{C\}$
* No partial dependency, no transitive dependency
* Candidate keys: $CK = \{AB, BD\}$

#### 3NF vs. BCNF:
* **In 3NF:** For $D \rightarrow A$, $A$ is a prime attribute $\implies$ Holds in 3NF ✓
* **In BCNF:** For every $X \rightarrow Y$, $X$ must be a superkey.
  * Here, $D$ is NOT a superkey (only a proper subset of candidate key $BD$).
  * Therefore, it **violates BCNF!**

---

## 5. Denormalization & Decomposition

<!-- Page 23 (Right), Page 24 (Left, Right) -->
<!-- Date: 08.09.2024 | Teacher: RI SIR -->

### Denormalization:
* **Advantages of Normalization:** Eliminates redundancy and anomalies, improves data consistency.
* **Disadvantages of Normalization:** Decomposes tables into many pieces, requiring costly join operations that degrade query response times.
* **When to Denormalize?**
  * When reading performance is critical, response times lag due to heavy joins, and data access is heavily read-dominated.

### Types of Decomposition:
1. **Lossless-Join Decomposition:**
   $$\Pi_{R_1}(R) \bowtie \Pi_{R_2}(R) = R$$
   * Natural join of decomposed sub-relations yields exactly the original relation without losing or introducing spurious tuples.
2. **Lossy Decomposition:**
   * Natural join generates spurious (ghost) tuples, corrupting original relationships.

---

<!-- Page 24 (Left) -->

### Conditions for Lossless-Join Decomposition:
Decomposition of $R$ into $R_1$ and $R_2$ is lossless if and only if:
$$(R_1 \cap R_2) \rightarrow R_1 \quad \text{OR} \quad (R_1 \cap R_2) \rightarrow R_2$$
*(The intersection attribute set must form a superkey of at least one decomposed sub-relation)*

#### Proof Example:
$$R(A, B, C), \quad FD = \{A \rightarrow B\}$$
Decomposed into:
$$R_1(A, B) \quad \text{and} \quad R_2(A, C)$$
1. $R_1 \cap R_2 = \{A\}$
2. $A^+ = \{A, B\} = R_1 \implies (R_1 \cap R_2) \rightarrow R_1$ holds.
3. Therefore, the decomposition is **Lossless**!

### Dependency Preservation:
* All functional dependencies in $F$ can be verified locally on individual decomposed relations without computing costly joins.

---

## 6. Comprehensive Worked Decomposition Problem

<!-- Page 25 (Left) -->
<!-- Date: 10.09.2024 -->

Given relation:
$$R(A, B, C, D, E, F)$$
$$FD = \{AB \rightarrow C, \quad C \rightarrow DE, \quad E \rightarrow F, \quad F \rightarrow A\}$$

1. **Candidate Keys:**
   * $AB^+ = \{A, B, C, D, E, F\}$
   * $BC^+ = \{B, C, D, E, F, A\}$
   * $BE^+ = \{B, E, F, A, C, D\}$
   * $BF^+ = \{B, F, A, C, D, E\}$
   * $\text{Candidate Keys} = \{AB, BC, BE, BF\}$
2. **Attribute Classes:**
   * $\text{Prime attributes} = \{A, B, C, E, F\}$
   * $\text{Non-prime attribute} = \{D\}$
3. **Anomaly Identification:**
   * In $C \rightarrow DE$: $C \rightarrow D$ is $\text{prime} \rightarrow \text{non-prime}$. Since $C$ is not a superkey, this violates 2NF/3NF/BCNF.
4. **Step-by-Step Lossless Decomposition:**
   * Decompose $R$ into:
     $$R_1(A, B, C, E, F) \quad \text{and} \quad R_2(C, D)$$
   * In $R_2(C, D)$: $C \rightarrow D$ holds, and $C$ is the candidate key of $R_2$ ✓
   * In $R_1(A, B, C, E, F)$: All attributes are prime, and FDs $\{AB \rightarrow C, E \rightarrow F, F \rightarrow A\}$ are preserved ✓

