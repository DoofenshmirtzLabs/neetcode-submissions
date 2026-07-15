class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique_solutions=set()
        for i in range(len(nums)-2):
            current_ele=nums[i]
            left=i+1
            right=len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left<right:
                current_sum=current_ele+nums[left]+nums[right]
                if current_sum==0:
                    unique_solutions.add(tuple(sorted([current_ele,nums[left],nums[right]])))
                    left+=1
                    right-=1
                elif current_sum<0:
                    left+=1
                else:
                    right-=1
            output=[]
        for sol in unique_solutions:
                output.append(sol)
        return output