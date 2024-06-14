class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        temp_list = set()
        for i in range(1,n):
            if '0' not in str(i) and '0' not in str(n-i):
        
                return [i, n-i]
        
2
