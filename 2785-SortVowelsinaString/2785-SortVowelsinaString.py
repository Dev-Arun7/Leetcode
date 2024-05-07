class Solution:
    def sortVowels(self, s: str) -> str:
        ref_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels = []
        ans = ""
        for letter in s:
            if letter in ref_set:
                vowels.append(letter)

        vowels.sort(reverse=True)

        for letter in s:
            if letter in ref_set:
                ans += vowels.pop()
            else:
                ans += letter

        return ans

"
