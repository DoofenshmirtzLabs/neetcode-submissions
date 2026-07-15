class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_window_sum=0
        min_window_len=float('inf')
        start=0
        for end in range(len(nums)):
            current_window_sum+=nums[end]
            while current_window_sum>=target:
                min_window_len=min(min_window_len,(end-start)+1)
                current_window_sum-=nums[start]
                start+=1
        return min_window_len if min_window_len!=float('inf') else 0