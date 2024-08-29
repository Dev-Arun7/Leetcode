            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for key in freq.keys():
            if freq[key] % 2 == 0:
                length += freq[key]
            else:
                if not odd:
                    length += freq[key]
                else:
                    length += freq[key] - 1
        
                    odd = True
        return length
        
"
"abccccdd"
"a"
7
1
7
1
