# ECE 2215: Database Systems — Subtopic-wise Question Bank (Finals 2017–2024 & Class Tests)

> **Complete & Verbatim Question Bank:** Every past semester-final question (**7 papers: 2017–2021, 2023–2024; 56 main questions, 148 sub-questions, 637 printed marks**) and every class-test question (**CT-01 to CT-04; 15 main questions, 26 parts, 80 marks**) is sorted below under its exact topic (`T01`–`T13`) across **77 subtopics** (`T01.1`–`T13.4`, extending up to `T08.11`) from [subtopicwise_list.md](file:///home/azaz/AntigravityxStudy/SemesterFinal_2_2/ECE_2215/subtopicwise_list.md).
> - All **148 unique final sub-questions (637 marks)** and **15 CT questions (26 parts, 80 marks)** appear verbatim with original schemas, side-by-side tables, and `*(Note: ...)*` annotations.
> - Each final sub-question is counted once under its primary subtopic, with the sole documented intentional 2 + 2 split on `2018 Q.5(c)` (2m under `T12.1` for DBMS failures + 2m under `T12.4` for RAID recovery, matching `ECE2215_PYQ_Analysis_Report.md` §C5). Thus, all 148 unique questions (637 marks) appear across 149 entry blocks (with Q.5(c) displayed as 2m in each section).

## Topic Overview & Reconciliation

- **[T01. DB Concepts & Architecture](#t01-db-concepts--architecture)** *(Unit 1)* — **44** Final Marks (`6.9%` · 13 sub-Qs · 7/7 papers) + **7** CT Marks (2 parts)
- **[T02. E-R / EER Modeling](#t02-e-r--eer-modeling)** *(Unit 2)* — **67** Final Marks (`10.5%` · 18 sub-Qs · 7/7 papers) + **10** CT Marks (2 parts)
- **[T03. Relational Model, Keys & Integrity](#t03-relational-model-keys--integrity)** *(Unit 3)* — **28** Final Marks (`4.4%` · 7 sub-Qs · 5/7 papers) + **5** CT Marks (1 part)
- **[T04. Relational Algebra & Calculus](#t04-relational-algebra--calculus)** *(Unit 3)* — **48** Final Marks (`7.5%` · 9 sub-Qs · 6/7 papers) + **8** CT Marks (6 parts)
- **[T05. SQL (DDL, DML, Aggregates, Subqueries)](#t05-sql-ddl-dml-aggregates-subqueries)** *(Unit 4)* — **130** Final Marks (`20.4%` · 23 sub-Qs · 7/7 papers) + **10** CT Marks (4 parts)
- **[T06. Joins & Views](#t06-joins--views)** *(Unit 4)* — **28** Final Marks (`4.4%` · 7 sub-Qs · 4/7 papers)
- **[T07. Triggers & Stored Procedures](#t07-triggers--stored-procedures)** *(Unit 4)* — **27** Final Marks (`4.2%` · 6 sub-Qs · 5/7 papers)
- **[T08. Normalization & Functional Dependencies](#t08-normalization--functional-dependencies)** *(Unit 5)* — **75** Final Marks (`11.8%` · 16 sub-Qs · 7/7 papers) + **20** CT Marks (7 parts)
- **[T09. Transactions, ACID & Anomalies](#t09-transactions-acid--anomalies)** *(Unit 6)* — **41** Final Marks (`6.4%` · 12 sub-Qs · 7/7 papers) + **14** CT Marks (3 parts)
- **[T10. Serializability](#t10-serializability)** *(Unit 6)* — **51** Final Marks (`8.0%` · 11 sub-Qs · 7/7 papers) + **6** CT Marks (1 part)
- **[T11. Concurrency Control Protocols](#t11-concurrency-control-protocols)** *(Unit 6)* — **37** Final Marks (`5.8%` · 9 sub-Qs · 6/7 papers)
- **[T12. Recovery System & RAID](#t12-recovery-system--raid)** *(Unit 7)* — **43** Final Marks (`6.8%` · 13 sub-Qs *(incl. 2018 Q.5(c) 2+2 split)* · 5/7 papers)
- **[T13. Security, Indexing & Hashing](#t13-security-indexing--hashing)** *(Unit 8)* — **18** Final Marks (`2.8%` · 5 sub-Qs · 4/7 papers)
- **Grand Total (13 Topics · 77 Subtopics)** — **637** Final Marks (`100%` · **148** unique sub-questions) + **80** CT Marks (**15** main questions / **26** parts)

---

## T01. DB Concepts & Architecture
*Weightage: **44** Final Marks (`6.9%` · `7/7` Papers) + **07** CT Marks · Syllabus Unit 1*

### T01.1 — Data vs information; what a DB and a DBMS are; DBMS applications · `0m` Finals (0) · *D01 S2–5*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Background concepts tested within **T01.2** (`2018 Q.1(a)`, `2019 Q.1(a)`).

### T01.2 — File system vs DBMS (8 disadvantages of file systems) · `21m` Finals (6) · *D01 S6–7*

**[2017 · Q.1(a) | 04 Marks | Sec A]**  
Write down four significant differences between a file processing system and a DBMS.

**[2018 · Q.1(a) | 03 Marks | Sec A]**  
"A database is a tool for storing information efficiently"- Justify this statement.

**[2019 · Q.1(a) | 03 Marks | Sec A]**  
Why DBMS is important? What are its advantages?

**[2021 · Q.1(a) | 04 Marks | Sec A | CLO1]**  
Discuss four significant differences between a file-processing system and a DBMS.

**[2023 · Q.1(b) | 03 Marks | Sec A | CLO1]**  
What are the advantages of DBMS over file processing system?

**[2024 · Q.1(a) | 04 Marks | Sec A | CO1]**  
A courier tracking company maintains large files for daily parcel updates. The data grows rapidly and requires fast retrieval. Choose between a file based system and a DBMS and justify the decision.

### T01.3 — Functions/roles of the DBA ("five functions"); relation schema · `10m` Finals (3) · *D01 S10, D02 S6*

**[2017 · Q.1(c) | 02 Marks | Sec A]**  
What are the main functions of a database administrator? Point out the name only.

**[2020 · Q.1(a) | 05 Marks | Sec A]**  
What are the five main functions of a database administrator? What is relation schema?

**[2021 · Q.1(b) | 03 Marks | Sec A | CLO1]**  
What are the five main functions of a database administrator?

### T01.4 — Data abstraction levels (physical/logical/view), schemas & instances (physical data independence: Ch. 1 §1.3.1) · `8m` Finals (2) + `5m` CTs (1) · *D01 S13–15 · Ch. 1 §1.3*

**[2017 · Q.2(b) | 04 Marks | Sec A]**  
What is the purpose of data abstraction? Describe the different level of data abstraction.

**[2019 · Q.2(a) | 04 Marks | Sec A]**  
What is data abstraction? Describe the different level of data abstraction.

**[CT-01 · Q.01 | 05 Marks | CO1]**  
Define data abstraction. Describe different types of data abstractions.

### T01.5 — DDL vs DML (procedural vs declarative) · `2m` Finals (1) · *D01 S16–19*

**[2023 · Q.1(c) | 02 Marks | Sec A | CLO1]**  
Explain DDL and DML with example.

### T01.6 — DBMS engine components (storage manager, query processor) · `0m` Finals (0) · *D01 S22–25*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

### T01.7 — 2-tier vs 3-tier architecture; DB application structure · `3m` Finals (1) + `2m` CTs (1) · *D01 S29–31*

**[2020 · Q.1(b) | 03 Marks | Sec A]**  
Differentiate between the two-tier architecture and three-tier architecture of database. Which is better suited for web application? Why?

**[CT-01 · Q.03 | 02 Marks | CO1]**  
Describe the structure of a database application.

---

## T02. E-R / EER Modeling
*Weightage: **67** Final Marks (`10.5%` · `7/7` Papers) + **10** CT Marks · Syllabus Unit 2*

### T02.1 — Entity sets, relationship sets, types of relationships (unary/binary/ternary) · `4m` Finals (1) · *D05 S7–16*

**[2021 · Q.5(a) | 04 Marks | Sec B | CLO1]**  
What is ER diagram? Illustrate different types of relationship that can be represented in ER diagram.

### T02.2 — Attribute types (simple/composite, single/multivalued, derived) · `8m` Finals (2) · *D05 S17–19*

**[2020 · Q.5(a) | 04 Marks | Sec B]**  
Differentiate between-  
(i) Simple and composite attribute  
(ii) Single-valued and multi-valued attribute

**[2021 · Q.3(b) | 04 Marks | Sec A | CLO4]**  
Define entity and attribute. Explain the following attributes-  
(i) Multi-valued  
(ii) Derived  
(iii) Composite

### T02.3 — Mapping cardinality (1:1, 1:N, M:N) & participation constraints · `8m` Finals (2) · *D05 S20–27*

**[2018 · Q.3(c) | 04 Marks | Sec A]**  
What is mapping cardinality? How a many to many relationship can be converted into table. Explain with example.

*(Sorting Note: Also converts M:N to table, see T02.6)*

**[2020 · Q.1(c) | 04 Marks | Sec A]**  
What is mapping cardinalities? Define different types of cardinalities.

> *Cross-ref:* **2018 Q.1(c)** (`05m`, in **T02.5**) tests participation constraints; **CT-02 Q.02(a)** (`04m`, in **T02.5**) asks for entities, keys, relationships, and cardinalities.

### T02.4 — Weak vs strong entity sets (discriminator, identifying relationship) · `11m` Finals (4) · *D05 S34–37*

**[2018 · Q.1(b) | 04 Marks | Sec A]**  
Define entity set. Explain the following with suitable example: (i) strong entity set and (ii) weak entity set.

**[2019 · Q.1(b) | 03 Marks | Sec A]**  
What are entity and entity set? How is a weak entity set handled in DBMS? Explain.

**[2020 · Q.2(c) | 02 Marks | Sec A]**  
Explain the difference between a weak and a strong entity set with appropriate example.

**[2021 · Q.8(c) | 02 Marks | Sec B | CLO1]**  
Explain weak and strong entity set with appropriate example.

### T02.5 — Design a full E-R diagram for a scenario · `24m` Finals (5) + `10m` CTs (1) · *D05 S7–39*

**[2017 · Q.1(b) | 06 Marks | Sec A]**  
Draw an E-R diagram for RUET student database which can be used to store student's basic information, course advisor's information, subject registration, result information.

**[2018 · Q.1(c) | 05 Marks | Sec A]**  
What is E-R model? Draw an E-R diagram that includes teacher, student and course entities with following constraints: (i) Each teacher must take at least one course; (ii) A student can register one or more courses; (iii) A course may have teacher or not.

*(Sorting Note: Tests participation constraints, see T02.3)*

**[2019 · Q.1(c) | 06 Marks | Sec A]**  
Suppose you are recruited as a database specialist by the Rajshahi High-Tech authority to help them design a database for train e-ticketing system efficiently. Now think the regular features and draw an E-R diagram accordingly.

**[2023 · Q.1(a) | 05 Marks | Sec A | CLO4]**  
Draw an ER diagram for RUET Central Library Management System. You have to consider the entities mentioned below:  
(i) Books (ii) Members (iii) Staff (iv) Borrowing (v) Reservations

**[2024 · Q.1(b) | 02 Marks | Sec A | CO3]**  
Draw an E-R diagram for RUET student database which can be used to store student’s basic information, course advisor’s information, subject registration, result information.

**[CT-02 · Q.02(a–b) | 10 Marks | CO3]**  
A university maintains information about Students, Courses, and Teachers. A student can enroll in several courses and each course can have many students. Each course is taught by one teacher, though a teacher may teach several courses.  
**(a)** Identify the entities, attributes, primary keys, relationships, and cardinalities. `[04 Marks]`  
**(b)** Draw the complete ER diagram. `[06 Marks]`

### T02.6 — Reduction of E-R to relational tables (M:N, ternary) · `5m` Finals (1) · *D05 S40–48*

**[2018 · Q.2(c) | 05 Marks | Sec A]**  
Consider a database used to record the marks that students get in different examinations of different course offerings. (i) Construct an E-R diagram that models examinations as entities, and uses a ternary relationship for the above database; (ii) Draw a relational data model for the above corresponding E-R diagram.

> *Cross-ref:* **2018 Q.3(c)** (`04m`, in **T02.3**) asks how a many-to-many relationship is converted into a table.

### T02.7 — EER: specialization / generalization · `2m` Finals (1) · *D05 S49–56*

**[2017 · Q.6(a) | 02 Marks | Sec B]**  
Write short note on specialization and generalization in DBMS.

### T02.8 — EER: aggregation · `5m` Finals (2) · *D05 S57–60*

**[2018 · Q.2(b) | 03 Marks | Sec A]**  
Define the concept of aggregation. Give two examples of where this concept is useful.

**[2020 · Q.3(a) | 02 Marks | Sec A]**  
What is aggregation in ER-model design?

---

## T03. Relational Model, Keys & Integrity
*Weightage: **28** Final Marks (`4.4%` · `5/7` Papers) + **05** CT Marks · Syllabus Unit 3*

### T03.1 — Relation, tuple, attribute, domain; domain vs data type · `2m` Finals (1) · *D02 S2–5, D03 S6*

**[2018 · Q.3(b) | 02 Marks | Sec A]**  
Differentiate between domain and data type.

### T03.2 — Keys: super / candidate / primary / alternate / composite / foreign · `21m` Finals (5) · *D02 S7, D06 S11–13*

**[2018 · Q.2(a) | 04 Marks | Sec A]**  
Explain the distinctions among the terms primary key, candidate key, and super key with proper example.

**[2019 · Q.6(b) | 06 Marks | Sec B]**  
Discuss the different keys in DBMS. Write down the importance and use of foreign key with example.

**[2020 · Q.2(b) | 04 Marks | Sec A]**  
Write short note about: Super Key, Candidate Key, Primary Key, and Foreign Key.

**[2021 · Q.2(b) | 03 Marks | Sec A | CLO1]**  
Differentiate among Superkey, Candidate Key and Primary Key with an appropriate example.

**[2023 · Q.3(b) | 04 Marks | Sec A | CLO2]**  
Explain the distinctions among the terms-  
(i) Primary key  
(ii) Candidate key  
(iii) Super key  
(iv) Composite key

### T03.3 — Referential integrity & FK syntax (MySQL) · `5m` Finals (1) · *D03 S8–10*

**[2021 · Q.1(c) | 05 Marks | Sec A | CLO2]**  
How do we achieve referential integrity in DBMS? Provide necessary MySQL query with an appropriate example.

### T03.4 — Schema diagrams · `0m` Finals (0) + `5m` CTs (1) · *D02 S8*

**[CT-01 · Q.02 | 05 Marks | CO1]**  
Draw a schema diagram for ECE, including 5 tables (Students, Courses, Instructors, Classroom, Results).

---

## T04. Relational Algebra & Calculus
*Weightage: **48** Final Marks (`7.5%` · `6/7` Papers) + **08** CT Marks · Syllabus Unit 3*

### T04.1 — Basic operators: $\sigma, \Pi, \times, \bowtie, \cup, \cap, -, \rho, \leftarrow$ · `0m` Finals (0) · *D02 S9–26*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Foundation for all relational algebra queries in **T04.2** and expression explanations in **T04.3**.

### T04.2 — Write RA queries on a given schema (incl. "only" queries → set difference, $\gamma$ count/max, RA modification/update) · `41m` Finals (7) + `4m` CTs (1) · *D02 S9–29; RA updates are 6e-only*

**[2017 · Q.2(a) | 08 Marks | Sec A]**  
Consider the following relational database.  
  `employee(person_name, street, city)`  
  `works(person_name, company_name, salary)`  
  `company(company_name, city)`  
  `manages(person_name, manager_name)`  
Now write down the relational algebra(Not SQL) to express each of following queries:  
(i) Find the names of all employees who live in the city same as their corresponding company location.  
(ii) Give a 10% salary raise to all the managers only.  
(iii) Update the city information of the employee named "James" to "Newtown".  
(iv) Find the company with most employees.

*(Sorting Note: Part iv uses $\gamma$ aggregation, see T04.4; parts ii–iii use RA updates)*

**[2018 · Q.3(a) | 06 Marks | Sec A]**  
Consider the following insurance database, where primary keys are underlined.  
person (<u>driver_id</u>, name, address)  
car (<u>license</u>, model, year)  
accident (<u>report_number</u>, date, location)  
owns (<u>driver_id</u>, license)  
participated (<u>driver_id</u>, car, <u>report_number</u>, damage_amount)

Write down the relational algebra statement for the following queries:  
(i) Find the total number of people who owned cars that were involved in accidents in 1989.  
(ii) Find the number of accidents in which the cars belonging to "John Smith" were involved.  
(iii) Update the damage amounts for the car with license number "AABB2019" in the accident with report_number "AR201930" to \$3000.

*(Sorting Note: Parts i–ii use $\gamma$ aggregation, see T04.4; part iii uses RA update)*

**[2019 · Q.2(b) | 08 Marks | Sec A]**  
Consider the following relational database.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

Now write down the relational algebra (Not SQL) to find out the following queries.  
(i) Find the names of those patients who have fever symptom.  
(ii) Consider that if any patient has high-fever symptom he/she will be suspected as corona patient. Find out such maximum number of patients in a date.  
(iii) Find out the mobile numbers of those patients who have provided samples in Rajshahi corona center and their results have become positive.  
(iv) Find out the name of those patients who have high fever symptom but test result have become negative.

*(Note: Printed as "Parient_ID" in Report schema in original question paper; refers to "Patient_ID")*

*(Sorting Note: Part ii uses $\gamma$ aggregation, see T04.4)*

**[2020 · Q.2(a) | 06 Marks | Sec A]**  
Consider the following relation schema:  
  person(<u>id</u>, name, age)  
  vaccine(<u>id</u>, center, dose_no, date)  
Now give expression in relational algebra to express-  
(i) Find the names of all persons who are adult.  
(ii) Find the names of all persons who have taken the $1^{\text{st}}$ dose only.  
(iii) Find the details of all persons who were given vaccine from "RMC" center and completed $2^{\text{nd}}$ dose.

**[2021 · Q.2(a) | 05 Marks | Sec A | CLO2]**  
Consider the following relation schema:  
  customer (<u>id</u>, name, age, gender)  
  order (<u>id</u>, product, price, date)

Now, give expression in relational algebra to-  
(i) find name of the customers who are male.  
(ii) find name of all customers who have purchased car as product.  
(iii) find the details of all customers who have purchased "phone" as product and the price is less than \$300.

**[2024 · Q.2(b) | 04 Marks | Sec A | CO1]**  
EMPLOYEE (EID, Name, Department, Salary)  
PROJECT (PID, Name, Budget)  
WORKS_ON (EID, PID, Hours)  
Suppose a company wants to find employees working on multiple projects. Write the relational algebra expression for it.

*(Sorting Note: Uses $\gamma$ aggregation, see T04.4)*

**[2024 · Q.5(a) | 04 Marks | Sec B | CO2]**  
Consider the following relation database:  
Patient (Patient_ID, Patient_Name, Mobile)  
History (Patient_ID, Symptom, Date)  
Report (Patient_ID, Corona_center, Test_result)  
Now, write down the relational algebra (Not SQL) to find out the following queris:  
i) Find the names of those patients who have fever symptom  
ii) Find out the mobile numbers of those patients who have provided samples in Rangpur corona center and their results have become positive.  
*(Note: "relation database" and "queris" printed verbatim in original paper; refers to relational database and queries)*

**[CT-01 · Q.04(v–viii) | 04 Marks | CO1]**  
Relations: $\text{STUDENT}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name}, \text{CGPA})$, $\text{COURSE}(\text{Course\_ID}, \text{Course\_Name}, \text{Student\_ID}, \text{Semester}, \text{Marks})$, $\text{ALUMNI}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name})$.  
Write the relational algebra expressions for the following conditions using the relations above:  
**(v)** Rename the relation $\text{STUDENT}$ as $\text{S}$ and display the $\text{Student\_ID}$ and $\text{Name}$ of all students.  
**(vi)** Retrieve the $\text{Student\_ID}$, $\text{Name}$, and $\text{Course\_Name}$ of all students who belong to the CSE department and scored 80 or more marks in any course.  
**(vii)** Retrieve the $\text{Student\_ID}$ and $\text{Name}$ of all students who are either in the $\text{STUDENT}$ relation or the $\text{ALUMNI}$ relation.  
**(viii)** Determine the number of students in each department.  
*(Note: Sub-parts are numbered v, vi, vii, viii on the original question script; part viii uses $\gamma$ aggregation, see T04.4).*

### T04.3 — Explain an RA expression in words · `4m` Finals (1) + `4m` CTs (1) · *D02 S15–24*

**[2021 · Q.2(c) | 04 Marks | Sec A | CLO2]**  
For each expression, explain in words what the expression does.  
Where takes(<u>id</u>, <u>course</u>, <u>sec_id</u>, sem, year, grade)  
(i) $\sigma_{year \ge 2009}(\text{takes}) \bowtie \text{student}$  
(ii) $\Pi_{id, name, course\_id}(\text{student} \bowtie \text{takes})$

**[CT-01 · Q.05(iii–iv) | 04 Marks | CO1]**  
Describe the following relational algebra expression:  
**(iii)** $\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$  
**(iv)** $\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$  
*(Note: Sub-parts are numbered iii, iv on the original question script; part iv is Deck 02 Slide 24 verbatim).*

### T04.4 — Extended RA: aggregation $_{G}\gamma_{F}$ (counted inside T04.2) · `0m` Finals (0) · *D02 S27–29 · Ch. 16 §16.1*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Counted inside **T04.2**: **2017 Q.2(a)(iv)** (*company with most employees*), **2018 Q.3(a)(i–ii)** (*total people / number of accidents*), **2019 Q.2(b)(ii)** (*maximum suspected patients in a date*), **2024 Q.2(b)** (*employees on multiple projects*), and **CT-01 Q.04(viii)** (*students per department*).

### T04.5 — Domain relational calculus (and division $\div$) · `3m` Finals (1) · *Not in 7e (online Ch. 27)*

**[2020 · Q.4(b) | 03 Marks | Sec A]**  
Let that, $R=(A, B, C)$ and $r_1$, $r_2$ both be relations on the schema R. Give an expression in the domain relational calculus that is equivalent to each of the followings.  
(i) $\pi_A(r_1)$  
(ii) $r_1 \cup r_2$  
(iii) $r_1 \cap r_2$

---

## T05. SQL (DDL, DML, Aggregates, Subqueries)
*Weightage: **130** Final Marks (`20.4%` · `7/7` Papers) + **10** CT Marks · Syllabus Unit 4*

### T05.1 — What SQL is; SQL short note · `2m` Finals (1) · *D03 S3–4*

**[2019 · Q.5(a) | 02 Marks | Sec B]**  
Write a short note on SQL.

### T05.2 — DDL + DML warm-up: `CREATE`, `INSERT`, `ALTER ... ADD`, `UPDATE`, `DELETE`, rename, filter · `33m` Finals (6) + `2m` CTs (1) · *D03 S5–11, S53–61*

**[2017 · Q.4(a) | 09 Marks | Sec A]**  
Considering following tables (INFO, MARKS, CREDIT) answer (i),(ii) & (iii).

<table style="border: none; border-collapse: collapse;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 15px;"><b>INFO</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>roll</th><th>name</th></tr></thead><tbody><tr><td>1710001</td><td>Amelia</td></tr><tr><td>1710002</td><td>Oliver</td></tr><tr><td>1710003</td><td>James</td></tr><tr><td>1710004</td><td>Sansa</td></tr></tbody></table></td><td style="border: none; padding-right: 15px;"><b>MARKS</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>roll</th><th>sub_code</th><th>gpa</th></tr></thead><tbody><tr><td>1710001</td><td>ECE 2205</td><td>3.50</td></tr><tr><td>1710001</td><td>ECE 2215</td><td>3.75</td></tr><tr><td>1710002</td><td>ECE 2205</td><td>3.75</td></tr><tr><td>1710002</td><td>ECE 2215</td><td>3.25</td></tr><tr><td>1710003</td><td>ECE 2205</td><td>4.00</td></tr><tr><td>1710003</td><td>ECE 2215</td><td>3.75</td></tr><tr><td>1710004</td><td>ECE 2205</td><td>3.50</td></tr><tr><td>1710004</td><td>ECE 2215</td><td>4.00</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>CREDIT</b><br><table border="1" style="border-collapse: collapse;"><thead><tr><th>sub_code</th><th>credit</th></tr></thead><tbody><tr><td>ECE 2205</td><td>3.00</td></tr><tr><td>ECE 2215</td><td>3.00</td></tr></tbody></table></td></tr></table>

(i) Write down the SQL query to create the table MARKS.  
(ii) Write down the SQL query to find out subject code and corresponding gpa of the student whose class serial 02.  
(iii) Write the the SQL query to calculate the cgpa of each student using the formula, $cgpa = \frac{\Sigma gpa \cdot credit}{\Sigma credit}$

*(Note: In the original printed question paper, Q.4 contains only sub-question (a) with 09 marks indicated in the margin, leaving a 3-mark deficit from the standard 12 marks).*

*(Sorting Note: Part iii calculates CGPA, cross-ref T05.5)*

**[2018 · Q.7(a) | 04 Marks | Sec B]**  
Write down the SQL queries for following operations.  
(i) Create table for student (<u>roll</u>, Name, <u>Dept</u>)  
(ii) Insert one example entry for student table  
(iii) Modify the student table to student(<u>roll</u>, Name, dept, session)  
(iv) Show the roll and name of the students of ECE department only.

**[2019 · Q.5(c) | 02 Marks | Sec B]**  
Write down the SQL queries to create the following tables.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

*(Note: Printed as "SQI." and "Parient_ID" in original question paper)*

**[2021 · Q.3(a) | 08 Marks | Sec A | CLO2]**  
Consider the following E-comerce database:  
  client (<u>c_no</u>, name, city, state, baldue)  
  product (<u>p_no</u>, description, profit_percent, quantity, sell_price, cost_price)  
  salesman (<u>s_no</u>, name, city, state, sal_amount, target, sold_yearly, remarks)

Now write the appropriate MySql code to execute the following query:  
(i) Change the city of client no "C0005" to "Barishal".  
(ii) Delete all salesmen whose salaries are equal to 35000 Tk.  
(iii) Add a column called "Telephone" of datatype numeric and size = '11' to the client table.  
(iv) Find products whose selling price is more than 500. Calculate a new selling price as original price*15. Rename the new column in the output as new_price.

*(Note: "E-comerce" and "MySql" printed verbatim from original question paper)*

*(Sorting Note: Part iv uses `AS` column rename, cross-ref T05.3)*

**[2023 · Q.3(a) | 06 Marks | Sec A | CLO2]**  
Write SQL queries for the following:  
(i) Create a table "Employee" with attributes: EmpID (primary key), Name, Age and Department.  
(ii) Insert a record into this table: EmpID=1, Name='Nafisa', Age=21, department='HR'.  
(iii) Find employees whose salary is greater than the average salary of their department.

*(Sorting Note: Part iii is a correlated subquery, cross-ref T05.6)*

**[2024 · Q.4(b) | 04 Marks | Sec A | CO2]**  
Write down the SQL queries for following operations:  
i) Create table for student (<u>roll</u>, name, dept)  
ii) Insert one example entry for student tbale  
iii) Modify the student table to student (roll, name, dept, session)  
iv) Show the roll and name of the students of ECE dept only.  
*(Note: "tbale" printed verbatim in original paper; refers to table)*

**[CT-02 · Q.01(a) | 02 Marks | CO2]**  
Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(a)** Display all students from the ECE department.

### T05.3 — Basic query clauses: `DISTINCT`, `ORDER BY`, `AS`, `LIKE` (finals counted in T05.5/5.8) · `0m` Finals (0) + `2m` CTs (1) · *D03 S14, S17–24*

**[CT-02 · Q.01(b) | 02 Marks | CO2]**  
Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(b)** Display students from the ECE department whose CGPA is greater than 3.50, arranged by CGPA in descending order.

> *Cross-ref:* Finals counted inside **T05.2 / T05.5 / T05.8**: **2019 Q.7(a)(ii)** (`LIKE 'A%'`, in **T05.5**), **2021 Q.3(a)(iv)** (`AS new_price`, in **T05.2**), and **2024 Q.7(b)(iii–iv)** (short notes on `Order By` and `As`, in **T05.8**).

### T05.4 — Aggregate functions (theory) · `7m` Finals (2) · *D03 S30–31*

**[2019 · Q.8(a) | 04 Marks | Sec B]**  
Discuss about four aggregate functions.

**[2024 · Q.7(a) | 03 Marks | Sec B | CO1]**  
Define aggregated functions.  
EMPLOYEE (EID, Name, Department, Salary)  
SALES (SID, EID, SaleAmount, SaleDate)  
The management wants to reward the top-earing department. Write a SQL query to find the total salary paid per department.  
*(Note: "top-earing" printed verbatim in original paper; refers to top-earning)*

*(Sorting Note: Also includes a `GROUP BY` query for total salary per department, cross-ref T05.5)*

### T05.5 — Aggregation queries: `GROUP BY` + `HAVING`, CGPA = $\Sigma(\text{gpa}\cdot\text{credit})/\Sigma\text{credit}$, extremes without `LIMIT` (min/max/2nd-highest) · `24m` Finals (3) + `3m` CTs (1) · *D03 S30–43, S51*

**[2018 · Q.7(b) | 08 Marks | Sec B]**  
Consider the following data tables:

`Product (p_id, p_name, quantity, unit_price)`  
`Customer (c_id, c_name, contact)`  
`Sales (c_id, p_id, quantity)`

Write down SQL expressions for following queries.  
(i) Show the information of those customers who have bought more than five different products.  
(ii) Show the information of those products that were sold more than ten pieces.  
(iii) Show the information of the product with maximum sale (maximum sold amount of money or bought by the maximum customer).  
(iv) Show the product id and corresponding remaining quantity of that product.

**[2019 · Q.7(a) | 12 Marks | Sec B]**  
Considering the following data tables (Student, GPA, Credits) answer (i), (ii), (iii), & (iv).

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Student</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>St Name</th></tr></thead><tbody><tr><td>2010001</td><td>Abdullah</td></tr><tr><td>2010002</td><td>Ahmad</td></tr><tr><td>2010003</td><td>Mohammad</td></tr><tr><td>2010004</td><td>Muaz</td></tr><tr><td>2010005</td><td>Minhaz</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>GPA</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>St_ID</th><th>Sub_Code</th><th>gpa</th></tr></thead><tbody><tr><td>2010001</td><td>ECE-1103</td><td>3.00</td></tr><tr><td>2010002</td><td>ECE-1107</td><td>3.25</td></tr><tr><td>2010004</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010005</td><td>ECE-1103</td><td>4.00</td></tr><tr><td>2010003</td><td>ECE-1107</td><td>3.75</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>Credit</b><br><table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>Sub_Code</th><th>Credit</th></tr></thead><tbody><tr><td>ECE-1103</td><td>3.00</td></tr><tr><td>ECE-1107</td><td>3.00</td></tr></tbody></table></td></tr></table>  
(i) Write down the SQL query to show the list of students who got the lowest gpa.  
(ii) Write down the SQL query to find out the registered subjects of those students whose name started with "A".  
(iii) Write the SQL query to calculate the cgpa of each student using the formula,

$\displaystyle cgpa = \frac{\sum gpa \cdot Credit}{\sum Credit}$

(iv) Generate a list showing each subject code and corresponding highest gpa.

*(Note: In sub-question (i), printed as "SQI." in original question paper)*

*(Sorting Note: Part ii uses `LIKE 'A%'`, cross-ref T05.3)*

**[2024 · Q.1(c) | 04 Marks | Sec A | CO2]**  
STUDENT (SID, Name, Age, Major)  
COURSE (CID, Title, Credits)  
ENROLLMENT (SID, CID, Grade)  
Using the above schema, write a SQL query to find the average grade for each course.

**[CT-02 · Q.01(d) | 03 Marks | CO2]**  
Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(d)** Display the students having the second-highest CGPA without using LIMIT.

> *Cross-ref:* **2017 Q.4(a)(iii)** (in **T05.2**'s 9m) asks for $cgpa = \frac{\Sigma gpa \cdot credit}{\Sigma credit}$; **2020 Q.3(b)(i)** (in **T05.7**'s 10m) uses `GROUP BY` + `HAVING AVG(Salary) > 30000`; **2024 Q.7(a)** (in **T05.4**'s 3m) asks for total salary paid per department.

### T05.6 — Subqueries theory ("two examples"): `IN`, `SOME/ALL`, `EXISTS`, scalar, correlated, `WITH` · `8m` Finals (2) + `3m` CTs (1) · *D03 S35–52*

**[2019 · Q.8(b) | 04 Marks | Sec B]**  
Write down two examples of using sub-queries.

**[2024 · Q.6(a) | 04 Marks | Sec B | CO2]**  
Explain sub-queries with two suitable examples.

**[CT-02 · Q.01(c) | 03 Marks | CO2]**  
Given $\text{STUDENT}(\text{StudentID}, \text{Name}, \text{Department}, \text{Semester}, \text{CGPA})$, write SQL query:  
**(c)** Find students whose CGPA is greater than the overall average CGPA.

> *Cross-ref:* **2023 Q.3(a)(iii)** (in **T05.2**'s 6m) asks for a correlated subquery (*salary > average salary of their department*).

### T05.7 — Multi-table business-schema query sets (MySQL): Covid, Company, Insurance, E-commerce · `44m` Finals (5) · *D03 S12–61, D04*

**[2019 · Q.5(b) | 08 Marks | Sec B]**  
Consider the following relational database.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

Now write down the SQL (Not Algebra) to find out the following queries.  
(i) Find the names of those patients who have-fever symptom.  
(ii) Consider that if any patient has high fever symptom he/she will be suspected as corona patient. Find out such maximum number of patients in a date.  
(iii) Find out the mobile numbers of those patients who have provided samples in Rajshahi corona center and their results have become positive.  
(iv) Find out the name of those patients who have high fever symptom but test result have become negative.

*(Note: In the physical question paper, SECTION-B heading and Q.5(a)–(b) appear at the bottom of Page 1; Q.5(c) continues at the top of Page 2)*  
*(Note: Printed as "Parient_ID" in Report schema in original question paper; refers to "Patient_ID")*

**[2020 · Q.3(b) | 10 Marks | Sec A]**  
Consider the following company database schema.  
  employee(<u>ssn</u>, fname, lname, DoB, Address, Sex, Salary, dept_no)  
  department(<u>dnumber</u>, dname, mgr_ssn, mgr_start_date)  
  dept_location(<u>dnumber</u>, <u>dlocation</u>)  
  project(<u>pnumber</u>, pname, dnum)  
  works_on(<u>essn</u>, <u>pno</u>, hours)  
  dependent(<u>essn</u>, <u>dependent_name</u>, Sex, DoB, relationship)  
Now write down the MySQL query for the followings.  
(i) For each department whose average salary is more than \$30,000, retrieve the department_name and the number of employees working for that department.  
(ii) Find the names of all employees who are working on project number "5" and are from the same department.  
(iii) Find the number of dependent people of those employees who are from "H&R" department.

**[2020 · Q.7(b) | 08 Marks | Sec B]**  
Define RDMS. Consider the following insurance database where the primary keys are underlined.  
  Person(<u>driver_id</u>, name, address)  
  Car(<u>license</u>, model, year)  
  Accident(<u>report_no</u>, date, location)  
  Owner(driver_id, license)  
  Participated(driver_id, report_no, car, damage_amount)  
Write MySQL for the following queries-  
(i) Find the number of accidents in which the cars belonging to "John Smith" were involved.  
(ii) Add a new accident to the database, assuming any values for required attributes.  
(iii) Update the car "Mazda" belonging to "John".  
(iv) Update the damage amounts \$3000 for the car with license number "YJK-100" in the accident with report number "APR2197".

*(Note: Printed as "RDMS" in original question paper; refers to "RDBMS")*

**[2021 · Q.4(a) | 12 Marks | Sec A | CLO2]**  
Consider the following E-comerce database:  
  client (<u>c_no</u>, name, city, state, Baldue)  
  product (<u>p_no</u>, description, profit_percent, quantity, sell_price, cost_price)  
  salesman (<u>s_no</u>, name, city, state, sal_amount, target, sold_yearly, remarks)  
  order (<u>order_no</u>, client_no, order_date, delivery_address, salesman_no, del_type, del_date, order_status)  
  order_details (<u>order_no</u>, product_no, quantity_ordered, product_rate)

(i) Find the total value of each product sold.  
(ii) Find the products and their quantities for the orders placed by client no "C0001" and "C0002".  
(iii) Find the product no and description of the products not being sold.  
(iv) Find if the product "Lyera Top" has been ordered by any client and print the client_no, name to whom it was sold.

*(Note: "E-comerce" and "Lyera Top" printed verbatim from original question paper)*

**[2024 · Q.5(b) | 06 Marks | Sec B | CO2]**  
Define RDMS. Consider the following insurance database where the primary keys are underlined.  
Person (<u>driver_id</u>, name, address)  
Car (<u>license</u>, model, year)  
Accident (<u>report_no</u>, data, location)  
Owner (driver_id, license)  
Participated (driver_id, report_no, car, damage_amount)  
Write MySQL for the following queries –  
i) Find the number of accidents in which the cars belonging to “John Smith” were involved.  
ii) Add a new accident to the database, assuming any values for required attributes.  
iii) Update the car “Mazda” belonging to “John”.  
iv) Update the damage amounts \$3000 for the car with license number “YJK-100” in the accident with report number “APR2197”.  
*(Note: "RDMS" and "data" printed verbatim in original paper; refers to RDBMS and date)*

### T05.8 — Short notes: `ON DELETE CASCADE`, `GROUP BY`, `ORDER BY`, `AS` · `10m` Finals (3) · *D03 S20–32 + Ch. 4 §4.4.5*

**[2019 · Q.8(c) | 04 Marks | Sec B]**  
Write short note on the following statements.  
(i) ON CASCADE DELETE.  
(ii) Group By.

**[2023 · Q.6(c) | 02 Marks | Sec B | CLO2]**  
Write short note on " ON CASCADE DELETE".

**[2024 · Q.7(b) | 04 Marks | Sec B | CO1]**  
Write short note on the following statements –  
i) ON CASCADE DELETE  
ii) Group By  
iii) Order By  
iv) As

