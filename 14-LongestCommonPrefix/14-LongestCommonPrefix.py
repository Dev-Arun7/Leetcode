class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(l):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:

                    return result
            result -= temp
        return result
        ref_word = strs[0]
        for word in strs:
            if len(word) < l:

        l = len(ref_word)

                ref_word = word
                l = len(word)  
        
[
["flower","flow","flight"]
["dog","racecar","car"]
["ab", "a"]
"fl"
""
"a"
"fl"
""
"a"
