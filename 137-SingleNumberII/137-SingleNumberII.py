class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(num for num in nums if nums.count(num) != 3)
        
[
