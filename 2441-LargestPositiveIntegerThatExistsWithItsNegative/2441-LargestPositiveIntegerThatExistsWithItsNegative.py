class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if nums[i] + nums[j] == 0 and nums[i] > ans:
                    ans = nums[i]
        return ans
[
