class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = []

        for i in range(n - k + 1):
            window_max = nums[i]
            for j in range(i, i + k):
                window_max = max(window_max, nums[j])
            
            res.append(window_max)

        return res

# Time Complexity: O(n * k), where n is the length of the nums list and k is the size of the sliding window.
# We traverse the list once and for each window, we find the maximum by iterating through the k elements.
# Space Complexity: O(1), excluding the space used for the result list.