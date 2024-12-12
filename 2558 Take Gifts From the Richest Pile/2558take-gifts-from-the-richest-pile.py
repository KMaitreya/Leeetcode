class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts=[-x for x in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            heapq.heappush(gifts, -math.floor(abs(heapq.heappop(gifts))**0.5))

        return -sum(gifts)