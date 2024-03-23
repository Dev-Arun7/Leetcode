class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ref_set = set()
        for i in nums:
            if i in ref_set:
                return i
            else:
                ref_set.add(i)
        
[
