class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for i in words:
                if word in i and word != i:
                    result.append(word)
                    break
        return result
        
[
