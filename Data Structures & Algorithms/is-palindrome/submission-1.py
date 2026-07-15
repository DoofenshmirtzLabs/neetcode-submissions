class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        
        temp=""
        for char in s:
            if char.isalnum():
                temp+=char.lower()

        end=len(temp)-1
        print(temp)

        while start<end:
            if  temp[start]!=temp[end]:
               return False
            start+=1
            end-=1
        return True 
        