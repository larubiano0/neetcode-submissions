class TimeMap:

    def __init__(self):
        self.key_values = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_values:
            self.key_values[key] = []

        self.key_values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_values:
            return ""

        low = 0
        high = len(self.key_values[key]) - 1
        result = ""

        while low <= high:
            mid = low + (high - low) // 2

            if self.key_values[key][mid][1] <= timestamp:
                result = self.key_values[key][mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return result

