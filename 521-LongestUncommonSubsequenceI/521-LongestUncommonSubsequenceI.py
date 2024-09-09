class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If both strings are equal, return -1 (no uncommon subsequence exists)
        if a == b:
            return -1
        
        # If the strings are not equal, return the length of the longer string
        return max(len(a), len(b))
"
"aba"
"cdc"
"aaa"
"bbb"
"aaa"
"aaa"
"aefawfawfawfaw"
"aefawfeawfwafwaef"
3
3
-1
17
3
3
-1
17
