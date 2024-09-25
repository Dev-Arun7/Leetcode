class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        l = len(nums) + 1
        for i in range(l):
            if i not in num_set:
                return i
        
[
[3,0,1]
[0,1]
[9,6,4,2,3,5,7,0,1]
2
2
8
2
2
8
