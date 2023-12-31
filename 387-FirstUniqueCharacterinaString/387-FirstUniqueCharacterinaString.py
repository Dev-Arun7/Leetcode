class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, char in enumerate(s):
            if s.count(char) == 1:
                return i
        return -1
        
"
