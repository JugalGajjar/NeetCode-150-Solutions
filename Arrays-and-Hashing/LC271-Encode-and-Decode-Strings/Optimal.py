class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        n = len(s)

        while i < n:
            # Find the delimiter '#' separating length and content
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            # Extract exactly 'length' characters after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move pointer to the start of the next length prefix
            i = end

        return res

# Encode
# Time Complexity: O(n), where n is the total number of characters in all strings combined.
# We traverse each character in the input list of strings once to encode them.
# Space Complexity: O(n), where n is the total number of characters in all strings combined.

# Decode
# Time Complexity: O(n), where n is the total number of characters in the encoded string.
# We traverse each character in the encoded string once to decode it.
# Space Complexity: O(m), where m is the number of strings in the decoded list.