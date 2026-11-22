class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ""

        for string in strs:
            res += (str(len(string)) + "#" + string)
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            print("j: ", j)

            res.append(s[j+1: j+1+length])

            i = j + 1 + length

            print("i: ", i)
        return res
