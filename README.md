# ECE 2215: Database Systems — Study Vault

> **Course Code:** ECE 2215  
> **Course Title:** Database Systems *(printed as Data Base Systems on the official syllabus)*  
> **Credits:** 3.00  
> **Department:** Electrical & Computer Engineering (ECE), Rajshahi University of Engineering & Technology (RUET)  
> **Instructors:** Mst. Nafia Islam Shishir & Md. Rakibul Islam  
> **Primary Textbook:** Abraham Silberschatz, Henry F. Korth, & S. Sudarshan, *Database System Concepts* (7th Edition, McGraw-Hill, 2019)

A complete, Obsidian- and BossNotes-compatible study vault for **ECE 2215**. It brings together every past exam paper, class test, two-layer solved answer bank, lecture slide deck, student class notebook, and the full digitized textbook in one cross-linked repository.

---

## Vault at a Glance

| Resource Category | Directory / File | Scope & Metrics |
| :--- | :--- | :--- |
| **Course Syllabus & Mapping** | [`syllabus.md`](syllabus.md) | Official 8-unit RUET curriculum and cross-resource alignment matrix |
| **Past Exam Archive** | [`PreviousYearQuestion/`](PreviousYearQuestion/README.md) | **7 Semester Finals** (`2017`–`2021`, `2023`–`2024`; 148 sub-questions, 637 printed marks) + **4 Class Tests** (`CT-01`–`CT-04`; 26 parts, 80 marks) = **174 question parts** (717 marks) |
| **PYQ Analytics & Taxonomy** | [`ECE2215_PYQ_Analysis_Report.md`](ECE2215_PYQ_Analysis_Report.md)<br>[`subtopicwise_list.md`](subtopicwise_list.md)<br>[`subtopicwise_questions.md`](subtopicwise_questions.md) | Quantitative era analysis, **13 topics (`T01`–`T13`) / 77 subtopics (`T01.1`–`T13.4`)**, priority tiers, and full verbatim subtopic-sorted question bank |
| **Solved Answers (Exam Style)** | [`Topicwise_answers_exam_style/`](Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) | **13 topic files** (`T01`–`T13`), **136 H3 question blocks**, **77 H2 subtopics**, and **21 custom diagrams** written as concise, mark-calibrated exam-sheet solutions |
| **Solved Answers (Explanation)** | [`Topicwise_answers_explaination/`](Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md) | **13 topic files** (`T01`–`T13`, 136 H3 blocks) with step-by-step derivations, concrete verification checks, `Common mistakes` callouts, exam tips, and source links |
| **Official Lecture Slides** | [`LectureSlides/`](LectureSlides/00_Index.md) | **8 slide decks** (`01`–`08`), **371 slides**, **102 extracted figures**, and a master PYQ-to-slide cross-reference index |
| **Student Class Notes (Raidah)** | [`Classnote_by_Raidah/`](Classnote_by_Raidah/README.md) | Roll `2310035`: unified 65-side notebook, teacher exam suggestions ([`suggestions.md`](Classnote_by_Raidah/suggestions.md)), **11 topic files** (`T01`–`T06`, `T08`–`T12`), **11 diagrams** |
| **Student Handnotes (Fahim)** | [`Handnote_by_Fahim_2310002/`](Handnote_by_Fahim_2310002/README.md) | Roll `2310002`: unified 62-page notebook, **6 topic files** (`T01`–`T03`, `T05`–`T07`, including classroom coverage of SQL Triggers), **20 diagrams** |
| **Reference Textbook** | [`Textbook/`](Textbook/README.md) | Silberschatz *Database System Concepts* (7th Ed.): **29 sections** (Front Matter, Chapters 01–26, Appendix A, Index), 1,373 PDF pages (1,344 printed pages), **368 figures** |

---

## Quick Start: How to Study from This Repo

