---
title: "T04 · Relational Algebra and Calculus · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T03 · Relational Model, Keys and Integrity](T03_Relational_Model_Keys_and_Integrity.md) | [Exam-style layer](../Topicwise_answers_exam_style/T04_Relational_Algebra_and_Calculus.md) | [Next: T05 · SQL (DDL, DML, Aggregates, Subqueries) →](T05_SQL_DDL_DML_Aggregates_Subqueries.md)

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

**What the examiner wants.**  
Four distinct relational algebra expressions worth 2 marks each. The question tests natural joins across three tables. It also tests tuple updates using generalized projection and set union, attribute assignment, and aggregation with max filtering.

**Key idea.**  
Relational algebra expressions manipulate relation instances as mathematical sets. For updates, standard relational algebra has no in-place mutation. We express updates by computing the modified tuples and taking their union with the untouched tuples. For aggregation, group by company and find the peak count.

**Step-by-step solution.**

**(i) Employees living in the same city as their company:**

1. Join `employee` with `works` on `person_name`. This matches each person with their employer.
2. Join the result with `company`. Both `employee` and `company` share the attribute `city`, while `works` and `company` share `company_name`. The natural join $\bowtie$ automatically enforces `employee.city = company.city` and `works.company_name = company.company_name`.
3. Project `person_name`:

$$
T_1 \leftarrow \text{employee} \bowtie \text{works} \bowtie \text{company}
$$

$$
\Pi_{\text{person\_name}}(T_1)
$$

Equivalently, written as a single expression:

$$
\boxed{\Pi_{\text{person\_name}}(\text{employee} \bowtie \text{works} \bowtie \text{company})}
$$

**(ii) Give a 10% salary raise to all managers only:**

1. The `manages` relation pairs `(person_name, manager_name)`. Extract all distinct manager names and rename the attribute to `person_name` to join with `works`:

$$
M \leftarrow \rho_{M(\text{person\_name})}(\Pi_{\text{manager\_name}}(\text{manages}))
$$

2. Match managers with their work records:

$$
T_{\text{mgr}} \leftarrow \text{works} \bowtie M
$$

3. Construct the updated tuples with a 10% raise using generalized projection:

$$
T_{\text{raised}} \leftarrow \Pi_{\text{person\_name}, \text{company\_name}, \text{salary} * 1.1}(T_{\text{mgr}})
$$

4. Identify all non-manager tuples that must remain untouched:

$$
T_{\text{untouched}} \leftarrow \text{works} - T_{\text{mgr}}
$$

5. Reassign the relation `works` as the union of raised and untouched records:

$$
\boxed{\text{works} \leftarrow T_{\text{raised}} \cup T_{\text{untouched}}}
$$

**(iii) Update city of employee "James" to "Newtown":**

1. Select the employee tuple for "James":

$$
T_{\text{james}} \leftarrow \sigma_{\text{person\_name} = \text{"James"}}(\text{employee})
$$

2. Project the updated attributes, replacing the city value with the constant string `"Newtown"`:

$$
T_{\text{updated}} \leftarrow \Pi_{\text{person\_name}, \text{street}, \text{"Newtown"}}(T_{\text{james}})
$$

3. Subtract James from the original relation to retain all untouched employee records:

$$
T_{\text{untouched}} \leftarrow \text{employee} - T_{\text{james}}
$$

4. Union the updated tuple with the untouched tuples:

$$
\boxed{\text{employee} \leftarrow T_{\text{updated}} \cup T_{\text{untouched}}}
$$

**(iv) Find the company with the most employees:**

1. Group the `works` relation by `company_name` and count the employees:

$$
T_{\text{counts}} \leftarrow {}_{\text{company\_name}}\gamma_{\text{count}(\text{person\_name}) \ \text{as} \ \text{num\_emp}}(\text{works})
$$

2. Find the highest employee count across all companies:

$$
T_{\text{max}} \leftarrow \gamma_{\text{max}(\text{num\_emp}) \ \text{as} \ \text{max\_emp}}(T_{\text{counts}})
$$

3. Take the Cartesian product of $T_{\text{counts}}$ and $T_{\text{max}}$, select the tuples where the company count equals the maximum count, and project the company name:

$$
\boxed{\Pi_{\text{company\_name}}(\sigma_{\text{num\_emp} = \text{max\_emp}}(T_{\text{counts}} \times T_{\text{max}}))}
$$

**Check.**  
Consider sample data:
- `employee`: `("Alice", "Road 1", "Dhaka")`, `("Bob", "Road 2", "Rajshahi")`.
- `works`: `("Alice", "Apex", 50000)`, `("Bob", "Apex", 45000)`.
- `company`: `("Apex", "Dhaka")`.
- `manages`: `("Bob", "Alice")`.

- Part (i): Alice lives in Dhaka and Apex is in Dhaka. Bob lives in Rajshahi. Natural join returns `("Alice")`.
- Part (ii): Alice is in `manages.manager_name`. Alice gets $50000 \times 1.1 = 55000$. Bob is untouched at $45000$. The union restores both employees.
- Part (iv): Apex has count 2. Max count is 2. The selection matches Apex.

