---
title: "T04 · Relational Algebra and Calculus · Exam-Style Answers"
tags:
  - ece2215
  - database-systems
  - exam-style
---

[← Prev: T03 · Relational Model, Keys and Integrity](T03_Relational_Model_Keys_and_Integrity.md) | [Explanation layer](../Topicwise_answers_explaination/T04_Relational_Algebra_and_Calculus.md) | [Next: T05 · SQL (DDL, DML, Aggregates, Subqueries) →](T05_SQL_DDL_DML_Aggregates_Subqueries.md)

---

# T04 · Relational Algebra and Calculus

> [!info] Topic card
> **Syllabus:** Unit 3 · **Weight:** 48 final marks (7.5%) in 6/7 papers + 8 CT marks
> **Sources:** Deck 02 · Textbook Ch. 2 §2.6, Ch. 16 §16.1
> **Blocks in this file:** 9 final + 2 CT questions (10 blocks: 8 final + 2 CT)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T04.1 | Basic operators | 0 + 0 | No questions | [[#T04.1 · Basic operators\|Go]] |
| T04.2 | Write RA queries on a given schema | 41 + 4 | 2017 Q.2(a), 2018 Q.3(a), 2019 Q.2(b), 2020 Q.2(a), 2021 Q.2(a), 2024 Q.2(b), 2024 Q.5(a), CT-01 Q.04(v–viii) | [[#T04.2 · Write RA queries on a given schema\|Go]] |
| T04.3 | Explain an RA expression in words | 4 + 4 | 2021 Q.2(c), CT-01 Q.05(iii–iv) | [[#T04.3 · Explain an RA expression in words\|Go]] |
| T04.4 | Extended RA: aggregation | 0 + 0 | No questions | [[#T04.4 · Extended RA: aggregation\|Go]] |
| T04.5 | Domain relational calculus | 3 + 0 | 2020 Q.4(b) | [[#T04.5 · Domain relational calculus\|Go]] |

---

## T04.1 · Basic operators

*No questions from past finals or class tests.*

*See also:* [[#T04.2 · Write RA queries on a given schema]] (queries using basic operators) and [[#T04.3 · Explain an RA expression in words]] (interpreting basic algebraic operations).

---

## T04.2 · Write RA queries on a given schema

### 2017 Q.2(a) · 08 Marks

*Section A · Asked in: 2017 · L1 (asked once)*

**Question.** Consider the following relational database.  
  `employee(person_name, street, city)`  
  `works(person_name, company_name, salary)`  
  `company(company_name, city)`  
  `manages(person_name, manager_name)`  
Now write down the relational algebra(Not SQL) to express each of following queries:  
(i) Find the names of all employees who live in the city same as their corresponding company location.  
(ii) Give a 10% salary raise to all the managers only.  
(iii) Update the city information of the employee named "James" to "Newtown".  
(iv) Find the company with most employees.

**Answer.**

**(i) Employees living in the same city as their company:**

Natural join matches `person_name`, `company_name`, and ensures `employee.city = company.city`:

$$
T_1 \leftarrow \text{employee} \bowtie \text{works} \bowtie \text{company}
$$

$$
\Pi_{\text{person\_name}}(T_1)
$$

Equivalently, in a single expression:

$$
\boxed{\Pi_{\text{person\_name}}(\text{employee} \bowtie \text{works} \bowtie \text{company})}
$$

**(ii) Give a 10% salary raise to all managers only:**

Identify manager names, join with their work records, compute the raise, and union with untouched non-manager records:

$$
M \leftarrow \rho_{M(\text{person\_name})}(\Pi_{\text{manager\_name}}(\text{manages}))
$$

$$
T_{\text{mgr}} \leftarrow \text{works} \bowtie M
$$

$$
T_{\text{raised}} \leftarrow \Pi_{\text{person\_name}, \text{company\_name}, \text{salary} * 1.1}(T_{\text{mgr}})
$$

$$
T_{\text{untouched}} \leftarrow \text{works} - T_{\text{mgr}}
$$

$$
\boxed{\text{works} \leftarrow T_{\text{raised}} \cup T_{\text{untouched}}}
$$

**(iii) Update city of employee "James" to "Newtown":**

Replace the city attribute for James and keep all other employee records unchanged:

$$
T_{\text{james}} \leftarrow \sigma_{\text{person\_name} = \text{"James"}}(\text{employee})
$$

$$
T_{\text{updated}} \leftarrow \Pi_{\text{person\_name}, \text{street}, \text{"Newtown"}}(T_{\text{james}})
$$

$$
T_{\text{untouched}} \leftarrow \text{employee} - T_{\text{james}}
$$

$$
\boxed{\text{employee} \leftarrow T_{\text{updated}} \cup T_{\text{untouched}}}
$$

**(iv) Find the company with the most employees:**

Count employees per company, find the maximum count, and select the matching company name:

$$
T_{\text{counts}} \leftarrow {}_{\text{company\_name}}\gamma_{\text{count}(\text{person\_name}) \ \text{as} \ \text{num\_emp}}(\text{works})
$$

$$
T_{\text{max}} \leftarrow \gamma_{\text{max}(\text{num\_emp}) \ \text{as} \ \text{max\_emp}}(T_{\text{counts}})
$$

$$
\boxed{\Pi_{\text{company\_name}}(\sigma_{\text{num\_emp} = \text{max\_emp}}(T_{\text{counts}} \times T_{\text{max}}))}
$$

---

### 2018 Q.3(a) · 06 Marks

*Section A · Asked in: 2018 · L1 (asked once)*

**Question.** Consider the following insurance database, where primary keys are underlined.  
person (<u>driver_id</u>, name, address)  
car (<u>license</u>, model, year)  
accident (<u>report_number</u>, date, location)  
owns (<u>driver_id</u>, license)  
participated (<u>driver_id</u>, car, <u>report_number</u>, damage_amount)

Write down the relational algebra statement for the following queries:  
(i) Find the total number of people who owned cars that were involved in accidents in 1989.  
(ii) Find the number of accidents in which the cars belonging to "John Smith" were involved.  
(iii) Update the damage amounts for the car with license number "AABB2019" in the accident with report_number "AR201930" to \$3000.

**Answer.**

*Assumption: The calendar year is extracted from the `date` attribute using $\text{year}(\text{date}) = 1989$.*

**(i) Total number of people who owned cars involved in accidents in 1989:**

Join accident records from 1989 with participated cars and ownership data, then count distinct owners:

$$
T_1 \leftarrow \sigma_{\text{year}(\text{date}) = 1989}(\text{accident}) \bowtie \text{participated}
$$

$$
T_2 \leftarrow T_1 \bowtie_{\text{participated.car} = \text{owns.license}} \text{owns}
$$

$$
\boxed{\gamma_{\text{count-distinct}(\text{owns.driver\_id})}(T_2)}
$$

**(ii) Number of accidents involving cars belonging to "John Smith":**

Find cars owned by John Smith, join with accident participation records, and count distinct accidents:

$$
T_{\text{john\_cars}} \leftarrow \sigma_{\text{name} = \text{"John Smith"}}(\text{person}) \bowtie \text{owns}
$$

$$
T_{\text{accidents}} \leftarrow T_{\text{john\_cars}} \bowtie_{\text{owns.license} = \text{participated.car}} \text{participated}
$$

$$
\boxed{\gamma_{\text{count-distinct}(\text{report\_number})}(T_{\text{accidents}})}
$$

**(iii) Update damage amounts for car "AABB2019" in accident "AR201930" to \$3000:**

Define the predicate for the specific accident record and update the `damage_amount` attribute:

$$
P \equiv (\text{car} = \text{"AABB2019"} \land \text{report\_number} = \text{"AR201930"})
$$

$$
T_{\text{target}} \leftarrow \sigma_P(\text{participated})
$$

$$
T_{\text{updated}} \leftarrow \Pi_{\text{driver\_id}, \text{car}, \text{report\_number}, 3000}(T_{\text{target}})
$$

$$
T_{\text{untouched}} \leftarrow \text{participated} - T_{\text{target}}
$$

$$
\boxed{\text{participated} \leftarrow T_{\text{updated}} \cup T_{\text{untouched}}}
$$

---

### 2019 Q.2(b) · 08 Marks

*Section A · Asked in: 2019, 2024 Q.5(a) (Sec B, 4 marks, CO2) · L2 merge*

**Question (2019 Q.2(b)).** Consider the following relational database.  
`Patient (Patient_ID, Patient_name, Mobile)`  
`History (Patient_ID, Symptom, Date)`  
`Report (Parient_ID, Corona_center, Test_result)`

Now write down the relational algebra (Not SQL) to find out the following queries.  
(i) Find the names of those patients who have fever symptom.  
(ii) Consider that if any patient has high-fever symptom he/she will be suspected as corona patient. Find out such maximum number of patients in a date.  
(iii) Find out the mobile numbers of those patients who have provided samples in Rajshahi corona center and their results have become positive.  
(iv) Find out the name of those patients who have high fever symptom but test result have become negative.

*(Note: Printed as "Parient_ID" in Report schema in original question paper; refers to "Patient_ID")*

**Question (2024 Q.5(a)).** Consider the following relation database:  
Patient (Patient_ID, Patient_Name, Mobile)  
History (Patient_ID, Symptom, Date)  
Report (Patient_ID, Corona_center, Test_result)  
Now, write down the relational algebra (Not SQL) to find out the following queris:  
i) Find the names of those patients who have fever symptom  
ii) Find out the mobile numbers of those patients who have provided samples in Rangpur corona center and their results have become positive.  
*(Note: "relation database" and "queris" printed verbatim in original paper; refers to relational database and queries)*

**Answer.**

*Assumption: In relation `Report`, `Parient_ID` is a typographical misprint for `Patient_ID`.*

**(i) Names of patients who have fever symptom:**

Join patients with their history records filtered for fever, then project the patient names:

$$
\boxed{\Pi_{\text{Patient\_name}}(\text{Patient} \bowtie \sigma_{\text{Symptom} = \text{"fever"}}(\text{History}))}
$$

**(ii) Maximum number of suspected patients (high-fever symptom) on a date:**

Filter records for "high-fever", count patients per date, and take the maximum:

$$
T_1 \leftarrow \sigma_{\text{Symptom} = \text{"high-fever"}}(\text{History})
$$

$$
T_{\text{daily}} \leftarrow {}_{\text{Date}}\gamma_{\text{count}(\text{Patient\_ID}) \ \text{as} \ \text{patient\_count}}(T_1)
$$

$$
\boxed{\gamma_{\text{max}(\text{patient\_count})}(T_{\text{daily}})}
$$

**(iii) Mobile numbers of patients tested in Rajshahi corona center with positive results:**

Filter reports for Rajshahi center and positive results, join with Patient, and project mobile numbers:

$$
\boxed{\Pi_{\text{Mobile}}(\text{Patient} \bowtie \sigma_{\text{Corona\_center} = \text{"Rajshahi"} \land \text{Test\_result} = \text{"positive"}}(\text{Report}))}
$$

**(iv) Names of patients who have high fever symptom but negative test result:**

Find patients who have high fever and whose test result is negative:

$$
T_{\text{high}} \leftarrow \Pi_{\text{Patient\_ID}}(\sigma_{\text{Symptom} = \text{"high-fever"}}(\text{History}))
$$

$$
T_{\text{neg}} \leftarrow \Pi_{\text{Patient\_ID}}(\sigma_{\text{Test\_result} = \text{"negative"}}(\text{Report}))
$$

$$
\boxed{\Pi_{\text{Patient\_name}}(\text{Patient} \bowtie (T_{\text{high}} \cap T_{\text{neg}}))}
$$

*Short version for 2024 Q.5(a) (Sec B, 4 marks, CO2):*  
Answer parts (i) and (ii) only. Part (i) matches part (i) above. Part (ii) targets Rangpur instead of Rajshahi:

$$
\Pi_{\text{Mobile}}(\text{Patient} \bowtie \sigma_{\text{Corona\_center} = \text{"Rangpur"} \land \text{Test\_result} = \text{"positive"}}(\text{Report}))
$$

---

### 2020 Q.2(a) · 06 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Consider the following relation schema:  
  person(<u>id</u>, name, age)  
  vaccine(<u>id</u>, center, dose_no, date)  
Now give expression in relational algebra to express-  
(i) Find the names of all persons who are adult.  
(ii) Find the names of all persons who have taken the $1^{\text{st}}$ dose only.  
(iii) Find the details of all persons who were given vaccine from "RMC" center and completed $2^{\text{nd}}$ dose.

**Answer.**

*Assumption: An adult is defined as a person with $\text{age} \ge 18$. The attribute `vaccine.id` references `person.id`.*

**(i) Names of all adult persons:**

$$
\boxed{\Pi_{\text{name}}(\sigma_{\text{age} \ge 18}(\text{person}))}
$$

**(ii) Names of all persons who have taken the $1^{\text{st}}$ dose only:**

Subtract persons who took dose 2 from persons who took dose 1, then join with person to get names:

$$
T_{\text{dose1}} \leftarrow \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 1}(\text{vaccine}))
$$

$$
T_{\text{dose2}} \leftarrow \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 2}(\text{vaccine}))
$$

$$
T_{\text{only1}} \leftarrow T_{\text{dose1}} - T_{\text{dose2}}
$$

$$
\boxed{\Pi_{\text{name}}(\text{person} \bowtie T_{\text{only1}})}
$$

Equivalently, written as a single expression:

$$
\Pi_{\text{name}}(\text{person} \bowtie (\Pi_{\text{id}}(\sigma_{\text{dose\_no} = 1}(\text{vaccine})) - \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 2}(\text{vaccine}))))
$$

**(iii) Details of all persons vaccinated from "RMC" center who completed $2^{\text{nd}}$ dose:**

Select vaccine records matching center "RMC" and dose 2, then join with person:

$$
T_{\text{rmc2}} \leftarrow \sigma_{\text{center} = \text{"RMC"} \land \text{dose\_no} = 2}(\text{vaccine})
$$

$$
\boxed{\text{person} \bowtie T_{\text{rmc2}}}
$$

To display person attributes only:

$$
\Pi_{\text{person.id}, \text{name}, \text{age}}(\text{person} \bowtie T_{\text{rmc2}})
$$

---

### 2021 Q.2(a) · 05 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** Consider the following relation schema:  
  customer (<u>id</u>, name, age, gender)  
  order (<u>id</u>, product, price, date)

Now, give expression in relational algebra to-  
(i) find name of the customers who are male.  
(ii) find name of all customers who have purchased car as product.  
(iii) find the details of all customers who have purchased "phone" as product and the price is less than \$300.

**Answer.**

*Assumption: The attribute `order.id` represents the customer identifier that placed the order.*

**(i) Names of male customers:**

$$
\boxed{\Pi_{\text{name}}(\sigma_{\text{gender} = \text{"male"}}(\text{customer}))}
$$

**(ii) Names of all customers who purchased car as product:**

Join customer and order on `id`, filter for product "car", and project customer names:

$$
\boxed{\Pi_{\text{name}}(\text{customer} \bowtie \sigma_{\text{product} = \text{"car"}}(\text{order}))}
$$

**(iii) Details of all customers who purchased "phone" priced under \$300:**

Filter order records for product "phone" with price below 300, then join with customer:

$$
T_{\text{target\_orders}} \leftarrow \sigma_{\text{product} = \text{"phone"} \land \text{price} < 300}(\text{order})
$$

$$
\boxed{\text{customer} \bowtie T_{\text{target\_orders}}}
$$

To project customer attributes only:

$$
\Pi_{\text{customer.id}, \text{name}, \text{age}, \text{gender}}(\text{customer} \bowtie T_{\text{target\_orders}})
$$

---

### 2024 Q.2(b) · 04 Marks

*Section A · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** EMPLOYEE (EID, Name, Department, Salary)  
PROJECT (PID, Name, Budget)  
WORKS_ON (EID, PID, Hours)  
Suppose a company wants to find employees working on multiple projects. Write the relational algebra expression for it.

**Answer.**

Group `WORKS_ON` by `EID`, filter for counts strictly greater than 1, and join with `EMPLOYEE`:

$$
T_{\text{counts}} \leftarrow {}_{\text{EID}}\gamma_{\text{count}(\text{PID}) \ \text{as} \ \text{proj\_count}}(\text{WORKS\_ON})
$$

$$
T_{\text{multi}} \leftarrow \sigma_{\text{proj\_count} > 1}(T_{\text{counts}})
$$

$$
\boxed{\Pi_{\text{EID}, \text{Name}}(\text{EMPLOYEE} \bowtie T_{\text{multi}})}
$$

*Alternative (pure relational algebra without aggregation):*  
Self-join `WORKS_ON` with itself to find matching employees on different projects:

$$
\Pi_{\text{EID}, \text{Name}}(\text{EMPLOYEE} \bowtie \Pi_{W_1.\text{EID}}(\sigma_{W_1.\text{EID} = W_2.\text{EID} \land W_1.\text{PID} \neq W_2.\text{PID}}(\rho_{W_1}(\text{WORKS\_ON}) \times \rho_{W_2}(\text{WORKS\_ON}))))
$$

---

### CT-01 Q.04(v–viii) · 04 Marks

*CT-01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Relations: $\text{STUDENT}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name}, \text{CGPA})$, $\text{COURSE}(\text{Course\_ID}, \text{Course\_Name}, \text{Student\_ID}, \text{Semester}, \text{Marks})$, $\text{ALUMNI}(\text{Student\_ID}, \text{Name}, \text{Dept\_Name})$.  
Write the relational algebra expressions for the following conditions using the relations above:  
**(v)** Rename the relation $\text{STUDENT}$ as $\text{S}$ and display the $\text{Student\_ID}$ and $\text{Name}$ of all students.  
**(vi)** Retrieve the $\text{Student\_ID}$, $\text{Name}$, and $\text{Course\_Name}$ of all students who belong to the CSE department and scored 80 or more marks in any course.  
**(vii)** Retrieve the $\text{Student\_ID}$ and $\text{Name}$ of all students who are either in the $\text{STUDENT}$ relation or the $\text{ALUMNI}$ relation.  
**(viii)** Determine the number of students in each department.  
*(Note: Sub-parts are numbered v, vi, vii, viii on the original question script; part viii uses $\gamma$ aggregation, see T04.4).*

**Answer.**

**(v) Rename relation STUDENT as S and display Student_ID and Name:**

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}}(\rho_S(\text{STUDENT}))}
$$

