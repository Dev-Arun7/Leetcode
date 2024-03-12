class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i%2 == 1:
                if count > 0:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 1
            else:
                count = 0
        return False
        
[
