# T12: Recovery System & RAID — Class Notes (Raidah)

**Course:** ECE 2215: Database Systems  
**Student:** Raidah (Roll: 2310035)  
**Topic Reference:** Syllabus Unit 7 | `subtopicwise_list.md` T12 (43 marks · 6.8% · 5/7 · 🟠)  
**Source Pages:** Pages 32 (Right), 33 (Left, Right)

---

## 1. Introduction to RAID

<!-- Page 32 (Right) -->

**RAID $\rightarrow$ Redundant Array of Independent Disks**
* Combines multiple physical disk drives into a single logical storage unit to provide performance improvement, fault tolerance, or both.

---

## 2. RAID Level Architectures

<!-- Page 32 (Right) & Page 33 (Left, Right) -->

### RAID 0 (Block-Level Data Striping)
Data blocks are striped cyclically across all disks without any redundancy or parity information.

![Fig_DBMS_p32_01: Hand-drawn RAID 0 architecture diagram showing block-level data stripping across Disk 0 and Disk 1](diagrams/DBMS_classnote_2310035_p32_fig01.jpg)
*Figure 32.1 — RAID 0: Block-level data striping across Disk 0 and Disk 1 (Page 32)*

* **Advantages:** High performance and high throughput. Reads and writes execute in parallel across multiple disks (no single disk becomes a bottleneck; I/O load is distributed across drives).
* **Disadvantages:** Zero fault tolerance; if any disk fails, all data is lost.

---

### RAID 1 (Disk Mirroring)
Data written to primary disk is completely duplicated (mirrored) onto an identical secondary disk.

![Fig_DBMS_p32_02: Hand-drawn RAID 1 architecture diagram showing data disk mirroring between Disk 0 and Disk 1](diagrams/DBMS_classnote_2310035_p32_fig02.jpg)
*Figure 32.2 — RAID 1: Disk mirroring between Disk 0 and Disk 1 (Page 32)*

* **Advantages:** High reliability and complete fault tolerance; system survives failure of one disk in the mirror pair.
* **Disadvantages:** Low storage efficiency (50% overhead since every disk requires a duplicate mirror).

---

### RAID 1+0 / RAID 10 (Striped Array of Mirrored Disks)
Combines the high fault tolerance of RAID 1 with the high I/O throughput of RAID 0 (RAID 0 striped across multiple RAID 1 mirror sets).

![Fig_DBMS_p32_03: Hand-drawn RAID 1+0 (RAID 10) architecture diagram showing striped array of mirrored disks (RAID 0 over RAID 1)](diagrams/DBMS_classnote_2310035_p32_fig03.jpg)
*Figure 32.3 — RAID 1+0 (RAID 10): Striped mirrored sets (Page 32)*

* **Architecture:** First create RAID 1 mirror pairs, then stripe them together using RAID 0.
* **Advantages:** High performance + High security and fault tolerance.

---

### RAID 3 (Bit-Interleaved Parity with Dedicated Parity Disk)

<!-- Page 33 (Left) -->

Data is divided and striped across data disks at the byte or bit level, while parity bits are written to a single dedicated parity disk.

![Fig_DBMS_p33_01: Hand-drawn RAID 3 architecture diagram showing bit-interleaved data stripping across Disks 0-2 with dedicated parity disk on Disk 3](diagrams/DBMS_classnote_2310035_p33_fig01.jpg)
*Figure 33.1 — RAID 3: Bit-interleaved parity disk (Page 33)*

* **Parity Disk:** `Disk 3` stores the computed parity for corresponding bits on `Disk 0`, `Disk 1`, and `Disk 2`.
* **Advantage:** If any single disk fails, the missing data can be reconstructed using the parity bit and data from the surviving disks.

---

### RAID 5 (Block-Interleaved Distributed Parity)

<!-- Page 33 (Left) -->

Data and parity blocks are distributed circularly across all disks in the array, eliminating the dedicated parity disk bottleneck.

![Fig_DBMS_p33_02: Hand-drawn RAID 5 architecture diagram showing block-interleaved distributed parity (AP, BP, CP, DP) across Disks 0-3](diagrams/DBMS_classnote_2310035_p33_fig02.jpg)
*Figure 33.2 — RAID 5: Block-interleaved distributed parity (Page 33)*

* **Parity Distribution:** Parity blocks $A_P, B_P, C_P, D_P$ are spread across `Disk 0` through `Disk 3`.
* **Advantage:** Balances data and performance (distributing parity prevents a single dedicated parity disk from becoming an I/O bottleneck).

---

### RAID 6 ($P + Q$ Dual Distributed Parity)

<!-- Page 33 (Right) -->

Extends RAID 5 by maintaining two independent parity computations ($P$ and $Q$ parity) distributed across all disks.

![Fig_DBMS_p33_03: Hand-drawn RAID 6 architecture diagram showing block-interleaved dual distributed parity (P+Q parity: Ap/Aq, Bp/Bp, Cp/Cq, Dp/Dq) across Disks 0-4](diagrams/DBMS_classnote_2310035_p33_fig03.jpg)
*Figure 33.3 — RAID 6: Dual distributed parity (Page 33)*

* **Parity Blocks:** $A_P, A_Q, B_P, B_Q, \dots$ computed via independent mathematical algorithms (XOR and Reed-Solomon codes).
* **Advantage:** No data is lost even if two disks fail simultaneously (survives 2 concurrent disk failures).

