class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions: List[Tuple[int, int]]) -> List[int]:
            # Build the graph and in-degree array
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            # Perform topological sort using Kahn's algorithm
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            # Check if topological sort is possible (i.e., all nodes are processed)
            if len(topo_order) == k:
                return topo_order
            return []
        
        # Get the row and column orders using topological sort
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        # If either sort returns an empty list, return an empty matrix
        if not row_order or not col_order:
            return []
        
        # Build the position mappings
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        # Create the result matrix and place the numbers
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix