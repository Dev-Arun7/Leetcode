class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums) + 1
        num_set = set(nums)
        for n in range(l):
            if n not in num_set:
                return n
        return -1
        
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
