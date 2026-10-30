---
title: "T02 (Part 1) · E-R and EER Modeling: Basics, Weak Entities & Intro Scenarios · Textbook Solutions"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T02
topic_id: T02
part: 1
exercise_count: 13
source_chapters:
  - "Chapter 06"
---

[← Prev: T01](T01_DB_Concepts_and_Architecture.md) | [Exam-style T02](../Topicwise_answers_exam_style/T02_ER_and_EER_Modeling.md) | [Next: T02 Part 2 →](T02_Part2_ER_Scenarios_Reduction_EER.md)

---

# T02 (Part 1) · E-R and EER Modeling: Basics, Weak Entities & Intro Scenarios

> [!info] Topic Card
> **Topic:** T02 · E-R and EER Modeling (Part 1 · Basics, Weak Entities & Intro Scenarios)
> **Source Chapter:** Silberschatz 7e, Chapter 6 (*Database Design Using the E-R Model*)
> **Exercise Scope:** 13 problems (Practice Exercises 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.9, 6.10, 6.13; Exercises 6.17, 6.18, 6.19)
> **Covered Subtopics:** T02.1, T02.2, T02.3, T02.4, T02.5 (Part A)
> **Past Exam Hits:**
> - ⚠️ **Direct Hit**: PE 6.2 recycled in **2018 Q.2(c)** [4 Marks] (Student, Course, Exam ternary vs binary)
> - ⚠️ **Direct Hit**: EX 6.17 recycled in **2020 Q.2(c)** [3 Marks] and **2021 Q.8(c)** [3 Marks] (Weak vs strong entity sets)

---

## Exercise Directory

| Exercise | Type | Descriptive Title | Subtopic | RUET Exam Hit |
| :--- | :---: | :--- | :---: | :---: |
| **PE 6.5** | Practice | E-R Diagram as a Graph: Disconnected Graphs and Cycles | T02.1 | Conceptual Graph Theory |
| **PE 6.6** | Practice | Ternary Relationship Decomposition into Binary Relationships | T02.1 | Foundation for Ternary Reduction |
| **PE 6.3** | Practice | Sports Team Scoring Statistics & Derived Attributes | T02.2 | Derived Attributes Concept |
| **EX 6.18** | Exercise | Common Attributes Across Entity Sets and Design Fixes | T02.2 | Schema Normalization Trap |
| **PE 6.9** | Practice | Enforcing One-to-One Mapping on the Advisor Relationship | T02.3 | Cardinality SQL Constraints |
| **PE 6.10** | Practice | Enforcing Total Participation via NOT NULL in Combined Schemas | T02.3 | Relational Reduction Rules |
| **PE 6.7** | Practice | Redundancy from Converting Weak Entities to Strong Entities | T02.4 | Weak Entity Mechanics |
| **EX 6.17** | Exercise | Distinction Between Weak and Strong Entity Sets | T02.4 | ⚠️ **2020 Q.2(c), 2021 Q.8(c)** |
| **EX 6.19** | Exercise | Rationale for Weak Entity Sets in Database Modeling | T02.4 | Conceptual Justification |
| **PE 6.1** | Practice | Car Insurance Enterprise E-R Modeling Scenario | T02.5 | Enterprise Scenario Modeling |
| **PE 6.2** | Practice | Student Exam Marks: Ternary vs Binary Design | T02.5 | ⚠️ **2018 Q.2(c)** |
| **PE 6.4** | Practice | Dangers of Repeating Entity Sets with Attributes | T02.5 | Schema Anti-Patterns |
| **PE 6.13** | Practice | Modeling Temporal Changes and Valid-Time Intervals | T02.5 | Advanced E-R Extensions |

---

## T02.1 · Entity sets, relationship sets, types of relationships

### Exercise 6.5 · E-R Diagram as a Graph: Disconnected Graphs and Cycles

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.5
> - **Subtopic:** T02.1 (Entity sets, relationship sets, types of relationships)
> - **Classification:** Conceptual Analysis / Graph-Theoretic Schema Properties
> - **Related RUET Questions:** 2021 Q.5(a) (Types of relationships and diagrammatic representation)

**Question (Silberschatz 7e Exercise 6.5).**

An E-R diagram can be viewed as a graph. What do the following mean in terms of the structure of an enterprise schema?

a. The graph is disconnected.  
b. The graph has a cycle.

#### 1. Core Principles & Concept Overview

In graph-theoretic terms, an Entity-Relationship (E-R) diagram is an undirected bipartite graph $G = (V_E \cup V_R, E_{\text{links}})$. The vertex set consists of two disjoint partitions:
1. $V_E$, the set of entity set nodes (drawn as rectangles).
2. $V_R$, the set of relationship set nodes (drawn as diamonds).

Edges $e = (u, v) \in E_{\text{links}}$ connect entity sets to relationship sets. Graph topology reveals the operational cohesion and integrity constraints of an enterprise schema.

#### 2. Detailed Step-by-Step Solution

##### Part (a): The Graph is Disconnected

A graph is disconnected if it contains two or more connected components with no edges connecting them.

```text
Component 1 (Academic Domain)           Component 2 (Transport Domain)
[STUDENT] ----- <Takes> ----- [COURSE]    [BUS] ----- <Assigned_To> ----- [DRIVER]
```

**Meaning for Enterprise Structure:**
- The enterprise database consists of two or more completely independent operational domains.
- Entities in one component share zero direct or indirect relationships with entities in the other component.
- *Query Implications:* A query joining entities across disconnected components (for example, `STUDENT` and `DRIVER`) produces a Cartesian product ($R \times S$). The database has no shared foreign key path or logical relationship to filter tuples.
- *Design Verdict:* Disconnected schemas often indicate either two distinct sub-enterprises merged into one physical database, or a missing relationship that the designer forgot to model.

##### Part (b): The Graph has a Cycle

A cycle occurs when there is a closed path of alternating entities and relationships:

$$
E_1 - R_1 - E_2 - R_2 - \dots - E_k - R_k - E_1
$$

where no entity set is repeated except the start and end nodes.

```text
       [DEPARTMENT]
       /          \
 <Employs>      <Offers>
     /              \
[INSTRUCTOR]      [COURSE]
     \              /
     <Teaches_Course>
```

**Meaning for Enterprise Structure:**
- **Alternative Semantic Paths:** Entities can be reached through multiple distinct logical routes. For example, an instructor belongs to a department that offers a course, and the instructor also directly teaches that course.
- **Integrity Constraint Requirements:** Cycles create the possibility of semantic inconsistency. If `Instructor_A` works for `Department_ECE`, but teaches `Course_CSE101` offered by `Department_CSE`, is that allowed? The designer must specify whether the cycle enforces an identity constraint (the instructor must teach only courses offered by their own department) or allows cross-department assignments.
- **Redundancy Evaluation:** In some cases, one edge of the cycle is functionally redundant and can be derived from the others. In other cases, each relationship models a distinct business rule that must be preserved.

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions on E-R foundations (such as 2021 Q.5a) test whether students understand how visual diagrams translate into relational constraints.
- When explaining cycles, always give a concrete university or hospital example. Show how a cycle can either represent healthy multi-path navigation or dangerous business inconsistency.

---

### Exercise 6.6 · Ternary Relationship Decomposition into Binary Relationships

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.6
> - **Subtopic:** T02.1 (Entity sets, relationship sets, types of relationships)
> - **Classification:** Mathematical & Structural Analysis / Decomposition Theory
> - **Related RUET Questions:** 2018 Q.2(c) (Ternary exam marks relationship)

**Question (Silberschatz 7e Exercise 6.6).**

Consider the representation of the ternary relationship of Figure 6.29a using the binary relationships illustrated in Figure 6.29b (attributes not shown).

