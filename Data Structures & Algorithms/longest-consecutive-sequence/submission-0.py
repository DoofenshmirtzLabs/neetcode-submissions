class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_set=set(nums)
        max_count=float("-inf")
        for num in range(len(nums)):
            current_count=0
            if nums[num]-1 in hash_set:
                current_count=1
                max_count=max(max_count,current_count)
            else:
                while nums[num]+1 in hash_set:
                    current_count+=1
                    nums[num]+=1
                max_count=max(max_count,current_count)
        return max_count+1