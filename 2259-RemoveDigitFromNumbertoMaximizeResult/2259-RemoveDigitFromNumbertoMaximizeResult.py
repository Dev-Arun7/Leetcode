class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        out = float('-inf')
        l = len(number)
        for i in range(l):
            if number[i] == digit:
                temp = int(number[:i] + number[i+1:])
                out = max(out, temp)
        
        return str(out)
"
"123"
"3"
"1231"
"1"
"551"
"5"
"12"
"231"
"51"
"12"
"231"
"51"
