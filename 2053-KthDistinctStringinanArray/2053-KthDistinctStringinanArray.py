class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        for i in arr:
            if arr.count(i) == 1:
                count += 1
                if count == k:
                    return i
        return ""
        
[
