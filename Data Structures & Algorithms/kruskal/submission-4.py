class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        
        return self.parent[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p1] += 1

        return True
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []

        for n1, n2, weight in edges:
            heapq.heappush(minHeap, [weight, n1, n2])
        
        mst = []
        unionFind = UnionFind(n)

        while minHeap and len(mst) < n-1:
            weight, n1, n2 = heapq.heappop(minHeap)

            if not unionFind.union(n1, n2):
                continue
            
            mst.append(weight)
        
        return sum(mst) if len(mst) == n-1 else -1