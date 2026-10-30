# 981. Time Based Key-Value Store

**Difficulty:** Medium

## Problem
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
* `TimeMap()` Initializes the object of the data structure.
* `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
* `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

**Example 1:** <br>
Input: <br>
["TimeMap", "set", "get", "get", "set", "get", "get"] <br>
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]] <br>

Output: <br>
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation: <br>
TimeMap timeMap = new TimeMap(); <br>
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1. <br>
timeMap.get("foo", 1);         // return "bar" <br>
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar". <br>
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4. <br>
timeMap.get("foo", 4);         // return "bar2" <br>
timeMap.get("foo", 5);         // return "bar2"

Constraints: <br>
1 <= key.length, value.length <= 100 <br>
`key` and `value` consist of lowercase English letters and digits. <br>
1 <= timestamp <= 10^7 <br>
All the timestamps `timestamp` of `set` are strictly increasing. <br>
At most `2 * 10^5` calls will be made to `set` and `get`.


## Solution

#### **Intuition:**
We need a data structure that associates each `key` with multiple `(timestamp, value)` entries and retrieves the value with the largest timestamp less than or equal to a target query `timestamp`.

A hash map mapping each `key` to an array of `(timestamp, value)` pairs is a natural fit. For the `get` operation, linearly scanning backward through the array takes $O(m)$ time per call (where $m$ is the number of entries for that key). With up to $2 \times 10^5$ calls, linear searches can degrade overall performance.

Crucially, the problem specifies that **all timestamps in** `set` **calls arrive in strictly increasing order**. This guarantee means the list of pairs for each key is naturally sorted by timestamp. 

Because the entries are sorted, we can replace the linear scan with **Binary Search**:
- If `history[mid].timestamp <= timestamp`: this entry is valid, so we record it as our candidate answer and search the right half (`left = mid + 1`) to check if a larger valid timestamp exists.
- If `history[mid].timestamp > timestamp`: this entry is too recent, so we search the left half (`right = mid - 1`).

This allows each `get` operation to run in $O(\log m)$ logarithmic time.

#### **Logic:**
1. Data Structure (`__init__`):
   - Initialize a hash map `store = {}` mapping `key -> list of (timestamp, value)` pairs.
2. Insertion (`set`):
   - If `key` is not in `store`, initialize an empty list for it: `store[key] = []`.
   - Append `(timestamp, value)` to `store[key]`. Since timestamps arrive strictly in ascending order, the list remains sorted.
3. Lookup (`get`):
   - If `key` does not exist in `store`, return `""`.
   - Let `history = store[key]`. Set pointers `left = 0`, `right = len(history) - 1`, and `res = ""`.
   - Binary Search Loop (`while left <= right`):
     - Compute midpoint: `mid = left + (right - left) // 2`.
     - If `history[mid][0] <= timestamp`:
       - Record `res = history[mid][1]` (potential answer).
       - Try to find a larger timestamp: `left = mid + 1`.
     - Otherwise (`history[mid][0] > timestamp`):
       - Search earlier timestamps: `right = mid - 1`.
   - Return `res`.

#### **Example Walkthrough:**
Consider operations on key `"foo"`:
- `set("foo", "bar", 1)` $\rightarrow$ `store["foo"] = [(1, "bar")]`
- `set("foo", "bar2", 4)` $\rightarrow$ `store["foo"] = [(1, "bar"), (4, "bar2")]`

Now, trace `get("foo", 3)`:
* Target `timestamp = 3`, `history = [(1, "bar"), (4, "bar2")]`
* `left = 0`, `right = 1`, `res = ""`

| Iteration | `left` | `right` | `mid` | `history[mid]` | Condition (`mid_time <= 3`) | Action | Next Range |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | `0` | `1` | **`0`** | `(1, "bar")` | $1 \le 3$ (True) | `res = "bar"`, search right $\rightarrow$ `left = mid + 1 = 1` | `[1 ... 1]` |
| 2 | `1` | `1` | **`1`** | `(4, "bar2")` | $4 \le 3$ (False) | Search left $\rightarrow$ `right = mid - 1 = 0` | Empty |

* Loop terminates because `left (1) > right (0)`.
* **Output:** `"bar"`

Trace `get("foo", 5)`:
* Target `timestamp = 5`, `history = [(1, "bar"), (4, "bar2")]`
* `left = 0`, `right = 1`, `res = ""`

| Iteration | `left` | `right` | `mid` | `history[mid]` | Condition (`mid_time <= 5`) | Action | Next Range |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | `0` | `1` | **`0`** | `(1, "bar")` | $1 \le 5$ (True) | `res = "bar"`, search right $\rightarrow$ `left = 1` | `[1 ... 1]` |
| 2 | `1` | `1` | **`1`** | `(4, "bar2")` | $4 \le 5$ (True) | `res = "bar2"`, search right $\rightarrow$ `left = 2` | Empty |

* Loop terminates because `left (2) > right (1)`.
* **Output:** `"bar2"`

#### **Time Complexity:**
`set(key, value, timestamp)`: <br>
$O(1)$ amortized time to append the entry to the list in the hash map.

`get(key, timestamp)`: <br>
$O(\log m)$ where $m$ is the total number of timestamps recorded for that specific key.

#### **Space Complexity:**
$O(N)$, where $N$ is the total number of set calls, storing all key, timestamp, and value entries across the hash map.