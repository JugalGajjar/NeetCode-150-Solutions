# 21. Merge Two Sorted Lists

**Difficulty:** Easy

## Problem
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:** <br>
Input: list1 = [1,2,4], list2 = [1,3,4] <br>
Output: [1,1,2,3,4,4]

**Example 2:** <br>
Input: list1 = [], list2 = [] <br>
Output: []

**Example 3:** <br>
Input: list1 = [], list2 = [0] <br>
Output: [0]

**Constraints:** <br>
The number of nodes in both lists is in the range `[0, 50]`. <br>
-100 <= Node.val <= 100 <br>
Both `list1` and `list2` are sorted in non-decreasing order.


## Solution

#### **Intuition:**
A brute-force solution extracts all elements into an array, sorts the array, and reconstructs a brand-new linked list, taking $O((n + m) \log(n + m))$ time and $O(n + m)$ extra memory.

However, both input linked lists are **already sorted in non-decreasing order**. This allows us to use an **Iterative Two-Pointer (Merge)** technique:
- By comparing the current nodes of both lists (`list1.val` vs `list2.val`), the smaller (or equal) value is always guaranteed to be the next element in the final sorted list.
- We splice the existing nodes directly by rearranging pointers in-place, without allocating new list nodes.
- Using a **dummy head node** (`dummy = ListNode()`) simplifies edge cases by giving us a fixed reference to the start of the merged list, eliminating separate conditional branches for setting the initial head.
- Once either list is exhausted, the remaining non-empty list is already fully sorted and can be linked directly to the end of our merged list in $O(1)$ time.

#### **Logic:**
1. Initialize Sentinel Node & Tail Pointer:
   - Create `dummy = ListNode()` to serve as a pre-head anchor.
   - Set `tail = dummy` to keep track of the last node in the merged list.
2. Iterate While Both Lists are Non-Empty (`while list1 and list2`):
   - Compare Values:
     - If `list1.val <= list2.val`: attach `list1` to `tail.next` and advance `list1 = list1.next`.
     - Else (`list2.val < list1.val`): attach `list2` to `tail.next` and advance `list2 = list2.next`.
   - Advance Tail: Move `tail = tail.next`.
3. Attach Remainder:
   - At least one list will become `None`. Connect the remaining elements of the non-empty list directly: `tail.next = list1 if list1 else list2`.
4. Return Result: Return `dummy.next` (the head of the newly merged list).

#### **Example Walkthrough:**
Consider Example 1: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`

* **Initial State:** `dummy = ListNode(0)`, `tail = dummy`

| Step | `list1` Head | `list2` Head | Comparison (`list1.val vs list2.val`) | Node Attached (`tail.next`) | Advanced Pointer | Merged Chain (`dummy -> ...`) |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `1` | `1` | `1 <= 1` | `1` (from `list1`) | `list1` moves to `2` | `dummy -> 1` |
| 2 | `2` | `1` | `2 > 1` | `1` (from `list2`) | `list2` moves to `3` | `dummy -> 1 -> 1` |
| 3 | `2` | `3` | `2 <= 3` | `2` (from `list1`) | `list1` moves to `4` | `dummy -> 1 -> 1 -> 2` |
| 4 | `4` | `3` | `4 > 3` | `3` (from `list2`) | `list2` moves to `4` | `dummy -> 1 -> 1 -> 2 -> 3` |
| 5 | `4` | `4` | `4 <= 4` | `4` (from `list1`) | `list1` moves to `None` | `dummy -> 1 -> 1 -> 2 -> 3 -> 4` |

* **Loop Ends:** `list1` is now `None`.
* **Attach Remainder:** `tail.next = list2` (attaches the remaining `[4]`).
* **Final Result:** `dummy.next` points to `1 -> 1 -> 2 -> 3 -> 4 -> 4`.

#### **Time Complexity:**
$O(n + m)$ <br>
Where $n$ and $m$ are the lengths of `list1` and `list2`. Each loop iteration processes one node from either list in $O(1)$ time, taking at most $n + m$ steps total.

#### **Space Complexity:**
$O(1)$ <br>
Only pointers (`dummy`, `tail`) are created; existing list nodes are spliced together in-place without additional allocations.