class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for i, num in enumerate(heights) if num != expected[i])
        
[
