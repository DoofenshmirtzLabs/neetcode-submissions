class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        def combinations(start,current_list,size):

            if size<=target_size:
                temp_list=tuple(sorted(current_list))
                if temp_list not in memo:
                    memo.add(temp_list)
                    res.append(current_list.copy())

            if size>target_size:
                return 
            
            for idx in range(start,target_size):
                current_num=nums[idx]

                current_list.append(current_num)

                combinations(idx+1,current_list,size+1)

                current_list.pop()
        
        res=[]
        memo=set()
        target_size=len(nums)
        combinations(0,[],0)

        return res

