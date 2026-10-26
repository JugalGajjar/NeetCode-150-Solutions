# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy

## Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:** <br>
Input: prices = [7,1,5,3,6,4] <br>
Output: 5

Explanation: <br>
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:** <br>
Input: prices = [7,6,4,3,1] <br>
Output: 0

Explanation: <br>
In this case, no transactions are done and the max profit = 0.

**Constraints:** <br>
1 <= prices.length <= 10^5 <br>
0 <= prices[i] <= 10^4


## Solution

#### **Intuition:**
To maximize profit from a single transaction, we want to buy at the lowest possible price and sell at the highest possible price *after* that buying day.

A brute-force solution checks every possible buy-and-sell day pair in $O(n^2)$ time. However, notice that if we decide to sell on day `i`, our profit is maximized by having bought at the minimum price seen anywhere between day `0` and day `i - 1`. 

Instead of looking forward at all future days, we can traverse the list linearly from left to right while keeping track of the minimum buying price seen so far (`min_price`). At each day, we calculate the potential profit if we sold today (`price - min_price`) and update our overall `max_profit`. This allows us to find the optimal transaction in a single linear pass ($O(n)$) without extra memory.

#### **Logic:**
1. Initialize State:
   - `min_price = float('inf')` to track the lowest stock price encountered so far.
   - `max_profit = 0` to record the highest profit found.
2. One-Pass Traversal: Iterate through each `price` in `prices`:
   - If `price < min_price`: Update `min_price = price`. A cheaper buy day has been found, which could yield higher profits for future selling days.
   - Otherwise: Calculate profit if selling today (`price - min_price`) and update `max_profit = max(max_profit, price - min_price)`.
3. Return Result: Return `max_profit`.

#### **Example Walkthrough:**
Consider Example 1: `prices = [7, 1, 5, 3, 6, 4]`

* **Initial State:** `min_price = ∞`, `max_profit = 0`

| Day (`i`) | `price` | `price < min_price`? | Updated `min_price` | Potential Profit (`price - min_price`) | Updated `max_profit` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | `7` | `7 < ∞` (Yes) | `7` | — | `0` |
| 1 | `1` | `1 < 7` (Yes) | `1` | — | `0` |
| 2 | `5` | `5 < 1` (No) | `1` | $5 - 1 = 4$ | $\max(0, 4) =$ **`4`** |
| 3 | `3` | `3 < 1` (No) | `1` | $3 - 1 = 2$ | $\max(4, 2) =$ **`4`** |
| 4 | `6` | `6 < 1` (No) | `1` | $6 - 1 = 5$ | $\max(4, 5) =$ **`5`** |
| 5 | `4` | `4 < 1` (No) | `1` | $4 - 1 = 3$ | $\max(5, 3) =$ **`5`** |

* **Final Result:** `5`

#### **Time Complexity:**
$O(n)$ <br>
Single linear pass through the array of length $n$.

#### **Space Complexity:**
$O(1)$ <br>
Constant auxiliary space as two scalar variables (`min_price` and `max_profit`) are maintained.