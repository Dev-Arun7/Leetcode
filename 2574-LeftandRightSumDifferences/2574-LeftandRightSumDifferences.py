class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        right_sum = []
        result = []
        l = len(nums)
        for i in range(l):
            left_sum.append(sum(nums[:i]))
            right_sum.append(sum(nums[i+1:]))
        for i in range(l):
            result.append(abs(left_sum[i] - right_sum[i]))
        return result
        
[
