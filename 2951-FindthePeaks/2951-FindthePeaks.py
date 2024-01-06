class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        l = len(mountain)
        result = [i for i in range(1,l-1) if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]]
        return result
[