> [!warning] Common mistakes
> - Writing only the selection or projection for updates. Omitting the union with untouched tuples silently deletes all other employees from the database.
> - Using SQL keywords like `UPDATE` or `SET`. The question explicitly says "relational algebra (Not SQL)".
> - Writing $\Pi_{\text{company\_name}}(\gamma_{\text{max}(\dots)})$ directly. A scalar aggregation returns only the maximum number, not the company name. You must join or multiply back to get the name.

**Exam tip.**  
Break long relational algebra queries into named temporary relations using $\leftarrow$. It prevents syntax errors and earns partial marks even if an index is misnamed.

**Sources.**  
`[Lecture Deck 02 · Slides 15–29](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`  
`[Textbook Ch. 16 §16.1](../Textbook/Chapter_16_Query_Optimization/Chapter%2016%20-%20Query%20Optimization.md)`

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

**What the examiner wants.**  
Three relational algebra statements worth 2 marks each. Tests multi-table joins, distinct counting with aggregation ($\gamma$), and relational tuple updating.

**Key idea.**  
In part (i) and (ii), a person may own multiple cars or be involved in multiple accidents. Use `count-distinct` to count individual people and distinct accident reports without duplicate inflation. In part (iii), apply generalized projection on the matching record and union with all unaffected records.

**Step-by-step solution.**

*Assumption: The calendar year is extracted from the `date` attribute using $\text{year}(\text{date}) = 1989$.*

**(i) Total number of people who owned cars involved in accidents in 1989:**

1. Filter accident records for 1989 and join with `participated` on `report_number`:

$$
T_1 \leftarrow \sigma_{\text{year}(\text{date}) = 1989}(\text{accident}) \bowtie \text{participated}
$$

2. Join with `owns` matching `participated.car = owns.license`. This links each involved vehicle to its registered owner:

$$
T_2 \leftarrow T_1 \bowtie_{\text{participated.car} = \text{owns.license}} \text{owns}
$$

3. Count distinct owner IDs so that an owner whose car had multiple accidents is counted once:

$$
\boxed{\gamma_{\text{count-distinct}(\text{owns.driver\_id})}(T_2)}
$$

**(ii) Number of accidents involving cars belonging to "John Smith":**

1. Find the driver ID of John Smith and join with `owns` to find his registered vehicle licenses:

$$
T_{\text{john\_cars}} \leftarrow \sigma_{\text{name} = \text{"John Smith"}}(\text{person}) \bowtie \text{owns}
$$

2. Join with `participated` by matching license numbers with `participated.car`:

$$
T_{\text{accidents}} \leftarrow T_{\text{john\_cars}} \bowtie_{\text{owns.license} = \text{participated.car}} \text{participated}
$$

3. Count distinct accident report numbers:

$$
\boxed{\gamma_{\text{count-distinct}(\text{report\_number})}(T_{\text{accidents}})}
$$

**(iii) Update damage amounts for car "AABB2019" in accident "AR201930" to \$3000:**

1. Define the selection condition identifying the exact record to modify:

$$
P \equiv (\text{car} = \text{"AABB2019"} \land \text{report\_number} = \text{"AR201930"})
$$

2. Select the target record:

$$
T_{\text{target}} \leftarrow \sigma_P(\text{participated})
$$

3. Replace the `damage_amount` attribute with the literal value 3000:

$$
T_{\text{updated}} \leftarrow \Pi_{\text{driver\_id}, \text{car}, \text{report\_number}, 3000}(T_{\text{target}})
$$

4. Separate all unaffected records in `participated`:

$$
T_{\text{untouched}} \leftarrow \text{participated} - T_{\text{target}}
$$

5. Reassign `participated` as the union of both sets:

$$
\boxed{\text{participated} \leftarrow T_{\text{updated}} \cup T_{\text{untouched}}}
$$

**Check.**  
Trace part (iii):
- Suppose `participated` contains tuples `("D1", "AABB2019", "AR201930", 1500)` and `("D2", "XY100", "AR201930", 500)`.
- $T_{\text{target}}$ isolates `("D1", "AABB2019", "AR201930", 1500)`.
- $T_{\text{updated}}$ produces `("D1", "AABB2019", "AR201930", 3000)`.
- $T_{\text{untouched}}$ retains `("D2", "XY100", "AR201930", 500)`.
- Union contains both tuples with the updated value intact.

> [!warning] Common mistakes
> - Using `count` instead of `count-distinct`. If John Smith's car is involved in an accident with two drivers participating, a simple count would count the same accident twice.
> - Confusing `car` attribute in `participated` with the table `car`. The attribute `participated.car` stores the license plate string.
> - Forgetting the untouched set difference during the update.

**Exam tip.**  
When counting people or entities involved across multiple events, always write `count-distinct` rather than plain `count`.

**Sources.**  
`[Lecture Deck 02 · Slides 16–29](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`  
`[Textbook Ch. 16 §16.1](../Textbook/Chapter_16_Query_Optimization/Chapter%2016%20-%20Query%20Optimization.md)`

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

