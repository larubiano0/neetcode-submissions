class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = "".join([str(len(st)) + "#" + st for st in strs])
        return final_string

    def decode(self, s: str) -> List[str]:
        i = 0
        final_list = []
        n = ""
        while i < len(s):
            if s[i].isdigit():
                n += s[i]
                i += 1
            else:
                i+=1
                final_list.append(s[i:i+int(n)])
                i += int(n)
                n = ""
        return final_list
