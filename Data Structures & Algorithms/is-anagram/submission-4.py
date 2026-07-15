from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        counter_s,counter_t=defaultdict(int),defaultdict(int)

        for char in s:
            counter_s[char]+=1
        
        for char in t:
            counter_t[char]+=1
        return counter_s==counter_t
