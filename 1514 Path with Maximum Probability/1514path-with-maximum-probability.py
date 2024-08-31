class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))

        # Distances array
        dist = [0.0] * n
        dist[start_node] = 1.0

        # Queue for BFS
        queue = deque([start_node])

        while queue:
            curr = queue.popleft()

            for node, prob in adj[curr]:
                new_prob = dist[curr] * prob

                if new_prob > dist[node]:
                    dist[node] = new_prob
                    queue.append(node)

        return dist[end_node]