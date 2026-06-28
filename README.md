# Arcanus: Privacy-Preserving Firewall for Agentic AI 🛡️

<!-- Add your project banner/screenshot here, e.g.: -->
<!-- <img width="1920" height="1080" alt="Arcanus Dashboard" src="YOUR_IMAGE_URL_HERE" /> -->

[![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-React-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![Redis](https://img.shields.io/badge/Redis-Caching-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Supabase](https://img.shields.io/badge/Supabase-pgvector-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge)](https://docs.pydantic.dev/)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-Orchestration-purple?style=for-the-badge)](https://www.litellm.ai/)

> *⚠️ Disclaimer:* Arcanus is a research/educational security prototype targeting enterprise HR-data scenarios. The advanced PPML features (ZK-ML, TEEs) are in active development — review the project status before relying on them in production.

---

## Problem Statement

- *Prompt Injection & Jailbreaking:* Agentic AI systems connected to sensitive enterprise data (e.g., HR records) are vulnerable to natural-language attacks that override their original instructions.

- *Unauthorized Data Exfiltration:* Without strict access controls, any user can phrase a query to extract data they shouldn't have access to — regardless of their actual role.

- *Persona-Switching Attacks:* Attackers often try to manipulate an AI agent into adopting a different "persona" that ignores its original safety constraints.

- *No Privacy-Preserving Audit Trail:* Most enterprise AI deployments lack a way to audit *every* request without exposing the sensitive content of those requests.

- There is a need for a *zero-trust security interception layer* that sits between users and core enterprise AI agents — fast enough not to add noticeable latency, but rigorous enough to catch both obvious and subtle attacks.

---

## Project Objective

*Arcanus* is a 3-layer privacy-preserving firewall designed specifically for agentic AI systems, acting as a security gauntlet between users and core enterprise AI agents.

The platform aims to:
- *Deny by Default:* Every request must pass all three security layers — failing any one results in an immediate block.
- *Zero-Latency First Pass:* Catch obvious attacks deterministically within a strict 10ms budget, before any expensive LLM call.
- *Role-Aware Enforcement:* Apply context-aware policies based on the user's actual role, not just the phrasing of their request.
- *Full Auditability Without Latency Cost:* Log every allowed/blocked request in the background with zero impact on time-to-first-token (TTFT).

---

## Sustainable Development Goals (SDGs)

### SDG 8: Decent Work and Economic Growth
- *Target 8.8:* Protects employee privacy and labor data (e.g., salary information) from unauthorized access by enforcing strict role-based policies.

### SDG 9: Industry, Innovation and Infrastructure
- *Target 9.c:* Builds resilient, security-hardened infrastructure for the safe adoption of agentic AI in enterprise environments.

### SDG 16: Peace, Justice and Strong Institutions
- *Target 16.5 / 16.6:* Promotes accountable, transparent institutions through full request auditability and deny-by-default access governance.

---

## Proposed Solution

Arcanus uses a *3-Layer Security Gauntlet* architecture. Every incoming natural-language request must successfully clear all three layers before reaching the core enterprise AI — if any layer fails, the request is blocked immediately.

### Architecture & Workflow:

<img width="1536" height="1024" alt="ChatGPT Image Jun 28, 2026, 12_38_42 PM" src="https://github.com/user-attachments/assets/43842953-2487-44f2-b355-1d4b48ea268b" />


*Request flow through the 3-layer gauntlet — Heuristics → RBAC → LLM Judge*

1. *Layer 1 — Heuristic Scanner (Instant Block):* Zero-latency, deterministic filtering using exact-match signatures and RegEx — catches explicit instruction overrides, Base64-encoded payloads, and known-bad semantic hashes via Redis. Must execute within a 10ms budget.
2. *Layer 2 — Role-Based Access Control (Badge Check):* Maps the user's role to forbidden keyword groups. An "intern" role querying "salary" is blocked instantly, regardless of phrasing.
3. *Layer 3 — LLM-as-a-Judge (Smart Guard):* For prompts that survive Layers 1 and 2, a secondary high-speed LLM evaluates semantic intent and assigns a threat score (0–100). Crossing the risk threshold triggers a block.
4. *Audit Logging:* Every request — allowed or blocked — is logged via a fire-and-forget background task to Supabase, so auditing never adds latency to the response.
5. *Admin Dashboard:* A real-time Audit Trail dashboard displays allowed/blocked requests, threat scores, and overall system health.

---

## 🛠️ Technologies Used

### *Backend (The Gauntlet)*
- *Framework:* FastAPI (Python 3.11+) running on `uvloop` for high-throughput async routing
- *Validation:* Pydantic v2 (Rust-based) — aggressive schema validation, no manual type casting
- *AI Orchestration:* LiteLLM for unified model routing, fallbacks, and cost tracking
- *State & Caching:* Redis (`redis.asyncio`) for semantic caching and exact-match blocking

### *Database & Auditing*
- *Database:* Supabase (PostgreSQL with `pgvector`)
- *Auditing:* Fire-and-forget background tasks — zero impact on time-to-first-token (TTFT)

### *Frontend (The Dashboard)*
- *Framework:* Next.js / React (Node.js v18+)
- *Purpose:* Real-time Audit Trail dashboard for admins to monitor requests, threat scores, and system health

### *Advanced Privacy Features (PPML — In Progress)*
- *Zero-Knowledge ML:* EZKL for cryptographic proofs that rules were applied without revealing the prompt
- *Encrypted Vector Search:* Concrete ML / LightPHE for encrypting embeddings before storage
- *Trusted Execution Environments:* Secure enclaves for running evaluation scripts away from memory observation

---

## 🎯 Key Features

- ✅ *Deny-by-Default Gauntlet:* All three layers must pass; any failure blocks the request immediately
- ✅ *10ms Heuristic Layer:* Instant blocking of known attack signatures and encoded payloads
- ✅ *Role-Aware RBAC:* Context-sensitive keyword policies tied to the user's actual role
- ✅ *LLM-as-a-Judge:* Catches subtle, semantically-disguised prompt injection and jailbreak attempts
- ✅ *Zero-Latency Auditing:* Every request logged in the background with no TTFT impact
- ✅ *Live Admin Dashboard:* Real-time visibility into allowed/blocked requests and threat scores
- 🔄 *Privacy-Preserving ML (Upcoming):* ZK-ML, encrypted vector search, and TEE-based evaluation

---

## 📸 Demo / Screenshots

### 1. Dashboard Overview
The real-time Audit Trail dashboard — allowed/blocked requests, threat scores, and system health at a glance.
<img width="1919" height="963" alt="Screenshot 2026-05-27 130054" src="https://github.com/user-attachments/assets/29f8e9e1-7320-428a-bd10-4f849546c682" />


### 2. RBAC Denied
A request blocked at the Role-Based Access Control layer — e.g., an "intern" role querying restricted HR data.
><img width="1919" height="968" alt="Screenshot 2026-05-27 130112" src="https://github.com/user-attachments/assets/84aa978b-ab4d-420e-a88e-880af66aa8c9" />

### 3. RBAC Allowed
A request that successfully clears the RBAC layer based on the user's permitted role.
<img width="1909" height="957" alt="Screenshot 2026-05-27 130141" src="https://github.com/user-attachments/assets/1469c181-1cde-430d-9c8c-53e6ea5b70d5" />


---

## 💻 Local Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Redis instance
- A Supabase project (PostgreSQL + pgvector)

### 1. Clone the Repository
```bash
git clone https://github.com/MonishRCSE/Arcanus.git
cd Arcanus
```

### 2. Start the Backend Gauntlet
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env   # add Redis URL, Supabase credentials, LiteLLM keys
uvicorn main:app --reload --port 8000
```
The API will be available at `http://localhost:8000/docs`

### 3. Start the Frontend Dashboard
```bash
cd frontend
npm install
npm run dev
```
The dashboard will be available at `http://localhost:3000`

---

## 📊 Project Status

Based on the project's master ledger:

| Domain | Status | Notes |
|:-------|:-------|:------|
| *Backend Infrastructure* | ✅ *Completed* | Schema definitions + service skeleton |
| *3-Layer Gauntlet* | ✅ *Completed* | Heuristics, RBAC, and LLM Judge all implemented |
| *Frontend Dashboard* | 🔄 *In Progress* | Stylizing MVP Audit Trail UI in Next.js |
| *PPML Features* | 🔄 *In Progress* | ZK-ML, encrypted vector search, TEEs |
| *E2E Testing & Deployment* | ⏳ *Pending* | Latency optimization + final deployment |

---

<p align="center">
  <strong>Zero-Trust for Every Prompt</strong><br>
  Built with ❤️ by Monish
</p>
