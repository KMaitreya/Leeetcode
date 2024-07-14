class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        # Initialize counters for pieces and total cost
        h_pieces = 1
        v_pieces = 1
        total_cost = 0
        
        # Initialize indices for horizontal and vertical cuts
        h_index = 0
        v_index = 0
        
        # While there are cuts to be made
        while h_index < len(horizontalCut) and v_index < len(verticalCut):
            if horizontalCut[h_index] >= verticalCut[v_index]:
                # Make a horizontal cut
                total_cost += horizontalCut[h_index] * v_pieces
                h_pieces += 1
                h_index += 1
            else:
                # Make a vertical cut
                total_cost += verticalCut[v_index] * h_pieces
                v_pieces += 1
                v_index += 1
        
        # Add remaining horizontal cuts
        while h_index < len(horizontalCut):
            total_cost += horizontalCut[h_index] * v_pieces
            h_index += 1
        
        # Add remaining vertical cuts
        while v_index < len(verticalCut):
            total_cost += verticalCut[v_index] * h_pieces
            v_index += 1
        
        return total_cost