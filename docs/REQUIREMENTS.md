# REQUIREMENTS.md – sql‑quest  

**Document version:** 1.0 – 2026‑06‑19  
**Author:** Senior Product/Engineering Lead, Axentx  

---  

## 1. Overview  

`sql-quest` is a **SQL query management platform** that automates, tracks, and streamlines execution of ad‑hoc (one‑off) queries across heterogeneous data sources. It is built for data engineers who need a repeatable, auditable, and secure workflow for extracting, transforming, and delivering data without writing custom scripts for each source.

The product must:

* Provide a unified interface (web UI + CLI) to author, store, and run queries.  
* Support connections to the major relational and analytical stores used by our customers (PostgreSQL, MySQL, Snowflake, BigQuery, Redshift, Azure Synapse, etc.).  
* Enforce role‑based access control (RBAC) and secret management for credentials.  
* Capture full execution metadata (who, when, source, runtime, row count, errors).  
* Export results in common formats (CSV, JSON, Parquet) and optionally push to downstream destinations (S3, GCS, Azure Blob, Kafka).  
* Integrate with existing Axentx pipelines (e.g., validation, monitoring, billing) via REST/Webhooks.  

---  

## 2. Functional Requirements  

| ID | Requirement | Description |
|----|-------------|-------------|
| **FR‑1** | **Multi‑source connectivity** | The system shall allow administrators to configure connections to at least the following data sources: PostgreSQL, MySQL, MariaDB, Microsoft SQL Server, Snowflake, Google BigQuery, Amazon Redshift, Azure Synapse. Each connection must support TLS encryption and optional IAM/SSO authentication. |
| **FR‑2** | **Secure credential storage** | Database credentials, API keys, and OAuth tokens shall be stored encrypted at rest using a customer‑provided KMS (AWS KMS, GCP KMS, Azure Key Vault) or the built‑in Axentx vault. Retrieval must be audited. |
| **FR‑3** | **Query authoring & versioning** | Users shall be able to create, edit, and save SQL statements in the UI/CLI. Each saved query must be versioned (auto‑incremented) and retain a changelog (author, timestamp, diff). |
| **FR‑4** | **Parameterized execution** | Queries may declare named parameters (`{{param}}`). At execution time the user (or an automated trigger) must supply values via a JSON payload or UI form. Validation of parameter types (string, number, date) shall be performed before execution. |
| **FR‑5** | **One‑off execution workflow** | A user can trigger a saved query as a “one‑off” run. The system shall: <br> a. Resolve the target connection. <br> b. Substitute parameters. <br> c. Execute the statement. <br> d. Capture execution metadata (start/end time, rows processed, CPU/IO). <br> e. Store the result set (up to 10 M rows) in a temporary result store. |
| **FR‑6** | **Result export & delivery** | After execution, the user may: <br> a. Download results as CSV, JSON, or Parquet. <br> b. Push results to a configured external bucket (S3, GCS, Azure Blob). <br> c. Publish to a Kafka topic (optional). |
| **FR‑7** | **Audit logging** | Every operation (create, edit, delete, execute, export, permission change) must be logged to the central Axentx audit service with user ID, timestamp, and operation details. |
| **FR‑8** | **RBAC & SSO integration** | The platform shall integrate with the corporate IdP (SAML 2.0 / OIDC) and support role definitions: *Viewer*, *Editor*, *Operator*, *Admin*. Permissions map to CRUD on queries, execution rights, and connection management. |
| **FR‑9** | **CLI & API** | A fully‑featured command‑line client (`sql-quest-cli`) and a RESTful API (OpenAPI 3.0) shall expose all UI functionality: connection CRUD, query CRUD, execution, export, and audit retrieval. |
| **FR‑10** | **Scheduling hooks (optional)** | Although primary use‑case is one‑off, the system shall expose a webhook endpoint that external schedulers (Airflow, Prefect) can call to trigger a query execution with a JSON payload. |
| **FR‑11** | **Error handling & retry** | If a query fails due to transient connectivity or timeout, the system shall automatically retry up to 2 times with exponential back‑off. Persistent failures must be reported to the user and logged. |
| **FR‑12** | **Integration with Axentx validation pipeline** | Upon successful execution, the system shall emit a `query.completed` event to the Axentx event bus, containing query ID, result location, and metadata for downstream validation. |
| **FR‑13** | **Search & tagging** | Users shall be able to tag queries (e.g., `finance`, `etl`, `ad‑hoc`) and search by name, tag, owner, or source connection. |
| **FR‑14** | **Multi‑tenant isolation** | In a SaaS deployment, each tenant’s data (connections, queries, results
