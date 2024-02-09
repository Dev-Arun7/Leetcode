class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                            ans =  nums[i] + nums[j] + nums[k]
        return ans
        ans = -1
                        if ans == -1:
                        else:
                            ans = min(ans, nums[i] + nums[j] + nums[k] )
[
