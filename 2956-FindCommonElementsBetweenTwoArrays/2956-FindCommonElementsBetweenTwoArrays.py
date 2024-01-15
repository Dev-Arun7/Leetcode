class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1 = count_2 = 0
        set_1 = set(nums1)
        set_2 = set(nums2)
        count_1 = sum(1 for i in nums1 if i in set_2)
        count_2 = sum(1 for i in nums2 if i in set_1)
        return [count_1, count_2]
        
[
