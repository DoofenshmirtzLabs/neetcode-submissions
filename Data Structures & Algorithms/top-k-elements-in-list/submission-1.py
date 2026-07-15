class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[]for i in range(len(nums)+1)]
        count={}

        for num in nums:
            count[num]=1+count.get(num,0)
        
        for num,cnt in count.items():
            freq[cnt].append(num)

        result=[]
        
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                if len(result)<k:
                    result.append(num)
        return result


        