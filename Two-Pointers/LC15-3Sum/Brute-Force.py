class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Sort triplet to ensure duplicates can be filtered by the set
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)

        return [list(t) for t in res]

# Time Complexity: O(n^3), where n is the length of the nums list.
# We have three nested loops, each iterating through the list.
# Space Complexity: O(m), where m is the number of unique triplets found.
# We use a set to store unique triplets, which can take up space proportional to the number of unique triplets.