class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[0]*numRows
        for i in range(numRows):
            l[i]=[0]*(i+1)
            l[i][0]=1
            l[i][i]=1
            for j in range(1,i):
                l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l
5
