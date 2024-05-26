class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ""
        for i in range(len(s)):
            result += s[indices.index(i)]
        return result

"
