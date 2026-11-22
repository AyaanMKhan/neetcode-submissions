class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -(stones[i])
        
        heapq.heapify(stones)


        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, x-y)
        

        return abs(stones[0]) if stones else 0
 
        
        