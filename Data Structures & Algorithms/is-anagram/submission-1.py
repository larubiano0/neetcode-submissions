class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for j in t:
            if j not in hashmap:
                return False
            else:
                if hashmap[j] == 1:
                    hashmap.pop(j)
                else:
                    hashmap[j] -= 1  

        if not hashmap:
            return True
        else:
            return False       