class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        # Two-pointer merge
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        total_len = m + n
        mid = total_len // 2

        if total_len % 2 == 1:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0

# Time Complexity: O(m + n) where m and n are the lengths of the two arrays.
# This is because we are merging the two arrays into one sorted array.
# Space Complexity: O(m + n) since we are storing the merged array which contains all elements from both input arrays.