**What the examiner wants.**  
Four relational algebra queries worth 2 marks each. Covers selection on joined tables and daily grouping with peak aggregation. Also tests multi-table filtering and set intersection between history and lab test reports.

**Key idea.**  
Link patients to clinical records via `Patient_ID`. Natural joins equate common keys. For part (ii), group by `Date` and count patients, then find the global maximum of these daily totals.

**Step-by-step solution.**

*Assumption: In relation `Report`, `Parient_ID` is a typographical misprint for `Patient_ID`.*

**(i) Names of patients who have fever symptom:**

1. Select records from `History` where `Symptom = "fever"`.
2. Natural join with `Patient` on `Patient_ID`.
3. Project the patient names:

$$
\boxed{\Pi_{\text{Patient\_name}}(\text{Patient} \bowtie \sigma_{\text{Symptom} = \text{"fever"}}(\text{History}))}
$$

**(ii) Maximum number of suspected patients (high-fever symptom) on a date:**

1. Select history records for patients exhibiting high fever:

$$
T_1 \leftarrow \sigma_{\text{Symptom} = \text{"high-fever"}}(\text{History})
$$

2. Group the suspected cases by `Date` and count the patients on each date:

$$
T_{\text{daily}} \leftarrow {}_{\text{Date}}\gamma_{\text{count}(\text{Patient\_ID}) \ \text{as} \ \text{patient\_count}}(T_1)
$$

3. Find the maximum count across all recorded dates:

$$
\boxed{\gamma_{\text{max}(\text{patient\_count})}(T_{\text{daily}})}
$$

**(iii) Mobile numbers of patients tested in Rajshahi corona center with positive results:**

1. Filter `Report` for center "Rajshahi" and test result "positive".
2. Natural join with `Patient` on `Patient_ID`.
3. Project `Mobile`:

$$
\boxed{\Pi_{\text{Mobile}}(\text{Patient} \bowtie \sigma_{\text{Corona\_center} = \text{"Rajshahi"} \land \text{Test\_result} = \text{"positive"}}(\text{Report}))}
$$

**(iv) Names of patients who have high fever symptom but negative test result:**

1. Retrieve the IDs of patients recorded with high fever:

$$
T_{\text{high}} \leftarrow \Pi_{\text{Patient\_ID}}(\sigma_{\text{Symptom} = \text{"high-fever"}}(\text{History}))
$$

2. Retrieve the IDs of patients whose test results returned negative:

$$
T_{\text{neg}} \leftarrow \Pi_{\text{Patient\_ID}}(\sigma_{\text{Test\_result} = \text{"negative"}}(\text{Report}))
$$

3. Find the patients satisfying both conditions using set intersection, join with `Patient`, and project their names:

$$
\boxed{\Pi_{\text{Patient\_name}}(\text{Patient} \bowtie (T_{\text{high}} \cap T_{\text{neg}}))}
$$

*Short version for 2024 Q.5(a) (Sec B, 4 marks, CO2):*  
Answer parts (i) and (ii) only. Part (i) matches part (i) above. Part (ii) targets Rangpur instead of Rajshahi:

$$
\Pi_{\text{Mobile}}(\text{Patient} \bowtie \sigma_{\text{Corona\_center} = \text{"Rangpur"} \land \text{Test\_result} = \text{"positive"}}(\text{Report}))
$$

**Check.**  
Suppose:
- `History`: `(P1, "high-fever", "2020-04-01")`, `(P2, "high-fever", "2020-04-01")`, `(P3, "high-fever", "2020-04-02")`.
- `Report`: `(P1, "Rajshahi", "negative")`, `(P2, "Rajshahi", "positive")`.

- Part (ii): Count on 2020-04-01 is 2. Count on 2020-04-02 is 1. The max operation yields 2.
- Part (iv): $T_{\text{high}} = \{P1, P2, P3\}$. $T_{\text{neg}} = \{P1\}$. Intersection is $\{P1\}$. The query correctly retrieves P1's name.

> [!warning] Common mistakes
> - Halting or getting confused by the misprint `Parient_ID`. Write one assumption line and continue with `Patient_ID`.
> - Treating "high fever but negative test result" as set difference of symptom strings rather than the intersection of patient IDs across the two relations.
> - Forgetting the outer projection, which outputs raw IDs and extra columns instead of the requested names or mobile numbers.

**Exam tip.**  
When a question repeats across years with only a city name swapped, the query structure is identical. Memorize the two-step pattern for daily extremes: group by date with count, then apply scalar max.

