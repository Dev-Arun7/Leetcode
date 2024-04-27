class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = float('-inf')
        left = 0
        right = l - 1
        while left < (l // 2):
            max_sum = max(max_sum, (nums[left] + nums[right]))
            left += 1
            right -= 1

        l = len(nums)
        return max_sum
[
