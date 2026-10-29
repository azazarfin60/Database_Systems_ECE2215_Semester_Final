---
title: "T07 · Triggers and Stored Procedures · Explanations"
tags:
  - ece2215
  - database-systems
  - explanation
---

[← Prev: T06 · Joins and Views](T06_Joins_and_Views.md) | [Exam-style layer](../Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) | [Next: T08 · Normalization and Functional Dependencies →](T08_Normalization_and_Functional_Dependencies.md)

---

# T07 · Triggers and Stored Procedures

> [!info] Topic card
> **Syllabus:** Unit 4 · **Weight:** 27 final marks (4.2%) in 5/7 papers
> **Sources:** Textbook Ch. 5 §5.2–5.3 (no lecture slides for this topic)
> **Blocks in this file:** 6 final questions (4 blocks)

## Subtopics in this file

| ID | Subtopic | Marks (Finals + CT) | Questions | Jump |
| :-- | :-- | :--: | :-- | :-- |
| T07.1 | What a trigger is, its purposes, and its syntax | 9 + 0 | 2018 Q.8(a), 2020 Q.8(a) | [[#T07.1 · What a trigger is, its purposes, and its syntax\|Go]] |
| T07.2 | Triggers for security before and after a breach | 8 + 0 | 2017 Q.8(b), 2024 Q.2(a) | [[#T07.2 · Triggers for security before and after a breach\|Go]] |
| T07.3 | Implement a trigger or stored procedure | 10 + 0 | 2023 Q.6(b), 2024 Q.6(b) | [[#T07.3 · Implement a trigger or stored procedure\|Go]] |

---

## T07.1 · What a trigger is, its purposes, and its syntax

### 2018 Q.8(a) · 05 Marks

*Section B · Asked in: 2018, 2020 · L2 merge*

**Question (2018 Q.8(a)).** What is triggering? What are the purposes of using trigger? Write the syntax for creating trigger?

**Question (2020 Q.8(a)).** What is triggering? What are the purposes of using triggering? Write the syntax for creating a trigger.

**Answer.**

**What the examiner wants.**  
A complete three-part answer: the definition of trigger and triggering (1.5 marks), four distinct practical purposes (1.5 marks), and the exact syntax for creating a trigger (2 marks).

**Key idea.**  
A trigger is an automated stored routine. It wakes up when a table event occurs, tests an optional condition, and runs an action. Think of a smoke detector. When smoke appears (event), it checks whether smoke density is high (condition), and rings an alarm (action). This structure is the ECA model.

**Step-by-step solution.**  

#### 1. What is Triggering?

A **trigger** is a stored SQL block. The DBMS executes it automatically when a modification occurs on a table or view.

The automatic detection of the event and execution of the trigger action is called **triggering**.

Triggers follow the **ECA (Event-Condition-Action) model**:
- **Event:** A database modification (`INSERT`, `UPDATE`, or `DELETE`) that activates the trigger.
- **Condition:** An optional boolean test checked when the event occurs.
- **Action:** The SQL statements that run automatically if the condition is satisfied.

#### 2. Purposes of Using Triggers

1. **Enforcing Complex Integrity Constraints:** Triggers enforce business rules across multiple tables that standard table constraints (`CHECK`, `FOREIGN KEY`) cannot express.
2. **Auditing and Security:** Triggers automatically log sensitive operations into audit tables with user identity, timestamp, and before-and-after values.
3. **Maintaining Derived and Summary Data:** Triggers keep summary values synchronized across tables. For example, they update a student credit total or warehouse stock automatically.
4. **Automating Workflows and Alerts:** Triggers generate reorders when inventory falls below minimum levels, create notifications, or clean up related dependent records.

#### 3. Syntax for Creating a Trigger (MySQL 8)

**General Template:**

```sql
DELIMITER //

CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
BEGIN
    -- Trigger body statements
    -- Access row values via OLD.column_name and NEW.column_name
    -- Terminate and rollback on error using SIGNAL
END //

DELIMITER ;
```

- `BEFORE | AFTER`: Specifies whether the action executes before modifying table data or after the modification completes.
- `INSERT | UPDATE | DELETE`: Identifies the DML event that activates the trigger.
- `ON table_name`: Specifies the target table.
- `FOR EACH ROW`: Defines a row-level trigger that runs once for each affected row.
- `OLD` and `NEW`: Transition qualifiers that refer to column values before and after the change.

**Example (Enforcing non-negative stock before insert):**

```sql
DELIMITER //

CREATE TRIGGER trg_check_product_stock
BEFORE INSERT ON Products
FOR EACH ROW
BEGIN
    IF NEW.stock < 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: Stock level cannot be negative';
    END IF;
END //

DELIMITER ;
```

*Variant for 2020 Q.8(a) (4 marks):* The same definition, purposes, syntax template, and example answer the question directly.

**Check.**  
*Quick self-test:*
- Q: Why is `FOR EACH ROW` needed?  
  A: It instructs the database engine to fire the trigger logic individually for each row modified by the statement.
- Q: Which transition qualifiers are available during an `UPDATE` event?  
  A: Both `OLD` (values before the change) and `NEW` (values after the change).
- Q: Can an `INSERT` trigger access `OLD.column_name`?  
  A: No. There is no existing record before an insert, so `OLD` is undefined.

> [!warning] Common mistakes
> - Forgetting `DELIMITER //`, which causes MySQL command line tools to fail on the inner semicolons.
> - Confusing `BEFORE` and `AFTER` timing. Use `BEFORE` to validate or modify incoming data. Use `AFTER` to update secondary tables or write audit logs.
> - Omitting the ECA (Event-Condition-Action) model when explaining the core mechanism.
> - Using SQL:1999 standard syntax (`REFERENCING NEW ROW`, `WHEN (condition)`) in MySQL. MySQL 8 does not support these clauses and uses built-in `NEW.col` / `OLD.col` with `IF ... THEN` constructs instead.

**Exam tip.**  
Divide your answer into three clear numbered headings: Definition and ECA model, Purposes, and Syntax. This structure lets the examiner assign full marks quickly.

**Sources.**  
- [Textbook Ch. 5 §5.3](../Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md)

---

## T07.2 · Triggers for security before and after a breach

### 2017 Q.8(b) · 05 Marks

*Section B · Asked in: 2017, 2024 (CO2) · L2 merge*

**Question (2017 Q.8(b)).** Using examples, discuss how Trigger can contribute to the security of database, before and after a security breach.

**Question (2024 Q.2(a)).** Discuss how trigger can contribute to the security of database before and after a security breach. Explain with example.

**Answer.**

**What the examiner wants.**  
A structured analysis of database security in two distinct operational phases: prevention before a breach (2.5 marks) and auditing or forensics after a breach (2.5 marks). Both parts must provide practical SQL trigger examples.

**Key idea.**  
Think of `BEFORE` triggers as security guards stationed at the door. They check identity and inspect the request before letting changes touch the table. If anything looks wrong, they block the action on the spot. Think of `AFTER` triggers as security cameras. Once an action takes place, they record an unalterable log of who did what and when. This allows investigators to analyze the damage later.

**Step-by-step solution.**  

Triggers protect database security at two stages: proactive prevention before a breach and forensic auditing after a breach.

#### 1. Before a Security Breach: Prevention via BEFORE Triggers

`BEFORE` triggers act as real-time security gatekeepers. They evaluate incoming data modifications before changes reach the database.

- **Security Role:** They validate user identity, verify business timing, and inspect the values being written. If a policy violation appears, the trigger halts the transaction using `SIGNAL SQLSTATE '45000'`.
- **Key Contributions:**
  - Blocks unauthorized operations outside working hours.
  - Prevents illegal privilege escalation or unauthorized salary updates.
  - Validates and sanitizes input data to stop malicious updates.

**Example (Blocking salary changes outside working hours):**

```sql
DELIMITER //

CREATE TRIGGER trg_prevent_unauthorized_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary <> OLD.salary THEN
        IF CURRENT_TIME() NOT BETWEEN '09:00:00' AND '17:00:00' THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Security Alert: Salary edits outside office hours are blocked';
        END IF;
    END IF;
END //

DELIMITER ;
```

#### 2. After a Security Breach: Auditing and Forensics via AFTER Triggers

`AFTER` triggers execute immediately after a modification succeeds on a table.

- **Security Role:** If an attacker bypasses application checks, `AFTER` triggers write the unauthorized changes into an independent audit log table.
- **Key Contributions:**
  - Creates a tamper-evident audit trail capturing `USER()`, `NOW()`, the modified table, and both `OLD` and `NEW` column values.
  - Supplies forensic evidence to pinpoint how and when the attacker breached the system.
  - Helps administrators trace unauthorized modifications and restore corrupted data to its original state.

**Example (Logging security role modifications):**

```sql
DELIMITER //

CREATE TRIGGER trg_audit_role_change
AFTER UPDATE ON user_roles
FOR EACH ROW
BEGIN
    IF OLD.role <> NEW.role THEN
        INSERT INTO security_audit_log (
            user_id, old_role, new_role, changed_by, changed_at
        ) VALUES (
            OLD.user_id, OLD.role, NEW.role, USER(), NOW()
        );
    END IF;
END //

DELIMITER ;
```

*Short version for 2024 Q.2(a) (3 marks):* State how `BEFORE` triggers block unauthorized actions with `SIGNAL` and how `AFTER` triggers record tamper-evident audit logs with `USER()` and timestamps. Provide one concise trigger example.

**Check.**  
*Execution trace comparison:*
1. **Trace 1 (Before breach test):**  
   An unauthorized script executes `UPDATE employees SET salary = salary + 5000 WHERE employee_id = 101;` at 20:30.  
   The `BEFORE UPDATE` trigger checks `CURRENT_TIME()`. The time falls outside the 09:00 to 17:00 window. The trigger raises `SIGNAL SQLSTATE '45000'`. The database rolls back the transaction. The database table remains completely untouched.
2. **Trace 2 (After breach test):**  
   An attacker compromises credentials and runs `UPDATE user_roles SET role = 'admin' WHERE user_id = 42;`.  
   The update succeeds. The `AFTER UPDATE` trigger immediately fires and inserts `(42, 'user', 'admin', 'attacker_session', '2026-10-30 14:15:00')` into `security_audit_log`. The administrator queries this log to detect the breach, identify the compromised account, and revert the unauthorized role change.

> [!warning] Common mistakes
> - Writing general database security points (like firewalls or user passwords) instead of explaining trigger mechanisms.
> - Attempting to use an `AFTER` trigger to block an unauthorized update. By the time an `AFTER` trigger executes, the row modification has already taken place.
> - Forgetting to capture both `OLD` and `NEW` values in the audit table. Without `OLD` values, security administrators cannot revert corrupted data.

**Exam tip.**  
Split your answer cleanly into two bold sections: "Before a Breach (Prevention via BEFORE Triggers)" and "After a Breach (Auditing and Forensics via AFTER Triggers)". Provide one short SQL example for each section.

**Sources.**  
- [Textbook Ch. 5 §5.3](../Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md)

---

## T07.3 · Implement a trigger or stored procedure

### 2023 Q.6(b) · 06 Marks

*Section B · CLO2 · Asked in: 2023 · L1 (asked once)*

**Question.** Considering the tables (Products, Orders, and Auditlog) answer (i) and (ii).  
(i) Create a stored procedure to place an order consider stock availability, updates the stock.  
(ii) Create a trigger to log every stock update in the Auditlog table automatically.

**Answer.**

**What the examiner wants.**  
Implementation of two distinct database routines: a stored procedure that checks stock availability and places an order within a safe transaction (3 marks), and an automatic `AFTER UPDATE` trigger that logs every inventory change into an audit table (3 marks).

**Key idea.**  
The stored procedure coordinates the ordering workflow: it locks the item row, checks whether enough units exist, creates the order record, and reduces inventory. The trigger acts as an automatic observer: whenever product stock changes for any reason, it automatically writes a historical log entry.

**Step-by-step solution.**  

*Assumption: The table schemas are `Products(product_id, name, stock, price)`, `Orders(order_id, product_id, quantity, order_date)`, and `Auditlog(log_id, product_id, old_stock, new_stock, changed_at)`.*

#### (i) Stored Procedure to Place an Order

The stored procedure verifies available stock using row-level locking (`FOR UPDATE`), places the order, and reduces the inventory within a transaction:

```sql
DELIMITER //

CREATE PROCEDURE PlaceOrder (
    IN p_product_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE v_stock INT;

    START TRANSACTION;

    -- Lock the target product row to prevent concurrent race conditions
    SELECT stock INTO v_stock
    FROM Products
    WHERE product_id = p_product_id
    FOR UPDATE;

    -- Validate product existence and stock sufficiency
    IF v_stock IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: Product does not exist';
    ELSEIF v_stock < p_quantity THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: Insufficient stock available';
    ELSE
        -- Record the new order
        INSERT INTO Orders (product_id, quantity, order_date)
        VALUES (p_product_id, p_quantity, NOW());

        -- Deduct ordered quantity from stock
        UPDATE Products
        SET stock = stock - p_quantity
        WHERE product_id = p_product_id;

        COMMIT;
    END IF;
END //

DELIMITER ;
```

#### (ii) Trigger to Log Stock Updates Automatically

An `AFTER UPDATE` trigger detects when the `stock` column changes and writes an audit record to `Auditlog`:

```sql
DELIMITER //

CREATE TRIGGER trg_log_stock_update
AFTER UPDATE ON Products
FOR EACH ROW
BEGIN
    -- Log only when the stock quantity actually changes
    IF OLD.stock <> NEW.stock THEN
        INSERT INTO Auditlog (product_id, old_stock, new_stock, changed_at)
        VALUES (OLD.product_id, OLD.stock, NEW.stock, NOW());
    END IF;
END //

DELIMITER ;
```

**Check.**  
*Trace with concrete sample tuples:*
- Setup: `Products(101, 'Monitor', 10, 150.00)`.
- *Execution 1:* Client calls `CALL PlaceOrder(101, 3);`.  
  1. The procedure locks row 101. Available stock is $10 \ge 3$.  
  2. Inserts record into `Orders(order_id, 101, 3, NOW())`.  
  3. Updates `Products` setting `stock = 10 - 3 = 7`.  
  4. Commits transaction.  
  5. The update on `Products` automatically fires `trg_log_stock_update`. Since $\text{OLD.stock} (10) \neq \text{NEW.stock} (7)$, it inserts `(101, 10, 7, NOW())` into `Auditlog`.
- *Execution 2:* Client calls `CALL PlaceOrder(101, 20);`.  
  Current stock is 7. Since $7 < 20$, the procedure raises `SIGNAL SQLSTATE '45000'`. No order is inserted and stock stays at 7.

> [!warning] Common mistakes
> - Decrementing inventory without checking whether available stock is sufficient, which causes negative stock values.
> - Missing `FOR UPDATE` on the stock check query. Without locking, concurrent transactions could read the same stock and sell more items than available in the warehouse.
> - Attaching the audit trigger to `Orders` instead of `Products`. Stock can also change through restocking, supplier returns, or inventory audits. The trigger must monitor `Products`.

**Exam tip.**  
Always state an explicit schema assumption line right at the start when schemas are omitted in the question. Use distinct prefixes like `p_` for parameters and `v_` for local variables to prevent naming clashes with column names.

**Sources.**  
- [Textbook Ch. 5 §5.2–5.3](../Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md)

---

### 2024 Q.6(b) · 04 Marks

*Section B · CO3 · Asked in: 2024 · L1 (asked once)*

**Question.** An e-commerce system wants to automate actions when a new order is inserted such as updating stock and sending email. Implement a database trigger that handles this workflow.

**Answer.**

**What the examiner wants.**  
An `AFTER INSERT` trigger on the orders table that automates post-order actions: updating product inventory (2 marks) and queueing email dispatch (2 marks). The answer must address the architectural reality of sending emails from within a database.

**Key idea.**  
A database engine manages transactional data on disk. It cannot open network sockets or send SMTP emails directly. Doing so inside a database transaction would introduce huge network latencies, hold table locks, and create single points of failure. The standard engineering pattern updates stock directly and inserts an email job into an `email_queue` table. An external application service polls this queue and sends the actual email over the network.

**Step-by-step solution.**  

*Assumption: The tables are `orders(order_id, product_id, quantity, customer_email)`, `products(product_id, stock)`, and `email_queue(queue_id, recipient, subject, body, queued_at)`.*

A trigger runs inside the database engine and cannot send external emails directly.
Instead, the trigger updates product stock and inserts a row into an `email_queue` table. An external mailer application reads this queue and sends the email.

```sql
DELIMITER //

CREATE TRIGGER trg_after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- 1. Deduct ordered quantity from product stock
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE product_id = NEW.product_id;

    -- 2. Enqueue email notification for external mailer service
    INSERT INTO email_queue (recipient, subject, body, queued_at)
    VALUES (
        NEW.customer_email,
        'Order Confirmation',
        CONCAT('Your order #', NEW.order_id, ' for product #', NEW.product_id, ' (Qty: ', NEW.quantity, ') has been placed successfully.'),
        NOW()
    );
END //

DELIMITER ;
```

**Check.**  
*Trace with concrete sample tuples:*
- Setup: `products(5, 50)`.
- Client runs: `INSERT INTO orders VALUES (501, 5, 4, 'customer@example.com');`.
- Execution:
  1. Row is written to `orders`.
  2. `trg_after_order_insert` fires immediately.
  3. `products.stock` becomes $50 - 4 = 46$.
  4. A row is added to `email_queue` with recipient `'customer@example.com'` and order details.
- Result: Product inventory stays accurate and an email task is queued without stalling the database engine.

> [!warning] Common mistakes
> - Writing pseudocode functions like `SEND_EMAIL()` directly inside the trigger. Database engines do not provide native email delivery mechanisms without external queues or helper daemons.
> - Using `BEFORE INSERT` instead of `AFTER INSERT`. If the order insertion fails later, the stock would have been decremented erroneously.
> - Hardcoding customer email or product identifiers instead of referencing `NEW.customer_email` and `NEW.product_id`.

**Exam tip.**  
Include the single-line note explaining that triggers cannot dispatch network emails directly. Then show the message queue pattern. Examiners award full marks for this practical engineering insight.

**Sources.**  
- [Textbook Ch. 5 §5.3](../Textbook/Chapter_05_Advanced_SQL/Chapter%2005%20-%20Advanced%20SQL.md)

---

[← Prev: T06 · Joins and Views](T06_Joins_and_Views.md) | [Exam-style layer](../Topicwise_answers_exam_style/T07_Triggers_and_Stored_Procedures.md) | [Next: T08 · Normalization and Functional Dependencies →](T08_Normalization_and_Functional_Dependencies.md)
