class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i != j and nums[i] + nums[j] == target:
                    count +=1
        return count
        
[
