class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = ''
        move = -1
        s_copy = [i for i in s if i.isalpha()]
        for i in s:
            if i.isalpha():
                ans += s_copy.pop()
            else:
                ans += i
        
        return ans
        
"
