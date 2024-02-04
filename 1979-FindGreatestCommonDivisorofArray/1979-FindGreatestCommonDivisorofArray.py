class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)
        for i in range(small,-1,-1):
            
        l = len(nums)
            if small % i == 0 and big % i == 0:
                return i
        
[
