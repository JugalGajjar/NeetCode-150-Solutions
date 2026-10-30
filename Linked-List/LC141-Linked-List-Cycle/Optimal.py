# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Time Complexity: O(n)
# In the worst case, we may need to traverse the entire linked list to determine if there is a cycle. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# Space Complexity: O(1)
# We are using only a constant amount of extra space.