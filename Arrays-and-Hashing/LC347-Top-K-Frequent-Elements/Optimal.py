from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Buckets where index represents frequency (0 to len(nums))
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        # Traverse buckets in descending order of frequency
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k:
                    return res
                
        return res

# Time Complexity: O(n), where n is the length of the input list.
# We traverse the list containing n elements to count frequencies and then traverse the buckets to collect the top k frequent elements.
# Space Complexity: O(n), where n is the length of the input list.
# We store the frequency counts in a hash map and the buckets can take up to O(n) space in the worst case.