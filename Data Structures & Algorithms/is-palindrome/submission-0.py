class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for i in range(len(s)):
            if s[i].isalnum():
                temp+=s[i]
        start=0
        end=len(temp)-1
        while start<end:
            left=temp[start].lower()
            right=temp[end].lower()
            if left!=right:
                return False
            start+=1
            end-=1
        return True
        