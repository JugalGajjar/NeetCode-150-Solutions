# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        vals = []

        # 1. Collect values from list1
        curr = list1
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # 2. Collect values from list2
        curr = list2
        while curr:
            vals.append(curr.val)
            curr = curr.next

        if not vals:
            return None

        # 3. Sort all values
        vals.sort()

        # 4. Construct a new linked list
        dummy = ListNode()
        tail = dummy
        for v in vals:
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next

# Time Complexity: O(n log n), where n is the total number of nodes in both linked lists.
# We collect all values and sort them, which takes O(n log n) time.
# Space Complexity: O(n), as we are storing all values in a list and creating a new linked list with the same number of nodes.