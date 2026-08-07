class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rowSet = set()
        colSet = set()

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        

        for i in range(m):
            for j in range(n):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0