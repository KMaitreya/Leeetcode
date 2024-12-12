class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles=[-x for x in piles]
        heapq.heapify(piles)

        for _ in range(k):
            temp=abs(heapq.heappop(piles))
            temp-=math.floor(temp/2)
            heapq.heappush(piles, -temp)

        return -sum(piles)
