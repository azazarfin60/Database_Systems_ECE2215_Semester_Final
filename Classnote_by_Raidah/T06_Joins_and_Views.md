# T06: Joins & Views — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 4 | `subtopicwise_list.md` T06 (28 marks · 4.4% · 4/7 · 🟠)  
**Source Pages:** Page 3 (Right), Page 11 (Right), Page 18 (Left)

---

## 1. SQL Join Relationships

<!-- Page 18 (Left) -->
<!-- Date: 28.07.2024 | Teacher: NIS MAM -->

### Inner Join Syntax:
```sql
SELECT * FROM table1
INNER JOIN table2
ON table1.matching_col = table2.matching_col;
```

### Equivalent Cartesian Product Query:
```sql
SELECT * FROM table1, table2
WHERE table1.matching_col = table2.matching_col;
```

### Inner Join vs. Natural Join:
* **Inner Join:** Requires an explicit join predicate (`ON` or `USING`) specifying which attributes must match.
  * *In an Inner Join, the matching condition must be explicitly specified (e.g., using ON or USING).*
* **Natural Join (`NATURAL JOIN`):** Automatically joins two tables based on all columns that share the same name and domain type; duplicate common columns are combined into a single column.
  * *In a Natural Join, the matching condition does not need to be specified (it automatically matches all attributes with identical names).*

---

## 2. Views in Relational Databases

<!-- Page 3 (Right), Page 11 (Right), Page 18 (Left) -->

* **Definition:** A view is a virtual relation that is not part of the physical schema, but is made visible to a user as a virtual table computed from underlying base tables.
* **Role in Data Abstraction:** Provides the **View Level** of data abstraction, hiding unnecessary or sensitive data from specific user groups and presenting customized schemas.
* **Security & Simplicity:** Simplifies complex multi-table join queries into straightforward virtual table selections.

