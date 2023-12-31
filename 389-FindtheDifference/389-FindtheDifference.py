class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = set(s)
        t_set = set(t)
        for i in t_set:
            if t.count(i) > s.count(i):
                return i
        return ""

        
"
