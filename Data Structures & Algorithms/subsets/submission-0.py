class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None

        res=[]
        
        #size varies from 0 to n 
        #for each size find all the possbile combinations
        current_list=[]

        def dfs(idx):

            if idx>=len(nums):
                
                res.append(current_list.copy())
                return 
            
            current_list.append(nums[idx])
            dfs(idx+1)

            current_list.pop()
            dfs(idx+1)
        
        dfs(0)
        return res

