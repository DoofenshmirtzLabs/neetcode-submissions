from collections import defaultdict

class Solution:
    def twosum(self, nums, target) -> list:
        left, right = 0, len(nums) - 1
        res = []  # We will collect ALL valid pairs here
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                res.append([nums[left], nums[right]])
                left += 1   # Move pointers to keep looking for more pairs
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return res  # Return the full list of pairs

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        # A set is much easier for tracking unique triplets
        seen_triplets = set()
        
        for index, num in enumerate(nums):
            # Pass the rest of the array to get all matching pairs
            outputs = self.twosum(nums[index+1:], -num)
            
            for output in outputs:
                # Create the triplet
                triplet = (num, output[0], output[1])
                
                # If we haven't seen this specific triplet before, save it!
                if triplet not in seen_triplets:
                    seen_triplets.add(triplet)
                    res.append([num, output[0], output[1]])
        
        return res