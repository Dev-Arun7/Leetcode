class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [i ** 2 for i in nums]
        return result
        result.sort()
        
[
