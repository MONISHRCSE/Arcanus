# Findings

## Research

- The project is an MVP for a hackathon.
- Target domain: Enterprise Analytics (HR data focus).
- Concept: A privacy-preserving intelligent system acting as an **Agentic AI Firewall**.
- Alignment: SDGs 8 (Decent Work/Privacy), 9 (Resilient Infrastructure), 16 (Accountable Institutions).

### Potential Hackathon Novelties (PPML - Privacy-Preserving Machine Learning)

To maximize the MVP's competitive edge, we will integrate a multi-layered PPML approach:

1. **Zero-Knowledge Machine Learning (ZK-ML):** Using **EZKL** (Python) to generate cryptographic proofs that the Layer 3 LLM Judge securely evaluated a prompt against our proprietary firewall SOPs without revealing the prompt or the rules.
2. **Encrypted Vector Search (FHE/PHE):** Using **Concrete ML** (by Zama) or **LightPHE** to encrypt HR data embeddings _before_ they are stored in Supabase pgvector. The semantic caching and RBAC heuristics evaluate cosine similarities on cyphertexts.
3. **Trusted Execution Environments (TEEs):** Designing the architecture such that the Layer 3 Python deterministic scripts conceptually run inside a Secure Enclave (e.g., AWS Nitro Enclaves simulation), proving the host OS cannot observe the LLM's raw memory.
4. **LLM-Firewall Concept:** Market research shows "LLM Firewalls" (like Securiti.ai) are the pinnacle of 2024/2025 AI security. Our MVP intercepts prompt injection, jailbreaks, and persona-switching natively.

## Discoveries & Learnings

- **Security Gauntlet Architecture:**
  1. **Layer 1: Heuristic Scanner** - Zero-latency, pattern-based detection (e.g., Base64, "ignore previous instructions").
  2. **Layer 2: Role-Based Access Control (RBAC)** - Context-aware policy enforcement (e.g., Interns cannot query "salary").
  3. **Layer 3: LLM-as-a-Judge** - Semantic intent analysis assigning a "threat score".
- **Delivery Payload:** The final product needs to be a web-based MVP dashboard showing the firewall intercepting requests and maintaining an Audit Trail.

## Constraints

- **Speed vs. Security:** Layers 1 and 2 must be extremely fast to minimize latency before hitting the heavier Layer 3.
- **Cost:** Layer 3 requires LLM API calls, which costs money and time; thus, Layers 1 and 2 should aggressively filter bad requests first.
- **Scope limitation:** This is an MVP for a small crowd presentation, so mock HR databases or simple in-memory stores can be used instead of actual integrations with enterprise ERPs.
