class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        sub_array = []
        sorted_array = sorted(nums, reverse = True)
        sub_array_total = 0
        for num in sorted_array:
            sub_array.append(num)
            sub_array_total += num
            total -= num
            if sub_array_total > total:
                return sub_array
        
[