**Sources.**  
`[Lecture Deck 02 · Slides 11–29](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

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

**What the examiner wants.**  
Three relational algebra expressions worth 2 marks each. Tests simple attribute filtering, the relational set difference operator ($-$) for an "only" query condition, and join filtering on multiple attributes.

**Key idea.**  
A person with two doses has a record for dose 1 and another record for dose 2. Selecting `dose_no = 1` alone will incorrectly return two-dose individuals. To find persons taking dose 1 *only*, subtract IDs with dose 2 from IDs with dose 1.

**Step-by-step solution.**

*Assumption: An adult is defined as a person with $\text{age} \ge 18$. The attribute `vaccine.id` references `person.id`.*

**(i) Names of all adult persons:**

Select persons with age 18 or older, then project their names:

$$
\boxed{\Pi_{\text{name}}(\sigma_{\text{age} \ge 18}(\text{person}))}
$$

**(ii) Names of all persons who have taken the $1^{\text{st}}$ dose only:**

1. Project the IDs of all persons who received dose 1:

$$
T_{\text{dose1}} \leftarrow \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 1}(\text{vaccine}))
$$

2. Project the IDs of all persons who received dose 2:

$$
T_{\text{dose2}} \leftarrow \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 2}(\text{vaccine}))
$$

3. Subtract $T_{\text{dose2}}$ from $T_{\text{dose1}}$ using set difference to keep persons with no second dose:

$$
T_{\text{only1}} \leftarrow T_{\text{dose1}} - T_{\text{dose2}}
$$

4. Join with `person` on `id` and project the names:

$$
\boxed{\Pi_{\text{name}}(\text{person} \bowtie T_{\text{only1}})}
$$

Equivalently, written as a single expression:

$$
\Pi_{\text{name}}(\text{person} \bowtie (\Pi_{\text{id}}(\sigma_{\text{dose\_no} = 1}(\text{vaccine})) - \Pi_{\text{id}}(\sigma_{\text{dose\_no} = 2}(\text{vaccine}))))
$$

**(iii) Details of all persons vaccinated from "RMC" center who completed $2^{\text{nd}}$ dose:**

1. Filter the `vaccine` table for center "RMC" and dose number 2:

$$
T_{\text{rmc2}} \leftarrow \sigma_{\text{center} = \text{"RMC"} \land \text{dose\_no} = 2}(\text{vaccine})
$$

2. Natural join with `person` on `id`:

$$
\boxed{\text{person} \bowtie T_{\text{rmc2}}}
$$

To restrict output to person attributes only:

$$
\Pi_{\text{person.id}, \text{name}, \text{age}}(\text{person} \bowtie T_{\text{rmc2}})
$$

**Check.**  
Sample data:
- `person`: `(1, "Rahim", 25)`, `(2, "Karim", 17)`, `(3, "Sara", 30)`.
- `vaccine`: `(1, "RMC", 1, "2021-01")`, `(1, "RMC", 2, "2021-02")`, `(3, "DMC", 1, "2021-01")`.

- Part (i): Rahim and Sara have age $\ge 18$. Output: `{"Rahim", "Sara"}`.
- Part (ii): $T_{\text{dose1}} = \{1, 3\}$. $T_{\text{dose2}} = \{1\}$. Difference $\{1, 3\} - \{1\} = \{3\}$. Join yields `{"Sara"}`. Rahim is excluded because he completed dose 2.
- Part (iii): Rahim matches RMC and dose 2. Join retrieves Rahim's full record.

> [!warning] Common mistakes
> - Writing $\sigma_{\text{dose\_no} = 1}(\text{vaccine})$ for part (ii). Rahim took dose 1 and dose 2. Filtering for dose 1 alone includes him, violating the requirement of taking dose 1 *only*.
> - Attempting set difference between `person` and `vaccine` directly. Set difference requires identical arity and compatible attribute domains. You must project to `id` first.
> - Forgetting to define what makes a person an adult. Always write an assumption line stating $\text{age} \ge 18$.

**Exam tip.**  
When an exam query says "only", use relational set difference ($-$). Subtract the forbidden set from the desired set.

**Sources.**  
`[Lecture Deck 02 · Slides 11–24](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

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

**What the examiner wants.**  
Three relational algebra expressions worth approximately 1.5, 1.5, and 2 marks. Evaluates single-table selection, natural join between customer and orders, and compound filtering combining string and numeric inequalities.

**Key idea.**  
The attribute `id` serves as customer primary key and appears as foreign key in `order`. Natural join equates `customer.id = order.id`. Filter on product names and numerical price thresholds.

**Step-by-step solution.**

*Assumption: The attribute `order.id` represents the customer identifier that placed the order.*

**(i) Names of male customers:**

Select tuples from `customer` where gender is "male", then project the customer name:

$$
\boxed{\Pi_{\text{name}}(\sigma_{\text{gender} = \text{"male"}}(\text{customer}))}
$$

**(ii) Names of all customers who purchased car as product:**

1. Select orders where product is "car".
2. Natural join with `customer` on `id`.
3. Project customer names:

$$
\boxed{\Pi_{\text{name}}(\text{customer} \bowtie \sigma_{\text{product} = \text{"car"}}(\text{order}))}
$$

**(iii) Details of all customers who purchased "phone" priced under \$300:**

1. Filter the `order` relation for product "phone" with price strictly below 300:

$$
T_{\text{target\_orders}} \leftarrow \sigma_{\text{product} = \text{"phone"} \land \text{price} < 300}(\text{order})
$$

2. Join the filtered orders with `customer`:

$$
\boxed{\text{customer} \bowtie T_{\text{target\_orders}}}
$$

To project customer attributes only:

$$
\Pi_{\text{customer.id}, \text{name}, \text{age}, \text{gender}}(\text{customer} \bowtie T_{\text{target\_orders}})
$$

**Check.**  
Sample data:
- `customer`: `(101, "Kamal", 30, "male")`, `(102, "Nila", 24, "female")`.
- `order`: `(101, "phone", 250, "2021-05-10")`, `(102, "phone", 400, "2021-06-01")`, `(102, "car", 15000, "2021-07-15")`.

- Part (i): Kamal has gender "male". Output: `{"Kamal"}`.
- Part (ii): Order with product "car" belongs to ID 102. Natural join with customer outputs `{"Nila"}`.
- Part (iii): Kamal's phone costs 250 ($< 300$). Nila's phone costs 400 ($\not< 300$). Result contains Kamal's record.

> [!warning] Common mistakes
> - Omitting the outer projection $\Pi_{\text{name}}$ in parts (i) and (ii). Without projection, all attributes from both tables are returned.
> - Putting quotes around numerical values like `price < "300"`. Price is a numeric attribute.
> - Writing a Cartesian product ($\times$) without specifying the join predicate `customer.id = order.id`.

**Exam tip.**  
When the question asks for "details of all customers", providing the joined relation or projecting the customer relation's attributes is accepted. Always state the join assumption on `id`.

**Sources.**  
`[Lecture Deck 02 · Slides 11–19](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

---

### 2024 Q.2(b) · 04 Marks

*Section A · CO1 · Asked in: 2024 · L1 (asked once)*

**Question.** EMPLOYEE (EID, Name, Department, Salary)  
PROJECT (PID, Name, Budget)  
WORKS_ON (EID, PID, Hours)  
Suppose a company wants to find employees working on multiple projects. Write the relational algebra expression for it.

**Answer.**

**What the examiner wants.**  
A relational algebra expression worth 4 marks to find employees assigned to more than one project. The examiner expects either aggregation with grouping and threshold filtering ($\gamma$), or classical pure relational algebra using a self-join.

**Key idea.**  
Count the distinct projects per employee. An employee works on multiple projects if their project count exceeds 1. Alternatively, perform a self-join on `WORKS_ON` where the employee ID is the same but the project IDs differ.

**Step-by-step solution.**

**Method 1: Aggregation Operation (Standard Solution)**

1. Group `WORKS_ON` by `EID` and count the project IDs:

$$
T_{\text{counts}} \leftarrow {}_{\text{EID}}\gamma_{\text{count}(\text{PID}) \ \text{as} \ \text{proj\_count}}(\text{WORKS\_ON})
$$

2. Filter for employees associated with more than one project:

$$
T_{\text{multi}} \leftarrow \sigma_{\text{proj\_count} > 1}(T_{\text{counts}})
$$

3. Natural join with `EMPLOYEE` on `EID` to retrieve employee details and project the name:

$$
\boxed{\Pi_{\text{EID}, \text{Name}}(\text{EMPLOYEE} \bowtie T_{\text{multi}})}
$$

**Method 2: Pure Relational Algebra via Self-Join (Classical Alternative)**

1. Take the Cartesian product of `WORKS_ON` with a renamed copy of itself:

$$
W_1 \leftarrow \rho_{W_1}(\text{WORKS\_ON})
$$

$$
W_2 \leftarrow \rho_{W_2}(\text{WORKS\_ON})
$$

2. Select pairs having the same `EID` but different `PID`:

$$
T_{\text{multi\_ids}} \leftarrow \Pi_{W_1.\text{EID}}(\sigma_{W_1.\text{EID} = W_2.\text{EID} \land W_1.\text{PID} \neq W_2.\text{PID}}(W_1 \times W_2))
$$

3. Join with `EMPLOYEE` to retrieve employee names:

$$
\Pi_{\text{EID}, \text{Name}}(\text{EMPLOYEE} \bowtie T_{\text{multi\_ids}})
$$

**Check.**  
Sample data for `WORKS_ON`:
- `(E1, P1, 10)`, `(E1, P2, 15)`, `(E2, P1, 20)`.

- Method 1: E1 has count 2 ($> 1$). E2 has count 1 ($\not> 1$). Join with EMPLOYEE returns E1.
- Method 2: Pairing `(E1, P1)` with `(E1, P2)` matches $E1 = E1$ and $P1 \neq P2$. E1 is selected. E2 has only one project, so no pair with different PID exists.

> [!warning] Common mistakes
> - Forgetting to join with `EMPLOYEE`. `WORKS_ON` contains only `EID`, not employee names.
> - In Method 2, writing $W_1.\text{PID} = W_2.\text{PID}$. That checks if an employee works on the same project twice, not multiple distinct projects.
> - Filtering for `Hours > 1` instead of `count(PID) > 1`.

**Exam tip.**  
Method 1 using $\gamma$ is concise and preferred. Mentioning the self-join method in one sentence shows complete mastery of both modern extended algebra and classical pure algebra.

**Sources.**  
`[Lecture Deck 02 · Slides 27–29](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 16 §16.1](../Textbook/Chapter_16_Query_Optimization/Chapter%2016%20-%20Query%20Optimization.md)`

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

**What the examiner wants.**  
Four distinct relational algebra queries worth 1 mark each. Evaluates the rename operator ($\rho$), multi-table selection and projection, union compatibility constraints, and aggregation with grouping ($\gamma$).

**Key idea.**  
Part (v) uses the rename operator $\rho$. Part (vi) combines selection on department and marks before joining. Part (vii) requires union compatibility: `STUDENT` has 4 attributes while `ALUMNI` has 3. Both relations must be projected to the same two attributes before applying $\cup$. Part (viii) groups by department name.

**Step-by-step solution.**

**(v) Rename relation STUDENT as S and display Student_ID and Name:**

1. Apply the rename operator $\rho_S$:
2. Project `Student_ID` and `Name`:

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}}(\rho_S(\text{STUDENT}))}
$$

**(vi) Student_ID, Name, and Course_Name for CSE students with Marks $\ge 80$:**

1. Filter students from the "CSE" department:

$$
T_1 \leftarrow \sigma_{\text{Dept\_Name} = \text{"CSE"}}(\text{STUDENT})
$$

2. Filter course enrollments where marks are 80 or above:

$$
T_2 \leftarrow \sigma_{\text{Marks} \ge 80}(\text{COURSE})
$$

3. Natural join $T_1$ and $T_2$ on `Student_ID`, then project the requested columns:

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}, \text{Course\_Name}}(T_1 \bowtie T_2)}
$$

**(vii) Student_ID and Name of students in either STUDENT or ALUMNI:**

1. The schema of `STUDENT` is `(Student_ID, Name, Dept_Name, CGPA)` (arity 4). The schema of `ALUMNI` is `(Student_ID, Name, Dept_Name)` (arity 3).
2. The union operation $r \cup s$ requires both relations to have identical arity and compatible domains.
3. Project each relation to `(Student_ID, Name)` first, then take the union:

$$
\boxed{\Pi_{\text{Student\_ID}, \text{Name}}(\text{STUDENT}) \cup \Pi_{\text{Student\_ID}, \text{Name}}(\text{ALUMNI})}
$$

**(viii) Number of students in each department:**

Group the `STUDENT` relation by `Dept_Name` and count `Student_ID`:

$$
\boxed{{}_{\text{Dept\_Name}}\gamma_{\text{count}(\text{Student\_ID})}(\text{STUDENT})}
$$

**Check.**  
- Part (vii): If `STUDENT` contains `(101, "A", "CSE", 3.8)` and `ALUMNI` contains `(201, "B", "EEE")`, direct union $\text{STUDENT} \cup \text{ALUMNI}$ fails because $4 \neq 3$. Projecting first yields `{(101, "A")}` and `{(201, "B")}`. The union produces `{(101, "A"), (201, "B")}`, which is valid and correct.
- Part (viii): Grouping `STUDENT` tuples by `Dept_Name` produces a two-column relation `(Dept_Name, count(Student_ID))`.

> [!warning] Common mistakes
> - Writing $\text{STUDENT} \cup \text{ALUMNI}$ directly. This violates union compatibility and loses marks immediately.
> - Forgetting `Course_Name` in the projection of part (vi).
> - Writing $\sigma$ instead of $\gamma$ for part (viii). Counting rows requires an aggregate operator.

**Exam tip.**  
Before applying $\cup$, $\cap$, or $-$, always check the column counts of both tables. If they differ, project the common target columns first.

**Sources.**  
`[Lecture Deck 02 · Slides 13–29](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

---

## T04.3 · Explain an RA expression in words

### 2021 Q.2(c) · 04 Marks

*Section A · CLO2 · Asked in: 2021 · L1 (asked once)*

**Question.** For each expression, explain in words what the expression does.  
Where takes(<u>id</u>, <u>course</u>, <u>sec_id</u>, sem, year, grade)  
(i) $\sigma_{year \ge 2009}(\text{takes}) \bowtie \text{student}$  
(ii) $\Pi_{id, name, course\_id}(\text{student} \bowtie \text{takes})$

**Answer.**

**What the examiner wants.**  
Accurate plain English descriptions of two relational algebra expressions (2 marks each). Evaluates understanding of selection, natural join semantics, projection, and attribute propagation.

**Key idea.**  
Trace the operation tree from the innermost operators to the outermost operators. Explain what filtering or pairing takes place at each step, and describe what the final relation represents.

**Step-by-step solution.**

**(i) Expression:** $\sigma_{year \ge 2009}(\text{takes}) \bowtie \text{student}$

1. **Selection Operation:** The term $\sigma_{year \ge 2009}(\text{takes})$ scans the `takes` relation and filters it. It keeps only the course enrollment records where the course was taken in the year 2009 or later.
2. **Natural Join Operation:** The join $\bowtie$ matches the filtered course enrollment records with tuples in the `student` relation on their common attribute `id`.
3. **What the join adds:** The join combines all student details (`name`, `dept_name`, `tot_cred`) with all enrollment details (`course`, `sec_id`, `sem`, `year`, `grade`).
4. **Summary in words:** Finds the full records (combining all student and enrollment information) of all students who took at least one course in the year 2009 or later.

**(ii) Expression:** $\Pi_{id, name, course\_id}(\text{student} \bowtie \text{takes})$

1. **Natural Join Operation:** The term $\text{student} \bowtie \text{takes}$ pairs each student with every course enrollment record that shares the same `id`.
2. **What the join adds:** It brings together the student's personal identity (`name`) and their enrolled course details (`course_id` / `course`).
3. **Projection Operation:** The operator $\Pi_{id, name, course\_id}$ selects only three attributes: the student ID (`id`), student name (`name`), and the course identifier (`course_id` / `course`). All other attributes (such as department name, section ID, semester, year, and grade) are discarded. Duplicate rows are removed automatically.
4. **Summary in words:** Displays a list showing the ID, name, and course ID for all students and each course they have taken.

**Check.**  
- Part (i): If student 101 took courses in 2008 and 2010, the selection drops the 2008 record. The join keeps the 2010 record paired with student 101's details. If student 102 took courses only in 2005, student 102 does not appear in the result.
- Part (ii): If student 101 took CS-101 and CS-201, the output contains two tuples: `(101, "Alice", "CS-101")` and `(101, "Alice", "CS-201")`.

> [!warning] Common mistakes
> - Writing a vague summary such as "joins student and takes table" without explaining what the filter condition or projection actually achieves.
> - Forgetting to mention that projection removes duplicates.
> - Overlooking that students who have taken no courses in 2009 or later are excluded from part (i).

**Exam tip.**  
Format your answer in three distinct bullet points: describe the inner operation, explain the outer operation, and give a one-sentence plain English summary of the final output.

**Sources.**  
`[Lecture Deck 02 · Slides 15–20](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

---

### CT-01 Q.05(iii–iv) · 04 Marks

*CT-01 · CO1 · Asked in: CT-01 · L1 (asked once)*

**Question.** Describe the following relational algebra expression:  
**(iii)** $\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$  
**(iv)** $\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$  
*(Note: Sub-parts are numbered iii, iv on the original question script; part iv is Deck 02 Slide 24 verbatim).*

**Answer.**

**What the examiner wants.**  
Accurate descriptions of two complex relational algebra expressions (2 marks each). Evaluates theta joins with selection and projection, and set difference between projected query expressions.

**Key idea.**  
Part (iii) performs a theta join on student identifiers, filters on an academic performance threshold (marks under 50), and projects the student names. Part (iv) is a classic set difference pattern identifying courses offered in a specific semester but not in another semester.

**Step-by-step solution.**

**(iii) Expression:** $\Pi_{\text{Name}} \left(\sigma_{\text{Marks} < 50} \left(\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}\right)\right)$

1. **Theta Join:** $\text{STUDENT} \bowtie_{\text{STUDENT.Student\_ID} = \text{COURSE.Student\_ID}} \text{COURSE}$ combines records from `STUDENT` and `COURSE` where the student IDs match. This pairs student personal data with their course enrollment records and marks.
2. **Selection:** The selection condition $\sigma_{\text{Marks} < 50}$ filters the joined relation. It keeps only tuples where the student scored strictly less than 50 marks.
3. **Projection:** The operator $\Pi_{\text{Name}}$ extracts only the `Name` attribute from the filtered records, eliminating any duplicate student names.
4. **Summary in words:** Finds the names of all students who scored less than 50 marks in at least one course.

**(iv) Expression:** $\Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017} (\text{section})\right) - \Pi_{\text{course\_id}} \left(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018} (\text{section})\right)$

1. **First Sub-expression:** Filters `section` for courses offered in Fall 2017 and projects their unique `course_id` values:

$$
S_{\text{Fall}} = \Pi_{\text{course\_id}}(\sigma_{\text{semester} = \text{"Fall"} \land \text{year} = 2017}(\text{section}))
$$

2. **Second Sub-expression:** Filters `section` for courses offered in Spring 2018 and projects their unique `course_id` values:

$$
S_{\text{Spring}} = \Pi_{\text{course\_id}}(\sigma_{\text{semester} = \text{"Spring"} \land \text{year} = 2018}(\text{section}))
$$

3. **Set Difference ($-$) :** Computes $S_{\text{Fall}} - S_{\text{Spring}}$. It retains all course IDs that appear in the Fall 2017 set but do not appear in the Spring 2018 set.
4. **Summary in words:** Finds all courses taught in the Fall 2017 semester that were not taught in the Spring 2018 semester.

**Check.**  
- Part (iii): If student "Suman" scored 42 in Math and 75 in Physics, the selection retains the Math row. Projection outputs "Suman". If a student scored above 50 in all courses, that student is excluded.
- Part (iv): If CS-101 was taught in Fall 2017 and Spring 2018, and CS-347 was taught only in Fall 2017:
  - $S_{\text{Fall}} = \{\text{CS-101}, \text{CS-347}\}$.
  - $S_{\text{Spring}} = \{\text{CS-101}\}$.
  - Difference is $\{\text{CS-347}\}$. CS-101 is eliminated.

> [!warning] Common mistakes
> - Calling the set difference operator minus or arithmetic subtraction. Use the technical term set difference.
> - Confusing set difference with intersection. Writing "taught in Fall 2017 AND Spring 2018" describes $r \cap s$, not $r - s$.
> - Forgetting that duplicate student names are removed by the projection operator.

**Exam tip.**  
Part (iv) is taken verbatim from Slide 24 of Lecture Deck 02. Knowing slide examples verbatim ensures rapid, confident full marks in class tests.

**Sources.**  
`[Lecture Deck 02 · Slides 18–24](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

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

**What the examiner wants.**  
Three Domain Relational Calculus (DRC) expressions worth 1 mark each. Evaluates the ability to translate projection, union, and intersection from relational algebra into predicate formulas over domain variables.

**Key idea.**  
Domain relational calculus uses domain variables corresponding to relation attributes rather than whole-tuple variables. A query expression has the form:

$$
\{\, \langle x_1, x_2, \dots, x_n \rangle \mid P(x_1, x_2, \dots, x_n) \,\}
$$

For a schema $R = (A, B, C)$, each relation instance consists of 3-tuples $\langle a, b, c \rangle$. Projection uses the existential quantifier ($\exists$) to bind omitted attributes. Union uses logical disjunction ($\lor$). Intersection uses logical conjunction ($\land$).

**Step-by-step solution.**

Let domain variables $a, b, c$ range over the domains of attributes $A, B, C$ respectively.

**(i) Domain calculus for $\pi_A(r_1)$:**

1. Projecting attribute $A$ produces a 1-attribute result tuple $\langle a \rangle$.
2. Attributes $B$ and $C$ do not appear in the result. We bind them using existential quantifiers:

$$
\boxed{\{\, \langle a \rangle \mid \exists b, c \; (\langle a, b, c \rangle \in r_1) \,\}}
$$

This formula states: "the set of all values $a$ such that there exist values $b$ and $c$ where $\langle a, b, c \rangle$ is a tuple in $r_1$."

**(ii) Domain calculus for $r_1 \cup r_2$:**

1. The union produces 3-tuples $\langle a, b, c \rangle$.
2. A tuple belongs to $r_1 \cup r_2$ if it belongs to $r_1$, or to $r_2$, or to both. We express this using logical disjunction ($\lor$):

$$
\boxed{\{\, \langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \lor \langle a, b, c \rangle \in r_2 \,\}}
$$

**(iii) Domain calculus for $r_1 \cap r_2$:**

1. The intersection produces 3-tuples $\langle a, b, c \rangle$.
2. A tuple belongs to $r_1 \cap r_2$ if and only if it belongs to both relations simultaneously. We express this using logical conjunction ($\land$):

$$
\boxed{\{\, \langle a, b, c \rangle \mid \langle a, b, c \rangle \in r_1 \land \langle a, b, c \rangle \in r_2 \,\}}
$$

**Check.**  
Quick self-test:
- **Q:** How does Domain Relational Calculus differ from Tuple Relational Calculus?  
  **A:** DRC uses individual domain variables $\langle a, b, c \rangle$ for each column. TRC uses a single tuple variable $t$ and attribute lookups like $t[A]$.
- **Q:** Why is an existential quantifier needed in part (i)?  
  **A:** The output tuple has arity 1 ($\langle a \rangle$). Variables $b$ and $c$ must be bound by $\exists b, c$ so the formula evaluates to true whenever at least one matching tuple exists in $r_1$.
- **Q:** Are these expressions safe?  
  **A:** Yes. Every variable in the result tuple is restricted to values that appear in the domains of relation $r_1$ or $r_2$.

> [!warning] Common mistakes
> - Writing Tuple Relational Calculus instead of Domain Relational Calculus. Writing $\{ t \mid t \in r_1 \lor t \in r_2 \}$ is TRC, not DRC.
> - Forgetting the existential quantifier $\exists b, c$ in projection. Writing $\{ \langle a \rangle \mid \langle a, b, c \rangle \in r_1 \}$ leaves $b$ and $c$ unbound, making the formula invalid.
> - Writing curly braces or angle brackets incorrectly. In DRC, the tuple of domain variables uses angle brackets $\langle \dots \rangle$ inside the set definition.

**Exam tip.**  
Always match the arity of the angle-bracketed domain variables on the left of the vertical bar to the arity of the resulting relation.

**Sources.**  
`[Lecture Deck 02 · Slides 9–10](../LectureSlides/02_Relational_Model.md)`  
`[Textbook Ch. 2 §2.6](../Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md)`

---

[← Prev: T03 · Relational Model, Keys and Integrity](T03_Relational_Model_Keys_and_Integrity.md) | [Exam-style layer](../Topicwise_answers_exam_style/T04_Relational_Algebra_and_Calculus.md) | [Next: T05 · SQL (DDL, DML, Aggregates, Subqueries) →](T05_SQL_DDL_DML_Aggregates_Subqueries.md)
