class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        temp = ''
        for i in words:
            for j in i:
                if j == separator:
                    if temp:
                        result.append(temp)
                        temp = ""
                else:
                    temp += j
                
        return result

            if temp:
            ····result.append(temp)
················temp·=·""

        
[
