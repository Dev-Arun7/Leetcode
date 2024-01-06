class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)
        for i in nums:
            if i != small:
                if i != big:
                    return i
        return -1
        
[
