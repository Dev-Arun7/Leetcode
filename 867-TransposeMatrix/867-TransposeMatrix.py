class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        temp = []
        nos = len(matrix[0])
        elements = len(matrix)
        for i in range(nos):
            while j < elements:
                temp.append(matrix[j][i])
                j += 1
            result.append(temp)
            temp = []
        return result
            j = 0
[
