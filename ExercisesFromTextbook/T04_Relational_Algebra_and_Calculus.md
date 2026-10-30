---
title: "T04 · Relational Algebra and Calculus · Textbook Exercise Solutions"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T04
topic_id: T04
exercise_count: 8
source_chapters:
  - "Chapter 02"
---

[← Prev: T03](T03_Relational_Model_Keys_and_Integrity.md) | [Index](00_Index.md) | [Next: T05 Part 1 →](T05_Part1_SQL_DDL_DML_Basics.md)

---

# T04 · Relational Algebra and Calculus · Textbook Solutions

> [!info] Topic Card
> **Topic:** T04 · Relational Algebra and Calculus  
> **Course:** ECE 2215: Database Systems · Dept. of ECE, RUET  
> **Exam Weight:** 48 final marks (7.5% across 6/7 semester finals) + 8 class test marks  
> **Textbook Reference:** Silberschatz, Korth & Sudarshan, *Database System Concepts* (7th Ed., 2019), Chapter 2 (§2.6)  
> **Past Exam Direct Hits:** 
> - ⚠️ **Direct Recycled Hit**: Practice Exercise 2.6 recycled directly into **2017 Q.2(a)** [8 Marks] (`employee`, `works`, `company`, `manages` database).
> - Universal set-difference patterns (PE 2.8, EX 2.18e) recycled into **2018 Q.3(a)**, **2020 Q.2(a)**, **2024 Q.2(b)**.
> - Domain Relational Calculus (DRC) formalization asked in **2020 Q.4(b)** [3 Marks].

---

## Table of Assigned Exercises

