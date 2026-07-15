from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        print(hashmap)

        for s in strs:
            sorteds="".join(sorted(s))
            hashmap[sorteds].append(s)
        
        return list(hashmap.values())