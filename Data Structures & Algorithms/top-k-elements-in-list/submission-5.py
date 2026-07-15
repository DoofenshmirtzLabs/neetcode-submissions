import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter=defaultdict(int)
        arr=[]

        for num in nums:
            counter[num]+=1
        count=counter.items()

        for key,value in count:
            heapq.heappush(arr, (-value, key))
        result=[]
        for i in range(k):
            result.append(heapq.heappop(arr)[1])
        
        return result