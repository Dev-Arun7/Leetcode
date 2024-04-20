class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = float('inf')
        singles = {'b':0, 'a':0, 'n':0}
        doubles = {'l':0, 'o':0}
        for i in text:
            if i in singles:
                singles[i] += 1
            elif i in doubles:
                doubles[i] += 1
        for i in singles:
            count = min(count, singles[i])
        for i in doubles:
            temp = doubles[i] // 2
            count = min(temp, count)



"
