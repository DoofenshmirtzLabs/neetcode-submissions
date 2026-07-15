import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        for index,l in enumerate(points):
            x,y=l[0],l[1]
            distance=pow((y**2+x**2),0.5)
            heapq.heappush(heap,(distance,[x,y]))
        res=[]
        for i in range(k):
            _,point=heapq.heappop(heap)
            res.append(point)
        
        return res

        


            
