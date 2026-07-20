import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #lower bound 1 ,upper bound=max(piles)

        left,right=1,max(piles)
        bound=-1
        while left<=right:
            mid=left+(right-left)//2

            if self.can_eat(piles,mid,h):
                bound=mid
                right=mid-1
            
            else:
                left=mid+1
           
        return bound
    
    def can_eat(self,arr,rate,target):
        total=0
        for num in arr:
            total+=math.ceil(float(num)/rate)
     
        return True if total<=target else False
