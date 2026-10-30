---
title: "T08 · Normalization & Functional Dependencies: Part 2 · Canonical Cover & 3NF Synthesis"
tags: [ece2215, database-systems, silberschatz-exercises, topic-T08]
topic_id: T08
part: 2
exercise_count: 15
source_chapters: ["Chapter 07"]
---

[← Prev: T08 Part 1](T08_Part1_FDs_and_Armstrong_Axioms.md) | [Index](00_Index.md) | [Next: T08 Part 3 →](T08_Part3_BCNF_and_Advanced_Normalization.md)

---

# T08 · Normalization & Functional Dependencies: Part 2 · Canonical Cover & 3NF Synthesis

> [!info] Topic Card
> - **Topic ID:** T08
> - **Topic Title:** Normalization & Functional Dependencies
> - **Syllabus Unit:** Unit 5 (Normalization & Functional Dependencies)
> - **Total PYQ Marks:** 75 marks across 7 semester finals (11.8% course share; ranked #2 overall)
> - **Part 2 Scope:** Canonical cover algorithms ($F_c$), extraneous attribute testing, 3NF synthesis algorithm, lossless-join decomposition tests, dependency preservation, and design trade-offs.
> - **Exercises Included:** 15 problems (PE 7.1, PE 7.7, PE 7.10, EX 7.12, EX 7.13, EX 7.14, EX 7.15, EX 7.16, EX 7.19, EX 7.20, EX 7.22, EX 7.29, EX 7.32, EX 7.33, EX 7.38)
> - **Key Exam Hits:** PE 7.7 was recycled verbatim in **RUET 2021 Q.6(b) (5 Marks)**.

---

## Table of Exercises

| # | Exercise | Subtopic | Focus / Key Concepts | RUET Direct Hit / Status | Jump |
| :-: | :-- | :-- | :-- | :-- | :-: |
| 1 | **PE 7.7** | T08.5 | Canonical Cover $F_c$ Computation for $R=(A,B,C,D,E)$ | ⚠️ **Direct Hit: 2021 Q.6(b) [5m]** | [[#Exercise 7.7 · Canonical Cover Computation for R A B C D E\|Jump]] |
| 2 | **EX 7.14** | T08.5 | Existence of Multiple Distinct Canonical Covers | Core Theory / Textbook Drill | [[#Exercise 7.14 · Multiple Canonical Covers for a Set of FDs\|Jump]] |
| 3 | **EX 7.15** | T08.5 | Hazard of Simultaneous Extraneous Attribute Deletion | Algorithm Integrity / Trap Analysis | [[#Exercise 7.15 · Why Extraneous Attributes Must Be Removed Sequentially\|Jump]] |
| 4 | **EX 7.16** | T08.6 | Lossless Guarantee of 3NF Synthesis via Candidate Key | Theorem Proof / Bounding Tuples | [[#Exercise 7.16 · Candidate Key Inclusion Guarantees Lossless 3NF\|Jump]] |
| 5 | **EX 7.19** | T08.6, T08.7 | Proof that Every 3NF Schema is in 2NF | Formal Proof / Partial vs Transitive | [[#Exercise 7.19 · Proof That Every 3NF Schema is in Second Normal Form 2NF\|Jump]] |
| 6 | **EX 7.22** | T08.6 | Lossless, Dependency-Preserving 3NF Synthesis of $R$ | Synthesis Algorithm Step-by-Step | [[#Exercise 7.22 · 3NF Decomposition of Schema R from Exercise 7.1\|Jump]] |
| 7 | **EX 7.33** | T08.6 | Full 3NF Synthesis Drill (CKs, $F_c$, Sub-schema Pruning) | Comprehensive 10-Mark Exam Drill | [[#Exercise 7.33 · Comprehensive 3NF Decomposition Drill\|Jump]] |
| 8 | **PE 7.1** | T08.11 | Lossless-Join Decomposition Test for Binary Splitting | Fundamental Theorem & Tableau | [[#Exercise 7.1 · Lossless Decomposition Test for Binary Decomposition\|Jump]] |
| 9 | **PE 7.10** | T08.11 | Null Values on the LHS of Functional Dependencies | Lossless Breakdown / SQL Semantics | [[#Exercise 7.10 · Impact of Null Values on Functional Dependencies and Decomposition\|Jump]] |
| 10 | **EX 7.12** | T08.11 | Proof of Tuple Containment: $u \subseteq r_1 \bowtie \dots \bowtie r_n$ | Relational Algebra Core Proof | [[#Exercise 7.12 · Proof of Universal Tuple Containment in Natural Join\|Jump]] |
| 11 | **EX 7.13** | T08.11 | Proving Non-Preservation of Functional Dependencies | Dependency Projection / Closure Test | [[#Exercise 7.13 · Non-Preservation of Dependencies in Binary Decomposition\|Jump]] |
| 12 | **EX 7.29** | T08.11 | Lossy Decomposition & Spurious Tuples Counterexample | Concrete Instance Construction | [[#Exercise 7.29 · Lossy Decomposition Counterexample with Spurious Tuples\|Jump]] |
| 13 | **EX 7.32** | T08.11, T08.9 | Implied FDs, BCNF Splitting, Lossless & Dependency Tests | Multi-part Exam Comprehensive Drill | [[#Exercise 7.32 · Multi-part BCNF Analysis Implied FDs Lossless and Dependency Tests\|Jump]] |
| 14 | **EX 7.20** | T08.10 | Schema in BCNF but Violating 4NF (Multivalued Dependencies) | 4NF Anomaly & MVD Decomposition | [[#Exercise 7.20 · Schema in BCNF but not in 4NF\|Jump]] |
| 15 | **EX 7.38** | T08.10, T08.11 | Why Choose a Non-BCNF Design (Trade-offs & Denormalization) | Design Theory / Performance Analysis | [[#Exercise 7.38 · Why Choose a Non-BCNF Database Design\|Jump]] |

---

## T08.5 · Canonical Cover ($F_c$) & Extraneous Attribute Testing

### Exercise 7.7 · Canonical Cover Computation for R=(A, B, C, D, E)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Practice Exercise 7.7 (p. 354)
> - **Subtopic:** T08.5 (Canonical cover $F_c$)
> - **RUET Direct Hit:** ⚠️ **Recycled verbatim in RUET 2021 Q.6(b) [5 Marks]**
> - **Prerequisites:** Exercise 7.6 functional dependency set $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$

**Question (Silberschatz 7e Practice Exercise 7.7).**
Using the functional dependencies of Exercise 7.6, compute the canonical cover $F_c$.

*(From Exercise 7.6: Relation schema $R = (A, B, C, D, E)$ with functional dependency set $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.)*

#### 1. Core Principles & Concept Overview

A canonical cover $F_c$ for a set of functional dependencies $F$ is a minimal equivalent set of dependencies. It satisfies three strict conditions:
1. $F_c$ logically implies all dependencies in $F$, and $F$ logically implies all dependencies in $F_c$ ($F_c^+ = F^+$).
2. No functional dependency in $F_c$ contains an extraneous attribute.
3. Each left-hand side of a functional dependency in $F_c$ is unique.

An attribute is extraneous if you can delete it without altering the closure of the dependency set:
- **Testing LHS attribute $A$ in $\alpha \rightarrow \beta$:** Attribute $A$ is extraneous on the left-hand side if $\beta \subseteq (\alpha - \{A\})_F^+$. You compute the closure of the remaining LHS attributes under the original set $F$. If this closure still derives $\beta$, attribute $A$ is not needed.
- **Testing RHS attribute $B$ in $\alpha \rightarrow \beta$:** Attribute $B$ is extraneous on the right-hand side if $B \in \alpha_{F'}^+$, where $F' = (F - \{\alpha \rightarrow \beta\}) \cup \{\alpha \rightarrow (\beta - \{B\})\}$. You compute the closure of $\alpha$ under the modified set $F'$ where $B$ has been removed. If the remaining rules still derive $B$, attribute $B$ is redundant.

#### 2. Detailed Step-by-Step Solution

Given relation schema $R = (A, B, C, D, E)$ and dependency set:
$$
F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Step 1: Check uniqueness of left-hand sides**
Look at the LHS attribute sets:
- $A \rightarrow BC$ has LHS $\{A\}$
- $CD \rightarrow E$ has LHS $\{CD\}$
- $B \rightarrow D$ has LHS $\{B\}$
- $E \rightarrow A$ has LHS $\{E\}$

All left-hand sides are already distinct. No union rule application is needed at this stage.

**Step 2: Test for extraneous attributes**

**Check Dependency 1: $A \rightarrow BC$**
- **Test attribute $B$ on the RHS:**
  Remove $B$ from the RHS. The modified set is:
  $$
  F' = \{A \rightarrow C, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
  $$
  Compute $A^+$ under $F'$:
  - $A^{(0)} = \{A\}$
  - Apply $A \rightarrow C$: $A^{(1)} = \{A, C\}$
  - No other dependency in $F'$ can be triggered.
  - $A_{F'}^+ = \{A, C\}$
  
  Does $A_{F'}^+$ contain $B$? No, $B \notin \{A, C\}$.
  So $B$ is **not extraneous**.

- **Test attribute $C$ on the RHS:**
  Remove $C$ from the RHS. The modified set is:
  $$
  F' = \{A \rightarrow B, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
  $$
  Compute $A^+$ under $F'$:
  - $A^{(0)} = \{A\}$
  - Apply $A \rightarrow B$: $A^{(1)} = \{A, B\}$
  - Apply $B \rightarrow D$: $A^{(2)} = \{A, B, D\}$
  - To trigger $CD \rightarrow E$, we need both $C$ and $D$. But $C$ is not present.
  - $A_{F'}^+ = \{A, B, D\}$
  
  Does $A_{F'}^+$ contain $C$? No, $C \notin \{A, B, D\}$.
  So $C$ is **not extraneous**.

**Check Dependency 2: $CD \rightarrow E$**
- **Test attribute $C$ on the LHS:**
  Can $C$ be removed? We test if $D \rightarrow E$ holds under the current set $F$.
  Compute $D^+$ under $F$:
  - $D^{(0)} = \{D\}$
  - No rule in $F$ has LHS $\{D\}$.
  - $D_F^+ = \{D\}$
  
  Does $D_F^+$ contain $E$? No, $E \notin \{D\}$.
  So $C$ is **not extraneous**.

- **Test attribute $D$ on the LHS:**
  Can $D$ be removed? We test if $C \rightarrow E$ holds under the current set $F$.
  Compute $C^+$ under $F$:
  - $C^{(0)} = \{C\}$
  - No rule in $F$ has LHS $\{C\}$.
  - $C_F^+ = \{C\}$
  
  Does $C_F^+$ contain $E$? No, $E \notin \{C\}$.
  So $D$ is **not extraneous**.

**Check Dependency 3: $B \rightarrow D$**
Both LHS and RHS have a single attribute. Deleting either attribute would eliminate the dependency or make it trivial.
So neither $B$ nor $D$ is extraneous.

**Check Dependency 4: $E \rightarrow A$**
Both LHS and RHS have a single attribute.
So neither $E$ nor $A$ is extraneous.

**Step 3: Resulting Canonical Cover**
No attributes were extraneous. All left-hand sides remain unique.
The canonical cover is:
$$
F_c = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

*(Note: In minimal cover form with singleton right-hand sides, the set is written as $\{A \rightarrow B, A \rightarrow C, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$. Silberschatz defines $F_c$ with combined left-hand sides, so the union form is standard.)*

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Hit: RUET 2021 Q.6(b) [5 Marks]
> This exact question was asked in RUET 2021 Q.6(b). Students often lose marks because of two mistakes:
> 1. Stating the answer without testing each attribute. RUET examiners look for explicit closure calculations ($A_{F'}^+$, $D_F^+$, $C_F^+$) showing why attributes cannot be dropped.
> 2. Confusing the testing rule: for a LHS attribute, test under $F$; for a RHS attribute, test under the reduced set $F'$. Always state which set of rules you are using for each closure.

---

### Exercise 7.14 · Multiple Canonical Covers for a Set of FDs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.14 (p. 356)
> - **Subtopic:** T08.5 (Canonical cover properties)
> - **Focus:** Non-uniqueness of canonical covers and dependency cycle analysis

**Question (Silberschatz 7e Exercise 7.14).**
Show that there can be more than one canonical cover for a given set of functional dependencies, using the following set of dependencies:
$$
X \rightarrow YZ, \quad Y \rightarrow XZ, \quad \text{and} \quad Z \rightarrow XY
$$

#### 1. Core Principles & Concept Overview

A canonical cover is not always unique. The final canonical cover depends on the sequence in which extraneous attributes are tested and removed. When circular functional dependencies exist among attributes (such as $X \leftrightarrow Y \leftrightarrow Z$), removing an attribute in one step alters the closure calculations for subsequent steps. This leads to distinct, equally minimal, and fully equivalent canonical covers.

#### 2. Detailed Step-by-Step Solution

Given:
$$
F = \{X \rightarrow YZ, Y \rightarrow XZ, Z \rightarrow XY\}
$$
All three left-hand sides ($X, Y, Z$) are unique.

Notice that every attribute functionally determines every other attribute:
$$
X^+ = \{X, Y, Z\}, \quad Y^+ = \{X, Y, Z\}, \quad Z^+ = \{X, Y, Z\}
$$
All three attributes are equivalent keys.

**Derivation of Canonical Cover 1 ($F_{c1}$):**

1. **Check $X \rightarrow YZ$:**
   Test if $Z$ is extraneous on the RHS.
   Form $F' = \{X \rightarrow Y, Y \rightarrow XZ, Z \rightarrow XY\}$.
   Compute $X^+$ under $F'$:
   - $X^{(0)} = \{X\}$
   - Apply $X \rightarrow Y$: $X^{(1)} = \{X, Y\}$
   - Apply $Y \rightarrow XZ$: $X^{(2)} = \{X, Y, Z\}$
   
   Since $Z \in X_{F'}^+$, attribute $Z$ is **extraneous** in $X \rightarrow YZ$.
   Replace $X \rightarrow YZ$ with $X \rightarrow Y$.
   Current set:
   $$
   F_1 = \{X \rightarrow Y, Y \rightarrow XZ, Z \rightarrow XY\}
   $$

2. **Check $Y \rightarrow XZ$:**
   Test if $X$ is extraneous on the RHS.
   Form $F'' = \{X \rightarrow Y, Y \rightarrow Z, Z \rightarrow XY\}$.
   Compute $Y^+$ under $F''$:
   - $Y^{(0)} = \{Y\}$
   - Apply $Y \rightarrow Z$: $Y^{(1)} = \{Y, Z\}$
   - Apply $Z \rightarrow XY$: $Y^{(2)} = \{X, Y, Z\}$
   
   Since $X \in Y_{F''}^+$, attribute $X$ is **extraneous** in $Y \rightarrow XZ$.
   Replace $Y \rightarrow XZ$ with $Y \rightarrow Z$.
   Current set:
   $$
   F_2 = \{X \rightarrow Y, Y \rightarrow Z, Z \rightarrow XY\}
   $$

3. **Check $Z \rightarrow XY$:**
   Test if $Y$ is extraneous on the RHS.
   Form $F''' = \{X \rightarrow Y, Y \rightarrow Z, Z \rightarrow X\}$.
   Compute $Z^+$ under $F'''$:
   - $Z^{(0)} = \{Z\}$
   - Apply $Z \rightarrow X$: $Z^{(1)} = \{X, Z\}$
   - Apply $X \rightarrow Y$: $Z^{(2)} = \{X, Y, Z\}$
   
   Since $Y \in Z_{F'''}^+$, attribute $Y$ is **extraneous** in $Z \rightarrow XY$.
   Replace $Z \rightarrow XY$ with $Z \rightarrow X$.
   
4. **Final Check for $F_{c1}$:**
   Our set is now:
   $$
   F_{c1} = \{X \rightarrow Y, Y \rightarrow Z, Z \rightarrow X\}
   $$
   This forms a directed cycle: $X \rightarrow Y \rightarrow Z \rightarrow X$.
   No further attributes can be removed without breaking the cycle.
   Each left-hand side is unique.
   Therefore, $F_{c1}$ is a valid canonical cover.

**Derivation of Canonical Cover 2 ($F_{c2}$):**

Now make the alternate choices by testing the opposite RHS attributes:

1. In $X \rightarrow YZ$, test attribute $Y$ on the RHS:
   Form $F' = \{X \rightarrow Z, Y \rightarrow XZ, Z \rightarrow XY\}$.
   Compute $X^+$ under $F'$:
   - $X \rightarrow Z$ yields $\{X, Z\}$.
   - $Z \rightarrow XY$ yields $\{X, Y, Z\}$.
   
   $Y \in X_{F'}^+$, so $Y$ is extraneous.
   Replace $X \rightarrow YZ$ with $X \rightarrow Z$.

2. In $Z \rightarrow XY$, test attribute $X$ on the RHS:
   Form $F'' = \{X \rightarrow Z, Y \rightarrow XZ, Z \rightarrow Y\}$.
   Compute $Z^+$ under $F''$:
   - $Z \rightarrow Y$ yields $\{Y, Z\}$.
   - $Y \rightarrow XZ$ yields $\{X, Y, Z\}$.
   
   $X \in Z_{F''}^+$, so $X$ is extraneous.
   Replace $Z \rightarrow XY$ with $Z \rightarrow Y$.

3. In $Y \rightarrow XZ$, test attribute $Z$ on the RHS:
   Form $F''' = \{X \rightarrow Z, Y \rightarrow X, Z \rightarrow Y\}$.
   Compute $Y^+$ under $F'''$:
   - $Y \rightarrow X$ yields $\{X, Y\}$.
   - $X \rightarrow Z$ yields $\{X, Y, Z\}$.
   
   $Z \in Y_{F'''}^+$, so $Z$ is extraneous.
   Replace $Y \rightarrow XZ$ with $Y \rightarrow X$.

4. **Final Check for $F_{c2}$:**
   Our set is now:
   $$
   F_{c2} = \{X \rightarrow Z, Z \rightarrow Y, Y \rightarrow X\}
   $$
   This forms the reverse directed cycle: $X \rightarrow Z \rightarrow Y \rightarrow X$.
   Both $F_{c1}$ and $F_{c2}$ are minimal, contain no extraneous attributes, have unique left-hand sides, and satisfy:
   $$
   (F_{c1})^+ = (F_{c2})^+ = F^+
   $$

Therefore, more than one canonical cover exists for the given set of dependencies.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Examiner Tip
> If an exam question asks whether a canonical cover is unique, answer clearly: **No, canonical covers are generally not unique.** Provide this exact three-dependency circular system ($X \rightarrow YZ, Y \rightarrow XZ, Z \rightarrow XY$) as your formal proof. Show the clockwise cycle $F_{c1}$ and the counterclockwise cycle $F_{c2}$ to secure full marks.

---

### Exercise 7.15 · Why Extraneous Attributes Must Be Removed Sequentially

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.15 (p. 356)
> - **Subtopic:** T08.5 (Algorithm correctness)
> - **Focus:** The danger of parallel/simultaneous attribute elimination

**Question (Silberschatz 7e Exercise 7.15).**
The algorithm to generate a canonical cover only removes one extraneous attribute at a time. Use the functional dependencies from Exercise 7.14 to show what can go wrong if two attributes inferred to be extraneous are deleted at once.

#### 1. Core Principles & Concept Overview

The extraneous attribute test is context-dependent. When an attribute $A$ is determined to be extraneous in $\alpha \rightarrow \beta$, its redundancy relies on the existence of alternative derivation paths provided by the *other* dependencies in the set. If two attributes $A_1$ and $A_2$ are both found to be extraneous when evaluated independently, removing both simultaneously can destroy the very derivation paths that justified their removal. This causes an irreversible loss of functional dependencies, meaning $F_{new}^+ \subset F^+$.

#### 2. Detailed Step-by-Step Solution

From Exercise 7.14, we have:
$$
F = \{X \rightarrow YZ, Y \rightarrow XZ, Z \rightarrow XY\}
$$

Consider the single dependency:
$$
X \rightarrow YZ
$$

**Test 1: Check attribute $Y$ in isolation**
Assume we remove $Y$. Does $X \rightarrow Y$ still hold?
Using the other dependencies:
- $X \rightarrow Z$ gives $Z$.
- $Z \rightarrow XY$ gives $Y$.
So $Y$ is reachable from $X$. Thus, $Y$ is inferred to be extraneous.

**Test 2: Check attribute $Z$ in isolation**
Assume we remove $Z$. Does $X \rightarrow Z$ still hold?
Using the other dependencies:
- $X \rightarrow Y$ gives $Y$.
- $Y \rightarrow XZ$ gives $Z$.
So $Z$ is reachable from $X$. Thus, $Z$ is also inferred to be extraneous.

**Failure Case: Simultaneous Deletion**
Suppose the algorithm deletes both $Y$ and $Z$ at the same time from the right-hand side of $X \rightarrow YZ$.
The dependency becomes:
$$
X \rightarrow \emptyset
$$
This effectively removes the dependency $X \rightarrow YZ$ from the set entirely!
The resulting set is:
$$
F_{bad} = \{Y \rightarrow XZ, Z \rightarrow XY\}
$$

Now test the closure of $X$ under $F_{bad}$:
- $X^{(0)} = \{X\}$
- Neither $Y \rightarrow XZ$ nor $Z \rightarrow XY$ can be applied, because neither $Y$ nor $Z$ is in $X^{(0)}$.
- Therefore:
$$
X_{F_{bad}}^+ = \{X\}
$$

Under $F_{bad}$, $X$ cannot determine $Y$, and $X$ cannot determine $Z$:
$$
X \rightarrow Y \notin F_{bad}^+, \quad X \rightarrow Z \notin F_{bad}^+
$$
Hence:
$$
F_{bad}^+ \neq F^+
$$
The modified set is no longer equivalent to the original set of functional dependencies.

**General Principle:**
Deleting $Y$ relied on the path through $Z$ ($X \rightarrow Z \rightarrow Y$).
Deleting $Z$ relied on the path through $Y$ ($X \rightarrow Y \rightarrow Z$).
Deleting both at once destroys both paths. The algorithm must delete one attribute, update the working set $F$, and re-evaluate closures before attempting to delete another attribute.

#### 3. RUET Exam Insights & Examiner Notes

> [!note] Common Trap
> In algorithm design questions, examiners frequently ask: *"Can we parallelize the canonical cover reduction step?"*
> The answer is **No**. Extraneous attribute elimination is strictly sequential. If an attribute is removed, all subsequent extraneous tests must be performed against the updated set $F'$.

---

## T08.6 · Third Normal Form (3NF) & 3NF Synthesis Algorithm

### Exercise 7.16 · Candidate Key Inclusion Guarantees Lossless 3NF

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.16 (p. 356)
> - **Subtopic:** T08.6 (3NF synthesis algorithm properties)
> - **Focus:** Mathematical proof that candidate key inclusion ensures a lossless join

**Question (Silberschatz 7e Exercise 7.16).**
Show that it is possible to ensure that a dependency-preserving decomposition into 3NF is a lossless decomposition by guaranteeing that at least one schema contains a candidate key for the schema being decomposed. (*Hint:* Show that the join of all the projections onto the schemas of the decomposition cannot have more tuples than the original relation.)

#### 1. Core Principles & Concept Overview

Bernstein's 3NF synthesis algorithm creates a relation schema $R_i = \alpha \beta$ for every dependency $\alpha \rightarrow \beta$ in a canonical cover $F_c$. This directly guarantees dependency preservation.
However, this set of schemas might not yield a lossless join. To ensure a lossless join, the algorithm includes a final rule:
*If no schema $R_i$ contains a candidate key of the original schema $R$, add a new schema $R_k = K$, where $K$ is any candidate key of $R$.*

To prove this makes the decomposition lossless, we prove that the natural join of the projections contains exactly the tuples of the original relation:
$$
\Pi_{R_1}(u) \bowtie \Pi_{R_2}(u) \bowtie \cdots \bowtie \Pi_{R_m}(u) = u
$$

#### 2. Detailed Step-by-Step Solution

Let relation schema $R$ be decomposed into $\rho = \{R_1, R_2, \dots, R_m\}$.
Let $u$ be any legal relation instance on $R$ satisfying functional dependency set $F$.
Let $r_i = \Pi_{R_i}(u)$ for each $i \in \{1, 2, \dots, m\}$.
Let $J = r_1 \bowtie r_2 \bowtie \cdots \bowtie r_m$ denote the natural join of all projections.

**Part 1: Proof that $u \subseteq J$ (No tuples are lost)**
From Exercise 7.12, for any relation instance $u$ and any decomposition $\rho$:
Every tuple $t \in u$ projects to tuples $t_i = t[R_i] \in r_i$.
Because these projections all originate from the same tuple $t$, they are consistent on all shared attributes ($t_i[R_i \cap R_j] = t_j[R_i \cap R_j]$).
By definition of the natural join, these tuples join together to reconstruct $t$.
Therefore:
$$
u \subseteq J \implies |u| \le |J|
$$

**Part 2: Proof that $J \subseteq u$ via Candidate Key Bounding (No spurious tuples exist)**
We are given that at least one schema in the decomposition, say $R_j$, contains a candidate key $K$ of $R$ ($K \subseteq R_j$).

1. **Tuple count of $r_j$:**
   Because $K$ is a candidate key of $R$, no two distinct tuples in $u$ can have the same values on $K$.
   Since $K \subseteq R_j$, no two distinct tuples in $u$ can have the same values on $R_j$.
   Therefore, the projection $\Pi_{R_j}(u)$ retains every tuple as distinct:
   $$
   |r_j| = |\Pi_{R_j}(u)| = |u|
   $$

2. **Bounding the join size $|J|$:**
   Consider the join $J = r_1 \bowtie \dots \bowtie r_j \bowtie \dots \bowtie r_m$.
   Every tuple $t' \in J$ must project onto a valid tuple in each relation $r_i$. In particular:
   $$
   t'[R_j] \in r_j
   $$
   Can multiple tuples in $J$ have the identical value on $R_j$?
   Suppose two tuples $t_1', t_2' \in J$ agreed on $R_j$:
   $$
   t_1'[R_j] = t_2'[R_j] \implies t_1'[K] = t_2'[K]
   $$
   The decomposition $\rho$ is dependency-preserving, so all dependencies in $F^+$ hold on $J$.
   Since $K$ is a candidate key for $R$, we have $K \rightarrow R \in F^+$.
   Because $K \rightarrow R$ holds on $J$, the attributes of $K$ uniquely determine all attributes in $J$.
   Therefore, two distinct tuples in $J$ cannot agree on $K$:
   $$
   t_1'[K] = t_2'[K] \implies t_1' = t_2'
   $$
   This proves that each tuple in $r_j$ joins with at most one tuple from the other relations:
   $$
   |J| \le |r_j|
   $$

3. **Combining the inequalities:**
   Substitute $|r_j| = |u|$:
   $$
   |J| \le |u|
   $$
   From Part 1, we already know:
   $$
   |u| \le |J|
   $$
   Therefore:
   $$
   |J| = |u|
   $$

Since $u \subseteq J$ and both sets have the exact same finite number of tuples, they must be identical sets:
$$
J = u \iff \Pi_{R_1}(u) \bowtie \Pi_{R_2}(u) \bowtie \cdots \bowtie \Pi_{R_m}(u) = u
$$
This completes the proof that guaranteeing at least one schema contains a candidate key ensures the decomposition is lossless.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Key Concept for Theory Questions
> When asked why Bernstein's 3NF synthesis algorithm includes Step 3 ("Add a candidate key schema if none exists"), write:
> 1. Step 2 (schemas from $F_c$) guarantees **dependency preservation**.
> 2. Step 3 (adding candidate key $K$) guarantees the **lossless-join property**.
> 3. Together, they guarantee both properties hold simultaneously in 3NF.

---

### Exercise 7.19 · Proof That Every 3NF Schema is in Second Normal Form (2NF)

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.19 (pp. 356-357)
> - **Subtopic:** T08.6, T08.7 (Normal form hierarchy)
> - **Focus:** Proving $\text{3NF} \implies \text{2NF}$ via transitive and partial dependencies

**Question (Silberschatz 7e Exercise 7.19).**
A functional dependency $\alpha \rightarrow \beta$ is called a partial dependency if there is a proper subset $\gamma$ of $\alpha$ such that $\gamma \rightarrow \beta$; we say that $\beta$ is partially dependent on $\alpha$. A relation schema $R$ is in **second normal form** (2NF) if each attribute $A$ in $R$ meets one of the following criteria:
- It appears in a candidate key.
- It is not partially dependent on a candidate key.

Show that every 3NF schema is in 2NF. (*Hint:* Show that every partial dependency is a transitive dependency.)

#### 1. Core Principles & Concept Overview

- **Prime attribute:** An attribute that is a member of at least one candidate key of $R$.
- **Nonprime attribute:** An attribute that does not belong to any candidate key of $R$.
- **2NF condition:** No nonprime attribute is partially dependent on any candidate key.
- **3NF condition (Silberschatz):** For every nontrivial functional dependency $\alpha \rightarrow \beta$ holding on $R$, at least one of the following holds:
  1. $\alpha$ is a superkey of $R$, or
  2. Each attribute $A \in \beta - \alpha$ is a prime attribute.

#### 2. Detailed Step-by-Step Solution

We prove this by contradiction.

**Step 1: Assume the contrary**
Suppose relation schema $R$ is in 3NF, but $R$ is **not in 2NF**.

**Step 2: Identify the violation of 2NF**
Since $R$ violates 2NF, there must exist at least one attribute $A \in R$ such that:
1. $A$ does not appear in any candidate key of $R$ ($A$ is a nonprime attribute).
2. $A$ is partially dependent on some candidate key $K$ of $R$.

By definition of partial dependency, there exists a proper subset $\gamma \subset K$ such that:
$$
\gamma \rightarrow A
$$

**Step 3: Evaluate $\gamma \rightarrow A$ against the 3NF requirements**
Now consider this dependency $\gamma \rightarrow A$ on schema $R$:
- Is $\gamma \rightarrow A$ nontrivial?
  Yes. Since $A$ is nonprime, $A$ cannot be in candidate key $K$. Since $\gamma \subset K$, it follows that $A \notin \gamma$. Thus, the dependency is strictly nontrivial.
- Is $\gamma$ a superkey of $R$?
  No. $K$ is a candidate key, meaning it is a *minimal* superkey. By definition of minimality, no proper subset of a candidate key can be a superkey. Since $\gamma \subset K$, $\gamma$ cannot be a superkey.
- Is $A$ a prime attribute?
  No. By Step 2, $A$ is nonprime.

**Step 4: Reach a contradiction**
The dependency $\gamma \rightarrow A$ satisfies neither condition of 3NF:
- The left-hand side $\gamma$ is not a superkey.
- The right-hand side attribute $A$ is not prime.

This violates our assumption that $R$ is in 3NF.
Therefore, no such partial dependency can exist in a 3NF schema.
Every 3NF schema must be in 2NF.

**Alternative Direct Proof (Using the Textbook Hint):**
1. Let $A$ be a nonprime attribute partially dependent on candidate key $K$. Then $\gamma \rightarrow A$ for some proper subset $\gamma \subset K$.
2. We have $K \rightarrow \gamma$ by Armstrong's reflexivity axiom, because $\gamma \subset K$.
3. Also, $\gamma \not\rightarrow K$ because $K$ is minimal.
4. And $\gamma \rightarrow A$ with $A \notin K$.
5. This matches the definition of a **transitive dependency**:
   $$
   K \rightarrow \gamma \quad \text{and} \quad \gamma \rightarrow A
   $$
   where $\gamma \not\rightarrow K$ and $A \notin K$.
6. Third Normal Form explicitly forbids any nonprime attribute from being transitively dependent on a candidate key.
7. Because every partial dependency is a transitive dependency, removing all transitive dependencies on nonprime attributes automatically removes all partial dependencies.
8. Hence, $\text{3NF} \implies \text{2NF}$.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Exam Structure Note
> Questions comparing normal forms frequently appear in RUET (e.g., 2017 Q.3(a), 2019 Q.3(a), CT-03 Q.03).
> When proving normal form containment, always use the prime / nonprime attribute definitions. Memorize this one-line summary:
> *"Every partial dependency is a special case of a transitive dependency where the intermediate set $\gamma$ is a proper subset of the key."*

---

### Exercise 7.22 · 3NF Decomposition of Schema R from Exercise 7.1

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.22 (p. 357)
> - **Subtopic:** T08.6 (3NF synthesis algorithm execution)
> - **Schema:** $R = (A, B, C, D, E)$ with $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$

**Question (Silberschatz 7e Exercise 7.22).**
Give a lossless, dependency-preserving decomposition into 3NF of schema $R$ of Exercise 7.1.

#### 1. Core Principles & Concept Overview

To generate a decomposition that is guaranteed to be both lossless and dependency-preserving in 3NF, we execute Bernstein's 3NF Synthesis Algorithm:
1. Compute the canonical cover $F_c$ for $F$.
2. For each dependency $\alpha \rightarrow \beta \in F_c$, create a relation schema $R_i = \alpha \beta$.
3. Check if at least one schema $R_i$ contains a candidate key for $R$. If not, create an additional schema containing any candidate key $K$.
4. Remove any redundant schema $R_i$ that is a subset of another schema $R_j$.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E)$ and:
$$
F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Step 1: Compute Canonical Cover $F_c$**
From our complete derivation in Exercise 7.7, the canonical cover is:
$$
F_c = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Step 2: Generate schemas from dependencies in $F_c$**
- From $A \rightarrow BC$: create schema $R_1 = (A, B, C)$
- From $CD \rightarrow E$: create schema $R_2 = (C, D, E)$
- From $B \rightarrow D$: create schema $R_3 = (B, D)$
- From $E \rightarrow A$: create schema $R_4 = (A, E)$

**Step 3: Check candidate keys of $R$**
Find all candidate keys of $R$:
- Test $A$: $A^+ = \{A, B, C, D, E\} = R$. So $A$ is a candidate key.
- Test $E$: $E \rightarrow A \implies E^+ = \{A, B, C, D, E\} = R$. So $E$ is a candidate key.
- Test $CD$: $CD \rightarrow E \rightarrow A \implies CD^+ = R$. Since $C^+ = \{C\}$ and $D^+ = \{D\}$, $CD$ is a minimal candidate key.
- Test $BC$: $B \rightarrow D \implies BC \rightarrow CD \rightarrow E \rightarrow A \implies BC^+ = R$. Since $B^+ = \{B, D\}$ and $C^+ = \{C\}$, $BC$ is a minimal candidate key.

The candidate keys of $R$ are:
$$
\{A\}, \quad \{E\}, \quad \{CD\}, \quad \{BC\}
$$

Now check if any generated schema contains a candidate key:
- $R_1 = (A, B, C)$ contains candidate key $\{A\}$ (and also $\{BC\}$).
- $R_2 = (C, D, E)$ contains candidate key $\{CD\}$.
- $R_4 = (A, E)$ contains candidate keys $\{A\}$ and $\{E\}$.

Since at least one schema contains a candidate key of $R$, **no additional candidate key schema is required**.

**Step 4: Check for schema redundancy**
Check if any schema is a proper subset of another:
- $R_1 = \{A, B, C\} \not\subseteq R_j$
- $R_2 = \{C, D, E\} \not\subseteq R_j$
- $R_3 = \{B, D\} \not\subseteq R_j$ (neither $R_1$ nor $R_2$ contains both $B$ and $D$)
- $R_4 = \{A, E\} \not\subseteq R_j$

No schema is a subset of another. All four schemas are retained.

**Step 5: Final 3NF Decomposition**
$$
\rho = \{R_1(A, B, C), R_2(C, D, E), R_3(B, D), R_4(A, E)\}
$$

**Properties verified:**
1. **3NF:** Every dependency holds on a schema where the LHS is a superkey (e.g., $A$ is a key in $R_1$, $CD$ is a key in $R_2$, $B$ is a key in $R_3$, $E$ is a key in $R_4$).
2. **Dependency Preservation:** Each dependency in $F_c$ belongs entirely to one decomposed schema.
3. **Lossless Join:** Guaranteed because $R_1, R_2, R_4$ contain candidate keys of $R$.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Crucial Comparison with Exercise 7.1
> In Exercise 7.1, decomposing $R$ into just $(A, B, C)$ and $(A, D, E)$ was lossless, but Exercise 7.13 shows it **lost** the dependency $B \rightarrow D$.
> The 3NF synthesis algorithm here generates four relations:
> $$
> \{R_1(A, B, C), R_2(C, D, E), R_3(B, D), R_4(A, E)\}
> $$
> Notice that $R_3(B, D)$ is present. This explicitly preserves $B \rightarrow D$. Explain this difference to show mastery of the material.

---

### Exercise 7.33 · Comprehensive 3NF Decomposition Drill

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.33 (p. 359)
> - **Subtopic:** T08.6 (Full 3NF synthesis pipeline)
> - **Focus:** Full 4-part problem: candidate keys, canonical cover, algorithm steps, and sub-schema elimination

**Question (Silberschatz 7e Exercise 7.33).**
Consider the schema $R = (A, B, C, D, E, G)$ and the set $F$ of functional dependencies:
$$
AB \rightarrow CD
$$
$$
ADE \rightarrow GDE
$$
$$
B \rightarrow GC
$$
$$
G \rightarrow DE
$$

Use the 3NF decomposition algorithm to generate a 3NF decomposition of $R$, and show your work. This means:
a. A list of all candidate keys
b. A canonical cover for $F$, along with an explanation of the steps you took to generate it
c. The remaining steps of the algorithm, with explanation
d. The final decomposition

#### 1. Core Principles & Concept Overview

This exercise walks through the complete 3NF synthesis algorithm. It tests:
1. Candidate key identification using attribute closure.
2. Eliminating trivial RHS attributes, testing for extraneous LHS attributes, and merging identical left-hand sides.
3. Applying the candidate key rule to guarantee a lossless join.
4. Detecting and eliminating redundant sub-schemas.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E, G)$ and:
$$
F = \{AB \rightarrow CD, ADE \rightarrow GDE, B \rightarrow GC, G \rightarrow DE\}
$$

---

#### Part (a): List of all Candidate Keys

1. **Examine attribute occurrences:**
   Look at the attributes that never appear on the right-hand side of any dependency in $F$:
   - RHS of $AB \rightarrow CD$: contains $C, D$
   - RHS of $ADE \rightarrow GDE$: contains $G, D, E$
   - RHS of $B \rightarrow GC$: contains $G, C$
   - RHS of $G \rightarrow DE$: contains $D, E$

   Attributes $A$ and $B$ **never appear on the right-hand side**.
   Therefore, $\{A, B\}$ must be present in every candidate key of $R$.

2. **Compute the closure of $\{A, B\}$:**
   - $AB^{(0)} = \{A, B\}$
   - Apply $AB \rightarrow CD$: $AB^{(1)} = \{A, B, C, D\}$
   - Apply $B \rightarrow GC$: $AB^{(2)} = \{A, B, C, D, G\}$
   - Apply $G \rightarrow DE$: $AB^{(3)} = \{A, B, C, D, E, G\} = R$

   Since $AB^+ = R$, the attribute set $AB$ is a superkey.
   Since both $A$ and $B$ are essential, no proper subset of $AB$ can be a key.
   Any other candidate key would have to be a superset of $AB$, which would violate minimality.

**Result for (a):**
The only candidate key for $R$ is:
$$
\boxed{AB}
$$

---

#### Part (b): Compute the Canonical Cover $F_c$

**Step 1: Simplify trivial attributes on the RHS**
In $ADE \rightarrow GDE$, the attributes $D, E$ appear on both LHS and RHS.
By Armstrong's decomposition rule, $ADE \rightarrow GDE$ implies $ADE \rightarrow G$ and $ADE \rightarrow DE$.
$ADE \rightarrow DE$ is trivial. We drop $DE$ from the RHS.
The dependency becomes:
$$
ADE \rightarrow G
$$
Our working set is:
$$
F = \{AB \rightarrow CD, ADE \rightarrow G, B \rightarrow GC, G \rightarrow DE\}
$$

**Step 2: Check for extraneous attributes**

1. **Test $AB \rightarrow CD$:**
   Can we remove $A$ from the LHS?
   We test if $B \rightarrow CD$ holds under $F$ by computing $B_F^+$:
   - $B^{(0)} = \{B\}$
   - Apply $B \rightarrow GC$: $B^{(1)} = \{B, C, G\}$
   - Apply $G \rightarrow DE$: $B^{(2)} = \{B, C, D, E, G\}$
   
   Notice that $B^+$ contains both $C$ and $D$!
   Since $CD \subseteq B_F^+$, attribute $A$ is **extraneous** on the LHS of $AB \rightarrow CD$.
   We remove $A$. The dependency simplifies to:
   $$
   B \rightarrow CD
   $$

2. **Combine dependencies with identical LHS:**
   Now we have two dependencies with LHS $B$:
   - $B \rightarrow CD$
   - $B \rightarrow GC$
   
   Apply the union rule to combine them:
   $$
   B \rightarrow CDEG
   $$
   Our working set is now:
   $$
   F' = \{B \rightarrow CDEG, ADE \rightarrow G, G \rightarrow DE\}
   $$

3. **Test RHS of $B \rightarrow CDEG$ for extraneous attributes:**
   - **Test attribute $D$:**
     Remove $D$ from the RHS to get $B \rightarrow CEG$. Test if $B \rightarrow D$ holds using remaining rules.
     $B \rightarrow CEG$ gives $\{B, C, E, G\}$.
     Then $G \rightarrow DE$ gives $D$!
     So $D$ is derivable through $G$. Therefore, $D$ is **extraneous** on the RHS.
     Remove $D$. The dependency becomes $B \rightarrow CEG$.
   - **Test attribute $E$:**
     Remove $E$ from the RHS to get $B \rightarrow CG$. Test if $B \rightarrow E$ holds.
     $B \rightarrow CG$ gives $\{B, C, G\}$.
     Then $G \rightarrow DE$ gives $E$!
     So $E$ is derivable through $G$. Therefore, $E$ is **extraneous** on the RHS.
     Remove $E$. The dependency becomes $B \rightarrow CG$.
   - **Test attribute $C$:**
     If we remove $C$, $B \rightarrow G$ gives $\{B, G, D, E\}$. $C$ cannot be derived. Not extraneous.
   - **Test attribute $G$:**
     If we remove $G$, $B \rightarrow C$ gives $\{B, C\}$. $G$ cannot be derived. Not extraneous.

   Thus, $B \rightarrow CDEG$ reduces cleanly to:
   $$
   B \rightarrow CG
   $$

4. **Test $ADE \rightarrow G$ for extraneous attributes:**
   - Can we remove $A$? Test $DE^+$: $DE^+ = \{D, E\}$. $G \notin DE^+$. $A$ is not extraneous.
   - Can we remove $D$? Test $AE^+$: $AE^+ = \{A, E\}$. $G \notin AE^+$. $D$ is not extraneous.
   - Can we remove $E$? Test $AD^+$: $AD^+ = \{A, D\}$. $G \notin AD^+$. $E$ is not extraneous.
   None of $A, D, E$ is extraneous on the LHS.

5. **Test $G \rightarrow DE$ for extraneous attributes:**
   - Test $D$ on RHS: With $G \rightarrow E$, $G^+ = \{G, E\}$. $D \notin G^+$. Not extraneous.
   - Test $E$ on RHS: With $G \rightarrow D$, $G^+ = \{G, D\}$. $E \notin G^+$. Not extraneous.
   - $G$ is a single attribute on the LHS. Not extraneous.

**Result for (b):**
The canonical cover is:
$$
\boxed{F_c = \{B \rightarrow CG, G \rightarrow DE, ADE \rightarrow G\}}
$$

---

#### Part (c): Remaining Steps of the Algorithm

1. **Step 1: Create a relation schema for each dependency in $F_c$:**
   - From $B \rightarrow CG$: create $R_1 = (B, C, G)$
   - From $G \rightarrow DE$: create $R_2 = (D, E, G)$
   - From $ADE \rightarrow G$: create $R_3 = (A, D, E, G)$

2. **Step 2: Candidate key check:**
   The only candidate key of $R$ is $AB$.
   Inspect the schemas:
   - $R_1 = (B, C, G)$ does not contain $A$.
   - $R_2 = (D, E, G)$ contains neither $A$ nor $B$.
   - $R_3 = (A, D, E, G)$ does not contain $B$.

   None of the generated schemas contains the candidate key $AB$.
   Therefore, we must create an additional relation schema:
   $$
   R_4 = (A, B)
   $$

3. **Step 3: Redundancy check (Eliminate sub-schemas):**
   Compare each schema to see if its attribute set is a subset of another schema:
   - $R_1 = \{B, C, G\} \not\subseteq R_j$
   - $R_2 = \{D, E, G\} \subseteq R_3 = \{A, D, E, G\}$!
     Notice that all attributes of $R_2$ ($\{D, E, G\}$) are completely contained in $R_3$ ($\{A, D, E, G\}$).
     Therefore, **$R_2$ is redundant and must be eliminated**.
   - $R_3 = \{A, D, E, G\}$ is not a subset of any schema.
   - $R_4 = \{A, B\}$ is not a subset of any schema.

---

#### Part (d): Final Decomposition

After eliminating redundant schema $R_2$, the final 3NF decomposition is:
$$
\boxed{\rho = \{R_1(B, C, G), R_3(A, D, E, G), R_4(A, B)\}}
$$

**Final Check:**
- $R_1(B, C, G)$ preserves $B \rightarrow CG$ (candidate key $B$).
- $R_3(A, D, E, G)$ preserves $ADE \rightarrow G$ and $G \rightarrow DE$ (candidate keys $ADE$ and $AG$).
- $R_4(A, B)$ provides the candidate key of the original relation, guaranteeing a lossless join.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] High-Mark Exam Question Pattern
> This is a classic 8 to 10-mark semester-final question. Examiners check three specific steps:
> 1. In Part (b), recognizing that $A$ is extraneous on the LHS of $AB \rightarrow CD$ because $B \rightarrow CDEG$.
> 2. In Part (c), adding $R_4(A, B)$ because no schema has the candidate key.
> 3. In Part (c), deleting $R_2(D, E, G)$ because it is a subset of $R_3(A, D, E, G)$. Students who forget to delete $R_2$ lose 1 to 2 marks.

---

## T08.11 · Lossless-Join Decomposition & Dependency Preservation

### Exercise 7.1 · Lossless Decomposition Test for Binary Decomposition

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Practice Exercise 7.1 (p. 354)
> - **Subtopic:** T08.11 (Lossless-join decomposition tests)
> - **Focus:** Fundamental theorem of binary lossless decomposition and Tableau method

**Question (Silberschatz 7e Practice Exercise 7.1).**
Suppose that we decompose the schema $R = (A, B, C, D, E)$ into
$$
(A, B, C)
$$
$$
(A, D, E)
$$
Show that this decomposition is a lossless decomposition if the following set $F$ of functional dependencies holds:
$$
A \rightarrow BC
$$
$$
CD \rightarrow E
$$
$$
B \rightarrow D
$$
$$
E \rightarrow A
$$

#### 1. Core Principles & Concept Overview

For a binary decomposition of schema $R$ into $R_1$ and $R_2$, the decomposition is a **lossless-join decomposition** with respect to $F$ if and only if at least one of the following functional dependencies is in $F^+$:
1. $R_1 \cap R_2 \rightarrow R_1$
2. $R_1 \cap R_2 \rightarrow R_2$

In simple terms: the common attributes of $R_1$ and $R_2$ must form a superkey for at least one of the decomposed schemas.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E)$ and:
$$
R_1 = (A, B, C), \quad R_2 = (A, D, E)
$$
$$
F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Step 1: Identify the shared attribute set**
$$
R_1 \cap R_2 = (A, B, C) \cap (A, D, E) = \{A\}
$$

**Step 2: Compute the attribute closure of the common attribute set under $F$**
We compute $A^+$:
- $A^{(0)} = \{A\}$
- Using $A \rightarrow BC$: $A^{(1)} = \{A, B, C\}$
- Using $B \rightarrow D$: $A^{(2)} = \{A, B, C, D\}$
- Using $CD \rightarrow E$: since $\{C, D\} \subseteq A^{(2)}$, we add $E$:
  $A^{(3)} = \{A, B, C, D, E\} = R$

Thus:
$$
A^+ = \{A, B, C, D, E\}
$$

**Step 3: Test the superkey conditions**
1. Does $R_1 \cap R_2 \rightarrow R_1$ hold?
   We test if $A \rightarrow (A, B, C)$.
   Since $\{A, B, C\} \subseteq A^+$, the dependency $A \rightarrow (A, B, C)$ holds.
   Therefore, $R_1 \cap R_2$ is a superkey for $R_1$.

2. Does $R_1 \cap R_2 \rightarrow R_2$ hold?
   We test if $A \rightarrow (A, D, E)$.
   Since $\{A, D, E\} \subseteq A^+$, the dependency $A \rightarrow (A, D, E)$ also holds.
   Therefore, $R_1 \cap R_2$ is also a superkey for $R_2$.

Since both conditions hold (satisfying either one is sufficient), the decomposition is **guaranteed to be lossless**.

**Alternative Verification: The Tableau (Chase) Method**
Let columns represent attributes $(A, B, C, D, E)$ and rows represent relations $R_1, R_2$.
Distinguished symbols are $a_i$; non-distinguished symbols are $b_{ij}$.

Initial Tableau:
$$
\begin{array}{c|ccccc}
\text{Relation} & A & B & C & D & E \\
\hline
R_1 & a_1 & a_2 & a_3 & b_{14} & b_{15} \\
R_2 & a_1 & b_{22} & b_{23} & a_4 & a_5 \\
\end{array}
$$

1. Apply $A \rightarrow BC$:
   Both rows agree on $A$ ($a_1$). Therefore, equate their $B$ and $C$ symbols.
   Change $b_{22} \rightarrow a_2$ and $b_{23} \rightarrow a_3$:
   $$
   \begin{array}{c|ccccc}
   \text{Relation} & A & B & C & D & E \\
   \hline
   R_1 & a_1 & a_2 & a_3 & b_{14} & b_{15} \\
   R_2 & a_1 & a_2 & a_3 & a_4 & a_5 \\
   \end{array}
   $$

Row 2 now consists entirely of distinguished symbols: $(a_1, a_2, a_3, a_4, a_5)$.
Because a row of all distinguished symbols was formed, the Chase terminates successfully.
The decomposition is lossless.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Quick Scoring Strategy
> In RUET exams, always write the theorem statement first:
> $$
> R_1 \cap R_2 \rightarrow R_1 \in F^+ \quad \text{or} \quad R_1 \cap R_2 \rightarrow R_2 \in F^+
> $$
> Then show the step-by-step closure derivation $A^{(0)} \rightarrow A^{(1)} \rightarrow A^{(2)} \rightarrow A^{(3)}$. This two-step structure takes under 3 minutes and guarantees full marks.

---

### Exercise 7.10 · Impact of Null Values on Functional Dependencies and Decomposition

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Practice Exercise 7.10 (p. 354)
> - **Subtopic:** T08.11 (Decomposition anomalies under nulls)
> - **Focus:** Failure of lossless-join property in the presence of SQL NULLs

**Question (Silberschatz 7e Practice Exercise 7.10).**
Our discussion of lossless decomposition implicitly assumed that attributes on the left-hand side of a functional dependency cannot take on null values. What could go wrong on decomposition, if this property is violated?

#### 1. Core Principles & Concept Overview

In relational theory, every attribute has a definite value. In commercial SQL databases, attributes can contain `NULL` to represent missing or unknown values.
SQL evaluates comparisons with `NULL` using three-valued logic (`UNKNOWN`). Specifically:
$$
\text{NULL} = \text{NULL} \implies \text{UNKNOWN}
$$
In a standard SQL natural join (or inner join on common attributes), tuples match only when the join condition evaluates to `TRUE`. Because `UNKNOWN` is treated as false in `WHERE` and `ON` clauses, rows containing `NULL` on the join attributes **do not match any row**, including rows with identical null values.

#### 2. Detailed Step-by-Step Solution

Two major problems arise when the left-hand side of a functional dependency contains null values during decomposition:

**Problem 1: Tuple Loss in Natural Join (Loss of Information)**
Consider schema $R(A, B, C)$ with functional dependency $A \rightarrow B$.
Decompose $R$ into $R_1(A, B)$ and $R_2(A, C)$.
The common attribute is $A$.

Suppose relation instance $r$ contains a tuple where $A$ is null:
$$
t_1 = (\text{null}, b_1, c_1)
$$
Project $r$ onto the decomposed schemas:
- $\Pi_{A, B}(r)$ contains $(\text{null}, b_1)$
- $\Pi_{A, C}(r)$ contains $(\text{null}, c_1)$

Now compute the standard natural join:
$$
\Pi_{A, B}(r) \bowtie \Pi_{A, C}(r)
$$
The join condition compares $R_1.A = R_2.A$.
Here, $\text{null} = \text{null}$ evaluates to `UNKNOWN`.
The join condition fails. The tuple is discarded!
The natural join yields an empty relation for this tuple:
$$
\Pi_{A, B}(r) \bowtie \Pi_{A, C}(r) = \emptyset \neq r
$$
The original tuple $t_1$ is lost. The decomposition is no longer lossless.

**Problem 2: Generation of Spurious Tuples under Outer Joins or Null-Equality**
Suppose the DBMS uses a null-matching join (such as `IS NOT DISTINCT FROM`) to avoid dropping nulls.
Now suppose $r$ contains two distinct tuples with null keys:
$$
t_1 = (\text{null}, b_1, c_1)
$$
$$
t_2 = (\text{null}, b_2, c_2)
$$
Projections:
- $R_1$: $\{(\text{null}, b_1), (\text{null}, b_2)\}$
- $R_2$: $\{(\text{null}, c_1), (\text{null}, c_2)\}$

If nulls are allowed to join with nulls, each row in $R_1$ joins with both rows in $R_2$. The join produces four tuples:
1. $(\text{null}, b_1, c_1)$ (original $t_1$)
2. $(\text{null}, b_1, c_2)$ (**spurious tuple!**)
3. $(\text{null}, b_2, c_1)$ (**spurious tuple!**)
4. $(\text{null}, b_2, c_2)$ (original $t_2$)

We cannot determine whether $b_1$ was originally associated with $c_1$ or $c_2$. The decomposition produces false associations (spurious tuples).

**Problem 3: Functional Dependency Definition Collapses**
The definition of an FD $\alpha \rightarrow \beta$ states:
$$
t_1[\alpha] = t_2[\alpha] \implies t_1[\beta] = t_2[\beta]
$$
If $\alpha$ contains nulls, SQL allows multiple rows with nulls in $\alpha$ to hold different values in $\beta$ (e.g., in a `UNIQUE` constraint that permits multiple nulls). Thus, $\alpha$ no longer functions as a key.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Concept Summary
> Always provide both failure modes in your answer:
> 1. **Under standard SQL inner join:** tuples with nulls on the join attributes are discarded completely (tuple loss).
> 2. **Under null-matching semantics:** multiple null tuples cross-match, producing false combinations (spurious tuples).
> This explains why primary key attributes must strictly enforce `NOT NULL`.

---

### Exercise 7.12 · Proof of Universal Tuple Containment in Natural Join

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.12 (p. 356)
> - **Subtopic:** T08.11 (Formal relational decomposition theory)
> - **Focus:** Proving that the join of projections always contains the original relation ($u \subseteq \bowtie r_i$)

**Question (Silberschatz 7e Exercise 7.12).**
Let $R_1, R_2, \ldots, R_n$ be a decomposition of schema $U$. Let $u(U)$ be a relation, and let $r_i = \Pi_{R_i}(u)$. Show that
$$
u \subseteq r_1 \bowtie r_2 \bowtie \cdots \bowtie r_n
$$

#### 1. Core Principles & Concept Overview

This theorem establishes a fundamental principle of relational database design: **projecting a relation onto sub-schemas and joining the results back together never loses original tuples.** At worst, the join may generate extra (spurious) tuples. Therefore, decomposition is either lossless ($u = \bowtie r_i$) or lossy-with-spurious-tuples ($u \subset \bowtie r_i$). A decomposition can never result in $u \not\subseteq \bowtie r_i$ (assuming no null values).

#### 2. Detailed Step-by-Step Solution

Let $U$ be a relation schema and let $R_1, R_2, \dots, R_n$ be a decomposition of $U$ such that:
$$
U = R_1 \cup R_2 \cup \cdots \cup R_n
$$
Let $u$ be any relation instance on schema $U$.
For each $i \in \{1, 2, \dots, n\}$, let:
$$
r_i = \Pi_{R_i}(u)
$$

We must prove that for every tuple $t \in u$, $t \in r_1 \bowtie r_2 \bowtie \cdots \bowtie r_n$.

1. **Pick an arbitrary tuple:**
   Let $t$ be an arbitrary tuple in $u$ ($t \in u$).

2. **Examine its projection onto each decomposed schema:**
   By definition of relational projection:
   $$
   t[R_i] \in \Pi_{R_i}(u) = r_i \quad \text{for each } i \in \{1, 2, \dots, n\}
   $$
   Let $t_i = t[R_i]$. Then $t_i \in r_i$ for all $i \in \{1, \dots, n\}$.

3. **Check compatibility for the natural join:**
   The definition of the natural join $r_1 \bowtie r_2 \bowtie \cdots \bowtie r_n$ is:
   A tuple $t'$ on schema $U$ belongs to $r_1 \bowtie \cdots \bowtie r_n$ if and only if there exist tuples $s_1 \in r_1, s_2 \in r_2, \dots, s_n \in r_n$ such that:
   $$
   t'[R_i] = s_i \quad \text{for all } i \in \{1, 2, \dots, n\}
   $$
   Consider our original tuple $t$. For each $i$:
   $$
   t[R_i] = t_i \in r_i
   $$
   Because all $t_i$ values were projected from the exact same tuple $t$, they are guaranteed to agree on all overlapping attributes:
   $$
   t_i[R_i \cap R_j] = t_j[R_i \cap R_j] = t[R_i \cap R_j] \quad \text{for all } i, j
   $$

4. **Conclusion:**
   The tuple $t$ satisfies every equality condition required by the natural join.
   Therefore, $t$ belongs to the join:
   $$
   t \in r_1 \bowtie r_2 \bowtie \cdots \bowtie r_n
   $$
   Since this holds for every tuple $t \in u$, it follows that:
   $$
   u \subseteq r_1 \bowtie r_2 \bowtie \cdots \bowtie r_n
   $$
   This completes the proof.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Theory Exam Strategy
> This is a clean 3 to 4-mark formal proof. Examiners look for:
> 1. Defining $t_i = t[R_i] \in r_i$.
> 2. Explaining that mutual consistency across intersections ($t_i[R_i \cap R_j] = t_j[R_i \cap R_j]$) is guaranteed because all projections originate from the same tuple $t$.
> 3. Concluding $u \subseteq \bowtie r_i$.

---

### Exercise 7.13 · Non-Preservation of Dependencies in Binary Decomposition

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.13 (p. 356)
> - **Subtopic:** T08.11 (Dependency preservation tests)
> - **Focus:** Proving that the lossless decomposition from Exercise 7.1 fails dependency preservation

**Question (Silberschatz 7e Exercise 7.13).**
Show that the decomposition in Exercise 7.1 is not a dependency-preserving decomposition.

*(From Exercise 7.1: $R = (A, B, C, D, E)$ decomposed into $R_1 = (A, B, C)$ and $R_2 = (A, D, E)$ under $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.)*

#### 1. Core Principles & Concept Overview

Let a decomposition of $R$ be $\rho = \{R_1, R_2, \dots, R_n\}$.
For each schema $R_i$, the restriction of $F$ to $R_i$ is:
$$
F_i = \{ \alpha \rightarrow \beta \in F^+ \mid \alpha \cup \beta \subseteq R_i \}
$$
The decomposition is **dependency-preserving** if:
$$
(F_1 \cup F_2 \cup \cdots \cup F_n)^+ = F^+
$$
If even one functional dependency $\alpha \rightarrow \beta \in F$ cannot be derived from the union of the local dependencies $\bigcup F_i$, enforcing the dependency requires an expensive join. In that case, the decomposition is not dependency-preserving.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E)$, decomposed into:
$$
R_1 = (A, B, C), \quad R_2 = (A, D, E)
$$
with functional dependency set:
$$
F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Step 1: Check each original dependency against the decomposed schemas**
1. $A \rightarrow BC$:
   Attributes $\{A, B, C\} \subseteq R_1$. This dependency can be enforced locally inside $R_1$. It is preserved.
2. $E \rightarrow A$:
   Attributes $\{A, E\} \subseteq R_2$. This dependency can be enforced locally inside $R_2$. It is preserved.
3. $B \rightarrow D$:
   Attribute $B \in R_1$, while attribute $D \in R_2$.
   Neither $R_1$ nor $R_2$ contains both $B$ and $D$.
4. $CD \rightarrow E$:
   Attribute $C \in R_1$, attribute $D \in R_2$, attribute $E \in R_2$.
   Neither $R_1$ nor $R_2$ contains $\{C, D\}$.

**Step 2: Test if $B \rightarrow D$ can be derived from $F_1 \cup F_2$**
Let $F' = F_1 \cup F_2$.
We compute the closure of $B$ under $F'$:

- What nontrivial dependencies hold in $F_1$ (attributes restricted to $\{A, B, C\}$)?
  - $A_F^+ = \{A, B, C, D, E\} \implies A \rightarrow BC \in F_1$.
  - $B_F^+ = \{B, D\}$. Restricted to $\{A, B, C\}$, we get $\{B\}$. No nontrivial dependency with LHS $\{B\}$ exists in $F_1$.
  - $C_F^+ = \{C\}$. No dependency.
  - $BC_F^+ = \{B, C, D\}$. Restricted to $\{A, B, C\}$, we get $\{B, C\}$. No new dependency.

- What nontrivial dependencies hold in $F_2$ (attributes restricted to $\{A, D, E\}$)?
  - $A_F^+ \cap \{A, D, E\} = \{A, D, E\} \implies A \rightarrow DE \in F_2$.
  - $E_F^+ \cap \{A, D, E\} = \{A, D, E\} \implies E \rightarrow AD \in F_2$.
  - $D_F^+ \cap \{A, D, E\} = \{D\}$. No dependency.

- Now compute $B^+$ under $F' = F_1 \cup F_2$:
  - $B^{(0)} = \{B\}$
  - In $F_1$, the only available rule requires $A$ as input ($A \rightarrow BC$). But we only have $\{B\}$.
  - In $F_2$, the rules require $A$ or $E$ ($A \rightarrow DE, E \rightarrow AD$). Neither is available.
  - No dependency can be applied.
  - Therefore:
  $$
  B_{F_1 \cup F_2}^+ = \{B\}
  $$

Does $B_{F_1 \cup F_2}^+$ contain $D$?
No, $D \notin \{B\}$.
Therefore:
$$
B \rightarrow D \notin (F_1 \cup F_2)^+
$$

**Step 3: Test if $CD \rightarrow E$ can be derived from $F_1 \cup F_2$**
Similarly, compute $\{C, D\}^+$ under $F_1 \cup F_2$:
- $\{C, D\}^{(0)} = \{C, D\}$
- Neither $C$ nor $D$ triggers any rule in $F_1$ or $F_2$.
- $\{C, D\}_{F_1 \cup F_2}^+ = \{C, D\}$, which does not contain $E$.
- Therefore:
$$
CD \rightarrow E \notin (F_1 \cup F_2)^+
$$

**Conclusion:**
Because the dependencies $B \rightarrow D$ and $CD \rightarrow E$ cannot be derived from the dependencies of the decomposed relations, the decomposition is **not dependency-preserving**.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Note on Trade-offs
> Compare Exercise 7.1 with Exercise 7.13:
> - Decomposition $(A, B, C)$ and $(A, D, E)$ **is lossless**, but **is not dependency-preserving**.
> To make it both lossless and dependency-preserving, we need the 3NF synthesis algorithm (Exercise 7.22), which produces four relations.

---

### Exercise 7.29 · Lossy Decomposition Counterexample with Spurious Tuples

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.29 (p. 357)
> - **Subtopic:** T08.11 (Counterexample construction for lossy joins)
> - **Focus:** Constructing a concrete relation instance where $\Pi_{R_1}(r) \bowtie \Pi_{R_2}(r) \neq r$

**Question (Silberschatz 7e Exercise 7.29).**
Show that the following decomposition of the schema $R$ of Exercise 7.1 is not a lossless decomposition:
$$
(A, B, C)
$$
$$
(C, D, E)
$$
*Hint:* Give an example of a relation $r(R)$ such that $\Pi_{A, B, C}(r) \bowtie \Pi_{C, D, E}(r) \neq r$.

*(From Exercise 7.1: $R = (A, B, C, D, E)$ with $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.)*

#### 1. Core Principles & Concept Overview

A binary decomposition of $R$ into $R_1, R_2$ is lossless if and only if $R_1 \cap R_2 \rightarrow R_1$ or $R_1 \cap R_2 \rightarrow R_2$.
If the shared attribute set fails to determine either relation, the decomposition is **lossy**. When projections of such a relation are joined, rows share identical values on the common attributes without being uniquely bound to the other attributes. This produces extra rows called **spurious tuples**.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E)$, decomposed into:
$$
R_1 = (A, B, C), \quad R_2 = (C, D, E)
$$
with functional dependencies:
$$
F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}
$$

**Part 1: Theoretical Verification**
1. Find common attributes:
   $$
   R_1 \cap R_2 = (A, B, C) \cap (C, D, E) = \{C\}
   $$
2. Compute $C^+$ under $F$:
   - $C^{(0)} = \{C\}$
   - No dependency in $F$ has LHS $\{C\}$.
   - Therefore:
   $$
   C^+ = \{C\}
   $$
3. Test superkey conditions:
   - Does $C \rightarrow (A, B, C)$ hold? No, $\{A, B, C\} \not\subseteq \{C\}$.
   - Does $C \rightarrow (C, D, E)$ hold? No, $\{C, D, E\} \not\subseteq \{C\}$.

Since $C$ is not a superkey for either $R_1$ or $R_2$, the decomposition is lossy.

---

**Part 2: Concrete Relation Counterexample**
We construct a relation instance $r(R)$ containing two tuples that satisfy all dependencies in $F$:

Let $r$ consist of two tuples $t_1$ and $t_2$:

| $A$ | $B$ | $C$ | $D$ | $E$ |
| :-: | :-: | :-: | :-: | :-: |
| $a_1$ | $b_1$ | $c$ | $d_1$ | $e_1$ |
| $a_2$ | $b_2$ | $c$ | $d_2$ | $e_2$ |

**Check that $r$ satisfies all dependencies in $F$:**
1. $A \rightarrow BC$: The $A$ values are $a_1, a_2$ (distinct). Satisfied.
2. $E \rightarrow A$: The $E$ values are $e_1, e_2$ (distinct). Satisfied.
3. $B \rightarrow D$: The $B$ values are $b_1, b_2$ (distinct). Satisfied.
4. $CD \rightarrow E$: The $CD$ values are $(c, d_1)$ and $(c, d_2)$ (distinct). Satisfied.

All dependencies in $F$ hold on $r$.

**Compute Projections:**

Projection onto $R_1(A, B, C)$:
$$
r_1 = \Pi_{A, B, C}(r):
$$

| $A$ | $B$ | $C$ |
| :-: | :-: | :-: |
| $a_1$ | $b_1$ | $c$ |
| $a_2$ | $b_2$ | $c$ |

Projection onto $R_2(C, D, E)$:
$$
r_2 = \Pi_{C, D, E}(r):
$$

| $C$ | $D$ | $E$ |
| :-: | :-: | :-: |
| $c$ | $d_1$ | $e_1$ |
| $c$ | $d_2$ | $e_2$ |

**Compute the Natural Join $r_1 \bowtie r_2$:**
The join matches rows where $r_1.C = r_2.C$.
Since every row in both tables has $C = c$, each of the two rows in $r_1$ joins with both rows in $r_2$:

| $A$ | $B$ | $C$ | $D$ | $E$ | Status |
| :-: | :-: | :-: | :-: | :-: | :-- |
| $a_1$ | $b_1$ | $c$ | $d_1$ | $e_1$ | Original tuple $t_1$ |
| $a_1$ | $b_1$ | $c$ | $d_2$ | $e_2$ | **Spurious tuple!** |
| $a_2$ | $b_2$ | $c$ | $d_1$ | $e_1$ | **Spurious tuple!** |
| $a_2$ | $b_2$ | $c$ | $d_2$ | $e_2$ | Original tuple $t_2$ |

The join contains $4$ tuples, while the original relation $r$ had only $2$ tuples!
Notice that the spurious tuple $(a_1, b_1, c, d_2, e_2)$ pairs $B = b_1$ with $D = d_2$, violating the dependency $B \rightarrow D$.
Therefore:
$$
\Pi_{A, B, C}(r) \bowtie \Pi_{C, D, E}(r) \neq r
$$
The decomposition is lossy.

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] How to Construct Counterexample Tables Rapidly
> When asked to construct a counterexample table for a lossy join:
> 1. Give the common attribute $C$ the **same value** ($c$) in both rows.
> 2. Give all other attributes distinct values ($a_1, a_2, b_1, b_2, \dots$) so that all candidate keys remain valid.
> 3. Show the resulting $2 \times 2 = 4$ joined rows, clearly labelling the 2 spurious tuples.

---

### Exercise 7.32 · Multi-part BCNF Analysis: Implied FDs, Lossless and Dependency Tests

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.32 (pp. 358-359)
> - **Subtopic:** T08.5, T08.9, T08.11 (Comprehensive normal form analysis)
> - **Focus:** Logical implication, BCNF decomposition, lossless test, and dependency preservation test

**Question (Silberschatz 7e Exercise 7.32).**
Consider the schema $R = (A, B, C, D, E, G)$ and the set $F$ of functional dependencies:
$$
A \rightarrow BC
$$
$$
BD \rightarrow E
$$
$$
CD \rightarrow AB
$$
a. Find a nontrivial functional dependency containing no extraneous attributes that is logically implied by the above three dependencies and explain how you found it.
b. Use the BCNF decomposition algorithm to find a BCNF decomposition of $R$. Start with $A \rightarrow BC$. Explain your steps.
c. For your decomposition, state whether it is lossless and explain why.
d. For your decomposition, state whether it is dependency preserving and explain why.

#### 1. Core Principles & Concept Overview

- A functional dependency $\alpha \rightarrow \beta$ is **nontrivial** if $\beta \not\subseteq \alpha$. It contains no extraneous attributes if no attribute can be dropped from $\alpha$ or $\beta$ while preserving logical implication.
- The **BCNF decomposition algorithm** finds a dependency $\alpha \rightarrow \beta$ that violates BCNF ($\alpha$ is not a superkey), and splits $R$ into $R_1 = \alpha \cup \beta$ and $R_2 = R - (\beta - \alpha)$. It then repeats this recursively on the sub-relations.
- BCNF decomposition is always guaranteed to be **lossless**. But it is **not always dependency-preserving**.

#### 2. Detailed Step-by-Step Solution

Given $R = (A, B, C, D, E, G)$ and:
$$
F = \{A \rightarrow BC, BD \rightarrow E, CD \rightarrow AB\}
$$

---

#### Part (a): Find an Implied Nontrivial FD with No Extraneous Attributes

We want to derive a new dependency from $F$:
1. Take $CD \rightarrow AB$. By Armstrong's decomposition rule:
   $$
   CD \rightarrow B
   $$
2. Augment both sides with $D$:
   $$
   CD \rightarrow BD
   $$
3. We are given $BD \rightarrow E$. By transitivity:
   $$
   CD \rightarrow E
   $$

**Verify properties of $CD \rightarrow E$:**
- **Nontrivial:** $E \notin \{C, D\}$. (Nontrivial).
- **Test LHS attribute $C$:**
  Does $D \rightarrow E$ hold? Compute $D^+$ under $F$: $D^+ = \{D\}$.
  Since $E \notin D^+$, attribute $C$ is **not extraneous**.
- **Test LHS attribute $D$:**
  Does $C \rightarrow E$ hold? Compute $C^+$ under $F$: $C^+ = \{C\}$.
  Since $E \notin C^+$, attribute $D$ is **not extraneous**.
- **Test RHS attribute $E$:**
  $E$ is a single attribute. Dropping it leaves $CD \rightarrow \emptyset$, which is trivial.

**Result for (a):**
A nontrivial functional dependency with no extraneous attributes is:
$$
\boxed{CD \rightarrow E}
$$

*(Another valid answer is $AD \rightarrow E$, derived from $A \rightarrow B \implies AD \rightarrow BD \rightarrow E$.)*

---

#### Part (b): BCNF Decomposition Starting with $A \rightarrow BC$

First identify the candidate keys of $R(A, B, C, D, E, G)$:
Attribute $G$ never appears on the right-hand side of any dependency. So $G$ must be in every candidate key.
Compute closures:
- $ADG^+ = \{A, B, C, D, E, G\} = R$
- $CDG^+ = \{A, B, C, D, E, G\} = R$
The candidate keys of $R$ are $ADG$ and $CDG$.

**Step 1: Check $A \rightarrow BC$ on $R$**
Compute $A^+$:
$$
A^+ = \{A, B, C\} \neq R
$$
Since $A$ is not a superkey of $R$, the dependency $A \rightarrow BC$ violates BCNF.
Decompose $R$ into:
$$
R_1 = A \cup BC = (A, B, C)
$$
$$
R_2 = R - (BC - A) = (A, D, E, G)
$$

**Step 2: Check sub-relation $R_1(A, B, C)$**
The functional dependencies holding on $R_1$ are generated by $A \rightarrow BC$.
$A^+ \cap R_1 = \{A, B, C\} = R_1$.
$A$ is a superkey of $R_1$.
No other nontrivial dependencies exist in $R_1$.
Therefore, **$R_1(A, B, C)$ is in BCNF**.

**Step 3: Check sub-relation $R_2(A, D, E, G)$**
What dependencies hold on $R_2$?
Compute closures of attribute subsets of $R_2$ under $F$:
- $AD^+ = \{A, B, C, D, E\}$. Restricted to $R_2$, this gives $\{A, D, E\}$.
  Therefore, the dependency $AD \rightarrow E$ holds on $R_2$.
- Is $AD$ a superkey of $R_2$?
  $AD^+ \cap R_2 = \{A, D, E\} \neq \{A, D, E, G\}$ (attribute $G$ is missing).
  So $AD$ is not a superkey of $R_2$.

Thus, $AD \rightarrow E$ violates BCNF in $R_2$.
Decompose $R_2$ using $AD \rightarrow E$:
$$
R_{21} = AD \cup E = (A, D, E)
$$
$$
R_{22} = R_2 - (E - AD) = (A, D, G)
$$

**Step 4: Check sub-relation $R_{21}(A, D, E)$**
$AD \rightarrow E$ holds on $R_{21}$.
$AD$ is a superkey of $R_{21}$.
No other nontrivial dependencies exist.
Therefore, **$R_{21}(A, D, E)$ is in BCNF**.

**Step 5: Check sub-relation $R_{22}(A, D, G)$**
No nontrivial dependencies hold on $R_{22}$ (only trivial dependencies like $ADG \rightarrow ADG$).
The candidate key is $(A, D, G)$.
Therefore, **$R_{22}(A, D, G)$ is in BCNF**.

**Result for (b):**
The final BCNF decomposition is:
$$
\boxed{\rho = \{R_1(A, B, C), R_{21}(A, D, E), R_{22}(A, D, G)\}}
$$

---

#### Part (c): Is the Decomposition Lossless?

**Yes, the decomposition is guaranteed to be lossless.**
- At Step 1, $R$ is split into $R_1(A, B, C)$ and $R_2(A, D, E, G)$.
  The shared attribute set is $R_1 \cap R_2 = \{A\}$.
  Since $A \rightarrow BC$ holds, $A \rightarrow R_1$ holds.
  Thus, $R_1 \cap R_2$ is a superkey of $R_1$. The first split is lossless.
- At Step 2, $R_2$ is split into $R_{21}(A, D, E)$ and $R_{22}(A, D, G)$.
  The shared attribute set is $R_{21} \cap R_{22} = \{A, D\}$.
  Since $AD \rightarrow E$ holds, $AD \rightarrow R_{21}$ holds.
  Thus, $R_{21} \cap R_{22}$ is a superkey of $R_{21}$. This second split is also lossless.

By the inductive property of the BCNF algorithm, the overall decomposition is lossless.

---

#### Part (d): Is the Decomposition Dependency Preserving?

**No, the decomposition is NOT dependency-preserving.**
Test each original dependency in $F$:
1. $A \rightarrow BC$: Preserved in $R_1(A, B, C)$.
2. $BD \rightarrow E$: The attributes are $\{B, D, E\}$.
   - $B \in R_1$
   - $D \in R_{21}, R_{22}$
   - $E \in R_{21}$
   None of the decomposed relations contains all three attributes $\{B, D, E\}$.
   Can $BD \rightarrow E$ be derived from the union of local dependencies?
   Compute $BD^+$ under the local dependencies:
   - In $R_1(A, B, C)$, $B^+ = \{B\}$.
   - In $R_{21}(A, D, E)$, $D^+ = \{D\}$.
   - In $R_{22}(A, D, G)$, $D^+ = \{D\}$.
   Therefore, $BD_{local}^+ = \{B, D\}$.
   This closure cannot derive $A$, and cannot derive $E$.
   Thus, $BD \rightarrow E$ is **lost**.
3. $CD \rightarrow AB$: Attributes $\{A, B, C, D\}$ are not contained in any single schema. $CD_{local}^+ = \{C, D\}$, which cannot derive $A$ or $B$.
   Thus, $CD \rightarrow AB$ is also **lost**.

Because dependencies are lost, the decomposition does not preserve dependencies.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Textbook Pattern Note
> This exercise illustrates why BCNF is not always chosen over 3NF:
> - **BCNF:** Removes all redundancy from functional dependencies, but can lose dependencies (as proven in Part d).
> - **3NF:** Retains all dependencies, but may allow minor redundancy if an attribute is prime.

---

## T08.10 / T08.11 · Database Design Goals, Trade-offs & When to Choose Non-BCNF / 4NF

### Exercise 7.20 · Schema in BCNF but not in 4NF

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.20 (p. 357)
> - **Subtopic:** T08.10, Higher Normal Forms (BCNF vs 4NF)
> - **Focus:** Multivalued dependencies and independent many-to-many relationships

**Question (Silberschatz 7e Exercise 7.20).**
Give an example of a relation schema $R$ and a set of dependencies such that $R$ is in BCNF but is not in 4NF.

#### 1. Core Principles & Concept Overview

- **Boyce-Codd Normal Form (BCNF):** Considers only functional dependencies. A relation schema $R$ is in BCNF if for every nontrivial functional dependency $\alpha \rightarrow \beta$, $\alpha$ is a superkey of $R$.
- **Fourth Normal Form (4NF):** Considers multivalued dependencies (MVDs). A relation schema $R$ is in 4NF if for every nontrivial multivalued dependency $\alpha \twoheadrightarrow \beta$, $\alpha$ is a superkey of $R$.
- **The Gap:** If a table contains no nontrivial functional dependencies at all, its only candidate key is the entire set of attributes. Such a table is **automatically in BCNF**! However, if the table models two independent multi-valued facts about an entity, a nontrivial multivalued dependency exists. This violates 4NF and creates tuple duplication.

#### 2. Detailed Step-by-Step Solution

**Step 1: Define the schema**
Consider a university relation schema representing course information:
$$
R(\text{course}, \text{teacher}, \text{book})
$$
The real-world business rules:
1. A course can be taught by multiple teachers.
2. A course recommends a set of textbooks.
3. The textbooks used for a course are independent of which teacher teaches the course.

**Step 2: Functional Dependencies & BCNF Check**
- Does $\text{course} \rightarrow \text{teacher}$ hold? No, a course has multiple teachers.
- Does $\text{course} \rightarrow \text{book}$ hold? No, a course has multiple books.
- Does $\text{teacher} \rightarrow \text{course}$ or $\text{book} \rightarrow \text{course}$ hold? No.

There are **no nontrivial functional dependencies** on $R$.
Because there are no nontrivial FDs, the only candidate key is the composite key of all three attributes:
$$
\text{Candidate Key} = \{\text{course}, \text{teacher}, \text{book}\}
$$
Every functional dependency that holds on $R$ is trivial (e.g., $\text{course, teacher, book} \rightarrow \text{course}$).
Therefore, **$R$ is in BCNF**.

**Step 3: Multivalued Dependencies & 4NF Check**
Because teachers and books are independently associated with a course, the following multivalued dependencies hold:
$$
\text{course} \twoheadrightarrow \text{teacher}
$$
$$
\text{course} \twoheadrightarrow \text{book}
$$

Let us test if $\text{course} \twoheadrightarrow \text{teacher}$ satisfies 4NF:
1. Is it trivial?
   An MVD $\alpha \twoheadrightarrow \beta$ on $R$ is trivial if $\beta \subseteq \alpha$ or $\alpha \cup \beta = R$.
   Here, $\text{teacher} \not\subseteq \{\text{course}\}$, and $\{\text{course}, \text{teacher}\} \neq R$.
   So the dependency is **nontrivial**.
2. Is $\text{course}$ a superkey of $R$?
   No. The only candidate key is $\{\text{course}, \text{teacher}, \text{book}\}$.
   The attribute $\text{course}$ by itself is not a superkey.

Because a nontrivial MVD exists whose left-hand side is not a superkey, **$R$ is NOT in 4NF**.

**Step 4: Illustration of 4NF Redundancy**
If course `CS-101` has two teachers (`Dr. Smith`, `Dr. Jones`) and two books (`Silberschatz`, `Codd`), the table must store $2 \times 2 = 4$ rows:

| `course` | `teacher` | `book` |
| :-- | :-- | :-- |
| `CS-101` | `Dr. Smith` | `Silberschatz` |
| `CS-101` | `Dr. Smith` | `Codd` |
| `CS-101` | `Dr. Jones` | `Silberschatz` |
| `CS-101` | `Dr. Jones` | `Codd` |

Adding a third book requires inserting two new rows (one for each teacher).
This is a classic update anomaly.

**Decomposition into 4NF:**
Decompose $R$ into two schemas:
$$
R_1(\text{course}, \text{teacher})
$$
$$
R_2(\text{course}, \text{book})
$$
Both sub-relations are now in 4NF.

#### 3. RUET Exam Insights & Examiner Notes

> [!important] Exam Clarification
> When asked: *"Does BCNF eliminate all data redundancy?"*
> Answer: **No.** BCNF eliminates all redundancy caused by functional dependencies. It does not eliminate redundancy caused by multivalued dependencies (MVDs). Use this exact Course-Teacher-Book example to prove it.

---

### Exercise 7.38 · Why Choose a Non-BCNF Database Design

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 7, Exercise 7.38 (p. 360)
> - **Subtopic:** T08.10, T08.11 (Database design theory & trade-offs)
> - **Focus:** Practical engineering reasons to adopt 3NF or denormalized designs

**Question (Silberschatz 7e Exercise 7.38).**
In designing a relational database, why might we choose a non-BCNF design?

#### 1. Core Principles & Concept Overview

Relational database design balances three primary goals:
1. Minimizing data redundancy and avoiding anomalies (insertion, update, deletion).
2. Preserving functional dependencies.
3. Maximizing query performance and minimizing join overhead.

While BCNF completely eliminates functional dependency redundancy, achieving it can conflict with dependency preservation and query execution speed. In practice, designers often choose a non-BCNF design (such as 3NF or deliberate denormalization) for two main reasons.

#### 2. Detailed Step-by-Step Solution

**Reason 1: Preserving Functional Dependencies (The 3NF vs. BCNF Dilemma)**
It is not always mathematically possible to achieve BCNF while also preserving all functional dependencies.

**Classic Example:**
Consider schema $R(\text{street}, \text{city}, \text{zipcode})$ with dependencies:
$$
\text{zipcode} \rightarrow \text{city}
$$
$$
\text{street, city} \rightarrow \text{zipcode}
$$
Candidate keys are:
$$
\{\text{street}, \text{city}\}, \quad \{\text{street}, \text{zipcode}\}
$$
In $\text{zipcode} \rightarrow \text{city}$, attribute $\text{zipcode}$ is not a superkey.
This violates BCNF. (It is in 3NF because $\text{city}$ is a prime attribute).

To decompose this schema into BCNF, we must split it into:
$$
R_1(\text{zipcode}, \text{city}) \quad \text{and} \quad R_2(\text{street}, \text{zipcode})
$$
In this decomposition, the dependency $\text{street, city} \rightarrow \text{zipcode}$ is **lost**!
To enforce this constraint in BCNF, the database would have to perform an expensive natural join across $R_1$ and $R_2$ on every `INSERT` and `UPDATE`.
By keeping the schema in 3NF (a non-BCNF design), the database can enforce the dependency locally within a single table using simple uniqueness constraints.

**Reason 2: Query Performance & Join Overhead (Controlled Denormalization)**
High-performance relational databases handle millions of read queries per second.
- Normalizing a database to BCNF splits data across many small tables.
- Reconstructing user records requires multi-table SQL joins (`JOIN`).
- Joins increase disk I/O, consume CPU cycles, and lock index structures.

When an application is read-heavy (such as OLAP systems, data warehouses, or public web portals), database engineers intentionally choose a non-BCNF or denormalized design. Keeping related attributes in a single table eliminates join overhead, speeding up retrieval queries.

**Reason 3: Simplicity in Star Schemas and Reporting Marts**
In data warehouse design (such as Kimball Dimensional Modeling), dimension tables often use denormalized hierarchies (e.g., `City -> State -> Country` stored together in a single `Customer_Dimension` table). This simplifies reporting queries for business analysts and business intelligence tools.

**Summary Comparison:**

| Design Choice | Functional Dependency Redundancy | Dependency Preservation | Query Retrieval Speed (Reads) | Update Overhead |
| :-- | :-- | :-- | :-- | :-- |
| **BCNF** | Zero | Not always guaranteed | Slower (requires multi-table joins) | Low (no duplicate updates) |
| **3NF** | Minimal (only prime attributes) | Always guaranteed | Moderate (fewer joins than BCNF) | Low to Moderate |
| **Denormalized** | High | Preserved | Fastest (zero joins needed) | High (application must manage anomalies) |

#### 3. RUET Exam Insights & Examiner Notes

> [!tip] Scoring Summary for RUET Finals
> This question tests real-world database design trade-offs. In RUET exams (e.g., 2017 Q.3(a), CT-03 Q.04), state the two core technical reasons clearly:
> 1. **Dependency Preservation:** Some schemas cannot be placed into BCNF without losing dependencies (e.g., $\text{street, city, zipcode}$). 3NF is chosen to preserve constraints.
> 2. **Performance Optimization:** BCNF requires multiple table joins during reads. Denormalization reduces join overhead for read-heavy workloads.


---

[← Prev: T08 Part 1](T08_Part1_FDs_and_Armstrong_Axioms.md) | [Index](00_Index.md) | [Next: T08 Part 3 →](T08_Part3_BCNF_and_Advanced_Normalization.md)
