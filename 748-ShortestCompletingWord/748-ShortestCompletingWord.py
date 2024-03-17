        length = float('inf')

        for word in words:
            for char in plate:
                if word.count(char) < plate[char]:
                    break
        selected = ''
        
            else:
                if len(word) < length:
                    length = len(word)
                    selected = word
                    plate[i.lower()] += 1

        return selected

        
"
