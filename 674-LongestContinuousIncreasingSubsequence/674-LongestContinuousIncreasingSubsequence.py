class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        left = 0
        l = len(nums)
        for i in range(1, l):
            if nums[i] <= nums[i - 1]:
                left = i
            else:
                result = max(result, (i - left + 1))
        return result
        
[
