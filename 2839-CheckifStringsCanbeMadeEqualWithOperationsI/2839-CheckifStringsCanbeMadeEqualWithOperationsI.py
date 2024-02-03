        new1 += new[1]
        if new1 == s2:
            return True


        new = ''
        new += s1[0]
        new1 += new[2]
        new1 += new[0]
        new1 += new[3]
        new1 = ''
        if new == s2:
            return True
        new += s1[3]
        new += s1[0]
        new += s1[1]
        new += s1[2]
        new = ''
        if s1 == s2:
            return True
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
"
