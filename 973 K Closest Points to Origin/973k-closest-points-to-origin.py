class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points=[[point[0]**2+point[1]**2, point] for point in points]

        heapq.heapify(points)

        return [heapq.heappop(points)[1] for _ in range(k)]