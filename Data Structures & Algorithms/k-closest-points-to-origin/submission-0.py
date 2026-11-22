class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        

        heap = []

        for x, y in points:
            dist = (x**2+y**2)**(1/2)
            heapq.heappush(heap, (dist, x, y))
        
        res = []
        while k != 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        return res