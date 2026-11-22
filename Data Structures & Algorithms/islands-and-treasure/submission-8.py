class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid or not grid[0]:
            return None 
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visit = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))

        def addGate(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                addGate(r+1, c)
                addGate(r-1, c)
                addGate(r, c+1)
                addGate(r, c-1)

            dist += 1