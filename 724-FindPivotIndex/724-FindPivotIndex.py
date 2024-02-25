class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        _sum = 0
        l = len(nums)
        if len(nums) == 1:
            return 0

        else:
            for i in range(l):
                if i -1 > -1:
                    _sum += nums[i-1]
                else:
                    _sum += 0
                if _sum == total - (_sum + nums[i]):
                    return i
        return -1      
        
[
