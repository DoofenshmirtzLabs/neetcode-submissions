class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        x2=x
        if n>1:
            while n>1:
                x2=x2*x
                n-=1
            return x2
        else:
            x2=1/x
            n*=-1
            while n>1:
                x2=x2/x
                n-=1
            return x2