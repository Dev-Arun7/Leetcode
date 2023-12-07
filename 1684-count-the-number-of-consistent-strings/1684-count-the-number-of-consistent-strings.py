class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            status = True
            for i in word:
                if i not in allowed:
                    status = False
                    break
            if status:
                count += 1
        return count
        