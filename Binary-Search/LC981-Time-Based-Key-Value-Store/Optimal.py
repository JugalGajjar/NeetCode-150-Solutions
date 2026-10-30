class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        history = self.store[key]
        left, right = 0, len(history) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            if history[mid][0] <= timestamp:
                res = history[mid][1]  # Candidate found, try to find a larger timestamp
                left = mid + 1
            else:
                right = mid - 1

        return res

# set() Time Complexity: O(1) - Appending to the list is O(1) on average.
# get() Time Complexity: O(log n) - Binary search on the list of timestamps for the given key.
# Space Complexity: O(n) - Storing all the key-value pairs with their timestamps.