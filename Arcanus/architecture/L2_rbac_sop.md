# Layer 2: Role-Based Access Control (RBAC) SOP

## Description

The second layer enforces contextual, cryptographic usage policies based on the user's role. It matches the user's role against restricted operational keywords, utilizing FHE/PHE (Concrete ML/LightPHE) to evaluate encrypted vectors from Supabase.

## Inputs

- `user_id`: UUID of the requester.
- `role`: Role of the user (e.g., "intern", "manager", "hr_admin").
- `prompt`: The sanitized user input from L1.

## Outputs

- `action`: `ALLOW` or `BLOCK`.
- `reason`: Explanation of the clearance violation.

## Core Rules (The "Badge Check" List)

1. **Role Context Mapping**:
   - `intern`: Cannot access ["salary", "payroll", "performance review", "social security", "termination"].
   - `manager`: Cannot access ["board meetings", "merger", "ceo compensation"].
   - `hr_admin`: Unrestricted keywords.
2. **Encrypted Vector Similarity (FHE Integration - Mock/Target)**:
   - Encrypt the restricted keywords list using FHE.
   - Compute semantic cosine similarity against the `prompt` embedding entirely in the encrypted domain.
   - If similarity > 0.85 and role lacks clearance, BLOCK.

## Invariants

- Execution must complete within **40ms** (total backend timeout for L1 + L2 = 50ms).
- Fallback to exact-keyword matching if FHE engine timeout occurs.
- Fail closed: If user role is unrecognized or Redis session lookup fails, RETURN BLOCK.
