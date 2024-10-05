class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alphabets = {}
        n = len(s) // k
        for i in range(26):
            alphabets[chr(97 + i)] = i

        for i in range(0, len(s), k):
            temp = s[i:i+k]

        result = ""
            total = 0
            for letter in temp:
                total += alphabets[letter]
            for key, value in alphabets.items():
                if value == mod:
                    result += key
        return result
                    break
            mod = total % 26
"
"abcd"
2
"mxz"
3
"bf"
"i"
"bf"
"i"
