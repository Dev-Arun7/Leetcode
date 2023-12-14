class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        my_list = [num for num in nums if num != 0]
        my_list = sorted(set(my_list))
        return len(my_list)
[
