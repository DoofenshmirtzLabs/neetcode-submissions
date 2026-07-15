class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        #target-num:index
        for index,num in enumerate(nums):

            if num in seen:
                return [seen[num],index]
            key=target-num
            seen[key]=index
        
        
