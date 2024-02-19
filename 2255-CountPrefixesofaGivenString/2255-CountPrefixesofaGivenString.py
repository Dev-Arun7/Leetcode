class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        for i in words:
            l = len(i)
            if i == s[:l]:
                count += 1
        count = 0
        return count
        
[
