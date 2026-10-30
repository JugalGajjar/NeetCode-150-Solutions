class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # Scan backwards for the latest timestamp <= target timestamp
        history = self.store[key]
        for t, val in reversed(history):
            if t <= timestamp:
                return val

        return ""

# set() Time Complexity: O(1) - Appending to the list is O(1) on average.
# get() Time Complexity: O(n) - In the worst case, we may need to scan through all the timestamps for a given key.
# Space Complexity: O(n) - Storing all the key-value pairs with their timestamps.