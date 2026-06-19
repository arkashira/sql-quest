# TECH_SPEC.md – **sql‑quest**

**Product**: *SQL‑Quest* – A SQL query management platform that automates, tracks, and streamlines one‑off queries across heterogeneous data sources for data‑engineering teams.

---

## 1. Overview  

| Aspect | Description |
|--------|-------------|
| **Goal** | Provide a self‑service UI & API that lets data engineers submit ad‑hoc SQL, have the system safely execute it against registered data sources, store results, and expose them for downstream consumption. |
| **Target Users** | Data engineers, analytics engineers, BI developers, and data‑ops staff. |
| **Core Value** | Eliminates manual copy‑paste of credentials, ad‑hoc script sprawl, and undocumented query runs while preserving auditability and reproducibility. |
| **Scope** | • Query authoring & versioning  <br>• Secure credential handling  <br>• Multi‑source execution (PostgreSQL, MySQL, Snowflake, BigQuery, Redshift, etc.)  <br>• Result materialisation (CSV, Parquet, DB table)  <br>• Execution scheduling & retry  <br>• Auditing, RBAC, and lineage tracking. |
| **Out‑of‑Scope** | Long‑running ETL pipelines, data‑modeling, BI dashboarding (handled by downstream tools). |

---

## 2. Architecture Overview  

```
+-------------------+       +-------------------+       +-------------------+
|   Front‑End UI    | <---> |   API Gateway     | <---> |   Core Services   |
| (React + MUI)     |       | (FastAPI + Auth) |       |   - Query Service |
+-------------------+       +-------------------+       |   - Exec Engine   |
                                                        |   - Scheduler     |
                                                        |   - Metadata DB   |
                                                        +-------------------+
                                                               |
                                                               v
+-------------------+      +-------------------+      +-------------------+
|   Credential Vault| <--> |   Data Source SDK | <--> |   Worker Nodes    |
|   (HashiCorp Vault|      | (SQLAlchemy +     |      | (Celery workers) |
|    / AWS Secrets) |      |  source‑specific  |      +-------------------+
+-------------------+      |  adapters)        |
                           +-------------------+
                                   |
                                   v
                           +-------------------+
                           |   Result Store    |
                           | (PostgreSQL meta, |
                           |  S3/MinIO blobs)  |
                           +-------------------+
```

* **Front‑End** – React SPA (Material‑UI) consuming the public OpenAPI spec.  
* **API Gateway** – FastAPI (Python 3.11) exposing REST/GraphQL endpoints, handling OAuth2/JWT auth, rate‑limiting, and request validation.  
* **Core Services** – Modular Python packages:  
  * `query_service` – CRUD, versioning, validation, lineage.  
  * `exec_engine` – Translates a stored query into an executable job, resolves data‑source credentials, and dispatches to workers.  
  * `scheduler` – Celery beat + Redis for delayed / recurring runs.  
* **Worker Nodes** – Stateless Celery workers that run the actual SQL via SQLAlchemy‑compatible dialects. Results streamed to the Result Store.  
* **Credential Vault** – Centralised secret store (HashiCorp Vault or AWS Secrets Manager) accessed via a thin wrapper; never persisted in the metadata DB.  
* **Result Store** –  
  * **Metadata** – PostgreSQL (12+) holds `queries`, `executions`, `results`, `users`, `permissions`.  
  * **Blob storage** – Amazon S3 (or MinIO for on‑prem) stores large result sets (CSV/Parquet) and optional query logs.  

All components are containerised (Docker) and orchestrated via Helm charts on Kubernetes (or Docker‑Compose for local dev).

---

## 3. Component Detail  

### 3.1 Front‑End (UI)  

| Item | Tech | Responsibility |
|------|------|----------------|
| SPA | React 18 + TypeScript | Query authoring, history, result preview, admin console |
| UI Library | Material‑UI (MUI) v5 | Consistent design system |
| State Management | Redux Toolkit | Global auth & query state |
| API Client | `axios` + generated OpenAPI TS client | Typed HTTP calls |
| Auth | OIDC (Auth0 / Azure AD) | Token acquisition, silent refresh |

### 3.2 API Gateway  

| Item | Tech | Responsibility |
|------|------|----------------|
| Framework | FastAPI | Async request handling, OpenAPI generation |
| Auth | OAuth2 Authorization Code Flow + JWT validation (PyJWT) | Enforce RBAC |
| Validation | Pydantic v2 models | Request/response schema |
| Rate‑limit | `slowapi` (Redis‑backed) | Prevent abuse |
| Docs | Swagger UI (auto‑generated) | Interactive API exploration |

### 3.3 Core Services  

| Service | Module | Key Functions
