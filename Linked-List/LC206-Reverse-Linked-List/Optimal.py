# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # Preserve the next node
            curr.next = prev       # Reverse the current link
            prev = curr            # Move prev to current node
            curr = next_temp       # Advance current to next node

        return prev

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse each node once.
# Space Complexity: O(1), as we are using a constant amount of extra space for the pointers.