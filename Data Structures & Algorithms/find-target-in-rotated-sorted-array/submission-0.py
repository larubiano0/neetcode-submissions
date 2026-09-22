class Solution:
    def get_index_og(self, n, pivot, index):
        if n-pivot-index>0:
            return pivot+index
        else:
            return index-(n-pivot)
            

    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = low + (high-low)//2
            if nums[mid]>nums[high]:
                low = mid+1
            else:
                high = mid
        return low

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMin(nums) # [3,4,5,6,1,2] -> 4 -> [1,2] + [3,4,5,6] = nums[pivot:]+nums[:pivot]
        n = len(nums)
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[self.get_index_og(n, pivot, mid)] == target:
                return self.get_index_og(n, pivot, mid)
            elif nums[self.get_index_og(n, pivot, mid)] < target:
                low = mid+1
            else:
                high = mid-1
        return -1
        

        