*(Sorting Note: Parts iii–iv cover `ORDER BY` and `AS`, cross-ref T05.3)*

### T05.9 — `TRUNCATE` vs `DELETE` · `2m` Finals (1) · *Not in Silberschatz (answer from MySQL)*

**[2023 · Q.6(a) | 02 Marks | Sec B | CLO2]**  
What is the difference between 'Truncate' and 'Delete' in SQL?

---

## T06. Joins & Views
*Weightage: **28** Final Marks (`4.4%` · `4/7` Papers) · Syllabus Unit 4*

### T06.1 — Types of joins (inner/natural/theta, left/right/full outer, cross); inner vs outer · `11m` Finals (3) · *D04 S3–23*

**[2019 · Q.3(c) | 05 Marks | Sec A]**  
What is joining? Discuss each type of joining between two data tables with example.

**[2023 · Q.5(c) | 04 Marks | Sec B | CLO2]**  
Define joining. Discuss different types of joining with suitable example.

**[2024 · Q.3(c) | 02 Marks | Sec A | CO1]**  
Differentiate between inner joining and outer joining.

### T06.2 — Join outcome tables (natural/left/right/full on given data; MySQL has no `FULL OUTER JOIN` → `LEFT` $\cup$ `RIGHT`) · `11m` Finals (2) · *D04 S5–19*

