class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# Time Complexity: O(n), where n is the length of the prices list.
# We traverse the list once, keeping track of the minimum price and maximum profit.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the minimum price and maximum profit.