class Solution:
    def create_letter_dict(self,s:str)->dict:
        seen={}
        for letter in s:
            if letter in seen:
                seen[letter]+=1
            else:
                seen[letter]=1
        return seen
            

    def isAnagram(self, s: str, t: str) -> bool:
        return self.create_letter_dict(s)==self.create_letter_dict(t)
        