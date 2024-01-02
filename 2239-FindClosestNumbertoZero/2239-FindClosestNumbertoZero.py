class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        temp = abs(nums[0] - 0)
        result = nums[0]
        for i, num in enumerate(nums):
            if abs(num - 0) <= temp:
                temp = min(abs(num - 0), temp)

                result = num
        return result
[
