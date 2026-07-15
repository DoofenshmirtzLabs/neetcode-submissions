class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack=[]
        res=0

        for i in range(len(height)):
            while stack and height[i]>=height[stack[-1]]:
                mid_idx=stack.pop()
                mid=height[mid_idx]
                if stack:
                    l=height[stack[-1]]
                    r=height[i]
                    h=min(l,r)-mid
                    w=i-stack[-1]-1
                    res+=w*h

            stack.append(i)
        return res