1. **Check the high-yield roadmap:** Start with [`ECE2215_PYQ_Analysis_Report.md`](ECE2215_PYQ_Analysis_Report.md) and [`subtopicwise_list.md`](subtopicwise_list.md) to see which topics carry the most marks. SQL (`T05`), Normalization (`T08`), E-R Modeling (`T02`), and Serializability (`T10`) alone account for **over 50% of all final exam marks**.
2. **Read the lecture slides & class notes together:** Use [`LectureSlides/00_Index.md`](LectureSlides/00_Index.md) alongside [`Classnote_by_Raidah/`](Classnote_by_Raidah/README.md) (plus [`suggestions.md`](Classnote_by_Raidah/suggestions.md) for teacher pointers) and [`Handnote_by_Fahim_2310002/`](Handnote_by_Fahim_2310002/README.md) for classroom examples and SQL syntax.
3. **Practice by subtopic:** Open [`subtopicwise_questions.md`](subtopicwise_questions.md) to drill every past question on a single concept (for example, `T08.4` Candidate Keys or `T10.1` Conflict Serializability) across all years at once.
4. **Learn with the two-layer answer banks:**
   - Read [`Topicwise_answers_explaination/`](Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md) first to understand the step-by-step method, verify your result on a sample tuple or schedule, and avoid common pitfalls.
   - Review [`Topicwise_answers_exam_style/`](Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) right before the exam to see the exact length, table layout, and formatting expected on a 3-hour script.
5. **Simulate full papers:** Use the frozen papers in [`PreviousYearQuestion/`](PreviousYearQuestion/README.md) (`2017.md`–`2024.md` and `ClassTestQuestions.md`) for timed mock exams.

---

## 13-Topic Master Navigation & Exam Weightage

Every resource in this vault is organized around the same 13 topics (`T01`–`T13`). Across the 7 semester finals (**637 printed marks**) and 4 class tests (**80 marks**), the topics map as follows:

