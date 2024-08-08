class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l = len(s1)
        length = 0
        for i in range(l):
            if len(s2) <= i  or s2[i] != s1[i]:
                break
            if len(s3) <= i  or s3[i] != s1[i]:
                break
            length += 1
        if length == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - 3 * length
        
"
"abc"
"abb"
"ab"
"dac"
"bac"
"cac"
"cc"
"cccb"
"c"
2
-1
4
2
-1
4
