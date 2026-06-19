# Business Model Canvas – **sql‑quest**

> **Product**: A SQL query management tool that automates and streamlines one‑off queries from heterogeneous data sources for data engineers.  
> **Company**: Axentx – AI‑driven autonomous product development platform.  

---  

## 1. Value Proposition
| What we deliver | Why it matters |
|-----------------|----------------|
| **Instant, AI‑assisted query generation** – Leverages vLLM / SGLang to turn natural‑language requests into production‑ready SQL. | Cuts query‑writing time by ≈ 70 % for ad‑hoc analysis. |
| **Unified source‑agnostic connector layer** – Pulls data from Snowflake, BigQuery, Redshift, Postgres, MySQL, and on‑prem warehouses via a single UI/CLI. | Eliminates the need for custom ETL scripts per source. |
| **Versioned, auditable query store** – Every one‑off query is automatically persisted, tagged, and linked to data lineage. | Satisfies governance, compliance, and reproducibility requirements. |
| **Automated scheduling & result delivery** – Run once‑off queries on a timer, push results to Slack, email, or data lake. | Turns “one‑off” into repeatable, low‑maintenance workflows. |
| **Built‑in performance diagnostics** – Query cost estimator, execution plan visualizer, and auto‑tuning suggestions. | Reduces cloud spend and prevents runaway queries. |
| **Zero‑code integration** – REST/GraphQL API + Terraform provider for CI/CD pipelines. | Enables DevOps‑style management of analytical workloads. |

---

## 2. Customer Segments
| Segment | Primary Pain Points | Typical Buyer |
|---------|---------------------|---------------|
| **Data‑engineering teams** (mid‑size SaaS, fintech, e‑commerce) | Repetitive ad‑hoc queries, lack of audit trail, fragmented connectors. | Lead Data Engineer / Analytics Manager |
| **BI & Analytics squads** (enterprise) | Need fast, reliable access to disparate warehouses without writing SQL. | Head of Business Intelligence |
| **Data‑platform SaaS providers** (e.g., DBaaS, data‑mesh platforms) | Want to embed query‑as‑a‑service for their customers. | Product Manager, Platform Integration |
| **Consulting & Managed‑service firms** | Delivering one‑off analyses for multiple clients; need repeatable, billable process. | Senior Consultant / Delivery Lead |
| **Compliance‑focused orgs** (healthcare, finance) | Must retain query provenance and data‑lineage for audits. | Governance Officer / CISO |

---

## 3. Channels
| Channel | Description | Rationale |
|---------|-------------|-----------|
| **Product website & free tier** – self‑service sign‑up with 5 k query credits/mo. | Low‑friction acquisition, builds community. |
| **Marketplace listings** – AWS Marketplace, GCP Marketplace, Snowflake Marketplace. | Leverages existing procurement pipelines of target customers. |
| **Partner integrations** – native plugins for dbt, Airflow, Prefect, and Terraform Registry. | Captures DevOps‑oriented users already using those tools. |
| **Direct sales & enterprise demos** – targeted outreach to Fortune 500 data teams. | Accelerates high‑value contract closures. |
| **Developer evangelism** – webinars, open‑source SDKs, GitHub repos, conference talks. | Drives adoption and contributes to the open‑source connector ecosystem. |
| **Channel partners** – System integrators & consulting firms (e.g., Accenture, Deloitte). | Extends reach into regulated industries. |

---

## 4. Revenue Streams
| Stream | Pricing Model | Target Segment | Expected Contribution |
|--------|---------------|----------------|-----------------------|
| **SaaS subscription** – Tiered plans (Starter $49/mo, Professional $199/mo, Enterprise $799/mo). | Recurring subscription. | SMB & mid‑size teams. | 55 % |
| **Usage‑based add‑on** – Extra query credits, high‑volume data‑transfer, premium AI inference (vLLM). | Pay‑as‑you‑go per 1 k queries or per GB processed. | High‑volume enterprises. | 20 % |
| **Professional services** – On‑boarding, custom connector development, compliance audit assistance. | Fixed‑price or time‑and‑materials. | Enterprises & consulting firms. | 15 % |
| **Marketplace revenue share** – 70/30 split with cloud providers. | Embedded licensing. | Cloud‑native customers. | 5 % |
| **Data‑lineage API licensing** – Separate API key for external governance platforms. | Annual license. | Governance vendors. | 5 % |

*All plans include a 14‑day free trial with 10 k query credits.*

---

## 5. Cost Structure
| Category | Main Cost Drivers | Mitigation Strategies |
|----------|-------------------|-----------------------|
| **Engineering & R&D** – salaries (backend, UI, AI/ML, infra). | Core product development, AI model fine‑tuning (vLLM). | Leverage Axentx autonomous workforce; reuse existing codebases (e.g., iceoryx2 for IPC).
