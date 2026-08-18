class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        print(hashmap)
        top = []
        i = 0
        while hashmap and k>0:
            current_highest = 0
            current_highest_num = -1001
            for key, val in hashmap.items():
                if val > current_highest:
                    current_highest = val
                    current_highest_num = key
            k -= 1
            hashmap.pop(current_highest_num)
            top.append(current_highest_num)
        
        return top
        
