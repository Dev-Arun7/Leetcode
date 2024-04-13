class Solution:
    def reverseVowels(self, s: str) -> str:
        ref_stack = []
        ref_set = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


        for letter in s:
            if letter in ref_set:
                ref_stack.append(letter)
    
        for letter in s:
        result = ''
            if letter in ref_dict:
        ref_dict = {}
                ref_dict[letter] = 1
                result += ref_stack.pop()
            else:
                result += letter

        return result
        
"
