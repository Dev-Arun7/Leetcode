class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))  # Create a list with unique elements
        nums.clear()  # Clear the original list
        nums.extend(unique_nums)  # Add the unique elements back to the original list
        nums.sort()
        return len(nums)

[
