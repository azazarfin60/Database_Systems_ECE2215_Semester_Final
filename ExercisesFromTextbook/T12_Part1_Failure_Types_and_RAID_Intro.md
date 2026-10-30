---
title: "T12 · Recovery System and RAID (Part 1 · Failure Classification & Storage Crash Scenarios)"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T12
topic_id: T12
part: 1
exercise_count: 14
source_chapters:
  - "Chapter 12"
  - "Chapter 19"
---

[← Prev: T11 Part 3](T11_Part3_Deadlock_and_Timestamp_Ordering.md) | [Exam-style T12](../Topicwise_answers_exam_style/T12_Recovery_System_and_RAID.md) | [Next: T12 Part 2 →](T12_Part2_Recovery_Manager_and_Log_Recovery.md)

---

# T12 · Recovery System and RAID (Part 1 · Failure Classification & Storage Crash Scenarios)

> [!info] Topic Card
> - **Syllabus Unit:** Unit 7 (Recovery System & RAID)
> - **Topic Weight in RUET Exams:** 43 printed marks (6.8% total final share) across 5 of 7 recent semester finals
> - **Primary Source Texts:** Silberschatz 7e Chapter 12 (*Physical Storage Systems*, §12.1–§12.5) and Chapter 19 (*Recovery System*, §19.1–§19.3, §19.8)
> - **Scope of Part 1:** 14 assigned exercises covering storage hierarchies, access latencies, disk geometry, flash FTL mapping, atomic block writes under RAID 1 and RAID 5, interactive transaction recovery, partial block write detection, storage type I/O costs, stable storage limits, and disaster classification.

---

## Exercise Directory

| Exercise | Source | Focus / Concept | Key RUET Links |
| :--- | :--- | :--- | :--- |
| **PE 12.1** | Ch. 12 | SSD as storage tier vs. caching layer for magnetic disks | Memory hierarchy, query SLA |
| **PE 12.2** | Ch. 12 | Outer track sector allocation and short-stroking | Disk bandwidth, seek reduction |
| **PE 12.3** | Ch. 12 | Flash translation table (FTL), sizing, and extent compression | FTL memory overhead, storage systems |
| **PE 12.6** | Ch. 12 | Atomic block writes during power failure in RAID 1 and RAID 5 | 2018 Q.5(c), 2023 Q.7(c) |
| **PE 12.7** | Ch. 12 | Consecutive block allocation limits and OS extent policies | Disk fragmentation, I/O clustering |
| **PE 19.10** | Ch. 19 | Recovery of interactive transactions vs. batch transactions (ATM) | 2019 Q.4(b), 2024 Q.3(b) |
| **PE 19.12** | Ch. 19 | Torn writes, detection techniques, and RAID 1 recovery | 2018 Q.5(c), RAID precautions |
| **EX 12.8** | Ch. 12 | Storage media hierarchy and empirical access speeds | Storage latency gap, memory tiers |
| **EX 12.9** | Ch. 12 | Bad-sector remapping impact on data retrieval rates | Media defects, disk controllers |
| **EX 12.10** | Ch. 12 | Consecutive block placement: Magnetic disks vs. SSDs | Seek overhead, flash parallelism |
| **EX 19.14** | Ch. 19 | Volatile, nonvolatile, and stable storage I/O cost analysis | 2017 Q.6(c), storage classification |
| **EX 19.15** | Ch. 19 | Theoretical impossibility of stable storage and practical methods | 2019 Q.4(b), durability safeguards |
| **EX 19.26** | Ch. 19 | System crash vs. disaster classification | 2017 Q.6(c), 2023 Q.7(a) |
| **EX 19.27** | Ch. 19 | Remote backup systems: Durability degrees and trade-offs | Site failure, disaster recovery |

---

## T12.1 · Failure classification, precautions, recovery methods

### Exercise 12.1 · SSD Storage Layer versus Caching for Magnetic Disks

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Practice Exercise 12.1
> - **RUET Topic Mapping:** T12.1 (Failure classification, precautions, recovery methods) & Storage Architectures
> - **Related RUET Questions:** 2017 Q.6(c), 2019 Q.4(b), 2024 Q.3(b)

**Question (Silberschatz 7e Practice Exercise 12.1).**
SSDs can be used as a storage layer between memory and magnetic disks, with some parts of the database (e.g., some relations) stored on SSDs and the rest on magnetic disks. Alternatively, SSDs can be used as a buffer or cache for magnetic disks; frequently used blocks would reside on the SSD layer, while infrequently used blocks would reside on magnetic disk.
a. Which of the two alternatives would you choose if you need to support real-time queries that must be answered within a guaranteed short period of time? Explain why.
b. Which of the two alternatives would you choose if you had a very large *customer* relation, where only some disk blocks of the relation are accessed frequently, with other blocks rarely accessed.

#### 1. Core Principles & Concept Overview

Solid-state drives (SSDs) bridge the performance gap between volatile DRAM and magnetic disks. A database architect can deploy SSDs in two distinct roles:

1. **Storage Tiering (Storage Layer):** The database assigns specific relations, indices, or tablespaces to SSDs permanently. The placement is static and explicit. Data on SSD stays on SSD until a database administrator moves it.
2. **Caching Layer (Buffer / Secondary Cache):** The SSD acts as an automatic, transparent cache for magnetic disk blocks. Data moves between magnetic disk and SSD dynamically. It uses replacement policies like Least Recently Used (LRU) or Least Frequently Used (LFU).

```text
Alternative 1: Tiered Storage (Static Partitioning)
┌──────────────────────────────────────────────┐
│ Main Memory (DRAM Buffer Pool)               │
└──────────────────────┬───────────────────────┘
           ▲           │
           │           ▼
   ┌───────┴───────────────┬───────────────────┐
   │                       │                   │
   ▼                       ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Fast SSD    │    │ Magnetic HDD │    │ Magnetic HDD │
│ Table A, B   │    │ Table C      │    │ Table D      │
└──────────────┘    └──────────────┘    └──────────────┘

Alternative 2: SSD Caching Layer (Dynamic Block Migration)
┌──────────────────────────────────────────────┐
│ Main Memory (DRAM Buffer Pool)               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ SSD Cache (Hot Blocks of Tables A, B, C, D)  │
└──────────────────────┬───────────────────────┘
                       │ Cache Miss Fetch
                       ▼
┌──────────────────────────────────────────────┐
│ Magnetic Disk (Cold Full Working Storage)    │
└──────────────────────────────────────────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Real-Time Queries with Guaranteed Latency Bounds

- **Choice:** Select **Alternative 1 (Storage Layer / Explicit Tiering)**.
- **Reasoning:**
  - Real-time systems require hard or firm upper bounds on query execution times. The database must guarantee that worst-case latency stays below a strict threshold.
  - In Alternative 2 (caching), block placement depends on dynamic runtime cache hits and misses. If a query hits the SSD cache, read latency is fast ($\approx 50\ \mu\text{s}$ to $100\ \mu\text{s}$). But if a query experiences a cache miss, the system must fetch the missing block from magnetic disk.
  - A magnetic disk fetch requires a mechanical seek and rotational delay. This costs $5\text{ ms}$ to $10\text{ ms}$. This latency spike is roughly 100 times slower than an SSD read. Such an unexpected delay violates real-time deadlines.
  - In Alternative 1, the database administrator places all relations and indices involved in real-time queries permanently on the SSD storage layer.
  - Every access is guaranteed to hit the SSD. No request can ever trigger a slow magnetic disk seek. The worst-case latency remains strictly bounded and predictable.

##### Part (b): Very Large Customer Relation with Skewed Access

- **Choice:** Select **Alternative 2 (SSD Buffer / Caching Layer)**.
- **Reasoning:**
  - In a very large customer relation, total data volume is massive. Storing the entire relation on SSD under Alternative 1 is uneconomical. SSD storage costs significantly more per gigabyte than magnetic disk storage.
  - Most customer records are inactive or rarely accessed. Only a small fraction of "hot" records (recent active users, current open orders) are accessed frequently.
  - Under Alternative 1, relations are placed on storage devices as whole files. The database would have to keep the entire relation on SSD. That wastes expensive high-speed storage on cold, idle rows.
  - Under Alternative 2, the SSD caches data at the block level. The system automatically migrates only the frequently accessed customer blocks into the SSD cache. Infrequently accessed blocks stay on cheaper magnetic disks.
  - This approach maximizes cache hit rates while minimizing hardware cost per gigabyte.

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions on database failure and physical storage often ask how hardware choices affect transaction latency.
- State clearly that Alternative 1 guarantees predictable worst-case bounds. State that Alternative 2 optimizes average throughput per unit cost.
- Examiners look for the contrast between deterministic latency (needed for real-time SLAs) and statistical caching efficiency.

---

### Exercise 12.2 · Outer Track Sector Allocation on Magnetic Disks

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Practice Exercise 12.2
> - **RUET Topic Mapping:** T12.1 (Precautions against I/O bottlenecks) & Physical Storage
> - **Related RUET Questions:** 2017 Q.6(c), 2019 Q.4(b)

**Question (Silberschatz 7e Practice Exercise 12.2).**
Some databases use magnetic disks in a way that only sectors in outer tracks are used, while sectors in inner tracks are left unused. What might be the benefits of doing so?

#### 1. Core Principles & Concept Overview

Magnetic disk platters rotate around a central spindle at a Constant Angular Velocity (CAV). Common speeds include 7200 RPM and 15000 RPM. A track near the outer edge of the platter has a much larger circumference than a track near the center:

$$
C_{\text{outer}} = 2\pi r_{\text{outer}} \gg C_{\text{inner}} = 2\pi r_{\text{inner}}
$$

Modern magnetic hard disks use **Zoned Bit Recording (ZBR)**. Because linear recording density (bits per inch) is kept roughly constant across the platter surface, outer tracks hold significantly more sectors than inner tracks.

```text
Disk Platter Geometry (Zoned Bit Recording)
           . - ~ ~ ~ - .
       . '   Outer Track ' .        <-- Maximum circumference, most sectors/track,
     /      (High Speed)     \          highest transfer rate (MB/s).
    /         . - - .         \
   /        /  Inner  \        \    <-- Minimum circumference, fewest sectors/track,
  |        |   Track   |        |       lowest transfer rate.
   \        \         /        /
    \         ' - - '         /
     \                       /
       ' .                 ' .
           ' - ~ ~ ~ - '
     <------> Short-Stroke Range (Confined arm travel = 1-3 ms seek)
