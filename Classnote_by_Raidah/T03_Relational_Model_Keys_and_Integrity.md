# T03: Relational Model, Keys & Integrity — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 3 | `subtopicwise_list.md` T03 (28 marks · 4.4% · 5/7)  
**Source Pages:** Page 5 (Right), Page 7 (Left), Page 11 (Right), Page 12 (Right), Page 13 (Left), Page 19 (Right), Page 20 (Left)

---

## 1. Fundamentals of the Relational Model

<!-- Page 12 (Right) -->

* In the Relational Model, data are stored in tabular format (relations / tables).
* **Relation:** A mathematical relation / table made up of rows and columns.
* **Attribute (Column):** Named characteristics or properties of entities.
* **Tuple (Row):** A collection of attribute values representing an individual entity / record.
* **Atomic Attributes:** Every attribute value must be atomic (indivisible) — no multivalued or composite fields.
* **Tuple Ordering:** The order in which tuples appear in a relation is completely irrelevant.

---

## 2. Schemas vs. Instances

<!-- Page 7 (Left) & Page 11 (Right) -->

* **Schema:** Structural declaration / design of the relation (analogous to type/variable declaration in programming languages).
  * Structure rarely changes over time.
  * Formatted as: `Relation_Name(Attribute_1, Attribute_2, ..., Attribute_n)`.
* **Instance:** The actual data / content of the relation populated at a specific point in time (analogous to the variable's value).
  * *Values are variable (frequently change as tuples are inserted, deleted, or updated).*

### Bad Schema Design & Redundancy:

| instructor | dept | budget |
| :--- | :--- | :--- |
| A | ECE | 50k |
| B | EEE | 40k |
| C | ECE | 50k |
| D | CSE | 28k |
| E | EEE | 40k |
| F | ECE | 50k |

> [!CAUTION]
> Here department budget is repeatedly duplicated. If the ECE budget is modified, updating it in one row without updating all other rows causes data inconsistency $\rightarrow$ Bad schema design!

---

## 3. Comprehensive Key Hierarchy

<!-- Page 5 (Right), Page 7 (Left), Page 13 (Left), Page 19 (Right) -->

```text
                    +--------------------+
                    |     Superkey       |
                    +--------------------+
                              | (minimal subset)
                              v
                    +--------------------+
                    |   Candidate Key    |
                    +--------------------+
                       /              \
                      /                \
                     v                  v
           +------------------+    +-------------------+
           |   Primary Key    |    |   Alternate Key   |
           +------------------+    +-------------------+
```

### 1. Superkey:
* A set of one or more attributes that, taken collectively, allows us to identify uniquely a tuple in the relation $r(R)$.
* A combination / set of multiple attributes that uniquely identifies a tuple.

### 2. Candidate Key:
* A **minimal superkey**; a superkey for which no proper subset is itself a superkey.
* Removing any attribute from a Candidate Key loses the unique identification property (minimal / irreducible).

### 3. Primary Key:
* The candidate key chosen by the database designer as the principal means of uniquely identifying tuples in a relation.
* **Properties:** Unique and never `NULL`.
* *Once established, it should remain immutable, and subsequent records can be automatically sequenced/incremented (e.g., auto-incrementing from 32 to 33).*

### 4. Alternate Key:
* All candidate keys that were not chosen as the primary key.

### 5. Composite Key:
* A key that consists of two or more attributes together to uniquely identify a record (when no single attribute can uniquely identify it).

### 6. Foreign Key:
* An attribute (or set of attributes) in one relation that references the primary key of another relation.
* When establishing a relationship / connection between two tables, they are connected through a foreign key.
* Enforces **referential integrity**.

---

## 4. Prime vs. Non-Prime Attributes

<!-- Page 20 (Left) -->

* **Prime Attribute:** An attribute that is a member of at least one candidate key of the relation.
* **Non-prime Attribute:** An attribute that does not belong to any candidate key.

