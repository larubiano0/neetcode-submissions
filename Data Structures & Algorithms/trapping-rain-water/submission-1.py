class Solution:
    def trap(self, height: List[int]) -> int:
        highest_to_left = [0]
        highest_to_right = [0]
        for i in range(1, len(height)):
            highest_to_left.append(max(height[i-1], highest_to_left[-1]))
            highest_to_right.append(max(height[-i], highest_to_right[-1]))
        waters = []
        for i in range(len(height)):
            possible_w = min(highest_to_left[i], highest_to_right[-(i+1)])-height[i]
            if possible_w > 0:
                waters.append(possible_w)
        return sum(waters)
