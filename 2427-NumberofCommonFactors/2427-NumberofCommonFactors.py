class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = sum(1 for i in range(1,min(a,b)+1) if a % i == 0 and b % i == 0)
        return count
        
1