| ID | Topic Name | Final Marks (Share) | Exam Frequency | Exam-Style Answers | Step-by-Step Explanations | Lecture Slides | Class Notes (Raidah · Fahim) | Textbook Chapters |
| :-: | :--- | :-: | :-: | :-: | :-: | :--- | :--- | :--- |
| **`T01`** | **DB Concepts & Architecture** | 44 (`6.9%`) | 7/7 Finals, CT-01 | [Exam T01](Topicwise_answers_exam_style/T01_DB_Concepts_and_Architecture.md) | [Expl T01](Topicwise_answers_explaination/T01_DB_Concepts_and_Architecture.md) | [Deck 01](LectureSlides/01_Intro_to_Database_and_DBMS.md) | [Raidah T01](Classnote_by_Raidah/T01_DB_Concepts_and_Architecture.md) · [Fahim T01](Handnote_by_Fahim_2310002/T01_DB_Concepts_and_Architecture.md) | [Ch. 01](Textbook/Chapter_01_Introduction/Chapter%2001%20-%20Introduction.md) |
| **`T02`** | **E-R & EER Modeling** | 67 (`10.5%`) | 7/7 Finals, CT-02 | [Exam T02](Topicwise_answers_exam_style/T02_ER_and_EER_Modeling.md) | [Expl T02](Topicwise_answers_explaination/T02_ER_and_EER_Modeling.md) | [Deck 05](LectureSlides/05_ER_Model.md) | [Raidah T02](Classnote_by_Raidah/T02_ER_and_EER_Modeling.md) · [Fahim T02](Handnote_by_Fahim_2310002/T02_ER_and_EER_Modeling.md) | [Ch. 06](Textbook/Chapter_06_ER_Model/Chapter%2006%20-%20Database%20Design%20Using%20the%20E-R%20Model.md) |
| **`T03`** | **Relational Model, Keys & Integrity** | 28 (`4.4%`) | 5/7 Finals, CT-01 | [Exam T03](Topicwise_answers_exam_style/T03_Relational_Model_Keys_and_Integrity.md) | [Expl T03](Topicwise_answers_explaination/T03_Relational_Model_Keys_and_Integrity.md) | [Deck 02](LectureSlides/02_Relational_Model.md) (S2–8) | [Raidah T03](Classnote_by_Raidah/T03_Relational_Model_Keys_and_Integrity.md) · [Fahim T03](Handnote_by_Fahim_2310002/T03_Relational_Model_Keys_and_Integrity.md) | [Ch. 02](Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md) (§2.1–2.5) |
| **`T04`** | **Relational Algebra & Calculus** | 48 (`7.5%`) | 6/7 Finals, CT-01 | [Exam T04](Topicwise_answers_exam_style/T04_Relational_Algebra_and_Calculus.md) | [Expl T04](Topicwise_answers_explaination/T04_Relational_Algebra_and_Calculus.md) | [Deck 02](LectureSlides/02_Relational_Model.md) (S9–31) | [Raidah T04](Classnote_by_Raidah/T04_Relational_Algebra_and_Calculus.md) | [Ch. 02](Textbook/Chapter_02_Relational_Model/Chapter%2002%20-%20Introduction%20to%20the%20Relational%20Model.md) (§2.6), [Ch. 16](Textbook/Chapter_16_Query_Optimization/Chapter%2016%20-%20Query%20Optimization.md) (§16.1 $\gamma$) |
| **`T05`** | **SQL (DDL, DML, Aggregates, Subqueries)** | **130 (`20.4%`)** | **7/7 Finals, CT-02** | [Exam T05](Topicwise_answers_exam_style/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Expl T05](Topicwise_answers_explaination/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Deck 03](LectureSlides/03_Introduction_to_SQL.md) | [Raidah T05](Classnote_by_Raidah/T05_SQL_DDL_DML_Aggregates_Subqueries.md) · [Fahim T05](Handnote_by_Fahim_2310002/T05_SQL_DDL_DML_Aggregates_Subqueries.md) | [Ch. 03](Textbook/Chapter_03_Intro_SQL/Chapter%2003%20-%20Introduction%20to%20SQL.md), [Ch. 04](Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md) (§4.4) |
| **`T06`** | **SQL Joins & Views** | 28 (`4.4%`) | 4/7 Finals | [Exam T06](Topicwise_answers_exam_style/T06_Joins_and_Views.md) | [Expl T06](Topicwise_answers_explaination/T06_Joins_and_Views.md) | [Deck 04](LectureSlides/04_Joining_and_Views.md) | [Raidah T06](Classnote_by_Raidah/T06_Joins_and_Views.md) · [Fahim T06](Handnote_by_Fahim_2310002/T06_Joins_and_Views.md) | [Ch. 04](Textbook/Chapter_04_Intermediate_SQL/Chapter%2004%20-%20Intermediate%20SQL.md) (§4.1–4.2) |
| **`T07`** | **Triggers & Stored Procedures** | 27 (`4.2%`) | 5/7 Finals | [Exam T07](Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) | [Expl T07](Topicwise_answers_explaination/T07_Triggers_and_Stored_Procedures.md) | — | [Fahim T07](Handnote_by_Fahim_2310002/T07_Triggers_and_Stored_Procedures.md) *(Triggers)* | [Ch. 05](Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md) (§5.2–5.3) |
| **`T08`** | **Normalization & Functional Dependencies** | **75 (`11.8%`)** | **7/7 Finals, CT-03** | [Exam T08](Topicwise_answers_exam_style/T08_Normalization_and_Functional_Dependencies.md) | [Expl T08](Topicwise_answers_explaination/T08_Normalization_and_Functional_Dependencies.md) | [Deck 06](LectureSlides/06_DBMS_Normalization.md) | [Raidah T08](Classnote_by_Raidah/T08_Normalization_and_FDs.md) | [Ch. 07](Textbook/Chapter_07_Normalization/Chapter%2007%20-%20Relational%20Database%20Design.md) |
| **`T09`** | **Transactions, ACID & Anomalies** | 41 (`6.4%`) | 7/7 Finals, CT-04 | [Exam T09](Topicwise_answers_exam_style/T09_Transactions_ACID_and_Anomalies.md) | [Expl T09](Topicwise_answers_explaination/T09_Transactions_ACID_and_Anomalies.md) | [Deck 07](LectureSlides/07_Transactions.md) (S2–15, 28–33) | [Raidah T09](Classnote_by_Raidah/T09_Transactions_ACID_and_Anomalies.md) | [Ch. 17](Textbook/Chapter_17_Transactions/Chapter%2017%20-%20Transactions.md) (§17.1–17.5) |
| **`T10`** | **Serializability (Conflict/View, Graphs)** | 51 (`8.0%`) | 7/7 Finals, CT-04 | [Exam T10](Topicwise_answers_exam_style/T10_Serializability.md) | [Expl T10](Topicwise_answers_explaination/T10_Serializability.md) | [Deck 07](LectureSlides/07_Transactions.md) (S16–27), [Deck 08](LectureSlides/08_Concurrency_Control_Mechanisms.md) (S2–8) | [Raidah T10](Classnote_by_Raidah/T10_Serializability.md) | [Ch. 17](Textbook/Chapter_17_Transactions/Chapter%2017%20-%20Transactions.md) (§17.6), [Ch. 18](Textbook/Chapter_18_Concurrency_Control/Chapter%2018%20-%20Concurrency%20Control.md) (§18.5) |
| **`T11`** | **Concurrency Control Protocols (2PL, Deadlock, TSO)** | 37 (`5.8%`) | 6/7 Finals | [Exam T11](Topicwise_answers_exam_style/T11_Concurrency_Control_Protocols.md) | [Expl T11](Topicwise_answers_explaination/T11_Concurrency_Control_Protocols.md) | [Deck 08](LectureSlides/08_Concurrency_Control_Mechanisms.md) (S9–30) | [Raidah T11](Classnote_by_Raidah/T11_Concurrency_Control_Protocols.md) | [Ch. 18](Textbook/Chapter_18_Concurrency_Control/Chapter%2018%20-%20Concurrency%20Control.md) (§18.1–18.2, §18.5) |
| **`T12`** | **Recovery System & RAID** | 43 (`6.8%`) | 5/7 Finals | [Exam T12](Topicwise_answers_exam_style/T12_Recovery_System_and_RAID.md) | [Expl T12](Topicwise_answers_explaination/T12_Recovery_System_and_RAID.md) | — | [Raidah T12](Classnote_by_Raidah/T12_Recovery_and_RAID.md) *(RAID)* | [Ch. 19](Textbook/Chapter_19_Recovery_System/Chapter%2019%20-%20Recovery%20System.md), [Ch. 12](Textbook/Chapter_12_Physical_Storage/Chapter%2012%20-%20Physical%20Storage%20Systems.md) (§12.5 RAID) |
| **`T13`** | **Security, Indexing & Hashing** | 18 (`2.8%`) | 4/7 Finals | [Exam T13](Topicwise_answers_exam_style/T13_Security_Indexing_and_Hashing.md) | [Expl T13](Topicwise_answers_explaination/T13_Security_Indexing_and_Hashing.md) | — | — | [Ch. 09](Textbook/Chapter_09_App_Development/Chapter%2009%20-%20Application%20Development.md) (§9.8), [Ch. 14](Textbook/Chapter_14_Indexing/Chapter%2014%20-%20Indexing.md) (§14.2–14.5) |

