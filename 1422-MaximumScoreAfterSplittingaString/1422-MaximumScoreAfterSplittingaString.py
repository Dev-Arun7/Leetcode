class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        zeros = 0
        ones = s.count('1')
        l = len(s)
        temp = ''
        for i in range(l-1):
            temp += s[i]
            zeros = temp.count('0')
            if zeros + ones - (len(temp) - zeros) > score:
                score = zeros + ones - (len(temp) - zeros)
        return score
        
"
