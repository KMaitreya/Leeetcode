class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
    
        # Iterate through the matrix cells
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                # Fill the cell with the minimum of rowSum[i] and colSum[j]
                matrix[i][j] = min(rowSum[i], colSum[j])
                # Update the rowSum and colSum after filling the cell
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        
        return matrix