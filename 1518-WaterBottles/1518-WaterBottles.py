class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        temp = numBottles
        while temp >= numExchange:
            drinked += temp // numExchange
            temp = temp // numExchange

        return drinked
        remaining = 0
            temp += remaining
            remaining = temp % numExchange
        
9
