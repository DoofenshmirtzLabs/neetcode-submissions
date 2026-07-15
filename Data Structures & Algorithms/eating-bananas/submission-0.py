class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end=1,max(piles)
        res=end

        while start<=end:
            mid=(start+end)//2
            totaltime=0
            for p in piles:
                totaltime+=math.ceil(float(p)/mid)

            if totaltime<=h:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res

        