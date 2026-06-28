# Layer 1: Heuristic Scanner SOP

## Description

The first layer of the **Agentic AI Firewall**. Provides zero-latency, deterministic filtering of incoming prompts using exact-match signatures, RegEx, and basic pattern recognition.

## Inputs

- `prompt`: The raw user input string.

## Outputs

- `action`: `ALLOW` or `BLOCK`.
- `reason`: Explicit rule triggered (e.g., "B64_ENCODED_PAYLOAD").

## Core Rules (The "Instant Block" List)

1. **Instruction Override Patterns**:
   - Matches: `ignore previous instructions`, `forget what I told you`, `system prompt`.
2. **Obfuscation Detection**:
   - Detects Base64 patterns exceeding a certain length.
   - Detects excessive hex encoding.
3. **Semantic Exact-Match Cache (Redis)**:
   - Normalize prompt (lowercase, strip whitespace).
   - Compute hash. Check Redis for known bad hashes.

## Invariants

- Execution must complete within **10ms**.
- Do NOT perform LLM calls or complex semantic embeddings here.
- Fail closed: If regex compilation fails or timeout is hit, RETURN BLOCK.
