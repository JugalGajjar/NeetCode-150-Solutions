import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_speed = max(piles)

        for k in range(1, max_speed + 1):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)

            if total_hours <= h:
                return k

        return max_speed

# Time Complexity: O(n * m), where n is the number of piles and m is the maximum number of bananas in a pile.
# In the worst case, we may need to check all possible eating speeds from 1 to the maximum number of bananas in a pile, and for each speed, we iterate through all piles to calculate the total hours needed to finish eating all the bananas.
# Space Complexity: O(1)