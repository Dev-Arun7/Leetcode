class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = [words[i+2] for i in range(len(words)-2) if words[i] == first and words[i+1] == second]
        return result

"
