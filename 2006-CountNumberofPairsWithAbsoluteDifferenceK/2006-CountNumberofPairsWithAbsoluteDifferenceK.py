class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
        
[
