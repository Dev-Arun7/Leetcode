class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 9:
            return n
        elif len(word) < 17:
            return 8 + (2 * (n - 8))
        elif len(word) < 25:
            return 24 + (3 * (n - 16))
        else:
            return 48 + (4* (n-24))
        n = len(word)
        
"
