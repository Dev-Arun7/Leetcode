class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            temp = bin(i)
            result.append(str(temp).count('1'))
        return result
        
2
