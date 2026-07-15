class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #i cant sort to use counter ,i cant use hash_maps,o(1) xor?

        res=0

        for num in nums:
            res^=num
        
        print(res)
        return res