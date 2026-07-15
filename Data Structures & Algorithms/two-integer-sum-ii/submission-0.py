class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start<end:
            left=numbers[start]
            right=numbers[end]
            if left+right>target:
                end-=1
            elif left+right<target:
                start+=1
            else:
                return [start+1,end+1]
        