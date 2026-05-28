# LeetCode #121 - Best Time to Buy and Sell Stock  
# Difficulty: Easy | Beats: 46%
# Pattern: Sliding Window | Time: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
