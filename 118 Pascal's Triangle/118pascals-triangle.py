class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        op=[[1]]

        for i in range(1, numRows):
            temp=[1]
            for j in range(i-1):
                temp.append(op[i-1][j]+op[i-1][j+1])
            temp.append(1)
            op.append(temp)

        return op