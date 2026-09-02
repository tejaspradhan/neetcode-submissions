class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded+=s
            encoded+='°'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split('°')
        return decoded[:-1]