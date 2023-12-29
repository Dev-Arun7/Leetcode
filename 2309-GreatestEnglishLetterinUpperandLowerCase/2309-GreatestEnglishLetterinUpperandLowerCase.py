        lowers = []
        for i in s:
            if i.isupper():
                capitals.append(i)
            else:
                lowers.append(i)
        capitals.sort()
        for i in reversed(capitals):
        result = ''
            if i.lower() in lowers:
                result = i
                break
        return result
        capitals = []
class Solution:
    def greatestLetter(self, s: str) -> str:
"
