from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set()

        def addGate(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visit or grid[r][c] == -1:
                return
            q.append([r, c])
            visit.add((r, c))
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addGate(r+1, c)
                addGate(r-1, c)
                addGate(r, c+1)
                addGate(r, c-1)
            dist+=1
            