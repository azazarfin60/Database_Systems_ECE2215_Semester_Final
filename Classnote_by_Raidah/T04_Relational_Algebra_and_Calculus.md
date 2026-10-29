# T04: Relational Algebra & Calculus — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 3 | `subtopicwise_list.md` T04 (48 marks · 7.5% · 6/7)  
**Source Pages:** Page 13 (Right), Page 14 (Left, Right)

---

## 1. Fundamentals of Relational Algebra

<!-- Page 13 (Right) -->
<!-- CLASS-04 | 11.07.2024 | NIS MAM -->

Relational Algebra is a procedural query language consisting of a set of operations that take one or two relations as input and produce a new relation as their result.
* Builds up logical relations and expressions.

### Basic Fundamental Operations:

1. **Select ($\sigma$):** Extracts tuples that satisfy a specified predicate/condition.
2. **Project ($\Pi$):** Extracts specified attributes (columns) from a relation, eliminating duplicates.
3. **Union ($\cup$):** Combines tuples from two union-compatible relations.
4. **Set Difference ($- $):** Finds tuples in the first relation that do not appear in the second.
5. **Cartesian Product ($\times$):** Combines every tuple of the first relation with every tuple of the second relation (cross product pairing every tuple of the first relation with every tuple of the second).
6. **Rename ($\rho$):** Gives a name to the results of relational algebra expressions or renames attributes.
7. **Intersection ($\cap$):** Finds tuples common to both relations (applied using inner join or expressed as $r - (r - s)$).

---

## 2. Selection, Projection & Composition

<!-- Page 13 (Right) -->

### Select Operation Examples:
* Select all students in the ECE department:
$$\sigma_{\text{dept\_name} = \text{"ECE"}}(\text{student\_info})$$

* Select all students in ECE taught by Instructor $X$:
$$\sigma_{\text{dept\_name} = \text{"ECE"} \wedge \text{Instructor} = X}(\text{student\_info})$$

### Project Operation Examples:
* Project ID, Name, and Department Name:
$$\Pi_{\text{ID}, \text{Name}, \text{dept\_name}}(\text{student\_info})$$

### Composition of Relational Operations:
* Find the ID and Name of all students in the Physics department:
$$\Pi_{\text{ID}, \text{Name}}(\sigma_{\text{dept\_name} = \text{"PHYSICS"}}(\text{student\_info}))$$

---

## 3. Cartesian Product, Joins & Renaming

<!-- Page 14 (Left) -->

### Cartesian Product ($\times$):

Given `Instructor`:
| Instructor_ID | Instructor_Name |
| :--- | :--- |
| 1001 | X |
| 1002 | Y |

$$\text{student\_info} \times \text{Instructor}$$

### Join Operations:
* **Theta Join ($\bowtie_\theta$ / Condition Join):**
  A selection performed over a Cartesian product:
$$\sigma_{\text{instructor.ID} = \text{teaches.ID}}(\text{instructor} \times \text{teaches})$$

* **Natural Join ($\bowtie$):**
  Matches tuples where attributes with common names have identical values:
$$\text{student\_info} \bowtie \text{takes}$$

### Rename Operation ($\rho$):
Allows referencing a relation by an alias and optionally renaming its attributes:
$$\rho_{x}(E)$$
$$\rho_{x(A_1, A_2, \dots, A_n)}(E)$$

Example:
$$\rho_{X}(\Pi_{\text{ID}, \text{name}, \text{address}}(\text{Instructor}))$$

---

## 4. Extended Relational Algebra: Aggregation ($\gamma$)

<!-- Page 14 (Right) -->
<!-- CLASS-05 | 13.07.2024 | NIS MAM -->

Aggregate functions take a collection of values and return a single value (represented by $\gamma$, $g$, or handwritten $8$):

* **Average salary of all instructors:**
$$\gamma_{\text{avg}(\text{salary})}(\text{instructor})$$

* **Count of courses offered in 2018:**
$$\gamma_{\text{count}(\text{course\_id})}(\sigma_{\text{year} = 2018}(\text{section}))$$

* **Grouping with Aggregation ($_{G}\gamma_{F}$):**
  Find the average salary for each department:
$$_{\text{dept\_name}}\gamma_{\text{avg}(\text{salary})}(\text{instructor})$$
  * *(First column shows the grouping attribute `dept_name`, second shows the computed aggregate `avg(salary)`)*

---

## 5. Equivalent Queries in Relational Algebra

<!-- Page 14 (Right) -->

Two relational algebra expressions are equivalent if they produce the same result relation on every legal database instance:

$$\sigma_{\text{dept\_name} = \text{"Physics"} \wedge \text{salary} > 90000}(\text{instructor})$$
is equivalent to cascading selections:
$$\sigma_{\text{dept\_name} = \text{"Physics"}}(\sigma_{\text{salary} > 90000}(\text{instructor}))$$

---

## 6. Pitfalls in Relational Database Design

<!-- Page 14 (Right) -->

* **Data redundancy:** Leads to wasted storage and repetitive, inconsistent records.
* **Poor normalization choices:** Reduces the capability to represent entity facts cleanly.
* **Indexing overhead:** Over-indexing slows down write operations.
* **Referential integrity violations:** Incomplete foreign key constraints cause dangling pointers.
* **Improper primary key selection:** Using non-unique or volatile attributes as primary keys.
* **Lacking data constraints:** Allowing illegal or invalid values in domain attributes.
* **Designing only for the present:** Failing to design for future database scalability.

