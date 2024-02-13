            time = abs(letters[i] - letters[current])
            total += min(time, 26 - time) + 1
            current = i
            
        
        return total

     

        for i in word:
            letters[chr(ord('a')+ i)] = i + 1
        time = 0

        for i in range(26):
        total = 0
        letters = {}
        current = 'a'
class Solution:
    def minTimeToType(self, word: str) -> int:
"
