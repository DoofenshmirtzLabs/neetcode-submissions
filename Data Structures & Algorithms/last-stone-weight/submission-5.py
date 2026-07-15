import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap=[stone*-1 for stone in stones]
        heapq.heapify(heap)
        #print(heap)
        while len(heap)>1:
            curr1=-heapq.heappop(heap)
            curr2=-heapq.heappop(heap)
           # print(curr1,curr2)
            if curr1==curr2:
                continue
            if curr1<curr2:
                temp=curr2-curr1
                heapq.heappush(heap,-temp)
            else:
                temp=curr1-curr2
                heapq.heappush(heap,-temp)
           # print(heap)
        return -heap[0] if len(heap)==1 else 0
