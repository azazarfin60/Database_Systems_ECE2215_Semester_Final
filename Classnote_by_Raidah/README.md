# ECE 2215: Database Systems — Class Notes (Raidah)

* **Source File:** `DBMS_classnote_2310035.pdf` (34 pages / ~65 notebook sides)
* **Student:** Raidah (Roll: 2310035, Dept. of ECE, RUET)
* **Instructors:** Mst. Nafia Islam Shishir (`NIS MAM`) & Md. Rakibul Islam (`RI SIR`)
* **Unified Markdown:** [`DBMS_classnote_2310035.md`](DBMS_classnote_2310035.md)
* **Teacher Guides & Suggestions:** [`suggestions.md`](suggestions.md)

---

## Topic-wise Files (Mapped to `subtopicwise_list.md`)

| Topic ID | File | Subtopics & Syllabus Unit | Diagrams Embedded |
| :---: | :--- | :--- | :---: |
| **T01** | [`T01_DB_Concepts_and_Architecture.md`](T01_DB_Concepts_and_Architecture.md) | Unit 1: Concepts of DB, File system vs DBMS, DBA roles, 3 Abstraction levels, DDL/DML, DB Engine, 2/3-tier architecture | — |
| **T02** | [`T02_ER_and_EER_Modeling.md`](T02_ER_and_EER_Modeling.md) | Unit 2: Conceptual vs Logical, Degree of relationship, Attributes (composite, multivalued, derived), Cardinalities (1:1, 1:N, M:N), Participation (total/partial), Weak entities | `Fig_DBMS_p18_01`<br>`Fig_DBMS_p18_02` |
| **T03** | [`T03_Relational_Model_Keys_and_Integrity.md`](T03_Relational_Model_Keys_and_Integrity.md) | Unit 3: Relational model, Tuples/Attributes, Atomic domains, Schemas vs Instances, Bad schema design, Full Key hierarchy (Super, Candidate, Primary, Alternate, Composite, Foreign), Prime vs Non-prime | — |
| **T04** | [`T04_Relational_Algebra_and_Calculus.md`](T04_Relational_Algebra_and_Calculus.md) | Unit 3: Fundamental operations ($\sigma, \Pi, \times, \bowtie, \rho, \cup, -$), composition, extended aggregation ($\gamma$ avg, count, grouping), equivalent queries, design pitfalls | — |
| **T05** | [`T05_SQL_DDL_DML_Aggregates_Subqueries.md`](T05_SQL_DDL_DML_Aggregates_Subqueries.md) | Unit 4: DDL (`CREATE`, `ALTER`, `DROP`), DML (`INSERT`, `UPDATE`, `DELETE`), NULLs, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, `LIKE` with escape, `UNION ALL`, `SOME`/`ALL`, Correlated subqueries (`EXISTS`), Universal quantification (`NOT EXISTS` + `EXCEPT`), Set containment ($X - Y = \emptyset$), 2 Comprehensive Practice Schemas (Employee + Student/Enrollment) | — |
| **T06** | [`T06_Joins_and_Views.md`](T06_Joins_and_Views.md) | Unit 4: `INNER JOIN` vs Natural join, equivalent Cartesian product, Views in relational databases and data abstraction | — |
| **T08** | [`T08_Normalization_and_FDs.md`](T08_Normalization_and_FDs.md) | Unit 5: Anomalies (insert, update, delete), Row vs Column duplication, FDs (trivial, full, partial, transitive), Armstrong's Axioms, Closures $X^+$, Candidate keys, 1NF, 2NF, 3NF, BCNF, Denormalization, Lossless-join decomposition test $((R_1 \cap R_2) \rightarrow R_1 \text{ or } R_2)$, Full worked decomposition problem | — |
| **T09** | [`T09_Transactions_ACID_and_Anomalies.md`](T09_Transactions_ACID_and_Anomalies.md) | Unit 6: Transaction concept, \$50 transfer example, ACID properties, Transaction state lifecycle, Concurrent execution, Concurrency anomalies (lost update, dirty read, inconsistent analysis) | `Fig_DBMS_p26_01` |
| **T10** | [`T10_Serializability.md`](T10_Serializability.md) | Unit 6: Conflicting operations, Precedence graph construction, Indegree topological sort, Cycle test, Equivalent serial order ($T_2 \rightarrow T_3 \rightarrow T_1$), Blind writes, View serializability conditions, Relationship ($\text{Conflict} \subset \text{View}$) | `Fig_DBMS_p26_02` |
| **T11** | [`T11_Concurrency_Control_Protocols.md`](T11_Concurrency_Control_Protocols.md) | Unit 6: Deadlock, 4 Coffman conditions, Conservative 2PL, Timestamp deadlock prevention (Wait-Die vs Wound-Wait), Shared vs Exclusive locks, Starvation, 2PL Protocol (growing, lock point, shrinking), Timestamp Ordering (TSO) protocol rules and worked trace | `Fig_DBMS_p30_01` |
| **T12** | [`T12_Recovery_and_RAID.md`](T12_Recovery_and_RAID.md) | Unit 7: RAID Overview, RAID 0 (data striping), RAID 1 (mirroring), RAID 1+0 (striped mirrors), RAID 3 (bit-interleaved parity disk), RAID 5 (distributed parity), RAID 6 (dual $P+Q$ distributed parity) | `Fig_DBMS_p32_01`<br>`Fig_DBMS_p32_02`<br>`Fig_DBMS_p32_03`<br>`Fig_DBMS_p33_01`<br>`Fig_DBMS_p33_02`<br>`Fig_DBMS_p33_03` |

> [!NOTE]
> * **T07 (Triggers & Stored Procedures)** and **T13 (Security, Indexing & Hashing):** These topics were not included in Raidah's notebook. For classroom handnote coverage of SQL Triggers (`T07`), see [`../Handnote_by_Fahim_2310002/T07_Triggers_and_Stored_Procedures.md`](../Handnote_by_Fahim_2310002/T07_Triggers_and_Stored_Procedures.md); for Stored Procedures and `T13`, refer to the textbook chapters (`Chapter 05`, `Chapter 09`, `Chapter 14`).

