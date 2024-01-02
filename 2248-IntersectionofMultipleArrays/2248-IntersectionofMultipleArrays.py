class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ref_set = set(nums[0])
        result = []
        for i in nums:
            ref_set = ref_set.intersection(set(i))
        if ref_set:
            result = list(ref_set)
        return result
            result.sort()
        
[
