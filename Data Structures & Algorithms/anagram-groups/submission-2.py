from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        seen=defaultdict(list)
      
        #ill create an counter for each str in strs and if counters are same then ill group them

        for s in strs:
            counter=defaultdict(int)
            for ch in s:
                counter[ch]+=1
            counter_tuple=tuple(sorted(counter.items()))
            seen[counter_tuple].append(s)
        return list(seen.values())
