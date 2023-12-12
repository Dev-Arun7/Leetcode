            if i not in temp:
                temp += i
            else:
                if len(temp) > len(max_str):
                    max_str = temp
                _index = temp.find(i)
                temp = temp[_index + 1::]
                temp += i
        if len(temp) > len(max_str):
        temp = ''
        for i in s:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str = ''
"
