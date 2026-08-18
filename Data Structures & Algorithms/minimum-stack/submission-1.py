class MinStack:

    def __init__(self):
        self.stack = []
        self.freq = {}
        self.min_lookup = {}
        self.minim = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1

        if (val < self.minim):
            self.min_lookup[val] = self.minim
            self.minim = val

    def pop(self) -> None:
        val = self.stack.pop()
        if self.freq[val] == 1:
            if val == self.minim:
                self.minim = self.min_lookup.pop(val)
            self.freq.pop(val)
        else:
            self.freq[val] -=1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minim
        
