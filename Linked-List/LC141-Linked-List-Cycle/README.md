# 141. Linked List Cycle

**Difficulty:** Easy

## Problem
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that** `pos` **is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:** <br>
Input: head = [3,2,0,-4], pos = 1 <br>
Output: true

Explanation: <br>
There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:** <br>
Input: head = [1,2], pos = 0 <br>
Output: true

Explanation: <br>
There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:** <br>
Input: head = [1], pos = -1 <br>
Output: false

Explanation: <br>
There is no cycle in the linked list.

**Constraints:** <br>
The number of the nodes in the list is in the range `[0, 104]`. <br>
-10^5 <= Node.val <= 10^5 <br>
`pos` is -1 or a **valid index** in the linked-list.


## Solution

#### **Intuition:**
A straightforward approach stores every visited node's reference in a hash set. If we encounter a node already in the set, a cycle exists. However, this requires $O(n)$ extra memory.

To solve this in optimal $O(1)$ auxiliary space, we use **Floyd's Cycle-Finding Algorithm** (the Fast and Slow Pointers or "Tortoise and Hare" technique):
- Imagine two runners on a track: runner A moves at $1$ step per turn (`slow`), while runner B moves at $2$ steps per turn (`fast`).
- If the track is a straight line ending at `None` (acyclic), the faster runner will simply reach the end first.
- If the track contains a loop (cyclic), both runners will eventually enter the loop. Inside a closed loop, the faster runner gains on the slower runner by exactly $1$ node per step (relative velocity of $2 - 1 = 1$). 
- Because the distance between them shrinks by $1$ each iteration, the faster runner is mathematically guaranteed to catch up to and collide with the slower runner (`slow == fast`) without infinitely looping past them.

#### **Logic:**
1. Initialize Pointers:
   - Set both `slow = head` and `fast = head`.
2. Traverse the List (`while fast and fast.next`):
   - Check `fast` and `fast.next` to safely advance `fast` by two steps without triggering a `NoneType` attribute error.
   - Advance `slow` by $1$ node: `slow = slow.next`.
   - Advance `fast` by $2$ nodes: `fast = fast.next.next`.
   - Check Collision: If `slow == fast`, both pointers reference the exact same node in memory, confirming a cycle exists. Return `True`.
3. No Cycle: If `fast` or `fast.next` reaches `None`, the end of the list has been reached. Return `False`.

#### **Example Walkthrough:**
Consider Example 1: `head = [3, 2, 0, -4]`, tail `-4` points back to `Node(2)` (`pos = 1`).

* Structure: `3 -> 2 -> 0 -> -4 -> 2 (cycle)`
* Initial state: `slow = Node(3)`, `fast = Node(3)`

| Step | `slow` (moves 1) | `fast` (moves 2) | `slow == fast`? | Visual State |
| :---: | :---: | :---: | :---: | :--- |
| 0 | `Node(3)` | `Node(3)` | Initial | Both start at head |
| 1 | `Node(2)` | `Node(0)` | No | `fast` moves past `2` to `0` |
| 2 | `Node(0)` | `Node(2)` | No | `fast` moves past `-4` back to `2` |
| 3 | `Node(-4)` | `Node(-4)` | **Yes** | `fast` catches `slow` at `Node(-4)` |

* Pointers meet at `Node(-4)`.
* **Final Result:** `True`

Consider Example 3: `head = [1]`, `pos = -1` (no cycle)
* Initial state: `slow = Node(1)`, `fast = Node(1)`
* Loop condition checks: `fast.next` is `None`.
* Loop terminates immediately.
* **Final Result:** `False`

#### **Time Complexity:**
$O(n)$ <br>
If there is no cycle, `fast `reaches the end in at most $n/2$ steps. If there is a cycle of length $C$ with a non-cyclic prefix of length $K$, `slow` enters the cycle after $K$ steps, and `fast` catches `slow` within at most $C$ additional steps ($K + C = n$).

#### **Space Complexity:**
$O(1)$ <br>
Only two pointer references (`slow` and `fast`) are maintained.