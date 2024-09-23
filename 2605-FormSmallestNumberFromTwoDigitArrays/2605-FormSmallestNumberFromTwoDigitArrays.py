class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = min(nums1)
        n2 = min(nums2)
        if n1 == n2:
            return n1
        if n1 < n2:
            return int(str(n1) + str(n2))
        else:
        n1_set = set(nums1)
        n2_set = set(nums2)
        common_num = n1_set & n2_set
        if common_num:
            return min(common_num)
            return int(str(n2) + str(n1))
[
[4,1,3]
[5,7]
[3,5,2,6]
[3,1,7]
15
3
15
3
