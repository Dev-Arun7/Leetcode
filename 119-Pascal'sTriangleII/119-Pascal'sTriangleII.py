class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        for i in range(rowIndex+1):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res[rowIndex]
3
