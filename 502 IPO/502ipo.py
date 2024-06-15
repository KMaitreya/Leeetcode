class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = sorted(zip(capital, profits))
        max_heap = []
        current = 0
        n = len(profits)
        
        for _ in range(k):
            # Add all projects that we can afford to the heap
            while current < n and projects[current][0] <= w:
                heappush(max_heap, -projects[current][1])
                current += 1
            
            # If we have no projects in the heap, we can't do anything more
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            w += -heappop(max_heap)
        
        return w