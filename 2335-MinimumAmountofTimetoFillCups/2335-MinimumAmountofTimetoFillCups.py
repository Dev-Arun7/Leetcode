class Solution:
    def fillCups(self, amount: list[int]) -> int:
        result = 0
        amount.sort(reverse = True)
        while(amount[0] and amount[1]):
            result += 1
            amount[0] -= 1

        
            amount[1] -= 1
        if amount[0]:
            result += amount[0]
        return result
            amount.sort(reverse = True)

[
[1,4,2]
[5,4,4]
[5,0,0]
4
7
5
4
7
5
