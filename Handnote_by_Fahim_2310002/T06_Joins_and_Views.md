# T06: Joins & Views — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 4 | `subtopicwise_list.md` T06 (28 marks · 4.4% · 4/7)  
**Source Pages:** Page 50 (Bottom) – Page 55 (Top), Page 58 (Bottom) – Page 59 (Top)

---

<!-- Page 50 -->

## Joins in SQL

Join is used to combine rows from two or more tables, based on a related column between them.

### Types of Joins

![p050_fig01: Venn diagrams representing SQL join types: Inner Join, Left Join, Right Join, and Full Join (Outer Joins)](diagrams/p050_fig01.jpg)
*Figure 1 — SQL Join Types: Inner Join, Left Join, Right Join, Full Join (Page 50)*

- **Inner Join:** Returns records that have matching values in both tables.
- **Outer Joins:**
  - **Left Join:** Returns all records from the left table, and the matched records from the right table.
  - **Right Join:** Returns all records from the right table, and the matched records from the left table.
  - **Full Join:** Returns all records when there is a match in either left or right table.

---

<!-- Page 51 -->

## Inner Join

Returns records that have matching values in both tables.

### Syntax

```sql
SELECT column(s)
FROM tableA
INNER JOIN tableB
ON tableA.col_name = tableB.col_name;
```

### Example

#### Given Tables

**`student`**

| student_id | name |
| :--- | :--- |
| 101 | adam |
| 102 | bob |
| 103 | casey |

**`course`**

| student_id | course |
| :--- | :--- |
| 102 | english |
| 105 | math |
| 103 | science |
| 107 | computer science |

#### Query

```sql
SELECT *
FROM student
INNER JOIN course
ON student.student_id = course.student_id;
```

#### Output

| student_id | name | course |
| :--- | :--- | :--- |
| 102 | bob | english |
| 103 | casey | science |

---

<!-- Page 52 -->

## Left Join

Returns all records from the left table, and the matched records from the right table.

![Fig_p052_01: Venn diagram illustrating Left Join with set A and intersection shaded](diagrams/p052_fig01.jpg)
*Figure 1 — Left Join Venn Diagram (Page 52)*

### Syntax

```sql
SELECT column(s)
FROM tableA
LEFT JOIN tableB
ON tableA.col_name = tableB.col_name;
```

---

## Right Join

Returns all records from the right table and the matched records from the left table.

### Syntax

```sql
SELECT column(s)
FROM tableA
RIGHT JOIN tableB
ON tableA.col_name = tableB.col_name;
```

### Example Query

```sql
SELECT *
FROM student AS s
RIGHT JOIN course AS c
ON s.student_id = c.student_id;
```

---

<!-- Page 53 -->

## Full Join

Returns all records when there is a match in either left or right table.

### Syntax in MySQL

> [!NOTE]
> MySQL does not support direct `FULL OUTER JOIN`, so it is emulated using `UNION` of `LEFT JOIN` and `RIGHT JOIN`.

```sql
SELECT * FROM student AS a
LEFT JOIN course AS b
ON a.id = b.id
UNION
SELECT * FROM student AS a
RIGHT JOIN course AS b
ON a.id = b.id;
```

---

## Left Exclusive Join (Set Difference: $A - B$)

Returns only records present in the left table that have no match in the right table.

![Fig_p053_01: Venn diagram representing Left Exclusive Join (A - B) with set A shaded excluding the intersection](diagrams/p053_fig01.jpg)
*Figure 2 — Left Exclusive Join / Set Difference (Page 53)*

### Query

```sql
SELECT *
FROM student AS a
LEFT JOIN course AS b
ON a.id = b.id
WHERE b.id IS NULL;
```

---

<!-- Page 54 -->

## Right Exclusive Join

Returns only records present in the right table that have no match in the left table.

### Query

```sql
SELECT *
FROM student AS a
RIGHT JOIN course AS b
ON a.id = b.id
WHERE a.id IS NULL;
```

---

## Self Join

A regular join, but the table is joined with itself.

### Query

```sql
SELECT a.name AS manager_name, b.name
FROM employee AS a
JOIN employee AS b
ON a.id = b.manager_id;
```

### Example

**`Employee` Table**

| id | name | manager_id |
| :--- | :--- | :--- |
| 101 | adam | 103 (casey) |
| 102 | bob | 104 (donald) |
| 103 | casey | NULL |
| 104 | donald | 103 (casey) |

---

<!-- Page 55 -->

### Result (Self Join Output)

| manager_name | name |
| :--- | :--- |
| casey | adam |
| donald | bob |
| casey | donald |

---

<!-- Page 58 -->

## MySQL Views

A view is a virtual table based on the result-set of an SQL statement.

### Creating and Querying a View

```sql
CREATE VIEW view1 AS
SELECT roll_no, name FROM student;

SELECT * FROM view1;
```

> [!NOTE] View এর বৈশিষ্ট্য ও ব্যবহার
> view হলো virtual table। এখানে আসল table এর যতটুকু প্রয়োজন দেখা যায় এবং multiple operation যেগুলো table এ Apply হয় ঐগুলো view তেও Apply করা যায়।
>
> view delete করলেও overall database এ কোনো effect পড়ে না।

---

<!-- Page 59 -->

## MySQL Views (Overview & Use Cases)

A view in MySQL is a virtual table based on the result of a `SELECT` query. It does not store data itself — it always reflects the current data in the base tables.

### Views are useful when:

- You want to simplify complex queries
- You want to reuse logic
- You want to hide certain columns from users (security/privacy)
- You want a live snapshot of filtered data
