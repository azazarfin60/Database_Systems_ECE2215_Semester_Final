---
title: "T13 · Part 1: Security Threats & Authorization (Set A)"
tags:
  - ece2215
  - database-systems
  - silberschatz-exercises
  - topic-T13
topic_id: T13
part: 1
exercise_count: 15
source_chapters:
  - "Chapter 04"
  - "Chapter 09"
---

[← Prev: T12 Part 3](T12_Part3_Checkpoints_and_RAID_Levels.md) | [Index](00_Index.md) | [Next: T13 Part 2 →](T13_Part2_Security_and_Authorization_B.md)

---

# T13 · Part 1: Security Threats & Authorization (Set A)

> [!info] Topic Card
> **Topic:** T13 · Security, Indexing and Hashing  
> **Subtopic Coverage:** T13.1 · Database security threats & authorization (Set A)  
> **Source Chapters:** Silberschatz 7e Chapter 04 (*Intermediate SQL* §4.7) & Chapter 09 (*Application Development* §9.1–9.9)  
> **Assigned Exercises (15 Questions):** PE 9.1, PE 9.2, PE 9.3, PE 9.4, PE 9.6, PE 9.7, PE 9.9, PE 9.10, PE 9.11, PE 9.12, EX 4.11, EX 4.12, EX 4.23, EX 4.24, EX 4.25  
> **Prerequisites:** Relational Model Integrity Constraints, SQL DDL/DML, Operating Systems Process Models, Public Key Cryptography Basics

---

## Table of Exercises

