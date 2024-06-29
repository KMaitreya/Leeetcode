class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Build the graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Perform topological sort using Kahn's algorithm
        topo_order = []
        queue = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Initialize a list to store ancestors for each node
        ancestors = [set() for _ in range(n)]
        
        # Propagate ancestors in topological order
        for node in topo_order:
            for neighbor in graph[node]:
                # Add current node and all its ancestors to the neighbor
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
        
        # Convert sets to sorted lists
        result = [sorted(list(anc)) for anc in ancestors]
        
        return result