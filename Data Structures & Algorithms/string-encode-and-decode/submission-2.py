class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        while s != "":
            pos = s.find("#")
            n = int(s[:pos])
            decoded_str = s[pos + 1 : pos + n + 1]
            decoded_list.append(decoded_str)
            s = s[pos + n + 1:]
        return decoded_list