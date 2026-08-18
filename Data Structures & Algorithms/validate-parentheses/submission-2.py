class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {"(", "{", "["}
        c = {")": "(", "}":"{", "]":"["}
        for i in s:
            if i in o:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack[-1] == c[i]:
                    stack.pop()
                else:
                    return False
        return (stack == [])
            