a. Show a simple instance of $E$, $A$, $B$, $C$, $R_A$, $R_B$, and $R_C$ that cannot correspond to any instance of $A$, $B$, $C$, and $R$.

b. Modify the E-R diagram of Figure 6.29b to introduce constraints that will guarantee that any instance of $E$, $A$, $B$, $C$, $R_A$, $R_B$, and $R_C$ that satisfies the constraints will correspond to an instance of $A$, $B$, $C$, and $R$.

c. Modify the preceding translation to handle total participation constraints on the ternary relationship.

#### 1. Core Principles & Concept Overview

A ternary relationship set $R \subseteq A \times B \times C$ models simultaneous three-way associations. Silberschatz Section 6.9.4 shows that any non-binary relationship can be converted into an artificial entity set $E$ connected to $A$, $B$, and $C$ by three binary relationships $R_A$, $R_B$, and $R_C$.

```text
Original Ternary (6.29a):           Decomposed Binary (6.29b):
      [A]     [B]                         [A]     [B]
        \     /                             \     /
         < R >                            <RA>   <RB>
           |                                \     /
          [C]                                 [E]
                                               |
                                             <RC>
                                               |
                                              [C]
```

However, unconstrained binary relationships are weaker than the original ternary relationship. They permit orphan links, partial tuples, and duplicate triples.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Counterexample Instance

In the unconstrained binary representation, an entity $e \in E$ can connect to entities in $A$ and $B$ without connecting to any entity in $C$. Or $e$ can connect to multiple entities in $A$.

Consider this concrete instance:
- Entity sets:
  $$
  A = \{a_1\}, \quad B = \{b_1\}, \quad C = \{c_1\}
  $$
- Artificial entity set:
  $$
  E = \{e_1\}
  $$
- Binary relationship instances:
  $$
  R_A = \{(e_1, a_1)\}, \quad R_B = \{(e_1, b_1)\}, \quad R_C = \emptyset
  $$

**Why it fails to correspond to any ternary instance:**
- The entity $e_1$ associates $a_1$ and $b_1$, but has no associated entity in $C$.
- In the original ternary model, every relationship instance is a complete 3-tuple $(a, b, c) \in R$. An incomplete association like $(a_1, b_1, \text{null})$ cannot exist in $R$ unless null values are explicitly permitted.
- Therefore, this instance of $E, R_A, R_B, R_C$ cannot map to any valid instance of $R$.

##### Part (b): Structural Constraints for Exact Correspondence

To guarantee that every legal instance of the binary structure maps to a valid instance of ternary relationship $R$, three constraints must be enforced:

1. **Total Participation of $E$ in Each Binary Relationship:**
   - Every entity $e \in E$ must participate in at least one relationship in $R_A$, at least one in $R_B$, and at least one in $R_C$.
   - Depicted by **double lines** connecting $E$ to $R_A$, $R_B$, and $R_C$.
2. **Many-to-One Cardinality from $E$ to Each Participating Entity Set:**
   - Each $e \in E$ must be associated with *at most one* entity in $A$, at most one in $B$, and at most one in $C$.
   - Depicted by drawing **directed arrows** from $R_A$ to $A$, from $R_B$ to $B$, and from $R_C$ to $C$ (or writing cardinality $1..1$ on the entity edges).
   - *Result of Constraints 1 and 2:* Every $e \in E$ maps to exactly one triple $(a, b, c)$.
3. **Uniqueness Constraint on the Triplet:**
   - No two distinct entities $e_1, e_2 \in E$ may associate with the exact same combination of entities $(a, b, c)$.
   - In relational terms, the candidate key for $E$ must be the composite key:
     $$
     \text{Candidate Key}(E) = (\text{PK}_A, \text{PK}_B, \text{PK}_C)
     $$
   - This prevents duplicate identical relationships in $R$.

##### Part (c): Handling Total Participation of the Original Ternary Relationship

Suppose the original ternary relationship $R$ has a total participation constraint on entity set $A$. This means every entity $a \in A$ must appear in at least one triple $(a, b, c) \in R$.

**Modification to the Translation:**
- Enforce **total participation of $A$ in binary relationship $R_A$**.
- In the E-R diagram, draw a **double line** connecting entity set $A$ to relationship diamond $R_A$.
- In terms of relational constraints, this requires that every primary key value in table $A$ must exist as a foreign key value in the table implementing $R_A$ (or table $E$).

#### 3. RUET Exam Insights & Examiner Notes

- This exercise provides the mathematical proof behind relationship reduction.
- RUET 2018 Q.2(c) asked students to model student exam marks as a ternary relationship and then convert it into relational tables. Showing total participation and composite foreign keys gives full marks.

---

## T02.2 · Attribute types

### Exercise 6.3 · Sports Team Scoring Statistics & Derived Attributes

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.3
> - **Subtopic:** T02.2 (Attribute types)
> - **Classification:** Schema Design / Attribute Modeling & Computation Rules
> - **Related RUET Questions:** 2020 Q.5(a) (Attribute types), 2021 Q.3(b) (Derived attributes)

**Question (Silberschatz 7e Exercise 6.3).**

Design an E-R diagram for keeping track of the scoring statistics of your favorite sports team. You should store the matches played, the scores in each match, the players in each match, and individual player scoring statistics for each match. Summary statistics should be modeled as derived attributes with an explanation as to how they are computed.

#### 1. Core Principles & Concept Overview

In E-R modeling, attributes are categorized by structural complexity and storage behavior:
- **Stored Attributes:** Base values stored physically in database storage (for example, `date_of_birth`, goals scored in a specific match).
- **Derived Attributes:** Values not stored directly. They are computed dynamically from stored attributes or related records using mathematical or aggregate expressions. In Chen notation, derived attributes are enclosed in a **dashed ellipse**.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Entity Sets and Base Attributes

1. **`TEAM` Entity Set:**
   - `team_id` (Primary Key, underlined solid).
   - `team_name` (Simple, atomic).
   - `coach_name` (Simple).
   - `total_matches_played` (Derived attribute, dashed ellipse).
   - `total_wins` (Derived attribute, dashed ellipse).

2. **`PLAYER` Entity Set:**
   - `player_id` (Primary Key, underlined solid).
   - `player_name` (Composite: `first_name`, `last_name`).
   - `jersey_number` (Simple).
   - `position` (Simple: Forward, Midfielder, Defender, Goalkeeper).
   - `career_goals` (Derived attribute, dashed ellipse).
   - `career_matches` (Derived attribute, dashed ellipse).
   - `scoring_average` (Derived attribute, dashed ellipse).

3. **`MATCH` Entity Set:**
   - `match_id` (Primary Key, underlined solid).
   - `match_date` (Simple).
   - `opponent_name` (Simple).
   - `venue` (Simple: Home / Away).
   - `team_final_score` (Derived attribute, dashed ellipse).
   - `opponent_final_score` (Stored attribute).
   - `match_result` (Derived attribute: Win, Loss, Draw).

##### Step 2: Relationship Sets and Descriptive Attributes

1. **`Plays_In` Relationship Set (between `PLAYER` and `MATCH`):**
   - Cardinality: **Many-to-Many (M:N)**. Many players participate in a match, and a player participates in many matches.
   - Descriptive Attributes (Match-specific player performance):
     - `minutes_played` (Simple integer).
     - `goals_scored` (Simple integer).
     - `assists` (Simple integer).
     - `yellow_cards`, `red_cards` (Simple integers).

2. **`Competes_In` Relationship Set (between `TEAM` and `MATCH`):**
   - Cardinality: **One-to-Many (1:N)**. The team plays many matches. Each match record tracks this specific team.

##### Step 3: Formal Computation Rules for Derived Attributes

