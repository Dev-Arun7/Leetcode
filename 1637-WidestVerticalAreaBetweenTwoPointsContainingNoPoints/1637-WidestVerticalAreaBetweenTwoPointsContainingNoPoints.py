class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        temp = 0
        l = len(points)
        sorted_array = sorted(points, key=lambda x: x[0])
        for i in range(1, l):
            temp = max(temp, sorted_array[i][0] - sorted_array[i-1][0])

        return temp
        
[
