class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = len(arr1)
        for n1 in arr1:
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    count -= 1
                    break
        return count
        
[
