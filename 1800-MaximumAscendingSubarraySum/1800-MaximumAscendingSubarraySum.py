class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        if len(nums) > 0:
            res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += nums[i]
            else:

            temp = res
                res = max(res, temp)
                temp = nums[i]
        res = max(res, temp)
        return res
[
[10,20,30,5,10,50]
[10,20,30,40,50]
[12,17,15,13,10,11,12]
65
150
33
65
150
33
