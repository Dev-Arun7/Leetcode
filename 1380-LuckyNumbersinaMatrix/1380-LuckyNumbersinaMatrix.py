    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        lis = []
        for i in range(m):
            min_row = min(matrix[i])
            col_max = matrix[i].index(min_row)
            max_col = max(matrix[j][col_max] for j in range(m))
            if min_row == max_col:
                lis.append(min_row)
        return lis        
        
               
        
class Solution:
[[3,7,8],[9,11,13],[15,16,17]]
