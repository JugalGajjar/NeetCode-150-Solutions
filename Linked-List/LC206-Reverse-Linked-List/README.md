# 206. Reverse Linked List

**Difficulty:** Easy

## Problem
Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:** <br>
Input: head = [1,2,3,4,5] <br>
Output: [5,4,3,2,1]

**Example 2:** <br>
Input: head = [1,2] <br>
Output: [2,1]

**Example 3:** <br>
Input: head = [] <br>
Output: []

**Constraints:** <br>
The number of nodes in the list is the range `[0, 5000]`. <br>
-5000 <= Node.val <= 5000


## Solution

#### **Intuition:**
In a singly linked list, each node only holds a reference to the next node (`curr -> curr.next`). To reverse the list, we need to invert the direction of these pointers so that each node points backward to its predecessor (`curr.next = prev`).

A naive approach extracts all values into an auxiliary array/stack and rewrites them in reverse order, taking $O(n)$ extra space.

To achieve optimal $O(1)$ auxiliary space, we can reverse the pointers **in-place** using an **Iterative Two-Pointer** approach (`prev` and `curr`):
- If we immediately point `curr.next = prev`, we break the link to the remainder of the list and lose access to the remaining nodes.
- Therefore, before modifying `curr.next`, we temporarily store `next_temp = curr.next`.
- Once the pointer is reversed (`curr.next = prev`), we slide our two pointers forward: `prev` moves to `curr`, and `curr` moves to `next_temp`.
- When `curr` reaches `None`, `prev` will be pointing to the new head of the reversed list.

#### **Logic:**
1. Initialize Pointers:
   - `prev = None` (the original head will point to `None` as the new tail).
   - `curr = head` (starting node to process).
2. Iterate While `curr` is Not `None`:
   - Save Next Node: Store `next_temp = curr.next` so the rest of the list is preserved.
   - Reverse Link: Point `curr.next = prev`.
   - Advance Pointers:
     - Move `prev` forward to `curr`.
     - Move `curr` forward to `next_temp`.
3. Return Result: When `curr` becomes `None`, `prev` points to the new head of the reversed list. Return `prev`.

#### **Example Walkthrough:**
Consider Example 1: `head = [1, 2, 3, 4, 5]`

* **Initial State:** `prev = None`, `curr = Node(1)`

| Step | `curr` | `next_temp` (`curr.next`) | Pointer Modification (`curr.next = prev`) | `prev` Next (`prev = curr`) | `curr` Next (`curr = next_temp`) | Visual State of Reversed Sublist |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `1` | `2` | `1 -> None` | `1` | `2` | `1 -> None` |
| 2 | `2` | `3` | `2 -> 1` | `2` | `3` | `2 -> 1 -> None` |
| 3 | `3` | `4` | `3 -> 2` | `3` | `4` | `3 -> 2 -> 1 -> None` |
| 4 | `4` | `5` | `4 -> 3` | `4` | `5` | `4 -> 3 -> 2 -> 1 -> None` |
| 5 | `5` | `None` | `5 -> 4` | `5` | `None` | `5 -> 4 -> 3 -> 2 -> 1 -> None` |

* Loop terminates because `curr == None`.
* **Final Result:** Return `prev` (pointing to `5`). The reversed list is `5 -> 4 -> 3 -> 2 -> 1 -> None`.

#### **Time Complexity:**
$O(n)$ <br>
Single linear pass visiting each of the $n$ nodes exactly once.

#### **Space Complexity:**
$O(1)$ <br>
Pointers are updated in-place without allocating any extra nodes or data structures.