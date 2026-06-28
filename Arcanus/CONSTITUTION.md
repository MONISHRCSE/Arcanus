# Project Constitution

## Data Schemas

### 1. Firewall Request Payload (Input)

```json
{
  "user_id": "string",
  "role": "string",
  "prompt": "string",
  "session_id": "string (optional)"
}
```

### 2. Firewall Response Payload (Internal Routing)

```json
{
  "action": "ALLOW | BLOCK",
  "reason": "string",
  "layer_triggered": "0 (None) | 1 (Heuristic) | 2 (RBAC) | 3 (LLM Judge)",
  "threat_score": "number (0-100)",
  "safe_prompt": "string (Passed to core AI if ALLOW)"
}
```

### 3. Audit Log Payload (Database/Storage)

```json
{
  "timestamp": "ISO8601 string",
  "user_id": "string",
  "role": "string",
  "original_prompt": "string",
  "action": "ALLOW | BLOCK",
  "layer_triggered": "number",
  "threat_score": "number",
  "reason": "string"
}
```

## Behavioral Rules

1. **Deny by Default:** If any layer fails or throws an error, the request is BLOCKED.
2. **Zero-Trust Input:** All natural language prompts are treated as potentially hostile.
3. **Deterministic First:** Layers 1 (Heuristics) and 2 (RBAC) must execute deterministically before the probabilistic Layer 3 (LLM Judge) is invoked.
4. **Total Auditability:** Every single request, regardless of whether it was allowed or blocked, MUST be recorded in the Audit Log Payload format.
5. **No Hallucination on Blocks:** Block messages to the user must be standardized and not generated dynamically by an LLM to prevent prompt leakage.

## Architectural Invariants

- **Layer 1 (Architecture):** Technical SOPs in Markdown. Always update SOP before code.
- **Layer 2 (Navigation):** Reasoning layer for routing data.
- **Layer 3 (Tools):** Deterministic Python scripts. Atomic and testable.
- **Data-First:** Schema must be defined before building any Tool.
- **Self-Annealing:** Analyze error -> Patch script -> Test -> Update Architecture SOP.

## Critical Stack Constraints

- **Framework (API/Gateway):** Use **FastAPI** (Python 3.12+) with `uvloop` for high-throughput, async-first request routing. Do not use Flask, Django, or synchronous frameworks.
- **AI / LLM Orchestration:** Use **LiteLLM** for unified model routing, fallbacks, and cost-tracking. Do not write custom API wrappers for individual model providers (e.g., OpenAI or Anthropic SDKs directly).
- **Validation Layer:** Use **Pydantic v2** (Rust-based) strictly for all schema validation (Request, Response, Audit). Do not use manual type casting or raw JSON dictionaries for data passing.
- **State & Caching:** Use **Redis** (via `redis.asyncio`) for semantic caching, exact-match blocking, and RBAC session lookups. Do not use in-memory dictionaries that break horizontal scaling.
- **Database / Audit Trails:** Use **Supabase (Postgres with pgvector)**. Interacting via **Drizzle ORM** on the frontend and the **Supabase Python Client** for background fire-and-forget logging. Audit logs are mission-critical. Do not use MongoDB or unstructured NoSQL stores.

## Senior Coding Standards

1. **Aggressive Latency Budgets:**
   Layers 1 (Heuristics) and 2 (RBAC) must execute within a rigid **50ms budget**. Wrap these deterministic layers in `asyncio.wait_for()`. If a timeout is hit, trigger a immediate Fail-Closed (Block).
2. **Streaming with Mid-Stream Intercepts:**
   If Layer 3 evaluates to ALLOW, responses to the user must be streamed via Server-Sent Events (SSE). Implement mid-stream interceptors to terminate the connection instantly if late-stage models generate a blockable chunk mid-flight.
3. **Semantic Fire-walling at the Edge:**
   Always hash and normalize the incoming prompt (strip whitespace, lowercase). Check this against a Redis semantic cache of known malicious inputs. An >0.98 cosine similarity triggers an immediate Layer 1 block, completely bypassing the expensive LLM Judge.
4. **Fire-and-Forget Auditing:**
   Writing to the Audit Log database must never delay the firewall's response to the user. Decouple logging using background queues (e.g., FastAPI `BackgroundTasks` or Celery). Database latency must explicitly equal zero impact on TTFT (Time To First Token).
5. **No Blind "Rewrite" Retries:**
   If the LLM Judge flags a prompt as harmful, block it outright. Do not automatically ask the internal LLM to "rewrite it nicely" more than once. Log the violation and immediately penalize the `user_id` threat score.
6. **Zero-Trust Tool Sandboxing:**
   Deterministic Python scripts in Layer 3 must operate without implicit privileges. They must not have access to OS environment variables (`os.environ`), the local file system, or open internet sockets unless explicitly dependency-injected at execution time.
