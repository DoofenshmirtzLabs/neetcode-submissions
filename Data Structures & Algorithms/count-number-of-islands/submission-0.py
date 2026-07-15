class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows=len(grid)
        cols=len(grid[0])
        visited=[[-1]*cols for _ in range(rows)]
        def dfs(row,col,visited):
            
            if row>=rows or row<0 or col>=cols or col<0 or visited[row][col]==1 or grid[row][col]=='0':
                return 
         
            visited[row][col]=1
            dfs(row+1,col,visited)
            dfs(row-1,col,visited)
            dfs(row,col+1,visited)
            dfs(row,col-1,visited)
            return 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and visited[row][col]==-1:
                    dfs(row,col,visited)
                    count+=1
        return count