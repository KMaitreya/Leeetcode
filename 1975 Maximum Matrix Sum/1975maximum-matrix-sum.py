class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        n=len(matrix)
        cnt=0
        s=0
        m=abs(matrix[0][0])

        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    matrix[i][j]=abs(matrix[i][j])
                    cnt+=1
                s+=matrix[i][j]
                m=min(matrix[i][j], m)

        if cnt%2==0:
            return s
        return s-2*m