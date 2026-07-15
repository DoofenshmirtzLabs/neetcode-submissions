class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        visited=[[-1]*cols for _ in range(rows)]
        max_area=0

        def dfs(row,col):
            r=row
            c=col
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or visited[row][col]==1 :
                return 0
            visited[row][col]=1
            return (1+dfs(r + 1, c)+
            dfs(r - 1, c)+
            dfs(r , c-1)+
            dfs(r , c+1))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and visited[row][col]==-1:
                  
                    island_area=dfs(row,col)
                    max_area=max(max_area,island_area)
        return max_area
