class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        for x, y, z in zip(s, s[1:], s[2:]):
            if x != y and x != z and y != z:
                count += 1
        
        return count
        count = 0
        
"
