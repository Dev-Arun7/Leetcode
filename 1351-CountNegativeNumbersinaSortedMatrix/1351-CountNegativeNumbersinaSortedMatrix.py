class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            count += sum(1 for j in i if j<0)
        return count
        
[
