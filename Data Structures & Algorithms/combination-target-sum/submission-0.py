class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def combinations(start,current_list,current_sum):

            if current_sum==target:
                res.append(current_list[:])
            
            if current_sum>target:
                return 
            
            for current_idx in range(start,len(nums)):
                current_num=nums[current_idx]
                current_list.append(current_num)

                combinations(current_idx,current_list,current_sum+current_num)

                current_list.pop()
        
        res=[]
        combinations(start=0,current_list=[],current_sum=0)
        return res

