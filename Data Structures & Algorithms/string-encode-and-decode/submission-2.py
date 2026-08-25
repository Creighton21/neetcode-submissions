class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "/" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            slash_index = s.find("/", i)
            length = int(s[i:slash_index])
            i = slash_index + 1
            decoded_strs.append(s[i:i+length])
            i += length

        return decoded_strs