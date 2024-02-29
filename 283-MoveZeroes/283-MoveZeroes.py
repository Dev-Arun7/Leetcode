class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeros.append(nums.pop(i))
            else:
                i += 1
        nums.extend(zeros)

[
