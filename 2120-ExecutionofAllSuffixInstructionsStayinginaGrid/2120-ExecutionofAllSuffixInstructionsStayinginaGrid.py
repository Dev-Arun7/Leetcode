                        count += 1
                    else:
                        break
                elif s[j] == 'L':
                    pos[1] -= 1
                    if pos[1] >= 0:
                        count += 1
                    else:
                        break
                elif s[j] == 'U':
                    pos[0] -= 1
                    if pos[0] >= 0:
                        count += 1
                    else:
                if s[j] == 'R':
                    pos[1] += 1
                    if pos[1] < n:
        l = len(s)
        for i in range(l):
            count = 0
            pos = startPos.copy()
            for j in range(i, l):
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
3
