class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid)
        while grid:
            temp = 0
            for i in grid:
                max_value = max(i)
                i.remove(max_value)
                temp = max(temp, max_value)
            ans += temp
        return ans
            if not any(grid):
                break
        
[
