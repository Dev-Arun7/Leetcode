class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        l = len(nums2)
        for i in nums1:
            num_index = nums2.index(i)
            for j in range(num_index, l):
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result
        
[
