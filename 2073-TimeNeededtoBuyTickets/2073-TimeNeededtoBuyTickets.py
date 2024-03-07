        for i in range(n):
            if i < k:
                res += min(tickets[i], tickets[k])  # for all pos before k it will exhaust all tickets or get till number till kth place
                
            elif i > k:
                res += min(tickets[i], tickets[k]-1) #for all pos after k it can exhaust all tickets or get 1 less than the kth gets finished
                
        return res
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        res = tickets[k] #it has to buy all at kth position
        
class Solution:
[
