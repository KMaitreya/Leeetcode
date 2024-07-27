class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
         
        ALPHABET_SIZE = 26
    
        # Initialize the cost matrix with infinity
        inf = float('inf')
        cost_matrix = [[inf] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
        
        # Set the cost of transforming a character to itself to 0
        for i in range(ALPHABET_SIZE):
            cost_matrix[i][i] = 0
        
        # Fill the cost matrix with the given transformation costs
        for i in range(len(original)):
            from_char = ord(original[i]) - ord('a')
            to_char = ord(changed[i]) - ord('a')
            cost_matrix[from_char][to_char] = min(cost_matrix[from_char][to_char], cost[i])
        
        # Apply Floyd-Warshall algorithm to find the minimum cost for all pairs
        for k in range(ALPHABET_SIZE):
            for i in range(ALPHABET_SIZE):
                for j in range(ALPHABET_SIZE):
                    if cost_matrix[i][k] < inf and cost_matrix[k][j] < inf:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # Calculate the total cost to transform source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            s_index = ord(s_char) - ord('a')
            t_index = ord(t_char) - ord('a')
            
            if cost_matrix[s_index][t_index] == inf:
                return -1
            
            total_cost += cost_matrix[s_index][t_index]
        
        return total_cost