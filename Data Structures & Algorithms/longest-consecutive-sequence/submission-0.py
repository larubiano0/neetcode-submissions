class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited = set()
        highest = 0
        for i in nums:
            if i in visited:
                continue
            else:
                visited.add(i)
                current = i
                current_length = 1
                while current+1 in nums_set:
                    current_length += 1
                    current = current + 1
                    visited.add(current)
                if current_length > highest:
                    highest = current_length

        return highest