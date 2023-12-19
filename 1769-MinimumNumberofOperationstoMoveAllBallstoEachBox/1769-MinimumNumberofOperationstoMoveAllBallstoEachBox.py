class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        result = []
        temp = 0
        for i, num in enumerate(boxes):
            temp = 0
            for j, j_num in enumerate(boxes):
                if j_num == str(1):
                    temp += abs(i-j)
            result.append(temp)
        return result
"
