from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) # O(n)
        while low<=high:
            mid = low + (high-low)//2
            current = sum(map(lambda x: ceil(x / mid), piles))
            if current <= h:
                high = mid-1 
            elif current > h:
                low = mid+1
        return low
