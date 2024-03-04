            if word[0] in vowels:
                ans += word + 'ma' + (i+1) * 'a'
            else:
                ans += word[1:] + word[0] + 'ma' + (i+1) * 'a'

        vowels = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word_list = sentence.split()
        for i, word in enumerate(word_list):
            if i != 0:
                ans += ' '
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = ''
        return ans        
"
