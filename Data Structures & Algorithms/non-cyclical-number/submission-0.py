class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        seen=set()

        while n!=1:
            digits=[int(digit)**2 for digit in str(n)]
            n=sum(digits)
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
        
        