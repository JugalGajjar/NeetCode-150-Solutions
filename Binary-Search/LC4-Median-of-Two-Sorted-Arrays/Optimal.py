class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure A is the smaller array to minimize binary search range
        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A)

        while True:
            i = (left + right) // 2  # Cut in A
            j = half - i             # Cut in B

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            # Correct partition found
            if A_left <= B_right and B_left <= A_right:
                # Odd total length: right partition has the extra median element
                if total % 2 == 1:
                    return float(min(A_right, B_right))
                
                # Even total length: average of largest left and smallest right
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1

# Time Complexity: O(log(min(m, n))) where m and n are the lengths of the two arrays.
# This is because we perform a binary search on the smaller array.
# Space Complexity: O(1) since we are using a constant amount of extra space regardless of the input size.