class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map={}
        max_length=0

        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1
        
        for num in nums:
            if num-1 in nums:
                continue
            else:
                length=1
                temp=num
                while temp+1 in hash_map:
                    temp+=1
                    length+=1
                max_length=max(max_length,length)
        return max_length

        