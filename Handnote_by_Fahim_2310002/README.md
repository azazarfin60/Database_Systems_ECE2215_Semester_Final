# ECE 2215: Database Systems — Class Handnotes (Fahim)

* **Source File:** `Handnote_2310002.pdf` (62 pages)
* **Student:** Fahim (Roll: 2310002, Dept. of ECE, RUET)
* **Instructors:** Mst. Nafia Islam Shishir (`NIS MAM`) & Md. Rakibul Islam (`RI SIR`)
* **Unified Markdown:** [`Handnote_2310002.md`](Handnote_2310002.md)

---

## Topic-wise Files (Mapped to `subtopicwise_list.md`)

| Topic ID | File | Subtopics & Syllabus Unit | Diagrams Embedded |
| :---: | :--- | :--- | :---: |
| **T01** | [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) | Unit 1: Concepts of DB, Definitions (Data, Information, DB, Metadata), Functionalities & Properties, DB Environment Architecture, File System vs. DBMS, 4 DBMS Characteristics (Catalog, Abstraction, Views, Concurrency), Database Users (Actors on Scene vs Workers Behind Scene), DBMS Advantages, Data Models (Conceptual, Physical, Representational), Schemas vs Instances, Design Process & Issues | `p004_fig01`<br>`p005_fig01`<br>`p010_fig01` |
| **T02** | [`T02_ER_and_EER_Modeling.md`](T02_ER_and_EER_Modeling.md) | Unit 2: Introduction to E-R Model, Entity Sets, Attributes, Relationship Sets & Roles, Descriptive Attributes, Degree of Relationships & Cardinality Ratio, Attribute Types (Composite, Simple, Complex, Derived, Multi-valued) & Decomposition Tree, ER Diagram Notations Chart, Mapping Cardinalities (1:1, 1:N, M:1, M:N) | `p021_fig01`<br>`p024_fig01`<br>`p025_fig01`<br>`p026_fig01`<br>`p027_fig01`<br>`p028_fig01`<br>`p029_fig01`<br>`p030_fig01`<br>`p030_fig02` |
| **T03** | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) | Unit 3: Relational Model Terminologies (Relation Schema, Schema Construct, State/Instance), Relational Keys (Primary Key, Foreign Key characteristics, Student/City tables relationship example, Bengali FK intuition), Constraints & Foreign Key Syntax, Cascading Actions (`ON DELETE CASCADE`, `ON UPDATE CASCADE`) | `p018_fig01`<br>`p036_fig01`<br>`p037_fig01` |
| **T05** | [`T05_SQL_DDL_DML_Aggregates_Subqueries.md`](T05_SQL_DDL_DML_Aggregates_Subqueries.md) | Unit 4: SQL Overview & Relational vs NoSQL, CRUD, Database Structure & DDL (`CREATE/DROP DATABASE`, `CREATE TABLE`, datatypes, DDL/DQL/DML/DCL/TCL commands, `INSERT INTO`, `SELECT *`), SQL Constraints (`NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `DEFAULT`, `CHECK`), Querying with `SELECT` & Operators (`WHERE`, `AND`/`OR`, `BETWEEN`, `IN`, `NOT`, `LIMIT`, `ORDER BY`), Aggregations (`COUNT`, `MAX`, `MIN`, `SUM`, `AVG`, `GROUP BY`, `HAVING`), Table Modification (`UPDATE`, `DELETE`), Schema Modification (`ALTER TABLE ADD/DROP/MODIFY/CHANGE/RENAME`, `TRUNCATE` vs `DROP`), Set Operations (`UNION`, `UNION ALL`), SQL Subqueries (Nested queries: `WHERE` subquery, even roll dynamic subquery, `FROM` derived table), Pattern Matching with `LIKE` (`%`, `_`) | `p032_fig01`<br>`p056_fig01` |
| **T06** | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) | Unit 4: SQL Joins Overview & Venn Diagrams, Inner Join (syntax, matching example, output), Outer Joins (Left Join with Venn diagram, Right Join, Full Join via `UNION`), Exclusive Joins (Left Exclusive Join $A - B$, Right Exclusive Join $B - A$), Self Join (Employee/Manager hierarchy, query & output), Database Views (Virtual tables, `CREATE VIEW`, benefits, security/column abstraction, isolation) | `p050_fig01`<br>`p052_fig01`<br>`p053_fig01` |
| **T07** | [`T07_Triggers_and_Stored_Procedures.md`](T07_Triggers_and_Stored_Procedures.md) | Unit 4: Database Triggers Concept & Purposes, Trigger Syntax (`CREATE TRIGGER ... AFTER/BEFORE ... FOR EACH ROW BEGIN ... END;`), Firing Events & Timing (`INSERT`, `UPDATE`, `DELETE`, `BEFORE`, `AFTER`), Real-World Salary/Pay Intuition in Bengali, Trigger Structure & Event-Condition-Action Lifecycle | — |

---

## Notable Characteristics of Fahim's Notes

1. **Classroom Coverage of T07 (Triggers):** While Raidah's notes (`Classnote_by_Raidah/`) did not include Triggers (treating them as textbook-only), Fahim's handnotes provide explicit classroom coverage of SQL Triggers with syntax, timing rules, and Bengali intuition.
2. **Comprehensive SQL Hands-on Focus:** Detailed coverage of hands-on MySQL syntax, table constraints (`CHECK`, `DEFAULT`), cascading foreign keys (`ON DELETE/UPDATE CASCADE`), and SQL pattern matching (`LIKE`).
3. **Complete Set of Relational Joins:** Clear Venn diagram representations and concrete query demonstrations for Inner Join, Left Join, Right Join, Full Join (via MySQL `UNION`), Left Exclusive Join, Right Exclusive Join, and Self Join.
4. **Complementary Coverage:** Topics not covered in this handnote (such as Relational Algebra T04, Normalization T08, and Transactions/Concurrency/Recovery T09–T12) are fully detailed in `Classnote_by_Raidah/`, the official lecture slides (`LectureSlides/`), and the textbook chapters (`Textbook/`).
