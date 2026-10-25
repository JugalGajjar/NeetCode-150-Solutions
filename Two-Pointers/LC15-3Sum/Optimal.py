class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # If the current element is greater than 0, three positive numbers cannot sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

# Time Complexity: O(n^2), where n is the length of the nums list.
# We have one loop iterating through the list and a two-pointer approach inside it, which takes linear time.
# Space Complexity: O(m), where m is the number of unique triplets found.
# We use a list to store unique triplets, which can take up space proportional to the number of unique triplets.