class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit

# Time Complexity: O(n^2), where n is the length of the prices list.
# We have two nested loops, each iterating through the list of prices.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the maximum profit and indices.