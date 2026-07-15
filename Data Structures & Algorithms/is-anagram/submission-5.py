from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        counter1,counter2=Counter(s),Counter(t)
        if counter1==counter2:
            return True
        return False

