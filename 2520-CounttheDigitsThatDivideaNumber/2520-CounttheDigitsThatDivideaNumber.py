class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        ref = num
        while ref > 0:
            d =  ref % 10
            if num % d == 0:
                count += 1
            ref //= 10
        return count        
7
