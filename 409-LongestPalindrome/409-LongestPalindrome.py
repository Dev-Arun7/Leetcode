class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_set = set()
        my_list = []
        even = 0
        odd = 0
        for i in s:
            my_set.add(i)
            my_list.append(i)
        for i in my_set:
            temp = my_list.count(i)
            if temp % 2 == 0:
                even += temp
            else:
                even += temp
                even -= 1
                if temp > odd:
                    odd = temp
        if odd:
            even += 1
        return even
        
"abccccdd"
