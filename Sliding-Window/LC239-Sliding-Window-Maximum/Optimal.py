from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Stores indices
        res = []

        for i, num in enumerate(nums):
            # Remove indices that fall outside the current window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Maintain monotonic decreasing order: remove smaller elements from back
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(i)

            # Append the current window's maximum once the first window is complete
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

# Time Complexity: O(n), where n is the length of the nums list.
# Each element is added and removed from the deque at most once, leading to linear time complexity.
# Space Complexity: O(k), where k is the size of the sliding window.