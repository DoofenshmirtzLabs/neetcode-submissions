class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        output=[]
        dq=collections.deque()
        for end in range(len(nums)):
            while dq and nums[dq[-1]]<nums[end]:
                dq.pop()
            dq.append(end)
            if dq[0]<left:
                dq.popleft()
            if end>=k-1:
                output.append(nums[dq[0]])
                left+=1
        return output
        

            