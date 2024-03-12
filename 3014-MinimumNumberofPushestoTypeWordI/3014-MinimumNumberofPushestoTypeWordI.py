class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 9:
            return len(word)
        elif len(word) < 17:
            return 8 + (2 * (len(word) - 8))
        elif len(word) < 25:
            return 24 + (3 * (len(word) - 16))
        else:
            return 48 + (4*(len(word)-24))
        
"
