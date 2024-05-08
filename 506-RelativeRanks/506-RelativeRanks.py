class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]: 
        s=[]
        l=score.copy()
        l.sort(reverse=True)
        for i in range(len(l)):
            if score[i]==l[0]:
                s.append("Gold Medal")
            elif score[i]==l[1]:
                s.append("Silver Medal")
            elif score[i]==l[2]:
                s.append("Bronze Medal")
            else:
                s.append(str((l.index(score[i]))+1))
        return s  
[5,4,3,2,1]
