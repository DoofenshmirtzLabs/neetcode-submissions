class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product=[1] * len(nums)
        right_product=[1] * len(nums)

        for index,num in enumerate(nums):
            if index==len(nums)-1:
                break
            left_product[index+1]=left_product[index]*num
        
        for index,num in enumerate(nums[::-1]):
            if index==len(nums)-1:
                break
            right_product[index+1]=right_product[index]*num
        
        return [l * r for l, r in zip(left_product, right_product[::-1])]