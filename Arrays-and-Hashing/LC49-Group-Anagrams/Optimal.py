from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as the dictionary key
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

# Time Complexity: O(n * k), where n is the number of strings in the input list and k is the maximum length of a string.
# We traverse each string and count the frequency of each character, which takes O(k) time. We do this for all n strings.
# Space Complexity: O(n * k)
# We store all the strings in the hash map, and the keys are the character count tuples, which can take up to O(k) space each.