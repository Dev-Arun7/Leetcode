class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        i = 0
        while count != k:
            i += 1
            if i not in arr:
                count += 1
                if count  == k:
                    return i

[