---

## Past Exam Archive (`PreviousYearQuestion/`)

All 7 semester-final papers and 4 class tests are preserved verbatim in [`PreviousYearQuestion/`](PreviousYearQuestion/README.md):

| Exam Paper | Era & Format | Printed / Full Marks | Key Highlights |
| :--- | :--- | :---: | :--- |
| [`2017.md`](PreviousYearQuestion/2017.md) | Pre-OBE (Sec A + B) | 93 / 72 | File system vs. DBMS, RUET student E-R diagram, relational algebra, SQL DDL/DML, 3NF decomposition, 2PL, log-based recovery, hashing, triggers |
| [`2018.md`](PreviousYearQuestion/2018.md) | Pre-OBE (Sec A + B) | 96 / 72 | E-R aggregation & ternary relationships, insurance schema RA, 1NF/2NF, concurrency anomalies, deadlock, TSO rollback, conflict serializability, RAID |
| [`2019.md`](PreviousYearQuestion/2019.md) | Pre-OBE (Sec A + B) | 96 / 72 | 3-level data abstraction, railway e-ticketing E-R diagram, Covid patient RA, 1NF/2NF, schedule output trace, SQL queries, CGPA calculation |
| [`2020.md`](PreviousYearQuestion/2020.md) | Pre-OBE (Sec A + B) | 96 / 72 | 2-tier vs. 3-tier architecture, vaccine DB RA, SQL injection, domain relational calculus, natural/outer join tables, transaction states, view serializability |
| [`2021.md`](PreviousYearQuestion/2021.md) | Transitional OBE (CLO) | 96 / 72 | DBA roles, referential integrity in MySQL, RA with joins, candidate keys, canonical cover $F_c$, attribute closure $X^+$, wait-for graph cycle diagram |
| [`2023.md`](PreviousYearQuestion/2023.md) | Modern OBE (CLO) | 80 / 60 | RUET Central Library E-R diagram, 3NF conversion, SQL DDL/DML, candidate/super keys, RAID models, SQL Views, Stored Procedures, Triggers, WAL recovery |
| [`2024.md`](PreviousYearQuestion/2024.md) | Modern OBE (CO) | 80 / 60 | RUET student E-R & schema reduction, courier file vs. DBMS, SQL aggregates, security triggers, inner vs. outer joins, ACID, RAID levels, conflict serializability |
| [`ClassTestQuestions.md`](PreviousYearQuestion/ClassTestQuestions.md) | 4 Class Tests (CO) | 80 (`4 × 20`) | **CT-01:** Abstraction, schema diagram, RA · **CT-02:** SQL queries, E-R diagram · **CT-03:** Keys, prime attributes, 1NF–BCNF · **CT-04:** ACID, conflict serializability |

