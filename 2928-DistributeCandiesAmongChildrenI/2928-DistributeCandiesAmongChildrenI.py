class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for c1 in range(limit+1):
            for c2 in range(limit+1):
                c3 = n - c1 - c2
                if c3 >= 0 and c3 <= limit:
                    ans += 1
        return ans
        
5
