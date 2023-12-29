class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        

        result =  " ".join(words[::-1])
        return result
        
"
