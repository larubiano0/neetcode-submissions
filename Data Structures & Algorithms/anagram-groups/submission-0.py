class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_list = []
        for string in strs:
            hashmap = {}
            for c in string:
                if c not in hashmap:
                    hashmap[c] = 1
                else:
                    hashmap[c] += 1
            hashmap_list.append(hashmap)

        words_groups = []
        hashmap_groups = []
        
        for i in range(len(hashmap_list)):
            for j in range(len(words_groups)):
                if hashmap_groups[j][0] == hashmap_list[i]:
                    hashmap_groups[j].append(hashmap_list[i])
                    words_groups[j].append(strs[i])
                    break
            else:
                hashmap_groups.append([hashmap_list[i]])
                words_groups.append([strs[i]])
        return words_groups
                
            
