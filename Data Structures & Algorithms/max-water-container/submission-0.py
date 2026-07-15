class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return None
        start=0
        end=len(heights)-1

        max_area=0
        max_start,max_end=0,0
        while start<=end:
            water_lvl=min(heights[start],heights[end])
            area=water_lvl*(end-start)
            max_area=max(max_area,area)
            max_start=start
            max_end=end
            if heights[end]>heights[start]:
                start+=1
            else:
                end-=1
        return max_area   

        