class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        sentence = set(sentence)
        return len(sentence) == 26
        
"
