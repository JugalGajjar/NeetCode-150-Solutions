class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2

            # Calculate total hours needed at eating speed `mid`
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                res = mid
                right = mid - 1  # Try to find a slower valid speed
            else:
                left = mid + 1   # Speed too slow, must eat faster

        return res

# Time Complexity: O(n * log m), where n is the number of piles and m is the maximum number of bananas in a pile.
# We perform a binary search on the range of possible eating speeds (from 1 to max(piles)), and for each speed, we iterate through all piles to calculate the total hours needed to finish eating all the bananas.
# Space Complexity: O(1)
# We use constant extra space, as we only store a few variables for the binary search and total hours calculation.