class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m = prices[0]
        max_profit = 0
        for x in prices:
            if x < m:
                m = x
            else:
                if x - m > max_profit:
                    max_profit = x - m
        return max_profit
