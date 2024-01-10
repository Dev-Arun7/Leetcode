class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        _max = 0
        start = False
        zeros = 0
        ones = 0
        for i in s:
            if i == "0":
                if start == False:
                    zeros = 0
                    start = True
                    zeros += 1
                else:
                    zeros += 1
            else:
                if start == True:
                    start = False
                    ones += 1
                    
                    if ones <= zeros:
                        _max = max(_max, ones)
                else:
                    ones += 1
                    if ones <= zeros:
                        _max = max(_max, ones)

        return 2 * _max
                    ones = 0
       
"