```

#### 2. Detailed Step-by-Step Solution

Using only the sectors on outer tracks provides two primary performance benefits:

##### Benefit 1: Higher Data Transfer Rate (Increased Bandwidth)

- The disk rotates at constant angular speed $\omega = 2\pi \cdot (\text{RPM} / 60)$.
- One complete rotation takes a fixed time period:

$$
T_{\text{rot}} = \frac{60}{\text{RPM}}
$$

- For a 7200 RPM drive, $T_{\text{rot}} \approx 8.33\text{ ms}$. For a 15000 RPM drive, $T_{\text{rot}} = 4.0\text{ ms}$.
- Because outer tracks have larger circumferences, they store more sectors than inner tracks.
- When the read head stays over an outer track, it reads more sectors per rotation than over an inner track.
- The sustained data transfer rate is directly proportional to track radius:

$$
\text{Data Transfer Rate} = \frac{\text{Bytes per Track}}{T_{\text{rot}}} \propto r
$$

- Outer tracks often deliver $1.5\times$ to $2\times$ higher sequential read and write speeds compared to inner tracks on the same drive.

##### Benefit 2: Reduced Seek Times ("Short-Stroking")

- Seek time is the time needed to move the mechanical read/write head arm between cylinders.
- A full-stroke seek across the entire platter takes $15\text{ ms}$ to $20\text{ ms}$. An average random seek takes $8\text{ ms}$ to $10\text{ ms}$.
- If the database uses only the outer tracks (for example, the outermost 10% to 20% of cylinders), the actuator arm never moves across the full platter radius.
- Restricting arm movement to a narrow radial zone is known as **short-stroking**.
- Short-stroking reduces average seek time down to $1\text{ ms}$ to $3\text{ ms}$. This yields a massive increase in random I/O operations per second (IOPS).

##### Trade-Off Analysis

- The database sacrifices raw storage capacity because inner tracks remain unformatted or unused.
- But for write-ahead log (WAL) disks and high-throughput transaction processing, I/O speed is far more important than raw gigabyte capacity.

#### 3. RUET Exam Insights & Examiner Notes

- When explaining magnetic disk physics, always mention **Zoned Bit Recording (ZBR)** and **Constant Angular Velocity (CAV)**.
- State both benefits: sustained transfer bandwidth and reduced seek latency via short-stroking.
- This concept connects directly to database logging. Dedicated log disks use outer tracks to append log records with near-zero seek overhead.

---

### Exercise 12.3 · Flash Translation Table Sizing, Memory Creation, and Extent Compression

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Practice Exercise 12.3
> - **RUET Topic Mapping:** T12.1 (Storage precautions & controller architecture)
> - **Related RUET Questions:** Storage systems, physical database design

**Question (Silberschatz 7e Practice Exercise 12.3).**
Flash storage:
a. How is the flash translation table, which is used to map logical page numbers to physical page numbers, created in memory?
b. Suppose you have a 64-gigabyte flash storage system, with a 4096-byte page size. How big would the flash translation table be, assuming each page has a 32-bit address, and the table is stored as an array?
c. Suggest how to reduce the size of the translation table if very often long ranges of consecutive logical page numbers are mapped to consecutive physical page numbers.

#### 1. Core Principles & Concept Overview

NAND flash memory cannot overwrite data in place. An existing page must be erased before writing new data. But while reads and writes occur at the **page level** (typically 4 KB), erase operations occur only at the **block level** (typically 2 MB to 8 MB).

To handle this asymmetry, the Flash Translation Layer (FTL) performs out-of-place writes. It remaps logical page numbers (LPN) exposed to the operating system to different physical page numbers (PPN) in flash. The mapping is stored in the **flash translation table**.

```text
Logical vs. Physical Page Mapping in Flash Memory
Logical Page Numbers (OS View)         Physical Flash Pages (Chip View)
┌──────────────┐                       ┌──────────────┐
│  LPN 0       ├──────────────────────►│  PPN 512     │ (Block 2, Page 0)
├──────────────┤                       ├──────────────┤
│  LPN 1       ├──────────────────────►│  PPN 513     │ (Block 2, Page 1)
├──────────────┤                       ├──────────────┤
│  LPN 2       ├───────────┐           │  PPN 108     │ (Stale / Invalid)
├──────────────┤           │           ├──────────────┤
│  LPN 3       ├─────┐     └──────────►│  PPN 940     │ (Block 4, Page 12)
└──────────────┘     │                 ├──────────────┤
                     └────────────────►│  PPN 941     │ (Block 4, Page 13)
                                       └──────────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): How the Flash Translation Table is Created in Memory

- Because flash storage controller RAM is volatile, the translation table is rebuilt or restored upon power-up.
- SSD controllers use a two-part mechanism:
  1. **Periodic Mapping Checkpoints:** The controller periodically writes snapshots of the translation table to dedicated flash blocks.
  2. **Out-of-Band (OOB) Metadata Scan:** Each physical flash page has a small spare area (typically 64 to 512 bytes). This area stores error-correcting codes (ECC) and the **logical page number (LPN)** written to that physical page.
  3. **Power-On Reconstruction:** At system boot, the controller loads the latest checkpoint into RAM. Then it scans the spare areas of all flash blocks written after that checkpoint. It replays the updates to restore the latest mapping table.

##### Part (b): Exact Translation Table Sizing Calculation

Given parameters:
- Total storage capacity: $C = 64\text{ GB} = 64 \times 2^{30}\text{ bytes} = 68,719,476,736\text{ bytes}$
- Page size: $P = 4096\text{ bytes} = 2^{12}\text{ bytes}$
- Entry size: $E = 32\text{ bits} = 4\text{ bytes}$ per physical address

**Step 1: Compute the total number of logical pages ($N$):**

$$
N = \frac{C}{P} = \frac{64 \times 2^{30}\text{ bytes}}{4096\text{ bytes}} = \frac{2^6 \times 2^{30}}{2^{12}} = 2^{24}\text{ pages}
$$

$$
N = 16,777,216\text{ pages}
$$

**Step 2: Compute the size of the translation array ($S$):**

$$
S = N \times E = 2^{24} \times 4\text{ bytes} = 2^{26}\text{ bytes}
$$

$$
S = \frac{2^{26}}{2^{20}}\text{ MB} = 2^6\text{ MB} = 64\text{ MB}
$$

- The flash translation table requires exactly **64 MB** of controller RAM.
- For a 1 TB drive, this scaling demands 1 GB of fast controller RAM, which adds significant cost.

##### Part (c): Reducing Translation Table Size via Extent Mapping

- If consecutive logical page numbers map to consecutive physical page numbers, the controller can use **extent-based (range-based) mapping**.
- Instead of storing one 4-byte entry for every individual 4 KB page, the table stores an extent descriptor:

$$
\langle \text{Start\_LPN},\ \text{Start\_PPN},\ \text{Length} \rangle
$$

