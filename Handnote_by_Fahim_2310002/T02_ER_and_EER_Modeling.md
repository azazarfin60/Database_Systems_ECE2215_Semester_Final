# T02: E-R / EER Modeling — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 2 | `subtopicwise_list.md` T02 (67 marks · 10.5% · 7/7)  
**Source Pages:** Page 20 (Bottom) – Page 30

---

<!-- Page 20 -->

## Introduction to E-R Model

### The E-R Model

- **E-R Model** = Entity Relationship Model
- Facilitates database design by allowing specification of an enterprise schema.
- Represents the overall logical structure of a database.
- It is a high level data base <!-- note: data model -->
- Develops a conceptual design for databases.
- Portrayed as diagrams.

---

<!-- Page 21 -->

## E-R Model: Basic Components

### Basic Components

- Entity sets
- Attributes
- Relationship sets

![Fig_p021_01: ER diagram illustrating basic components: Instructor entity set with attributes ID, Name, Salary, connected via Advices relationship set to Student entity set with attributes ID, Name, Credits](diagrams/p021_fig01.jpg)
*Figure 21.1 — Basic components of an E-R diagram: Entity sets (Instructor, Student), Relationship set (Advices), and Attributes (Page 21)*

### Entity

- An entity is a thing or object in the real world.
- Distinguishable from all other objects.
- **Example:** Each person in an university is an entity.
- It has a set of properties, and the values for some set of properties may uniquely identify an entity.

---

<!-- Page 22 -->

- For instance, a person may have a `person-id` property whose value uniquely identifies that person.

### Entity Sets

- An entity set is a set of entities of the same type that share the same properties or attributes.
- **Example:** The set of all people who are instructors at a given university can be defined as the entity set instructor.
- It does not need to be disjoint.

### Attributes

- Each entity has a value for each of its attributes.
  - *I have a name, my sister has a name. Here name is attribute.*
- For instance, a particular instructor entity may have:
  - the value `12121` for `ID`
  - the value `Shishir` for `Name`,

---

<!-- Page 23 -->

- the value `ECE` for `Dept_name`, and
- the value `100000` for `Salary`.

### Relationship Sets

- It is an association among several entities.
- **Example:** adviser, borrows, teaches etc.
- A relationship set is a set of relationships of same type.
- $R \subseteq \{(e_1, e_2, \dots, e_n) \mid e_1 \in E_1, e_2 \in E_2, \dots, e_n \in E_n\}$ is a relationship.
- The part an entity plays in a relationship is the entity's **role**.

---

<!-- Page 24 -->

### Relationship Sets & Descriptive Attributes

![Fig_p024_01: Relationship set diagram showing mapping between Instructor entity set and Student entity set via Advices relationship set with descriptive attribute date](diagrams/p024_fig01.jpg)
*Figure 24.1 — Relationship set Advices between Instructor and Student entity sets with descriptive date attribute (Page 24)*

This advices relationship is going to contain an attribute so that it can handle this Association even better. This advices relationship may contain an attribute which is date where these dates helping us in providing more information where this date attribute is going to be a descriptive attribute on the advices relationship. This is a binary relation because it exists in two relations instructor and student.

---

<!-- Page 25 -->

### Cardinality Ratio & Degree of Relationship Sets

![Fig_p025_01: Relationship set diagram illustrating cardinality ratio and degree of relationship: Instructor Ramanujam participating in two associations (with students Rahman and Peter) via Advicer relationship set](diagrams/p025_fig01.jpg)
*Figure 25.1 — Relationship set showing cardinality ratio: Instructor Ramanujam participating in two associations (Page 25)*

Ramanujam entity participating in the advices relationship with the association two. This is cardinality ratio.

- $\ast$ The number of entity sets that participate in a relationship set is the **degree of the relationship**, here the advices relationship set has participation from two entity sets one is instructor another one is student so the **degree of participation** here is two because two entity sets are related or participating in the advices relationship set.

---

<!-- Page 26 -->

## Attributes

* There is a set of permitted values called the **domain** or **value set**.
* $\text{Domain of } \text{semester} = \{\text{Fall}, \text{winter}, \text{spring}, \text{summer}\}$
* $\text{Domain of } \text{course\_id} = \text{set of all strings (of a certain length)}$

### Types of Attribute

| Attribute | Type |
| :--- | :--- |
| **Name** | Composite Attribute |
| **DOB** | Simple / Single-valued |
| **Address** | Complex Attribute |
| **Age** | Derived Attribute |
| **Phone** | Multi-Valued Attribute |

#### Composite Attribute Decomposition Breakdown