```text
+-----------------------+-------------------------------------------------------------+
| Derived Attribute     | Computation Specification / Aggregate Expression            |
+-----------------------+-------------------------------------------------------------+
| PLAYER.career_goals   | SUM(Plays_In.goals_scored) for all matches of player_id     |
| PLAYER.career_matches | COUNT(Plays_In.match_id) for player_id                      |
| PLAYER.scoring_average| PLAYER.career_goals / PLAYER.career_matches                 |
| MATCH.team_final_score| SUM(Plays_In.goals_scored) for all players in match_id      |
| MATCH.match_result    | IF(team_final_score > opponent_final_score, 'Win',          |
|                       |    IF(team_final_score < opponent_final_score, 'Loss', 'Draw'))|
| TEAM.total_wins       | COUNT(matches where MATCH.match_result = 'Win')             |
+-----------------------+-------------------------------------------------------------+
```

##### Step 4: Textual E-R Diagram Structure

```text
  [ PLAYER ] =================== < Plays_In > =================== [ MATCH ]
  - player_id (PK)               - minutes_played                 - match_id (PK)
  - name (first, last)           - goals_scored                   - match_date
  - jersey_number                - assists                        - opponent_name
  - position                     - yellow_cards                   - opponent_score
  - (career_goals)*                                               - (team_final_score)*
  - (career_matches)*                                             - (match_result)*
  - (scoring_average)*
                                                                      ||
                                                                      || (1:N)
                                                                 < Competes_In >
                                                                      ||
                                                                  [ TEAM ]
                                                                  - team_id (PK)
                                                                  - team_name
                                                                  - (total_wins)*

  Note: Attributes in parentheses with asterisk (*...) are derived attributes.
```

#### 3. RUET Exam Insights & Examiner Notes

- RUET 2021 Q.3(b) asked to explain multi-valued, derived, and composite attributes for 4 marks.
- When an exam question asks for derived attributes, write the exact mathematical formula or SQL aggregate function (`SUM`, `COUNT`, `AVG`). Do not merely say "it is calculated from matches". Examiners award full marks for concrete computation rules.

---

### Exercise 6.18 · Common Attributes Across Entity Sets and Design Fixes

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Exercise 6.18
> - **Subtopic:** T02.2 (Attribute types)
> - **Classification:** Conceptual Schema Refactoring & Normalization
> - **Related RUET Questions:** 2018 Q.2(a) (Keys and attribute properties), 2020 Q.5(a)

**Question (Silberschatz 7e Exercise 6.18).**

Consider two entity sets $A$ and $B$ that both have the attribute $X$ (among others whose names are not relevant to this question).

a. If the two $X$s are completely unrelated, how should the design be improved?

b. If the two $X$s represent the same property and it is one that applies both to $A$ and to $B$, how should the design be improved? Consider three subcases:
- $X$ is the primary key for $A$ but not $B$
- $X$ is the primary key for both $A$ and $B$
- $X$ is not the primary key for $A$ nor for $B$

#### 1. Core Principles & Concept Overview

In high-quality database design, attribute names must reflect clear domain semantics. Duplicate attribute names across entity sets either indicate homonyms (unrelated things having the same name) or unmodeled relationships and shared superclasses.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Two $X$s are Completely Unrelated

If attribute $X$ in entity set $A$ has an entirely different real-world meaning from attribute $X$ in entity set $B$, keeping the same name causes schema ambiguity.

**Design Improvement:**
- Rename both attributes using qualifying semantic prefixes or context-specific terms.
- *Concrete Example:* Suppose $A$ is `STUDENT` and $B$ is `COURSE`. If both have attribute $X = \text{name}$, rename:
  - In `STUDENT`: rename $X$ to `student_name` (or `first_name`, `last_name`).
  - In `COURSE`: rename $X$ to `course_title`.
- This eliminates confusion in SQL queries and prevents accidental joins on unrelated columns.

##### Part (b): Two $X$s Represent the Same Property

###### Subcase 1: $X$ is the Primary Key for $A$ but Not $B$

- **Diagnosis:** $X$ identifies entities in $A$. Its presence inside $B$ is not an intrinsic property of $B$. It is an embedded foreign key attempting to represent a relationship.
- **Design Improvement:**
  1. Remove attribute $X$ from entity set $B$.
  2. Model an explicit **relationship set $R$** between entity set $A$ and entity set $B$.
  3. The cardinality is typically **many-to-one (N:1)** from $B$ to $A$ (many entities in $B$ associate with one entity in $A$).
  4. *Concrete Example:* Entity `DEPARTMENT` has primary key `dept_name`. Entity `INSTRUCTOR` has attribute `dept_name`. Do not place `dept_name` as a raw attribute of `INSTRUCTOR` in the E-R diagram. Instead, draw a relationship diamond `Member_Of` connecting `INSTRUCTOR` to `DEPARTMENT`.

###### Subcase 2: $X$ is the Primary Key for Both $A$ and $B$

- **Diagnosis:** $A$ and $B$ share the exact same identifying attribute. This implies they describe either the same underlying object in different roles, or a specialization hierarchy.
- **Design Improvement:**
  1. **Generalization / Specialization Hierarchy:** If $A$ and $B$ are distinct subtypes of a common entity, create a higher-level superclass entity set $C$ with primary key $X$. Let $A$ and $B$ inherit $X$ via an **ISA** relationship.
  2. **One-to-One (1:1) Relationship:** If $A$ and $B$ represent distinct concepts that are strictly paired, establish a 1:1 relationship between $A$ and $B$.
  3. **Entity Merge:** If $A$ and $B$ represent the exact same enterprise object, merge them into a single unified entity set.
  4. *Concrete Example:* `EMPLOYEE` has primary key `emp_id`. `INSTRUCTOR` has primary key `emp_id`. Model `INSTRUCTOR` as a specialized entity inheriting from `EMPLOYEE` via `ISA`.

###### Subcase 3: $X$ is Not the Primary Key for Either $A$ or $B$

- **Diagnosis:** Both entities share a common descriptive characteristic (for example, both `STUDENT` and `INSTRUCTOR` share attribute `address` or `phone_number`).
- **Design Improvement:**
  1. **Higher-Level Generalized Entity Set:** If $A$ and $B$ are similar kinds of entities, create a superclass entity set (for example, `PERSON` with attribute $X$). Make $A$ and $B$ inherit from `PERSON` via `ISA`.
  2. **Independent Entity Set:** If $X$ represents an independent enterprise object with its own life cycle (for example, `address` with city, state, zip code), convert $X$ into its own entity set. Relate both $A$ and $B$ to entity set $X$ through binary relationships.

#### 3. RUET Exam Insights & Examiner Notes

- This question is a classic test of conceptual modeling discipline.
- Students frequently make the mistake of putting foreign key attributes inside entity rectangles on E-R diagrams. Emphasize Subcase 1: foreign keys belong in relationship diamonds, never as attributes of the dependent entity set in an E-R diagram.

---

## T02.3 · Mapping cardinality and participation constraints

### Exercise 6.9 · Enforcing One-to-One Mapping on the Advisor Relationship

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.9
> - **Subtopic:** T02.3 (Mapping cardinality and participation constraints)
> - **Classification:** Schema Reduction & Relational Constraint Enforcement
> - **Related RUET Questions:** 2018 Q.3(c) (Mapping cardinality), 2020 Q.1(c) (Types of cardinalities)

**Question (Silberschatz 7e Exercise 6.9).**

Suppose the *advisor* relationship set were one-to-one. What extra constraints are required on the relation *advisor* to ensure that the one-to-one cardinality constraint is enforced?

#### 1. Core Principles & Concept Overview

In the standard university schema, the `advisor` relationship is **many-to-one (N:1)** from `student` to `instructor`:
- A student has at most one advisor.
- An instructor can advise multiple students.
- In the relation `advisor(s_id, i_id)`, the attribute `s_id` is the primary key.