- For example, if logical pages 1,000 to 1,255 map contiguously to physical pages 50,000 to 50,255:
  - Flat table: $256 \times 4\text{ bytes} = 1024\text{ bytes}$.
  - Extent descriptor: $\langle 1000,\ 50000,\ 256 \rangle$, which needs only 12 bytes.
  - Storage reduction: Over 98% memory savings for sequential allocations.
- Controllers organize these extents using balanced search trees (such as $B^+$-trees) in memory. They can also use hybrid mapping (page-level for random writes, block-level for sequential writes).

#### 3. RUET Exam Insights & Examiner Notes

- Always present the numerical calculation with powers of 2. Show the unit conversions clearly from bytes to megabytes.
- For part (a), mention both the checkpoint snapshot and the Out-of-Band (OOB) spare area scan.
- For part (c), use the standard database term **extent**. This links directly to file system allocation and table storage.

---

### Exercise 12.6 · Atomic Block Writes during Power Failure in RAID 1 and RAID 5

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Practice Exercise 12.6
> - **RUET Topic Mapping:** T12.1 (Precautions & atomic writes) & T12.4 (RAID recovery role)
> - **Related RUET Questions:** 2018 Q.5(c), 2023 Q.7(c)

**Question (Silberschatz 7e Practice Exercise 12.6).**
A power failure that occurs while a disk block is being written could result in the block being only partially written. Assume that partially written blocks can be detected. An atomic block write is one where either the disk block is fully written or nothing is written (i.e., there are no partial writes). Suggest schemes for getting the effect of atomic block writes with the following RAID schemes. Your schemes should involve work on recovery from failure.
a. RAID level 1 (mirroring)
b. RAID level 5 (block interleaved, distributed parity)

#### 1. Core Principles & Concept Overview

A disk block write spans multiple hardware magnetic or flash sectors. A sudden power loss mid-write causes a **torn write** (partial write). Some sectors contain new data, while others retain old data or corrupted ECC codes.

An **atomic block write** provides an all-or-nothing guarantee:
- Either the block reaches its fully updated new state ($B_{\text{new}}$).
- Or the block cleanly retains its undamaged prior state ($B_{\text{old}}$).

```text
Torn Write Vulnerability vs. Atomic Mirror Protocol
Unsafe Simultaneous Write:
Disk 1: [ Sector 1 (New) | Sector 2 (New) | Sector 3 (Old) ] <-- TORN WRITE!
Disk 2: [ Sector 1 (Old) | Sector 2 (Old) | Sector 3 (Old) ] <-- Power dies!

Ordered Safe RAID 1 Write Protocol:
Step 1: Write Disk 1 completely ──► Verify CRC ──► OK!
Step 2: Write Disk 2 completely ──► Verify CRC ──► OK!
Crash during Step 1? Disk 2 has valid B_old. Restore Disk 1 from Disk 2.
Crash during Step 2? Disk 1 has valid B_new. Restore Disk 2 from Disk 1.
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Atomic Block Writes in RAID 1 (Mirroring)

In RAID 1, every logical block is mirrored across two identical physical disks: Primary ($D_1$) and Secondary ($D_2$).

**1. Normal Write Protocol:**
- Never write to both disks at the exact same instant.
- Step 1: Write the updated block $B_{\text{new}}$ to disk $D_1$.
- Step 2: Wait for $D_1$ to complete the write and verify its checksum.
- Step 3: Write $B_{\text{new}}$ to disk $D_2$.
- Step 4: Acknowledge write completion to the operating system once both finish.

**2. Crash Recovery Protocol:**
- On power restoration, inspect corresponding blocks on $D_1$ and $D_2$ using error-detecting checksums.
- **Scenario 1 (Crash during Step 1):** Disk $D_1$ contains a partially written block. But disk $D_2$ was not yet touched and holds the valid $B_{\text{old}}$.
  - *Recovery action:* Copy $B_{\text{old}}$ from $D_2$ onto $D_1$. The block cleanly retains its old value.
- **Scenario 2 (Crash during Step 3):** Disk $D_1$ completed successfully and holds valid $B_{\text{new}}$. But disk $D_2$ suffered a partial write.
  - *Recovery action:* Copy $B_{\text{new}}$ from $D_1$ onto $D_2$. The block cleanly adopts its new value.
- **Scenario 3 (Both blocks valid but differ):** If $D_1$ has $B_{\text{new}}$ and $D_2$ has $B_{\text{old}}$ (crash occurred between Step 2 and Step 3), copy $D_1$ to $D_2$.

This protocol guarantees that no torn block ever persists. The write is strictly atomic.

##### Part (b): Atomic Block Writes in RAID 5 (Distributed Parity)

In RAID 5, updating a data block $D$ requires updating both the data block and its corresponding parity block $P$:

$$
P_{\text{new}} = P_{\text{old}} \oplus D_{\text{old}} \oplus D_{\text{new}}
$$

If power fails between writing $D$ and writing $P$, the stripe suffers the **RAID 5 write hole**. Parity becomes inconsistent with data.

**1. Normal Write Protocol using an Intention Log:**
- Use a dedicated non-volatile intent log (in battery-backed NVRAM or on a reserved disk log track).
- Step 1: Write an intention record to the non-volatile log:

$$
\langle \text{stripe\_id},\ \text{block\_id},\ D_{\text{new}},\ D_{\text{old}},\ P_{\text{new}} \rangle
$$

- Step 2: Flush the log record to stable storage.
- Step 3: Write the new data block $D_{\text{new}}$ to its target disk.
- Step 4: Write the new parity block $P_{\text{new}}$ to its target disk.
- Step 5: Mark the intention record as complete in the log.

**2. Crash Recovery Protocol:**
- On reboot, scan the intent log for incomplete operations:
- **Case 1 (Torn write on data block $D$):**
  - The controller detects a checksum failure on $D$.
  - It reconstructs $D_{\text{old}}$ using the surviving data blocks in the stripe and the unmodified parity block $P_{\text{old}}$:

$$
D_{\text{old}} = P_{\text{old}} \oplus \bigoplus_{j \neq \text{target}} D_j
$$

  - The controller overwrites the torn block with $D_{\text{old}}$ and discards the pending write.
- **Case 2 (Data write succeeded, but parity write $P$ was torn):**
  - Read $P_{\text{new}}$ directly from the intent log and write it to the parity disk. Or recompute parity using the valid $D_{\text{new}}$:

$$
P_{\text{new}} = \bigoplus_{\text{all } i} D_i
$$

- **Result:** In all crash scenarios, the stripe returns to a valid, self-consistent state. The block write behaves atomically.

#### 3. RUET Exam Insights & Examiner Notes

- This question is a favorite for RUET final questions on RAID reliability (such as 2018 Q.5(c) and 2023 Q.7(c)).
- Always state the **write ordering invariant**: never write to mirror disks simultaneously.
- Mention the **RAID 5 write hole** and how battery-backed NVRAM or write-ahead logging prevents parity corruption.

---

### Exercise 12.7 · Consecutive Block Allocation for Large Files and OS Extent Strategies

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Practice Exercise 12.7
> - **RUET Topic Mapping:** T12.1 (Storage precautions & physical file layout)
> - **Related RUET Questions:** Disk file management, performance precautions

**Question (Silberschatz 7e Practice Exercise 12.7).**
Storing all blocks of a large file on consecutive disk blocks would minimize seeks during sequential file reads. Why is it impractical to do so? What do operating systems do instead, to minimize the number of seeks during sequential reads?

#### 1. Core Principles & Concept Overview

Sequential file reads achieve maximum throughput when blocks reside on contiguous physical sectors. The disk head reads data continuously along a cylinder without moving the mechanical arm. But strictly contiguous allocation faces fundamental file system constraints.

```text
External Fragmentation & Allocation Dilemma
Physical Disk Blocks:
[ File A (3 MB) ] [ Free Hole (2 MB) ] [ File B (5 MB) ] [ Free Hole (1 MB) ]
                   ▲                                      ▲
                   └─ Cannot place a new 4 MB file here! ─┘
Total free space = 3 MB, but maximum contiguous hole = 2 MB!
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Why Strictly Consecutive Allocation is Impractical

1. **Dynamic File Growth:**
   - Database files, table spaces, and logs grow over time as transactions insert new records.
   - If a file is allocated contiguously, the disk space immediately following its last block may already belong to another file.
   - To grow the file, the operating system would have to relocate the entire file to a larger free region. Copying multi-gigabyte database files on every append operation causes intolerable I/O overhead.
2. **External Fragmentation:**
   - As files of varying sizes are created, expanded, and deleted, free disk space breaks into scattered non-contiguous segments.
   - Even when total free space on disk is large, the system may have no single contiguous block run large enough to hold a new file.
