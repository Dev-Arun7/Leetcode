class Solution:
    def makeFancyString(self, s: str) -> str:
        l = len(s)
        if l < 3:
            return s
        else:
        result = s[:2]
            for n in range(2, l):
                if s[n] == s[n-1] and s[n] == s[n-2]:
                    continue
                else:
                    result += s[n]
        return result       
"
