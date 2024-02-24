class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        temp = -1
        words = s.split()
        for word in words:
            if word.isdigit():
                if int(word) > temp:
                    temp = int(word)
                else:
                    return False
        return True
        
"
