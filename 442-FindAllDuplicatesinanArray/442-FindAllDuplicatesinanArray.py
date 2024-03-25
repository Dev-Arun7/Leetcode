class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        l = len(nums)
        i = 1
        while i < l:
            if sorted_nums[i] == sorted_nums[i-1]:

                ans.append(sorted_nums[i])
                i += 2
            else:
                i += 1
        return ans
        
[
