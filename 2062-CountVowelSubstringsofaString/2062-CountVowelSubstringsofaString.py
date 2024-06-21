class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ref = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        l = len(word)
        
        # Sliding window to check for vowel substrings
        for start in range(l):
            temp = set()
            for end in range(start, l):
                if word[end] in ref:
                    temp.add(word[end])
                    if len(temp) == 5:
                        count += 1
                else:
                    break  # Stop as soon as a non-vowel character is found
                
        return count

"
