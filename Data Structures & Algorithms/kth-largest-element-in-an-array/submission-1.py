import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[-num for num in nums]
        heapq.heapify(heap)

        while k:
            curr=heapq.heappop(heap)
            k-=1
            if k==0:
                return -curr
        