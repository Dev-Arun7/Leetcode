class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        l = len(nums)
        for i in range(l//2):
            temp = str(nums[i]) + str(nums[l-1-i])
            result += int(temp)
        return result
        if l % 2 == 1:
            result += nums[l//2]
        
[
