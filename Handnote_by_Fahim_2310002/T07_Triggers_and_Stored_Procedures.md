# T07: Triggers & Stored Procedures — Class Notes (Fahim)

**Course:** ECE 2215: Database Systems  
**Student:** Fahim (Roll: 2310002)  
**Instructors:** Mst. Nafia Islam Shishir (NIS MAM) & Md. Rakibul Islam (RI SIR)  
**Topic Reference:** Syllabus Unit 4 | `subtopicwise_list.md` T07 (27 marks · 4.2% · 5/7)  
**Source Pages:** Page 59 (Bottom), Page 60, Page 62

---

<!-- Page 59 -->

## Triggers

Trigger is a special kind of stored program that is automatically executed (triggered) when a specific event occurs in a table — such as `INSERT`, `UPDATE`, or `DELETE`.

### Triggers are commonly used for:

- Logging changes (audit trail)
- Enforcing additional business rules / integrity constraints
- Automatically updating related data

---

<!-- Page 60 -->

## Trigger Syntax

```sql
CREATE TRIGGER trigger_name
AFTER INSERT ON table_name
FOR EACH ROW
BEGIN
    statements to execute
END;
```

### Triggers can be fired:

- **BEFORE** or **AFTER** an event
- On **INSERT**, **UPDATE**, or **DELETE**

> [!NOTE] বাস্তব জীবনের উদাহরণ
> এইটা এমন যে employee এর salary বাড়লে hourly pay বাড়ে বা hourly pay বাড়লে salary বাড়বে automatically।

---

<!-- Page 62 -->

## Trigger (Overview & Structure)

- টেবিলের DML operation (`INSERT`, `UPDATE`, `DELETE`) এর উপর depend করে কাজ করে।
- কিছু command execute করে।
- একটি trigger always একটা table এই কাজ করে।

### Basic Structure

```sql
CREATE TRIGGER [trigger_name]
ON [table_name]
[AFTER / FOR / INSTEAD OF]
[INSERT / UPDATE / DELETE]
AS
{ trigger_body }
```
