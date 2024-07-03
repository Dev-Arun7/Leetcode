class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hash_1 = {}
        hash_2 = {}
        for n in nums1:
            hash_1[n] = hash_1.get(n, 0) + 1

        
        for n in nums2:
            hash_2[n] = hash_2.get(n, 0) + 1

        for n in hash_1:
            temp = min(hash_1[n], hash_2.get(n, 0))
            if temp > 0:
                for i in range(temp):
                    result.append(n)

        return result
        
[
