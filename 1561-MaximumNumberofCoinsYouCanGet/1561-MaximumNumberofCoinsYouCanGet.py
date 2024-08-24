class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        l = len(piles)
        l = (l/3) * 2
        total = 0
        i = 1
        while i < l:
            total += piles[i]
            i += 2
        return total
        
[
[2,4,1,2,7,8]
[2,4,5]
[9,8,7,6,5,1,2,3,4]
9
4
18
9
4
18
