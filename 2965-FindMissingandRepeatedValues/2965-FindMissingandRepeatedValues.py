        a = 0
        b = 0

        # Flatten the 2D grid using list comprehension
        flattened_grid = [element for row in grid for element in row]

        for i in range(1, len(flattened_grid) + 1):
            if i not in flattened_grid:
                b = i
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ref = []
            if flattened_grid.count(i) > 1:
                a = i
class Solution:

from typing import List
[
