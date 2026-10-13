class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []

        for string in strs:
            parts.append(str(len(string)))
            parts.append("–")
            parts.append(string)

        return "".join(parts)

    def decode(self, encoded: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(encoded):
            # Find the separator after the length
            j = encoded.find("–", i)

            length = int(encoded[i:j])
            start = j + 1
            end = start + length

            decoded.append(encoded[start:end])
            i = end

        return decoded
