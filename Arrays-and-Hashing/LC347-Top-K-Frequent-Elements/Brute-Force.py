from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Min-heap stores tuples of (frequency, num)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]

# Time Complexity: O(n log k), where n is the length of the input list.
# We traverse the list containing n elements to count frequencies and then maintain a heap of size k, which takes O(log k) time for each insertion.
# Space Complexity: O(n), where n is the length of the input list.
# We store the frequency counts in a hash map and the heap can take up to O(k) space, but in the worst case, we may store all unique elements in the hash map, which can take up to O(n) space.