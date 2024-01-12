class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l = len(num)
        for i in range(l-1, -1, -1):
            if num[i] != "0":
                break
        return num[:i+1]
 
        
"