**[2020 · Q.4(c) | 05 Marks | Sec A]**  
Consider the following tables:

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 25px;"><b>Courses</b><br><table border="1" style="border-collapse: collapse; text-align: center; margin-top: 4px;"><thead><tr><th style="padding: 3px 8px;">Code</th><th style="padding: 3px 8px;">Series</th><th style="padding: 3px 8px;">t code</th></tr></thead><tbody><tr><td>ECE 2215</td><td>2017</td><td>T1</td></tr><tr><td>ECE 4127</td><td>2016</td><td>T2</td></tr><tr><td>ECE 1203</td><td>2019</td><td>T3</td></tr><tr><td>ECE 2219</td><td>2017</td><td>T2</td></tr></tbody></table></td><td style="border: none;"><b>Teacher</b><br><table border="1" style="border-collapse: collapse; text-align: center; margin-top: 4px;"><thead><tr><th style="padding: 3px 8px;">t code</th><th style="padding: 3px 8px;">Designation</th></tr></thead><tbody><tr><td>T1</td><td>Head</td></tr><tr><td>T2</td><td>Professor</td></tr><tr><td>T3</td><td>Lecturer</td></tr><tr><td>T4</td><td>Lecturer</td></tr></tbody></table></td></tr></table>  
What will happen when the following actions will be performed on these two relations?  
(i) Natural Join  
(ii) Left Outer Join  
(iii) Right Outer Join  
(iv) Full Outer Join

