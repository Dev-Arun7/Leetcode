class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) > 2:
                return False
        else:
            return True
        
[