| Exercise ID | Exercise Type | Primary Operator / Core Concept | Subtopic | RUET Exam Relevance | Jump Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PE 2.5** | Conceptual / Derivation | Cartesian Product ($\times$), Selection ($\sigma$), Theta Join ($\bowtie_\theta$) | **T04.1** | Join semantics & Cartesian explosion | [[#Exercise 2.5 · Cartesian Product and Selection Equivalence to Theta Join\|Jump]] |
| **PE 2.6** | Query Formulation | Selection ($\sigma$), Projection ($\Pi$), Conjunction vs. Intersection ($\cap$) | **T04.2** | ⚠️ **Direct Hit: 2017 Q.2(a)** (Employee DB) | [[#Exercise 2.6 · Basic Selection and Projection on Employee Database\|Jump]] |
| **PE 2.7** | Query Formulation | Filter, Project & Natural Join ($\bowtie$) on Bank Database | **T04.2** | High (Recurring Banking Schema) | [[#Exercise 2.7 · Banking Queries: Branch Selection and Borrower Join\|Jump]] |
| **PE 2.8** | Advanced Formulation | Set Difference ($-$) for Negation & Universal Comparison (Max) | **T04.2** | High-Yield (Emulating `NOT IN` and `MAX`) | [[#Exercise 2.8 · Negation via Set Difference and Emulating Maximum Salary\|Jump]] |
| **PE 2.9** | Algebraic Derivation | Relational Division ($\div$) & Universal Quantification ($\forall$) | **T04.1** | Core Syllabus (Unit 3 Division Operator) | [[#Exercise 2.9 · Relational Division Definition and Basic Operator Derivation\|Jump]] |
| **EX 2.14** | Multi-Table Queries | Multi-table joins, Projection, Same-City Entity Comparison | **T04.2** | ⚠️ **Direct Hit: 2017 Q.2(a)(i)** (Same-city query) | [[#Exercise 2.14 · Employee Database Joins and Same-City Matching\|Jump]] |
| **EX 2.15** | Multi-Table Queries | Multi-Condition Joins, Depositor & Account Filtering | **T04.2** | High-Yield Banking Schema | [[#Exercise 2.15 · Banking Queries: Loan Amounts and Depositor Balances\|Jump]] |
| **EX 2.18** | Schema Navigation | Department Navigation, Natural Join Attribute Clash, Negation | **T04.2** | Critical (University Schema Exam Standard) | [[#Exercise 2.18 · University Schema: Instructor Navigation and Negative Existential Queries\|Jump]] |

---

## Reference Schemas Used in this Note

### 1. Employee Database Schema (Silberschatz 7e, Figure 2.17)
$$
\begin{aligned}
&\text{employee}(\underline{\text{ID}}, \text{person\_name}, \text{street}, \text{city}) \\
&\text{works}(\underline{\text{ID}}, \text{company\_name}, \text{salary}) \\
&\text{company}(\underline{\text{company\_name}}, \text{city}) \\
&\text{manages}(\underline{\text{ID}}, \text{manager\_id})
\end{aligned}
$$

> [!NOTE] 6th Edition vs. 7th Edition Schema Variant
> In Silberschatz 6th Edition and in RUET **2017 Q.2(a)**, `person_name` served as the primary key across `employee`, `works`, and `manages` (e.g. `works(person_name, company_name, salary)` and `manages(person_name, manager_name)`). In Silberschatz 7th Edition, a surrogate primary key `ID` is used, and `manager_id` replaces `manager_name`. Both notations are mathematically equivalent and fully cross-referenced below.

### 2. Bank Database Schema (Silberschatz 7e, Figure 2.18)
$$
\begin{aligned}
&\text{branch}(\underline{\text{branch\_name}}, \text{branch\_city}, \text{assets}) \\
&\text{customer}(\underline{\text{ID}}, \text{customer\_name}, \text{customer\_street}, \text{customer\_city}) \\
&\text{loan}(\underline{\text{loan\_number}}, \text{branch\_name}, \text{amount}) \\
&\text{borrower}(\underline{\text{ID}, \text{loan\_number}}) \\
&\text{account}(\underline{\text{account\_number}}, \text{branch\_name}, \text{balance}) \\
&\text{depositor}(\underline{\text{ID}, \text{account\_number}})
\end{aligned}
$$

### 3. University Database Schema (Silberschatz 7e, Appendix A)
$$
\begin{aligned}
&\text{instructor}(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{salary}) \\
&\text{department}(\underline{\text{dept\_name}}, \text{building}, \text{budget}) \\
&\text{course}(\underline{\text{course\_id}}, \text{title}, \text{dept\_name}, \text{credits}) \\
&\text{section}(\underline{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{building}, \text{room\_number}, \text{time\_slot\_id}) \\
&\text{teaches}(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}) \\
&\text{student}(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{tot\_cred}) \\
&\text{takes}(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{grade}) \\
&\text{advisor}(\underline{\text{s\_id}}, \text{i\_id})
\end{aligned}
$$

---

## T04.1 · Basic Relational Algebra Operators & Relational Division

### Exercise 2.5 · Cartesian Product and Selection Equivalence to Theta Join

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Practice Exercise 2.5 (Page 60)
> - **Subtopic:** T04.1 · Basic operators
> - **Core Operators:** Cartesian Product ($\times$), Selection ($\sigma$), Theta Join ($\bowtie_\theta$), Natural Join ($\bowtie$)
> - **Mathematical Focus:** Operator composability, algebraic identities, join definitions

**Question (Silberschatz 7e Practice Exercise 2.5).**
What is the result of first performing the Cartesian product of *student* and *advisor*, and then performing a selection operation on the result with the predicate $s\_id = \text{ID}$? (Using the symbolic notation of relational algebra, this query can be written as $\sigma_{s\_id = ID}(student \times advisor)$.)

#### 1. Core Principles & Concept Overview
The relational algebra is a procedural query language consisting of fundamental operators closed under relations.
1. **Cartesian Product ($r \times s$):** Combines every tuple $t_r \in r$ with every tuple $t_s \in s$. If $r$ has arity $k_1$ with $|r|$ tuples and $s$ has arity $k_2$ with $|s|$ tuples, $r \times s$ produces a relation of arity $k_1 + k_2$ containing $|r| \times |s|$ tuples.
2. **Selection ($\sigma_\theta(R)$):** Filters tuples that satisfy the propositional predicate $\theta$.
3. **Theta Join Definition ($\bowtie_\theta$):** By algebraic definition, a theta join is a Cartesian product followed by a selection condition:
$$
R \bowtie_\theta S \equiv \sigma_\theta(R \times S)
$$

```text
┌───────────────────────┐         ┌───────────────────────┐
│     student (R)       │         │     advisor (S)       │
│ ID, name, dept, cred  │         │       s_id, i_id      │
└───────────┬───────────┘         └───────────┬───────────┘
            │                                 │
            └───────────────┬─────────────────┘
                            ▼
            ┌───────────────────────────────┐
            │        Cartesian Product      │  Schema: (student.ID, name, dept, cred, s_id, i_id)
            │      student × advisor        │  Tuples: |student| × |advisor|
            └───────────────┬───────────────┘
                            │
                            ▼
            ┌───────────────────────────────┐
            │      Selection Operation      │  Filters condition: student.ID = advisor.s_id
            │   σ_{s_id = ID}(...)          │  Retains only actual student-advisor pairings
            └───────────────┬───────────────┘
                            ▼
            ┌───────────────────────────────┐
            │          Theta Join           │  student ⋈_{student.ID = advisor.s_id} advisor
            └───────────────────────────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Analyze the schemas of the participating relations
- $\text{student}(\underline{\text{ID}}, \text{name}, \text{dept\_name}, \text{tot\_cred})$
- $\text{advisor}(\underline{\text{s\_id}}, \text{i\_id})$ where $\text{s\_id}$ is a foreign key referencing $\text{student}(\text{ID})$ and $\text{i\_id}$ references $\text{instructor}(\text{ID})$.

##### Step 2: Compute the intermediate Cartesian product
$$
T_1 \leftarrow student \times advisor
$$
- **Schema of $T_1$:** 
  $$
  \text{Schema}(T_1) = (\text{student.ID}, \text{name}, \text{dept\_name}, \text{tot\_cred}, \text{s\_id}, \text{i\_id})
  $$
- **Semantic effect:** Every student tuple is indiscriminately paired with every advisor tuple. If there are 1,000 students and 800 advisor assignments, $T_1$ produces $800,000$ tuples, the vast majority of which represent false pairings where $\text{student.ID} \neq \text{advisor.s\_id}$.

##### Step 3: Apply the selection predicate
$$
T_2 \leftarrow \sigma_{s\_id = ID}(T_1) = \sigma_{s\_id = ID}(student \times advisor)
$$
- **Semantic effect:** The predicate $s\_id = ID$ retains only those combined tuples where the student's identifier matches the student ID recorded in the advisor relation.
- **Resulting Relation:** The result contains the complete student record ($\text{ID}, \text{name}, \text{dept\_name}, \text{tot\_cred}$) concatenated with their designated advisor's identifier ($\text{s\_id}, \text{i\_id}$).
- Since $\text{s\_id}$ and $\text{ID}$ have identical values in every resulting tuple, $\text{s\_id}$ is a redundant duplicate column.

##### Step 4: Equivalence to Theta Join and Natural Join
By algebraic equivalence, this operation is precisely the **Theta Join** ($\bowtie_\theta$):
$$
\boxed{\sigma_{s\_id = ID}(student \times advisor) \equiv student \bowtie_{student.\text{ID} = advisor.s\_id} advisor}
$$

Furthermore, if we project out the redundant join attribute $\text{s\_id}$ (or if the attribute in `advisor` were also named `ID`), the expression is isomorphic to a **Natural Join** ($\bowtie$):
$$
\Pi_{\text{ID}, \text{name}, \text{dept\_name}, \text{tot\_cred}, \text{i\_id}}(\sigma_{s\_id = ID}(student \times advisor)) \equiv student \bowtie \rho_{advisor(\text{ID}, \text{i\_id})}(advisor)
$$

##### Step 5: Relational Calculus Formulations (T04.5)
- **Domain Relational Calculus (DRC):**
$$
\{\langle i, n, d, c, s, a \rangle \mid \langle i, n, d, c \rangle \in student \land \langle s, a \rangle \in advisor \land s = i\}
$$
- **Tuple Relational Calculus (TRC):**
$$
\{t \mid \exists p \in student \; \exists q \in advisor \; (p[\text{ID}] = q[s\_id] \land t[\text{ID}] = p[\text{ID}] \land t[\text{name}] = p[\text{name}] \land t[\text{dept\_name}] = p[\text{dept\_name}] \land t[\text{tot\_cred}] = p[\text{tot\_cred}] \land t[s\_id] = q[s\_id] \land t[i\_id] = q[i\_id])\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!TIP] Exam Insight: Cartesian Explosion vs. Join Optimization
> In RUET theory questions (e.g., *Compare Cartesian product with Natural join*, 2018 Q.3b, 2021 Q.2c), examiners look for two critical observations:
> 1. **Schema redundancy:** Cartesian product preserves all attributes ($k_1 + k_2$), leaving duplicate join columns. Natural join automatically projects out duplicate column names.
> 2. **Evaluation cost:** A DBMS query optimizer *never* materializes $R \times S$ followed by $\sigma$ because the time complexity is $O(|R| \cdot |S|)$ and buffer space is quickly overwhelmed. Instead, it pushes the selection down to transform the expression into an indexed nested-loop or hash join ($R \bowtie_\theta S$).

---

### Exercise 2.9 · Relational Division Definition and Basic Operator Derivation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Practice Exercise 2.9 (Page 61–62)
> - **Subtopic:** T04.1 · Basic operators & Relational Division
> - **Core Operators:** Division ($\div$), Projection ($\Pi$), Cartesian Product ($\times$), Set Difference ($-$)
> - **RUET Syllabus Unit:** Unit 3 (Explicitly listed: *Relational algebra: fundamental and additional operators, Relational Division*)
> - **Theoretical Significance:** Emulation of Universal Quantification ($\forall$) in first-order logic.

**Question (Silberschatz 7e Practice Exercise 2.9).**
The **division operator** of relational algebra, “$\div$”, is defined as follows. Let $r(R)$ and $s(S)$ be relations, and let $S \subseteq R$; that is, every attribute of schema $S$ is also in schema $R$. Given a tuple $t$, let $t[S]$ denote the projection of tuple $t$ on the attributes in $S$. Then $r \div s$ is a relation on schema $R - S$ (that is, on the schema containing all attributes of schema $R$ that are not in schema $S$). A tuple $t$ is in $r \div s$ if and only if both of two conditions hold:
- $t$ is in $\Pi_{R - S}(r)$
- For every tuple $t_s$ in $s$, there is a tuple $t_r$ in $r$ satisfying both of the following:
  a. $t_r[S] = t_s[S]$
  b. $t_r[R - S] = t$

Given the above definition:
a. Write a relational algebra expression using the division operator to find the IDs of all students who have taken all Comp. Sci. courses. *(Hint: project takes to just ID and course_id, and generate the set of all Comp. Sci. course_ids using a select expression, before doing the division.)*
b. Show how to write the above query in relational algebra, without using division. *(By doing so, you would have shown how to define the division operation using the other relational algebra operations.)*

#### 1. Core Principles & Concept Overview
The relational division operator suits queries containing the universal quantifier phrase **"for all"** or **"for every"** (e.g., *"students who have taken all courses offered by..."*).
- Primitive relational algebra lacks an explicit universal quantifier ($\forall$).
- In formal logic, universal quantification is transformed into existential quantification via double negation:
$$
\forall x \, P(x) \iff \neg \exists x \, (\neg P(x))
$$
- In relational algebra, negation ($\neg$) is implemented via **Set Difference ($-$)**.
- Thus, $r \div s$ finds candidates in $\Pi_{R-S}(r)$ such that there does *not* exist any tuple in $s$ that they fail to match.

```text
                         ALGEBRAIC DERIVATION OF DIVISION: r ÷ s
                         
┌───────────────────────┐          ┌───────────────────────┐
│     All Candidates    │          │     Target Set (s)    │
│      Π_{R-S}(r)       │          │          s            │
└───────────┬───────────┘          └───────────┬───────────┘
            │                                  │
            └────────────────┬─────────────────┘
                             ▼
            ┌──────────────────────────────────┐
            │     All Possible Ideal Pairs     │
            │          Π_{R-S}(r) × s          │  (What every candidate MUST possess)
            └────────────────┬─────────────────┘
                             │
                             ▼  Minus Observed Pairs: - r
            ┌──────────────────────────────────┐
            │          Missing Pairs           │
            │       (Π_{R-S}(r) × s) - r       │  (Courses that candidate DID NOT take)
            └────────────────┬─────────────────┘
                             │
                             ▼  Project Candidates: Π_{R-S}(...)
            ┌──────────────────────────────────┐
            │    Disqualified Candidates       │
            │   Candidates with ≥ 1 missing    │
            └────────────────┬─────────────────┘
                             │
                             ▼  Subtract from All Candidates: Π_{R-S}(r) - Disqualified
            ┌──────────────────────────────────┐
            │         Final Result             │
            │   Candidates with 0 missing      │
            └──────────────────────────────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Relational algebra expression using the division operator ($\div$)

1. **Construct relation $r$ (Student course enrollments):**
   We extract the student identifier and course identifier pairs from the `takes` relation:
$$
r_1 \leftarrow \Pi_{\text{ID}, \text{course\_id}}(takes)
$$
   Here, $\text{Schema}(r_1) = \{\text{ID}, \text{course\_id}\}$.

2. **Construct relation $s$ (All Comp. Sci. courses):**
   We filter the `course` relation for courses belonging to the "Comp. Sci." department and project only their `course_id`:
$$
s_1 \leftarrow \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))
$$
   Here, $\text{Schema}(s_1) = \{\text{course\_id}\}$.

3. **Verify schema preconditions:**
   $S = \{\text{course\_id}\} \subset R = \{\text{ID}, \text{course\_id}\}$.  
   The resulting schema will be $R - S = \{\text{ID}\}$.

4. **Apply relational division:**
$$
\boxed{\Pi_{\text{ID}, \text{course\_id}}(takes) \div \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))}
$$

##### Part (b): Derivation of Division using Fundamental Operators ($\Pi, \times, -$)

We now systematically define $r_1 \div s_1$ without using $\div$:

1. **Step 1 — Identify all potential candidates:**
   Every student who has taken at least one course is a candidate:
$$
T_1 \leftarrow \Pi_{\text{ID}}(r_1) = \Pi_{\text{ID}}(takes)
$$

2. **Step 2 — Generate all required combinations (The Cartesian Universe):**
   Compute the Cartesian product of all candidate students with all Comp. Sci. courses. This produces the complete set of pairs $(\text{ID}, \text{course\_id})$ that would exist if *every* student had taken *every* Comp. Sci. course:
$$
T_2 \leftarrow T_1 \times s_1 = \Pi_{\text{ID}}(takes) \times \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))
$$

3. **Step 3 — Identify missing pairings (Courses candidates failed to take):**
   Subtract the observed enrollments $r_1$ from the hypothetical complete universe $T_2$. Any tuple $(\text{ID}, \text{course\_id})$ remaining in $T_3$ represents a Comp. Sci. course that student $\text{ID}$ **did not take**:
$$
T_3 \leftarrow T_2 - r_1 = \Big(\Pi_{\text{ID}}(takes) \times \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))\Big) - \Pi_{\text{ID}, \text{course\_id}}(takes)
$$

4. **Step 4 — Collect all disqualified students:**
   Project the student IDs from $T_3$. Any student appearing in $T_4$ has failed to take at least one Comp. Sci. course:
$$
T_4 \leftarrow \Pi_{\text{ID}}(T_3) = \Pi_{\text{ID}}\Big(\big(\Pi_{\text{ID}}(takes) \times s_1\big) - r_1\Big)
$$

5. **Step 5 — Subtract disqualified students from all candidates:**
   Subtract the disqualified students $T_4$ from the full set of candidate students $T_1$. The remaining students have **zero** missing Comp. Sci. courses—meaning they have taken all of them:
$$
\boxed{T_{\text{result}} \leftarrow T_1 - T_4 = \Pi_{\text{ID}}(takes) - \Pi_{\text{ID}}\Big(\big(\Pi_{\text{ID}}(takes) \times \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))\big) - \Pi_{\text{ID}, \text{course\_id}}(takes)\Big)}
$$

##### General Canonical Definition of Relational Division
For any relations $r(R)$ and $s(S)$ where $S \subset R$:
$$
\boxed{r \div s \equiv \Pi_{R - S}(r) - \Pi_{R - S}\Big((\Pi_{R - S}(r) \times s) - r\Big)}
$$

##### Relational Calculus Formulation (T04.5)
- **Domain Relational Calculus (DRC):**
$$
\{\langle i \rangle \mid \exists c, s, y, g (\langle i, c, s, y, g \rangle \in takes) \land \forall cid (\exists t, cr (\langle cid, t, \text{"Comp. Sci."}, cr \rangle \in course) \to \exists sec, sem, yr, gr (\langle i, cid, sec, sem, yr, gr \rangle \in takes))\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!WARNING] The Universal Quantifier Fallacy in RUET Finals
> Students frequently attempt to write universal queries using simple selection or projection, e.g.:
> $$
> \Pi_{\text{ID}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(takes \bowtie course)) \quad \text{--- INCORRECT!}
> $$
> This incorrect expression finds students who took **at least one** Comp. Sci. course, rather than **all** Comp. Sci. courses.
> 
> **Scoring Rubric in RUET Finals (typically 5 to 7 marks):**
> - **1 Mark:** Correctly projecting $takes$ to $(\text{ID}, \text{course\_id})$.
> - **1 Mark:** Correctly filtering Comp. Sci. courses.
> - **2 Marks:** Constructing the universal Cartesian space ($\Pi_{\text{ID}}(r) \times s$).
> - **2 Marks:** Computing the double negation via nested set differences ($T_{\text{all}} - \Pi(T_{\text{universal}} - r)$).

---

## T04.2 · Schema Query Formulation & Algebraic Equivalences

### Exercise 2.6 · Basic Selection and Projection on Employee Database

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Practice Exercise 2.6 (Page 60)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **RUET Past Exam Hit:** ⚠️ **Directly Recycled in 2017 Q.2(a)** [8 Marks]
> - **Core Concepts:** Attribute selection, relational projection, multi-table joining, intersection vs. conjunction

**Question (Silberschatz 7e Practice Exercise 2.6).**
Consider the employee database of Figure 2.17:
- $\text{employee}(\underline{\text{ID}}, \text{person\_name}, \text{street}, \text{city})$
- $\text{works}(\underline{\text{ID}}, \text{company\_name}, \text{salary})$
- $\text{company}(\underline{\text{company\_name}}, \text{city})$
- $\text{manages}(\underline{\text{ID}}, \text{manager\_id})$

Give an expression in the relational algebra to express each of the following queries:
a. Find the name of each employee who lives in city “Miami”.
b. Find the name of each employee whose salary is greater than \$100,000.
c. Find the name of each employee who lives in “Miami” and whose salary is greater than \$100,000.

#### 1. Core Principles & Concept Overview
- Queries requiring filtering on attributes from a single table use selection $\sigma$ followed by projection $\Pi$.
- Queries requiring attributes split across multiple relations (e.g., `salary` in `works` and `person_name` in `employee`) require combining relations via Natural Join ($\bowtie$) on their shared key `ID`.
- A conjunction ($P_1 \land P_2$) can be implemented either as a composite selection predicate or as the set intersection ($\cap$) of two subqueries, provided both subqueries project identical schemas.

#### 2. Detailed Step-by-Step Solution

##### Query (a): Employees living in Miami
1. **Filter:** Select tuples from `employee` where `city` equals `"Miami"`.
2. **Project:** Extract the `person_name` attribute.
$$
\boxed{\Pi_{\text{person\_name}}(\sigma_{\text{city} = \text{"Miami"}}(employee))}
$$
- **Step-by-step intermediate assignment:**
$$
T_1 \leftarrow \sigma_{\text{city} = \text{"Miami"}}(employee)
$$
$$
T_{\text{result}} \leftarrow \Pi_{\text{person\_name}}(T_1)
$$
- **DRC Formulation (T04.5):**
$$
\{\langle n \rangle \mid \exists i, s (\langle i, n, s, \text{"Miami"} \rangle \in employee)\}
$$

##### Query (b): Employees whose salary > \$100,000
1. **Identify attribute locations:** `salary` is stored in `works`, but `person_name` is in `employee`.
2. **Join relations:** Join `employee` and `works` on the shared attribute `ID`.
3. **Filter and Project:**
$$
\boxed{\Pi_{\text{person\_name}}(\sigma_{\text{salary} > 100000}(employee \bowtie works))}
$$
- **Optimized algebraic variant ($\sigma$-pushdown):**
  Filter the `works` relation prior to joining to minimize intermediate join cardinality:
$$
\boxed{\Pi_{\text{person\_name}}(employee \bowtie \sigma_{\text{salary} > 100000}(works))}
$$

> [!NOTE] 6th Edition / RUET 2017 Format
> In the 2017 exam paper, `works` was defined as `works(person_name, company_name, salary)`. Because `person_name` was directly present in `works`, no join was necessary:
> $$
> \Pi_{\text{person\_name}}(\sigma_{\text{salary} > 100000}(works))
> $$
> When solving for RUET, state which schema is assumed.

- **DRC Formulation (T04.5):**
$$
\{\langle n \rangle \mid \exists i, s, c, co, sal (\langle i, n, s, c \rangle \in employee \land \langle i, co, sal \rangle \in works \land sal > 100000)\}
$$

##### Query (c): Employees living in Miami AND earning > \$100,000

We provide two mathematically equivalent formulations:

- **Method 1: Composite Selection Predicate over Join**
$$
\boxed{\Pi_{\text{person\_name}}(\sigma_{\text{city} = \text{"Miami"} \land \text{salary} > 100000}(employee \bowtie works))}
$$

- **Method 2: Set Intersection ($\cap$) of Subqueries**
  Since both subqueries output union-compatible unary relations of schema $(\text{person\_name})$:
$$
\boxed{\Pi_{\text{person\_name}}(\sigma_{\text{city} = \text{"Miami"}}(employee)) \cap \Pi_{\text{person\_name}}(employee \bowtie \sigma_{\text{salary} > 100000}(works))}
$$

- **DRC Formulation (T04.5):**
$$
\{\langle n \rangle \mid \exists i, s, co, sal (\langle i, n, s, \text{"Miami"} \rangle \in employee \land \langle i, co, sal \rangle \in works \land sal > 100000)\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!IMPORTANT] Direct Exam Match: 2017 Q.2(a)
> In RUET 2017 Q.2(a), this exact scenario formed parts (i)–(iv). Students who omitted the join between `employee` and `works` when using the modern 7e schema lost marks because `person_name` and `salary` are in separate relations. Always verify whether an attribute requires a join.

---

### Exercise 2.7 · Banking Queries: Branch Selection and Borrower Join

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Practice Exercise 2.7 (Page 60)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **Database Schema:** Bank Database (Figure 2.18)
> - **Core Concepts:** Unary selection, multi-relation navigation, natural join vs. theta join

**Question (Silberschatz 7e Practice Exercise 2.7).**
Consider the bank database of Figure 2.18:
- $\text{branch}(\underline{\text{branch\_name}}, \text{branch\_city}, \text{assets})$
- $\text{customer}(\underline{\text{ID}}, \text{customer\_name}, \text{customer\_street}, \text{customer\_city})$
- $\text{loan}(\underline{\text{loan\_number}}, \text{branch\_name}, \text{amount})$
- $\text{borrower}(\underline{\text{ID}, \text{loan\_number}})$
- $\text{account}(\underline{\text{account\_number}}, \text{branch\_name}, \text{balance})$
- $\text{depositor}(\underline{\text{ID}, \text{account\_number}})$

Give an expression in the relational algebra for each of the following queries:
a. Find the name of each branch located in “Chicago”.
b. Find the ID of each borrower who has a loan in branch “Downtown”.

#### 1. Core Principles & Concept Overview
- Query (a) tests basic unary filtering on a single entity table.
- Query (b) requires connecting a relationship relation (`borrower`) with an entity relation (`loan`) across their shared foreign key (`loan_number`).

#### 2. Detailed Step-by-Step Solution

##### Query (a): Branch names located in Chicago
1. Filter `branch` on $\text{branch\_city} = \text{"Chicago"}$.
2. Project `branch_name`.
$$
\boxed{\Pi_{\text{branch\_name}}(\sigma_{\text{branch\_city} = \text{"Chicago"}}(branch))}
$$
- **Step-by-step intermediate assignment:**
$$
T_1 \leftarrow \sigma_{\text{branch\_city} = \text{"Chicago"}}(branch)
$$
$$
T_{\text{result}} \leftarrow \Pi_{\text{branch\_name}}(T_1)
$$
- **DRC Formulation (T04.5):**
$$
\{\langle b \rangle \mid \exists a (\langle b, \text{"Chicago"}, a \rangle \in branch)\}
$$

##### Query (b): IDs of borrowers who have a loan in branch "Downtown"
1. **Identify tables needed:** `borrower` provides `ID` and `loan_number`. `loan` provides `loan_number` and `branch_name`.
2. **Step 1 — Filter loans at the "Downtown" branch:**
$$
T_1 \leftarrow \sigma_{\text{branch\_name} = \text{"Downtown"}}(loan)
$$
3. **Step 2 — Join with `borrower` on `loan_number`:**
$$
T_2 \leftarrow borrower \bowtie T_1
$$
4. **Step 3 — Project the borrower `ID`:**
$$
\boxed{\Pi_{\text{ID}}(borrower \bowtie \sigma_{\text{branch\_name} = \text{"Downtown"}}(loan))}
$$
- **Alternative formulation without natural join (explicit Theta join):**
$$
\Pi_{\text{borrower.ID}}(\sigma_{\text{borrower.loan\_number} = \text{loan.loan\_number} \land \text{branch\_name} = \text{"Downtown"}}(borrower \times loan))
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i \rangle \mid \exists l, a (\langle i, l \rangle \in borrower \land \langle l, \text{"Downtown"}, a \rangle \in loan)\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!NOTE] Redundant Join Penalty
> A frequent mistake in RUET scripts is joining `customer` unnecessarily:
> $$
> \Pi_{\text{customer.ID}}(customer \bowtie borrower \bowtie loan)
> $$
> Because `borrower` already contains the `ID` attribute, joining with `customer` is redundant and incurs a grade deduction for inefficient relational query design.

---

### Exercise 2.8 · Negation via Set Difference and Emulating Maximum Salary

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Practice Exercise 2.8 (Page 61)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **RUET Relevance:** Very High. Emulating `NOT IN` and `MAX()` using primitive algebra is a favorite topic in finals (e.g. 2017 Q.2a(iv), 2020 Q.2a).
> - **Core Operators:** Set Difference ($-$), Cartesian Product ($\times$), Renaming ($\rho$), Projection ($\Pi$)

**Question (Silberschatz 7e Practice Exercise 2.8).**
Consider the employee database of Figure 2.17:
- $\text{employee}(\underline{\text{ID}}, \text{person\_name}, \text{street}, \text{city})$
- $\text{works}(\underline{\text{ID}}, \text{company\_name}, \text{salary})$
- $\text{company}(\underline{\text{company\_name}}, \text{city})$
- $\text{manages}(\underline{\text{ID}}, \text{manager\_id})$

Give an expression in the relational algebra to express each of the following queries:
a. Find the ID and name of each employee who does not work for “BigBank”.
b. Find the ID and name of each employee who earns at least as much as every employee in the database.

#### 1. Core Principles & Concept Overview
1. **The Set Difference Negation Principle:** In relational algebra, finding entities that *do not* satisfy condition $C$ cannot be solved by simply writing $\sigma_{\neg C}(R)$. An employee might have no record in `works` (unemployed) or might work for multiple companies. The mathematically sound approach is:
$$
\text{Result} = (\text{All Entities}) - (\text{Entities satisfying } C)
$$
2. **Emulating Universal Comparison ($\ge \text{all}$) without Aggregation:** Primitive relational algebra has no $\text{MAX}()$ function. To find the maximum salary:
   - Identify all salaries that are **strictly less than** at least one other salary (using a Cartesian self-product and $\sigma_{salary < salary'}$).
   - Subtract these non-maximum salaries from the complete set of salaries.

```text
               EMULATING MAX(SALARY) VIA SET DIFFERENCE
               
┌──────────────────────┐               ┌──────────────────────┐
│     works (w1)       │               │     works (w2)       │
│   (ID1, comp1, sal1) │               │   (ID2, comp2, sal2) │
└──────────┬───────────┘               └──────────┬───────────┘
           │                                      │
           └──────────────────┬───────────────────┘
                              ▼
           ┌──────────────────────────────────────┐
           │     Cartesian Product: w1 × w2       │
           └──────────────────┬───────────────────┘
                              │
                              ▼  Filter condition: w1.salary < w2.salary
           ┌──────────────────────────────────────┐
           │      Tuples where sal1 is NOT max    │
           │      (Someone earns strictly more)   │
           └──────────────────┬───────────────────┘
                              │
                              ▼  Project IDs: Π_{w1.ID}(...)
           ┌──────────────────────────────────────┐
           │       All Non-Top-Earner IDs         │  (T_inferior)
           └──────────────────┬───────────────────┘
                              │
                              ▼  Set Difference: All Working IDs - T_inferior
           ┌──────────────────────────────────────┐
           │         Maximum Earner ID(s)         │
           └──────────────────────────────────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Query (a): Employees who do not work for “BigBank”

- **Step 1 — Find all employees in the database:**
$$
T_{\text{all}} \leftarrow \Pi_{\text{ID}, \text{person\_name}}(employee)
$$

- **Step 2 — Find all employees who DO work for BigBank:**
$$
T_{\text{BigBank}} \leftarrow \Pi_{\text{ID}, \text{person\_name}}(employee \bowtie \sigma_{\text{company\_name} = \text{"BigBank"}}(works))
$$

- **Step 3 — Compute the set difference:**
$$
\boxed{T_{\text{result}} \leftarrow T_{\text{all}} - T_{\text{BigBank}}}
$$

- **Unified Single Expression:**
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}(employee) - \Pi_{\text{ID}, \text{person\_name}}(employee \bowtie \sigma_{\text{company\_name} = \text{"BigBank"}}(works))}
$$

> [!CAUTION] The "$\sigma_{\text{company\_name} \neq \text{'BigBank'}}$" Fatal Exam Trap
> Writing:
> $$
> \Pi_{\text{ID}, \text{person\_name}}(\sigma_{\text{company\_name} \neq \text{"BigBank"}}(employee \bowtie works))
> $$
> is fundamentally wrong. If an employee works for both `"BigBank"` and `"TechCorp"`, their `"TechCorp"` tuple satisfies $\text{company\_name} \neq \text{"BigBank"}$, causing them to be incorrectly included in the output! Set difference is the only valid algebraic solution.

- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \neg \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works)\}
$$

##### Query (b): Employees earning at least as much as every employee (Maximum Salary)

- **Step 1 — Identify all employees who earn strictly less than someone else:**
  We rename `works` to $d$ to form a Cartesian self-product:
$$
T_{\text{pairs}} \leftarrow works \times \rho_d(works)
$$
  Select tuples where the first employee's salary is strictly less than the second employee's salary:
$$
T_{\text{inferior\_ids}} \leftarrow \Pi_{works.\text{ID}}(\sigma_{works.\text{salary} < d.\text{salary}}(works \times \rho_d(works)))
$$

- **Step 2 — Subtract inferior earners from all working employees:**
  The employees remaining in $T_{\text{max\_id}}$ are those for whom no other employee earns a higher salary:
$$
T_{\text{max\_id}} \leftarrow \Pi_{\text{ID}}(works) - T_{\text{inferior\_ids}}
$$

- **Step 3 — Retrieve the names of the top earners:**
  Join $T_{\text{max\_id}}$ with `employee`:
$$
\boxed{T_{\text{result}} \leftarrow \Pi_{\text{ID}, \text{person\_name}}(employee \bowtie T_{\text{max\_id}})}
$$

- **Unified Nested Expression in Pure Primitive Algebra:**
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}\Big(employee \bowtie \Big(\Pi_{\text{ID}}(works) - \Pi_{works.\text{ID}}(\sigma_{works.\text{salary} < d.\text{salary}}(works \times \rho_d(works)))\Big)\Big)}
$$

- **Alternative Modern Extended Algebra using Aggregate Operator ($\gamma$):**
  If extended relational algebra is permitted:
$$
T_{\text{max\_sal}} \leftarrow \gamma_{\text{max}(\text{salary}) \ \text{as} \ \text{top\_sal}}(works)
$$
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}(employee \bowtie works \bowtie_{\text{salary} = \text{top\_sal}} T_{\text{max\_sal}})}
$$

- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \exists co, sal (\langle i, co, sal \rangle \in works \land \forall i_2, co_2, sal_2 (\langle i_2, co_2, sal_2 \rangle \in works \to sal \ge sal_2))\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!TIP] Pure vs. Extended Algebra Expectations
> When RUET questions state *"Write down the relational algebra (Not SQL)"*, examiners award maximum credit to students who show the pure Codd self-product difference technique for finding extrema ($\text{MAX}/\text{MIN}$), as it demonstrates a deep understanding of first-order relational completeness. Mentioning both the primitive set-difference derivation and the $\gamma$ operator guarantees full marks.

---

### Exercise 2.14 · Employee Database Joins and Same-City Matching

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Exercise 2.14 (Page 62)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **RUET Direct Hit:** ⚠️ **Part (d) was asked verbatim in 2017 Q.2(a)(i)** [2 Marks]
> - **Core Concepts:** Filtering, multi-table joining, natural join attribute alignment, same-city matching

**Question (Silberschatz 7e Exercise 2.14).**
Consider the employee database of Figure 2.17:
- $\text{employee}(\underline{\text{ID}}, \text{person\_name}, \text{street}, \text{city})$
- $\text{works}(\underline{\text{ID}}, \text{company\_name}, \text{salary})$
- $\text{company}(\underline{\text{company\_name}}, \text{city})$
- $\text{manages}(\underline{\text{ID}}, \text{manager\_id})$

Give an expression in the relational algebra to express each of the following queries:
a. Find the ID and name of each employee who works for “BigBank”.
b. Find the ID, name, and city of residence of each employee who works for “BigBank”.
c. Find the ID, name, street address, and city of residence of each employee who works for “BigBank” and earns more than \$10,000.
d. Find the ID and name of each employee in this database who lives in the same city as the company for which she or he works.

#### 1. Core Principles & Concept Overview
- Queries (a)–(c) involve joining `employee` and `works` on `ID` while progressively projecting more attributes.
- Query (d) requires joining three relations: `employee`, `works`, and `company`. Both `employee` and `company` share an attribute named `city`. Under a **Natural Join** ($\bowtie$), attributes with identical names across participating relations are automatically equated.

#### 2. Detailed Step-by-Step Solution

##### Query (a): ID and name of employees working for "BigBank"
Filter `works` on `company_name = "BigBank"`, natural join with `employee` on `ID`, and project `ID, person_name`:
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}(\sigma_{\text{company\_name} = \text{"BigBank"}}(works) \bowtie employee)}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works)\}
$$

##### Query (b): ID, name, and city of residence of employees working for "BigBank"
Same as (a), including `city` in the projection list:
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}, \text{city}}(\sigma_{\text{company\_name} = \text{"BigBank"}}(works) \bowtie employee)}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n, c \rangle \mid \exists s (\langle i, n, s, c \rangle \in employee) \land \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works)\}
$$

##### Query (c): ID, name, street address, and city of employees working for "BigBank" earning > \$10,000
Add the salary predicate $\text{salary} > 10000$ to the selection on `works`:
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}, \text{street}, \text{city}}(\sigma_{\text{company\_name} = \text{"BigBank"} \land \text{salary} > 10000}(works) \bowtie employee)}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n, s, c \rangle \mid \langle i, n, s, c \rangle \in employee \land \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works \land sal > 10000)\}
$$

##### Query (d): ID and name of employees who live in the same city as their company

- **Method 1: Natural Join Elegance ($\bowtie$)**
  Let us examine the attribute intersection across the three schemas:
  - $\text{Schema}(employee) = \{\text{ID}, \text{person\_name}, \text{street}, \text{city}\}$
  - $\text{Schema}(works) = \{\text{ID}, \text{company\_name}, \text{salary}\}$
  - $\text{Schema}(company) = \{\text{company\_name}, \text{city}\}$

  When computing $employee \bowtie works \bowtie company$, natural join equates:
  1. $employee.\text{ID} = works.\text{ID}$
  2. $works.\text{company\_name} = company.\text{company\_name}$
  3. $employee.\text{city} = company.\text{city}$

  Because the common attribute `city` between `employee` and `company` is automatically equated, the natural join directly enforces that the employee lives in the company's city:
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}(employee \bowtie works \bowtie company)}
$$

- **Method 2: Explicit Theta Join with Renaming ($\rho$)**
  To make the predicate unmistakable to an examiner who may overlook the natural join's handling of `city`:
$$
T_{\text{comp}} \leftarrow \rho_{\text{comp}(\text{c\_name}, \text{c\_city})}(company)
$$
$$
T_{\text{joined}} \leftarrow employee \bowtie works \bowtie_{works.\text{company\_name} = comp.\text{c\_name}} comp
$$
$$
\boxed{\Pi_{\text{ID}, \text{person\_name}}(\sigma_{\text{city} = \text{c\_city}}(T_{\text{joined}}))}
$$

- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists s, c, co, sal (\langle i, n, s, c \rangle \in employee \land \langle i, co, sal \rangle \in works \land \langle co, c \rangle \in company)\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!NOTE] 2017 Exam Match
> In **2017 Q.2(a)(i)**, the question asked: *"Find the names of all employees who live in the city same as their corresponding company location."*  
> Writing $\Pi_{\text{person\_name}}(employee \bowtie works \bowtie company)$ is standard in RUET exam scripts. Providing the explicit renaming theta-join version alongside it eliminates any ambiguity regarding how the dual `city` columns are handled.

---

### Exercise 2.15 · Banking Queries: Loan Amounts and Depositor Balances

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Exercise 2.15 (Page 62)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **Database Schema:** Bank Database (Figure 2.18)
> - **Core Concepts:** Range comparison, multi-table joining, selective attribute projection

**Question (Silberschatz 7e Exercise 2.15).**
Consider the bank database of Figure 2.18:
- $\text{branch}(\underline{\text{branch\_name}}, \text{branch\_city}, \text{assets})$
- $\text{customer}(\underline{\text{ID}}, \text{customer\_name}, \text{customer\_street}, \text{customer\_city})$
- $\text{loan}(\underline{\text{loan\_number}}, \text{branch\_name}, \text{amount})$
- $\text{borrower}(\underline{\text{ID}, \text{loan\_number}})$
- $\text{account}(\underline{\text{account\_number}}, \text{branch\_name}, \text{balance})$
- $\text{depositor}(\underline{\text{ID}, \text{account\_number}})$

Give an expression in the relational algebra for each of the following queries:
a. Find each loan number with a loan amount greater than \$10,000.
b. Find the ID of each depositor who has an account with a balance greater than \$6,000.
c. Find the ID of each depositor who has an account with a balance greater than \$6,000 at the “Uptown” branch.

#### 1. Core Principles & Concept Overview
- Query (a) operates entirely on `loan`.
- Query (b) joins `depositor` and `account` over `account_number`.
- Query (c) extends (b) by adding a selection condition on `branch_name`.

#### 2. Detailed Step-by-Step Solution

##### Query (a): Loan numbers with amount > \$10,000
1. Filter the `loan` relation where $\text{amount} > 10000$.
2. Project `loan_number`.
$$
\boxed{\Pi_{\text{loan\_number}}(\sigma_{\text{amount} > 10000}(loan))}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle l \rangle \mid \exists b, a (\langle l, b, a \rangle \in loan \land a > 10000)\}
$$

##### Query (b): Depositor IDs with an account balance > \$6,000
1. Filter `account` for balances strictly greater than 6000.
2. Natural join with `depositor` on `account_number`.
3. Project the customer `ID`.
$$
\boxed{\Pi_{\text{ID}}(depositor \bowtie \sigma_{\text{balance} > 6000}(account))}
$$
- **Step-by-step intermediate assignment:**
$$
T_1 \leftarrow \sigma_{\text{balance} > 6000}(account)
$$
$$
T_2 \leftarrow depositor \bowtie T_1
$$
$$
T_{\text{result}} \leftarrow \Pi_{\text{ID}}(T_2)
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i \rangle \mid \exists acc, b, bal (\langle i, acc \rangle \in depositor \land \langle acc, b, bal \rangle \in account \land bal > 6000)\}
$$

##### Query (c): Depositor IDs with an account balance > \$6,000 at the "Uptown" branch
1. Filter `account` using a compound predicate: $\text{branch\_name} = \text{"Uptown"} \land \text{balance} > 6000$.
2. Natural join with `depositor` on `account_number`.
3. Project `ID`.
$$
\boxed{\Pi_{\text{ID}}(depositor \bowtie \sigma_{\text{branch\_name} = \text{"Uptown"} \land \text{balance} > 6000}(account))}
$$
- **Alternative via intersection:**
$$
\Pi_{\text{ID}}(depositor \bowtie \sigma_{\text{balance} > 6000}(account)) \cap \Pi_{\text{ID}}(depositor \bowtie \sigma_{\text{branch\_name} = \text{"Uptown"}}(account))
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i \rangle \mid \exists acc, bal (\langle i, acc \rangle \in depositor \land \langle acc, \text{"Uptown"}, bal \rangle \in account \land bal > 6000)\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!TIP] Attribute Scope Checking
> When writing relational algebra for banking systems, check whether `branch_name` is present in `account` before attempting to join the `branch` table. Since `account` already contains `branch_name`, joining `branch` is redundant.

---

### Exercise 2.18 · University Schema: Instructor Navigation and Negative Existential Queries

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 2, Exercise 2.18 (Page 62–63)
> - **Subtopic:** T04.2 · Write RA queries on a given schema
> - **Database Schema:** Standard University Schema (Appendix A)
> - **RUET Relevance:** Very High. University schema queries recur in semester finals (e.g., 2019 Q.2b, 2021 Q.2a, 2024 Q.2b).
> - **Key Pitfalls:** The Natural Join Attribute Clash Trap and Negative Existential Queries.

**Question (Silberschatz 7e Exercise 2.18).**
Write the following queries in relational algebra, using the university schema:
a. Find the ID and name of each instructor in the Physics department.
b. Find the ID and name of each instructor in a department located in the building “Watson”.
c. Find the ID and name of each student who has taken at least one course in the “Comp. Sci.” department.
d. Find the ID and name of each student who has taken at least one course section in the year 2018.
e. Find the ID and name of each student who has not taken any course section in the year 2018.

#### 1. Core Principles & Concept Overview
- Query (a) is a straightforward single-table filter and projection.
- Query (b) joins `instructor` with `department`.
- **Query (c) exposes a critical pitfall: The Natural Join Attribute Clash Trap.** Both `student` and `course` have an attribute named `dept_name`. A naive natural join $student \bowtie takes \bowtie course$ inadvertently equates $student.\text{dept\_name} = course.\text{dept\_name}$, restricting the result to students taking Comp. Sci. courses *within their own department*. This unintended constraint must be prevented by projecting away `dept_name` before joining.
- Query (e) is a **Negative Existential Query**, which requires Set Difference ($-$) rather than a simple inequality predicate.

#### 2. Detailed Step-by-Step Solution

##### Query (a): ID and name of instructors in the Physics department
Filter `instructor` on `dept_name = "Physics"` and project `ID, name`:
$$
\boxed{\Pi_{\text{ID}, \text{name}}(\sigma_{\text{dept\_name} = \text{"Physics"}}(instructor))}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists sal (\langle i, n, \text{"Physics"}, sal \rangle \in instructor)\}
$$

##### Query (b): ID and name of instructors in departments in building "Watson"
Join `instructor` with `department` on their shared attribute `dept_name`:
$$
\boxed{\Pi_{\text{ID}, \text{name}}(instructor \bowtie \sigma_{\text{building} = \text{"Watson"}}(department))}
$$
- **Step-by-step intermediate assignment:**
$$
T_1 \leftarrow \sigma_{\text{building} = \text{"Watson"}}(department)
$$
$$
T_2 \leftarrow instructor \bowtie T_1
$$
$$
T_{\text{result}} \leftarrow \Pi_{\text{ID}, \text{name}}(T_2)
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists d, sal, b, bud (\langle i, n, d, sal \rangle \in instructor \land \langle d, \text{"Watson"}, bud \rangle \in department)\}
$$

##### Query (c): Students who have taken at least one course in the "Comp. Sci." department

> [!CAUTION] The Natural Join Attribute Clash Trap
> Look at the relation schemas:
> - $\text{student}(\underline{\text{ID}}, \text{name}, \mathbf{dept\_name}, \text{tot\_cred})$
> - $\text{takes}(\underline{\text{ID}, \text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}}, \text{grade})$
> - $\text{course}(\underline{\text{course\_id}}, \text{title}, \mathbf{dept\_name}, \text{credits})$
> 
> If you write:
> $$
> \Pi_{\text{ID}, \text{name}}(student \bowtie takes \bowtie \sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course)) \quad \text{--- INCORRECT!}
> $$
> 
> The natural join matches on **all** common attribute names: both `ID` (between `student` and `takes`), `course_id` (between `takes` and `course`), **and** `dept_name` (between `student` and `course`). This forces $student.\text{dept\_name} = \text{"Comp. Sci."}$, erroneously excluding any Physics, Math, or EE student who took a Comp. Sci. course!

**Correct Derivation (Projecting away the colliding attribute):**
1. Filter `course` for `"Comp. Sci."` and project **only** `course_id`:
$$
T_{\text{cs\_courses}} \leftarrow \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))
$$
2. Join with `takes` on `course_id`:
$$
T_{\text{cs\_takes}} \leftarrow takes \bowtie T_{\text{cs\_courses}}
$$
3. Join with `student` on `ID` (now free from any `dept_name` collision):
$$
T_{\text{cs\_students}} \leftarrow student \bowtie T_{\text{cs\_takes}}
$$
4. Project `ID` and `name`:
$$
\boxed{\Pi_{\text{ID}, \text{name}}\Big(student \bowtie \big(takes \bowtie \Pi_{\text{course\_id}}(\sigma_{\text{dept\_name} = \text{"Comp. Sci."}}(course))\big)\Big)}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists d, c (\langle i, n, d, c \rangle \in student) \land \exists cid, s, sm, y, g (\langle i, cid, s, sm, y, g \rangle \in takes \land \exists t, cr (\langle cid, t, \text{"Comp. Sci."}, cr \rangle \in course))\}
$$

##### Query (d): Students who took at least one course section in 2018
1. Filter `takes` for `year = 2018`.
2. Natural join with `student` on `ID`.
3. Project `ID, name`.
$$
\boxed{\Pi_{\text{ID}, \text{name}}(student \bowtie \sigma_{\text{year} = 2018}(takes))}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists d, c (\langle i, n, d, c \rangle \in student) \land \exists cid, s, sm, g (\langle i, cid, s, sm, 2018, g \rangle \in takes)\}
$$

##### Query (e): Students who have NOT taken any course section in 2018

> [!WARNING] The Inequality Selection Bug
> Writing:
> $$
> \Pi_{\text{ID}, \text{name}}(student \bowtie \sigma_{\text{year} \neq 2018}(takes)) \quad \text{--- FATAL ERROR!}
> $$
> If a student took a course in 2017 and another in 2018, their 2017 record satisfies $\text{year} \neq 2018$, causing them to appear in the output. Furthermore, a student who has never enrolled in any course at all has no records in `takes`, so an inner join drops them entirely.

**Correct Derivation via Set Difference ($-$):**
$$
\text{Result} = (\text{All Students}) - (\text{Students who took a course in 2018})
$$
1. Full set of students:
$$
T_{\text{all\_students}} \leftarrow \Pi_{\text{ID}, \text{name}}(student)
$$
2. Students who took at least one course in 2018 (from query d):
$$
T_{\text{2018\_students}} \leftarrow \Pi_{\text{ID}, \text{name}}(student \bowtie \sigma_{\text{year} = 2018}(takes))
$$
3. Compute the difference:
$$
\boxed{\Pi_{\text{ID}, \text{name}}(student) - \Pi_{\text{ID}, \text{name}}(student \bowtie \sigma_{\text{year} = 2018}(takes))}
$$
- **DRC Formulation (T04.5):**
$$
\{\langle i, n \rangle \mid \exists d, c (\langle i, n, d, c \rangle \in student) \land \neg \exists cid, s, sm, g (\langle i, cid, s, sm, 2018, g \rangle \in takes)\}
$$

#### 3. RUET Exam Insights & Examiner Notes
> [!TIP] Common Traps in RUET Finals
> Questions 2.18(c) and 2.18(e) reflect two classic exam patterns:
> 1. **Accidental Join Filtering:** When two tables share an attribute name that is *not* a foreign key between them (e.g., `dept_name` in both `student` and `course`), an unprojected natural join will equate them. Always project away the non-key colliding attribute.
> 2. **Universal Negation:** Questions containing phrases like *"who did not take"*, *"who never borrowed"*, or *"who do not work for"* require set difference ($-$) from a master relation.

---

## T04.5 · Relational Calculus Integration (Domain & Tuple Relational Calculus)

### Theoretical Foundations & Codd's Equivalence Theorem

> [!info] Subtopic Context
> Domain Relational Calculus (DRC) is part of Unit 3 of the ECE 2215 syllabus and was directly tested in **RUET 2020 Q.4(b)** [3 Marks]. 
> Codd's Equivalence Theorem establishes that **Basic Relational Algebra**, **Tuple Relational Calculus (TRC)**, and **Domain Relational Calculus (DRC)** are expressive equivalents restricted to **safe expressions**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      RELATIONAL QUERY LANGUAGES                        │
├──────────────────────────────────┬─────────────────────────────────────┤
│  Procedural (Algebraic)          │  Declarative (Predicate Calculus)   │
├──────────────────────────────────┼─────────────────────────────────────┤
│  Relational Algebra (RA)         │  Tuple Relational Calculus (TRC)    │
│  - User specifies HOW to compute │  - Variables range over tuples: {t} │
│  - Sequence of operators (σ, Π, ⋈)│                                    │
│                                  │  Domain Relational Calculus (DRC)   │
│                                  │  - Variables range over domain values│
│                                  │  - { <x1, x2, ..., xn> | P(...) }  │
└──────────────────────────────────┴─────────────────────────────────────┘
```

#### Syntax and Formal Definition of DRC
A general DRC expression has the form:
$$
\{\langle x_1, x_2, \dots, x_n \rangle \mid P(x_1, x_2, \dots, x_n)\}
$$
where:
- $\langle x_1, x_2, \dots, x_n \rangle$ are **domain variables** representing the resulting attributes.
- $P$ is a first-order logic formula built from:
  1. Membership atoms: $\langle v_1, v_2, \dots, v_k \rangle \in r$
  2. Comparison atoms: $x \ \theta \ y$ or $x \ \theta \ c$ (where $\theta \in \{=, \neq, <, \le, >, \ge\}$ and $c$ is a constant)
  3. Logical connectives: $\land$ (AND), $\lor$ (OR), $\neg$ (NOT)
  4. Quantifiers: $\exists x$ (existential), $\forall x$ (universal)

#### Safety of Calculus Expressions
An expression is **safe** if all values in the result come from the **active domain** ($\text{adom}(\psi)$)—the set of all constants appearing in the formula $\psi$ or in the relations referenced by $\psi$. For example, the unsafe expression:
$$
\{\langle x \rangle \mid \neg (\langle x \rangle \in r)\}
$$
generates an infinite number of values not present in the database. A safe expression ensures that:
1. Every tuple in the result contains values solely from $\text{adom}(\psi)$.
2. For every subformula $\exists x \, (P(x))$, $x$ can only take values from $\text{adom}(P)$.
3. For every subformula $\forall x \, (P(x))$, $x$ must be satisfied for all values outside $\text{adom}(P)$.

---

### Comprehensive DRC & TRC Translation Guide for All Assigned Exercises

| Exercise | Natural Language Description | Equivalent Safe DRC Expression |
| :--- | :--- | :--- |
| **PE 2.5** | Cartesian product of `student` and `advisor` filtered by $s\_id = \text{ID}$ | $\{\langle i, n, d, c, s, a \rangle \mid \langle i, n, d, c \rangle \in student \land \langle s, a \rangle \in advisor \land s = i\}$ |
| **PE 2.6(a)** | Names of employees living in "Miami" | $\{\langle n \rangle \mid \exists i, s (\langle i, n, s, \text{"Miami"} \rangle \in employee)\}$ |
| **PE 2.6(b)** | Names of employees earning $> \$100,000$ | $\{\langle n \rangle \mid \exists i, s, c, co, sal (\langle i, n, s, c \rangle \in employee \land \langle i, co, sal \rangle \in works \land sal > 100000)\}$ |
| **PE 2.6(c)** | Employees living in "Miami" and earning $> \$100,000$ | $\{\langle n \rangle \mid \exists i, s, co, sal (\langle i, n, s, \text{"Miami"} \rangle \in employee \land \langle i, co, sal \rangle \in works \land sal > 100000)\}$ |
| **PE 2.7(a)** | Branch names located in "Chicago" | $\{\langle b \rangle \mid \exists a (\langle b, \text{"Chicago"}, a \rangle \in branch)\}$ |
| **PE 2.7(b)** | Borrower IDs with loan at "Downtown" | $\{\langle i \rangle \mid \exists l, a (\langle i, l \rangle \in borrower \land \langle l, \text{"Downtown"}, a \rangle \in loan)\}$ |
| **PE 2.8(a)** | Employees who do not work for "BigBank" | $\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \neg \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works)\}$ |
| **PE 2.8(b)** | Employees earning maximum salary | $\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \exists co, sal (\langle i, co, sal \rangle \in works \land \forall i_2, co_2, sal_2 (\langle i_2, co_2, sal_2 \rangle \in works \to sal \ge sal_2))\}$ |
| **PE 2.9** | Students who took all Comp. Sci. courses | $\{\langle i \rangle \mid \exists c, s, y, g (\langle i, c, s, y, g \rangle \in takes) \land \forall cid (\exists t, cr (\langle cid, t, \text{"Comp. Sci."}, cr \rangle \in course) \to \exists sec, sem, yr, gr (\langle i, cid, sec, sem, yr, gr \rangle \in takes))\}$ |
| **EX 2.14(a)** | Employees working for "BigBank" | $\{\langle i, n \rangle \mid \exists s, c (\langle i, n, s, c \rangle \in employee) \land \exists sal (\langle i, \text{"BigBank"}, sal \rangle \in works)\}$ |
| **EX 2.14(d)** | Employees living in same city as their company | $\{\langle i, n \rangle \mid \exists s, c, co, sal (\langle i, n, s, c \rangle \in employee \land \langle i, co, sal \rangle \in works \land \langle co, c \rangle \in company)\}$ |
| **EX 2.15(b)** | Depositor IDs with account balance $> \$6,000$ | $\{\langle i \rangle \mid \exists acc, b, bal (\langle i, acc \rangle \in depositor \land \langle acc, b, bal \rangle \in account \land bal > 6000)\}$ |
| **EX 2.18(b)** | Instructors in building "Watson" | $\{\langle i, n \rangle \mid \exists d, sal, bud (\langle i, n, d, sal \rangle \in instructor \land \langle d, \text{"Watson"}, bud \rangle \in department)\}$ |
| **EX 2.18(c)** | Students who took a Comp. Sci. course | $\{\langle i, n \rangle \mid \exists d, c (\langle i, n, d, c \rangle \in student) \land \exists cid, s, sm, y, g (\langle i, cid, s, sm, y, g \rangle \in takes \land \exists t, cr (\langle cid, t, \text{"Comp. Sci."}, cr \rangle \in course))\}$ |
| **EX 2.18(e)** | Students who took NO course in 2018 | $\{\langle i, n \rangle \mid \exists d, c (\langle i, n, d, c \rangle \in student) \land \neg \exists cid, s, sm, g (\langle i, cid, s, sm, 2018, g \rangle \in takes)\}$ |

---

## Pedagogical Comparison: Relational Algebra vs. SQL vs. Relational Calculus

To synthesize the theoretical operations across the three query representations, the table below highlights how typical query patterns are expressed in each formalism:

| Operational Pattern | Relational Algebra | SQL (Declarative Standard) | Domain Relational Calculus (DRC) |
| :--- | :--- | :--- | :--- |
| **Selection ($\sigma$)** | $\sigma_{A = 'v'}(R)$ | `WHERE A = 'v'` | $\langle \dots, 'v', \dots \rangle \in R$ |
| **Projection ($\Pi$)** | $\Pi_{A, B}(R)$ | `SELECT A, B` | $\{\langle a, b \rangle \mid \exists \dots (\langle a, b, \dots \rangle \in R)\}$ |
| **Natural Join ($\bowtie$)** | $R \bowtie S$ | `NATURAL JOIN` / `JOIN ON ...` | $\langle a, b \rangle \in R \land \langle b, c \rangle \in S$ |
| **Intersection ($\cap$)** | $R \cap S$ | `INTERSECT` | $\langle \vec{x} \rangle \in R \land \langle \vec{x} \rangle \in S$ |
| **Set Difference ($-$)** | $R - S$ | `EXCEPT` / `NOT IN` | $\langle \vec{x} \rangle \in R \land \neg(\langle \vec{x} \rangle \in S)$ |
| **Universal Division ($\div$)** | $r \div s$ | `NOT EXISTS (... NOT EXISTS ...)` | $\forall y (\langle y \rangle \in s \to \langle x, y \rangle \in r)$ |
| **Aggregation ($\gamma$)** | ${}_A\gamma_{\text{count}(B)}(R)$ | `GROUP BY A` | *(Requires extended calculus)* |


---

[← Prev: T03](T03_Relational_Model_Keys_and_Integrity.md) | [Index](00_Index.md) | [Next: T05 Part 1 →](T05_Part1_SQL_DDL_DML_Basics.md)
