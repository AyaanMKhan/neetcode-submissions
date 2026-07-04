class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}

        for i in range(n):
            adjList[i] = []

        for src, dest, weight in edges:
            adjList[src].append([dest, weight])
            adjList[dest].append([src, weight])
        
        visit = set()
        visit.add(0)
        minHeap = []

        for nei, weight in adjList[0]:
            heapq.heappush(minHeap, [weight, 0, nei])
        
        mst = []

        while minHeap:
            weight, src, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            mst.append(weight)
            visit.add(node)

            for nei, weight in adjList[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [weight, node, nei])
        
        if len(visit) == n:
            return sum(mst)
        else:
            return -1