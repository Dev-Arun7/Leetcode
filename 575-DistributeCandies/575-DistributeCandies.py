class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = len(set(candyType))
        half = len(candyType) // 2
        return half if types > half else types
        
[
