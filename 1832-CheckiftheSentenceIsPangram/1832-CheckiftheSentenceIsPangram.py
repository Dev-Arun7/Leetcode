class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(string.ascii_lowercase)
        for i in letters:
            if i not in sentence_set:
                return False
        sentence_set = set(sentence)
        return True
        
"
