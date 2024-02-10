class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        min_len = min(len(word1), len(word2))
        for  i in range(min_len):
            ans += word1[i]
            ans += word2[i]
        if len(word1) > min_len:
            ans += word1[min_len:]
        else:
            ans += word2[min_len:]
        return ans

"
