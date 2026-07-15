class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}  # Create a dictionary to store numbers and their indices
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index
        return [] 
        