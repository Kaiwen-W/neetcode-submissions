class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through array
        # if reach buying price, e.g. prices[r] < prices[l] 
        # change l to r 

        l, r = 0, 0
        max_profit = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, (prices[r] - prices[l]))
        
        return max_profit