**[2024 · Q.4(a) | 06 Marks | Sec A | CO2]**  
Consider the following tables:

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>Courses</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">Code</th><th style="padding: 4px 10px;">Series</th><th style="padding: 4px 10px;">t_code</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">E_2215</td><td style="padding: 4px 10px;">2020</td><td style="padding: 4px 10px;">T1</td></tr><tr><td style="padding: 4px 10px;">E_4127</td><td style="padding: 4px 10px;">2021</td><td style="padding: 4px 10px;">T2</td></tr><tr><td style="padding: 4px 10px;">E_1203</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">T3</td></tr><tr><td style="padding: 4px 10px;">E_2219</td><td style="padding: 4px 10px;">2021</td><td style="padding: 4px 10px;">T3</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>Teacher</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">t_code</th><th style="padding: 4px 10px;">Designation</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">T1</td><td style="padding: 4px 10px;">Head</td></tr><tr><td style="padding: 4px 10px;">T2</td><td style="padding: 4px 10px;">AP</td></tr><tr><td style="padding: 4px 10px;">T3</td><td style="padding: 4px 10px;">AP</td></tr><tr><td style="padding: 4px 10px;">T4</td><td style="padding: 4px 10px;">Lecturer</td></tr></tbody></table></td></tr></table>  
Discuss the outcome when the following actions will be performed on these two relations.  
i) Natural Join  
ii) Left Outer Join  
iii) Right Outer Join  
iv) Full Outer Join

### T06.3 — Outer-join algebra $\mathbin{⟕}, \mathbin{⟖}, \mathbin{⟗}$ · `0m` Finals (0) · *D04 S6, S8, S10, S20 · Ch. 4 §4.1, Ch. 16 §16.2*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Tested together with **T06.2** (`2020 Q.4(c)`, `2024 Q.4(a)`) when writing outer-join expressions.

### T06.4 — Views: benefits, `CREATE VIEW` over several tables · `6m` Finals (2) · *D04 S24–28*

**[2023 · Q.5(a) | 03 Marks | Sec B | CLO2]**  
What are the benefits of VIEW?

**[2023 · Q.5(b) | 03 Marks | Sec B | CLO2]**  
Create a VIEW using SQL query that shows the EmployeeName, DepartmentName and salary for employees who earn a salary of more than 55,000.

<table style="border: none; border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><tr style="border: none; vertical-align: top;"><td style="border: none; padding-right: 18px; vertical-align: top;"><b>E.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">EmployeeID</th><th style="padding: 4px 10px;">EmployeeName</th><th style="padding: 4px 10px;">Department ID</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">Jhon</td><td style="padding: 4px 10px;">D01</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">Jane</td><td style="padding: 4px 10px;">D02</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">Alice</td><td style="padding: 4px 10px;">D01</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">Bob</td><td style="padding: 4px 10px;">D03</td></tr></tbody></table></td><td style="border: none; padding-right: 18px; vertical-align: top;"><b>D.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">DepartmentID</th><th style="padding: 4px 10px;">DepartmentName</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">D01</td><td style="padding: 4px 10px;">Sales</td></tr><tr><td style="padding: 4px 10px;">D02</td><td style="padding: 4px 10px;">HR</td></tr><tr><td style="padding: 4px 10px;">D03</td><td style="padding: 4px 10px;">IT</td></tr></tbody></table></td><td style="border: none; vertical-align: top;"><b>S.</b><br><table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">EmployeeID</th><th style="padding: 4px 10px;">Salary</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">50,000</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">60,000</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">55,000</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">70,000</td></tr></tbody></table></td></tr></table>

### T06.5 — View expansion, updatable & materialized views · `0m` Finals (0) · *D04 S29–34*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

---

## T07. Triggers & Stored Procedures
*Weightage: **27** Final Marks (`4.2%` · `5/7` Papers) · Syllabus Unit 4*

