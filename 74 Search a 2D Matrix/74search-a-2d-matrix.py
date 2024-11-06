class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        lst=[]

        for row in matrix:
            for val in row:
                lst.append(val)

        l, r=0, len(lst)-1

        while l<=r:
            m=(l+r)//2
            if target<lst[m]:
                r=m-1
            elif target>lst[m]:
                l=m+1
            else:
                return True
        return False