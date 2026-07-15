class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(current_step):

            if current_step==n:
                count[0]+=1
            
            if current_step>n:
                return
            
            dfs(current_step+1)
            dfs(current_step+2)
        
        count=[0]
        dfs(current_step=0)
        return count[0]
