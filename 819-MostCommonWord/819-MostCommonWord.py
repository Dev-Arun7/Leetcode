        count_ = 0
        result = ''
        for char in paragraph:
            if char.isalpha():
                temp += char.lower()
            else:
                if temp in bannedSet:
                    temp = ''
                else:
                    if len(temp) > 0:
                        words.append(temp)
                    temp = ''
        words.append(temp)
        
        for word in words:
            if word in hashMap:
                hashMap[word] += 1
            else:
                hashMap[word] = 1
                
        for word in hashMap:
            if hashMap[word] > count_:
                count_ = hashMap[word]
                result = word
        return result
        

"
"Bob hit a ball, the hit BALL flew far after it was hit."
["hit"]
"a."
[]
"Bob"
[]
"Bob. hIt, baLl"
["bob", "hit"]
"ball"
"a"
"bob"
"ball"
"ball"
"a"
"bob"
"ball"
