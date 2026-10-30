# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        # 1. Collect all node values
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # 2. Overwrite node values in reverse order
        curr = head
        while curr:
            curr.val = vals.pop()
            curr = curr.next

        return head

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse each node twice: once to collect values and once to overwrite them.
# Space Complexity: O(n), as we are using extra space to store the node values in a list.