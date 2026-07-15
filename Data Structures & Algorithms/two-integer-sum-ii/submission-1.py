class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #didnt use hashtable because question specifically says o(1) space
        left,right=0,len(numbers)-1

        while left<right:

            if numbers[left]+numbers[right]==target:
                return [left+1,right+1] #1-indexed 
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        

        