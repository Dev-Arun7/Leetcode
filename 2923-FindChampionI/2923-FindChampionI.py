class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        index = 0
        value = 0
        for i, element in enumerate(grid):
        return index
            temp = sum(element)
            if temp > value:
                value = temp
                index = i
        
[