**(vi) Student_ID, Name, and Course_Name for CSE students with Marks $\ge 80$:**

Filter students in CSE and courses with marks 80 or higher, join on `Student_ID`, and project:

$$
T_1 \leftarrow \sigma_{\text{Dept\_Name} = \text{"CSE"}}(\text{STUDENT})
$$

$$
T_2 \leftarrow \sigma_{\text{Marks} \ge 80}(\text{COURSE})
$$

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}, \text{Course\_Name}}(T_1 \bowtie T_2)}
$$

**(vii) Student_ID and Name of students in either STUDENT or ALUMNI:**

Project both relations to the same attributes to satisfy union compatibility, then take the union:

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}}(\text{STUDENT}) \cup \Pi_{\text{Student\_ID}, \text{Name}}(\text{ALUMNI})}
$$

**(viii) Number of students in each department:**

Group `STUDENT` by department name and count the student identifiers:

$$
\boxed{{}_{\text{Dept\_Name}}\gamma_{\text{count}(\text{Student\_ID})}(\text{STUDENT})}
$$

---

## T04.3 · Explain an RA expression in words

### 2021 Q.2(c) · 04 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** For each expression, explain in words what the expression does.  
Where takes(<u>id</u>, <u>course</u>, <u>sec_id</u>, sem, year, grade)  
(i) $\sigma_{year \ge 2009}(\text{takes}) \bowtie \text{student}$  
(ii) $\Pi_{id, name, course\_id}(\text{student} \bowtie \text{takes})$

