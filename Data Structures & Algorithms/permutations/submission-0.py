class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permutations(current_list,current_size):

            if current_size==target_size:

                res.append(current_list.copy())
            
            if current_size>target_size:
                return 
            

            for current_idx in range(len(nums)):
                current_num =nums[current_idx]

                if current_num not in current_list:
                    current_list.append(current_num)
                    permutations(current_list,current_size+1)
                    current_list.pop()
        res=[]
        target_size=len(nums)
        permutations(current_list=[],current_size=0)
        return res