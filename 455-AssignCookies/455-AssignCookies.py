class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in g:
            for j in s:
                if j >= i:
                    count += 1
                    s.remove(j)
        return count
                    break

[
