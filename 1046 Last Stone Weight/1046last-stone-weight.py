class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i]*=-1

        heapq.heapify(stones)
        

        while len(stones)!=1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            heapq.heappush(stones, abs(a-b)*-1)

        return stones[0]*-1