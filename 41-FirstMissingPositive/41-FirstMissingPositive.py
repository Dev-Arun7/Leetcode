class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_num = max(nums)
        for i in range(1,max_num+2):
            if i not in my_set:
                return i
        return 1
            
        
[
