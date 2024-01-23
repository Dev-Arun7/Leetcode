class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        for i, ch in enumerate(operations):
            if ch == 'C':
                score.pop()
            elif ch == 'D':
            elif ch == '+':
                score.append((score[-1]) + (score[-2]))
            else:
                score.append(int(ch))
        return sum(score)
                score.append((score[-1]) * 2)
        

[
