class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s-k) in prefix_map:
                res += prefix_map[s-k]
            
            if s in prefix_map:
                prefix_map[s] += 1
            else:
                prefix_map[s] = 1
        return res