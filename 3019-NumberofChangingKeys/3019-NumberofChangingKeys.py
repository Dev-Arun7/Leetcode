    def countKeyChanges(self, s: str) -> int:
        new = s.lower()
        l = len(new)
        return sum( 1 for i in range(l-1) if new[i] != new[i+1])



class Solution:
        
        
"
