class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for n in range(len(nums) + 1):
            if n not in nums:
                return n

        
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
