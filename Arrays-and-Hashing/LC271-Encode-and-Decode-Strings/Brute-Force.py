class Codec:
    def encode(self, strs: list[str]) -> str:
        # Delimiter-based joining
        return "\0".join(strs)

    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        return s.split("\0")

# Encode
# Time Complexity: O(n), where n is the total number of characters in all strings combined
# We traverse each character in the input list of strings once to encode them.
# Space Complexity: O(n), where n is the total number of characters in all strings combined

# Decode
# Time Complexity: O(n), where n is the total number of characters in the encoded string
# We traverse each character in the encoded string once to decode it.
# Space Complexity: O(m), where m is the number of strings in the decoded list.