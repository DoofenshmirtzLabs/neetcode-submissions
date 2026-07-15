import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        def slope(point):
            distance=float(math.sqrt(point[0]**2+point[1]**2))
            return distance

        for point in points:
            distance=slope(point)
            heapq.heappush(heap,[-distance,point])
            while len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
            current_distance,current_point=heapq.heappop(heap)
            res.append(current_point)
        return res