class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        brought = prices[0]
        for i in prices:
            if i <= brought:
                brought = i
            else:
                profit += i - brought
        return profit
                
                brought = i

[