*(Note: No 2022 examination was held due to post-pandemic session adjustments.)*

---

## Course Conventions & Exam Traps to Watch Out For

> [!IMPORTANT]
> **Deck Numbers vs. Textbook Chapter Numbers**  
> Lecture slide deck numbers match textbook chapters only for Decks `01`–`04`. Starting at Deck `05`, they diverge:
> - **Deck 05 (`05_ER_Model.md`)** maps to **Textbook Chapter 06** (*Database Design Using the E-R Model*).
> - **Deck 06 (`06_DBMS_Normalization.md`)** maps to **Textbook Chapter 07** (*Relational Database Design*).
> - **Deck 07 (`07_Transactions.md`)** maps to **Textbook Chapter 17** (*Transactions*).
> - **Deck 08 (`08_Concurrency_Control_Mechanisms.md`)** maps to **Textbook Chapter 18** (*Concurrency Control*).
> - **Units 7 & 8 (`T07`, `T12`, `T13`)** have no standalone slide decks; study them from **Chapters 05, 09, 12, 14, and 19** plus the student class notes ([`Raidah T12`](Classnote_by_Raidah/T12_Recovery_and_RAID.md) for RAID and [`Fahim T07`](Handnote_by_Fahim_2310002/T07_Triggers_and_Stored_Procedures.md) for SQL Triggers).

- **MySQL 8 Dialect:** RUET teaches and tests **MySQL 8**. Use `DELIMITER //` for multi-statement triggers and stored procedures, emulate `FULL OUTER JOIN` with `LEFT JOIN ... UNION ... RIGHT JOIN`, and use correlated subqueries, `MAX(...)`, or `NOT EXISTS` whenever an exam question forbids `LIMIT`.
- **Silberschatz 6th vs. 7th Edition Shifts:**
  - **Extended Relational Algebra:** Grouping/aggregation ($_{G}\gamma_{F}$) and outer-join operators ($\mathbin{⟕}, \mathbin{⟖}, \mathbin{⟗}$) are taught in `Deck 02` and `Deck 04`, while 7th Edition moves them from Chapter 02 to **Chapter 16 (§16.1–16.2)**. Relational algebra database modifications ($r \leftarrow r \cup E$, $r \leftarrow r - E$) follow 6th Edition syntax.
  - **Canonical Cover ($F_c$) & Thomas' Write Rule:** Tested in finals (`2021` Q.6b) and listed in the syllabus, but omitted from the slides. Find Canonical Cover in **Chapter 07 (§7.4.3)** and Thomas' Write Rule in **Chapter 18 (§18.5.2)**.
- **Timestamp Rollback Rule Trap:**
  - Under **Deadlock Prevention (`wait-die` / `wound-wait`)**, an aborted transaction restarts with its **original timestamp** to prevent starvation (`Deck 08` Slide 23; `Ch. 18` §18.2.2).
  - Under the **Timestamp Ordering (TSO) Protocol**, a rolled-back transaction is assigned a **brand-new timestamp** upon restart (`Ch. 18` §18.5.1; tested in `2018` Q.6b and `2024` Q.8b).
