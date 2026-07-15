class Solution:
    def isPalindrome(self, s: str) -> bool:

       
     
        temp=""
        s=s.lower()
        for char in s:
            if char.isalnum():
                temp+=char
        print(temp)
        left,right=0,len(temp)-1
        while left<right:
                if temp[left]!=temp[right]:
                    return False
                left+=1
                right-=1
        
        return True