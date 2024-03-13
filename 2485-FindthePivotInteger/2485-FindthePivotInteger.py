class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n * (n+1)) // 2
        right = 0
        for i in range(n, -1, -1):
            right += i
            if right == total - right + i:
                return i
        return -1
        
8