- **Running Schema:** Both the lecture slides and textbook use the **University Database** (`department`, `course`, `instructor`, `section`, `teaches`, `student`, `takes`, `advisor`, `time_slot`, `classroom`, `prereq`). Full DDL and sample tables are in [`Textbook/Appendix_A_University_Schema/`](Textbook/Appendix_A_University_Schema/Appendix%20A%20-%20Detailed%20University%20Schema.md).

---

## Repository Structure

```text
ECE_2215/
├── README.md                                      # You are here
├── syllabus.md                                    # Official RUET syllabus & cross-resource alignment matrix
├── ECE2215_PYQ_Analysis_Report.md                 # Comprehensive statistical analysis of all past papers
├── subtopicwise_list.md                           # 13-topic (T01–T13), 77-subtopic taxonomy & priority tiers
├── subtopicwise_questions.md                      # All 174 past exam & CT question parts sorted by subtopic
├── PreviousYearQuestion/                          # Verbatim past exam papers (2017–2024) + 4 Class Tests
│   ├── README.md
│   ├── 2017.md ... 2024.md
│   ├── ClassTestQuestions.md
│   └── diagrams/                                  # 1 extracted exam figure + .meta.json sidecar
├── Topicwise_answers_exam_style/                  # Concise, mark-calibrated exam-sheet solutions
│   ├── T01_DB_Concepts_and_Architecture.md ... T13_Security_Indexing_and_Hashing.md
│   └── diagrams/                                  # 21 generated diagrams (+ _scripts/ Python generators)
├── Topicwise_answers_explaination/                # Step-by-step explanations, checks, & mistake callouts
│   ├── T01_DB_Concepts_and_Architecture.md ... T13_Security_Indexing_and_Hashing.md
│   └── diagrams/                                  # 21 mirrored diagrams + .meta.json sidecars
├── LectureSlides/                                 # 8 official slide decks (371 slides)
│   ├── 00_Index.md
│   ├── 01_Intro_to_Database_and_DBMS.md ... 08_Concurrency_Control_Mechanisms.md
│   └── diagrams/                                  # 102 slide figures + .meta.json sidecars
├── Classnote_by_Raidah/                           # Student class notes (Roll 2310035, 65 notebook sides)
│   ├── README.md
│   ├── suggestions.md                             # Teacher exam blueprint & assignment guide
│   ├── DBMS_classnote_2310035.md                  # Unified notebook
│   ├── T01_*.md ... T12_*.md                      # 11 topic-split files (T01–T06, T08–T12)
│   └── diagrams/                                  # 11 cropped notebook figures + sidecars
├── Handnote_by_Fahim_2310002/                     # Student handnotes (Roll 2310002, 62 pages)
│   ├── README.md
│   ├── Handnote_2310002.md                        # Unified notebook
│   ├── T01_*.md ... T07_*.md                      # 6 topic-split files (T01–T03, T05–T07 incl. Triggers)
│   └── diagrams/                                  # 20 cropped handnote figures + sidecars
└── Textbook/                                      # Silberschatz 7th Ed. (29 sections, 1,373 PDF pages)
    ├── README.md
    ├── 00_Front_Matter/
    ├── Chapter_01_Introduction/ ... Chapter_26_Blockchain/
    ├── Appendix_A_University_Schema/
    └── Index/
```

---

## Viewing & Rendering Notes

- **Obsidian & BossNotes Compatible:** All Markdown notes follow strict dual-renderer formatting so they display cleanly in both **Obsidian** and **BossNotes** (remark/micromark + KaTeX):
  - Inline math uses `$...$` and display math uses `$$...$$` with `$$` placed alone on its own line.
  - Complex relational schemas, unnormalized tables with merged cells (`rowspan`), and multi-column transaction schedules use clean inline HTML tables inside Markdown table cells.
- **Page & Slide Markers:**
  - `Textbook/` files include `<!-- Page N -->` comments matching the **printed book page numbers** (`1`–`1344`).
  - `LectureSlides/` files include `<!-- Slide N -->` comments above every slide section (`371` total).
  - `Classnote_by_Raidah/` and `Handnote_by_Fahim_2310002/` preserve original notebook pagination via `<!-- Page N -->` markers.
- **Diagrams & Metadata Sidecars:** All **544 JPG figures** across the repository live in local `diagrams/` folders and are paired with `<filename>.jpg.meta.json` sidecar files containing figure descriptions, source page/slide coordinates, and generator metadata.

