class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        
        for src, dest in edges:
            adjList[src].append(dest)
        
        topSort = []
        visit = set()
        cycle = set()

        for i in range(n):
            if not self.dfs(i, adjList, visit, topSort, cycle):
                return []
        
        topSort.reverse()
        return topSort
    
    def dfs(self, src, adjList, visit, topSort, cycle):
        if src in cycle:
            return False
        
        if src in visit:
            return True
        
        cycle.add(src)
        
        

        for nei in adjList[src]:
            if not self.dfs(nei, adjList, visit, topSort, cycle):
                return False
        
        cycle.remove(src)
        visit.add(src)
        topSort.append(src)
        return True