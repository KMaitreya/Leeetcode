class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
    
        # Initialize degree count for each city
        degree = defaultdict(int)
        
        # Calculate the degree of each city
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Sort cities by their degree in descending order
        sorted_cities = sorted(degree.keys(), key=lambda x: degree[x], reverse=True)
        
        # Create a mapping of city to its assigned value
        city_to_value = {}
        value = n
        
        for city in sorted_cities:
            city_to_value[city] = value
            value -= 1
        
        # Calculate the total importance of all roads
        total_importance = 0
        for a, b in roads:
            total_importance += city_to_value[a] + city_to_value[b]
        
        return total_importance