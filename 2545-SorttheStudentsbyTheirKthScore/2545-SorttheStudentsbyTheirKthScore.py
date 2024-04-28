class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        l = len(score)

        for n in range(l-1):
            for j in range(n + 1, l):
                if score[n][k] < score[j][k]:
                    score[n], score[j] = score[j], score[n]
        return score
        
[
