class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            
            answer[i] = product

        return answer

# Time Complexity: O(n^2)
# We have two nested loops, each iterating through the array of length n.
# Space Complexity: O(1) - excluding the output array.