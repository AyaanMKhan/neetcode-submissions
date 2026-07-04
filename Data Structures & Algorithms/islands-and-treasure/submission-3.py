from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        def addGate(r, c):
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))
        
        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addGate(r + 1, c)
                addGate(r - 1, c)
                addGate(r, c + 1)
                addGate(r, c - 1)
            dist += 1

