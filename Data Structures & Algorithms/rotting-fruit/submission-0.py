class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        num_fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append([i, j])
        
        if num_fresh == 0:
            return 0
        

        minutes = -1

        adjList = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in adjList:
                    nr, nc = dr+row, dc+col
                    if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != FRESH:
                        continue
                    else:
                        grid[nr][nc] = ROTTEN
                        q.append([nr, nc])
                        num_fresh -= 1

            minutes += 1
        

        return minutes if num_fresh == 0 else -1