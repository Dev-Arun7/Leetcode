class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list=s.split()
        return len(word_list[-1])
        