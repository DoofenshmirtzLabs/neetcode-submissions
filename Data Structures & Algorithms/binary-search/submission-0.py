class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            current_mid=nums[mid]
            print(current_mid)
            if current_mid==target:
                return mid
            elif current_mid>target:
                end=mid-1
            else:
                start=mid+1
        return -1