class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_set = set(nums)
        l = len(nums)
        for i in my_set:
            if nums.count(i) > l//2:
                return i

[
