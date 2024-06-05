class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for w in words:
            curr_count = Counter(w)
            for c in count:
                count[c] = min(count[c], curr_count[c])
        res = []
        for c in count:
            for i in range(count[c]):
                res.append(c)
        return res
                
[
