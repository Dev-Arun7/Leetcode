class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i, word in enumerate(words):
        l = len(words)
            ref_set = set(word)
            for j in range( i+1, l):
                if ref_set == set(words[j]):
                    count += 1
        return count
        
[
