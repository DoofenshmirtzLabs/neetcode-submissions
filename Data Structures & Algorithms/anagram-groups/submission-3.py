from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)==1 or len(strs)==0:
            return [strs]
        
        table=defaultdict(list)

        res=[]

        for s in strs:
            temp="".join(sorted(s))
            table[temp].append(s)
        for values in table.values():
            res.append(values)
        
        return res
        
