class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            for i in word:
                if word.count(i) > chars.count(i):
                    break
        return count
            else:
                count += len(word)
            temp = 0
        
[
