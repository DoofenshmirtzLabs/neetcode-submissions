class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False
        hash_map={}
        for char in t:
            hash_map[char]=hash_map.get(char,0)+1
        
        for char in s:
            if char in hash_map:
                hash_map[char]=hash_map.get(char)-1
                current_value=hash_map.get(char)
                if current_value==0:
                    del hash_map[char]
            else:
                return False
        return True
        