* **Address:**
  * $\to$ `street`
    * $\to$ `street-number`
    * $\to$ `streetname`
    * $\to$ `apartment_number`
  * $\to$ `city`
  * $\to$ `state`
  * $\to$ `Postal-code`
* **Name:**
  * $\to$ `Firstname`
  * $\to$ `Middlename`
  * $\to$ `Lastname`

![p026_fig01: Composite attribute component breakdown for Address and Name](diagrams/p026_fig01.jpg)
*Figure 1 — Composite Attribute Breakdown for Address and Name (Page 26)*

---

<!-- Page 27 -->

## Attribute Characteristics & Types

* **Name** is not a simple attribute, it has multiple attributes which can be further divided.
* If something cannot be decomposed into smaller components that will be a **simple attribute**. Since name attribute is non-atomic in nature because they can be decomposed into smaller meaningful components or attributes, the attribute name is an example of **composite attribute**.
* A **phone number** can be many, so it needs to store multiple values (**multi-valued attribute**).
* **Age** is a **derived attribute** because age has to be updated according to the DOB (Date of Birth).

### ER Diagram Notations for Attributes

* **Simple / Single-valued:** Represented by an oval (ellipse) $\to$ $\bigcirc$
* **Composite:** Represented by an oval connected to its component ovals
* **Multi-Valued:** Represented by a double oval (concentric ellipses) $\to$ $\large\boldsymbol{\odot}$
* **Derived:** Represented by a dashed oval (dashed ellipse)
* **Null:** Null value attribute representation

![p027_fig01: ER diagram notations for different types of attributes (Simple, Composite, Multi-Valued, Derived, Null)](diagrams/p027_fig01.jpg)
*Figure 2 — ER Diagram Notations for Different Attribute Types (Page 27)*

---

<!-- Page 28 -->

## Mapping Cardinalities

* One-to-One cardinality
* One-to-Many cardinality
* Many-to-One cardinality
* Many-to-Many cardinality

* Also known as **Cardinality Ratio**.
* Used to express the number of entities to which another entity can be associated via a relationship set.
* Most useful in describing **binary relationship sets**.

### One-to-One Cardinality

![p028_fig01: One-to-one mapping cardinality between entity set A and entity set B](diagrams/p028_fig01.jpg)
*Figure 3 — One-to-One Mapping Cardinality (Page 28)*

$A, B$ are entity sets:
* $A = \{a_1, a_2, a_3, a_4\}$
* $B = \{b_1, b_2, b_3\}$
* Mappings:
  * $a_1 \to b_1$
  * $a_2 \to b_2$
  * $a_3 \to b_3$

---

<!-- Page 29 -->

An entity in entity set $A$ is associated with at most one entity in the other entity set, which is $B$.

### One-to-Many Cardinality

![p029_fig01: One-to-many mapping cardinality between entity set A and entity set B](diagrams/p029_fig01.jpg)
*Figure 4 — One-to-Many Mapping Cardinality (Page 29)*

* Mappings:
  * $a_1 \to b_1, b_2, b_3$
  * $a_2 \to b_4, b_5$
  * $a_3$ (unassociated)

An entity in entity set $A$ is actually associated with any number of entities in entity set $B$. This is called as **one-to-many**.

**Example:**
* Let assume entity set $A$ is **department** and entity set $B$ is **faculty members**.
* A department can have multiple faculty members, but a faculty member belongs to a department.

---

<!-- Page 30 -->

### Many-to-One Cardinality

![p030_fig01: Many-to-one mapping cardinality between entity set A and entity set B](diagrams/p030_fig01.jpg)
*Figure 5 — Many-to-One Mapping Cardinality (Page 30)*

* Mappings:
  * $a_1 \to b_1$
  * $a_2 \to b_1$
  * $a_3 \to b_2$
  * $a_4 \to b_3$
  * $a_5 \to b_3$

An entity in entity set $A$ is associated with at most one entity in entity set $B$. However, an entity in entity set $B$ can be associated with any number of entities in entity set $A$.

### Many-to-Many Cardinality

![p030_fig02: Many-to-many mapping cardinality between entity set A and entity set B](diagrams/p030_fig02.jpg)
*Figure 6 — Many-to-Many Mapping Cardinality (Page 30)*

* Mappings:
  * $a_1 \to b_1, b_2$
  * $a_2 \to b_1$
  * $a_3 \to b_3$
  * $a_4 \to b_3, b_4$

An entity in entity set $A$ can be associated with any number of entities in entity set $B$, and an entity in entity set $B$ can be associated with any number of entities in entity set $A$.
