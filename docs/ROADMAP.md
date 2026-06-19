# Roadmap – sql‑quest

## Vision
sql‑quest is an **SQL query management tool** that automatically pulls, executes, and stores one‑off queries from disparate data sources (Snowflake, BigQuery, Redshift, Postgres, etc.). It gives data engineers a single, versioned, audit‑ready place to run ad‑hoc queries, share results, and iterate without manual copy‑paste or spreadsheet work.

---

## Release Cadence

| Release | Target Date | Focus |
|---------|-------------|-------|
| **MVP** | **2026‑07‑15** | Core query ingestion, execution, and result storage |
| **v1.0** | 2026‑09‑30 | UI, sharing, scheduling, basic security |
| **v2.0** | 2027‑02‑28 | Advanced analytics, AI‑assisted query generation, multi‑tenant |
| **v3.0** | 2027‑08‑15 | Enterprise integrations, compliance, performance tuning |

---

## MVP – Must‑Have for Launch

| Feature | Description | Acceptance Criteria | Notes |
|---------|-------------|---------------------|-------|
| **Source Connector Registry** | Plug‑in architecture for Snowflake, BigQuery, Redshift, Postgres, Athena, etc. | • At least 4 connectors fully tested<br>• Connector config UI in CLI | Use existing `sql-connector` library from repo |
| **Query Ingestion API** | POST `/queries` – accepts SQL string, source ID, optional metadata | • Returns query ID, status `queued`<br>• Validates syntax before execution | Leverage `sqlparse` for syntax check |
| **Execution Engine** | Async worker pool that runs queries on target DB, streams results to storage | • Supports streaming results up to 1 GB<br>• Handles timeouts & cancellations | Use `vLLM` for async execution wrapper |
| **Result Storage** | Store results in S3 (or MinIO) + metadata in Postgres | • Query result accessible via `/results/{id}`<br>• Retention policy 30 days | Use `sqlalchemy` for metadata |
| **Audit Trail** | Immutable log of who ran what, when, and why | • Every execution logged in `audit_log` table<br>• Exportable to CSV | Use `uuid` for query IDs |
| **CLI Tool** | `sql-quest run <sql>` – quick one‑off execution | • Prints results to terminal<br>• Saves to storage | Wraps API calls |
| **Basic Auth** | Token‑based authentication for API | • Token stored in env var `SQ_TOKEN` | Use `fastapi` + `JWT` |

> **MVP‑Critical**: Source connectors, ingestion API, execution engine, result storage, audit trail, CLI, and basic auth.

---

## v1.0 – Core Product

| Theme | Features | Milestone |
|-------|----------|-----------|
| **User Experience** | • Web UI (React) for query creation, history, and result viewing<br>• Drag‑and‑drop source selection | 2026‑08‑31 |
| **Collaboration** | • Shareable query links with read/write permissions<br>• Comment threads on queries | 2026‑09‑15 |
| **Scheduling** | • Cron‑style scheduling of queries<br>• Email/Slack notifications on completion | 2026‑09‑25 |
| **Security** | • Role‑based access control (RBAC)<br>• Encryption at rest for results | 2026‑09‑30 |
| **Documentation** | • Auto‑generated docs for connectors<br>• In‑app help | 2026‑09‑30 |

---

## v2.0 – Advanced Capabilities

| Theme | Features | Milestone |
|-------|----------|-----------|
| **AI Assistance** | • Prompt‑based query generation (LLM integration)<br>• Auto‑suggested optimizations | 2027‑01‑15 |
| **Analytics Layer** | • Query performance dashboards<br>• Cost estimation per execution | 2027‑01‑31 |
| **Multi‑Tenant** | • Isolated data per tenant<br>• Tenant‑level billing | 2027‑02‑15 |
| **Compliance** | • GDPR/CCPA audit logs<br>• Data masking options | 2027‑02‑28 |
| **Performance** | • Result caching<br>• Parallel query execution | 2027‑02‑28 |

---

## v3.0 – Enterprise & Ecosystem

| Theme | Features | Milestone |
|-------|----------|-----------|
| **Enterprise Integrations** | • SSO (OAuth2, SAML)<br>• LDAP sync | 2027‑06‑15 |
| **Observability** | • Distributed tracing (OpenTelemetry)<br>• Centralized logging | 2027‑07‑01 |
| **Marketplace** | • Publish connectors as plugins | 2027‑07‑15 |
| **Self‑Healing** | • Auto‑scaling workers based on queue depth | 2027‑08‑01 |
| **Compliance Certifications** | • SOC2, ISO27001 readiness | 2027‑08‑15 |

---

## Roadmap Governance

- **Backlog Grooming**: Weekly sprint planning in GitHub Projects (Kanban board).
- **Feature Flags**: All new features gated behind `feature/*` flags in `config.yaml`.
- **Metrics**: Track `query_execution_time`, `storage_cost`, `user_retention`.
- **Feedback Loop**: Monthly demo to internal data engineering squad; collect NPS.

---

## Dependencies & Risks

| Dependency | Status | Mitigation |
|------------|--------|------------|
| **Database connectors** | Open‑source libs (Snowflake, BigQuery, etc.) | Keep up‑to‑date; fallback to JDBC |
| **LLM inference** | vLLM | Use local GPU cluster; fallback to OpenAI API |
| **Storage** | S3/MinIO | Use multi‑region buckets; enable versioning |
| **Auth** | JWT | Rotate keys quarterly; monitor token leaks |

---

## Summary

- **MVP** delivers a fully functional, secure, and auditable query execution pipeline.  
- **v1.0** focuses on user experience and collaboration.  
- **v2.0** adds AI, analytics, and multi‑tenant capabilities.  
- **v3.0** scales to enterprise with compliance, observability, and marketplace.

This roadmap aligns with Axentx’s validated‑need, revenue‑focused product strategy and leverages our existing datasets and connector libraries.
