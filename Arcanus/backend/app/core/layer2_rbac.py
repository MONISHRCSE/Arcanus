from typing import List

class Layer2RBAC:
    def __init__(self):
        # Mocking the restricted keywords for the hackathon MVP.
        # In a full FHE/Encrypted Vector DB setup, this would query Supabase pgvector
        # with Concrete ML encrypted embeddings for similarity > 0.85
        self.restricted_contexts = {
            "intern": ["salary", "payroll", "performance review", "social security", "termination", "ceo compensation"],
            "manager": ["board meetings", "merger", "ceo compensation", "c-suite"],
            "hr_admin": [] # Unrestricted
        }
    
    async def evaluate(self, user_id: str, role: str, prompt: str) -> bool:
        """
        Evaluate if the prompt passes Layer 2 specific to the user's role.
        """
        # 1. Fetch restrictions for role
        role_lower = role.lower()
        if role_lower not in self.restricted_contexts:
            # Deny by default if role is unrecognized 
            return False
            
        restrictions = self.restricted_contexts[role_lower]
        
        if not restrictions:
            return True # HR Admin
            
        # 2. Basic semantic intersection (Mocking the FHE Encrypted Vector search)
        prompt_lower = prompt.lower()
        for restricted_term in restrictions:
            if restricted_term in prompt_lower:
                # In production: Compute Cosine Similarity between FHE encrypted 'prompt' and 'restricted_term'
                return False
                
        return True