**Answer.**

**(i) Expression:** $\sigma_{year \ge 2009}(\text{takes}) \bowtie \text{student}$

1. **Selection:** Filters the `takes` relation to keep only enrollment records where `year` is 2009 or later.
2. **Natural Join:** Joins the filtered course enrollments with the `student` relation on their common attribute `id`.
3. **Meaning in words:** Retrieves full student and enrollment records for all students who took a course in 2009 or later.

**(ii) Expression:** $\Pi_{id, name, course\_id}(\text{student} \bowtie \text{takes})$

1. **Natural Join:** Matches each student with the courses they have taken by joining `student` and `takes` on `id`.
2. **Projection:** Keeps only student ID (`id`), name (`name`), and course ID (`course_id`). Discards other attributes and eliminates duplicates.
3. **Meaning in words:** Lists the ID, name, and course taken for every student and each course they enrolled in.

---

### CT-01 Q.05(iii–iv) · 04 Marks

*CT-01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Describe the following relational algebra expression:  
**(iii)** $\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$  
**(iv)** $\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$  
*(Note: Sub-parts are numbered iii, iv on the original question script; part iv is Deck 02 Slide 24 verbatim).*

**Answer.**

**(iii) Expression:** $\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$

1. **Theta Join:** Joins `STUDENT` and `COURSE` where `STUDENT.Student_ID = COURSE.Student_ID` to pair students with their course marks.
2. **Selection:** Filters the joined tuples to retain only records where `Marks < 50`.
3. **Projection:** Extracts the `Name` attribute and removes duplicates.
4. **Meaning in words:** Retrieves the names of all students who scored strictly less than 50 marks in at least one course.

