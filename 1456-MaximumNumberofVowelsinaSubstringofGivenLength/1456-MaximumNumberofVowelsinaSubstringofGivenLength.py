                window_count += 1
            right += 1
        while right < l:
            if s[right] in vowels:
                window_count += 1
            if s[left] in vowels:
        max_count = window_count
        for i in range(k):
            if s[i] in vowels:
        l = len(s)
        left, right, max_count, window_count = 0, 0, 0, 0
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
class Solution:
                window_count -= 1
            left += 1
"
