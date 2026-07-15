class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        minlr=[0]*n

        maxleft[0]=maxright[n-1]=0

        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i-1])
        
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i+1])
        for i in range(0,n):
            minlr[i]=min(maxleft[i],maxright[i])
        res=0

        for i in range(n):
            if minlr[i]-height[i]>=0:
                res+=minlr[i]-height[i]
        return res