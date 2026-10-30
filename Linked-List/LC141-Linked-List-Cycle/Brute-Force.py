# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False

# Time Complexity: O(n)
# In the worst case, we may need to traverse the entire linked list to determine if there is a cycle.
# We are using a set to keep track of the visited nodes, and checking for membership in a set takes O(1) time on average.
# Space Complexity: O(n)
# We are using a set to store the visited nodes, which can potentially store all the nodes in the linked list in the worst case.