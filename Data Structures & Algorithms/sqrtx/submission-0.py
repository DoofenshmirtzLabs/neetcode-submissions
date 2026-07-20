class Solution:
    def mySqrt(self, x: int) -> int:
        #bs on answers 1 to n max,

        left,right=1,x
        res=0

        while left<=right:

            mid=(left+right)//2

            temp=mid*mid

            if temp==x:
                return mid
            elif temp>x:
                right=mid-1
            else:
                #possible answer look right for closed value
                res=mid
                left=mid+1
        return res