### T07.1 — What a trigger is, its purposes, its syntax (ECA, `BEFORE/AFTER`, `FOR EACH ROW`) · `9m` Finals (2) · *Ch. 5 §5.3*

**[2018 · Q.8(a) | 05 Marks | Sec B]**  
What is triggering? What are the purposes of using trigger? Write the syntax for creating trigger?

**[2020 · Q.8(a) | 04 Marks | Sec B]**  
What is triggering? What are the purposes of using triggering? Write the syntax for creating a trigger.

### T07.2 — Triggers for security (before/after a breach) · `8m` Finals (2) · *Ch. 5 §5.3*

**[2017 · Q.8(b) | 05 Marks | Sec B]**  
Using examples, discuss how Trigger can contribute to the security of database, before and after a security breach.

**[2024 · Q.2(a) | 03 Marks | Sec A | CO2]**  
Discuss how trigger can contribute to the security of database before and after a security breach. Explain with example.

### T07.3 — Implement a trigger / stored procedure (place an order + audit log; order insert updates stock) · `10m` Finals (2) · *Ch. 5 §5.2–5.3*

**[2023 · Q.6(b) | 06 Marks | Sec B | CLO2]**  
Considering the tables (Products, Orders, and Auditlog) answer (i) and (ii).  
(i) Create a stored procedure to place an order consider stock availability, updates the stock.  
(ii) Create a trigger to log every stock update in the Auditlog table automatically.

**[2024 · Q.6(b) | 04 Marks | Sec B | CO3]**  
An e-commerce system wants to automate actions when a new order is inserted such as updating stock and sending email. Implement a database trigger that handles this workflow.

---

## T08. Normalization & Functional Dependencies
*Weightage: **75** Final Marks (`11.8%` · `7/7` Papers) + **20** CT Marks · Syllabus Unit 5*

### T08.1 — Why normalize: redundancy and insert/update/delete anomalies · `18m` Finals (4) + `3m` CTs (1) · *D06 S3–10*

**[2018 · Q.4(a) | 04 Marks | Sec A]**  
What problem may occur if databases are used without normalization? Discuss with proper example.

**[2019 · Q.6(a) | 06 Marks | Sec B]**  
Consider the following data tables.

**Student**  
<table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th>Roll</th><th>Name</th><th>Dept</th><th>Sub Code</th><th>Sub Grade</th><th>Reg Sub Code</th></tr></thead><tbody><tr><td>1710001</td><td>Mr. A</td><td>ECE</td><td>ECE-2103</td><td>A+</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710002</td><td>Mr. B</td><td>ECE</td><td>ECE-2107</td><td>A</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710003</td><td>Mr. C</td><td>ECE</td><td>ECE-2103</td><td>A-</td><td>ECE-2103</td></tr><tr><td>1710004</td><td>Mr. D</td><td>ECE</td><td>ECE-2107</td><td>A+</td><td>ECE-2107</td></tr><tr><td>1710001</td><td>Mr. A</td><td>ECE</td><td>ECE-2107</td><td>A-</td><td>ECE-2103<br>ECE-2107</td></tr><tr><td>1710002</td><td>Mr. B</td><td>ECE</td><td>ECE-2103</td><td>A+</td><td>ECE-2103<br>ECE-2107</td></tr></tbody></table>  
Now,  
(i) Carefully notice the entries and point out your opinion regarding space efficiency.  
(ii) What will happen if you update any particular information?  
(iii) What will happen if you are asked to delete 'ECE-2107' from the registered course list preserving all other information?

**[2021 · Q.6(c) | 04 Marks | Sec B | CLO1]**  
Consider the following table:

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;"><u>st_id</u></th><th style="padding: 4px 10px;">Name</th><th style="padding: 4px 10px;">Course</th><th style="padding: 4px 10px;">Session</th><th style="padding: 4px 10px;">Fee</th><th style="padding: 4px 10px;">Dept</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">101</td><td style="padding: 4px 10px;">Devi</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">102</td><td style="padding: 4px 10px;">Sona</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">103</td><td style="padding: 4px 10px;">Varun</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">104</td><td style="padding: 4px 10px;">Satish</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr><tr><td style="padding: 4px 10px;">105</td><td style="padding: 4px 10px;">Amisha</td><td style="padding: 4px 10px;">DBMS</td><td style="padding: 4px 10px;">2022</td><td style="padding: 4px 10px;">90k</td><td style="padding: 4px 10px;">CS</td></tr></tbody></table>  
Is there any data redundancy in the above table? What kinds of problems/ anomalities it will produce for this table in future?

*(Note: "problems/ anomalities" printed verbatim from original question paper)*

**[2023 · Q.2(b) | 04 Marks | Sec A | CLO4]**  
What are the anomalies that normalization aims to eliminate? Provide examples of insertion, deletion and update anomalies.

**[CT-03 · Q.02 | 03 Marks | CO3]**  
Mention the problems caused by an unnormalized relation.

