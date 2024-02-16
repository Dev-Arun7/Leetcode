class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)
        for i in range(l):
            for j in range(i, l):
        return ans
        
       
                    ans = max(temp, ans)
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    temp = nums[i] ^ nums[j]
        
[
