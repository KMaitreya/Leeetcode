class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Update the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 3: Run the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Count the number of reachable cities for each city
        min_count = float('inf')
        result_city = -1
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            # Step 5: Find the city with the smallest number of reachable cities
            if count <= min_count:
                if count < min_count or i > result_city:
                    result_city = i
                    min_count = count
        
        return result_city