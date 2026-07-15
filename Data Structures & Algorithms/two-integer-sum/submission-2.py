class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums):
            if num in seen:
                return [seen[num],index]
            result=target-num
            seen[result]=index
        

        