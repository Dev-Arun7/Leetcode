class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # flattening the list items
        letters = ''.join(words)
        l = len(words)
        #Finding the fequency of letters from flattern string
        counts = Counter(letters)
        for count in counts.values():
            if count % l != 0:
                return False
        return True

[
