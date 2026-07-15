class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        while len(stones)>1:
            newarr=[]
            heap=stones
            heapq.heapify(heap)
            while len(heap)>2:
                temp=heapq.heappop(heap)
                newarr.append(temp)
            
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            if x==y:
                stones=newarr
                continue
            else:
                newarr.append(abs(x-y))
            stones=newarr        
        return stones[0] if stones else 0