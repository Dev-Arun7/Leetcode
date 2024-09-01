class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        waiting = []
        finished = 0
        for arival, time in customers:
            if arival >= finished:
                finished = arival + time
            else:
                finished = finished + time
                waiting.append(finished - arival)
                waiting.append(finished - arival)

        return (sum(waiting) / len(waiting))

[
[[1,2],[2,5],[4,3]]
[[5,2],[5,4],[10,3],[20,1]]
5.00000
3.25000
5.00000
3.25000
