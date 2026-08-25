class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        if n == 1:
            return True
        while True:
            s = 0
            n_str_rev = str(n)[::-1]
            for i in n_str_rev:
                s+=int(i)**2
            if s == 1:
                return True
            if s in visited:
                return False
            visited.add(s)
            n = s
        return False
