class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        op=[1]

        if rowIndex==0:
            return op

        for i in range(1, rowIndex+1):
            temp=[1]
            for j in range(i-1):
                temp.append(op[j]+op[j+1])
            temp.append(1)
            op=temp
            if i==rowIndex:
                return op