class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref_word = strs[0]
        l = len(ref_word)

        for word in strs:
            if len(word) < l:
                ref_word = word
                l = len(word)  

        result = ""
        for i in range(l):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    return result
            result += temp
        return result

        
["flower","flow","flight"]
