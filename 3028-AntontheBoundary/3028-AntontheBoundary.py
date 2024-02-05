class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            ans += i
            if ans == 0:
                count += 1
        return count
        
[
