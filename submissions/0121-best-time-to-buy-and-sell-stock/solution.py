class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # you only want to sell if there is a price higher then what you buy for that you can sell
        buy = prices[0] # imagine you buy on the first day
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
    
