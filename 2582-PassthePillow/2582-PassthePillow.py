class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n-1)
        remainder = time % (n-1)
        if cycle % 2 == 1:
            return n - remainder
        else:
            return 1 + remainder
        
4
