class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()

        # Preprocess items to get maximum beauty up to each price.
        max_beauty_up_to_price = []
        premax = []
        mcnt = 0
        
        for price, beauty in items:
            mcnt = max(mcnt, beauty)
            max_beauty_up_to_price.append((price, mcnt))

        # Result array to store the maximum beauty for each query.
        result = []

        # Process each query.
        for query in queries:
            # Find the rightmost item whose price is <= query using binary search.
            index = bisect_right(max_beauty_up_to_price, (query, float('inf'))) - 1
            
            if index >= 0:
                result.append(max_beauty_up_to_price[index][1])
            else:
                result.append(0)  # No item found within the price range.
        
        return result