**(iv) Expression:** $\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$

1. **First Term:** Selects sections offered in Fall 2017 and projects their `course_id`.
2. **Second Term:** Selects sections offered in Spring 2018 and projects their `course_id`.
3. **Set Difference ($-$) :** Subtracts the second set of courses from the first set.
4. **Meaning in words:** Finds all courses taught in the Fall 2017 semester that were not taught in the Spring 2018 semester.

---

## T04.4 · Extended RA: aggregation

*No questions from past finals or class tests.*

*See also:* [[#T04.2 · Write RA queries on a given schema]] for questions using $\gamma$ aggregation: [[#2017 Q.2(a) · 08 Marks|2017 Q.2(a)(iv)]] (company with most employees), [[#2018 Q.3(a) · 06 Marks|2018 Q.3(a)(i–ii)]] (total people and number of accidents), [[#2019 Q.2(b) · 08 Marks|2019 Q.2(b)(ii)]] (maximum suspected patients in a date), [[#2024 Q.2(b) · 04 Marks|2024 Q.2(b)]] (employees on multiple projects), and [[#CT-01 Q.04(v–viii) · 04 Marks|CT-01 Q.04(viii)]] (students per department).

---

## T04.5 · Domain relational calculus

### 2020 Q.4(b) · 03 Marks

*Section A · Asked in: 2020 · L1 (asked once)*

**Question.** Let that, $R=(A, B, C)$ and $r_1$, $r_2$ both be relations on the schema R. Give an expression in the domain relational calculus that is equivalent to each of the followings.  
(i) $\pi_A(r_1)$  
(ii) $r_1 \cup r_2$  
(iii) $r_1 \cap r_2$

**Answer.**

Let relation instances $r_1$ and $r_2$ consist of tuples with three domain variables $\langle a, b, c \rangle$ corresponding to attributes $(A, B, C)$.

**(i) Domain calculus for $\pi_A(r_1)$:**

Project attribute $A$ by existentially quantifying domain variables $b$ and $c$:

$$
\boxed{\{\, \langle a \rangle \mid \exists b, c \; (\langle a, b, c \rangle \in r_1) \,\}}
$$

**(ii) Domain calculus for $r_1 \cup r_2$:**

A tuple belongs to the union if it belongs to $r_1$, or to $r_2$, or to both:

$$
\boxed{\{\, \langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \lor \langle a, b, c \rangle \in r_2 \,\}}
$$

**(iii) Domain calculus for $r_1 \cap r_2$:**

A tuple belongs to the intersection if it belongs to both $r_1$ and $r_2$:

$$
\boxed{\{\, \langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \land \langle a, b, c \rangle \in r_2 \,\}}
$$

---

[← Prev: T03 · Relational Model, Keys and Integrity](T03_Relational_Model_Keys_and_Integrity.md) | [Explanation layer](../Topicwise_answers_explaination/T04_Relational_Algebra_and_Calculus.md) | [Next: T05 · SQL (DDL, DML, Aggregates, Subqueries) →](T05_SQL_DDL_DML_Aggregates_Subqueries.md)