3. **Internal Fragmentation from Over-Allocation:**
   - To avoid relocation, the system would have to pre-allocate massive contiguous blocks based on guessed maximum sizes. If the file never uses that space, the unused capacity is wasted.

##### Part (b): What Operating Systems and DBMS Engines Do Instead

Modern file systems (such as Linux ext4, XFS, and NTFS) and database storage engines use several techniques:

1. **Extent-Based Allocation:**
   - Files are allocated as a collection of **extents**. An extent is a contiguous sequence of disk blocks (for example, 64 KB, 1 MB, or 8 MB).
   - Seeks occur only when moving between different extents. Within an extent, reads proceed sequentially at full platter speed.
   - This drastically cuts seek frequency while allowing files to grow by adding new extents anywhere on disk.
2. **Cylinder Groups and Block Groups:**
   - The OS partitions disk space into cylinder groups (as in Unix FFS and Linux ext4).
   - The file system allocates data blocks and metadata (inodes) for the same file within the same cylinder group.
   - This keeps seeks short and localized. The disk arm moves across only a few adjacent tracks rather than the full disk diameter.
3. **Delayed Allocation:**
   - When transactions generate dirty pages, the OS does not allocate disk blocks immediately.
   - It buffers data in RAM and waits until flushing large dirty page groups to disk.
   - This lets the allocator inspect the total write size at once and assign large, contiguous extents.
4. **Database File Pre-allocation:**
   - Database systems pre-allocate massive files upfront using system calls like `posix_fallocate()`.
   - The operating system reserves contiguous extents before active transaction processing begins.

#### 3. RUET Exam Insights & Examiner Notes

- Contrast naive single-block allocation with extent-based clustering.
- Note that extent-based allocation strikes a practical balance: it minimizes mechanical seek frequency without causing crippling external fragmentation.

---

### Exercise 19.10 · Recovery of Interactive Transactions versus Batch Transactions

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Practice Exercise 19.10
> - **RUET Topic Mapping:** T12.1 (Failure classification & recovery methods) & ACID Durability
> - **Related RUET Questions:** 2017 Q.6(c), 2019 Q.4(b), 2024 Q.3(b)

**Question (Silberschatz 7e Practice Exercise 19.10).**
Explain the reasons why recovery of interactive transactions is more difficult to deal with than is recovery of batch transactions. Is there a simple way to deal with this difficulty? (Hint: Consider an automatic teller machine transaction in which cash is withdrawn.)

#### 1. Core Principles & Concept Overview

Database recovery mechanisms rely on restoring internal data states:
- Undo restores old values from log records.
- Redo applies new values from log records.

This model assumes that all transaction effects exist solely as internal bits on volatile or non-volatile computer storage.

An **interactive transaction** interacts with the external physical world. It outputs information to human users, prints paper receipts, or commands physical actuators.

```text
The Real-World Boundary Problem in Transaction Recovery
Database Domain (Reversible)            External World (Irreversible)
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ Log Record: <T1, A, 1000, 500>│       │ Physical ATM Cash Dispenser   │
│ Buffer Page: Account A = 500  │       │ 500 USD Cash Delivered to User!│
└──────────────┬────────────────┘       └──────────────┬────────────────┘
               │                                       │
      Crash occurs here!                      Can software suck
  Undo phase restores A = 1000.               the cash back? NO!
```

#### 2. Detailed Step-by-Step Solution

##### Step 1: Why Interactive Transactions Are Harder to Recover

1. **Irreversible Real-World Actions:**
   - External physical actions cannot be rolled back by database software.
   - *ATM Example:* Consider an ATM cash withdrawal transaction $T_1$. The customer requests 500 dollars. The ATM cash dispenser mechanically ejects physical currency into the customer's hands.
   - Suppose the system crashes immediately after dispensing cash, before writing the log record $\langle T_1\text{ commit}\rangle$ to stable storage.
   - On reboot, the recovery manager sees $T_1$ as an uncommitted, active transaction. Standard recovery rules dictate rolling back $T_1$. The recovery manager restores the customer's account balance to its pre-withdrawal level.
   - The customer walks away with 500 dollars in cash, while the database shows no money was withdrawn. The bank suffers an unrecoverable financial loss.
2. **Human User Communication:**
   - If an interactive query displays an interim message ("Payment Approved") on a screen and then aborts, the user acts on false information. Human actions cannot be undone by software rollback.

##### Step 2: The Solution / How to Deal with This Difficulty

Database and banking systems solve this problem through two primary design rules:

1. **Deferred External Output (Commit-Then-Act Principle):**
   - The system postpones all irreversible physical actions until **after** the transaction successfully commits to stable storage.
   - In an ATM transaction:
     - Phase 1: Check account balance, verify PIN, and log the balance deduction.
     - Phase 2: Force the commit record $\langle T_1\text{ commit}\rangle$ to stable storage.
     - Phase 3: Only after the database confirms the commit on stable disk, send the hardware control signal to dispense physical cash.
2. **Idempotent Physical Dispensing & Resumption Logs:**
   - If the system crashes after Phase 2 but before or during Phase 3, recovery detects that $T_1$ committed.
   - A specialized hardware state machine checks whether cash was dispensed:
     - If not dispensed, it completes the cash ejection.
     - If cash jammed, it initiates a semantic **compensating transaction** to re-credit the customer's account and alerts technical support.
3. **Compensating Transactions (Sagas):**
   - When real-world outputs cannot be deferred, systems use business-level compensating transactions. For example, if an erroneous airline ticket is printed, the system does not roll back the database silently; it executes a cancellation workflow and issues a refund notice.

#### 3. RUET Exam Insights & Examiner Notes

- This question demonstrates the limits of classical write-ahead logging when software touches hardware actuators.
- Emphasize the **Deferred Output Rule**: never trigger external physical outputs until the transaction commit log record is safely written to stable storage.
- Connect this to RUET questions on ACID properties, specifically the real-world boundary of the Durability and Atomicity guarantees.

---

### Exercise 19.12 · Partial Block Writes (Torn Writes), Detection, and RAID 1 Recovery

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Practice Exercise 19.12
> - **RUET Topic Mapping:** T12.1 (Failure classification & precautions) & T12.4 (RAID recovery)
> - **Related RUET Questions:** 2018 Q.5(c), 2019 Q.4(b), 2024 Q.3(b)

**Question (Silberschatz 7e Practice Exercise 19.12).**
The recovery techniques that we described assume that blocks are written atomically to disk. However, a block may be partially written when power fails, with some sectors written, and others not yet written.
a. What problems can partial block writes cause?
b. Partial block writes can be detected using techniques similar to those used to validate sector reads. Explain how.
c. Explain how RAID 1 can be used to recover from a partially written block, restoring the block to either its old value or to its new value.

#### 1. Core Principles & Concept Overview

Database engines treat a database block (typically 4 KB, 8 KB, or 16 KB) as the atomic unit of I/O transfer. But physical disk hardware writes data in smaller sectors (historically 512 bytes, now 4 KB advanced format).

If power cuts out in the middle of writing a 16 KB block, only some sectors reach disk. This event is called a **torn write**.

