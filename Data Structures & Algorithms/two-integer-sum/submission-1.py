class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return []
        hash_map={}
        result=[]
        for i in range(len(nums)):
            num=nums[i]
            if num in hash_map:
                result.append(hash_map[num])
                result.append(i)


            temp=target-num
            hash_map[temp]=i
        return result

        