# STORIES.md

## Overview

**Project:** `sql-quest`  
**Goal:** Deliver a lightweight, secure, and extensible SQL query management tool that lets data engineers quickly run, schedule, and audit one‑off queries from multiple data sources.

The backlog below is organized into **epics** that reflect the core capabilities of the MVP. Each story follows the format:

```
As a <role>, I want <goal>, so that <benefit>
```

Acceptance criteria are written as **tests** that can be automated in the CI pipeline.

---

## Epics & Story Backlog

| Epic | Story ID | User Story | Acceptance Criteria |
|------|----------|------------|---------------------|
| **E1: Authentication & Authorization** | E1‑S1 | As a **data engineer**, I want to sign in with my corporate SSO so that I can securely access the tool. | • OAuth2 flow with Azure AD/Okta is implemented.<br>• Successful login redirects to the dashboard.<br>• Failed login shows a clear error message. |
| | E1‑S2 | As a **data engineer**, I want role‑based access control so that only authorized users can execute queries on sensitive sources. | • Admin can assign roles (Admin, Analyst, Viewer).<br>• Role permissions are enforced on the API layer.<br>• Unauthorized attempts return 403. |
| **E2: Data Source Management** | E2‑S1 | As a **data engineer**, I want to add a new JDBC/ODBC data source so that I can run queries against it. | • Source form validates connection string.<br>• Successful connection stores credentials encrypted at rest.<br>• Source appears in the “Sources” list. |
| | E2‑S2 | As a **data engineer**, I want to edit or delete a data source so that I can keep the catalog up‑to‑date. | • Edit form pre‑populates existing values.<br>• Delete prompts for confirmation.<br>• Changes persist after page refresh. |
| **E3: Query Creation & Execution** | E3‑S1 | As a **data engineer**, I want to write a SQL query in a web editor so that I can run it against a selected source. | • Editor supports syntax highlighting for SQL.<br>• “Run” button sends query to backend.<br>• Results appear in a paginated table. |
| | E3‑S2 | As a **data engineer**, I want to save a query as a “snippet” so that I can reuse it later. | • Snippet form captures name, description, and tags.<br>• Snippet appears in “My Snippets” list.<br>• Clicking a snippet pre‑loads it into the editor. |
| | E3‑S3 | As a **data engineer**, I want to schedule a query to run nightly so that I can automate recurring reports. | • Scheduler UI allows cron expression input.<br>• Scheduled job runs at the specified time.<br>• Results are stored and accessible via a unique URL. |
| **E4: Result Storage & Retrieval** | E4‑S1 | As a **data engineer**, I want to view the history of executed queries so that I can audit past work. | • History table lists query ID, source, timestamp, and status.<br>• Clicking an entry shows full query text and results. |
| | E4‑S2 | As a **data engineer**, I want to export query results to CSV/JSON so that I can use them elsewhere. | • Export button triggers file download.<br>• CSV/JSON format matches the displayed table. |
| **E5: Security & Compliance** | E5‑S1 | As a **security officer**, I want all query logs to be immutable so that we can satisfy audit requirements. | • Logs are written to a write‑once storage (e.g., S3 with versioning).<br>• No API endpoint allows deletion of logs. |
| | E5‑S2 | As a **data engineer**, I want query results to be masked for PII columns so that sensitive data is protected. | • Masking rules can be configured per source.<br>• Masked results display `****` for masked columns. |
| **E6: Performance & Scalability** | E6‑S1 | As a **product manager**, I want the tool to handle 100 concurrent query executions so that teams can work simultaneously. | • Load test shows <200 ms latency for 100 concurrent runs.<br>• Backend uses connection pooling. |
| **E7: Documentation & Help** | E7‑S1 | As a **new user**, I want an interactive tutorial so that I can learn how to use the tool quickly. | • Tutorial walks through adding a source, writing a query, and scheduling.<br>• Each step has a “Next” button and a “Skip” option. |
| **E8: Internationalization** | E8‑S1 | As a **global user**, I want to switch the UI language between English and Spanish so that I can use the tool in my native language. | • Language toggle updates all static text.<br>• Date/time formats adapt to locale. |

---

## MVP Release Order

1. **E1** – Secure authentication & RBAC  
2. **E2** – Data source CRUD  
3. **E3‑S1** – Query editor & execution  
4. **E3‑S2** – Snippet saving  
5. **E4‑S1** – Query history  
6. **E4‑S2** – Export results  
7. **E5‑S1** – Immutable logs  
8. **E5‑S2** – PII masking  
9. **E6** – Performance baseline  
10. **E7** – Interactive tutorial  
11. **E8** – Internationalization

---

## Notes for Implementation

- **Tech stack**: FastAPI backend, PostgreSQL for metadata, Redis for caching, React + Monaco Editor for the frontend.
- **Security**: Use `pgcrypto` for encrypted credentials, `bcrypt` for password hashing, and `helmet` middleware for HTTP headers.
- **Testing**: Unit tests for API endpoints, integration tests for end‑to‑end query flow, and load tests with k6.
- **CI/CD**: GitHub Actions with Docker builds, automated linting, and unit test coverage >90%.

---

*Prepared by the Senior Product/Engineering Lead, Axentx.*
