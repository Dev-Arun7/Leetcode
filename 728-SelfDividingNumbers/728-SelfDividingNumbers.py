class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            temp = str(i)
            for j in temp:
                if i % int(j) != 0:
                    break
            else:
                ans.append(i)
                
            if "0" in temp:
                continue
1
