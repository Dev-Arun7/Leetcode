class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_num = max(candies)
        for i in candies:
            if i + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result
        
[
