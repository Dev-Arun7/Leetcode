class Solution:
    def partitionString(self, s: str) -> int:
        temp = set()
        left, right = 0, 0
        l =  len(s)
        while left < l and right < l:
            if s[right] in temp:
                left = right
                temp.add(s[right])
                right += 1
        count = 0
            else:
                temp.add(s[right])
                count += 1
                temp.clear()
                right += 1
        if len(temp) > 0:
            count += 1
        return count

"
