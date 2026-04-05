class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)
        return max_profit
            