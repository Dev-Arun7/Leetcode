class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_set = set()
        l = len(pattern)
        for i in range(l):
            letter = pattern[i]
            for j in range(i, l):
                
        words = s.split()

                if pattern[j] == letter:
            word = words[i]
                    if words[j] != word:
                        return False
                elif pattern[j] != letter:
                    if words[j] == word:
                        return False
        return True
        l2 = len(words)
        if l != l2:
            return False
        
"
