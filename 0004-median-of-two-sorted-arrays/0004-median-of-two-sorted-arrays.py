class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        ans = sorted(nums1 + nums2)
        l = len(ans)
        if l % 2 == 0:
            n = (ans[(l//2) - 1] + ans[(l//2)]) / 2
        else:
            n = ans[l//2]
        return n
        