```text
Anatomy of a Torn Block Write
16 KB Database Block (Four 4 KB Sectors):
┌────────────────┬────────────────┬────────────────┬────────────────┐
│ Sector 0 (New) │ Sector 1 (New) │ Sector 2 (Old) │ Sector 3 (Old) │
│ Page Header    │ Data Rows      │ Data Rows      │ Page Trailer   │
│ PageLSN = 4500 │ Updated Record │ Stale Record   │ Old Checksum   │
└────────────────┴────────────────┴────────────────┴────────────────┘
        ▲                                                ▲
        └────── Mismatched PageLSN and Checksum! ────────┘
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Problems Caused by Partial Block Writes

1. **Database Page Corruption:**
   - A partially written block contains a mixture of new and old data.
   - Pointers, row offsets, slot arrays, and key values become corrupt. Reading the block causes engine crashes or returns garbled query results.
2. **Breakdown of Log-Based Recovery (WAL Failure):**
   - Standard recovery algorithms (such as ARIES) rely on the **PageLSN** (Log Sequence Number) stored in the page header to decide whether to redo or undo an update.
   - If the header was written (showing a new PageLSN) but the payload sectors were not, recovery assumes the update is present on disk and skips redo. The data remains corrupt forever.
   - Conversely, if the header is old but payload sectors are new, physiological undo operations fail because they apply undo transformations to already-altered data structures.

##### Part (b): How Partial Block Writes Can Be Detected

1. **Block-Level End-to-End Checksums:**
   - Before writing a block to disk, the database calculates a cryptographic hash or cyclic redundancy check (CRC-32) over the entire block payload.
   - It stores this checksum inside the page header.
   - On reading the page back from disk, the database recalculates the checksum over the payload sectors. If power failed mid-write, the recalculated checksum will not match the stored checksum.
2. **Header and Trailer Sequence Matching:**
   - The DBMS writes a matching sequence number or transaction timestamp into both the very first sector (page header) and the very last sector (page trailer) of the block.
   - If a torn write occurs, the sequence number in the header will differ from the trailer.
3. **Sector-Level Hardware ECC:**
   - If power fails while an individual sector is being magnetized or written to flash, the sector's hardware ECC fails. The disk controller flags an I/O read error upon reading that sector.

##### Part (c): How RAID 1 Recovers a Partially Written Block

RAID 1 maintains identical copies on two physical drives: Disk $D_1$ and Disk $D_2$.

**Recovery Protocol:**
- The database system follows an ordered write protocol during normal operations: write block to $D_1$ first, verify completion, then write block to $D_2$.
- After a power failure occurs, the recovery manager scans the disks:
  - **Case 1 ($D_1$ is torn, $D_2$ is valid):**
    - $D_1$ fails its checksum test.
    - $D_2$ was not yet touched and contains the undamaged **old value** ($B_{\text{old}}$).
    - Recovery copies $B_{\text{old}}$ from $D_2$ over to $D_1$. The block is cleanly restored to its old state.
  - **Case 2 ($D_1$ is valid, $D_2$ is torn):**
    - $D_1$ passes its checksum test and contains the valid **new value** ($B_{\text{new}}$).
    - $D_2$ fails its checksum test due to a partial write.
    - Recovery copies $B_{\text{new}}$ from $D_1$ over to $D_2$. The block is cleanly restored to its new state.
  - **Case 3 (Both valid, but have different sequence numbers):**
    - $D_1$ has $B_{\text{new}}$ and $D_2$ has $B_{\text{old}}$.
    - Recovery copies $D_1$ to $D_2$, bringing both to the new state.

In every case, the block cleanly returns to either $B_{\text{old}}$ or $B_{\text{new}}$.

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions often ask about precautions against system failure (2019 Q.4(b) and 2024 Q.3(b)). Torn write detection and RAID 1 mirroring are core technical precautions.
- Mention both detection methods: **Page Checksums** and **Header-Trailer Sequence Validation**.
- Show that RAID 1 enforces atomicity by preventing both disks from being in a torn state at the same time.

---

### Exercise 12.8 · Memory and Storage Hierarchy with Access Speeds

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Exercise 12.8
> - **RUET Topic Mapping:** T12.1 (Storage media hierarchy & I/O latency)
> - **Related RUET Questions:** Storage concepts, memory speed comparison

**Question (Silberschatz 7e Exercise 12.8).**
List the physical storage media available on the computers you use routinely. Give the speed with which data can be accessed on each medium.

#### 1. Core Principles & Concept Overview

Computer systems organize storage as a hierarchy. Higher levels provide faster access speeds and lower latency, but cost more per bit and offer smaller capacities. Lower levels offer massive capacity at low cost, but operate orders of magnitude slower.

```text
The Computer Storage Hierarchy
         ▲                Level / Medium          Typical Latency
        / \               ──────────────────      ───────────────
       /   \              CPU Registers           < 0.5 ns
      /     \             L1 / L2 / L3 Caches     1 ns - 20 ns
     /       \            Main Memory (DRAM)      50 ns - 100 ns
    /         \           Non-Volatile RAM (SCM)  100 ns - 300 ns
   /           \          NVMe Flash SSD          20 µs - 50 µs
  /             \         SATA Flash SSD          100 µs - 200 µs
 /               \        Magnetic HDD            5 ms - 10 ms
/─────────────────\       Tape Storage            Seconds to Minutes
Increasing Capacity       ──────────────────      ───────────────────
Decreasing Cost/Bit       Decreasing Speed        Increasing Latency
```

#### 2. Detailed Step-by-Step Solution

##### Empirical Storage Hierarchy Comparison Table

| Storage Medium | Technology | Volatility | Typical Capacity | Typical Access Latency | Bandwidth / Throughput |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CPU Registers** | Flip-flops / Static RAM | Volatile | $< 2\text{ KB}$ | $< 0.5\text{ ns}$ ($< 1\text{ cycle}$) | Hundreds of GB/s |
| **L1 CPU Cache** | On-chip SRAM | Volatile | $32\text{ KB} - 64\text{ KB}$ | $\approx 1\text{ ns}$ ($3 - 4\text{ cycles}$) | $\approx 1\text{ TB/s}$ aggregate |
| **L2 CPU Cache** | On-chip SRAM | Volatile | $512\text{ KB} - 1\text{ MB}$ | $\approx 3 - 5\text{ ns}$ ($12 - 15\text{ cycles}$) | Hundreds of GB/s |
| **L3 CPU Cache** | Shared on-die SRAM | Volatile | $16\text{ MB} - 64\text{ MB}$ | $\approx 10 - 20\text{ ns}$ ($40 - 60\text{ cycles}$) | $\approx 200\text{ GB/s}$ |
| **Main Memory** | DDR4 / DDR5 SDRAM | Volatile | $16\text{ GB} - 128\text{ GB}$ | $50\text{ ns} - 100\text{ ns}$ | $25 - 60\text{ GB/s}$ |
| **Storage-Class Memory** | Intel Optane / MRAM | Non-Volatile | $128\text{ GB} - 512\text{ GB}$| $100\text{ ns} - 300\text{ ns}$ | $5 - 10\text{ GB/s}$ |
| **NVMe Flash SSD** | 3D NAND Flash (PCIe) | Non-Volatile | $512\text{ GB} - 4\text{ TB}$ | $20\ \mu\text{s} - 50\ \mu\text{s}$ | $3 - 7\text{ GB/s}$ |
| **SATA Flash SSD** | NAND Flash (SATA III)| Non-Volatile | $500\text{ GB} - 2\text{ TB}$ | $100\ \mu\text{s} - 150\ \mu\text{s}$ | $\approx 550\text{ MB/s}$ |
| **Magnetic Hard Disk** | 7200 RPM Platters | Non-Volatile | $2\text{ TB} - 20\text{ TB}$ | $5\text{ ms} - 10\text{ ms}$ | $150 - 250\text{ MB/s}$ |
| **Optical / Tape** | LTO-9 Magnetic Tape | Non-Volatile | Multi-terabyte | Tens of seconds (mount/seek) | $300 - 400\text{ MB/s}$ |

##### Analysis of Latency Gaps

- Notice the massive latency cliff between DRAM and secondary storage:
  - Main memory to NVMe SSD: Latency jumps by a factor of roughly $1000\times$ ($50\text{ ns}$ to $50\ \mu\text{s}$).
  - Main memory to Magnetic Disk: Latency jumps by a factor of roughly $100,000\times$ ($50\text{ ns}$ to $5\text{ ms}$).
- Because disk access is so slow compared to the CPU, database systems use large memory buffer pools and log-based recovery to avoid synchronous disk seeks.

#### 3. RUET Exam Insights & Examiner Notes

- Provide numerical values with appropriate time units: nanoseconds ($\text{ns}$) for RAM/cache, microseconds ($\mu\text{s}$) for SSDs, and milliseconds ($\text{ms}$) for magnetic hard drives.
- Emphasize the $10^5\times$ speed difference between DRAM and magnetic disks. This gap justifies the existence of database buffer management and write-ahead logging.

---

### Exercise 12.9 · Disk Controller Bad-Sector Remapping and Retrieval Throughput

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Exercise 12.9
> - **RUET Topic Mapping:** T12.1 (Disk failure precautions & controller behavior)
> - **Related RUET Questions:** 2017 Q.6(c), 2019 Q.4(b)

**Question (Silberschatz 7e Exercise 12.9).**
How does the remapping of bad sectors by disk controllers affect data-retrieval rates?

#### 1. Core Principles & Concept Overview

Magnetic disk platters can develop physical surface defects. Magnetic coatings degrade, particle contamination occurs, or drive heads make contact with the platter. When a sector can no longer be read reliably, the disk controller marks it as a **bad sector**.

Modern disks reserve spare sectors on each track, cylinder, or at the inner edge of the platter. The controller maintains an internal grown defect list (G-list). It maps bad logical sector addresses to these spare physical sectors automatically.

```text
Bad Sector Remapping and Seek Interruption
Track N (Sequential Read Pipeline):
[ Sector 1 ] [ Sector 2 ] [ BAD 3 ] [ Sector 4 ] [ Sector 5 ]
                             │
                             ▼ Remapped to Spare Cylinder!
