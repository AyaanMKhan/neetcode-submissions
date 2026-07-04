from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))
        
        dist = 0

        # Multi-source BFS
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == -1 or
                        (nr, nc) in visit
                    ):
                        continue
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1
                