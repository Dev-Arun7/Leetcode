class Solution:
    def digitCount(self, num: str) -> bool:
        flag = True
        for i, digit in enumerate (num):
            if num.count(str(i)) == int(digit):
                continue
            else:
                return False
        return flag
        
"
