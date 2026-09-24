class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        islands = 0

        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j, m, n)
        
        return islands
    

    def dfs(self, grid, row, col, m, n):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                self.dfs(grid, row+1, col, m, n)
                self.dfs(grid, row-1, col, m, n)
                self.dfs(grid, row, col+1, m, n)
                self.dfs(grid, row, col-1, m, n)