> *Cross-ref:* **2017 Q.3(a)** (in **T08.6**) asks why normalization is important; **2020 Q.8(b)(i)** (in **T08.8**'s 8m) asks to identify anomalies; **CT-03 Q.03** (`03m`, in **T08.6**) asks for the main objective of normalization.

### T08.2 — FDs: trivial, full/partial, transitive; prime vs non-prime attributes · `0m` Finals (0) + `4m` CTs (1) · *D06 S14–17*

**[CT-03 · Q.01(b–c) | 04 Marks | CO3]**  
Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(b)** Identify the prime and non-prime attributes. `[02 Marks]`  
**(c)** Identify the partial and transitive dependencies. `[02 Marks]`

### T08.3 — Armstrong's axioms · `0m` Finals (0) · *D06 S18–24*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

### T08.4 — Attribute closure $X^+$, $F^+$, finding candidate keys · `4m` Finals (1) + `4m` CTs (1) · *D06 S25–29*

**[2021 · Q.5(b) | 04 Marks | Sec B | CLO1]**  
Compute the closure of the following set F of functional dependencies for relational schema r (A, B, C, D, E).

  $A \to BC$  
  $CD \to E$  
  $B \to D$  
  $E \to A$

List the candidate Keys for R.

**[CT-03 · Q.01(a) | 04 Marks | CO3]**  
Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(a)** Identify all the possible candidate key of the relation.

### T08.5 — Canonical cover $F_c$ (and how it differs from normalization) · `8m` Finals (2) · *Ch. 7 §7.4.3*

**[2021 · Q.6(a) | 03 Marks | Sec B | CLO1]**  
Differentiate between normalization and canonical cover in DBMS.

**[2021 · Q.6(b) | 05 Marks | Sec B | CLO1]**  
Define Functional dependency. Consider the following functional dependency set:

  $\text{FD} = \{$  
    $A \to BC,$  
    $CD \to E,$  
    $B \to D,$  
    $E \to A$  
  $\}$

Find the canonical form of the FD set.

### T08.6 — Define normalization (and its importance) & 1NF / 2NF / 3NF · `14m` Finals (4) + `3m` CTs (1) · *D06 S3–4, S30–40*

**[2017 · Q.3(a) | 03 Marks | Sec A]**  
What do you mean by normalization? Why normalization is important for database?

*(Sorting Note: Also asks why normalization is important, cross-ref T08.1 / T08.10)*

**[2017 · Q.8(c) | 03 Marks | Sec B]**  
What is 1NF, 2NF and 3NF?

**[2018 · Q.4(c) | 04 Marks | Sec A]**  
Explain the rules of 1NF and 2NF with a proper example.

**[2019 · Q.3(a) | 04 Marks | Sec A]**  
What is normalization? Discuss 1NF and 2NF.

**[CT-03 · Q.03 | 03 Marks | CO3]**  
Define normalization and state its main objective. *(Also cross-referenced in T08.1)*

### T08.7 — 2NF test from an FD set · `4m` Finals (1) · *D06 S31–36*

**[2021 · Q.5(c) | 04 Marks | Sec B | CLO1]**  
Given a relation R (A, B, C, D) and functional dependency at FD = { AB $\to$ CD, B $\to$ C }. Determine whether the given R is in 2NF? If not, convert it into 2NF.

*(Note: "functional dependency at FD" printed verbatim from original question paper)*

### T08.8 — Normalize an unnormalized table → 1NF → 2NF → 3NF · `27m` Finals (4) · *D06 S30–40*

**[2017 · Q.3(b) | 09 Marks | Sec A]**  
Consider the following data table com_employee. Is it already normalized? If not then normalize the table com_employee up to $3^{\text{rd}}$ normal form.

**com_employee**  
<table border="1" style="border-collapse: collapse;"><thead><tr><th>Pcode</th><th>Ptitle</th><th>EmpNo</th><th>EmName</th><th>EmCon</th><th>dNo</th><th>dName</th><th>HRate</th></tr></thead><tbody><tr><td>p1</td><td>Admission Test System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>1000</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1100</td></tr><tr><td>p1</td><td>Admission Test System</td><td>E4</td><td>James</td><td>508, 509</td><td>D3</td><td>HR</td><td>800</td></tr><tr><td>p2</td><td>Salary System</td><td>E1</td><td>Jones</td><td>501, 502</td><td>D1</td><td>IT</td><td>900</td></tr><tr><td>p2</td><td>Salary System</td><td>E3</td><td>Smith</td><td>505</td><td>D2</td><td>Database</td><td>1000</td></tr></tbody></table>

**[2020 · Q.8(b) | 08 Marks | Sec B]**  
Consider the given structure below:

<table border="1" cellpadding="4" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th style="padding: 3px 6px;">Proj. Num.</th><th style="padding: 3px 6px;">Proj. Name</th><th style="padding: 3px 6px;">Emp. No.</th><th style="padding: 3px 6px;">Emp. Name</th><th style="padding: 3px 6px;">Job Class</th><th style="padding: 3px 6px;">Chg/Hr</th><th style="padding: 3px 6px;">Hrs. Biller.</th><th style="padding: 3px 6px;">Total Charge</th></tr></thead><tbody><tr><td rowspan="2">13</td><td rowspan="2">Banking</td><td>103</td><td>John</td><td style="text-align: left;">Analyst</td><td>500</td><td>8</td><td>4000</td></tr><tr><td>105</td><td>Steve</td><td style="text-align: left;">Programmer</td><td>300</td><td>8</td><td>2400</td></tr><tr><td rowspan="2">26</td><td rowspan="2">Telecom</td><td>115</td><td>Jim</td><td style="text-align: left;">Business Analyst</td><td>100</td><td>10</td><td>1000</td></tr><tr><td>717</td><td>Joe</td><td style="text-align: left;">Engineer</td><td>300</td><td>7</td><td>2100</td></tr><tr><td rowspan="2">39</td><td rowspan="2">Finance</td><td>113</td><td>David</td><td style="text-align: left;">Team Leader</td><td>1000</td><td>4</td><td>4000</td></tr><tr><td>120</td><td>Jian</td><td style="text-align: left;">DBA</td><td>800</td><td>3</td><td>2400</td></tr></tbody></table>  
(i) Identify the anomalies in the given structure.  
(ii) Normalize it up to third Normal Form (3NF).

*(Note: In the original examination paper, "Hrs. Billed" is printed as "Hrs. Biller.", and the `Proj. Num.` and `Proj. Name` cells span both employee rows for each project)*

*(Sorting Note: Part i asks to identify anomalies, cross-ref T08.1)*

**[2023 · Q.2(a) | 06 Marks | Sec A | CLO4]**  
Consider a university tracking students, their courses and exam scores. A sample table is given below. Step by step convert this to 3NF.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 10px;">S_ID</th><th style="padding: 4px 10px;">S-Name</th><th style="padding: 4px 10px;">Courses</th><th style="padding: 4px 10px;">Instructors</th><th style="padding: 4px 10px;">Grades</th></tr></thead><tbody><tr><td style="padding: 4px 10px;">1</td><td style="padding: 4px 10px;">Alice</td><td style="padding: 4px 10px;">Math, Physics</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Brown</td><td style="padding: 4px 10px;">A, B+</td></tr><tr><td style="padding: 4px 10px;">2</td><td style="padding: 4px 10px;">Bob</td><td style="padding: 4px 10px;">Chemistry</td><td style="padding: 4px 10px;">Dr. White</td><td style="padding: 4px 10px;">A-</td></tr><tr><td style="padding: 4px 10px;">3</td><td style="padding: 4px 10px;">Charlie</td><td style="padding: 4px 10px;">Math, Biology, Chemistry</td><td style="padding: 4px 10px;">Dr. Smith, Dr. Gray, Dr. White</td><td style="padding: 4px 10px;">B+, A-, A</td></tr></tbody></table>

**[2024 · Q.3(a) | 04 Marks | Sec A | CO2]**  
A library database stores information about Books, Authors, Publishers and Borrowers. Create a table that contains some data redundancy and partial dependencies. Also, show the procedure to normalize the table.

### T08.9 — BCNF; 3NF vs BCNF; highest normal form · `0m` Finals (0) + `6m` CTs (2) · *D06 S41–46*

**[CT-03 · Q.01(d) | 02 Marks | CO3]**  
Consider $\text{ENROLLMENT}(\text{StudentID}, \text{StudentName}, \text{CourseID}, \text{CourseName}, \text{InstructorID}, \text{InstructorName}, \text{Grade})$ with functional dependencies: $\text{StudentID} \rightarrow \text{StudentName}$; $\text{CourseID} \rightarrow \text{CourseName}, \text{InstructorID}$; $\text{InstructorID} \rightarrow \text{InstructorName}$; $(\text{StudentID}, \text{CourseID}) \rightarrow \text{Grade}$.  
**(d)** Determine the highest normal form satisfied by the given relation. Give a proper justification.

**[CT-03 · Q.04 | 04 Marks | CO3]**  
Justify the statement: "Every BCNF relation is in 3NF, but every 3NF relation is not necessarily in BCNF."

### T08.10 — Pros/cons of normalization; denormalization · `0m` Finals (0) · *D06 S47–51*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Importance/pros of normalization asked in **2017 Q.3(a)** (counted in **T08.6**); cons and denormalization have never been asked in a final.

### T08.11 — Lossless-join decomposition & dependency preservation · `0m` Finals (0) · *D06 S52–62*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

---

## T09. Transactions, ACID & Anomalies
*Weightage: **41** Final Marks (`6.4%` · `7/7` Papers) + **14** CT Marks · Syllabus Unit 6*

### T09.1 — ACID properties (with the \$50 transfer example/diagram) · `18m` Finals (5) + `6m` CTs (1) · *D07 S3–7*

**[2017 · Q.5(a) | 04 Marks | Sec B]**  
Briefly discuss the ACID properties of transaction.

**[2018 · Q.4(b) | 04 Marks | Sec A]**  
Describe the ACID-properties of database system with appropriate diagram.

**[2021 · Q.7(a) | 04 Marks | Sec B | CLO1]**  
Explain the ACID properties of transaction.

**[2023 · Q.4(b) | 04 Marks | Sec A | CLO3]**  
Briefly explain the importance of ACID properties of transactions with suitable example.

**[2024 · Q.6(c) | 02 Marks | Sec B | CO3]**  
Briefly discuss the ACID properties of transaction.

**[CT-04 · Q.01 | 06 Marks | CO3]**  
Define a transaction? Explain the four ACID properties of a transaction with suitable examples.

### T09.2 — Consistency property alone, with example · `6m` Finals (2) · *D07 S6*

**[2019 · Q.3(b) | 03 Marks | Sec A]**  
Explain the consistency property of a database system with a proper example.

**[2024 · Q.2(c) | 03 Marks | Sec A | CO1]**  
Explain the consistency property of a database system with a proper example.

### T09.3 — Transaction states / life-cycle diagram · `6m` Finals (2) · *D07 S8–9*

**[2020 · Q.5(b) | 04 Marks | Sec B]**  
What is a transaction? Describe the life cycle of a transaction.

**[2023 · Q.4(c) | 02 Marks | Sec A | CLO3]**  
Draw state diagram of a transaction.

### T09.4 — Concurrent execution: advantages; serial vs concurrent vs serializable schedules · `4m` Finals (1) + `4m` CTs (1) · *D07 S10–15*

**[2018 · Q.6(a) | 04 Marks | Sec B]**  
Define transaction and schedule. What is the difference between serial schedule and serializable schedule?

**[CT-04 · Q.02 | 04 Marks | CO3]**  
Differentiate between a serial schedule and a concurrent schedule. Mention two advantages of concurrent execution of transactions.

### T09.5 — Concurrency problems (dirty read, lost update, unrepeatable read, phantom, incorrect summary) · `7m` Finals (2) + `4m` CTs (1) · *D07 S28–33*

**[2018 · Q.5(a) | 04 Marks | Sec B]**  
If concurrency-control management is not implemented properly what problem may occur? Explain with example.

**[2024 · Q.8(a) | 03 Marks | Sec B | CO3]**  
If concurrency-control management is not implemented properly what problem may occur? Explain with example.

**[CT-04 · Q.03 | 04 Marks | CO3]**  
Explains any two problems caused by concurrent execution. *(Note: Printed verbatim in original script)*.

---

## T10. Serializability
*Weightage: **51** Final Marks (`8.0%` · `7/7` Papers) + **06** CT Marks · Syllabus Unit 6*

### T10.1 — Define conflicting instructions & conflict serializability · `2m` Finals (1) · *D07 S16–19*

**[2017 · Q.5(b) | 02 Marks | Sec B]**  
What do you know about conflict serializability?

> *Cross-ref:* **2021 Q.7(b)** (`04m`, in **T10.3**) opens with *"Define conflict serializability."*

### T10.2 — Conflict equivalence by swapping (proof) · `4m` Finals (1) · *D07 S19–20*

**[2020 · Q.5(c) | 04 Marks | Sec B]**  
Draw a concurrent schedule equivalent to serial schedule. Prove its step by step swapping process.

### T10.3 — Precedence-graph test → cycle → serial order(s) · `26m` Finals (6) + `6m` CTs (1) · *D07 S18–21, S25–26*

**[2018 · Q.6(c) | 04 Marks | Sec B]**  
Consider the following schedule.

<table border="1" cellpadding="4" style="border-collapse: collapse; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th style="padding: 4px 20px; text-align: center;">T<sub>1</sub></th><th style="padding: 4px 20px; text-align: center;">T<sub>2</sub></th></tr></thead><tbody><tr><td style="padding: 3px 12px;">read(A);</td><td></td></tr><tr><td style="padding: 3px 12px;">A:=A+10;</td><td></td></tr><tr><td></td><td style="padding: 3px 12px;">read(A);</td></tr><tr><td></td><td style="padding: 3px 12px;">A:=A-100;</td></tr><tr><td></td><td style="padding: 3px 12px;">write(A);</td></tr><tr><td></td><td style="padding: 3px 12px;">read(B);</td></tr><tr><td style="padding: 3px 12px;">write(A);</td><td></td></tr><tr><td style="padding: 3px 12px;">read(B);</td><td></td></tr><tr><td style="padding: 3px 12px;">B:=B-10;</td><td></td></tr><tr><td style="padding: 3px 12px;">write(B)</td><td></td></tr><tr><td></td><td style="padding: 3px 12px;">B:=B+100;</td></tr><tr><td></td><td style="padding: 3px 12px;">write(B);</td></tr></tbody></table>  
Determine whether the schedule is conflict serializable or not?

**[2020 · Q.6(a) | 06 Marks | Sec B]**  
Which of the following schedule is (conflict) serializable? For each serializable schedule, determine the equivalent serial schedules.  
(i) $r_1(X);\, r_3(X);\, w_1(X);\, r_2(X);\, w_3(X)$  
(ii) $r_1(X);\, r_3(X);\, w_3(X);\, w_1(X);\, r_2(X)$

**[2021 · Q.7(b) | 04 Marks | Sec B | CLO3]**  
Define conflict serializability. Check whether the following schedule is a conflict serializable or not.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 20px;">$T_1$</th><th style="padding: 4px 20px;">$T_2$</th></tr></thead><tbody><tr><td style="padding: 4px 20px;">read(A)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">write(A)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">read(A)</td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">write(A)</td></tr><tr><td style="padding: 4px 20px;">read(B)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">write(B)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">read(B)</td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">write(B)</td></tr></tbody></table>

*(Sorting Note: First sentence asks to define conflict serializability, cross-ref T10.1)*

**[2021 · Q.7(c) | 04 Marks | Sec B | CLO3]**  
Consider the following schedule:

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 20px;">$T_1$</th><th style="padding: 4px 20px;">$T_2$</th></tr></thead><tbody><tr><td style="padding: 4px 20px;">r(A)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">w(A)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">r(B)</td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">w(B)</td></tr><tr><td style="padding: 4px 20px;">r(B)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">w(B)</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">r(A)</td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">w(A)</td></tr></tbody></table>  
Using precedence graph find whether the schedule is serializable or not. If serializable, then find the order of execution.

**[2023 · Q.8(b) | 04 Marks | Sec B | CLO3]**  
Check whether the given schedules S is conflict serializeable or not. If yes, then determine all the possible serialized schedules.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 20px;">$T_1$</th><th style="padding: 4px 20px;">$T_2$</th><th style="padding: 4px 20px;">$T_3$</th><th style="padding: 4px 20px;">$T_4$</th></tr></thead><tbody><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(A)$</td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(A)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">$W(B)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(A)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(A)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(B)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(B)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr></tbody></table>  
*(Note: "schedules S is conflict serializeable" printed verbatim from original question paper)*

**[2024 · Q.8(c) | 04 Marks | Sec B | CO3]**  
Consider the following schedule:

<table border="1" style="border-collapse: collapse; text-align: left;"><thead><tr><th style="text-align: center; padding: 4px 14px;">$T_1$</th><th style="text-align: center; padding: 4px 14px;">$T_2$</th></tr></thead><tbody><tr><td style="padding: 4px 14px;">read (A);<br>A=A+10;</td><td style="padding: 4px 14px;"></td></tr><tr><td style="padding: 4px 14px;"></td><td style="padding: 4px 14px;">read (A);<br>A=A-100;<br>write (A);<br>read (B);</td></tr><tr><td style="padding: 4px 14px;">write (A);<br>read (B);<br>B=B-10;<br>write (B);</td><td style="padding: 4px 14px;"></td></tr><tr><td style="padding: 4px 14px;"></td><td style="padding: 4px 14px;">B=B+100;<br>write (B);</td></tr></tbody></table>  
Determine whether the schedule is conflict serializable or not.

**[CT-04 · Q.04 | 06 Marks | CO3]**  
Determine whether the schedule is conflict serializable or not. If it is serializable, give the equivalent serial order.

| $T_1$ | $T_2$ | $T_3$ |
| :---: | :---: | :---: |
| $\text{Write}(A)$ | | |
| | $\text{Read}(A)$ | |
| | | $\text{Write}(B)$ |
| $\text{Write}(B)$ | | |
| | | $\text{Write}(B)$ |
| | $\text{Write}(A)$ | |
| | | $\text{Read}(B)$ |
| | $\text{Read}(B)$ | |

### T10.4 — Build serializable/non-serializable schedules ($T_1,T_2$ with "if A = 0 then B := B+1") · `13m` Finals (2) · *D07 S10–21*

**[2017 · Q.5(c) | 06 Marks | Sec B]**  
Consider the following two transactions.

**T1:**  
  `read(A);`  
  `read(B);`  
  `if A = 0 then B:=B+1;`  
  `write(B);`

**T2:**  
  `read(B);`  
  `read(A);`  
  `if B = 0 then A:=A+1;`  
  `write(A);`

Let the consistency requirement be $A = 0$ or $B = 0$ with $A=B=0$ the initial values.  
(i) Show a concurrent execution of T1 and T2 that produces a nonserializable schedule.  
(ii) Is there a concurrent execution of T1 and T2 that produces a serializable schedule?

**[2019 · Q.4(a) | 07 Marks | Sec A]**  
What is concurrency control? Consider the following two transactions.

**T1:**  
`read (P);`  
`read (Q);`  
`if P=10 then Q:=Q-5;`  
`write (Q);`

**T2:**  
`read (Q);`  
`read (P);`  
`if Q=10 then P:=P+5;`  
`write (P);`

Let the consistency requirement be P=5 or Q=5 with P=Q=5 the initial values.  
(i) Show a concurrent execution of T1 and T2 that produces a serializable schedule.  
(ii) Is there a concurrent execution of T1 and T2 that produces a serializable schedule?

*(Note: In the printed question paper, sub-question (ii) is printed identically to (i) as "Is there a concurrent execution of T1 and T2 that produces a serializable schedule?")*

### T10.5 — View serializability (3 conditions, blind writes) · `6m` Finals (1) · *D07 S22–23, S27*

**[2020 · Q.6(b) | 06 Marks | Sec B]**  
What is view serializability? Why do we need view serializability? Check the view serializability of the following schedule if any.

<table border="1" style="border-collapse: collapse; text-align: center; margin-top: 6px; margin-bottom: 6px;"><thead><tr><th style="padding: 4px 20px;">T<sub>1</sub></th><th style="padding: 4px 20px;">T<sub>2</sub></th></tr></thead><tbody><tr><td style="padding: 3px 12px;">R(X)</td><td style="padding: 3px 12px;"></td></tr><tr><td style="padding: 3px 12px;">W(X)</td><td style="padding: 3px 12px;"></td></tr><tr><td style="padding: 3px 12px;"></td><td style="padding: 3px 12px;">R(X)</td></tr><tr><td style="padding: 3px 12px;"></td><td style="padding: 3px 12px;">W(X)</td></tr><tr><td style="padding: 3px 12px;">R(Y)</td><td style="padding: 3px 12px;"></td></tr><tr><td style="padding: 3px 12px;">W(Y)</td><td style="padding: 3px 12px;"></td></tr><tr><td style="padding: 3px 12px;"></td><td style="padding: 3px 12px;">R(Y)</td></tr><tr><td style="padding: 3px 12px;"></td><td style="padding: 3px 12px;">W(Y)</td></tr></tbody></table>

### T10.6 — Recoverable / cascadeless / strict schedules · `0m` Finals (0) · *D08 S3–8*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

---

## T11. Concurrency Control Protocols
*Weightage: **37** Final Marks (`5.8%` · `6/7` Papers) · Syllabus Unit 6*

### T11.1 — Lock-based protocols: shared/exclusive locks, compatibility matrix, starvation · `0m` Finals (0) · *D08 S9–12*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* **2017 Q.7(a)** (`05m`, in **T11.2**) opens with *"What is starvation?"*

### T11.2 — Two-phase locking: growing/shrinking phases, lock point, inserting lock/unlock instructions · `9m` Finals (2) · *D08 S13–18*

**[2017 · Q.6(b) | 04 Marks | Sec B]**  
How concurrent execution of transactions are controlled using two phase based locking protocol? Briefly discuss with an example.

**[2017 · Q.7(a) | 05 Marks | Sec B]**  
What is starvation? Consider the following two transactions.

**T1:**  
  `read(A);`  
  `read(B);`  
  `if A = 0 then B:=B+15% of B;`  
  `write(B);`

**T2:**  
  `read(B);`  
  `read(A);`  
  `if B = 0 then A:=A+20% of A;`  
  `write(A);`

Add lock and unlock instructions to transaction T1 and T2, so that they observe the two phase locking protocol. Can the execution of these transactions result in a deadlock? Justify.

*(Sorting Note: Also asks what starvation is, cross-ref T11.1, and whether deadlock can occur, cross-ref T11.4)*

> *Cross-ref:* **2020 Q.7(a)** (`04m`, in **T11.4**) asks in its second half: *"Describe the time-shared locking protocol with example"* (misprint for 2PL).

### T11.3 — Strict / rigorous 2PL; drawbacks of 2PL · `0m` Finals (0) · *D08 S16–19*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

### T11.4 — Deadlock: conditions, prevention vs detection, wait-for graph, victim selection · `17m` Finals (4) · *D08 S20–25*

**[2017 · Q.7(b) | 04 Marks | Sec B]**  
Define deadlock. Explain how deadlock is prevented?

**[2018 · Q.5(b) | 04 Marks | Sec B]**  
What do you know about deadlock in transaction management? Under what conditions it is less expensive to avoid deadlock than to allow deadlocks to occur and then to detect them?

**[2020 · Q.7(a) | 04 Marks | Sec B]**  
What is deadlock? Describe the time-shared locking protocol with example.

*(Sorting Note: Second part asks for "time-shared locking protocol" [misprint for 2PL, cross-ref T11.2])*

**[2021 · Q.8(a) | 05 Marks | Sec B | CLO1]**  
What is deadlock? Consider the following wait-for-graph:

![Wait-for-graph for Q.8(a)](PreviousYearQuestion/diagrams/2021_p02_fig01.jpg)  
*Figure 2021_Q8.a — Wait-for-graph for deadlock detection (Source: Page 2, Q.8(a))*

Determine whether the schedule contains any deadlock or not.

*(Refer to the Wait-for-Graph Diagram and Detailed Text Representation below)*

> *Cross-ref:* **2017 Q.7(a)** (`05m`, in **T11.2**) asks at the end: *"Can the execution of these transactions result in a deadlock? Justify."*

> *Wait-for-Graph Details (`2021 Q.8(a)`):* Vertices $V = \{T_1, T_2, T_3, T_4, T_5\}$; Directed edges $E = \{(T_1, T_4), (T_1, T_2), (T_1, T_3), (T_4, T_5), (T_5, T_2), (T_2, T_4)\}$; Cycle $T_4 \to T_5 \to T_2 \to T_4 \implies$ **Deadlock**.

### T11.5 — Wait-die vs wound-wait · `0m` Finals (0) · *D08 S23*

*No direct standalone question in past finals or CTs (taught in slides/textbook — high-yield candidate).*

> *Cross-ref:* Covered as part of deadlock prevention in **2017 Q.7(b)** (`04m`, in **T11.4**); never asked by name (`wait-die` / `wound-wait`).

### T11.6 — Timestamp ordering: R-TS/W-TS rules, trace a schedule; rolled-back transaction gets a NEW timestamp · `11m` Finals (3) · *D08 S26–30 + Ch. 18 §18.5*

**[2018 · Q.6(b) | 04 Marks | Sec B]**  
When a transaction is rolled back under timestamp ordering and it is assigned a new timestamp? Why can it not simply keep its old timestamp?

**[2023 · Q.8(c) | 04 Marks | Sec B | CLO3]**  
Discuss the given schedule based on Timestamp ordering protocol.

<table border="1" style="border-collapse: collapse; text-align: center;"><thead><tr><th style="padding: 4px 20px;">$T_1(100)$</th><th style="padding: 4px 20px;">$T_2(200)$</th><th style="padding: 4px 20px;">$T_3(300)$</th></tr></thead><tbody><tr><td style="padding: 4px 20px;">$R(A)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(B)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;">$W(C)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$R(B)$</td></tr><tr><td style="padding: 4px 20px;">$R(C)$</td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(B)$</td><td style="padding: 4px 20px;"></td></tr><tr><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;"></td><td style="padding: 4px 20px;">$W(A)$</td></tr></tbody></table>  
*(Note: In the original paper schedule, $W(C)$ of $T_1$ and $R(B)$ of $T_3$ occupy essentially the same vertical tier. Since $C$ and $B$ are disjoint data items, the concurrency protocol evaluation remains unaffected).*

**[2024 · Q.8(b) | 03 Marks | Sec B | CO3]**  
When a transaction is rolled back under timestamp ordering and it is assigned a new timestamp? Why can it not simply keep its old timestamp?

---

## T12. Recovery System & RAID
*Weightage: **43** Final Marks (`6.8%` · `5/7` Papers) · Syllabus Unit 7*

### T12.1 — Failure classification, precautions, recovery methods · `17m` Finals (5) · *Ch. 19 §19.1*

**[2017 · Q.6(c) | 03 Marks | Sec B]**  
Classify and discuss the failures in DBMS.

**[2018 · Q.5(c) | 02/04 Marks | Sec B]**  
Discuss each type of failure that can happen in DBMS. How does RAID model help to recover a system?

*(Sorting Note: 4-mark question split 2 + 2 with T12.4: DBMS failures = 2m, RAID recovery = 2m)*

**[2019 · Q.4(b) | 05 Marks | Sec A]**  
How many ways a DBMS could be failed? What precautions should be taken considering the failure of DBMS and point out the recovery methods.

**[2023 · Q.7(a) | 03 Marks | Sec B | CLO2]**  
Explain the different types of failures that can occur in a database system.

**[2024 · Q.3(b) | 04 Marks | Sec A | CO1]**  
Discuss the ways of DBMS can be failed. Also, mention the precautions should be taken considering the failure of DBMS and point out the recovery methods.

### T12.2 — Role of the recovery manager (could a never-failing DB skip it?) · `4m` Finals (1) · *Ch. 17 §17.1, Ch. 19*

**[2018 · Q.8(b) | 04 Marks | Sec B]**  
Suppose that there is a database system that never failed, is a recovery manager required for this system? Justify your answer.

### T12.3 — Log-based recovery: WAL, undo/redo, checkpoints, crash example; shadow paging · `7m` Finals (2) · *Ch. 19 §19.3–19.4, Note 19.1*

**[2017 · Q.6(d) | 03 Marks | Sec B]**  
Discuss shortly the log-based recovery approach to ensure atomicity despite of failures of DBMS.

**[2023 · Q.7(b) | 04 Marks | Sec B | CLO2]**  
What is log based recovery? Illustrate with an example of a system crash and recovery process.

### T12.4 — RAID levels, comparing levels, RAID's role in recovery · `15m` Finals (5) · *Ch. 12 §12.5*

**[2018 · Q.5(c) | 02/04 Marks | Sec B]**  
Discuss each type of failure that can happen in DBMS. How does RAID model help to recover a system?

*(Sorting Note: 4-mark question split 2 + 2 with T12.1: DBMS failures = 2m, RAID recovery = 2m)*

**[2018 · Q.8(c) | 03 Marks | Sec B]**  
Describe the different RAID levels.

**[2023 · Q.4(a) | 04 Marks | Sec A | CLO1]**  
Discuss the features of RAID models.

**[2023 · Q.7(c) | 03 Marks | Sec B | CLO2]**  
Briefly describe the RAID model and its significance in database recovery.

**[2024 · Q.7(c) | 03 Marks | Sec B | CO3]**  
A multimedia archive contains very large image and video files. RAID is recommended for storage. Compare different RAID levels.

---

## T13. Security, Indexing & Hashing
*Weightage: **18** Final Marks (`2.8%` · `4/7` Papers) · Syllabus Unit 8*

### T13.1 — Database security threats; authorization · `4m` Finals (1) · *Ch. 9 §9.8, Ch. 4 §4.7*

**[2017 · Q.8(a) | 04 Marks | Sec B]**  
Describe four of the main threats to database security.

### T13.2 — SQL injection: how it works + prevention · `9m` Finals (2) · *Ch. 9 §9.8.1*

**[2020 · Q.4(a) | 04 Marks | Sec A]**  
What is an SQL injection attack? Explain how it works and what precautions must be taken to prevent SQL injection attack.

**[2021 · Q.8(b) | 05 Marks | Sec B | CLO4]**  
What is SQL injection attack? Describe the precautions that should be taken to prevent this attack.

### T13.3 — Indexing: dense vs sparse index (B+-tree as background) · `2m` Finals (1) · *Ch. 14 §14.2–14.3*

**[2023 · Q.8(a) | 02 Marks | Sec B | CLO1]**  
Write short note on dense and sparse index.

### T13.4 — Hashing: static vs dynamic · `3m` Finals (1) · *Ch. 14 §14.5, Ch. 24 §24.5*

**[2017 · Q.7(c) | 03 Marks | Sec B]**  
What is hashing? Differentiate between static and dynamic hashing.

---

## Quick Verification Index (All 148 Final Sub-Questions + 15 CT Questions)

- **2017** *(21 sub-Qs · 93m)*: **Q.1(a)** (04m) → `T01.2` · **Q.1(b)** (06m) → `T02.5` · **Q.1(c)** (02m) → `T01.3` · **Q.2(a)** (08m) → `T04.2` · **Q.2(b)** (04m) → `T01.4` · **Q.3(a)** (03m) → `T08.6` · **Q.3(b)** (09m) → `T08.8` · **Q.4(a)** (09m) → `T05.2` · **Q.5(a)** (04m) → `T09.1` · **Q.5(b)** (02m) → `T10.1` · **Q.5(c)** (06m) → `T10.4` · **Q.6(a)** (02m) → `T02.7` · **Q.6(b)** (04m) → `T11.2` · **Q.6(c)** (03m) → `T12.1` · **Q.6(d)** (03m) → `T12.3` · **Q.7(a)** (05m) → `T11.2` · **Q.7(b)** (04m) → `T11.4` · **Q.7(c)** (03m) → `T13.4` · **Q.8(a)** (04m) → `T13.1` · **Q.8(b)** (05m) → `T07.2` · **Q.8(c)** (03m) → `T08.6`
- **2018** *(23 sub-Qs · 96m)*: **Q.1(a)** (03m) → `T01.2` · **Q.1(b)** (04m) → `T02.4` · **Q.1(c)** (05m) → `T02.5` · **Q.2(a)** (04m) → `T03.2` · **Q.2(b)** (03m) → `T02.8` · **Q.2(c)** (05m) → `T02.6` · **Q.3(a)** (06m) → `T04.2` · **Q.3(b)** (02m) → `T03.1` · **Q.3(c)** (04m) → `T02.3` · **Q.4(a)** (04m) → `T08.1` · **Q.4(b)** (04m) → `T09.1` · **Q.4(c)** (04m) → `T08.6` · **Q.5(a)** (04m) → `T09.5` · **Q.5(b)** (04m) → `T11.4` · **Q.5(c)** (04m) → `T12.1`(2m)+`T12.4`(2m) · **Q.6(a)** (04m) → `T09.4` · **Q.6(b)** (04m) → `T11.6` · **Q.6(c)** (04m) → `T10.3` · **Q.7(a)** (04m) → `T05.2` · **Q.7(b)** (08m) → `T05.5` · **Q.8(a)** (05m) → `T07.1` · **Q.8(b)** (04m) → `T12.2` · **Q.8(c)** (03m) → `T12.4`
- **2019** *(19 sub-Qs · 96m)*: **Q.1(a)** (03m) → `T01.2` · **Q.1(b)** (03m) → `T02.4` · **Q.1(c)** (06m) → `T02.5` · **Q.2(a)** (04m) → `T01.4` · **Q.2(b)** (08m) → `T04.2` · **Q.3(a)** (04m) → `T08.6` · **Q.3(b)** (03m) → `T09.2` · **Q.3(c)** (05m) → `T06.1` · **Q.4(a)** (07m) → `T10.4` · **Q.4(b)** (05m) → `T12.1` · **Q.5(a)** (02m) → `T05.1` · **Q.5(b)** (08m) → `T05.7` · **Q.5(c)** (02m) → `T05.2` · **Q.6(a)** (06m) → `T08.1` · **Q.6(b)** (06m) → `T03.2` · **Q.7(a)** (12m) → `T05.5` · **Q.8(a)** (04m) → `T05.4` · **Q.8(b)** (04m) → `T05.6` · **Q.8(c)** (04m) → `T05.8`
- **2020** *(20 sub-Qs · 96m)*: **Q.1(a)** (05m) → `T01.3` · **Q.1(b)** (03m) → `T01.7` · **Q.1(c)** (04m) → `T02.3` · **Q.2(a)** (06m) → `T04.2` · **Q.2(b)** (04m) → `T03.2` · **Q.2(c)** (02m) → `T02.4` · **Q.3(a)** (02m) → `T02.8` · **Q.3(b)** (10m) → `T05.7` · **Q.4(a)** (04m) → `T13.2` · **Q.4(b)** (03m) → `T04.5` · **Q.4(c)** (05m) → `T06.2` · **Q.5(a)** (04m) → `T02.2` · **Q.5(b)** (04m) → `T09.3` · **Q.5(c)** (04m) → `T10.2` · **Q.6(a)** (06m) → `T10.3` · **Q.6(b)** (06m) → `T10.5` · **Q.7(a)** (04m) → `T11.4` · **Q.7(b)** (08m) → `T05.7` · **Q.8(a)** (04m) → `T07.1` · **Q.8(b)** (08m) → `T08.8`
- **2021** *(21 sub-Qs · 96m)*: **Q.1(a)** (04m) → `T01.2` · **Q.1(b)** (03m) → `T01.3` · **Q.1(c)** (05m) → `T03.3` · **Q.2(a)** (05m) → `T04.2` · **Q.2(b)** (03m) → `T03.2` · **Q.2(c)** (04m) → `T04.3` · **Q.3(a)** (08m) → `T05.2` · **Q.3(b)** (04m) → `T02.2` · **Q.4(a)** (12m) → `T05.7` · **Q.5(a)** (04m) → `T02.1` · **Q.5(b)** (04m) → `T08.4` · **Q.5(c)** (04m) → `T08.7` · **Q.6(a)** (03m) → `T08.5` · **Q.6(b)** (05m) → `T08.5` · **Q.6(c)** (04m) → `T08.1` · **Q.7(a)** (04m) → `T09.1` · **Q.7(b)** (04m) → `T10.3` · **Q.7(c)** (04m) → `T10.3` · **Q.8(a)** (05m) → `T11.4` · **Q.8(b)** (05m) → `T13.2` · **Q.8(c)** (02m) → `T02.4`
- **2023** *(22 sub-Qs · 80m)*: **Q.1(a)** (05m) → `T02.5` · **Q.1(b)** (03m) → `T01.2` · **Q.1(c)** (02m) → `T01.5` · **Q.2(a)** (06m) → `T08.8` · **Q.2(b)** (04m) → `T08.1` · **Q.3(a)** (06m) → `T05.2` · **Q.3(b)** (04m) → `T03.2` · **Q.4(a)** (04m) → `T12.4` · **Q.4(b)** (04m) → `T09.1` · **Q.4(c)** (02m) → `T09.3` · **Q.5(a)** (03m) → `T06.4` · **Q.5(b)** (03m) → `T06.4` · **Q.5(c)** (04m) → `T06.1` · **Q.6(a)** (02m) → `T05.9` · **Q.6(b)** (06m) → `T07.3` · **Q.6(c)** (02m) → `T05.8` · **Q.7(a)** (03m) → `T12.1` · **Q.7(b)** (04m) → `T12.3` · **Q.7(c)** (03m) → `T12.4` · **Q.8(a)** (02m) → `T13.3` · **Q.8(b)** (04m) → `T10.3` · **Q.8(c)** (04m) → `T11.6`
- **2024** *(22 sub-Qs · 80m)*: **Q.1(a)** (04m) → `T01.2` · **Q.1(b)** (02m) → `T02.5` · **Q.1(c)** (04m) → `T05.5` · **Q.2(a)** (03m) → `T07.2` · **Q.2(b)** (04m) → `T04.2` · **Q.2(c)** (03m) → `T09.2` · **Q.3(a)** (04m) → `T08.8` · **Q.3(b)** (04m) → `T12.1` · **Q.3(c)** (02m) → `T06.1` · **Q.4(a)** (06m) → `T06.2` · **Q.4(b)** (04m) → `T05.2` · **Q.5(a)** (04m) → `T04.2` · **Q.5(b)** (06m) → `T05.7` · **Q.6(a)** (04m) → `T05.6` · **Q.6(b)** (04m) → `T07.3` · **Q.6(c)** (02m) → `T09.1` · **Q.7(a)** (03m) → `T05.4` · **Q.7(b)** (04m) → `T05.8` · **Q.7(c)** (03m) → `T12.4` · **Q.8(a)** (03m) → `T09.5` · **Q.8(b)** (03m) → `T11.6` · **Q.8(c)** (04m) → `T10.3`
- **CT-01** *(9 parts · 20m)*: **Q.01** (05m) → `T01.4` · **Q.02** (05m) → `T03.4` · **Q.03** (02m) → `T01.7` · **Q.04(v–viii)** (04m) → `T04.2` · **Q.05(iii–iv)** (04m) → `T04.3`
- **CT-02** *(6 parts · 20m)*: **Q.01(a)** (02m) → `T05.2` · **Q.01(b)** (02m) → `T05.3` · **Q.01(c)** (03m) → `T05.6` · **Q.01(d)** (03m) → `T05.5` · **Q.02(a–b)** (10m) → `T02.5`
- **CT-03** *(7 parts · 20m)*: **Q.01(a)** (04m) → `T08.4` · **Q.01(b–c)** (04m) → `T08.2` · **Q.01(d)** (02m) → `T08.9` · **Q.02** (03m) → `T08.1` · **Q.03** (03m) → `T08.6` · **Q.04** (04m) → `T08.9`
- **CT-04** *(4 parts · 20m)*: **Q.01** (06m) → `T09.1` · **Q.02** (04m) → `T09.4` · **Q.03** (04m) → `T09.5` · **Q.04** (06m) → `T10.3`
