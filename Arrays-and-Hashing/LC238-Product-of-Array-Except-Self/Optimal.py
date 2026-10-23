class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # Pass 1: Compute prefix products directly in `answer`
        # answer[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: Multiply by suffix products from the right
        # postfix tracks the running product of elements to the right of i
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

# Time Complexity: O(n)
# We have two separate loops, each iterating through the array of length n.
# Space Complexity: O(1) - excluding the output array.