from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        if len(nums)==1 or len(nums)==0:
            return nums

        heap=[]
        table=defaultdict(int)

        for num in nums:
            table[num]+=1
        
        for key,value in table.items():
            heapq.heappush(heap,(-value,key))
        res=[]
        for _ in range(k):
            _,temp=heapq.heappop(heap)
            res.append(temp)
        return res