class Solution:
    def sortString(self, s: str) -> str:
        letter_set = set(s)
        freq = {}
        ans = ''
        for i in letter_set:
            freq[i] = s.count(i)
        while len(ans) != len(s):
            for i in ref:
        ref = 'abcdefghijklmnopqrstuvwxyz'
                if i in freq and freq[i] > 0:
                    ans += i
                    freq[i] -= 1
            for i in ref[::-1]:
                if i in freq and freq[i] > 0:
                    ans += i
                    freq[i] -= 1
        return ans
        
"
