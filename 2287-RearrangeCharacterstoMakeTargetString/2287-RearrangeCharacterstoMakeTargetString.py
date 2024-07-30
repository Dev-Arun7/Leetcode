        letterCount = {}
        for c in target:
            if c in letterCount:
                letterCount[c] += 1
            else:
                letterCount[c] = 1
        frequency = {}
        for char in s:
            if char in letterCount:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
        for n in frequency:

        

    def rearrangeCharacters(self, s: str, target: str) -> int:
class Solution:
            
        result = float('inf')

            result = min((frequency[n] // letterCount[n]), result)
        return result
        if len(frequency) != len(letterCount):
            return 0
"
"ilovecodingonleetcode"
"code"
"abcba"
"abc"
"abbaccaddaeea"
"aaaaa"
"abc"
"abcd"
2
1
1
0
2
1
1
0