If the business rule changes such that `advisor` becomes **one-to-one (1:1)**:
- A student has at most one advisor.
- An instructor can advise at most one student.

```text
Standard (N:1):                           Modified (1:1):
[STUDENT] ----- <Advisor> ----> [INSTRUCTOR]    [STUDENT] <--- <Advisor> ---> [INSTRUCTOR]
  PK: s_id                                        PK: s_id, UNIQUE: i_id
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Baseline Relational Schema

For the default many-to-one relationship, the relational table is:

$$
\text{advisor}(\underline{\text{s\_id}}, \text{i\_id})
$$

where:
- `s_id` is the primary key. This ensures each student appears at most once in the table.
- `s_id` references `student(ID)`.
- `i_id` references `instructor(ID)`.

##### Step 2: The Failure Under 1:1 Mapping

Under the baseline schema, the following instance is legal:

```text
+--------+--------+
|  s_id  |  i_id  |
+--------+--------+
| 10001  | 22222  |
| 10002  | 22222  |  <-- Instructor 22222 advises TWO students!
+--------+--------+
```

Because `i_id` is not constrained to be unique, an instructor can appear multiple times. This violates the 1:1 cardinality requirement.

##### Step 3: Required Extra Constraint

To guarantee that an instructor advises at most one student, the attribute `i_id` must be declared **`UNIQUE`**.

**Complete SQL DDL Specification:**

```sql
CREATE TABLE advisor (
    s_id   VARCHAR(5),
    i_id   VARCHAR(5),
    PRIMARY KEY (s_id),
    UNIQUE (i_id),
    FOREIGN KEY (s_id) REFERENCES student (ID) ON DELETE CASCADE,
    FOREIGN KEY (i_id) REFERENCES instructor (ID) ON DELETE SET NULL
);
```

**Alternative Valid Design:**
- Make `i_id` the primary key, and declare `s_id UNIQUE`.
- Either choice guarantees that each `s_id` appears at most once and each `i_id` appears at most once.

##### Step 4: Participation Considerations

- If participation of `instructor` in `advisor` is **total** (every instructor must advise a student), a relational table cannot enforce this by simple column constraints alone without a circular foreign key or SQL assertions.
- If participation is **partial**, the `UNIQUE (i_id)` constraint correctly allows instructors with zero advisees while prohibiting instructors with two or more.

#### 3. RUET Exam Insights & Examiner Notes

- RUET examiners often test how conceptual constraints map to SQL keywords.
- When answering this question, explicitly write the SQL table declaration showing `PRIMARY KEY (s_id)` paired with `UNIQUE (i_id)`. Mention that `UNIQUE` allows `NULL` values if participation is partial.

---

### Exercise 6.10 · Enforcing Total Participation via NOT NULL in Combined Schemas

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.10
> - **Subtopic:** T02.3 (Mapping cardinality and participation constraints)
> - **Classification:** Relational Reduction / SQL Constraint Mapping
> - **Related RUET Questions:** 2018 Q.1(c) (Participation constraints), 2021 Q.1(c) (Referential integrity)

**Question (Silberschatz 7e Exercise 6.10).**

Consider a many-to-one relationship $R$ between entity sets $A$ and $B$. Suppose the relation created from $R$ is combined with the relation created from $A$. In SQL, attributes participating in a foreign key constraint can be null. Explain how a constraint on total participation of $A$ in $R$ can be enforced using **not null** constraints in SQL.

#### 1. Core Principles & Concept Overview

When converting an E-R model into relational schemas:
- A many-to-one relationship $R$ from entity set $A$ to entity set $B$ can either be stored as a separate table $R(\underline{\text{PK}_A}, \text{PK}_B)$ or merged directly into the table representing entity set $A$.
- Merging eliminates a table and reduces query join overhead. The merged table schema is:

$$
\text{Relation } A(\underline{\text{PK}_A}, A_1, A_2, \dots, \text{FK}_B)
$$

where $\text{FK}_B$ is a foreign key referencing the primary key of table $B$.

#### 2. Detailed Step-by-Step Solution

##### Step 1: The Problem of Default Foreign Keys in SQL

In SQL standards, foreign key columns permit `NULL` values by default unless constrained otherwise:

```sql
CREATE TABLE A (
    a_id   INT PRIMARY KEY,
    b_id   INT,
    FOREIGN KEY (b_id) REFERENCES B (b_id)
);
```

If an entity $a_1 \in A$ has no associated entity in $B$, SQL sets `b_id = NULL`. This satisfies standard referential integrity because SQL considers a null foreign key valid.

However, if entity set $A$ has **total participation** in relationship $R$, every entity in $A$ *must* be related to at least one entity in $B$. A null value violates total participation.

```text
Entity Set A (Total Participation)        Entity Set B
[ a1 ] ====================> [ b1 ]
[ a2 ] ====================> [ b2 ]
[ a3 ] --------------------> NULL  (ILLEGAL under total participation!)
```

##### Step 2: Enforcement Using `NOT NULL`

To guarantee total participation of $A$ in $R$, declare the foreign key attribute $\text{FK}_B$ as **`NOT NULL`**.

```sql
CREATE TABLE A (
    a_id   INT PRIMARY KEY,
    name   VARCHAR(50),
    b_id   INT NOT NULL,   -- Guarantees total participation in relationship R
    FOREIGN KEY (b_id) REFERENCES B (b_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

##### Step 3: Formal Verification of the Constraint

1. **Existence:** Because `b_id` is declared `NOT NULL`, no tuple in $A$ can be inserted without supplying a non-null `b_id` value.
2. **Referential Validity:** Because `b_id` is a foreign key referencing $B(b_id)$, the value supplied must match an existing primary key value in table $B$.
3. **Conclusion:** Every entity instance in table $A$ is strictly bound to at least one (and because $R$ is many-to-one, exactly one) valid entity in table $B$. Thus, total participation of $A$ in $R$ is completely enforced.

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions on participation (such as 2018 Q.1c) ask students to show single vs double lines.
- In relational schema conversion questions, explain that a double line on the "many" side translates directly to a `NOT NULL` foreign key in the combined table.

---

## T02.4 · Weak vs strong entity sets

### Exercise 6.7 · Redundancy from Converting Weak Entities to Strong Entities

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.7
> - **Subtopic:** T02.4 (Weak vs strong entity sets)
> - **Classification:** Normalization & Redundancy Analysis
> - **Related RUET Questions:** 2018 Q.1(b), 2019 Q.1(b), 2020 Q.2(c), 2021 Q.8(c)

**Question (Silberschatz 7e Exercise 6.7).**

A weak entity set can always be made into a strong entity set by adding to its attributes the primary-key attributes of its identifying entity set. Outline what sort of redundancy will result if we do so.

#### 1. Core Principles & Concept Overview

A weak entity set lacks sufficient attributes to form a primary key of its own. It depends on an identifying strong entity set. For example:
- Identifying Entity: `course` with primary key `course_id`.
- Weak Entity: `section` with discriminator `sec_id, semester, year`.

If we artificially promote `section` to a strong entity set by directly incorporating `course_id` as a native attribute of `section`, several structural redundancies arise.

#### 2. Detailed Step-by-Step Solution

##### Step 1: The Transformation Mechanism

- **Original Weak Design:**
  - Entity `course`: `course_id`, `title`, `credits`.
  - Weak Entity `section`: `sec_id`, `semester`, `year`.
  - Identifying Relationship `sec_course`: Connects `section` to `course`.
- **Artificially Promoted Strong Design:**
  - Entity `section_strong`: `course_id`, `sec_id`, `semester`, `year`.
  - Primary Key: `(course_id, sec_id, semester, year)`.
  - Relationship `sec_course`: Still required to model the logical association between `course` and `section_strong`.

```text
Weak Entity Model:                     Artificially Strong Model:
[COURSE] <=== <sec_course> === [[SECTION]]    [COURSE] <--- <sec_course> ---> [SECTION_STRONG]
(course_id)                    (sec_id)       (course_id)                     (course_id, sec_id)
```

##### Step 2: Resulting Redundancies

1. **Redundancy in Relationship Representation:**
   - If the relationship `sec_course` is converted into a relational table, its schema is:
     $$
     \text{sec\_course}(\underline{\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year}})
     $$
   - Notice that every attribute in table `sec_course` is already present in table `section_strong`. The relationship table is completely redundant and duplicates data already stored.
2. **Duplication of Foreign Keys Across Descendant Relationships:**
   - If other entity sets relate to `section` (for example, `takes` linking `student` to `section`), foreign keys must include the full primary key `(course_id, sec_id, semester, year)`.
   - If `course_id` was already tracked through independent course relationships, the course identifier is stored redundantly across multiple tables.
3. **Update and Consistency Maintenance Overhead:**
   - If a course identifier is updated, changes must be propagated not only across the relationship paths but also across all converted strong entity tables that duplicate `course_id`.
4. **Loss of Conceptual Existence Dependency:**
   - In conceptual modeling, treating `section` as strong hides the fundamental business rule that a section cannot exist without a parent course.

#### 3. RUET Exam Insights & Examiner Notes

- This exercise demonstrates why weak entities are an essential modeling construct rather than a design inconvenience.
- Mention that converting weak entities to strong entities creates duplicate storage and violates third normal form (3NF) if relationship tables are retained.

---

### Exercise 6.17 · Distinction Between Weak and Strong Entity Sets

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Exercise 6.17
> - **Subtopic:** T02.4 (Weak vs strong entity sets)
> - **Classification:** Core Theory / High-Frequency Exam Question
> - **Past Exam Recycled:** ⚠️ **Direct Hit**:
>   - **2020 Q.2(c)** [3 Marks]: *"Explain the difference between a weak and a strong entity set with appropriate example."*
>   - **2021 Q.8(c)** [3 Marks]: *"Explain weak and strong entity set with appropriate example."*
>   - Closely related: **2018 Q.1(b)** [4 Marks], **2019 Q.1(b)** [3 Marks].

**Question (Silberschatz 7e Exercise 6.17).**

Explain the difference between a weak and a strong entity set.

#### 1. Core Principles & Concept Overview

In relational database design:
- A **strong entity set** possesses sufficient attributes to uniquely identify every entity instance among its members without reference to any external entity.
- A **weak entity set** does not contain enough attributes to form a standalone primary key. Its existence is dependent on an identifying (owner) entity set.

#### 2. Detailed Step-by-Step Solution

##### Step 1: Comprehensive Comparison Matrix

| Comparison Dimension | Strong Entity Set | Weak Entity Set |
| :--- | :--- | :--- |
| **Primary Key** | Has a complete primary key of its own. | Has no standalone primary key. It has only a **partial key (discriminator)**. |
| **Primary Key Formation** | Formed solely from its own native attributes. | Formed by combining the primary key of the identifying entity set with its own discriminator. |
| **Existence Dependency** | Independent. It exists in the enterprise on its own. | Existence-dependent on its identifying strong entity set. |
| **Participation** | Participation in relationships is typically partial. | Participation in the identifying relationship is **always total**. |
| **E-R Diagram Notation** | Drawn as a **single rectangle**. | Drawn as a **double rectangle**. |
| **Relationship Notation** | Connected via a **single diamond**. | Connected via a **double diamond** (identifying relationship). |
| **Discriminator Notation** | Primary key attributes are underlined with a **solid line**. | Discriminator attributes are underlined with a **dashed line**. |
| **Relational Deletion Rule**| Deletion does not inherently cascade unless explicitly requested. | Identifying foreign key must be declared with **`ON DELETE CASCADE`**. |

##### Step 2: Mathematical Formulation of Primary Key

Let $S$ be a strong identifying entity set with primary key:

$$
\text{PK}(S) = \{K_1, K_2, \dots, K_m\}
$$

Let $W$ be a weak entity set dependent on $S$, with discriminator (partial key):

$$
\text{Discriminator}(W) = \{D_1, D_2, \dots, D_n\}
$$

The primary key of the weak entity set is mathematically defined as:

$$
\text{PK}(W) = \text{PK}(S) \cup \text{Discriminator}(W) = \{K_1, K_2, \dots, K_m, D_1, D_2, \dots, D_n\}
$$

##### Step 3: Canonical Examples

###### Example 1: University Schema (`course` and `section`)

```text
[ COURSE ] ===================== < sec_course > ===================== [[ SECTION ]]
- course_id (PK)                                                       - sec_id (discriminator)
- title                                                                - semester (discriminator)
- credits                                                              - year (discriminator)
                                                                       - building
                                                                       - room_number
```

- **Strong Entity Set:** `course` has primary key `course_id`. It exists independently of whether any sections are taught.
- **Weak Entity Set:** `section` has attributes `sec_id`, `semester`, `year`, `building`, `room_number`. A section number like `Section 01` is meaningless without knowing the course.
- **Combined Primary Key for `section`:**
  $$
  \text{PK}(\text{section}) = (\text{course\_id}, \text{sec\_id}, \text{semester}, \text{year})
  $$

###### Example 2: Enterprise Schema (`employee` and `dependent`)

- **Strong Entity Set:** `employee` with primary key `emp_id`.
- **Weak Entity Set:** `dependent` with discriminator `first_name`.
- A dependent child named "Amina" can only be distinguished in health insurance records by knowing her parent's `emp_id`.
- **Combined Primary Key for `dependent`:**
  $$
  \text{PK}(\text{dependent}) = (\text{emp\_id}, \text{first\_name})
  $$

##### Step 4: Relational Schema Translation in SQL

```sql
-- Strong Entity Table
CREATE TABLE course (
    course_id   VARCHAR(8) PRIMARY KEY,
    title       VARCHAR(50),
    credits     NUMERIC(2, 0)
);

-- Weak Entity Table (Includes Owner PK + Discriminator as Composite PK)
CREATE TABLE section (
    course_id   VARCHAR(8),
    sec_id      VARCHAR(8),
    semester    VARCHAR(6),
    year        NUMERIC(4, 0),
    building    VARCHAR(15),
    room_number VARCHAR(7),
    PRIMARY KEY (course_id, sec_id, semester, year),
    FOREIGN KEY (course_id) REFERENCES course (course_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

#### 3. RUET Exam Insights & Examiner Notes

- This question was recycled word-for-word in 2020 Q.2(c) and 2021 Q.8(c).
- To obtain full marks (3 or 4 marks):
  1. Provide the structured comparison table with at least 5 distinct rows.
  2. Write out the primary key mathematical formula: $\text{PK}(\text{Weak}) = \text{PK}(\text{Strong}) \cup \text{Discriminator}$.
  3. Include a clean sketch showing the double rectangle, double diamond, and dashed underline.
  4. Write the SQL DDL showing `ON DELETE CASCADE`.

---

### Exercise 6.19 · Rationale for Weak Entity Sets in Database Modeling

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Exercise 6.19
> - **Subtopic:** T02.4 (Weak vs strong entity sets)
> - **Classification:** Conceptual Design Justification
> - **Related RUET Questions:** 2018 Q.1(b), 2019 Q.1(b)

**Question (Silberschatz 7e Exercise 6.19).**

We can convert any weak entity set to a strong entity set by simply adding appropriate attributes. Why, then, do we have weak entity sets?

#### 1. Core Principles & Concept Overview

In pure mathematics, any weak entity set can be transformed into a strong entity set by copying the owner's primary key attributes into the entity set or assigning a global surrogate key (such as an auto-incrementing integer or UUID). However, data modeling is not merely about unique rows. It is about capturing real-world semantics, constraints, and lifecycle dependencies faithfully.

#### 2. Detailed Step-by-Step Solution

Database designers retain weak entity sets for four fundamental reasons:

##### 1. Semantic Realism & Lifecycle Dependency Modeling

A weak entity set explicitly models **existence dependency**.
- In the real world, a course section does not exist on its own. If RUET cancels `ECE 2215`, all sections (`Section A`, `Section B`) immediately cease to exist.
- Modeling `section` as a weak entity set informs human developers and database management systems that the lifecycle of a section is strictly bound to its parent course.
- Promoting it to an independent strong entity conceals this core business dependency.

##### 2. Local Namespace vs. Global Key Overhead

Weak entity sets permit **local identifiers (discriminators)**.
- In a university with 500 courses, every course can have a `Section 01` and a `Section 02`. The section identifier only needs to be unique *within that specific course*.
- If every section had to be a strong entity without referencing the course key, the university would have to invent an artificial global identifier (for example, `sec_uid_98741`).
- Local discriminators simplify data entry for users. It is much easier for a registrar to enter "Course ECE 2215, Section 1" than to look up a globally unique surrogate section number.

##### 3. Automated Integrity Enforcement (`ON DELETE CASCADE`)

In relational systems, identifying relationships map directly to cascade rules:
- Because the weak entity is existence-dependent, the relational engine automatically enforces:
  ```sql
  FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE CASCADE
  ```
- If sections were independent strong entities, deleting a course would leave orphan sections unless complex custom triggers or external application logic were written.

##### 4. Eliminating Redundant Relationship Storage

In schema reduction:
- A relationship between two independent strong entity sets requires its own table or explicit link columns.
- For a weak entity set, the identifying relationship is automatically absorbed into the weak entity relation itself without requiring a separate table.
- This prevents table bloat and improves query join performance.

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions on weak entity handling (such as 2019 Q.1b: *"How is a weak entity set handled in DBMS?"*) evaluate whether students understand the trade-off between surrogate keys and composite weak keys.
- Frame your answer around semantic integrity, cascade deletion, and local discriminator namespaces.

---

## T02.5 · Design a full E-R diagram for a scenario (Part A · Intro Scenarios & Temporal Extensions)

### Exercise 6.1 · Car Insurance Enterprise E-R Modeling Scenario

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.1
> - **Subtopic:** T02.5 (Design a full E-R diagram for a scenario)
> - **Classification:** Enterprise Schema Design & Cardinality Modeling
> - **Related RUET Questions:** 2017 Q.1(b), 2019 Q.1(c), 2023 Q.1(a), 2024 Q.1(b)

**Question (Silberschatz 7e Exercise 6.1).**

Construct an E-R diagram for a car insurance company whose customers own one or more cars each. Each car has associated with it zero to any number of recorded accidents. Each insurance policy covers one or more cars and has one or more premium payments associated with it. Each payment is for a particular period of time, and has an associated due date, and the date when the payment was received.

#### 1. Core Principles & Concept Overview

Designing an enterprise E-R diagram requires extracting:
1. **Entity Sets:** Real-world objects with independent or dependent existence.
2. **Attributes:** Identifying primary keys and descriptive properties.
3. **Relationship Sets:** Associations among entities with exact mapping cardinalities (1:1, 1:N, M:N) and participation constraints (total vs partial).

#### 2. Detailed Step-by-Step Solution

##### Step 1: Enterprise Entity Identification & Attributes

1. **`CUSTOMER` Entity Set:**
   - `customer_id` (Primary Key, underlined).
   - `name` (Composite: `first_name`, `last_name`).
   - `address` (Composite: `street`, `city`, `post_code`).
   - `phone_number` (Simple).

2. **`CAR` Entity Set:**
   - `vin` (Vehicle Identification Number, Primary Key, underlined).
   - `license_plate` (Candidate Key).
   - `model` (Simple).
   - `year` (Simple integer).

3. **`ACCIDENT` Entity Set:**
   - `accident_id` (Primary Key, underlined).
   - `accident_date` (Simple).
   - `location` (Simple).
   - `police_report_no` (Simple).

4. **`POLICY` Entity Set:**
   - `policy_number` (Primary Key, underlined).
   - `policy_type` (Simple: Comprehensive, Third-party).
   - `start_date`, `end_date` (Simple dates).

5. **`PAYMENT` (Weak Entity Set dependent on `POLICY`):**
   - `payment_number` (Discriminator / Partial Key, dashed underline).
   - `due_date` (Simple date).
   - `payment_received_date` (Simple date; nullable if unpaid).
   - `period_start`, `period_end` (Coverage interval).
   - `amount` (Monetary value).

##### Step 2: Relationships and Mapping Cardinalities

1. **`Owns` (between `CUSTOMER` and `CAR`):**
   - Cardinality: **One-to-Many (1:N)** from `CUSTOMER` to `CAR`.
   - Participation:
     - `CUSTOMER`: Total participation (double line; prompt states "whose customers own one or more cars each").
     - `CAR`: Total participation (each car is owned by exactly one customer).

2. **`Involved_In` (between `CAR` and `ACCIDENT`):**
   - Cardinality: **Many-to-Many (M:N)**. A car can have zero to many recorded accidents. An accident can involve multiple cars.
   - Descriptive Attribute on Relationship: `damage_amount` (monetary estimate of damage for that specific car in that specific accident).

3. **`Covers` (between `POLICY` and `CAR`):**
   - Cardinality: **One-to-Many (1:N)** or **Many-to-Many (M:N)**. Prompt specifies: "Each insurance policy covers one or more cars". We model 1:N from `POLICY` to `CAR` (a policy covers one or more cars, and each car is covered under a policy). Total participation on `POLICY`.

4. **`Policy_Payment` (Identifying Relationship between `POLICY` and `PAYMENT`):**
   - Cardinality: **One-to-Many (1:N)**. A policy has one or more payments.
   - Notation: Double diamond. Total participation on weak entity `PAYMENT` (double line).

##### Step 3: Complete E-R Diagram Representation

```text
  [ CUSTOMER ]                                               [ ACCIDENT ]
  - customer_id (PK)                                         - accident_id (PK)
  - name                                                     - accident_date
  - address                                                  - location
      || (1)                                                     | (N)
      ||                                                         |
   < Owns >                                               < Involved_In >
      ||                                                  - damage_amount
      || (N)                                                     | (M)
    [ CAR ] =====================================================+
    - vin (PK)
    - license_plate
    - model
    - year
      || (N)
      ||
   < Covers >
      ||
      || (1)
   [ POLICY ] ================= < Policy_Payment > ================= [[ PAYMENT ]]
   - policy_number (PK)             (Double Diamond)                 - payment_num (disc.)
   - policy_type                                                     - due_date
   - start_date                                                      - received_date
   - end_date                                                        - period_start
                                                                     - period_end
                                                                     - amount
```

##### Step 4: Relational Database Schema Translation

```text
customer(customer_id, first_name, last_name, street, city, post_code, phone_number)
    PK: customer_id

car(vin, license_plate, model, year, customer_id, policy_number)
    PK: vin
    FK: customer_id references customer(customer_id)
    FK: policy_number references policy(policy_number)

accident(accident_id, accident_date, location, police_report_no)
    PK: accident_id

involved_in(vin, accident_id, damage_amount)
    PK: (vin, accident_id)
    FK: vin references car(vin)
    FK: accident_id references accident(accident_id)

policy(policy_number, policy_type, start_date, end_date)
    PK: policy_number

payment(policy_number, payment_num, due_date, received_date, period_start, period_end, amount)
    PK: (policy_number, payment_num)
    FK: policy_number references policy(policy_number) ON DELETE CASCADE
```

#### 3. RUET Exam Insights & Examiner Notes

- RUET scenario questions carry between 5 and 6 marks (such as 2017 Q.1b RUET Student DB, 2019 Q.1c Train E-ticketing, 2023 Q.1a Library).
- Examiners look for three exact details:
  1. Primary keys clearly underlined.
  2. Double lines showing total participation (for example, `customer` owning cars, `policy` covering cars).
  3. Descriptive attributes placed on relationship diamonds (for example, `damage_amount` on `Involved_In`).

---

### Exercise 6.2 · Student Exam Marks: Ternary vs Binary Design

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.2
> - **Subtopic:** T02.5 (Design a full E-R diagram for a scenario)
> - **Classification:** Multi-Way Relationship Modeling vs Binary Alternatives
> - **Past Exam Recycled:** ⚠️ **Direct Hit**:
>   - **2018 Q.2(c)** [4 Marks]: *"Consider a database used to record the marks that students get in different examinations of different course offerings. (i) Construct an E-R diagram that models examinations as entities, and uses a ternary relationship for the above database; (ii) Draw a relational data model for the above corresponding E-R diagram."*

**Question (Silberschatz 7e Exercise 6.2).**

Consider a database that includes the entity sets *student*, *course*, and *section* from the university schema and that additionally records the marks that students receive in different exams of different sections.

a. Construct an E-R diagram that models exams as entities and uses a ternary relationship as part of the design.

b. Construct an alternative E-R diagram that uses only a binary relationship between *student* and *section*. Make sure that only one relationship exists between a particular *student* and *section* pair, yet you can represent the marks that a student gets in different exams.

#### 1. Core Principles & Concept Overview

When modeling exam results:
- An examination is administered for a specific section of a course.
- Multiple students take the examination and receive individual marks.
- This interaction can either be modeled as a single **ternary relationship** linking `student`, `section`, and `exam`, or by aggregating/associating binary relationships.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Ternary Relationship Model (RUET 2018 Q.2c Verbatim)

###### Step 1: Entity Sets
1. `STUDENT`: `student_id` (PK), `name`, `dept_name`.
2. `SECTION`: `sec_id`, `semester`, `year` (along with identifying `course_id`).
3. `EXAM`: `exam_id` (PK), `exam_type` (Midterm, Final, Quiz), `max_marks`.

###### Step 2: Ternary Relationship Set
- Relationship: `Scores` (or `Exam_Result`).
- Degree: **3 (Ternary)**. Connects `STUDENT`, `SECTION`, and `EXAM`.
- Descriptive Attribute: `marks` (the numerical score obtained by a student in an exam of a section).

```text
       [ STUDENT ]           [ SECTION ]
            \                     /
             \                   /
              \                 /
               <     Scores    > --- ( marks )
                      /
                     /
                    /
                 [ EXAM ]
```

###### Step 3: Relational Schema Reduction (Part ii of RUET 2018 Q.2c)
```text
student(student_id, name, dept_name)
    PK: student_id

course(course_id, title, credits)
    PK: course_id

section(course_id, sec_id, semester, year)
    PK: (course_id, sec_id, semester, year)
    FK: course_id references course(course_id)

exam(exam_id, exam_type, max_marks)
    PK: exam_id

scores(student_id, course_id, sec_id, semester, year, exam_id, marks)
    PK: (student_id, course_id, sec_id, semester, year, exam_id)
    FK: student_id references student(student_id)
    FK: (course_id, sec_id, semester, year) references section(course_id, sec_id, semester, year)
    FK: exam_id references exam(exam_id)
```

##### Part (b): Binary Relationship Design (With Single Link Between Student & Section)

The problem imposes a strict constraint:
1. Only a **single binary relationship** may exist between a particular `student` and `section` pair (the standard `takes` relationship).
2. The model must still record the marks that a student receives across multiple exams in that section.

There are two standard textbook solutions:

###### Approach 1: E-R Aggregation (Preferred Architectural Solution)

Treat the binary relationship set `takes` (between `student` and `section`) as a higher-level aggregate entity.
1. `takes` associates `student` and `section`. A student is enrolled in a section exactly once.
2. We aggregate `takes` into a rectangular box `[ (STUDENT) <takes> (SECTION) ]`.
3. An entity set `EXAM` is related to `SECTION` via a binary relationship `Offered_For` (each section offers exams).
4. A binary relationship `Scores` connects `EXAM` to the aggregated entity `takes`. The attribute `marks` sits on `Scores`.

```text
  +---------------------------------------------+
  |                                             |
  |   [ STUDENT ] ----- < takes > ----- [ SECTION ]
  |                                             |
  +---------------------------------------------+
                        |
                        |
                    < Scores > --- ( marks )
                        |
                        |
                    [ EXAM ]
```

###### Approach 2: Associative Entity / Weak Entity Design

1. Treat `EXAM` as a weak entity set dependent on `SECTION` (an exam exists only within the context of a section).
   - Discriminator of `EXAM`: `exam_name` (Quiz 1, Midterm).
2. Between `STUDENT` and `SECTION`, there is only the binary relationship `takes`.
3. To store marks without violating the single-relationship rule, convert the enrollment into an entity set `REGISTRATION` (or `ENROLLMENT`).
   - `REGISTRATION` participates in a binary relationship with `STUDENT` (1:N) and `SECTION` (1:N).
   - A binary relationship `Has_Mark` connects `REGISTRATION` and `EXAM`, with descriptive attribute `marks`.

#### 3. RUET Exam Insights & Examiner Notes

- RUET 2018 Q.2(c) was taken directly from Part (a) of this exercise.
- In exam answers, explicitly define the composite primary key of the relational table `scores`. Examiners specifically look for the union of all three primary keys: `(student_id, course_id, sec_id, semester, year, exam_id)`.

---

### Exercise 6.4 · Dangers of Repeating Entity Sets with Attributes

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.4
> - **Subtopic:** T02.5 (Design a full E-R diagram for a scenario)
> - **Classification:** Design Methodology & Schema Anti-Patterns
> - **Related RUET Questions:** General E-R Modeling Questions

**Question (Silberschatz 7e Exercise 6.4).**

Consider an E-R diagram in which the same entity set appears several times, with its attributes repeated in more than one occurrence. Why is allowing this redundancy a bad practice that one should avoid?

#### 1. Core Principles & Concept Overview

In conceptual database design, an entity set represents a distinct collection of enterprise objects. Drawing multiple boxes for the same entity set and repeating its attribute list creates redundancy at the conceptual schema layer.

```text
Bad Practice (Redundant Replication):
[STUDENT: roll, name, dept] ----- <Takes> ----- [COURSE]
                                                  |
[STUDENT: roll, name, dept] ----- <Advises> ----+
```

#### 2. Detailed Step-by-Step Solution

Repeating an entity set with its attributes is considered an anti-pattern for four key reasons:

##### 1. Risk of Schema Inconsistency During Evolution
If an entity set is drawn in three different places across a large E-R diagram, a schema designer who updates an attribute (such as adding a `blood_group` attribute or modifying `phone_number` to multi-valued) may update it in one occurrence and forget the others. This introduces contradictory definitions within the same enterprise schema.

##### 2. Visual and Semantic Ambiguity
A reader or database administrator reviewing the diagram cannot tell whether the duplicate boxes represent:
- The exact same entity set participating in different roles.
- Two distinct entity sets that coincidentally share similar attributes (for example, undergraduate vs graduate students).
- A horizontal partition of the data.
This ambiguity impairs clear communication between business stakeholders and system developers.

##### 3. Automated CASE Tool Translation Failures
Modern database design tools (such as ERwin, Dia, or MySQL Workbench) parse E-R diagrams to automatically generate SQL DDL tables. If an entity set appears multiple times with distinct box instances, the code generator may create redundant duplicate tables (such as `student_1`, `student_2`), leading to denormalization and severe data anomalies.

##### 4. Violation of Proper Role Modeling
The E-R model provides an explicit, clean mechanism for entities participating in multiple relationships: **role indicators**.
- If an entity participates in multiple relationships (even recursive ones), draw a single entity set box and connect it via distinct relationship edges labeled with their respective roles (for example, `course_id` and `prereq_id` in a prerequisite relationship).

```text
Correct Design (Single Entity Set with Role Labels):
                     +----- < Takes > ----- [ COURSE ]
                     |                        |
[ STUDENT ] ---------+                        |
(roll, name, dept)   |                        |
                     +----- < Advises > ------+
```

#### 3. RUET Exam Insights & Examiner Notes

- When students draw E-R diagrams for complex RUET exam scenarios (such as the 2019 train ticketing or 2023 library systems), they often draw separate boxes for `STUDENT` or `USER` whenever a new relationship appears.
- Examiners penalize duplicate boxes. Always draw the entity box once and route lines to different relationship diamonds.

---

### Exercise 6.13 · Modeling Temporal Changes and Valid-Time Intervals

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Practice Exercise 6.13
> - **Subtopic:** T02.5 (Design a full E-R diagram for a scenario)
> - **Classification:** Advanced E-R Extensions / Temporal Database Design
> - **Related RUET Questions:** 2017 Q.1(b), 2024 Q.1(b) (Dynamic Result & Advisor Tracking)

**Question (Silberschatz 7e Exercise 6.13).**

An E-R diagram usually models the state of an enterprise at a point in time. Suppose we wish to track *temporal changes*, that is, changes to data over time. For example, Zhang may have been a student between September 2015 and May 2019, while Shankar may have had instructor Einstein as advisor from May 2018 to December 2018, and again from June 2019 to January 2020. Similarly, attribute values of an entity or relationship, such as *title* and *credits* of *course*, *salary*, or even *name* of *instructor*, and *tot_cred* of *student*, can change over time. One way to model temporal changes is as follows: We define a new data type called **valid time**, which is a time interval, or a set of time intervals. We then associate a *valid_time* attribute with each entity and relationship, recording the time periods during which the entity or relationship is valid. The end time of an interval can be infinity; for example, if Shankar became a student in September 2018, and is still a student, we can represent the end time of the *valid_time* interval as infinity for the Shankar entity. Similarly, we model attributes that can change over time as a set of values, each with its own *valid_time*.

a. Draw an E-R diagram with the *student* and *instructor* entities, and the *advisor* relationship, with the above extensions to track temporal changes.

b. Convert the E-R diagram discussed above into a set of relations.

#### 1. Core Principles & Concept Overview

Standard E-R diagrams model a **snapshot** of the real world at the current instant. In contrast, a **temporal database** retains historical states.
- **Valid Time:** The time period during which a fact is true in the real world. Modeled as an interval:
  $$
  I = [t_{\text{start}}, t_{\text{end}})
  $$
  where $t_{\text{end}} = \infty$ denotes a currently active fact.
- Adding temporal tracking transforms simple attributes into multivalued composite structures, and changes single-key relationships into time-indexed histories.

#### 2. Detailed Step-by-Step Solution

##### Part (a): Temporal E-R Diagram Construction

###### Step 1: Handling Temporal Entities
Both `student` and `instructor` exist over time. They receive an entity-level `valid_time` interval.
- Attributes whose values change over time (such as `tot_cred` for a student, or `salary` and `name` for an instructor) are modeled as **multivalued composite attributes**.
- Each component of the multivalued attribute consists of:
  $$
  \{\text{attribute\_value}, \text{valid\_time}\}
  $$

###### Step 2: Handling Temporal Relationships
The `advisor` relationship connects `student` and `instructor`. A student can have different advisors at different periods, or have the same advisor over disconnected intervals.
- The `advisor` relationship receives a descriptive attribute: `valid_time` ($[t_{\text{start}}, t_{\text{end}})$).

```text
[ STUDENT ] ===================== < advisor > ===================== [ INSTRUCTOR ]
- ID (PK)                         - [valid_time]                    - ID (PK)
- [valid_time]                      (start_time, end_time)          - [valid_time]
- { (name, valid_time) }                                            - { (name, valid_time) }
- { (tot_cred, valid_time) }                                        - { (salary, valid_time) }
- dept_name                                                         - dept_name
```

*Diagram Notation Notes:*
- Attributes enclosed in brackets `[...]` represent temporal intervals.
- Attributes enclosed in braces `{(...)}` represent multivalued composite attributes tracking historical values.

##### Part (b): Relational Schema Conversion

Converting temporal E-R constructs to relational tables requires flattening intervals and decomposing temporal attributes to satisfy First Normal Form (1NF).

###### Step 1: Base Entity Life-Span Relations
Track the valid existence periods of students and instructors:

$$
\text{student}(\underline{\text{ID}, \text{start\_time}}, \text{end\_time}, \text{dept\_name})
$$

$$
\text{instructor}(\underline{\text{ID}, \text{start\_time}}, \text{end\_time}, \text{dept\_name})
$$

*Primary Key Note:* `ID` alone cannot be the primary key because an entity can be active, deactivated, and reactivated over multiple intervals. The composite key is `(ID, start_time)`.

###### Step 2: Temporal Attribute Decomposition Relations
Because `name`, `tot_cred`, and `salary` change over time, they must be factored into separate temporal tables:

$$
\text{student\_tot\_cred}(\underline{\text{ID}, \text{start\_time}}, \text{end\_time}, \text{tot\_cred})
$$

$$
\text{instructor\_salary}(\underline{\text{ID}, \text{start\_time}}, \text{end\_time}, \text{salary})
$$

$$
\text{instructor\_name}(\underline{\text{ID}, \text{start\_time}}, \text{end\_time}, \text{name})
$$

###### Step 3: Temporal Relationship Relation
The `advisor` relationship schema must record multiple historical advising assignments for the same student:

$$
\text{advisor}(\underline{\text{s\_id}, \text{start\_time}}, \text{end\_time}, \text{i\_id})
$$

where:
- `s_id` references `student(ID)`.
- `i_id` references `instructor(ID)`.
- Primary Key is `(s_id, start_time)`: A student has at most one advisor at any given point in time, but may have different advisors across different start times.

###### Step 4: Complete SQL DDL Specification

```sql
-- Temporal Advisor Table
CREATE TABLE advisor_history (
    s_id        VARCHAR(5),
    i_id        VARCHAR(5) NOT NULL,
    start_time  DATE NOT NULL,
    end_time    DATE DEFAULT '9999-12-31', -- Represents infinity
    PRIMARY KEY (s_id, start_time),
    FOREIGN KEY (s_id) REFERENCES student (ID),
    FOREIGN KEY (i_id) REFERENCES instructor (ID),
    CHECK (start_time < end_time)
);
```

#### 3. RUET Exam Insights & Examiner Notes

- While standard RUET questions ask for static snapshot diagrams, semester final questions frequently include time-variant data (such as semester-wise results or changing advisors across sessions).
- Highlighting that `start_time` must become part of the composite primary key in temporal tables shows deep relational database maturity.

---

[← Prev: T01](T01_DB_Concepts_and_Architecture.md) | [Exam-style T02](../Topicwise_answers_exam_style/T02_ER_and_EER_Modeling.md) | [Next: T02 Part 2 →](T02_Part2_ER_Scenarios_Reduction_EER.md)
