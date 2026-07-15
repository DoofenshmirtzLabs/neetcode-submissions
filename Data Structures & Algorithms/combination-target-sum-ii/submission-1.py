class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #have to track solutions to make sure only unqiue once are inserted,use memo to track solutions for an given number in array
        def combinations(start,current_list,current_sum):

            if current_sum==target:
                temp_list=tuple(sorted(current_list))
                if temp_list not in memo:
                    
                    memo[temp_list]=1
                    res.append(current_list.copy())
            
            if current_sum>target:
                return
            
            for current_idx in range(start,len(candidates)):
                current_num=candidates[current_idx]

                current_list.append(current_num)

                combinations(current_idx+1,current_list,current_sum+current_num)

                current_list.pop()
        
        res=[]
        memo={}
        combinations(0,current_list=[],current_sum=0)

        return res
