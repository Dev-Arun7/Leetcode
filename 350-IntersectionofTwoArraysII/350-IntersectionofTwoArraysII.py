
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        result = []
        
        for n in nums2:
            if count[n] > 0:
                result.append(n)
                count[n] -= 1
        
        return result
[
