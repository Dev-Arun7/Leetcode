class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        cash = sorted(costs)
        for c in cash:
            if c <= coins:
                total += 1
                coins -= c
            else:
                return total
        return total
[
[1,3,2,4,1]
7
[10,6,8,7,7,8]
5
[1,6,3,1,2,5]
20
4
0
6
4
0
6
