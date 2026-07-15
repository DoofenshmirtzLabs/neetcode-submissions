class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,temprature in enumerate(temperatures):
            while stack and temprature>stack[-1][0]:
                temp,index=stack.pop()
                res[index]=i-index
            stack.append((temprature,i))
        return res
        