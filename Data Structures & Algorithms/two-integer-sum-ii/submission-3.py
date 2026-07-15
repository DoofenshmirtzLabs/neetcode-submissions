class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #binary search solution nlogn

        for index,num in enumerate(numbers):
            key=target-num

            left,right=index+1,len(numbers)-1
            while left<=right:

                mid=left+(right-left)//2

                if numbers[mid]==key:
                    return [index+1,mid+1]
                
                elif numbers[mid]<key:
                    left=mid+1
                else:
                    right=mid-1
        
        return []
            