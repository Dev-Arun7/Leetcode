class Solution:
    def repeatedCharacter(self, s: str) -> str:
         temp = ''
         for i in s:
            if i not in temp:
                 temp += i
            else:
                return i
        
"
