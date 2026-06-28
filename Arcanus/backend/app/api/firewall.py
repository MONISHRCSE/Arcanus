import asyncio
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import ValidationError
from datetime import datetime

from ..models.schemas import FirewallRequestPayload, FirewallResponsePayload, AuditLogPayload
from ..core.layer1_heuristic import Layer1HeuristicScanner
from ..core.layer2_rbac import Layer2RBAC
from ..core.layer3_judge import Layer3LLMJudge

router = APIRouter(prefix="/firewall", tags=["firewall"])

# Initialize Singletons
l1_scanner = Layer1HeuristicScanner()
l2_rbac = Layer2RBAC()
l3_judge = Layer3LLMJudge()

from ..core.db import supabase

def write_audit_log(payload: AuditLogPayload):
    """
    Fire-and-forget database write to Supabase.
    """
    if supabase is None:
        print("[AUDIT LOG - MOCKED / NO DB KEYS]", payload.dict())
        return

    try:
        data = {
            "timestamp": payload.timestamp,
            "user_id": payload.user_id,
            "role": payload.role,
            "original_prompt": payload.original_prompt,
            "action": payload.action,
            "layer_triggered": payload.layer_triggered,
            "threat_score": payload.threat_score,
            "reason": payload.reason
        }
        res = supabase.table("audit_logs").insert(data).execute()
        print(f"[Supabase Insert Success] Action={payload.action} | Threat={payload.threat_score}")
    except Exception as e:
        print(f"[Supabase Audit Log Error]: {e}")

@router.post("/evaluate", response_model=FirewallResponsePayload)
async def evaluate_prompt(request: FirewallRequestPayload, background_tasks: BackgroundTasks):
    """
    The main Security Gauntlet endpoint.
    Executes L1 and L2 under a rigid 50ms latency budget.
    Executes L3 asynchronously if L1 and L2 pass.
    """
    # ---------------------------------------------------------
    # LAYER 1: Heuristic Scanner (Zero-Latency)
    # ---------------------------------------------------------
    try:
        # Wrap in timeout as per Senior Coding Standards
        l1_passed = await asyncio.wait_for(l1_scanner.evaluate(request.prompt), timeout=0.02)
        if not l1_passed:
            verdict = FirewallResponsePayload(
                action="BLOCK", reason="Layer 1: Malicious Pattern Detected", layer_triggered=1, threat_score=100
            )
            background_tasks.add_task(write_audit_log, AuditLogPayload(
                timestamp=datetime.utcnow().isoformat(), user_id=request.user_id, role=request.role,
                original_prompt=request.prompt, action=verdict.action, layer_triggered=verdict.layer_triggered,
                threat_score=verdict.threat_score, reason=verdict.reason
            ))
            return verdict
    except asyncio.TimeoutError:
        verdict = FirewallResponsePayload(action="BLOCK", reason="Layer 1 Timeout", layer_triggered=1, threat_score=100)
        return verdict

    # ---------------------------------------------------------
    # LAYER 2: Request-Based Access Control (RBAC)
    # ---------------------------------------------------------
    try:
        l2_passed = await asyncio.wait_for(l2_rbac.evaluate(request.user_id, request.role, request.prompt), timeout=0.03)
        if not l2_passed:
            verdict = FirewallResponsePayload(
                action="BLOCK", reason="Layer 2: RBAC Context Violation", layer_triggered=2, threat_score=100
            )
            background_tasks.add_task(write_audit_log, AuditLogPayload(
                timestamp=datetime.utcnow().isoformat(), user_id=request.user_id, role=request.role,
                original_prompt=request.prompt, action=verdict.action, layer_triggered=verdict.layer_triggered,
                threat_score=verdict.threat_score, reason=verdict.reason
            ))
            return verdict
    except asyncio.TimeoutError:
        verdict = FirewallResponsePayload(action="BLOCK", reason="Layer 2 Timeout", layer_triggered=2, threat_score=100)
        return verdict

    # ---------------------------------------------------------
    # LAYER 3: LLM Judge
    # ---------------------------------------------------------
    verdict = await l3_judge.evaluate(request.prompt)
    
    # Audit Logging
    background_tasks.add_task(write_audit_log, AuditLogPayload(
        timestamp=datetime.utcnow().isoformat(), user_id=request.user_id, role=request.role,
        original_prompt=request.prompt, action=verdict.action, layer_triggered=verdict.layer_triggered,
        threat_score=verdict.threat_score, reason=verdict.reason
    ))
    
    return verdict
