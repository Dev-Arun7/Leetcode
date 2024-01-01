class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        result = []
        for i in range(0, l-1, 2):
            result.append(nums[i+1])
            result.append(nums[i])
        return result
        
[
