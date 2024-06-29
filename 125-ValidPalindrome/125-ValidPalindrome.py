class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for chr in s:
            if chr.isalnum():
                temp += chr
        return temp == temp[::-1]
        temp = temp.lower()
        
"
