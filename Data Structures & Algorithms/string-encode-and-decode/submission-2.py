class Solution:

    def encode(self, strs: List[str]) -> str:

        final = ""

        for string in strs:
            final = final + str(len(string)) + "#" + string

        return final

    def decode(self, s: str) -> List[str]:

        final = []

        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            final.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return final
            