Spare Track:           [ Sector 3' ]

Head Action:
Read Sec 1, 2 ──► Seek to Spare Track ──► Wait Rotation ──► Read Sec 3'
              ──► Seek BACK to Track N ──► Wait Rotation ──► Read Sec 4, 5
Result: A 100 µs read turns into a 20 ms mechanical stall!
```

#### 2. Detailed Step-by-Step Solution

Bad-sector remapping affects data retrieval rates in two distinct ways:

##### 1. Breakdown of the Sequential Read Pipeline

- Under normal conditions, consecutive logical sectors reside on the same cylinder track.
- The disk controller streams these sectors sequentially at full platter rotational speed without moving the actuator arm.
- When the controller encounters a remapped sector, the normal streaming pipeline breaks down:
  - If the spare sector is on a **dedicated spare cylinder**, the disk arm must physically seek to that spare cylinder.
  - The head waits for rotational latency until the spare sector spins underneath.
  - The controller reads the sector.
  - Then the arm must seek all the way back to the original cylinder track to continue reading the remaining sectors.
- This operation incurs **two mechanical seeks** and **two rotational delays**.
- A sequential transfer that should take less than $100\ \mu\text{s}$ suddenly takes $10\text{ ms}$ to $20\text{ ms}$.
- Local data retrieval throughput drops by over 99% during that request.

##### 2. Sector Slipped vs. Remapped Tracking

- *Sector Slipped (Track-Level Sparing):* If the spare sector is located on the exact same track, the controller simply slides sector addresses over by one slot. This avoids arm movement. But it introduces a one-sector rotational delay on every revolution.
- *Spare Track Redirection (Cylinder-Level Sparing):* When track spares run out, the drive redirects requests to distant spare cylinders. This introduces severe arm thrashing and unpredictable I/O pauses.

##### Impact on Database Systems

- In relational databases, a table scan expects smooth sequential I/O.
- Encountering remapped sectors causes unexpected I/O stalls in query pipelines.
- If multiple bad sectors accumulate on a disk, it signals imminent mechanical failure. The database administrator must replace the drive and rebuild the array from RAID parity.

#### 3. RUET Exam Insights & Examiner Notes

- Clearly distinguish between intra-track sparing (minor rotational hiccup) and inter-cylinder sparing (major dual-seek penalty).
- Note that bad-sector remapping preserves data correctness, but severely degrades deterministic I/O performance.

---

### Exercise 12.10 · Importance of Consecutive Block Placement on Magnetic Disks versus SSDs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 12 · Exercise 12.10
> - **RUET Topic Mapping:** T12.1 (Storage precautions & physical organization)
> - **Related RUET Questions:** Disk performance, storage design

**Question (Silberschatz 7e Exercise 12.10).**
Operating systems try to ensure that consecutive blocks of a file are stored on consecutive disk blocks. Why is doing so very important with magnetic disks? If SSDs were used instead, is doing so still important, or is it irrelevant? Explain why.

#### 1. Core Principles & Concept Overview

File systems strive to allocate contiguous logical blocks to contiguous physical blocks. The performance impact of this policy differs sharply between mechanical disks and solid-state drives:
- **Magnetic Hard Disks (HDD):** Governed by mechanical arm movement and platter rotation.
- **Solid-State Drives (SSD):** Electronic semiconductor memory with no moving parts.

```text
Access Physics: Magnetic Disk vs. Solid-State Drive
Magnetic HDD:
Mechanical Arm ──► Moves radially (Seek: 4-10 ms)
Platter Spin   ──► Rotates to sector (Rotational delay: 2-4 ms)
Scattered blocks = Disastrous seek overhead!

Solid-State Drive (SSD):
Controller ──► Directly addresses flash chips via electronic signals.
Random Read Latency ≈ Sequential Read Latency (25-50 µs)
No mechanical seek exists!
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Why Consecutive Placement is Crucial on Magnetic Disks

- On magnetic disks, total access time for a block is the sum:

$$
T_{\text{access}} = T_{\text{seek}} + T_{\text{rotational}} + T_{\text{transfer}}
$$

- For scattered blocks:
  - Reading each block requires moving the arm ($T_{\text{seek}} \approx 4 - 8\text{ ms}$) and waiting for rotation ($T_{\text{rotational}} \approx 2 - 4\text{ ms}$).
  - Actual data transfer time $T_{\text{transfer}}$ takes only $0.02\text{ ms}$ for a 4 KB block.
  - Over 99% of total time is wasted on mechanical delays.
  - Random throughput drops to $1 - 2\text{ MB/s}$.
- For consecutive blocks:
  - The arm seeks once to the starting cylinder.
  - All subsequent blocks are read in a single continuous stream as the track spins beneath the head.
  - Seek and rotational delays drop to near zero for subsequent blocks.
  - Throughput achieves maximum sustained rates ($150 - 250\text{ MB/s}$).

##### Part (b): Is Consecutive Placement Still Important on SSDs, or Is It Irrelevant?

- **Direct Answer:** Consecutive placement is **NOT completely irrelevant**. While SSDs eliminate mechanical seek delays, storing files in contiguous block ranges remains significantly beneficial for several structural reasons:

1. **Internal Parallelism and Channel Striping:**
   - Modern SSDs contain multiple NAND flash dies connected across parallel channels (typically 8 to 16 channels).
   - Flash controllers stripe contiguous logical page ranges across these parallel channels and dies.
   - Reading consecutive logical blocks activates all channels simultaneously. This yields sequential bandwidths of $3000\text{ MB/s}$ to $7000\text{ MB/s}$, compared to $400\text{ MB/s}$ to $600\text{ MB/s}$ for random reads.
2. **Flash Translation Layer (FTL) Efficiency:**
   - Contiguous blocks can be tracked using compact extent descriptors $\langle \text{Start\_LPN},\ \text{Start\_PPN},\ \text{Length} \rangle$.
   - Fragmented, scattered blocks require separate entries in the FTL mapping table. This increases controller memory consumption and triggers FTL cache misses.
3. **OS Kernel I/O Request Merging:**
   - Operating systems merge contiguous block requests into large single Direct Memory Access (DMA) transactions (e.g., one 128 KB read rather than thirty-two 4 KB reads).
   - This cuts CPU interrupt processing and system call overhead significantly.
4. **Garbage Collection and Write Amplification:**
   - Writing files contiguously groups data with similar lifespans into the same erase blocks.
   - This reduces data fragmentation inside flash memory, lowering write amplification during garbage collection.

- **Summary:** Consecutive placement is no longer needed to avoid mechanical seek penalties. But it remains important for exploiting flash controller parallelism and reducing mapping overhead.

#### 3. RUET Exam Insights & Examiner Notes

- Do not say that contiguous placement is "completely irrelevant" on SSDs. State that mechanical seek penalty is eliminated, but channel-level parallelism and FTL extent efficiency still favor contiguous allocation.
- This clear distinction earns full marks in RUET storage and systems questions.

---

### Exercise 19.14 · Volatile, Nonvolatile, and Stable Storage I/O Cost Analysis

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Exercise 19.14
> - **RUET Topic Mapping:** T12.1 (Failure classification & storage types)
> - **Related RUET Questions:** 2017 Q.6(c), 2018 Q.5(c), 2023 Q.7(a)

**Question (Silberschatz 7e Exercise 19.14).**
Explain the difference between the three storage types—volatile, nonvolatile, and stable—in terms of I/O cost.

#### 1. Core Principles & Concept Overview

Database recovery theory categorizes storage media into three classes based on durability and survival characteristics:

1. **Volatile Storage:** Memory that loses its contents during a system crash or power outage (e.g., DRAM, CPU cache).
2. **Nonvolatile Storage:** Media that retains contents across system crashes and power failures, but remains vulnerable to physical hardware damage (e.g., magnetic disks, SSDs, optical media).
3. **Stable Storage:** An idealized storage medium whose contents survive all failures, including disk crashes and physical site disasters.

```text
Storage Cost vs. Durability Comparison
Storage Class     Survives Crash?    Survives Disk Head Crash?    Relative I/O Cost
─────────────     ───────────────    ─────────────────────────    ─────────────────
Volatile          NO                 N/A                          Lowest (Nanoseconds)
Nonvolatile       YES                NO                           Medium (Microseconds to Milliseconds)
Stable            YES                YES                          Highest (Replicated Multi-Disk Writes)
```

#### 2. Detailed Step-by-Step Solution

##### 1. Volatile Storage I/O Cost

- **Mechanism:** Direct memory operations (CPU reads and writes over the memory bus to DRAM).
- **Time Cost:** Access latencies range from **10 ns to 100 ns**.
- **I/O Cost Profile:** Extremely low.
  - Requires zero operating system disk interrupts.
  - Involves no peripheral bus transfers.
  - Does not force transaction wait states.
- **Limitation:** Data is wiped clean if power fails.

##### 2. Nonvolatile Storage I/O Cost

- **Mechanism:** Transferring blocks from main memory buffers across a storage bus (PCIe/NVMe, SAS, or SATA) to persistent media.
- **Time Cost:**
  - Solid-state drives (NVMe SSD): **$20\ \mu\text{s}$ to $100\ \mu\text{s}$**.
  - Magnetic hard disks (HDD): **$5\text{ ms}$ to $10\text{ ms}$**.
- **I/O Cost Profile:** Moderate to high.
  - Involves OS kernel system calls (`write`, `fsync`).
  - Requires DMA transfers and device driver interrupt handling.
  - For magnetic disks, it incurs mechanical seek and rotational delays.
- **Limitation:** Survives software and power crashes, but data is lost if the drive experiences head crashes or hardware failure.

##### 3. Stable Storage I/O Cost

- **Mechanism:** Stable storage cannot be implemented as a single physical device. It is implemented by replicating data across multiple independent nonvolatile storage units with ordered write protocols.
- **Standard Implementation Protocol (Silberschatz §19.2):**
  1. Write the block to Primary Disk $D_1$. Wait for write completion.
  2. Read back from $D_1$ to verify ECC and checksums.
  3. Write the block to Secondary Disk $D_2$. Wait for write completion.
  4. Read back from $D_2$ to verify ECC and checksums.
- **Time Cost:**
  - Multiplies nonvolatile I/O costs: at least **two physical writes** plus **two verification reads**.
  - For magnetic disks, this costs **$20\text{ ms}$ to $40\text{ ms}$**.
  - If replicated to a remote geographic site across a Wide Area Network (WAN), network round-trip time (RTT) adds another **$20\text{ ms}$ to $80\text{ ms}$**.
- **I/O Cost Profile:** Highest.
  - Forces strict synchronization barriers.
  - Demands multi-device coordination and checksum computation.
  - Incurs network transfer delays for disaster-tolerant setups.

##### Summary Ranking of I/O Cost

$$
\text{Cost}(\text{Volatile Storage}) \ll \text{Cost}(\text{Nonvolatile Storage}) \ll \text{Cost}(\text{Stable Storage})
$$

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions regularly ask students to classify storage media and failure types (2017 Q.6(c), 2023 Q.7(a)).
- Always explain **how** stable storage is approximated. It is not a hardware chip; it is an ordered replication protocol across multiple nonvolatile devices.
- State clearly that stable storage I/O cost includes multiple disk writes plus read-back verification passes.

---

### Exercise 19.15 · Theoretical Impossibility of Stable Storage and Practical Engineering Approximations

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Exercise 19.15
> - **RUET Topic Mapping:** T12.1 (Precautions against failure & stable storage)
> - **Related RUET Questions:** 2017 Q.6(c), 2019 Q.4(b), 2024 Q.3(b)

**Question (Silberschatz 7e Exercise 19.15).**
Stable storage cannot be implemented.
a. Explain why it cannot be.
b. Explain how database systems deal with this problem.

#### 1. Core Principles & Concept Overview

By theoretical definition, **stable storage** guarantees that data will *never* be lost under *any* circumstances. It must survive power failures, hardware faults, software bugs, natural disasters, and physical destruction.

In the real physical world, every hardware component has a non-zero probability of failure.

```text
Engineering Approximation of Stable Storage
Local Database Server                   Remote Standby Data Center
┌─────────────────────────────┐         ┌─────────────────────────────┐
│ Primary RAID 1/6 Disk Array ├────┬───►│ Secondary Mirrored Storage  │
└─────────────────────────────┘    │    └─────────────────────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Air-Gapped Archival │
                        │ Cloud / Tape Backup │
                        └─────────────────────┘
Combined MTTDL exceeds tens of thousands of years!
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Why Stable Storage Cannot Be Implemented Theoretically

1. **Non-Zero Physical Failure Probability:**
   - Any physical storage device has a finite Mean Time Between Failures (MTBF) and a non-zero probability of failure $P(F) > 0$.
   - Even if data is mirrored across $N$ independent disks, the probability that all $N$ disks fail simultaneously or consecutively before replacement is strictly greater than zero:

$$
P(\text{total data loss}) = \prod_{i=1}^N P(F_i) > 0
$$

2. **Correlated and Common-Mode Failures:**
   - Replicated disks often share common failure modes:
     - Identical firmware bugs that crash all drives at a specific power-on hour.
     - Power supply voltage spikes that fry all connected drives simultaneously.
     - Controller bugs that write corrupted data to all mirrors.
3. **Catastrophic Site Disasters:**
   - Earthquakes, major floods, fires, building collapses, explosions, wars, or nuclear electromagnetic pulses (EMP) can destroy an entire facility. All local copies perish together.
4. **Conclusion:**
   - Because physical reality cannot eliminate catastrophic events or hardware decay, 100% absolute durability is mathematically and physically impossible.

##### Part (b): How Database Systems Deal with This Problem

Database systems use engineering approximations to reduce the probability of data loss to a near-zero level:

1. **Disk Redundancy (RAID 1, RAID 5, RAID 6):**
   - Systems mirror data or maintain dual distributed parity across independent disks.
   - RAID 6 survives the simultaneous failure of any two disks in the same array.
2. **Ordered Multi-Copy Write Protocol:**
   - As described in Silberschatz §19.2, updates are written to primary disk $D_1$, verified, and then written to secondary disk $D_2$.
   - If a crash occurs during either write, the undamaged copy restores the corrupted one.
3. **Geographic Remote Replication:**
   - The database transmits transaction log records over high-speed networks to a remote backup data center located hundreds of miles away.
   - If a flood, fire, or earthquake destroys the primary site, the remote site takes over without data loss.
4. **Air-Gapped Off-Site Archival Backups:**
   - The system regularly takes full database snapshots and writes them to offline magnetic tapes or immutable cloud object storage (WORM: Write-Once-Read-Many).
   - These backups are stored in fireproof, geographically separated vaults.
5. **Periodic Data Scrubbing:**
   - Background controller processes read disk blocks periodically to verify checksums and catch silent bit rot early.

These combined techniques yield durability levels exceeding $99.999999999\%$ ("eleven nines"), which is sufficient for all practical applications.

#### 3. RUET Exam Insights & Examiner Notes

- Part (a) requires a solid theoretical argument: cite non-zero failure probabilities, common-mode hardware faults, and site-wide disasters.
- Part (b) requires listing practical engineering solutions: RAID arrays, ordered replication protocols, off-site backups, and remote geographic mirrors.
- This maps directly to the "precautions against failure" requirement in RUET questions 2019 Q.4(b) and 2024 Q.3(b).

---

### Exercise 19.26 · Failure Classification: System Crash versus Disaster

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Exercise 19.26
> - **RUET Topic Mapping:** T12.1 (Failure classification)
> - **Related RUET Questions:** 2017 Q.6(c), 2018 Q.5(c), 2023 Q.7(a)

**Question (Silberschatz 7e Exercise 19.26).**
Explain the difference between a system crash and a “disaster.”

#### 1. Core Principles & Concept Overview

Failure classification is a foundational topic in database recovery. The recovery strategy depends entirely on which storage levels survive the failure:

- **System Crash:** Affects volatile storage only. Non-volatile storage remains intact.
- **Disaster:** Destroys both volatile storage and local non-volatile storage.

```text
System Crash vs. Disaster Impact
Failure Type        Volatile Memory (DRAM)    Local Non-Volatile Disk    Recovery Source
────────────        ──────────────────────    ───────────────────────    ───────────────
System Crash        LOST / CORRUPTED          INTACT & USABLE            Local Disk Log
Disaster            LOST / CORRUPTED          DESTROYED / INACCESSIBLE   Remote Site / Tape
```

#### 2. Detailed Step-by-Step Solution

##### 1. System Crash

- **Definition:** An unexpected failure in hardware or system software that halts the CPU and terminates DBMS execution.
- **Common Causes:**
  - Sudden electrical power failure (blackout without UPS).
  - Operating system kernel panic or Blue Screen of Death.
  - DBMS process crash (segmentation fault, assertion failure, out-of-memory kill).
  - CPU, motherboard, or memory bus hardware faults.
- **Storage State:**
  - **Volatile Storage (RAM / Cache):** All contents are lost. Any unwritten buffer pool modifications vanish.
  - **Nonvolatile Storage (Disk / SSD):** Remains physically intact and uncorrupted (*fail-stop assumption*).
- **Recovery Method:**
  - Automated local recovery using Write-Ahead Logging (WAL).
  - Upon reboot, the DBMS recovery manager parses the log from the last checkpoint.
  - It executes a **Redo phase** (reapplying updates of committed transactions) and an **Undo phase** (rolling back active, uncommitted transactions).
- **Recovery Time:** Seconds to minutes. No human intervention needed.

##### 2. Disaster (Site / Media Disaster)

- **Definition:** A catastrophic physical event that destroys or permanently damages the computing facility, including its local non-volatile storage media.
- **Common Causes:**
  - Natural catastrophes: Earthquakes, floods, hurricanes, tornadoes.
  - Physical disasters: Data center fires, structural building collapses.
  - Man-made events: Sabotage, explosions, major electrical grid surges that fry all storage controllers.
- **Storage State:**
  - **Volatile Storage:** Completely lost.
  - **Local Nonvolatile Storage:** Completely destroyed, ruined, or physically inaccessible.
- **Recovery Method:**
  - The local recovery manager **cannot** recover the database because on-disk logs and data files no longer exist.
  - Recovery requires **Disaster Recovery (DR)** mechanisms:
    1. Activating a remote hot-standby site that received replicated logs over the network.
    2. Or rebuilding the database from off-site archival backup tapes and replaying archival logs.
- **Recovery Time:** Minutes (for automated remote site failover) to days (for tape retrieval and hardware replacement).

##### Comparison Summary Table

| Evaluation Criterion | System Crash | Disaster |
| :--- | :--- | :--- |
| **Physical Scope** | Confined to running processes / host | Affects entire building or data center |
| **Volatile Storage (RAM)** | Lost | Lost |
| **Nonvolatile Storage (Disk)**| **Intact and readable** | **Destroyed or inaccessible** |
| **Primary Recovery Tool** | Local write-ahead log on disk | Remote replica / off-site tape backups |
| **Human Intervention** | Fully automatic on reboot | Requires administrator / DR team action |
| **Recovery Time Objective** | Seconds to minutes | Minutes to days |

#### 3. RUET Exam Insights & Examiner Notes

- RUET questions 2017 Q.6(c), 2018 Q.5(c), and 2023 Q.7(a) ask students to "classify and discuss the failures in DBMS".
- Present the three textbook classes: **Transaction Failure**, **System Crash**, and **Disk Failure**.
- Then present **Disaster** as the catastrophic extension where local disk redundancy is wiped out. This demonstrates complete mastery of the recovery curriculum.

---

### Exercise 19.27 · Remote Backup Systems and Degrees of Durability Selection

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e · Chapter 19 · Exercise 19.27
> - **RUET Topic Mapping:** T12.1 (Precautions & recovery methods) & Distributed Recovery
> - **Related RUET Questions:** Disaster recovery precautions, remote replication

**Question (Silberschatz 7e Exercise 19.27).**
For each of the following requirements, identify the best choice of degree of durability in a remote backup system:
a. Data loss must be avoided, but some loss of availability may be tolerated.
b. Transaction commit must be accomplished quickly, even at the cost of loss of some committed transactions in a disaster.
c. A high degree of availability and durability is required, but a longer running time for the transaction commit protocol is acceptable.

#### 1. Core Principles & Concept Overview

In a remote backup architecture, a primary site processes active transactions and ships log records over a network to a secondary (backup) site. The protocol governing transaction commit determines the trade-off between **latency**, **availability**, and **durability**:

```text
Remote Backup Modes (Silberschatz §19.8)
One-Safe (Asynchronous):
Primary Site: Commit locally ──► Acknowledge client immediately!
                       └──► Log shipped asynchronously ──► Backup Site
Result: Ultra-fast commit, but committed transactions can be lost in a disaster.

Two-Safe (Synchronous):
Primary Site ──► Writes Log ──► Ships Log ──► Backup Site writes Log
       ▲                                              │
       └────────────── Acknowledged OK ───────────────┘
Primary Commits!
Result: Zero data loss. But if backup fails, primary must freeze (loses availability).

Two-Very-Safe (Quorum / Multi-Site Consensus):
Primary + Multiple Backups coordinate via multi-phase commit / quorum.
Result: Zero data loss, high availability, but higher commit protocol latency.
```

#### 2. Detailed Step-by-Step Solution

##### Part (a): Data Loss Must Be Avoided, Availability Loss Tolerated

- **Best Choice:** **Two-Safe Remote Backup Mode (Synchronous Replication)**.
- **Operational Mechanism:**
  - A transaction $T_i$ cannot commit at the primary site until its commit log record $\langle T_i\text{ commit}\rangle$ is written to stable storage at **both** the primary site and the remote backup site.
  - The primary site sends log records to the backup and blocks. It completes the commit only after receiving a network acknowledgment from the backup.
- **Trade-Off Analysis:**
  - *Durability:* Guaranteed zero data loss ($\text{RPO} = 0$). Even if a disaster destroys the primary site, every committed transaction exists on the remote backup.
  - *Availability:* If the remote backup site crashes or the network link disconnects, the primary site stops committing transactions. It chooses to stall rather than commit data that cannot be replicated. This satisfies the condition that availability loss can be tolerated.

##### Part (b): Fast Transaction Commit, Tolerating Disaster Data Loss

- **Best Choice:** **One-Safe Remote Backup Mode (Asynchronous Replication)**.
- **Operational Mechanism:**
  - A transaction $T_i$ commits immediately once its commit log record is flushed to local stable storage at the primary site.
  - Log records are transmitted to the remote backup site asynchronously in the background.
- **Trade-Off Analysis:**
  - *Latency / Speed:* Commits complete with zero network delay. Transactions run at maximum local disk speed.
  - *Durability:* If a disaster destroys the primary site, log records currently in flight across the network are lost. The remote site will lack the most recently committed transactions ($\text{RPO} > 0$). This directly satisfies the requirement.

##### Part (c): High Availability and High Durability Required, Longer Commit Running Time Acceptable

- **Best Choice:** **Two-Very-Safe Mode with Multi-Site Quorum Consensus (e.g., 3-Site Synchronous Replication / Raft / Paxos Commit)**.
- **Operational Mechanism:**
  - The architecture uses at least three geographically separated sites (or a primary and two independent remote backups).
  - A transaction commits only after a quorum (majority) of sites write the log record to stable storage.
  - If any single site or network link fails, the remaining majority continues processing transactions without interruption.
- **Trade-Off Analysis:**
  - *Durability:* Survives the complete destruction of any single site without losing a single committed transaction ($\text{RPO} = 0$).
  - *Availability:* System remains available even during site failures ($\text{RTO} \approx 0$). Automated failover elects a new leader without human intervention.
  - *Commit Time:* The multi-phase commit protocol requires multiple WAN network round trips. This increases transaction commit latency, which the requirement explicitly accepts.

#### 3. RUET Exam Insights & Examiner Notes

- When answering questions on remote backup systems, use precise industry terms:
  - **One-safe:** Fast local commit, asynchronous log shipping, potential data loss on disaster.
  - **Two-safe:** Synchronous commit at both sites, zero data loss, primary stalls if backup fails.
  - **Two-very-safe:** Quorum-based multi-site commit, zero data loss, high availability, higher commit latency.
- Connect this to RUET disaster recovery questions. Examiners value linking theoretical commit protocols to real-world banking and disaster recovery plans.

---

## Quick Reference Summary of Formulae and Protocols

### 1. Flash Translation Table (FTL) Sizing Formula
For capacity $C$, page size $P$, and address entry size $E$:

$$
N_{\text{pages}} = \frac{C}{P}, \qquad S_{\text{FTL}} = N_{\text{pages}} \times E = \left(\frac{C}{P}\right) \times E
$$

### 2. Disk Rotational Delay and Bandwidth
For rotational speed in $\text{RPM}$:

$$
T_{\text{rot}} = \frac{60}{\text{RPM}}\text{ seconds}, \qquad T_{\text{avg\_rot}} = \frac{1}{2} T_{\text{rot}}
$$

$$
\text{Data Transfer Rate} \propto r \cdot \omega
$$

### 3. RAID 5 Parity Reconstruction Formula
For a failed or torn data block $D_k$:

$$
D_k = P \oplus \bigoplus_{j \neq k} D_j
$$

### 4. Recovery Invariant for Atomic Writes in RAID 1
Always enforce sequential writes during updates:
1. Write block to $D_1$. Wait for completion.
2. Verify checksum on $D_1$.
3. Write block to $D_2$. Wait for completion.
*Invariant:* Never write to both mirrors concurrently. This prevents simultaneous torn blocks.
