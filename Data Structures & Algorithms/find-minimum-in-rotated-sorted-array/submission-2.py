class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        global_min=float('inf')

        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2

            #figure out which side is sorted

            if nums[left]<=nums[mid]:
                #left side is sorted
                global_min=min(global_min,nums[left])

                left=mid+1
            
            else:
                global_min=min(global_min,nums[mid])

                right=mid-1
        
        return global_min


