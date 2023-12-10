class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        temp = 0
        for i in nums:
            temp += i
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
        return abs(element_sum - digit_sum)
[
