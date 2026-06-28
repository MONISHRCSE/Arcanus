# Layer 3: LLM-as-a-Judge (ZK-ML) SOP

## Description

The final, probabilistic layer of the security gauntlet. Evaluates the semantic intent of the prompt to detect subtle or novel attacks (e.g., storytelling, persona-switching).

## Inputs

- `prompt`: The sanitized user input from L2.

## Outputs

- `action`: `ALLOW` or `BLOCK`.
- `threat_score`: Integer (0-100).
- `reason`: Extracted explanation of malicious intent.

## Core Rules (The "Smart Guard")

1. **LLM Orchestration**:
   - Use `litellm` to call the default model (e.g., Grok-4-latest / GPT-4o-mini).
   - System prompt must strictly ask the model to act as a cybersecurity evaluator and output JSON conforming exactly to the Firewall Response Payload schema.
2. **Zero-Knowledge Machine Learning (ZK-ML Integration - Target)**:
   - Execute the inference graph within `ezkl`.
   - Generate a ZK-SNARK proof demonstrating the `threat_score` was computed by the approved LLM weights against the approved system prompt, ensuring the prompt was not read by a centralized server admin.
3. **Thresholding**:
   - Any `threat_score >= 75` is an automatic BLOCK.
   - Any score below 75 is an ALLOW, triggering the SSE streaming of the safe prompt to the downstream AI worker.

## Invariants

- This layer has no hard timeout but must be fully asynchronous.
- No "Rewrite" retries. If the LLM returns an invalid JSON or a score >= 75, we immediately block.
- Total Auditability: The resulting ZK-Proof and the exact threat score are shipped to the Postgres database via a background task.
