                result.append([nums1[c1][0], (nums1[c1][1] + nums2[c2][1])])
                c1 += 1
                c2 += 1
            elif nums1[c1][0] < nums2[c2][0]:
                result.append([nums1[c1][0], nums1[c1][1]])
                c1 += 1
            else:
                result.append([nums2[c2][0], nums2[c2][1]])
                c2 += 1
        while c1 < len(nums1):
            result.append([nums1[c1][0], nums1[c1][1]])

            c1 += 1
        
        while c2 < len(nums2):
            result.append([nums2[c2][0], nums2[c2][1]])
            c2 += 1
            if nums1[c1][0] == nums2[c2][0]:
        while c1 < len(nums1) and c2 < len(nums2):
        result = []
        c1 = 0
        c2 = 0
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
class Solution:

        return result
        
[
