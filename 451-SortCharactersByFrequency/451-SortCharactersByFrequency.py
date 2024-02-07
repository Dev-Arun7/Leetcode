class Solution:
    def frequencySort(self, s: str) -> str:
        my_set = set(s)
        freq = {}
        for i in my_set:
            freq[i] = s.count(i)
        sorted_dict = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        

        ans = ''

        for letter, count in sorted_dict:
            ans += letter * count
        
        return ans
        
"
