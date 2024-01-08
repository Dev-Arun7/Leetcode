class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return sum(1 for i in nums if i < target)
[
