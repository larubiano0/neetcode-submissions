class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]*len(nums)
        left = [1]*len(nums)
        i = 0
        while i<len(nums):
            if i>0:
                right[i]*=nums[i-1]*right[i-1]
                left[-(i+1)]*=nums[-(i+1)+1]*left[-(i+1)+1]
            i += 1
        
        return [r*l for r, l in zip(right, left)]
        