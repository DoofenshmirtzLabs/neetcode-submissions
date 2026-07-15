class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return nums
        count={}
        result=[]

        for num in nums:
            count[num]=count.get(num,0)+1
        
        heap=[]

        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

        