| Exercise ID | Source Chapter | Primary Focus / Concept | Difficulty | Jump Link |
| :-- | :-- | :-- | :--: | :-- |
| **PE 9.1** | Ch. 09 §9.2–9.3 | Servlets vs. CGI Performance & Process vs. Thread Architecture | Easy | [[#Exercise 9.1 · Servlets vs. CGI Execution Architecture & Performance\|Jump]] |
| **PE 9.2** | Ch. 09 §9.2.3 | Connectionless vs. Persistent Protocols in Web Applications | Medium | [[#Exercise 9.2 · Connectionless vs. Connection-Oriented Protocols in Web Applications\|Jump]] |
| **PE 9.3** | Ch. 09 §9.5, 9.8 | Client-Side State Tampering via Hidden Form Variables | Easy | [[#Exercise 9.3 · Client-Side State Tampering via Hidden Form Variables\|Jump]] |
| **PE 9.4** | Ch. 09 §9.3, 9.8 | Broken Access Control, Forced Browsing & Missing Authorization | Medium | [[#Exercise 9.4 · Broken Access Control and Forced Browsing Risks\|Jump]] |
| **PE 9.6** | Ch. 09 §9.7.1 | Multi-Tier Web Caching Strategies (Query, Dynamic Page, Edge/CDN) | Medium | [[#Exercise 9.6 · Multi-Tier Caching Strategies for Web Server Performance\|Jump]] |
| **PE 9.7** | Ch. 09 §9.7.1 | Connection Leaks & Connection Pool Diagnostics using `netstat` | Hard | [[#Exercise 9.7 · Diagnosing Connection and Connection Pool Leaks using netstat\|Jump]] |
| **PE 9.9** | Ch. 09 §9.9.2 | Limitations of Indexing & Primary Keys on Encrypted Attributes | Hard | [[#Exercise 9.9 · Limitations of Indexing and Primary Keys on Encrypted Attributes\|Jump]] |
| **PE 9.10** | Ch. 09 §9.9.2 | Transparent Data Encryption (TDE) vs. Attribute-Level Encryption | Medium | [[#Exercise 9.10 · Transparent Data Encryption (TDE) vs. Attribute-Level Encryption\|Jump]] |
| **PE 9.11** | Ch. 09 §9.9.3 | Public Key Infrastructure (PKI) & Rogue CA Impersonation Risks | Hard | [[#Exercise 9.11 · Impact of Certificate Authority (CA) Impersonation and Rogue Certificates\|Jump]] |
| **PE 9.12** | Ch. 09 §9.3, 9.9 | Secure Password Storage: Salted Cryptographic Hashing | Medium | [[#Exercise 9.12 · Secure Password Storage: Salted Cryptographic Hashing and Verification\|Jump]] |
| **EX 4.11** | Ch. 04 §4.7.1 | Database Multi-Granular Authorization vs. OS File Access Controls | Easy | [[#Exercise 4.11 · Database Multi-Granular Authorization vs. Operating System Access Controls\|Jump]] |
| **EX 4.12** | Ch. 04 §4.7.6 | SQL `granted by current_role` Clause Semantics | Hard | [[#Exercise 4.12 · SQL granted by current_role Clause Semantics and Cascading Protection\|Jump]] |
| **EX 4.23** | Ch. 04 §4.7.2, 4.7.6 | Role-Based Access Control (RBAC) & Institutional Continuity | Medium | [[#Exercise 4.23 · Role-Based Access Control and Manager Privilege Delegation\|Jump]] |
| **EX 4.24** | Ch. 04 §4.7.5–4.7.6 | Cycle Detection in SQL Authorization Graphs (`public with grant option`) | Hard | [[#Exercise 4.24 · Cycle Analysis in SQL Authorization Graphs\|Jump]] |
| **EX 4.25** | Ch. 04 §4.7.4 | The `references` Authorization Privilege in Foreign Key Declarations | Medium | [[#Exercise 4.25 · The references Authorization Privilege in Foreign Key Declarations\|Jump]] |

---

## T13.1 · Database security threats; authorization

---

### Exercise 9.1 · Servlets vs. CGI Execution Architecture & Performance

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.2–9.3
> - **Type:** Practice Exercise 9.1
> - **Difficulty:** Easy · **RUET Relevance:** High (DBMS application architectures & connectivity)

**Question (Silberschatz 7e Exercise 9.1).**  
What is the main reason why servlets give better performance than programs that use the common gateway interface (CGI), even though Java programs generally run slower than C or C++ programs?

#### 1. Core Principles & Concept Overview
The execution performance of web-to-database tier middleware is determined primarily by **operating system process management overhead** and **resource amortization**, rather than the raw algorithmic CPU execution speed of compiled machine code versus interpreted bytecode:
- **Common Gateway Interface (CGI) Process Model:** CGI uses a *fork-and-exec* architecture. For every single HTTP request received, the operating system kernel creates an entirely new process.
- **Java Servlet Multi-Threaded Model:** Servlets run inside a single, persistently executing Java Virtual Machine (JVM) process (the servlet container, e.g., Apache Tomcat, Jetty). Requests are serviced by lightweight concurrent threads sharing a single heap and connection pool.

#### 2. Detailed Step-by-Step Solution

The superior performance of Java Servlets over native C/C++ CGI programs stems from four fundamental architectural mechanisms:

##### 1. Process Creation vs. Thread Dispatch Overhead
- **CGI Overhead:** In CGI, when a web server receives an HTTP request, it issues system calls:
  $$
  \text{HTTP Request} \implies \texttt{fork()} \longrightarrow \texttt{execve()} \longrightarrow \text{Process Initialization} \longrightarrow \texttt{exit()}
  $$
  The OS kernel must allocate a new Process Control Block (PCB), create virtual memory page tables, map executable sections, establish standard I/O pipes, and tear them all down upon request termination. Under high concurrency ($N$ simultaneous requests), the OS spends the majority of its CPU cycles on context switches, memory paging, and kernel scheduling rather than servicing the business logic.
- **Servlet Efficiency:** The servlet container initializes once when the application server boots. Subsequent HTTP requests invoke the pre-loaded servlet instance by dispatching a lightweight worker thread:
  $$
  \text{HTTP Request} \implies \text{Worker Thread from Thread Pool} \longrightarrow \texttt{service(req, resp)}
  $$
  Thread creation and context switching within the same virtual address space consume orders of magnitude fewer CPU cycles than process-level context switches.

```text
CGI Architecture (Heavyweight Process-per-Request):
Web Server  ───fork()───> [OS Process 1 (C/C++ binary)] ───Connect───> DBMS
            ───fork()───> [OS Process 2 (C/C++ binary)] ───Connect───> DBMS
            ───fork()───> [OS Process 3 (C/C++ binary)] ───Connect───> DBMS

Servlet Container Architecture (Single Process, Multi-Threaded):
Web Server ──> [ JVM Process / Application Container ]
                   ├── Thread 1 (Servlet instance) ──┐
                   ├── Thread 2 (Servlet instance) ──┼──> [JDBC Connection Pool] ──> DBMS
                   └── Thread 3 (Servlet instance) ──┘
```

##### 2. Database Connection Lifecycles and Amortization
- **CGI Bottleneck:** Because a CGI process terminates immediately after sending its HTML response, it cannot maintain persistent database connections. Every single invocation must execute a costly full database connection sequence:
  $$
  \text{TCP Handshake} \longrightarrow \text{TLS Handshake} \longrightarrow \text{DBMS Authentication} \longrightarrow \text{Session Setup} \approx 50\text{--}200\text{ ms}
  $$
- **Servlet Pooling:** Servlets retain open connections in an in-memory **JDBC Connection Pool**. A thread simply borrows an existing active connection, executes its query in $1\text{--}5\text{ ms}$, and returns it to the pool without closing the physical TCP socket.

##### 3. Memory Footprint and Virtual Memory Thrashing
- $N$ concurrent CGI requests require $N$ separate copies of the program's data segments, process stacks, and runtime libraries in RAM, leading to memory exhaustion and disk paging/thrashing.
- $N$ concurrent servlet threads share the same JVM heap, class metadata, and compiled code, allocating only a private thread execution stack (typically $512\text{ KB}$ to $1\text{ MB}$ per thread).

##### 4. Just-In-Time (JIT) Compilation in Long-Running Processes
- Although C/C++ is ahead-of-time compiled, an ephemeral CGI program never runs long enough for CPU branch predictors or OS file caches to optimize.
- In contrast, the JVM's HotSpot JIT compiler monitors servlet execution over thousands of requests, compiling critical bytecode loops into highly optimized native machine code.

#### 3. RUET Exam Insights & Examiner Notes
- **Key Marking Criteria:** RUET examiners expect candidates to explicitly contrast the **process-per-request model of CGI** (`fork()`) with the **thread-per-request model of Servlets**, and to highlight **database connection pooling** as the critical real-world differentiator.
- **Common Mistake:** Stating merely that "Java is modern and C is old." The question explicitly acknowledges that C/C++ executes faster than Java in raw CPU benchmarks; candidates must explain why the *system architecture overhead* dominates CPU execution speed.

---

### Exercise 9.2 · Connectionless vs. Connection-Oriented Protocols in Web Applications

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.2.3
> - **Type:** Practice Exercise 9.2
> - **Difficulty:** Medium · **RUET Relevance:** Medium (Database application tier design)

**Question (Silberschatz 7e Exercise 9.2).**  
List some benefits and drawbacks of connectionless protocols over protocols that maintain connections.

#### 1. Core Principles & Concept Overview
- **Connectionless Protocols (e.g., HTTP/1.0, Stateless Request-Response):** The client transmits a request, the server returns a response, and the underlying transport connection is closed. Neither party maintains synchronized session state in the transport layer between interactions.
- **Connection-Oriented Protocols (e.g., Stateful TCP Channels, WebSockets, Database Native Wire Protocols):** A dedicated logical connection is explicitly established via a handshake, maintained through keep-alives, and closed via a teardown protocol.

#### 2. Detailed Step-by-Step Solution

##### Benefits of Connectionless Protocols

1. **Extreme Scalability and Server Resource Conservation:**
   - Operating systems allocate finite kernel resources for every open socket: a socket file descriptor, input/output socket buffers (typically $64\text{ KB}$ each), and kernel tracking structures.
   - If a web server maintains continuous open connections to all clients, an idle client sitting on a web page for 30 minutes holds server resources hostage. Connectionless protocols release socket descriptors immediately upon response delivery, allowing a single server with a limit of $65{,}536$ file descriptors to serve hundreds of thousands of active users.

2. **Fault Tolerance and Resilience to Network Disconnections:**
   - Mobile and distributed clients frequently drop connections (e.g., moving between cellular towers or Wi-Fi networks).
   - In a connection-oriented protocol, a broken connection triggers timeout exceptions, state cleanup, and complex reconnection handshakes. In a connectionless model, intermittent disconnections between requests have zero impact on the server or user session.

3. **Stateless Load Balancing and Horizontal Scaling:**
   - Because no persistent transport channel binds a client to a specific server process, subsequent requests from the same user can be routed seamlessly by reverse proxies (e.g., Nginx, HAProxy) to any healthy backend server node in a cluster without sticky-session constraints.

##### Drawbacks of Connectionless Protocols

1. **Session Management and State Reconstruction Overhead:**
   - Web applications (e.g., e-commerce shopping carts, university grading portals) inherently require conversational continuity.
   - In a connectionless architecture, the application must artificially synthesize state using client-side tokens, cookies, or URL rewriting. On *every single request*, the server must re-authenticate the user, retrieve the session object from an external database or cache (e.g., Redis), and reconstruct context, incurring processing overhead.

2. **Transport Handshake Latency:**
   - When connections are torn down after every request, subsequent requests incur the round-trip latency (RTT) of repeated TCP three-way handshakes and TLS cryptographic handshakes:
     $$
     \text{Latency}_{\text{Setup}} = 1.5 \times \text{RTT}_{\text{TCP}} + 2 \times \text{RTT}_{\text{TLS}}
     $$
   *(Note: Modern HTTP/1.1 persistent connections (`Keep-Alive`) and HTTP/2 multiplexing mitigate this drawback while retaining stateless application semantics).*

3. **Inability to Support Server-Initiated Asynchronous Push:**
   - Under a strict connectionless model, the server cannot independently notify a client of real-time database updates (e.g., stock price alerts, auction bids). The client must repeatedly poll the server, generating wasteful network traffic.

#### 3. RUET Exam Insights & Examiner Notes
- **Comparative Summary Table for RUET Scripts:**

| Dimension | Connectionless Protocols (HTTP) | Connection-Oriented Protocols (Stateful TCP/WebSockets) |
| :-- | :-- | :-- |
| **Server Socket Footprint** | Released immediately after response | Held permanently during idle periods |
| **Server Memory Consumption** | Minimal; scales with active requests | High; scales with total connected clients |
| **Fault Tolerance** | High; server crashes do not break state | Low; connection loss aborts ongoing state |
| **State Tracking** | Requires external cookies/sessions | Built-in via persistent socket context |
| **Real-time Push** | Requires polling or upgrade protocols | Native bidirectional full-duplex communication |

---

### Exercise 9.3 · Client-Side State Tampering via Hidden Form Variables

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.5, 9.8
> - **Type:** Practice Exercise 9.3
> - **Difficulty:** Easy · **RUET Relevance:** High (Web application security threats)

**Question (Silberschatz 7e Exercise 9.3).**  
Consider a carelessly written web application for an online-shopping site, which stores the price of each item as a hidden form variable in the web page sent to the customer; when the customer submits the form, the information from the hidden form variable is used to compute the bill for the customer. What is the loophole in this scheme? (There was a real instance where the loophole was exploited by some customers of an online-shopping site before the problem was detected and fixed.)

#### 1. Core Principles & Concept Overview
- **Fundamental Law of Database Security:** *Never trust client-supplied input.* The client environment (web browser, local DOM, network payload) is entirely under the control of the end user.
- **Hidden Form Fields (`<input type="hidden">`):** Hidden HTML attributes are purely visual display directives instructing the browser rendering engine not to paint the element on the screen. They provide zero security, encryption, or integrity protection.

#### 2. Detailed Step-by-Step Solution

##### 1. The Loophole / Vulnerability Mechanics
In the vulnerable application, the product page renders an HTML form containing the item price:

```html
<!-- Vulnerable Client Form -->
<form action="/checkout" method="POST">
    <p>Product: Textbook Database System Concepts</p>
    <input type="hidden" name="item_id" value="CS101_BOOK">
    <input type="hidden" name="price" value="85.00">
    <label>Quantity: <input type="number" name="quantity" value="1"></label>
    <button type="submit">Purchase</button>
</form>
```

When submitted, the browser transmits a POST payload:
```http
POST /checkout HTTP/1.1
Content-Type: application/x-www-form-urlencoded

item_id=CS101_BOOK&price=85.00&quantity=1
```

The careless backend servlet reads the parameters directly:
```java
// Careless Servlet Code:
double price = Double.parseDouble(request.getParameter("price"));
int qty = Integer.parseInt(request.getParameter("quantity"));
double totalBill = price * qty; // Security Hole!
processPayment(totalBill);
```

An attacker can exploit this loophole using simple browser tools:
1. Open Developer Tools (`F12` / Inspect Element) and modify the HTML:
   ```html
   <input type="hidden" name="price" value="0.01">
   ```
2. Or intercept the HTTP POST request using a local proxy (e.g., OWASP ZAP or Burp Suite) and rewrite the payload to `price=0.01`.
3. The server computes the bill as $0.01 \times 1 = 0.01$ (\$0.01), processes the charge, and dispatches an \$85.00 textbook for one cent.

##### 2. Secure Architectural Remediation
To eliminate this loophole, the server must maintain **authoritative ownership of transactional business rules**:
1. **Server-Side Data Retrieval:** The client must submit only non-authoritative identifiers (e.g., `item_id`, `quantity`). The server queries the authoritative database to retrieve the legitimate unit price:
   ```java
   // Secure Servlet Code:
   String itemId = request.getParameter("item_id");
   int qty = Integer.parseInt(request.getParameter("quantity"));

   PreparedStatement ps = conn.prepareStatement(
       "SELECT price FROM products WHERE item_id = ?"
   );
   ps.setString(1, itemId);
   ResultSet rs = ps.executeQuery();
   if (rs.next()) {
       double officialPrice = rs.getDouble("price");
       double totalBill = officialPrice * qty; // Authoritative computation
       processPayment(totalBill);
   }
   ```
2. **Cryptographic Signing (HMAC):** If state *must* reside on the client, the server must append a Keyed-Hash Message Authentication Code (HMAC) signed with a server-side secret key $K$:
   $$
   \text{Token} = (\text{item\_id}, \text{price}, \text{HMAC}_K(\text{item\_id} \parallel \text{price}))
   $$
   If an attacker alters `price`, the recomputed hash fails verification, and the request is aborted.

#### 3. RUET Exam Insights & Examiner Notes
- **Exam Strategy:** When asked about parameter tampering, always state clearly: (1) why hidden HTML fields are not secure, (2) the exact attack steps, and (3) the correct database-backed remedy.

---

### Exercise 9.4 · Broken Access Control and Forced Browsing Risks

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.3, 9.8
> - **Type:** Practice Exercise 9.4
> - **Difficulty:** Medium · **RUET Relevance:** High (OWASP Top 10 Broken Access Control)

**Question (Silberschatz 7e Exercise 9.4).**  
Consider another carelessly written web application which uses a servlet that checks if there was an active session but does not check if the user is authorized to access that page, instead depending on the fact that a link to the page is shown only to authorized users. What is the risk with this scheme? (There was a real instance where applicants to a college admissions site could, after logging into the web site, exploit this loophole and view information they were not authorized to see; the unauthorized access was, however, detected, and those who accessed the information were punished by being denied admission.)

#### 1. Core Principles & Concept Overview
- **Authentication vs. Authorization:**
  - *Authentication:* Verifying the identity of a principal ("*Who are you?*").
  - *Authorization:* Verifying the permissions of an authenticated principal ("*Are you permitted to access resource $R$?*").
- **Security Through Obscurity:** Hiding a hyperlink from the graphical user interface does not protect the underlying endpoint.
- **Forced Browsing / Broken Object-Level Authorization (BOLA):** An attacker accesses restricted URLs directly by typing them into the browser address bar or incrementing resource IDs.

#### 2. Detailed Step-by-Step Solution

##### 1. The Vulnerability Mechanics
Consider a university admissions portal with two user roles: `Applicant` and `Admissions_Officer`.
- When an applicant logs in, the navigation menu displays only:
  - `Home` (`/applicant/home`)
  - `My Profile` (`/applicant/profile`)
- The navigation link to `View All Admission Decisions` (`/admin/viewDecisions`) is rendered exclusively when `role == 'Admissions_Officer'`.

The backend servlet for `/admin/viewDecisions` performs only an authentication check:
```java
// Vulnerable Access Control in Servlet:
HttpSession session = request.getSession(false);
if (session == null || session.getAttribute("userid") == null) {
    response.sendRedirect("/login.html");
    return; // Block unauthenticated anonymous users
}

// FLAW: No check on session.getAttribute("role")!
// System assumes: "If they reached this servlet, they clicked the admin link."
displayConfidentialAdmissionsDecisions(out);
```

##### 2. The Exploitation Risk (Forced Browsing)
1. An applicant logs in with valid applicant credentials. The server creates an active session and issues a valid `sessionid` cookie.
2. The applicant guesses, discovers via JavaScript code inspection, or reads from application documentation the URL `/admin/viewDecisions` or `/admin/decisions?applicant_id=2310001`.
3. The applicant types this URL directly into the browser (Forced Browsing).
4. The servlet executes `request.getSession(false)`. Because the applicant has an active session, the check succeeds!
5. The applicant bypasses the UI restriction entirely, viewing confidential admission statuses, test scores, and committee deliberations of other applicants before official release.

##### 3. Remediation: Enforcing Server-Side Role-Based Authorization
Every endpoint, servlet, and REST API route must independently verify permissions against the authenticated user's role and identity:

```java
// Secure Access Control Implementation:
HttpSession session = request.getSession(false);
if (session == null || session.getAttribute("userid") == null) {
    response.sendRedirect("/login.html");
    return;
}

String role = (String) session.getAttribute("role");
if (!"Admissions_Officer".equals(role)) {
    // Log security violation audit event
    auditLogger.warn("Unauthorized access attempt by user: " + session.getAttribute("userid"));
    response.sendError(HttpServletResponse.SC_FORBIDDEN, "Access Denied: Insufficient Privileges");
    return;
}

displayConfidentialAdmissionsDecisions(out);
```

#### 3. RUET Exam Insights & Examiner Notes
- **Conceptual Takeaway:** UI-level visibility controls are purely cosmetic usability features; authorization must be strictly enforced at the **server-side application logic layer** or via **database fine-grained row-level security (e.g., Oracle VPD)**.

---

### Exercise 9.6 · Multi-Tier Caching Strategies for Web Server Performance

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.7.1
> - **Type:** Practice Exercise 9.6
> - **Difficulty:** Medium · **RUET Relevance:** High (Performance tuning in web databases)

**Question (Silberschatz 7e Exercise 9.6).**  
List three ways in which caching can be used to speed up web server performance.

#### 1. Core Principles & Concept Overview
Caching reduces response latency, CPU utilization, and database I/O by storing previously computed results in fast, volatile memory (RAM) and reusing them for identical subsequent requests. In a modern database-driven web architecture, caching operates at three distinct tiers:
1. Database Query Result Tier (Data Layer)
2. Application Dynamic HTML / Page Fragment Tier (Business Logic Layer)
3. Edge / Reverse Proxy / Browser Tier (Presentation & Transport Layer)

```text
[ Client Browser ] <=== HTTP Cache-Control ===> [ CDN / Reverse Proxy Cache ]
                                                        │
                                                        ▼
                                           [ Application Server Cache ]
                                           (Page & Fragment HTML Cache)
                                                        │
                                                        ▼
                                           [ In-Memory Key-Value Cache ]
                                                (Redis / Memcached)
                                                        │
                                                        ▼
                                            [ Relational Database (DBMS) ]
```

#### 2. Detailed Step-by-Step Solution

##### 1. Database Query Result Caching (In-Memory Key-Value Stores)
- **Mechanism:** Frequent, read-heavy SQL queries that perform complex relational joins, group-by aggregations, or full-table scans (e.g., fetching a product catalog or top-selling books) are cached in fast main-memory systems such as **Redis** or **Memcached**.
- **Operation:** When a servlet requires data for a key $K$, it first queries the cache:
  $$
  \text{Fetch}(K) \longrightarrow \begin{cases} \text{Cache Hit:} & \text{Return cached object in } < 1\text{ ms} \\ \text{Cache Miss:} & \text{Execute SQL on DBMS, store in cache with TTL, return} \end{cases}
  $$
- **Benefit:** Eliminates query parsing, query optimization, disk block fetching, and lock contention on the relational database server.

##### 2. Application-Level Page and Fragment Caching (Dynamic View Materialization)
- **Mechanism:** Instead of re-rendering an entire JSP, Django template, or HTML document from scratch for every request, the application server caches the generated HTML output (or components of it, such as headers, navigation bars, or department listings).
- **Operation:** Subsequent GET requests with identical request parameters are served directly from the application server's in-memory page buffer without executing backend business logic or ORM transformations.
- **Benefit:** Saves substantial application server CPU cycles spent on template compilation, string concatenation, and object-relational mapping.

##### 3. Reverse Proxy and Edge / CDN Caching (HTTP Gateway Caching)
- **Mechanism:** Edge servers deployed on Content Delivery Networks (CDNs, e.g., Cloudflare) or local reverse proxies (e.g., Varnish, Nginx) positioned in front of the application server cache both static assets (CSS, JavaScript, images) and cacheable dynamic GET responses.
- **Operation:** Utilizes standard HTTP caching headers:
  ```http
  Cache-Control: public, max-age=3600, s-maxage=86400
  ETag: "68efe-d22a4b80"
  ```
- **Benefit:** Requests are terminated geographically close to the user without touching the web server, application server, or database, dramatically reducing network round-trip time (RTT) and bandwidth consumption.

#### 3. RUET Exam Insights & Examiner Notes
- **Crucial Theoretical Nuance:** Mention **cache invalidation strategies** (Time-To-Live [TTL] expiration vs. write-through/write-behind invalidation triggers) to earn full marks. Cached query results are essentially application-tier *materialized views*.

---

### Exercise 9.7 · Diagnosing Connection and Connection Pool Leaks using `netstat`

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.7.1
> - **Type:** Practice Exercise 9.7
> - **Difficulty:** Hard · **RUET Relevance:** High (System administration & DB connection management)

**Question (Silberschatz 7e Exercise 9.7).**  
The `netstat` command (available on Linux and on Windows) shows the active network connections on a computer. Explain how this command can be used to find out if a particular web page is not closing connections that it opened, or if connection pooling is used, not returning connections to the connection pool. You should account for the fact that with connection pooling, the connection may not get closed immediately.

#### 1. Core Principles & Concept Overview
- **TCP Socket States:** `netstat -an` displays network socket endpoints and their lifecycle states:
  - `ESTABLISHED`: Socket is currently connected and actively transmitting/receiving data.
  - `CLOSE_WAIT`: Local operating system kernel received a `FIN` packet from the remote endpoint; waiting for the local application to call `close()`.
  - `TIME_WAIT`: Socket closed locally; waiting $2 \times \text{MSL}$ to ensure remote endpoint received the `ACK`.
- **Connection Leak (Unpooled):** Application opens a raw socket to the database (`port 3306`/`5432`) on each request but fails to execute `conn.close()` in a `finally` block or try-with-resources construct.
- **Connection Pool Leak (Pooled):** Physical sockets between the application server and DBMS remain permanently open in the pool. A leak occurs when a thread borrows a connection via `dataSource.getConnection()` but fails to release it back to the pool (`conn.close()` which triggers pool reclamation).

#### 2. Detailed Step-by-Step Solution

##### Case 1: Unpooled Connections (Direct Database Connections per Request)
If connection pooling is *not* used, every invocation of the web page should open a connection, run queries, and close it immediately.

1. **Baseline Measurement:** Execute `netstat` on the application server machine before testing:
   ```bash
   netstat -anp | grep :5432   # (assuming PostgreSQL on port 5432)
   ```
   Note the initial count of active connections to the database.
2. **Stress / Repetitive Testing:** Issue $K$ consecutive requests (e.g., $K = 50$) to the suspect web page.
3. **Observation & Analysis:**
   - **Normal Behavior:** Connections transition to `TIME_WAIT` and vanish after the timeout. The number of `ESTABLISHED` sockets returns to the baseline.
   - **Connection Leak Detected:** The number of `ESTABLISHED` or `CLOSE_WAIT` sockets to the database port increases by $K$ (or proportionally) and **remains permanently allocated** indefinitely after the HTTP requests have completed. This proves that the servlet code abandoned socket descriptors without calling `close()`.

##### Case 2: Connection Pooling is Used
With connection pooling, physical TCP connections to the DBMS are maintained permanently open by design up to `maxPoolSize` (e.g., 20 connections) and are *not* closed when an individual request finishes. Therefore, simply observing open TCP sockets to the database does not prove a leak.

To diagnose a connection pool leak using `netstat`:

1. **Identify the Pool Capacity Limit:** Suppose the application server's connection pool is configured with $\text{maxConnections} = N$ (e.g., $N = 10$).
2. **Execute Controlled Requests Exceeding Capacity:** Send $M$ sequential requests to the suspect web page, where $M > N$ (e.g., $M = 25$ requests, sent one after another).
3. **Track Client-to-App-Server Socket Accumulation:**
   - If the servlet fails to return borrowed connections to the pool, after the first $N$ requests, **all $N$ pool connections become permanently checked out (leaked)**.
   - When request $N+1$ arrives, the pool has no available connections. The thread blocks indefinitely waiting for a connection to be returned.
   - Run `netstat` monitoring the **HTTP port** of the web application server:

```bash
netstat -an | grep :8080 | grep ESTABLISHED
```
   - **Diagnosis:** New incoming client HTTP connections hang and remain frozen in `ESTABLISHED` state until they hit web server gateway timeouts ($504\text{ Gateway Timeout}$).
4. **Inspect DBMS Backend Socket Activity:**
   - On the database host, run:

```bash
netstat -anp | grep :5432
```
   - All $N$ pooled connections remain continuously `ESTABLISHED`, but cross-referencing with database process views (`pg_stat_activity` or `information_schema.processlist`) reveals they are in state `IDLE in transaction` or idle waiting for input, yet the application pool reports 100% exhaustion.
5. **Definitive Test (The Freeze Test):** Once the pool leaks all $N$ connections, subsequent requests to *any* other database-dependent page on the application server will immediately block and fail to complete, confirming pool exhaustion.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner Expectation:** Full-credit answers must distinguish between the socket behavior of **raw connections** (which should close) and **connection pools** (which intentionally stay open). Explaining that pooled connection leaks cause *pool starvation* that manifests as hanging HTTP client sockets is the key analytical insight.

---

### Exercise 9.9 · Limitations of Indexing and Primary Keys on Encrypted Attributes

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.9.2
> - **Type:** Practice Exercise 9.9
> - **Difficulty:** Hard · **RUET Relevance:** High (Physical storage, indexing, and cryptography)

**Question (Silberschatz 7e Exercise 9.9).**  
A database relation may have the values of certain attributes encrypted for security. Why do database systems not support indexing on encrypted attributes? Using your answer to this question, explain why database systems do not allow encryption of primary-key attributes.

#### 1. Core Principles & Concept Overview
- **Cryptographic Security Goal (Indistinguishability & Diffusion):** Modern secure encryption algorithms (e.g., AES in CBC or GCM mode) utilize random Initialization Vectors (IVs) or salts so that:
  1. Identical plaintext values encrypt to entirely different ciphertexts:
     $$
     x = y \centernot\implies E_K(x) = E_K(y)
     $$
  2. The natural mathematical ordering of plaintexts is completely destroyed:
     $$
     x < y \centernot\implies E_K(x) < E_K(y)
     $$
- **Indexing Fundamentals:** A $B^+$-tree index requires a strict total order relation ($\le$) over keys. A hash index requires a deterministic mapping ($x = y \implies h(x) = h(y)$).
- **Primary Key Constraints:** Require **entity integrity** (`NOT NULL`) and **uniqueness** ($\forall t_1, t_2: t_1[PK] = t_2[PK] \implies t_1 = t_2$).

#### 2. Detailed Step-by-Step Solution

##### 1. Why Database Systems Do Not Support Indexing on Encrypted Attributes

1. **Destruction of Order-Preserving Semantics ($B^+$-Tree Invalidation):**
   - In a $B^+$-tree, internal routing nodes direct searches based on whether a search key $v$ satisfies $v < K_i$ or $v \ge K_i$.
   - Because secure encryption produces pseudo-random ciphertexts, the numerical/lexicographical order of ciphertexts bears zero correlation to the underlying plaintexts:
     $$
     \text{Plaintext: } 10 < 20 \quad \text{vs.} \quad \text{Ciphertext: } \text{AES}(10) = \texttt{0x9F4B...} > \text{AES}(20) = \texttt{0x1A8C...}
     $$
   - Consequently, range queries (`WHERE salary BETWEEN 50000 AND 80000`) cannot navigate a $B^+$-tree index built on ciphertexts. Every range query would degenerate into an expensive full-table scan where *every single tuple* must be decrypted in memory.

2. **Randomized Encryption Destroys Equality Matching:**
   - To defeat dictionary attacks and frequency analysis, database encryption standards prepend a unique random salt or Initialization Vector (IV) to each attribute value prior to encryption.
   - If two employees both earn \$75{,}000, their encrypted values will be:
     $$
     E_K(75{,}000 \parallel \text{IV}_1) \ne E_K(75{,}000 \parallel \text{IV}_2)
     $$
   - A hash index or $B^+$-tree search for $E_K(75{,}000)$ cannot find matches because identical plaintexts do not yield identical ciphertexts.
   *(Note: While deterministic encryption without IVs permits equality lookups, it severely weakens security by revealing data frequency distributions to eavesdroppers).*

##### 2. Why Database Systems Do Not Allow Encryption of Primary-Key Attributes

1. **Uniqueness Enforcement Requires Instant Equality Probes:**
   - When a user executes `INSERT INTO student VALUES ('2310001', 'Rahim', ...)` or updates an existing record, the DBMS must verify that `'2310001'` does not already exist.
   - In an unencrypted database, the DBMS traverses the $B^+$-tree primary index in $O(\log_B N)$ disk I/O operations to verify uniqueness.
   - If the primary key were encrypted with randomized encryption, the DBMS cannot perform an index search. To enforce the uniqueness constraint, the DBMS would have to:
     1. Retrieve every single block of the relation from disk.
     2. Decrypt every primary key value in memory using the secret key.
     3. Compare the plaintext candidate with all existing plaintexts ($O(N)$ decryptions).
   - This turns an $O(\log N)$ insert into a catastrophic $O(N)$ CPU-and-I/O bottleneck that freezes the database under normal transactional workloads.

2. **Foreign Key Integrity Verification:**
   - Referencing foreign keys (`takes.ID REFERENCES student.ID`) must check target existence upon insert/update and enforce cascading rules on delete. If the primary key is encrypted, referential integrity verification across tables becomes computationally intractable.

#### 3. RUET Exam Insights & Examiner Notes
- **Key Takeaway:** Indexing requires either **order preservation** (for trees) or **deterministic mapping** (for hashing). Secure encryption deliberately eradicates both properties to guarantee cryptographic diffusion. Uniqueness validation on primary keys is entirely dependent on efficient indexing.

---

### Exercise 9.10 · Transparent Data Encryption (TDE) vs. Attribute-Level Encryption

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.9.2
> - **Type:** Practice Exercise 9.10
> - **Difficulty:** Medium · **RUET Relevance:** High (Physical database encryption architectures)

**Question (Silberschatz 7e Exercise 9.10).**  
Exercise 9.9 addresses the problem of encryption of certain attributes. However, some database systems support encryption of entire databases. Explain how the problems raised in Exercise 9.9 are avoided if the entire database is encrypted.

#### 1. Core Principles & Concept Overview
- **Attribute-Level Encryption (Logical Tier):** Operates above the storage engine. Specific attribute columns are stored as ciphertext in database records. The query processing engine sees only encrypted bytes.
- **Transparent Data Encryption (TDE) / Entire Database Encryption (Physical Storage Tier):** Operates below the database buffer manager. Relational tables, attribute values, and $B^+$-tree indices reside in **plaintext in volatile RAM (the buffer pool)** and are encrypted only when written to non-volatile disk blocks.

```text
+-----------------------------------------------------------+
|               Query Processing & Index Engine             |
|   (Operates strictly on PLAINTEXT pages in Buffer Pool)   |
|   - Primary Key Uniqueness Checked in O(log N)            |
|   - B+ Tree Range Queries & Joins Execute Normally        |
+-----------------------------------------------------------+
                             ▲
                             │ Page Read / Write Requests
                             ▼
+-----------------------------------------------------------+
|              Database Buffer Manager (RAM)                |
|      [Page 1: Plaintext]      [Page 2: Plaintext]         |
+-----------------------------------------------------------+
         ▲ Decrypt on Read           │ Encrypt on Flush
         │ (Using Database Key)      ▼ (Using Database Key)
+-----------------------------------------------------------+
|          Disk I/O Subsystem (Cryptographic Boundary)      |
+-----------------------------------------------------------+
                             │
                             ▼
+-----------------------------------------------------------+
|             Physical Storage Media (Disk / SSD)           |
|        All database files, logs, and indices AT REST      |
|             are 100% encrypted (Ciphertext)               |
+-----------------------------------------------------------+
```

#### 2. Detailed Step-by-Step Solution

##### How Entire Database Encryption (TDE) Avoids the Problems of Exercise 9.9

1. **Indices and Data Operate in Plaintext in Main Memory:**
   - In full database encryption, encryption and decryption occur at the **disk block (page) I/O layer**.
   - When the DBMS needs a disk block containing relation tuples or $B^+$-tree index nodes, the buffer manager reads the ciphertext block from disk and immediately **decrypts it into plaintext memory** using a secure Database Encryption Key (DEK).
   - Because the data pages exist in unencrypted plaintext while resident in RAM, the query execution engine builds and traverses $B^+$-trees and hash indices using standard numeric and lexicographical orderings ($<$ and $=$).
   - Range queries (`BETWEEN`), equality joins, and sorting operations execute at full hardware speed without requiring specialized cryptographic search schemes.

2. **Primary Key Uniqueness Enforcement Remains $O(\log N)$:**
   - When a new record is inserted, the DBMS checks for duplicate primary keys against the in-memory $B^+$-tree index pages.
   - Because the primary key values in the index are plaintext, comparison operations are standard and immediate.
   - The system verifies uniqueness in $O(\log_B N)$ page accesses without decrypting the entire relation.

3. **Transparent Re-Encryption on Disk Writes:**
   - When the buffer manager flushes a dirty page back to disk storage (or writes to write-ahead transaction log files [WAL]), the block is transparently encrypted before touching persistent media.
   - Physical theft of hard drives, stolen backup tapes, or unauthorized file system access yields only unreadable ciphertext blocks.

#### 3. RUET Exam Insights & Examiner Notes
- **Architectural Distinction:** Emphasize that TDE protects **data-at-rest** against physical theft while maintaining full in-memory relational semantics. It does *not* protect against a compromised DBA account logged into the active database engine.

---

### Exercise 9.11 · Impact of Certificate Authority (CA) Impersonation and Rogue Certificates

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.9.3
> - **Type:** Practice Exercise 9.11
> - **Difficulty:** Hard · **RUET Relevance:** Medium (Public Key Cryptography & PKI)

**Question (Silberschatz 7e Exercise 9.11).**  
Suppose someone impersonates a company and gets a certificate from a certificate-issuing authority. What is the effect on things (such as purchase orders or programs) certified by the impersonated company, and on things certified by other companies?

#### 1. Core Principles & Concept Overview
- **Digital Certificates (X.509):** A cryptographic attestation issued by a trusted Certificate Authority (CA) that cryptographically binds an organization's identity (e.g., `MegaCorp Inc.`) to a public key $K_{\text{pub}}$, signed with the CA's private key $K_{\text{CA-priv}}$:
  $$
  \text{Cert} = \text{Sign}_{K_{\text{CA-priv}}}(\text{Identity} \parallel K_{\text{pub}} \parallel \text{Validity Period})
  $$
- **Digital Signatures & Non-Repudiation:** Documents or software code signed using the private key $K_{\text{priv}}$ corresponding to the certificate cannot be forged unless the private key is obtained.
- **Rogue / Fraudulent Certificate:** If an attacker deceives a CA into issuing a certificate declaring the attacker's public key as belonging to `MegaCorp Inc.`, the attacker possesses the matching private key!

#### 2. Detailed Step-by-Step Solution

##### 1. Effect on Things Certified by the Impersonated Company

1. **Catastrophic Forgery and Loss of Authenticity:**
   - The impersonator possesses the private key corresponding to the validly signed rogue certificate. The attacker can now digitally sign fraudulent documents, electronic purchase orders, bank transactions, and executable software binaries (code signing).
   - Any client, operating system, or browser that verifies the signature against the CA's trusted root store will confirm the signature is mathematically valid and attribute the action to the legitimate company.

2. **Repudiation Crisis and Operational Paralysis:**
   - Customers and business partners can no longer distinguish between genuine contracts signed by the legitimate company's authentic key and fraudulent contracts signed by the impersonator.
   - When the fraud is discovered, the company must issue emergency **Certificate Revocation List (CRL)** and **Online Certificate Status Protocol (OCSP)** revocations.
   - Once revoked, **all legitimate programs, purchase orders, and documents signed during the compromise window become suspect** and will trigger security warnings, causing severe financial and reputational harm.

##### 2. Effect on Things Certified by Other Companies

1. **Cryptographic Independence (Zero Direct Effect):**
   - Public key cryptography guarantees mathematical isolation between key pairs. Other companies possess their own distinct private keys and distinct certificates:
     $$
     K_{\text{priv-other}} \ne K_{\text{priv-impersonator}}
     $$
   - The impersonator cannot forge purchase orders, sign binaries, or intercept communications for any other company. Documents certified by other companies remain mathematically valid and secure.

2. **Systemic Indirect Repercussions (Loss of CA Trust):**
   - If the CA issued the fraudulent certificate due to gross negligence, flawed domain validation, or an internal infrastructure breach (e.g., the real-world *DigiNotar* collapse in 2011):
     - Major operating systems and browser vendors (Google, Microsoft, Apple, Mozilla) will **revoke trust in the entire root certificate of the offending CA**.
     - If the CA's root certificate is removed from global trust stores, **all certificates issued to innocent third-party companies by that CA are immediately distrusted**, triggering widespread website outages and application crashes across unaffected organizations.

#### 3. RUET Exam Insights & Examiner Notes
- **Answer Structure:** Structure the answer clearly into two sections: (1) direct catastrophic impact on the victim company (forgery, loss of non-repudiation, revocation overhead), and (2) cryptographic isolation for other companies, accompanied by the systemic risk of whole-CA untrusting.

---

### Exercise 9.12 · Secure Password Storage: Salted Cryptographic Hashing and Verification

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 09 (*Application Development*), Section 9.3 (Footnote 4), Section 9.9
> - **Type:** Practice Exercise 9.12
> - **Difficulty:** Medium · **RUET Relevance:** Very High (Appears in past RUET finals on DB security)

**Question (Silberschatz 7e Exercise 9.12).**  
Perhaps the most important data items in any database system are the passwords that control access to the database. Suggest a scheme for the secure storage of passwords. Be sure that your scheme allows the system to test passwords supplied by users who are attempting to log into the system.

#### 1. Core Principles & Concept Overview
- **Cleartext / Reversible Storage Prohibition:** Passwords must *never* be stored in plaintext or with reversible two-way encryption (since master decryption keys can be leaked or stolen).
- **Cryptographic One-Way Hash Functions:** Mathematical functions $H(m)$ that are computationally infeasible to invert ($m$ cannot be deduced from $H(m)$) and collision-resistant.
- **Vulnerabilities of Naive Hashing:**
  - *Dictionary Attacks:* Precomputing hashes of common passwords.
  - *Rainbow Table Attacks:* Massive precomputed lookup tables of hashes.
  - *Identical Hash Leakage:* If two users choose the same password `Password123`, their stored hashes are identical, revealing shared secrets.
- **Cryptographic Salt:** A unique, cryptographically strong random bit string generated per user and combined with the password before hashing.
- **Work-Factor / Key Derivation Functions (Slow Hashing):** Algorithms designed with tunable CPU/memory costs (e.g., **bcrypt**, **PBKDF2**, **Argon2**) to prevent GPU/ASIC brute-force cracking.

#### 2. Detailed Step-by-Step Solution

##### 1. Database Schema for User Credentials
The database maintains a dedicated authentication table storing only one-way derivatives:

```sql
CREATE TABLE user_credentials (
    user_id       VARCHAR(50) PRIMARY KEY,
    salt          VARCHAR(64) NOT NULL,    -- Random salt (e.g., 32 bytes hex)
    password_hash VARCHAR(128) NOT NULL,   -- Cryptographic hash output
    hash_algorithm VARCHAR(20) DEFAULT 'argon2id',
    work_factor   INTEGER DEFAULT 12
);
```

##### 2. User Registration / Password Creation Scheme
When a user sets or changes their password:
1. User provides plaintext candidate password $P$.
2. The authentication service generates a cryptographically secure, high-entropy pseudo-random salt $S$ of at least 128 bits ($16$ bytes):
   $$
   S \longleftarrow \texttt{CSPRNG()} \quad (\text{e.g., } \texttt{/dev/urandom})
   $$
3. The system computes the salted hash using a slow cryptographic Key Derivation Function (KDF):
   $$
   H = \text{Argon2id}(P \parallel S, \text{memory}=64\text{MB}, \text{iterations}=3)
   $$
4. The system inserts the tuple $(\text{user\_id}, S, H)$ into the database. The plaintext password $P$ is immediately overwritten and purged from volatile RAM.

##### 3. User Login / Password Testing Scheme
When a user attempts to log into the system:
1. The user supplies candidate credentials: $(\text{user\_id}, P_{\text{attempt}})$.
2. The authentication engine queries the database:
   ```sql
   SELECT salt, password_hash FROM user_credentials WHERE user_id = ?;
   ```
3. If the user does not exist, the engine executes a dummy hash operation against a fake salt (to prevent username enumeration via timing attacks) and returns authentication failure.
4. If the user exists, the engine retrieves the stored salt $S$ and stored hash $H$.
5. The engine computes the candidate hash using the exact same algorithm parameters:
   $$
   H_{\text{attempt}} = \text{Argon2id}(P_{\text{attempt}} \parallel S, \text{memory}=64\text{MB}, \text{iterations}=3)
   $$
6. The engine compares $H_{\text{attempt}}$ with $H$ using a **constant-time byte comparison algorithm** (to prevent side-channel timing attacks):
   $$
   \text{Verify}(H_{\text{attempt}}, H) \longrightarrow \begin{cases} \text{True:} & \text{Password valid; create session} \\ \text{False:} & \text{Reject login attempt} \end{cases}
   $$

```text
REGISTRATION:
Plaintext P ──┐
              ├──> [ Salted Slow Hash: Argon2 / bcrypt ] ──> Store (User, Salt, Hash) in DB
Random Salt S ┘

LOGIN VERIFICATION:
Attempt P' ──┐
             ├──> [ Salted Slow Hash: Argon2 / bcrypt ] ──> Computed Hash H'
Stored Salt S ┘                                                    │
                                                         Constant-Time Equality?
                                                                   │
                                        Stored Hash H <────────────┴───> Grant / Deny
```

##### Why This Scheme is Resilient
- **Rainbow Tables Defeated:** Because every user has a distinct random salt $S$, precomputed rainbow tables are useless. An attacker must build a separate $2^{64}$ table for every single user.
- **Identical Passwords Masked:** If two users choose `welcome2026`, their stored hashes $H_1$ and $H_2$ are completely different because $S_1 \ne S_2$.
- **Offline Brute-Force Resistance:** High memory/CPU work factors ensure that guessing attempts require significant time per candidate, rendering GPU cluster attacks infeasible.

#### 3. RUET Exam Insights & Examiner Notes
- **High-Scoring Elements:** Draw the Registration vs. Login verification workflow diagram, define **salt**, and explicitly name modern key derivation algorithms (Argon2, bcrypt, PBKDF2) rather than obsolete hashes (MD5, SHA-1).

---

### Exercise 4.11 · Database Multi-Granular Authorization vs. Operating System Access Controls

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.7.1
> - **Type:** End-of-Chapter Exercise 4.11
> - **Difficulty:** Easy · **RUET Relevance:** High (Unit 1 and Unit 8 authorization models)

**Question (Silberschatz 7e Exercise 4.11).**  
Operating systems usually offer only two types of authorization control for data files: read access and write access. Why do database systems offer so many kinds of authorization?

#### 1. Core Principles & Concept Overview
- **Operating System File Abstraction:** Operating systems view data files as uninterpreted linear streams of raw bytes. OS authorization (`r`, `w`, `x` permissions in Unix/POSIX, or basic ACLs in Windows) operates at the physical file/inode container level.
- **Relational Database Abstraction:** Databases possess rich semantic awareness of schemas, relations, attributes, integrity constraints, and transactional consistency.
- **Principle of Least Privilege:** Users must be granted only the absolute minimum permissions necessary to perform their specialized business functions.

#### 2. Detailed Step-by-Step Solution

Database systems offer diverse, granular authorization controls (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `REFERENCES`, `INDEX`, `ALTER`, `EXECUTE`) for four fundamental reasons:

##### 1. Semantic Deconstruction of "Write" Operations
In an operating system, granting "write" permission to a file allows a user to overwrite existing data, truncate the file to zero bytes, append garbage, or delete the file entirely. In a database, these operations carry vastly different operational and risk profiles:
- **`INSERT`:** Permits appending new business records (e.g., an order entry clerk entering a new purchase order) without granting permission to alter or tamper with historical records.
- **`UPDATE`:** Permits altering existing data values (e.g., updating a customer address) without granting the ability to delete entire tuples.
- **`DELETE`:** Permits removing tuples from a relation. This is highly destructive and restricted to senior administrators.
- **`ALTER` / `DROP`:** Controls modifying the schema definition (adding columns, deleting tables), strictly separated from DML data modification.

##### 2. Attribute-Level (Columnar) Granularity
OS file permissions cannot hide specific bytes within a record. In contrast, database systems allow authorization on specific columns within the same relation:
```sql
GRANT SELECT (ID, name, dept_name) ON instructor TO student_advisor;
-- Access to the 'salary' column is strictly withheld!
```

##### 3. Enforcing Inter-Table Relational Constraints (`REFERENCES`)
A database must protect referential integrity. Creating a foreign key referencing another table restricts future `DELETE` and `UPDATE` operations on that table. The database therefore provides a dedicated **`REFERENCES`** privilege, preventing users from creating constraints that could restrict or freeze tables owned by other users.

##### 4. Procedural and Behavioral Encapsulation (`EXECUTE`)
Database systems manage executable logic (stored procedures, functions, triggers). Granting **`EXECUTE`** on a procedure allows a user to perform complex business updates through strict validated logic without granting direct `INSERT` or `UPDATE` access to the underlying base tables.

#### 3. RUET Exam Insights & Examiner Notes
- **Comparative Table for RUET Exam:**

| Dimension | Operating System File Authorization | Database Management System Authorization |
| :-- | :-- | :-- |
| **Data View** | Unstructured byte stream / flat file | Highly structured relations, tuples, attributes |
| **Permission Types** | Read (`r`), Write (`w`), Execute (`x`) | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `REFERENCES`, `INDEX`, `ALTER`, `EXECUTE` |
| **Field-Level Control** | Impossible (all-or-nothing file access) | Granular column-level and view-level authorization |
| **Integrity Awareness** | None | Enforces constraints, foreign keys, and relational integrity |

---

### Exercise 4.12 · SQL `granted by current_role` Clause Semantics and Cascading Protection

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.7.6
> - **Type:** End-of-Chapter Exercise 4.12
> - **Difficulty:** Hard · **RUET Relevance:** High (SQL authorization graphs and RBAC)

**Question (Silberschatz 7e Exercise 4.12).**  
Suppose a user wants to grant select access on a relation to another user. Why should the user include (or not include) the clause **granted by current_role** in the grant statement?

#### 1. Core Principles & Concept Overview
- **Default Grantor Semantics:** When a user executes a standard SQL `GRANT` statement without specifying a grantor clause:
  ```sql
  GRANT SELECT ON department TO Amit;
  ```
  The database engine records the grantor as the individual user's personal account (`session_user`).
- **Role-Based Grantor Semantics (`GRANTED BY CURRENT_ROLE`):**
  ```sql
  GRANT SELECT ON department TO Amit GRANTED BY CURRENT_ROLE;
  ```
  The database records the active **role** (e.g., `dean`, `registrar`) as the grantor node in the authorization graph.
- **Cascading Revocation Rule:** If a privilege is revoked from user $U$, any privileges granted *by* $U$ to downstream users are automatically revoked (cascaded), unless supported by an alternate independent path from the root.

#### 2. Detailed Step-by-Step Solution

##### Why a User SHOULD Include `granted by current_role`

1. **Protection Against Accidental Cascading Revocation on Personnel Turnover:**
   - In institutional settings, users exercise authority by virtue of their **office/role**, not their personal identity.
   - Suppose user *Satoshi* holds the role `dean`. While acting as dean, Satoshi grants `SELECT ON department TO Amit`.
   - **Without the clause:** The grantor is recorded as the user `Satoshi`. If Satoshi later leaves the university, retires, or transfers to another department, the DBA revokes the `dean` role from `Satoshi`. Under standard SQL cascading revocation:
     $$
     \text{Revoke from Satoshi} \implies \text{All grants executed by Satoshi cascade and are revoked from Amit!}
     $$
     Amit improperly loses access to departmental data even though Amit is still an active faculty member.
   - **With `GRANTED BY CURRENT_ROLE`:** The grantor in the authorization graph is the permanent institutional role `dean`. When the DBA revokes `dean` from Satoshi, the edge originating from the `dean` role to Amit remains intact. Amit retains access uninterrupted under the new incoming dean.

```text
Without 'granted by current_role' (Fragile User-Linked Graph):
DBA ──> [Satoshi] ──> [Amit]
Revoking Satoshi breaks the path to Amit!

With 'granted by current_role' (Robust Role-Linked Graph):
DBA ──> [Role: Dean] ──> [Amit]
             ▲
             │ (Membership)
         [Satoshi]
Revoking Satoshi's membership in Dean leaves the Dean ──> Amit grant intact!
```

##### Why a User Should NOT Include `granted by current_role`

1. **Personal / Private Object Ownership:**
   - If user *Satoshi* creates a private research table and temporarily delegates access to a graduate student assistant, that authorization is tied strictly to Satoshi's personal tenure. If Satoshi departs, his personal delegations *should* terminate immediately.
2. **Current Role is Undefined (NULL):**
   - In SQL, sessions start with `current_role` set to `NULL` by default unless explicitly activated via `SET ROLE <role_name>`. Executing `GRANTED BY CURRENT_ROLE` when `current_role IS NULL` causes the database to return an error.

#### 3. RUET Exam Insights & Examiner Notes
- **Key Exam Principle:** Explicitly mention that `GRANTED BY CURRENT_ROLE` decouples **institutional privileges** from **transient individuals**, preventing the catastrophic disruption of cascading revocation when personnel leave organizations.

---

### Exercise 4.23 · Role-Based Access Control and Manager Privilege Delegation

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.7.2, 4.7.6
> - **Type:** End-of-Chapter Exercise 4.23
> - **Difficulty:** Medium · **RUET Relevance:** High (Role-Based Access Control [RBAC] design)

**Question (Silberschatz 7e Exercise 4.23).**  
Explain why, when a manager, say Satoshi, grants an authorization, the grant should be done by the manager role, rather than by the user Satoshi.

#### 1. Core Principles & Concept Overview
- **Role-Based Access Control (RBAC):** Privileges are associated with roles, and users are assigned to appropriate roles.
- **Graph Reachability and Node Invalidation:** A user retains an authorization if and only if there is a directed path from the root (DBA) to the user node in the authorization graph.

#### 2. Detailed Step-by-Step Solution

##### 1. The Personnel Identity Problem
Employees in organizations are transient:
- A manager (e.g., Satoshi) will eventually be promoted, transferred to a different branch, take a sabbatical, or resign from the company.
- However, the organizational unit and the subordinates' need to access database tables persist.

##### 2. The Cascading Revocation Failure Scenario
Suppose Satoshi grants privileges using his personal user identity:
```sql
-- Executed as User Satoshi (Default)
GRANT SELECT, UPDATE ON budget TO finance_team;
```
This establishes the authorization graph path:
$$
\text{DBA} \longrightarrow \text{Satoshi} \longrightarrow \text{finance\_team}
$$

When Satoshi leaves the managerial post:
1. The system administrator revokes manager privileges from Satoshi:
   ```sql
   REVOKE manager_privileges FROM Satoshi CASCADE;
   ```
2. Because `finance_team` received authorization directly from the node `Satoshi`, SQL's cascading revocation algorithm traverses all outbound edges from `Satoshi`.
3. The authorization path from the root to `finance_team` is severed:
   $$
   \text{DBA} \centernot\longrightarrow \text{Satoshi} \centernot\longrightarrow \text{finance\_team}
   $$
4. The entire finance team is instantly locked out of critical corporate budget relations, halting daily business operations.

##### 3. The Role-Based Delegation Architecture
If Satoshi sets his active role to `manager` and executes the grant on behalf of the role:
```sql
SET ROLE manager;
GRANT SELECT, UPDATE ON budget TO finance_team GRANTED BY CURRENT_ROLE;
```
The authorization graph path is established through the role entity:
$$
\text{DBA} \longrightarrow \text{manager\_role} \longrightarrow \text{finance\_team}
$$
User Satoshi is merely an authorized member of `manager_role`:
$$
\text{manager\_role} \owns \text{Satoshi}
$$

When Satoshi leaves the position:
1. The administrator simply revokes Satoshi's membership in `manager_role`:
   ```sql
   REVOKE manager FROM Satoshi;
   ```
2. The node `manager_role` and its outbound grant edge to `finance_team` remain completely untouched.
3. The finance team experiences zero downtime, and a newly appointed manager seamlessly inherits oversight without re-granting hundreds of individual table permissions.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner Scoring Focus:** Candidates must emphasize that roles represent **persistent institutional offices**, whereas user accounts represent **transient human individuals**. Granting by role ensures organizational continuity and eliminates operational outages caused by cascading revokes.

---

### Exercise 4.24 · Cycle Analysis in SQL Authorization Graphs

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.7.5–4.7.6
> - **Type:** End-of-Chapter Exercise 4.24
> - **Difficulty:** Hard · **RUET Relevance:** High (Formal properties of authorization graphs)

**Question (Silberschatz 7e Exercise 4.24).**  
Suppose user A, who has all authorization privileges on a relation $r$, grants select on relation $r$ to **public** with grant option. Suppose user B then grants select on $r$ to A. Does this cause a cycle in the authorization graph? Explain why.

#### 1. Core Principles & Concept Overview
- **SQL Authorization Graph $G = (V, E)$:** A directed graph where vertices $V$ represent database users/roles, and a directed edge $(U_i, U_j) \in E$ denotes that user $U_i$ granted a specific privilege to user $U_j$.
- **The Pseudo-User `public`:** Represents the universal set of all current and future users in the database system:
  $$
  \forall U_k \in \text{Users}, \quad U_k \in \mathbf{public}
  $$
- **`WITH GRANT OPTION` Semantics:** Allows the grantee to propagate the privilege to other users.
- **Cycle Definition:** A directed cycle exists in $G$ if there exists a sequence of vertices $\langle v_1, v_2, \dots, v_k \rangle$ such that $(v_i, v_{i+1}) \in E$ and $v_k = v_1$.

#### 2. Detailed Step-by-Step Solution

##### 1. Formal Graph Construction Step-by-Step

**Step 1: Initial State**
- User $A$ possesses all privileges on relation $r$ with grant option (e.g., $A$ is the relation creator or received privileges from the DBA root):
  $$
  \text{DBA} \longrightarrow A
  $$

**Step 2: User $A$ Grants to `public` With Grant Option**
- User $A$ executes:
  ```sql
  GRANT SELECT ON r TO public WITH GRANT OPTION;
  ```
- Because user $B$ is a constituent member of `public`, this statement effectively grants the `SELECT` privilege with grant option to user $B$.
- In the formal authorization graph, there is a directed path from $A$ to $B$ (either directly through the expansion of `public` into all users, or via the `public` node):
  $$
  A \xrightarrow{\text{grant}} B \quad (\text{or } A \longrightarrow \mathbf{public} \longrightarrow B)
  $$

**Step 3: User $B$ Grants Select to User $A$**
- User $B$, now possessing `SELECT` on $r$ along with the grant option, executes:
  ```sql
  GRANT SELECT ON r TO A;
  ```
- This adds a new directed edge from node $B$ to node $A$:
  $$
  B \xrightarrow{\text{grant}} A
  $$

```text
Directed Cycle in the Authorization Graph:

             +---------------------------------------+
             |                                       |
             ▼                                       │
       [ User A ] ───(Grant to public WITH GRANT)──> [ User B ]
             │                                       ▲
             +───────────────────────────────────────+
```

##### 2. Cycle Analysis
- **Conclusion: YES, this creates a directed cycle in the authorization graph.**
- The path $A \longrightarrow B$ combined with the edge $B \longrightarrow A$ forms a closed directed loop:
  $$
  A \longrightarrow B \longrightarrow A
  $$

##### 3. Security Implications on Revocation (Does the Cycle Defeat Revoke?)
A common exam concern is whether such a cycle allows users to bypass authorization revocation:
- Suppose the DBA revokes all privileges on $r$ from user $A$:
  ```sql
  REVOKE ALL PRIVILEGES ON r FROM A CASCADE;
  ```
- Does user $A$ retain `SELECT` privilege because of the inbound grant from user $B$?
- **NO.** SQL's formal authorization semantics require that a user possesses a privilege **if and only if there exists a directed path from an independent root (the DBA or object owner) down to that user**.
- Once the DBA revokes from $A$, the incoming edge $\text{DBA} \longrightarrow A$ is severed. The subgraph $\{A, B\}$ has mutual cycles, but neither $A$ nor $B$ has a path traceable back to the root.
- Therefore, the SQL engine eliminates the entire disconnected cycle component, and both $A$ and $B$ lose the privilege.

#### 3. RUET Exam Insights & Examiner Notes
- **Full Marks Requirement:** State unequivocally that a directed cycle **is created**. Trace the edges ($A \to B$ via `public`, and $B \to A$). Conclude with the root reachability rule to demonstrate complete mastery of SQL authorization theory.

---

### Exercise 4.25 · The `references` Authorization Privilege in Foreign Key Declarations

> [!info] Exercise Metadata
> - **Source:** Silberschatz 7e, Chapter 04 (*Intermediate SQL*), Section 4.7.4
> - **Type:** End-of-Chapter Exercise 4.25
> - **Difficulty:** Medium · **RUET Relevance:** High (DDL constraints and security privileges)

**Question (Silberschatz 7e Exercise 4.25).**  
Suppose a user creates a new relation $r_1$ with a foreign key referencing another relation $r_2$. What authorization privilege does the user need on $r_2$? Why should this not simply be allowed without any such authorization?

#### 1. Core Principles & Concept Overview
- **Referential Integrity Constraint:** A foreign key in $r_1$ referencing primary key $PK$ of $r_2$ requires that:
  $$
  \forall t_1 \in r_1: t_1[FK] \ne \text{null} \implies \exists t_2 \in r_2 \text{ such that } t_1[FK] = t_2[PK]
  $$
- **Bidirectional Behavioral Constraint:** While a foreign key primarily restricts insertions into $r_1$, it simultaneously imposes strict **deletion and update restrictions on relation $r_2$**.

#### 2. Detailed Step-by-Step Solution

##### 1. The Required Authorization Privilege
To declare a foreign key referencing relation $r_2$, the user must possess the **`REFERENCES`** privilege on the specific referenced attribute(s) of $r_2$, or on the entire relation $r_2$:

```sql
-- Granted by Owner of r2 (e.g., Department Head) to User1:
GRANT REFERENCES (dept_name) ON department TO Mariano;

-- User Mariano can now define r1:
CREATE TABLE student_project (
    project_id   INTEGER PRIMARY KEY,
    dept_name    VARCHAR(20),
    FOREIGN KEY (dept_name) REFERENCES department(dept_name)
);
```

##### 2. Why Creating Foreign Keys Cannot Be Allowed Without Authorization

At first glance, it might appear that creating a foreign key only constrains the creator's own relation $r_1$. However, this is fundamentally untrue due to the reciprocal nature of referential integrity:

1. **Foreign Keys Restrict Future Deletion and Update Operations on $r_2$:**
   - Suppose User 1 (owner of $r_1$) is allowed to reference relation $r_2$ (`department`) without authorization.
   - User 1 inserts a tuple into $r_1$ referencing `'Geology'`.
   - Now, consider the legitimate owner or authorized administrators of $r_2$. If the department administrator attempts to delete the `'Geology'` department or change its name:

```sql
DELETE FROM department WHERE dept_name = 'Geology';
```
   - The database engine will **intercept and abort the deletion** with a referential integrity violation error:
     $$
     \texttt{ERROR: update or delete on table "department" violates foreign key constraint}
     $$
   - User 1 has effectively **restricted the legal operations of the owner of $r_2$** without their consent!

2. **Potential for Malicious Denial-of-Service (DoS) and Table Freezing:**
   - If foreign keys could be declared without the `REFERENCES` privilege, any untrusted user could create dummy tables with foreign keys referencing every primary key in critical corporate tables (`customer`, `account`, `orders`).
   - By inserting referencing rows, the rogue user could artificially freeze the entire database, preventing legitimate administrators from purging obsolete accounts, archiving records, or restructuring data.

3. **Restricting Forced Cascading Side-Effects:**
   - If the referencing table is defined with `ON DELETE CASCADE`, a deletion in $r_2$ might trigger cascading deletes in third-party schemas, creating complex hidden dependencies.

#### 3. RUET Exam Insights & Examiner Notes
- **Examiner Tip:** State clearly: "A foreign key in relation $r_1$ restricts `DELETE` and `UPDATE` operations on relation $r_2$." Mentioning this reciprocal restriction is the exact reason why the **`REFERENCES`** privilege exists in the SQL standard.


---

[← Prev: T12 Part 3](T12_Part3_Checkpoints_and_RAID_Levels.md) | [Index](00_Index.md) | [Next: T13 Part 2 →](T13_Part2_Security_and_Authorization_B.md)
