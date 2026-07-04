class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for src, dest, weight in edges:
            adjList[src].append([dest, weight])
            adjList[dest].append([src, weight])
        

        visit = set()
        minHeap = []
        mst = []
        visit.add(0)
        for nei, cost in adjList[0]:
            heapq.heappush(minHeap, [cost, 0, nei])
        
        while minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)

            if n2 in visit:
                continue
            
            visit.add(n2)
            mst.append(weight)

            for nei, cost in adjList[n2]:
                if nei not in visit:
                    heapq.heappush(minHeap, [cost, n2, nei])
        
        if len(visit) == n:
            return sum(mst)
        else:
            return -1
