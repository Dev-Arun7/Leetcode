class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                for j in range(i, -1, -1):
        
                    if s[j] != ' ':

        count = 0
                        count += 1
                    else:
                        return count
                    

        
                return count
        
"
