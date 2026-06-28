import re

class Layer1HeuristicScanner:
    def __init__(self):
        # Known instruction overrides
        self.forbidden_patterns = [
            r"ignore previous instructions",
            r"forget what i told you",
            r"system prompt",
            r"you are now",
            r"bypass your safety"
        ]
        self.pattern_regex = re.compile("|".join(self.forbidden_patterns), re.IGNORECASE)
    
    async def evaluate(self, prompt: str) -> bool:
        """
        Evaluate if the prompt passes Layer 1.
        Returns False if malicious (BLOCK), True if safe (ALLOW).
        """
        # 1. Regex Match for Overrides
        if self.pattern_regex.search(prompt):
            return False
            
        # 2. Base64 Obfuscation detection (naive heuristic)
        # Often prompt injections hide behind Base64. If a long, uninterrupted string > 50 chars matches b64, flag it.
        b64_pattern = re.compile(r"^[A-Za-z0-9+/]{50,}={0,2}$")
        for word in prompt.split():
            if b64_pattern.match(word):
                return False
                
        # 3. Redis Exact Match Semantic Cache checking would go here...
        
        return True
