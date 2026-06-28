from pydantic import BaseModel, Field
from typing import Optional

class FirewallRequestPayload(BaseModel):
    user_id: str = Field(..., description="UUID of the requester")
    role: str = Field(..., description="Role of the user (e.g., intern, manager, hr_admin)")
    prompt: str = Field(..., description="The natural language prompt to evaluate")
    session_id: Optional[str] = Field(None, description="Optional session tracking ID")

class FirewallResponsePayload(BaseModel):
    action: str = Field(..., description="ALLOW or BLOCK")
    reason: str = Field(..., description="Explanation of the verdict")
    layer_triggered: int = Field(..., description="0 (None), 1 (Heuristic), 2 (RBAC), 3 (LLM Judge)")
    threat_score: int = Field(..., ge=0, le=100, description="Computed vulnerability score (0-100)")
    safe_prompt: Optional[str] = Field(None, description="The passed prompt if ALLOW")

class AuditLogPayload(BaseModel):
    timestamp: str
    user_id: str
    role: str
    original_prompt: str
    action: str
    layer_triggered: int
    threat_score: int
    reason: str
