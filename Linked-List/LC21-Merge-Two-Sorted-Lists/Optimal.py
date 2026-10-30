# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining portion of whichever list is non-empty
        tail.next = list1 if list1 else list2

        return dummy.next

# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
# We traverse each list once.
# Space Complexity: O(1), as we are using a constant amount of extra space for the dummy node and tail pointer, and we are modifying the existing nodes rather than creating new ones.