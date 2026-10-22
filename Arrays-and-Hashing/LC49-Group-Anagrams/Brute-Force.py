from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())

# Time Complexity: O(n * k log k), where n is the number of strings in the input list and k is the maximum length of a string.
# Sorting each string takes O(k log k) time, and we do this for all n strings.
# Space Complexity: O(n * k)
# We store all the strings in the hash map, and the keys are the sorted strings, which can also take up to O(k) space each.