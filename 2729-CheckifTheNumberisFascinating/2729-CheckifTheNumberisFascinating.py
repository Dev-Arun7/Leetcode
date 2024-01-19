class Solution:
    def isFascinating(self, n: int) -> bool:
        num = str(n * 2) + str(n * 3) + str(n)
        if "0" in num:
            return False
        for i in range(1, 10):
            if num.count(str(i)) > 1:
                return False
        return True
        
1
